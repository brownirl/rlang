import sys, os

from grounding.groundings.state.factor import Factor
sys.path.append(os.path.abspath("./"))

import random
import numpy as np
from lmdp.grounding import *

from simple_rl.tasks import TaxiOOMDP, TaxiState
from simple_rl.mdp.oomdp.OOMDPObjectClass import OOMDPObject
from functools import partial
from collections import deque
import copy

from taxi_utils import taxi_state_generator

# Taxi MDP Parameters
WIDTH, HEIGHT = 5, 5
agent = {"x":1, "y":1, "has_passenger":0}
passengers = [{"x":4, "y":1, "dest_x":2, "dest_y":1, "in_taxi":0}, {"x":3, "y":2, "dest_x":4, "dest_y":1, "in_taxi":0}]
walls = [{"x": 2, "y": 2}]

## Utils
passenger_n_features = len(passengers[0])
wall_n_features = len(walls[0]) if len(walls) > 0 else 0
agent_n_features = len(agent)

#### VOCABULARY

#-----factors
# agent

# [0, 1, 2]
agent_state = Factor(list(range(agent_n_features)), name="agent")

# walls
walls_state = {}

""" 
init_idx = 3
len(walls) = 1
wall_n_features = 2
{"wall_0"": StateFactor([3, 4], "wall_0")}


"""

init_idx = agent_n_features
for i in range(len(walls)):
    walls_state.update({"wall_"+str(i): 
                        Factor(list(range(init_idx, init_idx + (i+1)*wall_n_features)), "wall_"+str(i))})
    init_idx += (i+1)*wall_n_features

# passengers
passenger_state = {}
for p in range(len(passengers)):
    passenger_state["passenger_"+str(p)] = Factor(list(range(init_idx, init_idx + passenger_n_features)), "passenger_"+str(p))
    init_idx += (p+1)*passenger_n_features

locals().update(walls_state)
locals().update(passenger_state)

#-----features 
passenger_pos_dest= {}
for name, passenger in passenger_state.items():
    passenger_pos_dest.update({name + "_pos": passenger[:2]})
    passenger_pos_dest.update({name + "_dest": passenger[2:4]})
    passenger_pos_dest.update({name +"_intaxi": passenger[4] == 1})

locals().update(passenger_pos_dest)

agent_position = agent_state[:2]  #agent_pos

#-----symbols 

# wall = Symbol()# wall

passenger_in_taxi = agent_state[2] == 1 # passenger in taxi

#-----subpolicies
# primitive actions
actions = ("down", "up", "left", "right", "pickup", "dropoff")
actions = dict(zip(actions, actions))
locals().update(actions) 

# move_to_cell
def move_to_cell(x, y, state):
    pos = agent_position(state)
    d = pos - np.array((x, y)) # manhattan distance
    direction = [0, 1]
    random.shuffle(direction)
    a_hor = _move_horizontally(pos, d, state)
    a_ver = _move_vertically(pos, d, state)

    if(d[0] != 0 or d[1] != 0): # not in dest
        if (d[0] != 0 and d[1] != 0): # if both directions are possible, flip a coin
            if direction[0] == 0: # move horizontally if possible
                return a_hor if a_hor is not None else a_ver
            else:   # move vertically if possible
                return a_ver if a_ver is not None else a_hor
        elif d[0] != 0: # move horizontally is possible
            return a_hor if a_hor is not None else a_ver
        else:
            return a_ver if a_ver is not None else a_hor

def _move_vertically(pos, d, state):
    if d[1] < 0 and _is_free_to_move(pos + (0, 1), state):
        return actions["up"]
    elif _is_free_to_move(pos + (0, -1), state):
        return actions["down"]

def _move_horizontally(pos, d, state):
    if d[0] < 0 and _is_free_to_move(pos + (1, 0), state):
        return actions["right"]
    elif _is_free_to_move(pos + (-1, 0), state):
        return actions["left"]

def _is_free_to_move(pos, state):
    for w in walls_state.values():
        if np.array_equal(pos, w(state)):
            return False
    return True

# pickup passenger (parameterized options)
def pick_up_passenger(passenger, state):
    passenger_state = passenger(state)
    if ((agent_position != passenger[:2])(state)):
        return move_to_cell(passenger_state[0], passenger_state[1], state)
    return actions["pickup"]

# dropoff passenger
def dropoff_passenger(passenger, state):
    passenger_state = passenger(state)
    if ((passenger[2:4] != agent_position)(state)):
        return move_to_cell(passenger_state[2], passenger_state[3], state) # go to destination
    return actions["dropoff"]

import numpy as np
from lmdp.grounding import State
terminal_state = State(np.array((4,1,0,2,2,2,1,2,1,0,4,1,4,1,0)))
passenger_1_in_dest = (passenger_1_dest == passenger_1_pos)
# assert (passenger_1_in_dest & bool_not(passenger_1_intaxi))(terminal_state) == True



taxi_mdp = TaxiOOMDP(WIDTH, HEIGHT, agent=agent, passengers=passengers, walls=walls)

taxi_states = partial(taxi_state_generator, WIDTH, HEIGHT, passengers, walls)
# for s in taxi_state_generator(5,5,passengers, walls):
#     print(s)

