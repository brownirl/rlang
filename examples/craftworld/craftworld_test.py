import sys, os
sys.path.append(os.path.abspath("./"))

from envs import Craftworld
from lmdp.experiment_runner import run_agents
from lmdp.agents import RandomAgent, QLearningAgent
from lmdp.agents.ppo import PPO, ppo_hyperparameters
from lmdp.agents.simple_rl_agent import SimpleRLAgent
from networks import CraftFeatureNetwork, fc_value_head, fc_policy_head

def experiment_params():
    return {"instances":1, 
            "episodes": 10, 
            "steps":100,
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
    ppo_params = ppo_hyperparameters(feature_model_constructor=CraftFeatureNetwork(*mdp.get_grid_params()),
                                     policy_model_constructor=fc_policy_head(),
                                     value_model_constructor=fc_value_head()
                                    )   
    ppo = PPO(mdp.actions, mdp.get_curr_state().features().shape, **ppo_params)
    run_agents([SimpleRLAgent(ppo, mdp.actions, name='ppo')], mdp, experiment_params())