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
import functools

def _policy(execute_f, do_not_execute_f, name): # adapt to partial function
    def _policy_f(state):
        a, d_a = None, None
        if execute_f is not None:
            a = execute_f(state)
        if do_not_execute_f is not None:
            d_a = do_not_execute_f(state)
        return (a, d_a)
    return Policy(_policy_f, name=name)

class PolicyElements(PartialFunction):
    counter = 0
    def __init__(self, policy=[]):
        PartialFunction.__init__(self, domain=["state"], codomain=["action"])
        for p in policy:
            self.add(p[0], p[1])

    def add(self, symbol, action_pair):
        '''
            args:
                action_pair: (action_to_execute, action_not_execute)
        '''
        self.add_specification(symbol, _policy(*action_pair, name=f'p_element_{PolicyElements.counter}'))
        PolicyElements.counter += 1
    
    def execute(self, symbol, action):
        self.add(symbol, (action, None))
        
    def do_not_execute(self, symbol, action):
        self.add(symbol, (None, action))


all = ['PolicyElements']


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

    policy = PolicyElements([(not_goal, (up, None))])
    policy.execute(diagonal, up)
    policy.do_not_execute(diagonal, down)

    s1 = GridWorldState(1, 1)
    s2 = GridWorldState(0, 1)

    print(f"{policy(s1)} == 'up'")
