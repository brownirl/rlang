import copy, argparse
from collections import defaultdict

import numpy as np

import gym


from rlang import parse_file, parse
from rlang.src.grounding import State, Action

import numpy as np
import torch
from torch import nn

from examples.utils.control_sharing import ControlSharingPolicy, beta_scheduler
from examples.utils.rlang_policy import RLangPolicy
from examples.utils.reinforce_agent import train_reinforce

from pfrl.policies import SoftmaxCategoricalHead


def policy_mixing(policy_model, advice_policy):
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

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--rlang", type=str, default="./near_optimal_policy.rlang", help="Path to RLang policy"
    )
    args, _ = parser.parse_known_args()

    cartpole_policy = parse_file(args.rlang)['balance_pole']


    _, model = make_uninformed_agent_model()
    rlang_advice_policy = make_rlang_agent_model(model, cartpole_policy, n_actions=2)
    learning_policy = policy_mixing(model, rlang_advice_policy)

    train_reinforce(learning_policy, anneal=True, demo=True) # evaluate at zero
    train_reinforce(learning_policy, anneal=True) # RLang-informed agent

if __name__ == '__main__':
    rlang_experiment()
