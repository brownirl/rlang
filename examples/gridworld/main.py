import copy
from collections import defaultdict

import numpy as np
from simple_rl.run_experiments import run_agents_on_mdp
from simple_rl.tasks import GridWorldMDP
from simple_rl.agents import QLearningAgent

from rlang import parse_file, parse
from rlang.src.grounding import State, Action


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
    width, height = 6, 6
    alpha = 0.1
    gamma = 0.99

    mdp = create_mdp()
    knowledge = parse_file("gridworld.rlang")

    # initialize Q table
    q_func_r = defaultdict(lambda: defaultdict(lambda: 0.0))

    for w in range(width):
        for h in range(height):
            for a, ai in {'up': 1, 'down': 2, 'left': 3, 'right': 4}.items():
                s = (w, h)
                si = State([w, h])
                # Insert known reward into Q table
                q_func_r[s][a] = knowledge.reward_function(state=si, action=ai)

    q_func_rt = copy.deepcopy(q_func_r)

    for w in range(width):
        for h in range(height):
            for a, ai in {'up': 1, 'down': 2, 'left': 3, 'right': 4}.items():
                s = (w, h)
                si = State([w, h])
                s_primei = knowledge.transition_function(state=si, action=ai)
                if s_primei is not None:
                    # We may know enough to do a TD update
                    s_prime = s_primei.view(np.ndarray)
                    s_prime = (s_prime[0][0], s_prime[0][1])
                    if q_func_rt[s_prime]:
                        # print(q_func_rt[s_prime])
                        q_func_rt[s][a] = (1 - alpha) * q_func_rt[s][a] + alpha * \
                                          (knowledge.reward_function(state=si, action=ai, next_state=s_primei) +
                                           gamma * max(q_func_rt[s_prime].values()))

    # for w in range(width):
    #     for h in range(height):
    #         for a, ai in {'up': 1, 'down': 2, 'left': 3, 'right': 4}.items():
    #             s = (w, h)
    #             si = State([w, h])
    #             predictions = knowledge.full_predictions(state=si, action=ai)
    #             print(predictions)
    #             for p in predictions.values():
    #                 print(p, p(state=si, action=ai))

    agent = QLearningAgent(mdp.get_actions())
    RLang_agent_1 = QLearningAgent(mdp.get_actions(), name="RLang Q-Learning (Rewards)", custom_q_init=q_func_r)
    RLang_agent_2 = QLearningAgent(mdp.get_actions(), name="RLang Q-Learning (Rewards, Transitions)",
                                   custom_q_init=q_func_rt)
    run_agents_on_mdp([agent, RLang_agent_1, RLang_agent_2], mdp)


if __name__ == '__main__':
    rlang_experiment()
