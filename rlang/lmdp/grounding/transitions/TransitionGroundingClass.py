'''
    Grounding for (deterministic) Transitions specifications
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: August 2020
'''

from lmdp.grounding.GroundingClass import Grounding
from lmdp.grounding.PartialFunctionClass import PartialFunction
from lmdp.grounding.booleans.BooleanFunClass import BooleanExpression
from collections import defaultdict


class TransitionGrounding(Grounding, PartialFunction):

    def __init__(self, transitions=[], name=None):
        '''
            Args:
                -transitions: list of triples (symbol, action, EffectSymbol) 
        '''
        if (name is None):
            name = 'transitions'
        Grounding.__init__(self, name)
        PartialFunction.__init__(self, domain=["state", "action"], codomain=["set_of_states"])
        for t in transitions:
            self.add(*t)  # initialize transitions

    def __call__(self, state, action):
        '''
            Given a (state, action) pair, it returns a symbol corresponding 
            to the next state (list)
        '''
        return super().__call__(state, action)

    def add(self, boolean_expression_sa, action=None, effect=None):
        '''
            add a new transition
            Args:
                - symbol (starting symbol)
                - action 
                - Effect Predicate
        '''
        if (effect is None):
            raise "Effect must be specified"
        if (action is not None):
            boolean_cond = BooleanExpression(lambda **args: boolean_expression_sa(**args) and args["action"] == action,
                                             domain=["state", "action"])
        else:
            boolean_cond = boolean_expression_sa
        self.add_specification(boolean_cond, effect)

    # def __create_dict(self, transitions):
    #     self.__transitions = defaultdict(lambda: defaultdict())
    #     for (symbol, action, symbol_next) in transitions:
    #         self.__transitions[symbol][action] = symbol_next


if __name__ == "__main__":
    from simple_rl.mdp.StateClass import State
    from lmdp.grounding.states.NextStateGroundingClass import next_state
    from lmdp.grounding import StateFactor
    from lmdp.grounding.booleans.BooleanFunClass import any_state, any_action
    from lmdp.grounding.states.Effect import Effect
    import numpy as np

    x = StateFactor(0, "x")
    s = State(data=np.array([1, 0]))
    s_prime = State(data=np.array([2, 1]))
    s_prime_1 = State(data=np.array([1, 1]))
    up = Effect(any_state and any_action, next_state(x) == x + 1)

    transition = TransitionGrounding([(any_state, 'up', up)])

    print(f"{transition(s, 'up')[0](s_prime)} == True")
