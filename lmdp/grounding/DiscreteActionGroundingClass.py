'''
    Grounding for Discrete Actions
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: August 2020
'''

from ActionGroundingClass import ActionGrounding

class DiscreteActionGrounding(ActionGrounding):

    def __init__(self, mdp_action, name=None):
        if (name is None):
            name = "discrete-action-" + str(ActionGrounding.counter)
        ActionGrounding.__init__(self, name )
        self.__mdp_action = mdp_action

    def __call__(self, *args):
        return self.__mdp_action


if __name__ == "__main__":
    down = DiscreteActionGrounding("down")
    up = DiscreteActionGrounding("up")
    print(f"action {up.name}: {up()}")