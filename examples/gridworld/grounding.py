import sys, os
sys.path.append(os.path.abspath("./"))
from simple_rl.tasks.grid_world.GridWorldMDPClass import GridWorldMDP
from lmdp.grounding import *
from lmdp.grounding.states.StateClass import State, BatchedState
from lmdp import *

# MDP parameters
width, height = 6,6
lava_locs=[(3,2), (1,4), (2,4), (2,5)]
walls=[(3, 1)]
goal_locs=[(5,1)]

mdp = GridWorldMDP(width, height, walls=walls, lava_locs=lava_locs, goal_locs=goal_locs, slip_prob=0.33, step_cost=0)

lmdp = LMDP(mdp, factor_names=["x", "y"])