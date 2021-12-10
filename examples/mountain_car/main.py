import copy
from collections import defaultdict
import argparse

import gym

from rlang import parse_file, parse
from rlang.src.grounding import State, Action

from examples.utils.rlang_policy import RLangPolicy
from examples.utils.reinforce_agent import train_reinforce
from examples.utils.control_sharing import beta_scheduler,ControlSharingPolicy, linear_scheduler

import numpy as np
from torch import nn

from pfrl.policies import SoftmaxCategoricalHead

def policy_mixing(policy_model, advice_policy):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mix-beta", type=float, default=1., help="initial mixing parameter"
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
    
    return ControlSharingPolicy(policy_model, advice_policy, scheduler)

def make_rlang_agent_model(model, rlang_policy, n_actions):
    advice_policy = RLangPolicy(rlang_policy, n_actions=n_actions)
    return advice_policy

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
    knowledge = parse_file("examples/mountain_car/policy.rlang")
    _, model = make_uninformed_agent_model(obs_size=2, action_space=3)
    rlang_advice_policy = make_rlang_agent_model(model, knowledge['gain_momentum'], n_actions=3)
    learning_policy = policy_mixing(model, rlang_advice_policy)
    train_reinforce(learning_policy, demo=True, env="MountainCar-v0")


if __name__ == '__main__':
    rlang_experiment()
