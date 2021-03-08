import sys, os
sys.path.append(os.path.abspath("./lmdp"))


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
passengers = [{"x":4, "y":4, "dest_x":1, "dest_y":1, "in_taxi":0}]#, {"x":3, "y":2, "dest_x":4, "dest_y":1, "in_taxi":0}]
walls = [{"x": 2, "y": 2}]

## Utils
passenger_n_features = len(passengers[0])
wall_n_features = len(walls[0])
agent_n_features = len(agent)

#### VOCABULARY

#-----factors
# agent

agent_state = StateFactor(list(range(agent_n_features)), name="agent")

# walls
walls_state = {}
init_idx = agent_n_features
for i in range(len(walls)):
    walls_state.update({"wall_"+str(i): 
                        StateFactor(list(range(init_idx, init_idx + (i+1)*wall_n_features)), "wall_"+str(i))})
    init_idx += i*wall_n_features
# passengers
passenger_state = {}
for p in range(len(passengers)):
    passenger_state["passenger_"+str(p)] = StateFactor(list(range(init_idx, agent_n_features + (p+1)*passenger_n_features)), "passenger_"+str(p))
    init_idx += p*passenger_n_features

locals().update(walls_state)
locals().update(passenger_state)

#-----features 
passenger_pos_dest= {}
for name, passenger in passenger_state.items():
    passenger_pos_dest.update({name + "_pos": passenger[:2]})
    passenger_pos_dest.update({name + "_dest": passenger[2:4]})
    passenger_pos_dest.update({name +"_intaxi": passenger[4]})

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
    d = agent_position(state) - np.array((x, y)) # manhattan distance
    if(abs(d[0]) + abs(d[1]) > 0):
        if(d[0] != 0):
            return actions["right"] if d[0] < 0 else actions["left"]
        else:
            return actions["up"] if d[1] < 0 else actions["down"]

# pickup passenger (parameterized options)
def pick_up_passenger(passenger, state):
    passenger_state = passenger(state)
    if (agent_position(state) != passenger_state[:2]):
        return move_to_cell(passenger_state[0], passenger_state[1], state)
    return actions["pickup"]

# dropoff passenger
def dropoff_passenger(passenger, state):
    passenger_state = passenger(state)
    if (agent_position(state) != passenger_state[2:4]):
        return move_to_cell(passenger_state[2], passenger_state[3], state) # go to destination
    return actions["dropoff"]



taxi_mdp = TaxiOOMDP(WIDTH, HEIGHT, agent=agent, passengers=passengers, walls=walls)

taxi_states = partial(taxi_state_generator, WIDTH, HEIGHT, passengers, walls)