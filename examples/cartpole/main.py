import copy
from collections import defaultdict

import numpy as np

import gym

from rlang import parse_file, parse
from rlang.src.grounding import State, Action

import numpy as np
import torch
from torch import nn

from control_sharing import ControlSharingPolicy
from run_rlang_agent import train_agent_eval_agent

from pfrl.policies import SoftmaxCategoricalHead

def create_mdp():
    # MDP parameters
    mdp = gym.make('CartPole-v0')
    return mdp

def cartpole_policy_1(state):
    LEFT = 0
    RIGHT = 1
    state = state[0]
    cart_position = state[0]
    cart_velocity = state[1]
    pole_angle = state[2]
    pole_ang_velocity = state[3]

    if pole_ang_velocity > 0:
        return {LEFT: 0., RIGHT: 1.}
    else:
        return {LEFT: 1., RIGHT: 0.}


def cartpole_policy_2(state):
    LEFT = 0
    RIGHT = 1
    cart_position = state[0]
    cart_velocity = state[1]
    pole_angle = state[2]
    pole_ang_velocity = state[3]

    if pole_ang_velocity > 0:
        if pole_angle >= 0:
            return RIGHT
        elif cart_velocity > 0:
            return LEFT
        else:
            return RIGHT
    else:
        if pole_angle <= 0:
            return LEFT
        elif cart_velocity > 0:
            return LEFT
        else:
            return RIGHT

def cartpole_policy_pirl(state):
    LEFT = 0
    RIGHT = 1
    cart_position = state[0]
    cart_velocity = state[1]
    pole_angle = state[2]
    pole_ang_velocity = state[3]


    if (cart_position + cart_velocity - pole_ang_velocity > 0):
        return LEFT
    return RIGHT



class beta_scheduler:
    def __init__(self, init_beta=1., annealing_factor=0.75):
        self.init_beta = 1
        self.current_beta = init_beta
        self.annealing_factor=annealing_factor
        self._t = 0
        self._freq = 200

    def __call__(self):
        if self._t % self._freq == 0:   
            self.current_beta *= self.annealing_factor
        self._t += 1
        return self.current_beta
    
    def reset(self):
        self.current_beta = self.init_beta
        self._t = 0


class linear_scheduler:
    def __init__(self, n_steps=1e5, init=1., end=0.):
        self._init = init
        self._end = end
        self._steps = n_steps
        self._t = 0

    def __call__(self):
        beta = self._init - self._t * (self._init-self._end)/self._steps
        self._t += 0
        return beta

    def reset(self):
        self._t = 0

class RLangPolicy(nn.Module):
    def __init__(self, rlang_policy, epsilon=1e-8, n_actions=2):
        self.rlang_policy = rlang_policy
        self.eps = epsilon
        self.n_actions = n_actions
        super().__init__()


    def forward(self, state):
        actions_prob = torch.zeros(self.n_actions)
        actions_mask = torch.zeros(self.n_actions)
        for action, prob in self.rlang_policy(state).items():
            actions_prob[action] = prob
            actions_mask[action] = 1
        if len(actions_prob) < self.n_actions: # redistribute the remaining prob uniformly
            remaining_prob = (1. - actions_prob.sum()) / (len(actions_prob)-self.n_actions)
            actions_prob = torch.Tensor(actions_prob)
            actions_prob -= self.eps * (len(actions_prob)-self.n_actions) if remaining_prob == 0 else actions_prob
            remaining_prob = self.eps if remaining_prob == 0 else remaining_prob
            actions_prob += (1-actions_mask) * remaining_prob
        else:
            if (actions_prob == 0).any():
                actions_prob += self.eps
        return torch.log(actions_prob).unsqueeze(0)

def make_rlang_agent_model(model, rlang_policy, n_actions, annealing_factor=0.99, beta=0.75):
    advice_policy = RLangPolicy(rlang_policy, n_actions=n_actions)
    # return ControlSharingPolicy(model, advice_policy, beta_scheduler(annealing_factor=annealing_factor))
    return ControlSharingPolicy(model, advice_policy, lambda: beta)     

def make_uninformed_agent_model(obs_size=4, action_space=2, hidden_size=200):
    model = nn.Sequential(
        nn.Linear(obs_size, hidden_size),
        nn.LeakyReLU(0.2),
        nn.Linear(hidden_size, hidden_size),
        nn.LeakyReLU(0.2),
        nn.Linear(hidden_size, action_space),
    )

    agent_model = nn.Sequential(
        model, 
        SoftmaxCategoricalHead()
    )
    return agent_model, model

def rlang_experiment():
    knowledge = parse_file("examples/cartpole/policy.rlang") 
    beta = 0.5
    for seed in (0, 11, 13, 2000, 10000):
        _, model = make_uninformed_agent_model()
        rlang_policy_model = make_rlang_agent_model(model, cartpole_policy_1, n_actions=2, beta=beta)
        train_agent_eval_agent(rlang_policy_model, beta=beta, name="rlang-informed-" + str(beta) + '-seed-' + str(seed), seed=seed) # RLang-informed agent
        agent_policy_model, model = make_uninformed_agent_model()
        train_agent_eval_agent(agent_policy_model, name=f"uninformed-{seed}", seed=seed, beta=0) # Uninformed agent

if __name__ == '__main__':
    rlang_experiment()
