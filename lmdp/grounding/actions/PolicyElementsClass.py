'''
    Policy Grounding Class
        based on Partial Functions.
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: January 2021
'''
import sys, os
sys.path.append(os.path.abspath("./"))

from lmdp.grounding.actions.PolicyGroundingClass import Policy
from lmdp.grounding.actions.PolicyFromDictClass import PolicyFromDict
from lmdp.grounding.PartialFunctionClass import PartialFunction


class PolicyElements(PartialFunction):
    def __init__(self, policy=[]):
        PartialFunction.__init__(self, domain=["state"], codomain=["action"])
        for p in policy:
            self.add(p[0], p[1])

    def add(self, symbol, action):
        self.add_specification(symbol, action)


if __name__ == "__main__":
    from lmdp.grounding.states.StateGroundingClass import StateFactor
    from lmdp.grounding.states.SymbolClass import Symbol
    from lmdp.grounding.actions.DiscreteActionGroundingClass import DiscreteActionGrounding
    
    import numpy as np
    from simple_rl.tasks import GridWorldMDP
    from simple_rl.tasks import GridWorldState
    
    # 2-dimension state vector in gridworld
    x = StateFactor(0, "x")
    y = StateFactor(1, "y")
    position = StateFactor([0, 1], "position")
    diagonal = Symbol(x == y, "diagonal")
    goal = Symbol(position == np.array([10, 10]), "goal")
    not_goal = Symbol(position != np.array([10, 10]))


    # Actions in gridworld
    up = DiscreteActionGrounding("up", "up")
    down = DiscreteActionGrounding("up", "up")
    right = DiscreteActionGrounding("right", 'right')
    left = DiscreteActionGrounding("left", "left")

    policy = PolicyElements([(not_goal, up)])
    policy.add(diagonal, up)

    s1 = GridWorldState(1, 1)
    s2 = GridWorldState(0, 1)

    print(f"{policy(s1)} == 'up'")
