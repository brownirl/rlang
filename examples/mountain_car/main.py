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



def mountain_car_policy_1(state):
    LEFT = 0
    NO_OP = 1
    RIGHT = 2
    velocity = state[1]

    if state[0] < 0 and velocity == 0:
        return LEFT
    elif state[0] > 0 and velocity == 0:
        return RIGHT
    elif state[0] == 0 and velocity == 0:
        return LEFT
    else:
        return NO_OP

def mountain_car_policy_2(state):
    LEFT = 0
    NO_OP = 1
    RIGHT = 2
    velocity = state[1]

    if velocity < 0:
        return LEFT
    return RIGHT


def rlang_experiment():
    mdp = create_mdp()
    knowledge = parse_file("examples/mountain_car/policy.rlang") 
    agent = TestAgent(mountain_car_policy_2)

    eval_agent(agent, mdp)


if __name__ == '__main__':
    rlang_experiment()
