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

    lmdp = LMDP(taxi_mdp)

    # reward function
    with lmdp.when(bool_and(passenger_0_pos == passenger_0_dest, A == "dropoff", passenger_in_taxi)) as c:
        c.reward(1) 

    # transition dynamics
    with lmdp.when(bool_and(A == "dropoff", bool_not(passenger_in_taxi))) as c:
        c.effect(S_prime == S)
    with lmdp.when(bool_and(agent_position == passenger_0_pos, A == "pickup")) as c:
        c.effect(passenger_in_taxi)

    # policy structure
    passenger_0_in_dest = (passenger_0_dest == passenger_0_pos)
    init_passenger_0_pick_up = bool_and(
                                        bool_not(passenger_in_taxi), # taxi is free
                                        bool_not(passenger_0_in_dest) # passenger 0 need to be taken to dest
                                        )

    with lmdp.when(init_passenger_0_pick_up) as c:
        c.subpolicy(name='pickup-passenger-0', 
                    policy= partial(pick_up_passenger, passenger_0),
                    until=passenger_0_intaxi) # take passenger 0 to dest 
    
    with lmdp.when(passenger_0_intaxi) as c:
        c.subpolicy(name='dropoff-passenger-0', 
                    policy=partial(dropoff_passenger, passenger_0), 
                    until=passenger_0_in_dest & bool_not(passenger_0_intaxi))
    
    # with lmdp.when(bool_and(passenger_0_in_dest, passenger_0_intaxi)) as c:
    #     c.subpolicy(name='dropoff-0',
    #                 policy = lambda *args, **kwargs: "dropoff",
    #                 until=bool_not(passenger_0_intaxi))
    
    passenger_1_in_dest = (passenger_1_dest == passenger_1_pos)
    init_passenger_1_pick_up = bool_and(
                                        bool_not(passenger_in_taxi), # taxi is free
                                        bool_not(passenger_1_in_dest) # passenger 0 need to be taken to dest
                                        )

    with lmdp.when(init_passenger_1_pick_up) as c:
        c.subpolicy(name='pickup-passenger-1', 
                    # policy=partial(pick_up_passenger, passenger_1),
                    until=passenger_1_intaxi) # take passenger 0 to dest 
    
    with lmdp.when(passenger_1_intaxi) as c:
        c.subpolicy(name='dropoff-passenger-1', 
                    #policy=partial(dropoff_passenger, passenger_1), 
                    until=passenger_1_in_dest & bool_not(passenger_1_intaxi))
    
    # with lmdp.when(bool_and(passenger_1_in_dest, passenger_1_intaxi)) as c:
    #     c.subpolicy(name='dropoff-1',
    #                 policy = lambda *args, **kwargs: "dropoff",
    #                 until= bool_not(passenger_1_intaxi))
    
    # with lmdp.when(bool_and(passenger_0_in_dest, passenger_0_pos == agent_position)) as c:
    #     # do not pick up.
    #  

    # with lmdp.when(bool_and(passenger_0_pos == agent_position, init_passenger_0_pick_up)) as c:
    #     c.policy(action="pickup")

    #### Run agents
    inner_factory = QLearningFactory(taxi_mdp.get_actions(), alpha=0.1, epsilon=0.1, anneal=True)
    lang_hierarchical_agent = RLangSMDPQAgent(taxi_mdp.get_actions(), lmdp, inner_factory, anneal=False, epsilon=0.01, alpha=0.5)

    #Flat Q Learning
    flat_q_learning = QLearningAgent(taxi_mdp.get_actions(), alpha=0.1, epsilon=0.1, anneal=True, name="Flat-Q-Learning")

    run_agents([SimpleRLAgent(lang_hierarchical_agent, lang_hierarchical_agent.get_options(), name="RLang-Intraoption-Q-Agent")], 
                taxi_mdp, 
                experiment_params(instances=1, episodes=1000, steps=1000, cumulative_plot=False))
    
    # run_agents([flat_q_learning], 
    #             taxi_mdp, 
    #             experiment_params(instances=1, episodes=300, steps=1000))