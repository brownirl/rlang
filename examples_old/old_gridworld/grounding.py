import sys, os
from grounding.groundings.state.factor import Factor
sys.path.append(os.path.abspath("./"))
from simple_rl.tasks.grid_world.GridWorldMDPClass import GridWorldMDP
from lmdp.grounding import *
from lmdp.grounding.states.StateClass import State, BatchedState
from lmdp import *
from lmdp.grounding.states.StateGroundingClass import StateFactor


# This is included for testing purposes
position_test = Factor([0, 1], "position_test")
position_test_2 = Factor([0, 1], "position_test_2")