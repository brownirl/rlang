import sys, os
sys.path.append(os.path.abspath("./"))

# envs
from simple_rl.tasks.grid_world.GridWorldMDPClass import GridWorldMDP

#agents
from lmdp.agents import RMaxLangAgent, RMaxAgent, RandomAgent

#lmdp
import lmdp as rlang
from lmdp.experiment_runner import *
from lmdp.utils.StateSpaceGenClass import StateSpaceGen
from lmdp.experiment_runner import run_agents

mdp = GridWorldMDP(width=5, height=5, walls=[(3, 1)], lava_locs=[(3,2)], goal_locs=[(5,1)])

glmdp = rlang.LMDP(mdp, factor_names=["x", "y"])
goal = rlang.Symbol((glmdp.state("x") == 5).and_(glmdp.state("y") == 1))
wall = rlang.Symbol((glmdp.state("x") == 3).and_(glmdp.state("y") == 1))
goal_row = rlang.Symbol(glmdp.state("y") == 5)


glmdp.reward.add(goal_row, 0.1)
glmdp.reward.add(wall, -1)
glmdp.reward.add(goal, 1)

lang_rmax_agent = RMaxLangAgent(mdp.get_actions(), lmdp=glmdp)
lang_rmax_agent.update_from_lang()

random = RandomAgent(mdp.get_actions())
rmax_agent = RMaxAgent(mdp.get_actions())

run_agents([lang_rmax_agent, rmax_agent], mdp)


