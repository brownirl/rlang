import sys, os
sys.path.append(os.path.abspath("./"))
# envs
from simple_rl.tasks.grid_world.GridWorldMDPClass import GridWorldMDP
from simple_rl.tasks.grid_world.GridWorldStateClass import GridWorldState
#agents
from lmdp.agents import RMaxLangAgent, RMaxAgent, RandomAgent
#lmdp
from lmdp import *
from lmdp.experiment_runner import *
from lmdp.experiment_runner import run_agents
from functools import partial

import numpy as np

def experiment_params():
    return {"instances":3, 
            "episodes": 300, 
            "steps":100,
            "clear_old_results":True,
            "rew_step_count":1,
            "track_disc_reward":False,
            "open_plot":True,
            "verbose":False,
            "reset_at_terminal":False,
            "cumulative_plot": True,
            "dir_for_plot":"results/rmax",
            "experiment_name_prefix":"",
            "track_success":False,
            "success_reward":None}


def gridworld_state_space(width, height): # state space iterator
    for x in range(1,width+1):
        for y in range(1, height+1):
            yield GridWorldState(x, y)

if __name__ == "__main__":
    from vocab import *

    lmdp = LMDP(mdp, factor_names=["x", "y"])
    with lmdp.when(lava @ effect_action) as c: # when you fall in lava (@ is the function composition operator)
        c.reward(-1)
    with c.otherwise().when(goal @ effect_action): # otherwise when in goal
        c.reward(1)

    with lmdp.when(wall @ effect_action) as c: # when the action taken takes you to a wall position 
        c.effect(S) # next state is the current state
    with lmdp.when(bool_and(any_state, any_action)) as c:
        c.effect(effect_action)

    #### Run agents
    
    random = RandomAgent(mdp.get_actions())
    lang_rmax_agent = RMaxLangAgent(mdp.get_actions(), lmdp=lmdp,  s_a_threshold=30)
    lang_rmax_agent.update_from_lang(partial(gridworld_state_space, width, height))
    rmax_agent = RMaxAgent(mdp.get_actions(), s_a_threshold=30, max_reward=1)

    run_agents([lang_rmax_agent, rmax_agent], mdp, experiment_params())

    

