import copy
from collections import defaultdict

import numpy as np

import gym

from rlang import parse_file, parse
from rlang.src.grounding import State, Action

import numpy as np
import torch
from torch import nn

from examples.control_sharing import ControlSharingPolicy
from train_agent import train_agent_ppo

from pfrl.policies import SoftmaxCategoricalHead

import random

from product_policy import ProductPolicy

def no_op_policy(state):
    DO_NOTHING = 0
    LEFT = 1
    CENTER = 2
    RIGHT = 3
    state = state[0]
    position = state[0:2]
    velocity = state[2:4]
    angle = state[4]
    angle_velocity = state[5]
    left_leg_touch = state[6]
    right_leg_torch = state[7]
    goal = np.zeros((2,))
    
    return {DO_NOTHING: 1., LEFT: 0., CENTER: 0., RIGHT: 0.}



def move_right(state):
    DO_NOTHING = 0
    LEFT = 1
    CENTER = 2
    RIGHT = 3

    position = state[0:2]
    velocity = state[2:4]
    angle = state[4]
    angle_velocity = state[5]
    leg_leg_touch = state[6]
    right_leg_torch = state[7]

    action_dist = {DO_NOTHING: 0., LEFT: 0., CENTER: 0., RIGHT: 0.}

    if velocity[0] > 0:
        action_dist[DO_NOTHING] = 0.5
        action_dist[CENTER] = 0.5
    elif angle > 0.1:
        action_dist[CENTER] = 1.
    elif angle_velocity > 0:
        action_dist[DO_NOTHING] = 0.5
        action_dist[LEFT] = 0.5

    return action_dist


def move_left(state):
    DO_NOTHING = 0
    LEFT = 1
    CENTER = 2
    RIGHT = 3

    position = state[0:2]
    velocity = state[2:4]
    angle = state[4]
    angle_velocity = state[5]
    leg_leg_touch = state[6]
    right_leg_torch = state[7]

    action_dist = {DO_NOTHING: 0., LEFT: 0., CENTER: 0., RIGHT: 0.}

    if velocity[0] < 0:
        action_dist[DO_NOTHING] = 0.5
        action_dist[CENTER] = 0.5
    elif angle < -0.1:
        action_dist[CENTER] = 1.
    elif angle_velocity < 0:
        action_dist[DO_NOTHING] = 0.5
        action_dist[RIGHT] = 0.5

    return action_dist

def control_velocity(state):
    velocity = state[2:4]
    action_dist = {DO_NOTHING: 0., LEFT: 0., CENTER: 0., RIGHT: 0.}
    if velocity[0] < -0.05:
        return move_right(state)
    elif velocity[0] > 0.05:
        return move_left(state)
    else:
        action_dist[DO_NOTHING] = 1.
    return action_dist

def fall_in_place(state):
    DO_NOTHING = 0
    LEFT = 1
    CENTER = 2
    RIGHT = 3
    
    position = state[0:2]
    velocity = state[2:4]
    angle = state[4]
    angle_velocity = state[5]
    leg_leg_touch = state[6]
    right_leg_torch = state[7]
    goal = np.zeros((2,))
    

    action_dist = {DO_NOTHING: 0., LEFT: 0., CENTER: 0., RIGHT: 0.}
    
    if angle.abs() < 0.005:
            action_dist[CENTER] = 0.5
            action_dist[DO_NOTHING] = 0.5
            return action_dist
    # correct angle.
    elif angle > 0:
        if angle_velocity >= 0:
            action_dist[RIGHT] = 1.
        else:
            action_dist[DO_NOTHING] = 1.
    elif angle < 0:
        if angle_velocity <= 0:
            action_dist[LEFT] = 1.
        else:
            action_dist[DO_NOTHING] = 1.

    elif position[0] < -0.05:
        return move_right(state)
    elif position[0] > 0.05:
        return move_left(state)
    elif velocity[0].abs() > 0.05:
        return control_velocity(state)
    else:
        action_dist[DO_NOTHING] = 1.
    
    return action_dist
            
class beta_scheduler:
    def __init__(self, init_beta=0.99, annealing_factor=0.75):
        self.init_beta = 1
        self.current_beta = init_beta
        self.annealing_factor=annealing_factor
        self._t = 0
        self._freq = 2

    def __call__(self):
        if self._t % self._freq == 0:   
            self.current_beta *= self.annealing_factor
        self._t += 1
        return self.current_beta
    
    def reset(self):
        self.current_beta = self.init_beta
        self._t = 0


class RLangPolicy(nn.Module):
    def __init__(self, rlang_policy, epsilon=1e-8, n_actions=2):
        self.rlang_policy = rlang_policy
        self.eps = epsilon
        self.n_actions = n_actions
        super().__init__()


    def _dict_to_tensor(self, state):
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

    def forward(self, state):
        batch = state.size()[0]
        if batch == 1:
            return self._dict_to_tensor(state[0])
        else:
            acts = [self._dict_to_tensor(state[i]) for i in range(batch)]
            return torch.cat(acts, dim=0)
                

def make_rlang_agent_model(model, rlang_policy, n_actions, annealing_factor=0.9995, beta=1.):
    advice_policy = RLangPolicy(rlang_policy, n_actions=n_actions)
    return ControlSharingPolicy(model, advice_policy, beta_scheduler(init_beta=beta, annealing_factor=annealing_factor))
    # return ControlSharingPolicy(model, advice_policy, lambda: beta)

def make_uninformed_agent_model(obs_size=4, action_space=2, hidden_size=64):
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
    env = "LunarLander-v2"
    _, model = make_uninformed_agent_model(action_space=4, obs_size=8)
    rlang_policy_model = make_rlang_agent_model(model, fall_in_place, n_actions=4, beta=0.7, annealing_factor=0.98)
    train_agent_ppo(rlang_policy_model, env="LunarLander-v2", steps=5e5, demo=True) # evaluate at 0.
    train_agent_ppo(rlang_policy_model, 
                            name="rlang-informed",
                            env=env,
                            output_dir='lunar_lander_results',
                            render=False) # RLang-informed agent

if __name__ == '__main__':
    rlang_experiment()
