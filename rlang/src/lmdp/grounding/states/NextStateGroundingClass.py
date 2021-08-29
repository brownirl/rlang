'''
    Next State Grounding class
        - Wrapper for State Grounding that allows to ground names
        to the 'next state' of a transition tuple (s, s')
    author: Rafael Rodriguez-Sanchez
    date: January 2021
'''
import sys, os

sys.path.append(os.path.abspath("/"))
from lmdp.utils.expression_utils import Domain
from lmdp.grounding.states.StateGroundingClass import StateFactor, StateFeature
from lmdp.grounding.real.RealExpressionClass import RealExpression
from lmdp.grounding.booleans.BooleanFunClass import BooleanExpression
from lmdp.grounding.states.PredicateClass import Predicate


class NextStatePredicate(Predicate, BooleanExpression):
    def __init__(self, symbol):
        self._symbol = symbol
        self._domain = Domain(["next_state"])
        BooleanExpression.__init__(self, self.executor, domain=["next_state"])

    def executor(self, next_state):
        return self._symbol(next_state)


class NextStateGrounding(StateFactor, RealExpression):
    def __init__(self, state_grounding):
        """ 
        Wrapper for State Grounding that grounds names
        to the 'next state' of a transition tuple (s, s')
        
        Args:
            state_grounding (StateFactor, StateFeature): [description]
        """
        self._domain = Domain(["next_state"])
        self.__state_grounding = state_grounding
        RealExpression.__init__(self, self.executor, domain=["next_state"])

    def executor(self, next_state):
        # if (len(args) < 2):
        #     raise "Error: Arguments must (s, s') or you should set current state"
        # else:
        #     next_state = args[1] # second argument must be s'

        return self.__state_grounding(next_state)

    @property
    def domain(self):
        return self._domain

    def number_of_features(self):
        return self.__state_grounding.number_of_features()

    def dim(self):
        return self.__state_grounding.dim()

    @property
    def domain(self):
        return self._domain

    def real_expression(self):
        return RealExpression(self, dimension=self.number_of_features(), domain=["next_state"])


def next_state(grounding):
    if (isinstance(grounding, Predicate)):
        return NextStatePredicate(grounding)
    elif (isinstance(grounding, (StateFactor, StateFeature))):
        return NextStateGrounding(grounding)


if __name__ == '__main__':
    from simple_rl.mdp.StateClass import State
    import numpy as np

    x = StateFactor(0, "x")
    s = State(data=np.array([1, 0]))
    s_prime = State(data=np.array([2, 1]))

    f = next_state(x) == x + 1
    g = next_state(x) - 1 == x

    print(f(s, s_prime))
    print(g(s, s_prime))
