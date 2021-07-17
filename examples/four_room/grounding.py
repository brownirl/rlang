from lmdp.grounding import *
from simple_rl.tasks.grid_world.GridWorldMDPClass import GridWorldMDP, GridWorldState
from simple_rl.tasks.four_room.FourRoomMDPClass import FourRoomMDP
import math
import numpy as np


#### aux functions

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


# MDP parameters
height, width = 10, 10
goals = [(8, 4)]

#### Factors
position = StateFactor([0,1], "position") # definition of new factor.
x, y = position[0], position[1]


### Symbols
goal = Symbol(bool_and(x == 8, y == 4))

half_width = math.ceil(width / 2.0)
half_height = math.ceil(height / 2.0)

room_1 = Symbol(bool_and(x <= half_width, y < half_height), "room_1")
room_2 = Symbol(bool_and(x >= half_width, y < half_height), "room_2")
room_3 = Symbol(bool_and(x <= half_width, y >= half_height), "room_3")
room_4 = Symbol(bool_and(x >= half_width, y >= half_height-1), "room_4")

hallways = compute_hallways(width, height)

### Effects

# def action_effect(state, action): # actions effects on state/Transition Dynamics
#         if action == 'up':
#             return  GridWorldState(state.x, state.y + 1)
#         if action == 'down':
#             return  GridWorldState(state.x, state.y-1)
#         if action == 'left':
#             return GridWorldState(state.x - 1, state.y)
#         if action == 'right':
#             return GridWorldState(state.x + 1, state.y)

# effect_action = PredictiveEffect(bool_and(any_state, any_action), action_effect)

### actions
actions = ("up", "down", "left", "right")
locals().update(dict(zip(actions, actions)))
### Subpolicies

def hallway_policy(hallway, wall_type):
    distance_to_hallway = position - hallway
    def policy(state):
        d = distance_to_hallway(state) # manhattan distance
        if(abs(d[0]) + abs(d[1]) > 0):
            if (wall_type == 'hor'): # below or above the wall
                if(d[0] != 0):
                    return "right" if d[0] < 0 else "left"
                else:
                    return "up" if d[1] < 0 else "down"
            elif (wall_type == 'ver'): # right or left of the wall
                if(d[1] != 0):
                    return "up" if d[1] < 0 else "down"
                else:
                    return "right" if d[0] < 0 else "left"

    return policy

four_room_mdp = FourRoomMDP(goal_locs=goals, slip_prob=0.33, step_cost=0, rand_init=True) # initialize mdp