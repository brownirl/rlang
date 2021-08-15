'''
    Policy Grounding Class
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: v0 August 2020
          v1 January 2021
'''
from rlang.src.lmdp.grounding.actions.ActionGroundingClass import ActionGrounding
from rlang.src.lmdp.grounding.GroundingClass import Grounding
from rlang.src.lmdp.grounding.expressions.ExpressionsClass import Expression


class Policy(Grounding, Expression):

    def __init__(self, policy, name="policy"):
        self.policy_fun = policy
        Grounding.__init__(self, name=name)
        Expression.__init__(self, self.policy_fun, domain=["state"], codomain=["action"], name=name)

    def __repr__(self):
        return Grounding.__repr__(self)
