import copy
from collections import defaultdict

import numpy as np
from simple_rl.run_experiments import run_agents_on_mdp
from simple_rl.tasks import GridWorldMDP
from simple_rl.agents import QLearningAgent

from rlang import parse_file, parse
from rlang.src.grounding import State, Action

from agents.RLangQLearningAgentClass import RLangQLearningAgent


def create_mdp():
    # MDP parameters
    width, height = 6, 6
    lava_locs = [(3, 2), (1, 4), (2, 4), (2, 5)]
    walls = [(3, 1)]
    goal_locs = [(5, 1)]

    mdp = GridWorldMDP(width, height, walls=walls, lava_locs=lava_locs, goal_locs=goal_locs, slip_prob=0.0,
                       step_cost=0)
    return mdp


def simple_experiment():
    mdp = create_mdp()
    agent = QLearningAgent(mdp.get_actions())
    run_agents_on_mdp([agent], mdp)


def rlang_experiment():
    # We need to know these MDP and Q Learning parameters
    mdp = create_mdp()
    knowledge = parse_file("gridworld.rlang")

    states = list()
    for w in range(mdp.width):
        for h in range(mdp.height):
            states.append((w, h))

    agent = QLearningAgent(mdp.get_actions())
    rlang_agent = RLangQLearningAgent(mdp.get_actions(), states, knowledge)
    # rlang_agent_2 = RLangQLearningAgent(mdp.get_actions(), states, knowledge, name="RLang-Q-learning-transition",
    #                                     use_transition=True)
    run_agents_on_mdp([agent, rlang_agent], mdp)


if __name__ == '__main__':
    rlang_experiment()
