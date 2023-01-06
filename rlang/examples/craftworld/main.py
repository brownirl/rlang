from craftworld_env import Craftworld, Cookbook, CraftworldGYM
from simple_rl.run_experiments import run_agents_on_mdp
from simple_rl.agents import QLearningAgent
from efficient_rl.agents import Rmax, FactoredRmax, DOORmax, QLearning

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


def efficient_rl():
    agent_names = ['Rmax', 'Q Learning', 'Q Learning optimistic initalization']
    envs = [CraftworldGYM(goal='gold', path_to_recipes='craftworld_env/recipes.yaml'),
            CraftworldGYM(goal='gold', path_to_recipes='craftworld_env/recipes.yaml'),
            CraftworldGYM(goal='gold', path_to_recipes='craftworld_env/recipes.yaml')]



    # agents = [Rmax(M=1, nS=500, nA=5, r_max=20, gamma=0.95, delta=0.01, env_name='craft-gold'),
    #           QLearning(nS=500, nA=5, gamma=0.95, alpha=0.1, epsilon=0.6,
    #                     optimistic_init=False, env_name='craft-gold'),  # alpha/epsilon p.33/34 Diuks Diss
    #           QLearning(nS=500, nA=5, gamma=0.95, alpha=1, epsilon=0, r_max=20,
    #                     optimistic_init=True, env_name='craft-gold')]  # alpha/epsilon p.33/34 Diuks Diss


if __name__ == '__main__':
    # dev()
    # baseline_test()
    efficient_rl()