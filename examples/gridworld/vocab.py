import sys, os
sys.path.append(os.path.abspath("./"))
from simple_rl.tasks.grid_world.GridWorldMDPClass import GridWorldMDP
from lmdp.grounding import *
from lmdp.grounding.states.StateClass import State, BatchedState

# MDP parameters
width, height = 6,6
lava_locs=[(3,2), (1,4), (2,4), (2,5)]
walls=[(3, 1)]
goal_locs=[(5,1)]

#### Factors
position = StateFactor([0,1], "position") # definition of new factor.
x, y = position[0], position[1]


### Symbols
goal = Symbol(bool_and(x == 5, y == 1))
wall = Symbol(bool_and(x == 3, y == 1))
lava = Symbol(position.in_(lava_locs))

### Effects
@effect
def effect_action(state, action): # actions effects on state/Transition Dynamics
        if action == 'up':
            return position(state) + (0,1)
        if action == 'down':
            return position(state) + (0,-1)
        if action == 'left':
            return position(state) + (-1, 0)
        if action == 'right':
            return position(state) + (1, 0)

# effect_action = PredictiveEffect(bool_and(any_state, any_action), action_effect)

mdp = GridWorldMDP(width, height, walls=walls, lava_locs=lava_locs, goal_locs=goal_locs, slip_prob=0.33, step_cost=0)