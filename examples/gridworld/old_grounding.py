import sys, os

from grounding.expressions.ExpressionsClass import S
from lmdp.grounding.states.StateGroundingClass import StateFactor

sys.path.append(os.path.abspath("./"))
from simple_rl.tasks.grid_world.GridWorldMDPClass import GridWorldMDP
from lmdp import *

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

effect_action = PredictiveEffect(bool_and(any_state, any_action), action_effect)

mdp = GridWorldMDP(width, height, walls=walls, lava_locs=lava_locs, goal_locs=goal_locs, slip_prob=0.33, step_cost=0)

lmdp = LMDP(mdp, factor_names=["x", "y"])

 # how to convert this to RLang and was there a reason why it wasn't in the grounding/vocab file? 
 # Is there a way to separate lmdp from the following effects if we make when into a keyword for a conditional / is it possible to express them as effects? 
 
with lmdp.when(lava @ effect_action) as c: # when you fall in lava (@ is the function composition operator)
    c.reward(-1)
with c.otherwise().when(goal @ effect_action): # otherwise when in goal
    c.reward(1)
with lmdp.when(wall @ effect_action) as c: # when the action taken takes you to a wall position 
    c.effect(S) # next state is the current state
with lmdp.when(bool_and(any_state, any_action)) as c:
    c.effect(effect_action)