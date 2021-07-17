'''
    Grounding for Discrete Actions
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: August 2020
'''

from lmdp.grounding.actions.ActionGroundingClass import ActionGrounding
from lmdp.grounding.booleans.BooleanFunClass import BooleanExpression
from lmdp.grounding.expressions.ExpressionsClass import Expression


class DiscreteActionGrounding(ActionGrounding):

    def __init__(self, mdp_action, name=None):
        if (name is None):
            name = "discrete-action-" + str(ActionGrounding.counter)
        ActionGrounding.__init__(self, lambda **args: mdp_action, name)
        self.__mdp_action = mdp_action

    def __eq__(self, other):
        if (isinstance(other, ActionGrounding) or isinstance(other, Expression)):
            return BooleanExpression(lambda **args: self.__call__(**args) == other(**args), domain=["action"])
        else:
            return NotImplemented


if __name__ == "__main__":
    down = DiscreteActionGrounding("down")
    up = DiscreteActionGrounding("up")
    print(f"action {up.name}: {up()} == up")
    print(f"action {down.name}: {down()} == down")
