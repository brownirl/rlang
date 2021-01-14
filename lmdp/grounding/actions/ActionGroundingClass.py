'''
    Abstract class for Action Grounding
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: August 2020
'''

from lmdp.grounding.GroundingClass import Grounding

class ActionGrounding(Grounding):
    counter = 0
    def __init__(self, action_function, name=None):
        if (name is None):
            name = "action-" + str(ActionGrounding.counter)
        Grounding.__init__(self, name, domain=["Action"])
        ActionGrounding.counter += 1
        self.action_function = action_function

    def __call__(self, *args):
        return self.action_function(*args)