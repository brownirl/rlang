import sys, os
sys.path.append(os.path.abspath("./lmdp"))

from lmdp import *
from lmdp.agents.AbstractValueIterationClass import AAValueInteration
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
    room_2 = Symbol(bool_and(lmdp('x') >= half_width, lmdp('y') < half_height), "room_2")
    room_3 = Symbol(bool_and(lmdp('x') <= half_width, lmdp('y') >= half_height), "room_3")
    room_4 = Symbol(bool_and(lmdp('x') >= half_width, lmdp('y') >= half_height-1), "room_4")
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


if __name__=="__main__":
    from simple_rl.mdp.StateClass import State
    from vocab import *
    
    lmdp = LMDP(four_room_mdp, factor_names=["x", "y"]) # mdp is given to bind factors

    lmdp.add(position) # add position to lmdp symbols
    
    rooms = (room_1, room_2, room_3, room_4)
    for r in rooms:
        lmdp.add(r) # add room symbols to lmdp

    for room in rooms:
        with lmdp.when(room) as c: # compute and create hallway policies for each room
            for idx in (('hor', 0),('ver', 1)):
                c.subpolicy(policy=hallway_policy(hallways[room.name][idx[1]], wall_type=idx[0]), until=bool_not(room), name='subpolicy-'+room.name+'-'+idx[0])

    ############# TEST ################
    
    pos1 = State(data=[2,1]) # room_1 position
    pos2 = State(data=[1,6]) # room_3 position
    room1_to_room3 = State(data=[2,6]) 
    opt = lmdp('subpolicy-room_1-hor')
    assert lmdp('subpolicy-room_1-hor').is_executable(pos1) == True
    assert lmdp('subpolicy-room_1-hor').is_executable(pos2) == False
    assert lmdp('subpolicy-room_1-hor')(state=pos1) == 'up'
    assert lmdp('subpolicy-room_3-ver').is_executable(room1_to_room3) == True
    assert lmdp('subpolicy-room_3-ver')(state=room1_to_room3) == 'up'

    ########### Value Iteration #############

    value_iter = AAValueInteration(four_room_mdp, lmdp, max_iterations=1000, max_rollout=50)
    print("====Value Iteration Planner Initialized====\nPlanning...")
    value_iter.run_vi()
    vi_action_seq, vi_state_seq = value_iter.plan(four_room_mdp.get_init_state())
    print(list(map(lambda o: o.name, vi_action_seq)))
    print(vi_state_seq)