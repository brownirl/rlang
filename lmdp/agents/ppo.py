from lmdp.agents.Agent import AgentFactory, Agent
from lmdp.grounding.states.StateClass import BatchedState as RLangState
from lmdp.grounding.states.StateClass import State as RLState
from lmdp.agents.factories import _all_state_wrapper, environment, action_space, state_space

import random
from copy import deepcopy

import numpy as np
import torch
import torch.nn as nn
from torch.optim import Adam

import all.agents
from all.agents import Agent as allAgent
from all.presets.classic_control.models import fc_policy_head, fc_value_head, fc_relu_features
from all.approximation import VNetwork, FeatureNetwork
from all.logging import DummyWriter
from all.policies import SoftmaxPolicy
from all.presets.preset import ParallelPreset


def ppo_hyperparameters(**kwargs): 
    hyperparameters = {
        "device": "cpu",
        # Common settings
        "discount_factor": 0.99,
        # Adam optimizer settings
        "lr": 1e-3,
        # Other optimization settings
        "clip_grad": 0.1,
        "entropy_loss_scaling": 0.001,
        # Batch settings
        "epochs": 4,
        "minibatches": 4,
        "n_envs": 1,
        "n_steps": 8,
        # GAE settings
        "lam": 0.95,
        # Model construction
        "feature_model_constructor": fc_relu_features,
        "value_model_constructor": fc_value_head,
        "policy_model_constructor": fc_policy_head
    }
    hyperparameters.update(kwargs)
    return hyperparameters

class PPO2(all.agents.PPO):
    def act(self, states):
        states['mask'] = torch.tensor(states['mask'])
        self._buffer.store(self._states, self._actions, torch.tensor(states.reward))
        self._train(states)
        self._states = states
        self._actions = self.policy.no_grad(self.features.no_grad(states)).sample().unsqueeze(0)
        return self._actions[0]



class PPO(allAgent):
    def __init__(self, envs, **hyperparameters):
        ## filter out extra params
        params = ppo_hyperparameters().keys() & hyperparameters.keys()
        h = {}
        for p in params:
            h[p] = hyperparameters[p] 
        
        _ppo_const, _ = ppo(**h)
        self._ppo_agent = _ppo_const(envs)
        self._params = deepcopy(hyperparameters)
        self._envs = envs
        self._ppo = deepcopy(self._ppo_agent)

    def get_params(self):
        return self._params

    def act(self, state):
        action = self._ppo_agent.act(state)
        return action

    def eval(self, state):
        action = self._ppo_agent.eval(state)
        return action

    def stop(self, state):
        pass

    def reset(self):
        self._ppo_agent = self._ppo



class SimpleRL_PPO(Agent):
    def __init__(self, actions, state_shape, **hyperparameters):
        envs = [environment(action_space(len(actions), actions), state_space(state_shape))]
        _ppo_const, _ = ppo(**hyperparameters)
        self._ppo_agent = _ppo_const(envs)
        self._params = deepcopy(hyperparameters)
        self._actions = actions
        self._state_shape = state_shape
        self._envs = envs

        self._ppo = deepcopy(self._ppo_agent)

    def get_params(self):
        return self._params

    def act(self, state):
        state = _all_state_wrapper(state)
        action = self._ppo_agent.act(state).item()
        return self._actions[action]

    def eval(self, state):
        state = _all_state_wrapper(state)
        action = self._ppo_agent.eval(state).item()
        return self._actions[action]

    def stop(self, state):
        pass

    def end_of_episode(self):
        pass

    def reset(self):
        self._ppo_agent = self._ppo