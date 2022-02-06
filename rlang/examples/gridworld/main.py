from simple_rl.run_experiments import run_agents_on_mdp
from simple_rl.tasks import GridWorldMDP
from simple_rl.agents import QLearningAgent

import context
import rlang
from rlang.agents import RLangQLearningAgent


def create_mdp():
    # MDP parameters
    width, height = 6, 6
    lava_locs = [(3, 2), (1, 4), (2, 4), (2, 5)]
    walls = [(3, 1)]
    goal_locs = [(5, 1)]

    mdp = GridWorldMDP(width, height, walls=walls, lava_locs=lava_locs, goal_locs=goal_locs, slip_prob=0.0,
                       step_cost=0)
    states = list()
    for w in range(mdp.width):
        for h in range(mdp.height):
            states.append((w, h))

    return mdp, states


def simple_experiment():
    mdp, states = create_mdp()
    agent = QLearningAgent(mdp.get_actions())
    run_agents_on_mdp([agent], mdp)


def rlang_experiment():
    # We need to know these MDP and Q Learning parameters
    mdp, states = create_mdp()

    # Parse RLang program into knowledge object
    knowledge = rlang.parse_file("gridworld.rlang")

    # Create a baseline Q-Learning agent
    agent = QLearningAgent(mdp.get_actions())

    # Create RLang Q-Learning agent
    rlang_agent = RLangQLearningAgent(
        actions=mdp.get_actions(), states=states, knowledge=knowledge)

    # Compare performance of agents on mdp
    run_agents_on_mdp([agent, rlang_agent], mdp)


if __name__ == '__main__':
    rlang_experiment()
