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

    
def train_baseline():
    agent_policy_model , model = make_uninformed_agent_model(action_space=4, obs_size=8)
    train_agent_ppo(agent_policy_model, env="LunarLander-v2", steps=5e5, demo=True)
    train_agent_ppo(agent_policy_model, env="LunarLander-v2", steps=5e5)
if __name__ == '__main__':
    train_baseline()
