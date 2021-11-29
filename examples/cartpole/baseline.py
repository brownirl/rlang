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
from run_rlang_agent import train_reinforce

from pfrl.policies import SoftmaxCategoricalHead

import argparse


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
    agent_policy_model, model = make_uninformed_agent_model()
    train_reinforce(agent_policy_model, beta=0.75, output_dir='.') # Uninformed agent

if __name__ == '__main__':
    rlang_experiment()