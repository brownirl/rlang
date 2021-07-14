import sys, os
sys.path.append(os.path.abspath("./"))
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

def experiment_params(**kwargs):
    default_params = {
        "instances":1, 
        "episodes": 3000, 
        "steps":25,
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


if __name__ == "__main__":
    from lmdp.agents.factories import QLearningFactory
    from lmdp.agents.lang_hierarchical import RLangIntraoptionQAgent, RLangSMDPQAgent
    from lmdp.agents.simple_rl_agent import SimpleRLAgent
    from vocab import *

    lmdp_none = LMDP(taxi_mdp)
    lmdp_full = LMDP(taxi_mdp)
    
    ############ policy structure
    passenger_0_in_dest = (passenger_0_dest == passenger_0_pos)
    init_passenger_0_pick_up = bool_and(
                                        bool_not(passenger_in_taxi), # taxi is free
                                        bool_not(passenger_0_in_dest) # passenger 0 need to be taken to dest
                                        )

    with lmdp_none.when(init_passenger_0_pick_up) as c:
        c.subpolicy(name='pickup-passenger-0', 
                    until=passenger_0_intaxi) # take passenger 0 to dest 
    
    with lmdp_none.when(passenger_0_intaxi) as c:
        c.subpolicy(name='dropoff-passenger-0', 
                    until=passenger_0_in_dest & bool_not(passenger_0_intaxi))

    passenger_1_in_dest = (passenger_1_dest == passenger_1_pos)
    init_passenger_1_pick_up = bool_and(
                                        bool_not(passenger_in_taxi), # taxi is free
                                        bool_not(passenger_1_in_dest) # passenger 0 need to be taken to dest
                                        )

    with lmdp_none.when(init_passenger_1_pick_up) as c:
        c.subpolicy(name='pickup-passenger-1', 
                    until=passenger_1_intaxi) # take passenger 1 to dest 
    
    with lmdp_none.when(passenger_1_intaxi) as c:
        c.subpolicy(name='dropoff-passenger-1', 
                    until=passenger_1_in_dest & bool_not(passenger_1_intaxi))

    #### full options

    with lmdp_full.when(init_passenger_0_pick_up) as c:
        c.subpolicy(name='pickup-passenger-0', 
                    policy= partial(pick_up_passenger, passenger_0),
                    until=passenger_0_intaxi) # take passenger 0 to dest 
    
    with lmdp_full.when(passenger_0_intaxi) as c:
        c.subpolicy(name='dropoff-passenger-0', 
                    policy=partial(dropoff_passenger, passenger_0), 
                    until=passenger_0_in_dest & bool_not(passenger_0_intaxi))

    with lmdp_full.when(init_passenger_1_pick_up) as c:
        c.subpolicy(name='pickup-passenger-1', 
                    policy=partial(pick_up_passenger, passenger_1),
                    until=passenger_1_intaxi) # take passenger 1 to dest 
    
    with lmdp_full.when(passenger_1_intaxi) as c:
        c.subpolicy(name='dropoff-passenger-1', 
                    policy=partial(dropoff_passenger, passenger_1), 
                    until=passenger_1_in_dest & bool_not(passenger_1_intaxi))

    #### Run agents
    inner_factory = QLearningFactory(taxi_mdp.get_actions(), alpha=0.1, epsilon=0.1, anneal=True)
    rlang_none = RLangSMDPQAgent(taxi_mdp.get_actions(), lmdp_none, inner_factory, anneal=False, epsilon=0.01, alpha=0.5)
    rlang_full = RLangSMDPQAgent(taxi_mdp.get_actions(), lmdp_full, inner_factory, anneal=False, epsilon=0.01, alpha=0.5)

    #Flat Q Learning
    flat_q_learning = QLearningAgent(taxi_mdp.get_actions(), alpha=0.1, epsilon=0.1, anneal=True, name="Flat-Q-Learning")

    run_agents([SimpleRLAgent(rlang_full, rlang_full.get_options(), name="RLang-Option-Q-Agent (F)"),
                SimpleRLAgent(rlang_none, rlang_none.get_options(), name="RLang-Option-Q-Agent (N)"),
                flat_q_learning], 
                taxi_mdp, 
                experiment_params(instances=5, episodes=1000, steps=1000, cumulative_plot=True))