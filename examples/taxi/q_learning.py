import sys, os
sys.path.append(os.path.abspath("./lmdp"))
# envs
from simple_rl.tasks.grid_world.GridWorldMDPClass import GridWorldMDP
from simple_rl.tasks.grid_world.GridWorldStateClass import GridWorldState
#agents
from lmdp.agents import RandomAgent, QLearningAgent, QLearningLangAgent
#lmdp
from lmdp import *
from lmdp.experiment_runner import *
from lmdp.experiment_runner import run_agents
from functools import partial

import numpy as np

def experiment_params():
    return {"instances":5, 
            "episodes": 100, 
            "steps":400,
            "clear_old_results":True,
            "rew_step_count":1,
            "track_disc_reward":False,
            "open_plot":True,
            "verbose":False,
            "reset_at_terminal":False,
            "cumulative_plot":not False,
            "dir_for_plot":"results",
            "experiment_name_prefix":"",
            "track_success":False,
            "success_reward":None}



if __name__ == "__main__":
    from vocab import *

    lmdp = LMDP(taxi_mdp)

    with lmdp.when(bool_and(passenger_0_pos == passenger_0_dest, A == "dropoff", passenger_in_taxi)) as c:
        c.reward(1.0) 

    with lmdp.when(bool_and(A == "dropoff", bool_not(passenger_in_taxi))) as c:
        c.effect(S_prime == S)

    #### Run agents
    
    random = RandomAgent(taxi_mdp.get_actions())

    q_learning_agent = QLearningAgent(taxi_mdp.get_actions(), anneal=True, epsilon=0.2)
    lang_q_learning_agent = QLearningLangAgent(taxi_mdp.get_actions(), lmdp=lmdp, anneal=True, epsilon=0.2)
    lang_q_learning_agent.update_from_lang(taxi_states)
    run_agents([lang_q_learning_agent, q_learning_agent, random], taxi_mdp, experiment_params())

    

