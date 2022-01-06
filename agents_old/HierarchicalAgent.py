'''
    Hierarchical RL Agents
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: March 2021
'''
import random
from lmdp.grounding.states.StateClass import State as RLangState
from copy import deepcopy


class HierarchicalAgent:
    def __init__(self, actions, options, outer_agent, inner_agent, warmup_period=0, discount_factor=0.99):
        self._actions = actions
        self._options = options
        self._outer_agent = OuterAgent(options, outer_agent)
        self._inner_agent = InnerAgent(actions, options, inner_agent)
        self._gamma = discount_factor
        self._t = 0
        self._r = 0
        self._curr_option = None
        self._warmup = warmup_period
        self._steps = 0
        self._inner = deepcopy(self._inner_agent)
        self._outer = deepcopy(self._outer_agent)

    def act(self, state):
        r = state['reward']
        s = {'observation': state['observation'], 'reward': self._r, 'done': state['done']}
        self._r += r * self._gamma ** self._t  # accumulates discounted reward
        if self._curr_option is None or not self.inner_is_executing(state):
            o = self.outer_agent_act(s)  # outer agent act
            self._curr_option = o
            self._inner_agent.execute(o)  # start option o
        self._steps += 1
        return self.inner_agent_act(state)

    def outer_agent_act(self, state):
        if self._steps >= self._warmup:
            o = self._outer_agent.act(state)
        else:
            o = self.random_policy(state)  # uniformly at random during warmup
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

    def random_policy(self, state):
        active_options = self.get_active_options(state)
        return random.choice(active_options)

    def get_active_options(self, state):
        return [o for o in self._options if o.initiation(RLangState(state['observation']))]

    def reset(self):
        self.end_of_episode()
        self._inner_agent = deepcopy(self._inner)
        self._outer_agent = deepcopy(self._outer)

    def end_of_episode(self):
        self._t = 0
        self._r = 0
        self._curr_option = None
        self._steps = 0


class SubgoalHierarchicalAgent(HierarchicalAgent):
    def inner_is_executing(self, state):
        if self._inner_agent.is_executing(state):  # not terminated
            if (
                    not self._curr_option.is_executable(
                        state['observation'])):  # initiation condition if false -> Interrupt
                s = {'observation': state['observation'], 'reward': -.01, 'done': True}
                self._inner_agent.act(s)  # extra step to update inner agent with intrinsic reward
                self._inner_agent.stop(state)
                self._curr_option = None
                return False
            return True
        elif (self._curr_option.terminated(state['observation'])):  # goal reached.
            s = {'observation': state['observation'], 'reward': 1, 'done': True}
            self._inner_agent.act(s)  # extra step to update inner agent with intrinsic reward
            self._inner_agent.stop(state)
            self._curr_option = None
            return False

    def inner_agent_act(self, state):
        s = {'observation': state['observation'], 'reward': -.01, 'done': state['done']}
        return self._inner_agent.act(s)


class OptionAgent(HierarchicalAgent):

    def __init__(self, actions, options, outer_agent, inner_agent, discount_factor=0.99):
        inner_agent_factory = lambda *args: inner_agent
        HierarchicalAgent.__init__(self, actions, options, outer_agent, inner_agent_factory,
                                   discount_factor=discount_factor)

    def inner_agent_act(self, state):
        return self._inner_agent.eval(state)


from agents import OptQLearningFactory


class IntraoptionQAgent(SubgoalHierarchicalAgent):
    def __init__(self, actions, options, inner_agent, warmup_period=0, discount_factor=0.99, alpha=0.1, epsilon=0.1,
                 anneal=True):
        outer_agent = OptQLearningFactory(options, alpha=alpha, epsilon=epsilon, gamma=discount_factor, anneal=anneal)
        SubgoalHierarchicalAgent.__init__(self, actions, options, outer_agent, inner_agent, warmup_period=warmup_period,
                                          discount_factor=discount_factor)

    def act(self, state):
        o = self.outer_agent_act(state)  # outer agent act
        if self._curr_option is None or not self.inner_is_executing(state):
            self._curr_option = o
            self._inner_agent.execute(o)  # start option o
        self._steps += 1
        return self.inner_agent_act(state)

    def outer_agent_act(self, state):
        o = self._outer_agent.act(state)
        if self._steps < self._warmup:
            o = self.random_policy(state)  # uniformly at random during warmup
        return o


class SMDPQAgent(SubgoalHierarchicalAgent):
    def __init__(self, actions, options, inner_agent, warmup_period=0, discount_factor=0.99, alpha=0.1, epsilon=0.1,
                 anneal=True):
        outer_agent = OptQLearningFactory(options, alpha=alpha, epsilon=epsilon, gamma=discount_factor, anneal=anneal)
        self._t = 0
        self._max_inner_steps = 100
        SubgoalHierarchicalAgent.__init__(self, actions, options, outer_agent, inner_agent, warmup_period=warmup_period,
                                          discount_factor=discount_factor)

    def act(self, state):
        self._t += 1
        if self._curr_option is None or not self.inner_is_executing(state):  # or self._t > self._max_inner_steps:
            o = self.outer_agent_act(state)  # outer agent act
            self._curr_option = o
            self._inner_agent.execute(o)  # start option o
            self._t = 0  # restart time counter
        if state['done']:
            return random.choice(self._actions)
        return self.inner_agent_act(state)  # rollout option

    def outer_agent_act(self, state):
        o = self._outer_agent.act(state, self._t)
        if self._steps < self._warmup:
            o = self.random_policy(state)  # uniformly at random during warmup
        return o


class InnerAgent:
    def __init__(self, actions, options, agent_factory):
        self._executing_agent = None
        self._executing_option = None
        agents = [(o._id, agent_factory(o)) for o in options]
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


class OuterAgent:
    def __init__(self, options, agent_factory):
        self._agent = agent_factory(options)

    def act(self, state, timestep=1):
        return self._agent.act(state, timestep=timestep)

    def eval(self, state):
        return self._agent.eval(state)

    def __repr__(self):
        return repr(self._agent)
