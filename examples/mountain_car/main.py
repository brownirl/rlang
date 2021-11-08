import copy
from collections import defaultdict

import numpy as np
from gym.envs.classic_control import MountainCarEnv

from rlang import parse_file, parse
from rlang.src.grounding import State, Action

from agents.RLangQLearningAgentClass import RLangQLearningAgent

def create_mdp():
    # MDP parameters
    mdp = MountainCarEnv()
    return mdp

def run_experiment():
    mdp = create_mdp()


def rlang_experiment():
    mdp = create_mdp()
    knowledge = parse_file("examples/mountain_car/policy.rlang") 
    print(knowledge.full_predictions([0, 0]))


if __name__ == '__main__':
    rlang_experiment()
