import copy
from collections import defaultdict

import numpy as np

import gym

from rlang import parse_file, parse
from rlang.src.grounding import State, Action

import torch
from torch import nn

from examples.control_sharing import ControlSharingPolicy
from train_agent import train_agent_ppo

import pfrl
from pfrl.policies import SoftmaxCategoricalHead

import random, os

from supervised_init import supervised_init, evaluate_policy
from product_policy import ProductPolicy


import argparse

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
            

def gym_policy(state):

    '''
        Adapted from https://github.com/openai/gym/blob/master/gym/envs/box2d/lunar_lander.py
    '''
    DO_NOTHING = 0
    LEFT = 1
    CENTER = 2
    RIGHT = 3

    position = state[0:2]
    velocity = state[2:4]
    angle = state[4]
    angle_velocity = state[5]
    left_leg_touch = state[6]
    right_leg_torch = state[7]

    action_dist = {DO_NOTHING: 0., LEFT: 0., CENTER: 0., RIGHT: 0.}

    angle_targ = position[0] * 0.5 + velocity[0] * 1.0  # angle should point towards center
    if angle_targ > 0.4:
        angle_targ = 0.4  # more than 0.4 radians (22 degrees) is bad
    if angle_targ < -0.4:
        angle_targ = -0.4
    hover_targ = 0.55 * torch.abs(
        position[0]
    )  # target y should be proportional to horizontal offset

    angle_todo = (angle_targ - angle) * 0.5 - (angle_velocity) * 1.0
    hover_todo = (hover_targ - position[1]) * 0.5 - (velocity[1]) * 0.5

    if left_leg_touch or right_leg_torch:  # legs have contact
        angle_todo = 0
        hover_todo = (
            -(velocity[1]) * 0.5
        )  # override to reduce fall speed, that's all we need after contact

    a = DO_NOTHING
    if hover_todo > torch.abs(angle_todo) and hover_todo > 0.05:
        a = CENTER
    elif angle_todo < -0.05:
        a = RIGHT
    elif angle_todo > +0.05:
        a = LEFT

    action_dist[a] = 1.
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
    def __init__(self, rlang_policy, epsilon=1e-8, n_actions=2, obs_normalizer=None):
        self.rlang_policy = rlang_policy
        self.eps = epsilon
        self.n_actions = n_actions
        self.obs_normalizer = obs_normalizer
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
        state = self.obs_normalizer.inverse(state) if self.obs_normalizer is not None else state
        batch = state.size()[0]
        if batch == 1:
            return self._dict_to_tensor(state[0])
        else:
            acts = [self._dict_to_tensor(state[i]) for i in range(batch)]
            return torch.cat(acts, dim=0)
                
    def set_obs_normalizer(self, obs_normalizer):
        self.obs_normalizer = obs_normalizer

def make_advice_policy(rlang_policy, n_actions):
    advice_policy = RLangPolicy(rlang_policy, n_actions=n_actions)
    return advice_policy


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

    value_network = torch.nn.Sequential(
        nn.Linear(8, 64),
        nn.Tanh(),
        nn.Linear(64, 64),
        nn.Tanh(),
        nn.Linear(64, 1),
    )
    return agent_model, model, value_network


def supervised_initialization(model, learning_policy, advice_policy, value_network):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--sup-advice-policy", type=str, default='./lunar_lander_policy', help="Saved Advice Policy path"
    )
    parser.add_argument(
        "--sup-lr", type=float, default=1e-5, help="Supervised init learning rate"
    )
    parser.add_argument(
        "--sup-batchsize", type=int, default=32, help="Supervised init batchsize"
    )

    parser.add_argument(
        "--sup-n-trajectories", type=int, default=1000, help="Supervised init Number of trajectories"
    )

    parser.add_argument(
        "--sup-epochs", type=int, default=100, help="Supervised init Number of Epochs to initialize Value function"
    )

    parser.add_argument(
        "--sup-iters", type=int, default=40000, help="Supervised init Number of iterations to initialize Policy function"
    )
    
    env = "LunarLander-v2"
    args, _ = parser.parse_known_args()
    policy_path = args.sup_advice_policy

    if not os.path.exists(policy_path):
        supervised_init(model, advice_policy, gym.make(env).observation_space, batchsize=args.sup_batchsize, iters=args.sup_iters, lr=args.sup_lr)
        torch.save(learning_policy.state_dict(), policy_path)
    else:
        learning_policy.load_state_dict(torch.load(policy_path))

    evaluate_policy(learning_policy, value_network, gym.make(env), epochs=args.sup_epochs, n_trajectories=args.sup_n_trajectories)

    return learning_policy, value_network

def policy_mixing(policy_model, advice_policy, obs_normalizer=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mix-beta", type=float, default=0.8, help="initial mixing parameter"
    )
    parser.add_argument(
        "--mix-scheduler", type=str, default="exponential", help="exponential, linear or constant"
    )

    parser.add_argument(
        "--mix-decay-rate", type=float, default=0.9999, help="annealing factor"
    )

    parser.add_argument(
        "--steps", type=int, default=5e5, help="annealing factor"
    )

    args, _ = parser.parse_known_args()
    scheduler_type = args.mix_scheduler.strip().lower()
    if scheduler_type == "exponential":
        scheduler = beta_scheduler(args.mix_beta, args.mix_decay_rate)
    elif scheduler_type == "linear":
        scheduler = linear_scheduler(init=args.mix_beta, n_steps=args.steps/1000)
    elif scheduler_type == "constant":
        scheduler = lambda: args.mix_beta
    else:
        raise ValueError(f"No scheduler of type {scheduler_type}")
    advice_policy.set_obs_normalizer(obs_normalizer)
    return ControlSharingPolicy(policy_model, advice_policy, scheduler)
    
def product_policy(model, advice_policy):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--product-eps", type=float, default=0.1, help="epsilon-greedy exploration"
    )
    args, _ = parser.parse_known_args()

    return ProductPolicy(model, advice_policy)

def oracle_policy(policy, vf):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--oracle", type=str, default="", help="path to oracle policy"
    )
    args, _ = parser.parse_known_args()
    
    model = pfrl.nn.Branched(policy, vf)
    opt = torch.optim.Adam(model.parameters(), lr=3e-4, eps=1e-5)
    obs_normalizer = pfrl.nn.EmpiricalNormalization(
        8, clip_threshold=5
    )
    agent = pfrl.agents.PPO(
        model,
        opt,
        obs_normalizer=obs_normalizer,
        gpu=-1,
        update_interval=1,
        minibatch_size=1,
        epochs=1,
        clip_eps_vf=None,
        entropy_coef=0,
        standardize_advantages=True,
        gamma=0.995,
        lambd=0.97,
    )

    agent.load(args.oracle)
    

    return policy, vf, obs_normalizer


def rlang_experiment():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--experiment", type=str, default="policy-mixing", help="supervised, product policy or policy mixing"
    )
    
    parser.add_argument(
        "--policy", type=str, default="heuristic", help="heuristic or suboptimal"
    )

    args, _ = parser.parse_known_args()
    
    env = "LunarLander-v2"
    learning_policy, model, value_network = make_uninformed_agent_model(action_space=4, obs_size=8)

    policy = gym_policy if args.policy == 'heuristic' else fall_in_place

    advice_policy = make_advice_policy(policy, n_actions=4)
    obs_normalizer = pfrl.nn.EmpiricalNormalization(
        8, clip_threshold=5
    )
    obs_normalizer = None
    anneal = False
    experiment = args.experiment.lower().strip() 
    if experiment == "supervised":
        print("Supervised initialization experiment")
        learning_policy, value_network = supervised_initialization(model, learning_policy, advice_policy, value_network)
    elif experiment == "policy-mixing":
        print("Policy Mixing experiment")
        learning_policy = policy_mixing(model, advice_policy, obs_normalizer=obs_normalizer)
        anneal = True
    elif experiment == "product-policy":
        print("Product policy experiment")
        learning_policy = product_policy(learning_policy, advice_policy)
    elif experiment == "oracle":
        print("Oracle experiment")
        advice_model = model
        advice_policy, _, obs_normalizer = oracle_policy(learning_policy, value_network)
        learning_policy, learning_model, value_network = make_uninformed_agent_model(action_space=4, obs_size=8)
        model.requires_grad_ = False
        learning_policy = policy_mixing(learning_model, advice_model)
        anneal = True

    train_agent_ppo(value_network, learning_policy, anneal=anneal, obs_normalizer=obs_normalizer, env="LunarLander-v2", steps=5e5, demo=True) # evaluate at 0.
    train_agent_ppo(value_network, learning_policy, anneal=anneal, obs_normalizer=obs_normalizer, 
                            name="rlang-informed",
                            env=env,
                            output_dir='lunar_lander_results',
                            render=False) # RLang-informed agent

if __name__ == '__main__':
    rlang_experiment()
