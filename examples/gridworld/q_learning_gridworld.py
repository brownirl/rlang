import sys, os
sys.path.append(os.path.abspath("./"))
# envs
from simple_rl.tasks.grid_world.GridWorldStateClass import GridWorldState
from simple_rl.tasks.grid_world.GridWorldMDPClass import GridWorldMDP
#agents
from lmdp.agents import RandomAgent, QLearningAgent, QLearningLangAgent
#lmdp
from rlang.src.lmdp import RLMDP
from lmdp.experiment_runner import run_agents
from functools import partial


def experiment_params():
    return {"instances":2, 
            "episodes": 1000, 
            "steps":100,
            "clear_old_results":True,
            "rew_step_count":1,
            "track_disc_reward":False,
            "open_plot":True,
            "verbose":False,
            "reset_at_terminal":False,
            "cumulative_plot": True,
            "dir_for_plot":"results",
            "experiment_name_prefix":"",
            "track_success":False,
            "success_reward":None}

def gridworld_state_space(width, height): # state space iterator
    for x in range(1,width+1):
        for y in range(1, height+1):
            yield GridWorldState(x, y)

if __name__ == "__main__":
    #### Run agents
    # MDP parameters
    width, height = 6, 6
    lava_locs = [(3, 2), (1, 4), (2, 4), (2, 5)]
    walls = [(3, 1)]
    goal_locs = [(5, 1)]

    mdp = GridWorldMDP(width, height, walls=walls, lava_locs=lava_locs, goal_locs=goal_locs, slip_prob=0.33,
                       step_cost=0)

    lmdp = RLMDP(mdp, "gridworld.rlang", factor_names=["x", "y"])

    print(lmdp.listener.new_vars)

    # random = RandomAgent(mdp.get_actions())
    # epsilon = 0.1
    # alpha = 0.05
    # q_learning_agent = QLearningAgent(mdp.get_actions(), epsilon=epsilon, alpha=alpha, anneal=True)
    # lang_q_learning_agent = QLearningLangAgent(mdp.get_actions(), lmdp=lmdp, epsilon=epsilon/10, alpha=alpha, anneal=True)
    # lang_q_learning_agent.update_from_lang(partial(gridworld_state_space, width, height))
    # run_agents([lang_q_learning_agent , q_learning_agent], mdp, experiment_params())

    

