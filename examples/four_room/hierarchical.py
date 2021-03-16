import sys, os
sys.path.append(os.path.abspath("./"))
from lmdp import *
from lmdp.experiment_runner import run_agents

import simple_rl as rl
import math
import numpy as np

def compute_hallways(width, height):
    '''
    Args:
        width (int)
        height (int)

    Returns:
        (dict): Contains the two hallways corresponding to each room.
    '''

    half_width = math.ceil(width / 2.0)
    half_height = math.ceil(height / 2.0)
    hallways = []
    # Wall from left to middle.
    for i in range(1, width + 1):
        if i == half_width:
            half_height -= 1
        if i + 1 == math.ceil(width / 3.0) or i == math.ceil(2 * (width + 2) / 3.0):
            hallways.append(np.array((i, half_height)))

    # Wall from bottom to top.
    for j in range(1, height + 1):
        if j + 1 == math.ceil(height / 3.0) or j == math.ceil(2 * (height + 2) / 3.0):
            hallways.append(np.array((half_width, j)))
    
    return {"room_1": (hallways[0] + (0,1), hallways[2] + (1,0)), "room_2": (hallways[1]+ (0,1), hallways[2]-(1,0)), 
            "room_3": (hallways[0] - (0,1), hallways[3] + (1,0)), "room_4": (hallways[1]-(0,1), hallways[3]-(1,0))}

def compute_rooms(lmdp, width, height):
    half_width = math.ceil(width / 2.0)
    half_height = math.ceil(height / 2.0)
    
    room_1 = Symbol(bool_and(lmdp('x') <= half_width, lmdp('y') <= half_height), "room_1")
    room_2 = Symbol(bool_and(lmdp('x') > half_width, lmdp('y') < half_height), "room_2")
    room_3 = Symbol(bool_and(lmdp('x') < half_width, lmdp('y') > half_height), "room_3")
    room_4 = Symbol(bool_and(lmdp('x') >= half_width, lmdp('y') > half_height-1), "room_4")
    return (room_1, room_2, room_3, room_4)

def hallway_policy(lmdp, hallway, wall_type):
    distance_to_hallway = lmdp("position") - hallway
    def policy(state):
        d = distance_to_hallway(state) # manhattan distance
        if(abs(d[0]) + abs(d[1]) > 0):
            if (wall_type == 'hor'): # below or above the wall
                if(d[0] != 0):
                    return lmdp('right')() if d[0] < 0 else lmdp('left')()
                else:
                    return lmdp('up')() if d[1] < 0 else lmdp('down')()
            elif (wall_type == 'ver'): # right or left of the wall
                if(d[1] != 0):
                    return lmdp('up')() if d[1] < 0 else lmdp('down')()
                else:
                    return lmdp('right')() if d[0] < 0 else lmdp('left')()

    return policy


def experiment_params(**kwargs):
    default_params = {
        "instances":1, 
        "episodes": 5000, 
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
    new_params = default_params.update(kwargs)
    return default_params#new_params

if __name__=="__main__":
    from lmdp.agents.HierarchicalAgent import SubgoalHierarchicalAgent
    from lmdp.agents.factories import DQNFactory, masked_fc_relu_q, OptDQNFactory

    from lmdp.agents.simple_rl_agent import SimpleRLAgent
    from lmdp.grounding.actions.options import Option

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

    # options to navigate to neighboring rooms
    # with lmdp.when(room_1) as c: 
    #     c.subpolicy(until=bool_not(room_1) | room_2, name='subpolicy-room1-room2')
    #     c.subpolicy(until=bool_not(room_1) | room_3, name='subpolicy-room1-room3')
    # with lmdp.when(room_2) as c: 
    #     c.subpolicy(until=bool_not(room_2) | room_1, name='subpolicy-room2-room1')
    #     c.subpolicy(until=bool_not(room_2) | room_4, name='subpolicy-room2-room4')
    # with lmdp.when(room_3) as c: 
    #     c.subpolicy(until=bool_not(room_3) |room_1, name='subpolicy-room3-room1')
    #     c.subpolicy(until=bool_not(room_3) |room_4, name='subpolicy-room3-room4')
    # with lmdp.when(room_4) as c: 
    #     c.subpolicy(until=bool_not(room_4) | room_2, name='subpolicy-room4-room2')
    #     c.subpolicy(until=bool_not(room_4) | room_3, name='subpolicy-room4-room3')
    
    with lmdp.when(room_1) as c: 
        c.subpolicy(until=room_2, name='o-room1-room2')
        c.subpolicy(until=room_3, name='o-room1-room3')
    with lmdp.when(room_2) as c: 
        c.subpolicy(until=room_1, name='o-room2-room1')
        c.subpolicy(until=room_4, name='o-room2-room4')
    with lmdp.when(room_3) as c: 
        c.subpolicy(until=room_1, name='o-room3-room1')
        c.subpolicy(until=room_4, name='o-room3-room4')
    with lmdp.when(room_4) as c: 
        c.subpolicy(until=room_2, name='o-room4-room2')
        c.subpolicy(until=room_3, name='o-room4-room3')

    ### Hierarchical Q-Learning
    options = sorted([sp.to_option2() for sp in lmdp.get_subpolicies()], key=lambda o: o._id)
    inner_factory = DQNFactory(four_room_mdp.get_actions(), state_space=(2,), alpha=0.001)
    outer_factory = OptDQNFactory(options, state_space=(2,), alpha=0.001, model=masked_fc_relu_q(options))
    agent = SubgoalHierarchicalAgent(four_room_mdp.get_actions(), options, outer_factory, inner_factory)

    run_agents([SimpleRLAgent(agent, options)], four_room_mdp, experiment_params())
    # run_agents([SimpleRLAgent(inner_factory(None), four_room_mdp.get_actions())], four_room_mdp, experiment_params())
    


