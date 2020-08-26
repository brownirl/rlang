'''
    Grounding for Discrete Actions
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: August 2020
'''

from GroundingClass import Grounding

class DiscreteActionGrounding(Grounding):
    counter = 0
    def __init__(self, mdp_action, name=None):
        if (name is None):
            name = "action-" + str(DiscreteActionGrounding.counter)
        Grounding.__init__(self, name )
        DiscreteActionGrounding.counter += 1
        self.__mdp_action = mdp_action

    def __call__(self, *args):
        return self.__mdp_action


if __name__ == "__main__":
    up = DiscreteActionGrounding("up", name="up")
    print(f"action up: {up()}")