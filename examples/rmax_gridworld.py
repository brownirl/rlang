import sys, os
sys.path.append(os.path.abspath("./"))

# envs
from simple_rl.tasks.grid_world.GridWorldMDPClass import GridWorldMDP
from simple_rl.tasks.grid_world.GridWorldStateClass import GridWorldState
#agents
from lmdp.agents import RMaxLangAgent, RMaxAgent, RandomAgent
#lmdp
from lmdp import *
from lmdp.experiment_runner import *
from lmdp.experiment_runner import run_agents
from functools import partial

import numpy as np

def gridworld_state_space(width, height): # state space iterator
    for x in range(1,width+1):
        for y in range(1, height+1):
            yield GridWorldState(x, y)

def action_effect(state, action): # actions effects on state/Transition Dynamics
        if action == 'up':
            return  GridWorldState(state.x, state.y + 1)
        if action == 'down':
            return  GridWorldState(state.x, state.y-1)
        if action == 'left':
            return GridWorldState(state.x - 1, state.y)
        if action == 'right':
            return GridWorldState(state.x + 1, state.y)

if __name__ == "__main__":
    width, height = 6,6
    lava_locs=[(3,2), (1,4), (2,4), (2,5)]
    walls=[(3, 1)]
    goal_locs=[(5,1)]
    mdp = GridWorldMDP(width, height, walls=walls, lava_locs=lava_locs, goal_locs=goal_locs, slip_prob=0)

    #### 
    lmdp = LMDP(mdp, factor_names=["x", "y"])
    lmdp.add(StateFactor([0,1], "position")) # definition of new factor.

    ### Prior Info
    goal = lmdp.add(Symbol(bool_and(lmdp("x") == 5, lmdp("y") == 1)))
    wall = lmdp.add(Symbol(bool_and(lmdp("x") == 3, lmdp("y") == 1)))
    lava = Symbol(lambda state: (lmdp("x")(state), lmdp("y")(state)) in lava_locs) # TODO: Improve this
    effect_action = PredictiveEffect(bool_and(any_state, any_action), action_effect)
    
    with lmdp.when(lava @ effect_action) as c: # when you fall in lava (@ is the function composition operator)
        c.reward(-1.1)
    with c.otherwise().when(goal @ effect_action ): # otherwise when in goal
        c.reward(0.9)
    with c.otherwise(): # any other case is step cost
        c.reward(-.1)

    #### Run agents
    lang_rmax_agent = RMaxLangAgent(mdp.get_actions(), lmdp=lmdp,  s_a_threshold=10)
    lang_rmax_agent.update_from_lang(partial(gridworld_state_space, width, height))

    random = RandomAgent(mdp.get_actions())
    rmax_agent = RMaxAgent(mdp.get_actions(), s_a_threshold=10)

    run_agents([lang_rmax_agent, rmax_agent], mdp)


