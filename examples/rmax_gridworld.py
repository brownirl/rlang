import sys, os
sys.path.append(os.path.abspath("./"))

# envs
from simple_rl.tasks.grid_world.GridWorldMDPClass import GridWorldMDP

#agents
from lmdp.agents import RMaxLangAgent, RMaxAgent, RandomAgent

#lmdp
from lmdp import *
from lmdp.experiment_runner import *
from lmdp.utils.StateSpaceGenClass import StateSpaceGen
from lmdp.experiment_runner import run_agents

mdp = GridWorldMDP(width=5, height=5, walls=[(3, 1)], lava_locs=[(3,2)], goal_locs=[(5,1)])

glmdp = LMDP(mdp, factor_names=["x", "y"])
goal = glmdp.add(Symbol((glmdp("x") == 5).and_(glmdp("y") == 1)))
wall = glmdp.add(Symbol((glmdp("x") == 3).and_(glmdp("y") == 1)))
goal_row = glmdp.add(Symbol(glmdp("y") == 5))

with glmdp.when(goal_row) as c:
    c.reward(0.1)

with glmdp.when(wall) as c:
    c.reward(-1)

glmdp.reward.add(goal, 1)

lang_rmax_agent = RMaxLangAgent(mdp.get_actions(), lmdp=glmdp)
lang_rmax_agent.update_from_lang()

random = RandomAgent(mdp.get_actions())
rmax_agent = RMaxAgent(mdp.get_actions())

run_agents([lang_rmax_agent, rmax_agent], mdp)


