import sys, os
sys.path.append(os.path.abspath('./'))

from lmdp import *
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
    
    return {"room_1": (hallways[0], hallways[2]), "room_2": (hallways[1], hallways[2]), 
            "room_3": (hallways[0], hallways[3]), "room_4": (hallways[1], hallways[3])}

def compute_rooms(lmdp, width, height):
    half_width = math.ceil(width / 2.0)
    half_height = math.ceil(height / 2.0)
    
    room_1 = Symbol((lmdp('x') < half_width) & (lmdp('y') < half_height), "room_1")
    room_2 = Symbol((lmdp('x') > half_width) & (lmdp('y') < half_height), "room_2")
    room_3 = Symbol((lmdp('x') < half_width) & (lmdp('y') > half_height), "room_3")
    room_4 = Symbol((lmdp('x') > half_width) & (lmdp('y') > half_height), "room_4")
    return (room_1, room_2, room_3, room_4)

def hallway_policy(lmdp, hallway):
    distance_to_hallway = lmdp("position") - hallway
    def policy(state):
        d = distance_to_hallway(state) # manhattan distance
        if(abs(d[0]) + abs(d[1]) > 0):
            if(abs(d[0]) > abs(d[1])): # d_x > d_y, hence move in the x axis first
                return lmdp('right') if d[0] < 0 else lmdp('left') 
            else:
                return lmdp('up') if d[1] < 0 else lmdp('down')

    return policy


if __name__=="__main__":
    from simple_rl.mdp.StateClass import State
    
    height, width = 9, 9 
    
    four_room_mdp = rl.tasks.FourRoomMDP() # initialize mdp
    lmdp = LMDP(four_room_mdp, factor_names=["x", "y"]) # mdp is given to bind factors

    lmdp.add(StateFactor([0, 1], name='position'))
    rooms = compute_rooms(lmdp, width, height) # compute rooms symbols
    hallways = compute_hallways(width, height)

    for r in rooms:
        lmdp.add(r) # add room symbols to lmdp

    for room in rooms:
        with lmdp.when(room) as c: # compute and create hallway policies for each room
            for idx in (0,1):
                c.subpolicy(policy=hallway_policy(lmdp, hallways[room.name][idx]), until= room.not_(), name='subpolicy-'+room.name+'-'+str(idx))

    ############# TEST ################
    
    pos1 = State(data=[2,1]) # room_1 position
    pos2 = State(data=[1,6]) # room_3 position
    opt = lmdp('subpolicy-room_1-0')
    assert lmdp('subpolicy-room_1-0').is_executable(pos1) == True
    assert lmdp('subpolicy-room_1-0').is_executable(pos2) == False
    assert lmdp('subpolicy-room_1-0')(state=pos1)() == 'up'