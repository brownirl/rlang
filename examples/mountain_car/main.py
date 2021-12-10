import copy
from collections import defaultdict

import numpy as np

import gym

from rlang import parse_file, parse
from rlang.src.grounding import State, Action

from agents.RLangQLearningAgentClass import RLangQLearningAgent

import numpy as np

from test_agent import TestAgent
from eval_agent import eval_agent

def create_mdp():
    # MDP parameters
    mdp = gym.make('MountainCar-v0')
    return mdp

def run_experiment():
    mdp = create_mdp()



def rlang_experiment():
    mdp = create_mdp()
    knowledge = parse_file("examples/mountain_car/policy.rlang")


if __name__ == '__main__':
    rlang_experiment()
