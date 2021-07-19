'''
    Effect Predicate class
        - This class defines a set of states parameterized by a (state, action)
          pair.
    author: Rafael Rodriguez-Sanchez
    date: v0 September 2020
          v1 January 2021
'''
import sys, os

sys.path.append(os.path.abspath("/"))

from lmdp.grounding.states.PredicateClass import Predicate
from lmdp.grounding.expressions.ExpressionsClass import Expression
from functools import partial


class EffectSymbol(Expression):
    def __init__(self, boolean_fun):
        # if (name is None):
        #     name = "effect-symbol-" + str(Predicate.counter)
        # Predicate.__init__(self, boolean_fun, name)
        # self.__fun = boolean_fun  
        self._boolean_fun = boolean_fun
        Expression.__init__(self, self._boolean_fun, domain=["state", "action", "next_state"], codomain=["boolean"])

    # def executor(self, state, action):
    #     return partial(self._boolean_fun, state, action)


if __name__ == '__main__':
    from simple_rl.mdp.StateClass import State
    from lmdp.grounding.states.NextStateGroundingClass import next_state
    from lmdp.grounding import StateFactor

    import numpy as np

    # x = StateFactor(0, "x")
    # s = State(data=np.array([1,0]))
    # s_prime = State(data= np.array([2,1]))
    # s_prime_1 = State(data=np.array([1, 1]))

    # up = EffectSymbol(next_state(x) == x + 1)(s, "up")
    # print(f"{up(s_prime)} == True")
