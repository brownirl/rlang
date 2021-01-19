'''
    Abstract class for Action Grounding
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: August 2020
'''

from lmdp.grounding.GroundingClass import Grounding
from lmdp.grounding.expressions.ExpressionsClass import Expression

class ActionGrounding(Grounding, Expression):
    counter = 0
    def __init__(self, action_function, name=None):
        if (name is None):
            name = "action-" + str(ActionGrounding.counter)
        Grounding.__init__(self, name)
        Expression.__init__(self, action_function, domain=["state"], codomain=["action"])
        ActionGrounding.counter += 1