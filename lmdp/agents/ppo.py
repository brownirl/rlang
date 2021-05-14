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

def ppo(
        # Common settings
        device="cpu",
        discount_factor=0.99,
        # Adam optimizer settings
        lr=1e-3,
        # Other optimization settings
        clip_grad=0.1,
        entropy_loss_scaling=0.001,
        epsilon=0.2,
        # Batch settings
        epochs=4,
        minibatches=4,
        n_envs=1,
        n_steps=8,
        # GAE settings
        lam=0.95,
        # Model construction
        feature_model_constructor=fc_relu_features,
        value_model_constructor=fc_value_head,
        policy_model_constructor=fc_policy_head,
        **kwargs
):
    """
    PPO classic control preset.

    Args:
        device (str): The device to load parameters and buffers onto for this agent.
        discount_factor (float): Discount factor for future rewards.
        lr (float): Learning rate for the Adam optimizer.
        clip_grad (float): The maximum magnitude of the gradient for any given parameter.
            Set to 0 to disable.
        entropy_loss_scaling (float): Coefficient for the entropy term in the total loss.
        epsilon (float): Value for epsilon in the clipped PPO objective function.
        epochs (int): Number of times to iterature through each batch.
        minibatches (int): The number of minibatches to split each batch into.
        n_envs (int): Number of parallel actors.
        n_steps (int): Length of each rollout.
        lam (float): The Generalized Advantage Estimate (GAE) decay parameter.
        feature_model_constructor (function): The function used to construct the neural feature model.
        value_model_constructor (function): The function used to construct the neural value model.
        policy_model_constructor (function): The function used to construct the neural policy model.
    """
    def _ppo(envs, writer=DummyWriter()):
        env = envs[0] if isinstance(envs, list) else envs
        feature_model = feature_model_constructor(env).to(device)
        value_model = value_model_constructor().to(device)
        policy_model = policy_model_constructor(env).to(device)

        feature_optimizer = Adam(feature_model.parameters(), lr=lr)
        value_optimizer = Adam(value_model.parameters(), lr=lr)
        policy_optimizer = Adam(policy_model.parameters(), lr=lr)

        features = FeatureNetwork(
            feature_model, feature_optimizer, clip_grad=clip_grad)
        v = VNetwork(
            value_model,
            value_optimizer,
            clip_grad=clip_grad,
            writer=writer
        )
        policy = SoftmaxPolicy(
            policy_model,
            policy_optimizer,
            clip_grad=clip_grad,
            writer=writer
        )
        return PPO2(
            features,
            v,
            policy,
            epsilon=epsilon,
            epochs=epochs,
            lam=lam,
            minibatches=minibatches,
            n_envs=n_envs,
            n_steps=n_steps,
            discount_factor=discount_factor,
            entropy_loss_scaling=entropy_loss_scaling,
            writer=writer
        )
    return _ppo, n_envs


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