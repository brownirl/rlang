'''
    RLang-informed Value Iteration with Options
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: January 2021

'''
from lmdp.agents.LangAgentClass import LangAgent
from simple_rl.planning.ValueIterationClass import ValueIteration
from simple_rl.abstraction.AbstractValueIterationClass import AbstractValueIteration as AVI
from simple_rl.abstraction.action_abs.ActionAbstractionClass import ActionAbstraction

class AAValueInteration(LangAgent):

    def __init__(self, mdp, lmdp, vi_sample_rate=5, max_iterations=1000, amdp_sample_rate=5, delta=0.001, max_rollout=1000):
        aa = _subpolicies_to_aa(lmdp.get_subpolicies(), mdp.get_actions())
        agent = AVI(mdp, action_abstr=aa, max_iterations=max_iterations, vi_sample_rate=vi_sample_rate, amdp_sample_rate=amdp_sample_rate, delta=delta, max_rollout=max_rollout)
        LangAgent.__init__(self, agent, lmdp)

def _subpolicies_to_aa(subpolicies, primitive_actions):
    o = []
    for s in subpolicies:
        o.append(s.to_option())

    return ActionAbstraction(options=o, prim_actions=primitive_actions, prims_on_failure=True)