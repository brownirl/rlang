from lmdp.agents.ReinforceMLPAgentClass import ReinforceMLPAgent
from lmdp.agents.Agent import AgentFactory
from all.presets.classic_control.models import fc_relu_q
class ReinforceFactory(AgentFactory):
    def __init__(self, actions, state_dim=1, name="", gamma=0.95, alpha=0.01, 
                                N=5, hidden_size=16, n_hidden_layers=1):
        self._agent = ReinforceAgent(actions, state_dim=1, name="", gamma=0.95, alpha=0.01, 
                                N=5, hidden_size=16, n_hidden_layers=1)
    
    
class ReinforceAgent(ReinforceMLPAgent):
    
    def act(self, state):
        action = super().act(state['observation'], state['reward'])
        return action

    def eval(self, state):
        return super().act(state['observation'], state['reward'])

    def stop(self, state):
        self.end_of_episode()

#=================================================================
from simple_rl.agents.QLearningAgentClass import QLearningAgent
class QLearningFactory(AgentFactory):
    def __init__(self, actions, name="qlearning", alpha=0.1, gamma=0.99,
                 epsilon=0.1, explore="uniform", anneal=False,
                 custom_q_init=None, default_q=0):
        self._agent = QLearning(actions, name="qlearning", alpha=0.1, gamma=0.99,
                 epsilon=0.1, explore="uniform", anneal=False,
                 custom_q_init=None, default_q=0)

class QLearning(QLearningAgent):
    def act(self, state):
        action = super().act(state['observation'], state['reward'])
        return action

    def eval(self, state):
        return super().act(state['observation'], state['reward'])

    def stop(self, state):
        self.end_of_episode()


#=====================================================================
from lmdp.agents.Agent import Agent
from all.presets.classic_control import vqn
from all.core.state import State
from collections import namedtuple
from copy import deepcopy
import torch
action_space = namedtuple('action_space', ['n', 'actions'])
state_space = namedtuple('state_space', ['shape'])
environment = namedtuple('environment', ['action_space', 'state_space'])

class QN(Agent):
    def __init__(self, actions, state_s, gamma=0.99, alpha=0.1, epsilon=0.1):
        envs = [environment(action_space(len(actions), actions), state_space(state_s))]
        self._vqn = vqn(discount_factor=gamma, lr=alpha, epsilon=epsilon, n_envs=1)[0](envs)
        self._actions = dict(enumerate(actions))

    def act(self, state):
        state = _all_state_wrapper(state)
        action = self._vqn.act(state).item()
        return self._actions[action]
    
    def eval(self, state):
        state = _all_state_wrapper(state)
        action = self._vqn.eval(state).item()
        return self._actions[action]
    
    def stop(self, state):
        pass
    
def _all_state_wrapper(state):
    state = deepcopy(state)
    state['observation'] = torch.from_numpy(state['observation'].features()).float()
    # return State.array([State(state)]) # return all.State object
    return State(state)

class QNFactory(AgentFactory):
    def __init__(self, actions, state_space, gamma=0.99, alpha=0.1, epsilon=0.1):
        AgentFactory.__init__(self, QN(actions, state_space, gamma, alpha, epsilon))


#===================================================================================================
from all.presets.classic_control import dqn
from lmdp.agents.option_dqn import dqn as odqn
class DQN(Agent):
    def __init__(self, actions, state_s, gamma=0.99, 
                alpha=0.1, epsilon=0.1, replay_start_size=1000, 
                replay_buffer_size=2000, final_exploration_frame=5000, 
                target_update_frequency=10, model=fc_relu_q):
        envs = [environment(action_space(len(actions), actions), state_space(state_s))]
        self._dqn = dqn(discount_factor=gamma, 
                        lr=alpha, 
                        replay_start_size=replay_start_size, 
                        replay_buffer_size=replay_buffer_size, 
                        final_exploration_frame=final_exploration_frame, 
                        model_constructor=model)(envs[0])
        self._actions = dict(enumerate(actions))

    def act(self, state):
        state = _all_state_wrapper(state)
        action = self._dqn.act(state)
        return self._actions[action]
    
    def eval(self, state):
        state = _all_state_wrapper(state)
        action = self._dqn.eval(state)
        return self._actions[action]
    
    def stop(self, state):
        pass

class OptDQN(DQN):
    def __init__(self, actions, state_s, gamma=0.99, alpha=0.1, 
                epsilon=0.1, replay_start_size=7000, 
                final_exploration_frame=10000, replay_buffer_size=2000,  
                target_update_frequency=5, model=fc_relu_q):
        envs = [environment(action_space(len(actions), actions), state_space(state_s))]
        self._dqn = odqn(discount_factor=gamma, 
                        lr=alpha, 
                        replay_start_size=replay_start_size, 
                        replay_buffer_size=replay_buffer_size, 
                        final_exploration_frame=final_exploration_frame, 
                        model_constructor=model, 
                        target_update_frequency=target_update_frequency)(envs[0])
        self._actions = dict(enumerate(actions))

class OptDQNFactory(AgentFactory):
    def __init__(self, actions, state_space, gamma=0.99, alpha=0.1, epsilon=0.1, model=fc_relu_q):
        AgentFactory.__init__(self, OptDQN(actions, state_space, gamma, alpha, epsilon, model=model))

class DQNFactory(AgentFactory):
    def __init__(self, actions, state_space, gamma=0.99, alpha=0.1, epsilon=0.1, model=fc_relu_q):
        AgentFactory.__init__(self, DQN(actions, state_space, gamma, alpha, epsilon, model=model))

from lmdp.grounding.states.StateClass import BatchedState as RLangState

import torch.nn as nn
import numpy as np
class OptionInitMask(nn.Module):
    def __init__(self, options):
        super(OptionInitMask, self).__init__()
        self._options = options

    def forward(self, states):
        mask = torch.from_numpy(np.array([o.initiation(RLangState(states)) for o in self._options]))
        return mask.transpose(1,0)


class masked_q(nn.Module):
    def __init__(self, p_model, options):
        super(masked_q, self).__init__()
        self._option_mask = OptionInitMask(options).requires_grad_(False)
        self._policy = p_model

    def forward(self, states):
        mask = self._option_mask(states)
        return mask * self._policy(states)

def masked_fc_relu_q(options):
    def _q(env):
        return masked_q(fc_relu_q(env), options)
    return _q

