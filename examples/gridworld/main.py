from simple_rl.run_experiments import run_agents_on_mdp
from simple_rl.tasks import GridWorldMDP
from simple_rl.agents import QLearningAgent

from rlang import parse_file
from rlang.src.grounding import State, Action


def create_mdp():
    # MDP parameters
    width, height = 6, 6
    lava_locs = [(3, 2), (1, 4), (2, 4), (2, 5)]
    walls = [(3, 1)]
    goal_locs = [(5, 1)]

    mdp = GridWorldMDP(width, height, walls=walls, lava_locs=lava_locs, goal_locs=goal_locs, slip_prob=0.33,
                       step_cost=0)
    return mdp


def simple_experiment():
    mdp = create_mdp()
    agent = QLearningAgent(mdp.get_actions())
    run_agents_on_mdp([agent], mdp)


def rlang_experiment():
    mdp = create_mdp()
    knowledge = parse_file("gridworld.rlang")

    # exec = {'state': State([3, 1]), 'action': knowledge['up']}
    #
    # t = knowledge.transition_function
    # predictions = knowledge.full_predictions(**exec)
    # next_position = predictions['position']
    #
    # print(next_position(**exec))
    # print(knowledge.transition_function(**a))

    # knowledge.full_predictions(**a)


if __name__ == '__main__':
    rlang_experiment()
