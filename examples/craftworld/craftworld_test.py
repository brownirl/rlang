import sys, os
sys.path.append(os.path.abspath("./"))

from envs import Craftworld
from lmdp.experiment_runner import run_agents
from lmdp.agents import RandomAgent, QLearningAgent

from simple_rl.agents import RMaxAgent
def experiment_params():
    return {"instances":1, 
            "episodes": 500, 
            "steps":500,
            "clear_old_results":True,
            "rew_step_count":1,
            "track_disc_reward":False,
            "open_plot":True,
            "verbose":False,
            "reset_at_terminal":False,
            "cumulative_plot": False,
            "dir_for_plot":"results",
            "experiment_name_prefix":"",
            "track_success":False,
            "success_reward":None}

if __name__=="__main__":
    mdp = Craftworld('gold', 'envs/craftworld/recipes.yaml')
    random = RandomAgent(mdp.get_actions())
    run_agents([random], mdp, experiment_params())