from all.agents import Agent, DQN
from all.core import State
from all.presets import Preset
from all.logging import DummyWriter
from all.approximation import QNetwork, FixedTarget
from all.logging import DummyWriter
from all.memory import ExperienceReplayBuffer
from all.optim import LinearScheduler
from all.policies import GreedyPolicy

from lmdp.agents.all_option_dqn import OptionGreedyPolicy, OptionInitMask, masked_q
from lmdp.grounding.states.StateClass import State as RLangState

import torch
from torch.optim import Adam

from functools import partial
from collections import namedtuple
from collections.abc import Iterable
import copy

import dill

class RLangOptionAgent(Iterable, Agent):
    '''
        Wrapper of an option as an Agent for 
        RLang-derived subpolicies.
    '''
    def __init__(self, non_learnable_option):
        self.option = non_learnable_option

    def act(self, state):
        return self.option.policy(RLangState(state['observation']))

    def eval(self, state):
        return self.option.policy(RLangState(state['observation']))
    
    def stop(self, state):
        pass
    
    def __getitem__(self, key):
        if key == 0:
            return self.option.get_id()
        elif key == 1:
            return self

    def __iter__(self):
        return iter((self.option.get_id(), self))

class InnerAgent(Agent):
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
        if (self._executing_option.terminated(RLangState(state['observation']))):
            return False
        return True
    
    def eval(self, state):
        return self._executing_agent.eval(state)

class RLangInnerAgent(InnerAgent):
    def __init__(self, options, agent_factory, writer=DummyWriter()):
        super().__init__([], options['learnable'], agent_factory)
        self._option_agents.update(dict([(o._id, RLangOptionAgent(o)) for o in options['non_learnable']]))
        self._writer = writer
        self._return = 0.

    def act(self, state):
        self._train()
        self._return += state['reward']
        return super().act(state)
    
    def execute(self, option):
        ## log return for currently executing option
        if self._executing_option is not None:
            self.__log_performance(self._return, self._executing_option)
            self._return = 0
        self._executing_option = option
        self._executing_agent = self._option_agents[option._id]

    def __log_performance(self, returns, option):
        self._writer.add_evaluation(f'returns/{repr(option)}/frame', returns, step="frame")

    def _train(self):
        for o_id, agent in self._option_agents.items():
            if self._executing_option is not None and o_id != self._executing_option._id:
                agent._train_step()
    

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
        s = State({'observation': state['observation'], 'reward': self._r, 'done': state['done']})
        self._r += r * self._gamma ** self._t # accumulates discounted reward
        if self._curr_option is None or not self.inner_is_executing(state):
            o = self.outer_agent_act(s) # outer agent act
            self._curr_option = self._options[o]
            self._inner_agent.execute(self._curr_option) # start option o
        self._steps += 1
        return self.inner_agent_act(state)
    
    def eval(self, state):
        r = state['reward']
        s = {'observation': state['observation'], 'reward': self._r, 'done': state['done']}
        self._r += r * self._gamma ** self._t # accumulates discounted reward
        if self._curr_option is None or not self.inner_is_executing(state):
            o = self.outer_agent_eval(s) # outer agent act
            self._curr_option = o
            self._inner_agent.execute(o) # start option o
        self._steps += 1
        return self._inner_agent.eval(state)

    def outer_agent_eval(self, state):
        o = self._outer_agent.eval(state)
        self._r, self._t = 0, 0
        return o

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
    def __init__(self, *args, **kwargs):
        self._step_cost = 0.
        self._goal_reward = 1.
        super().__init__(*args, **kwargs)

    def inner_is_executing(self, state):
        if self._inner_agent.is_executing(state): # not terminated
            if (not self._curr_option.is_executable(RLangState(state['observation']))): # initiation condition if false -> Interrupt
                s =  State({'observation': state['observation'], 'reward': self._step_cost, 'done': False})
                self._inner_agent.act(s) # extra step to update inner agent with intrinsic reward
                self._inner_agent.stop(state)
                self._curr_option = None
                return False
            return True
        elif (self._curr_option.terminated(RLangState(state['observation']))): # goal reached.
            s =  State({'observation': state['observation'], 'reward': self._goal_reward, 'done': True})
            self._inner_agent.act(s) # extra step to update inner agent with intrinsic reward
            # self._inner_agent.stop(state)
            self._curr_option = None
            return False
    
    def inner_agent_act(self, state):
        s = State( {'observation': state['observation'], 'reward': self._step_cost, 'done': state['done']} )
        return self._inner_agent.act(s)


class HDQNAgent(SubgoalHierarchicalAgent):
    HDQN_PARAMS = [ 'q', 
                    'policy', 
                    'replay_buffer', 
                    'discount_factor',
                    'loss',
                    'minibatch_size',
                    'replay_start_size',
                    'update_frequency']

    def __init__(self, options, discount_factor, outer_dqn_params, inner_dqn_params, writer=DummyWriter()):
        ## initialize OptionDQN 
        outer_dqn = DQN(**outer_dqn_params())
        ## DQN per option
        inner_dqn = RLangInnerAgent(options, self.__inner_factory(inner_dqn_params), writer=writer)
        super().__init__(options, outer_dqn, inner_dqn, discount_factor=discount_factor)
        self._options = options['learnable'] + options['non_learnable']


    def __inner_factory(self, inner_params):
        def _factory(option):
            params = inner_params(repr(option))
            return _DQN(**params)
        return _factory

class HDQNPreset(Preset):
    HDQN_hyperparams = ['options', 'discount_factor', 'outer_dqn_params', 'inner_dqn_params']
    def __init__(self, env, device, name, **hyperparameters):
        super().__init__(name, device, hyperparameters)
        self._env = env

    def agent(self, writer=DummyWriter(), train_steps=float('inf')):
        ## option dqn models
        self._outer_dqn_params = lambda: self.__outer_params(writer)
        ## dqn models
        self._inner_dqn_params = lambda name: self.__inner_params(writer, name)

        self._agent = HDQNAgent(
            self.hyperparameters['options'], 
            self.hyperparameters['discount_factor'],
            self._outer_dqn_params,
            self._inner_dqn_params,
            writer=writer
        )

        return self._agent


    def __get_options(self):
        return self.hyperparameters['options']['learnable'] + self.hyperparameters['options']['non_learnable']

    def __outer_params(self, writer):
        _env_c = namedtuple('env', ['action_space'])
        _action_space = namedtuple('action_space', ['n'])
        _env = _env_c(_action_space(len(self.__get_options())))

        _model = self.hyperparameters['outer_dqn_params']['model_constructor'](_env).to(self.device)
        hyperparameters = self.hyperparameters['outer_dqn_params']

        optimizer = Adam(_model.parameters(), lr=hyperparameters['lr'])
        
        q = QNetwork(
            masked_q(_model, self.__get_options()),
            optimizer,
            target=FixedTarget(hyperparameters['target_update_frequency']),
            writer=writer,
            name='q_network/outer'
        )

        policy = OptionGreedyPolicy(
            q,
            self.__get_options(),
            epsilon=LinearScheduler(
                hyperparameters['initial_exploration'],
                hyperparameters['final_exploration'],
                hyperparameters['replay_start_size'],
                hyperparameters['final_exploration_step'] - hyperparameters['replay_start_size'],
                name="outer/exploration",
                writer=writer
            )
        )

        replay_buffer = ExperienceReplayBuffer(
            hyperparameters['replay_buffer_size'],
            device=self.device
        )

        params = {
            'q': q,
            'policy': policy,
            'replay_buffer': replay_buffer,
            'discount_factor': self.hyperparameters['discount_factor'],
            'minibatch_size': hyperparameters['minibatch_size'],
            'replay_start_size': hyperparameters['replay_start_size'],
            'update_frequency': hyperparameters['update_frequency']
        }

        return params



    def __inner_params(self, writer, name):

        inner_model = self.hyperparameters['inner_dqn_params']['model_constructor'](self._env).to(self.device)

        hyperparameters = self.hyperparameters['inner_dqn_params']

        optimizer = Adam(inner_model.parameters(), lr=hyperparameters['lr'])

        q = QNetwork(
            inner_model,
            optimizer,
            target=FixedTarget(hyperparameters['target_update_frequency']),
            writer=writer,
            name=name+'/option/q'
        )

        policy = GreedyPolicy(
            q,
            self._env.action_space.n,
            epsilon=LinearScheduler(
                hyperparameters['initial_exploration'],
                hyperparameters['final_exploration'],
                hyperparameters['replay_start_size'],
                hyperparameters['final_exploration_step'] - hyperparameters['replay_start_size'],
                name=f"option/{name}/exploration",
                writer=writer
            )
        )

        replay_buffer = ExperienceReplayBuffer(
            hyperparameters['replay_buffer_size'],
            device=self.device
        )

        params = {
            'q': q,
            'policy': policy,
            'replay_buffer': replay_buffer,
            'discount_factor': self.hyperparameters['discount_factor'],
            'minibatch_size': hyperparameters['minibatch_size'],
            'replay_start_size':hyperparameters['replay_start_size'],
            'update_frequency':hyperparameters['update_frequency']
        }

        return params

    def test_agent(self):
        return HDQNTestAgent(self._agent)

    def save(self, filename):
        # del self.hyperparameters['outer_dqn_params']['model_constructor']
        # del self.hyperparameters['inner_dqn_params']['model_constructor']
        pass
        #return torch.save(self, filename, pickle_module=dill)

class HDQNTestAgent(Agent):
    def __init__(self, agent):
        self._agent = agent

    def act(self, state):
        return self._agent.eval(state)
    
    def eval(self, state):
        return self._agent.eval(state)

class _DQN(DQN):
    def _train_step(self):
        if self.__should_train():
            # sample transitions from buffer
            (states, actions, rewards, next_states, _) = self.replay_buffer.sample(self.minibatch_size)
            # forward pass
            values = self.q(states, actions)
            # compute targets
            targets = rewards + self.discount_factor * torch.max(self.q.target(next_states), dim=1)[0]
            # compute loss
            loss = self.loss(values, targets)
            # backward pass
            self.q.reinforce(loss)

    def __should_train(self):
        return (self._frames_seen > self.replay_start_size and self._frames_seen % self.update_frequency == 0)
