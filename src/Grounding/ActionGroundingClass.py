'''
    Abstract class for Action Grounding
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: August 2020
'''

from GroundingClass import Grounding

class ActionGrounding(Grounding):
    counter = 0
    def __init__(self, name=None):
        if (name is None):
            name = "action-" + str(ActionGrounding.counter)
        Grounding.__init__(self, name)
        ActionGrounding.counter += 1

    def __call__(self, *args):
        pass