import sys, os
sys.path.append(os.path.abspath("./"))
# envs
from simple_rl.tasks.grid_world.GridWorldStateClass import GridWorldState
#agents
from lmdp.agents import RMaxLangAgent, RMaxAgent, RandomAgent
#lmdp
from lmdp.experiment_runner import run_agents
from functools import partial


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
    #### Run agents
    
    random = RandomAgent(mdp.get_actions())
    lang_rmax_agent = RMaxLangAgent(mdp.get_actions(), lmdp=lmdp,  s_a_threshold=30)
    lang_rmax_agent.update_from_lang(partial(gridworld_state_space, width, height))
    rmax_agent = RMaxAgent(mdp.get_actions(), s_a_threshold=30, max_reward=1)

    run_agents([lang_rmax_agent, rmax_agent], mdp, experiment_params())

    

