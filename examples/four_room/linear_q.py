import sys, os
sys.path.append(os.path.abspath("./"))
from lmdp import *
from lmdp.experiment_runner import run_agents

import simple_rl as rl
import numpy as np

def experiment_params(**kwargs):
    default_params = {
        "instances":1, 
        "episodes": 1000, 
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
    default_params.update(kwargs)
    return default_params

if __name__=="__main__":
    from lmdp.agents.HierarchicalAgent import SubgoalHierarchicalAgent, OptionAgent
    from lmdp.agents.factories import DQNFactory, masked_fc_relu_q, OptDQNFactory
    from lmdp.agents import RandomAgent
    from lmdp.agents.simple_rl_agent import SimpleRLAgent
    from lmdp.grounding.actions.options import Option
    from lmdp.utils.features import FourierBasis
    from simple_rl.agents import LinearQAgent
    from simple_rl.abstraction import FeatureWrapper
    from vocab import *
    
    lmdp = LMDP(four_room_mdp, factor_names=["x", "y"]) # mdp is given to bind factors

    lmdp.add(position) # add position to lmdp symbols
    room_1 = Symbol(bool_and(x <= half_width, y <= half_height), "room_1")
    room_2 = Symbol(bool_and(x > half_width, y < half_height), "room_2")
    room_3 = Symbol(bool_and(x < half_width, y > half_height), "room_3")
    room_4 = Symbol(bool_and(x >= half_width, y > half_height-1), "room_4")
    rooms = (room_1, room_2, room_3, room_4)
    
    for r in rooms:
        lmdp.add(r) # add room symbols to lmdp

    ### Linear Q Learning with Fourier Bases
    random_agent = RandomAgent(four_room_mdp.get_actions())
    feats = FourierBasis(2, [width, height], order=7)
    agent_params={"actions":four_room_mdp.get_actions(), "num_features":feats.num_features(), "alpha":0.3, "epsilon":0.4, "rand_init": True}
    linear_q = FeatureWrapper(LinearQAgent, feature_mapper=feats, agent_params=agent_params)
    run_agents([linear_q], four_room_mdp, experiment_params(instances=10, episodes=1000, steps=500))


