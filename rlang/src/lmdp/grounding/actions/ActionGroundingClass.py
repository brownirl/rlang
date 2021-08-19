'''
    Abstract class for Action Grounding
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: v0 August 2020
          v1 January 2021
'''

from rlang.src.lmdp.grounding.GroundingClass import Grounding
from rlang.src.lmdp.grounding.expressions.ExpressionsClass import Expression


class ActionGrounding(Expression, Grounding):
    counter = 0

    def __init__(self, action_function, name=None):
        if (name is None):
            name = "action-" + str(ActionGrounding.counter)
        Grounding.__init__(self, name)
        Expression.__init__(self, action_function, domain=[], codomain=["action"], name=name)
        ActionGrounding.counter += 1
