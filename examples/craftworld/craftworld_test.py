import sys, os
sys.path.append(os.path.abspath("./lmdp"))

from envs import Craftworld
from lmdp.experiment_runner import run_agents
from lmdp.agents import RandomAgent, QLearningAgent

from simple_rl.agents import RMaxAgent

if __name__=="__main__":
    mdp = Craftworld('gold', 'lmdp/envs/craftworld/recipes.yaml')
    random = RandomAgent(mdp.get_actions())
    rmax_agent = RMaxAgent(mdp.get_actions(),  gamma=0.99)
    run_agents([rmax_agent], mdp)