from simple_rl.run_experiments import run_agents_on_mdp
from simple_rl.tasks import GridWorldMDP
from simple_rl.agents import QLearningAgent

from rlang import parse_file


def run_simple_experiment():
    # MDP parameters
    width, height = 6, 6
    lava_locs = [(3, 2), (1, 4), (2, 4), (2, 5)]
    walls = [(3, 1)]
    goal_locs = [(5, 1)]

    mdp = GridWorldMDP(width, height, walls=walls, lava_locs=lava_locs, goal_locs=goal_locs, slip_prob=0.33,
                       step_cost=0)
    agent = QLearningAgent(mdp.get_actions())
    run_agents_on_mdp([agent], mdp)


def run_experiment_with_RLang():
    knowledge = parse_file("gridworld.rlang")
    print(knowledge['x'])


if __name__ == '__main__':
    run_experiment_with_RLang()
