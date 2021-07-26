import sys, os
sys.path.append(os.path.abspath("./"))
from simple_rl.tasks.grid_world.GridWorldMDPClass import GridWorldMDP
from lmdp.grounding import *
from lmdp.grounding.states.StateClass import State, BatchedState
from lmdp import *
from lmdp.grounding.states.StateGroundingClass import StateFactor

# This is included for testing purposes
position_test = StateFactor([0, 1], "position_test")