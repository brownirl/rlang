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

# effect_action = PredictiveEffect(bool_and(any_state, any_action), action_effect)

# how to convert bool_and(any_state, any_action) and c.effect(effect_action) into rlang?

# with lmdp.when(lava @ effect_action) as c: # when you fall in lava (@ is the function composition operator)
#     c.reward(-1)
# with c.otherwise().when(goal @ effect_action): # otherwise when in goal
#     c.reward(1)
# with lmdp.when(wall @ effect_action) as c: # when the action taken takes you to a wall position 
#     c.effect(S) # next state is the current state
# with lmdp.when(bool_and(any_state, any_action)) as c:
#     c.effect(effect_action)