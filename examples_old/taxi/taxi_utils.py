import numpy as np

from simple_rl.tasks import TaxiOOMDP, TaxiState
from simple_rl.mdp.oomdp.OOMDPObjectClass import OOMDPObject
from functools import partial, reduce
from collections import deque
import copy

def position_generator(width, height): 
    for x in range(1,width+1):
        for y in range(1, height+1):
            yield (x, y)


def taxi_state_generator(width, height, passengers_init, walls): # state space iterators
    passenger_idx = dict(enumerate(passengers_init))
    passenger_position_generators = dict(map(lambda p: (p, partial(position_generator, width, height)), range(len(passengers_init))))
    
    for agent_position in position_generator(width, height):
        passengers = list(reversed(list(range(len(passengers_init)))[1:]))
        active_generators = [(0, passenger_position_generators[0]())]
        state = [agent_position] + [0] * len(passengers_init)
        while len(active_generators) > 0:
            p, gen = active_generators.pop()
            try:
                state[p+1] = next(gen)
            except StopIteration:
                passengers.append(p)
                continue
            active_generators.append((p, gen))
            
            if len(passengers) > 0: # there are more variable to unroll
                p = passengers.pop()
                gen = passenger_position_generators[p]()
                active_generators.append((p, gen))
            else:
                for s in __taxi_state_tuple(state, passengers_init, walls):
                    yield s



def __taxi_state(state, passengers, walls):
    object_classes = ("agent", "wall", "passenger")
    agent_attributes = ("x", "y", "has_passenger")
    passenger_attributes = ("x", "y", "dest_x", "dest_y", "in_taxi")
    agent = state[0]+(0,) # has no passenger
    a_states = [dict(zip(agent_attributes, agent))]
    p_states = []
    p_states_2 = []

    objects = []

    for i, p in enumerate(passengers):
        p_state = state[i+1] + tuple((p[i] for i in ("dest_x", "dest_y"))) + (0,)
        p_states.append(dict(zip(passenger_attributes, p_state)))

    objects.append([a_states, walls, p_states])
    for i, p in enumerate(p_states):
        # Add state that has passenger in taxi_efficient_rl
        if agent[0]== p["x"] and agent[1] == p["y"]:
            o = [[dict(zip(agent_attributes, copy.deepcopy(agent)[:-1] + (1,)))], walls]
            p_states_2 = copy.deepcopy(p_states)
            p_states_2[i]["in_taxi"] = 1 #dict(zip(passenger_attributes, p[:-1] + (1,))) # ith passenger in taxi_efficient_rl
            o.append(p_states_2)
            objects.append(o)
    # objects = zip(a_states, [walls, walls], [p_states, p_states_2])
    return map(lambda o : TaxiState(__oomdp_objects_from_dicts(zip(object_classes, o))), objects)
            
def __oomdp_objects_from_dicts(Object):
    o = {}
    for name, obj in Object:
         o[name] = [OOMDPObject(attributes=o_dict, name=name) for o_dict in obj]
    return o

def __taxi_state_tuple(state, passengers, walls):
    # object_classes = ("agent", "wall", "passenger")
    # agent_attributes = ("x", "y", "has_passenger")
    # passenger_attributes = ("x", "y", "dest_x", "dest_y", "in_taxi")
    agent = state[0]+(0,) # has no passenger
    # a_states = [dict(zip(agent_attributes, agent))]
    p_states = []
    p_states_2 = []

    objects = []
    w_ = tuple(reduce(lambda x, y: x+y, [w.values() for w in walls]))
    for i, p in enumerate(passengers):
        p_state = state[i+1] + tuple((p[i] for i in ("dest_x", "dest_y"))) + (0,)
        p_states.append(p_state)
    p_ = tuple(reduce(lambda x, y: x+y, [p for p in p_states]))
    objects.append(agent + w_ + p_)
    for i, p in enumerate(p_states):
        # Add state that has passenger in taxi_efficient_rl
        if agent[0]== p[0] and agent[1] == p[0]:
            o = copy.deepcopy(agent)[:-1] + (1,) + w_
            p_states_2 = copy.deepcopy(p_states)
            p_states_2[i] = p_states_2[i][:-1] + (1,0) #dict(zip(passenger_attributes, p[:-1] + (1,))) # ith passenger in taxi_efficient_rl
            p_ = tuple(reduce(lambda x, y: x+y,[p for p in p_states]))
            o = o + p_
            objects.append(o)
    return objects
    # objects = zip(a_states, [walls, walls], [p_states, p_states_2])

    