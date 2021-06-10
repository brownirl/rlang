import sys, os
sys.path.append(os.path.abspath("./"))

from lmdp import *
from lmdp.agents.AbstractValueIterationClass import AAValueInteration
import simple_rl as rl
import math
import numpy as np

if __name__=="__main__":
    from simple_rl.mdp.StateClass import State
    from lmdp.grounding.states.StateClass import State as RLangState
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
    
    pos1 = RLangState(data=[2,1]) # room_1 position
    pos2 = RLangState(data=[1,6]) # room_3 position
    room1_to_room3 = RLangState(data=[2,6]) 
    opt = lmdp('subpolicy-room_1-hor')
    assert lmdp('subpolicy-room_1-hor').is_executable(pos1) == True
    assert lmdp('subpolicy-room_1-hor').is_executable(pos2) == False
    assert lmdp('subpolicy-room_1-hor')().policy(state=pos1) == 'right'
    assert lmdp('subpolicy-room_3-ver').is_executable(room1_to_room3) == True
    assert lmdp('subpolicy-room_3-ver')().policy(state=room1_to_room3) == 'up'

    ########### Value Iteration #############

    value_iter = AAValueInteration(four_room_mdp, lmdp, max_iterations=1000, max_rollout=50)
    print("====Value Iteration Planner Initialized====\nPlanning...")
    value_iter.run_vi()
    vi_action_seq, vi_state_seq = value_iter.plan(four_room_mdp.get_init_state())
    print(list(map(lambda o: o.name, vi_action_seq)))
    print(vi_state_seq)