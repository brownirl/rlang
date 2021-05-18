from all.agents import Agent
from all.presets import Preset
from all.logging import DummyWriter
from lmdp.agents.all_option_dqn import OptionDQNPreset
from lmdp.agents.dqn import DQNPreset
from lmdp.grounding.states.StateClass import State as RLangState
from functools import partial

class HierarchicalAgent(Agent):
    def __init__(self, options, outer_agent, inner_agent, discount_factor=0.99):
        self._options = options
        self._outer_agent = outer_agent
        self._inner_agent = inner_agent
        self._gamma = discount_factor
        self._t = 0
        self._r = 0
        self._curr_option = None
        self._steps = 0

    def act(self, state):
        r = state['reward']
        s = {'observation': state['observation'], 'reward': self._r, 'done': state['done']}
        self._r += r * self._gamma ** self._t # accumulates discounted reward
        if self._curr_option is None or not self.inner_is_executing(state):
            o = self.outer_agent_act(s) # outer agent act
            self._curr_option = o
            self._inner_agent.execute(o) # start option o
        self._steps += 1
        return self.inner_agent_act(state)
    
    def outer_agent_act(self, state):
        o = self._outer_agent.act(state)
        self._r, self._t = 0, 0
        return o

    def inner_agent_act(self, state):
        return self._inner_agent.act(state)

    def inner_is_executing(self, state):
        return self._inner_agent.is_executing(state)
    
    def get_options(self):
        return self._inner_agent._option_agents
    
    def get_inner_agent(self):
        return self._inner_agent
        
    def get_active_options(self, state):
        return [o for o in self._options if o.initiation(RLangState(state['observation']))]

    def reset(self):
        self._t = 0
        self._r = 0
        self._curr_option = None
        self._steps = 0
        
        
class SubgoalHierarchicalAgent(HierarchicalAgent):
    def inner_is_executing(self, state):
        if self._inner_agent.is_executing(state): # not terminated
            if (not self._curr_option.is_executable(state['observation'])): # initiation condition if false -> Interrupt
                s =  {'observation': state['observation'], 'reward': -.01, 'done': True}
                self._inner_agent.act(s) # extra step to update inner agent with intrinsic reward
                self._inner_agent.stop(state)
                self._curr_option = None
                return False
            return True
        elif (self._curr_option.terminated(state['observation'])): # goal reached.
            s =  {'observation': state['observation'], 'reward': 1, 'done': True}
            self._inner_agent.act(s) # extra step to update inner agent with intrinsic reward
            self._inner_agent.stop(state)
            self._curr_option = None
            return False
    
    def inner_agent_act(self, state):
        s =  {'observation': state['observation'], 'reward': -.01, 'done': state['done']}
        return self._inner_agent.act(s)


class InnerAgent:
    def __init__(self, actions, options, agent_factory):
        self._executing_agent = None
        self._executing_option = None
        agents = [(o._id, agent_factory()) for o in options]
        self._option_agents = dict(agents)

    def execute(self, option):
        self._executing_option = option
        self._executing_agent = self._option_agents[option._id]

    def act(self, state):
        action = self._executing_agent.act(state)
        return action
    
    def stop(self, state):
        self._executing_agent.stop(state)

    def is_executing(self, state):
        if (self._executing_agent is None or self._executing_option is None):
            self._curr_option = None
            return False
        if (self._executing_option.terminated(state['observation'])):
            return False
        return True
    
    def eval(self, state):
        return self._executing_agent.eval(state)

class HDQN(Preset):
    def __init__(self, env, device, name, options, discount_factor, outer_parameters, inner_parameters):
        self.outer_preset = OptionDQNPreset(env, device, name, options, **outer_parameters)
        self.inner_preset = DQNPreset(env, device, name, **inner_parameters)
        self._options = options
        self._discount_factor = discount_factor
    
    def agent(self, writer=DummyWriter(), train_steps=float('inf')):
        outer = self.outer_preset.agent(writer=writer, train_steps=train_steps)
        inner_factory = partial(self.inner_preset.agent, writer=DummyWriter(), train_steps=train_steps)
        inner = InnerAgent([], self._options, inner_factory)
        return SubgoalHierarchicalAgent(self._options, outer, inner, self._discount_factor)

