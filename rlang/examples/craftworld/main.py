from craftworld_env import Craftworld, Cookbook
from simple_rl.run_experiments import run_agents_on_mdp
from simple_rl.agents import QLearningAgent

import context
import rlang
from rlang.agents import RLangQLearningAgent


def baseline_test():
    """
    This is just for ensuring that Craftworld actually works.
    We should be able to chuck a SimpleRL agent directly into it.
    It works

    """
    mdp = Craftworld(goal='gold', path_to_recipes='craftworld_env/recipes.yaml')
    agent = QLearningAgent(mdp.get_actions())
    run_agents_on_mdp([agent], mdp, steps=400, episodes=100)


def dev():
    cookbook = Cookbook('craftworld_env/recipes.yaml')
    knowledge = rlang.parse_file('craftworld.rlang')
    print(knowledge)


if __name__ == '__main__':
    # dev()
    baseline_test()
