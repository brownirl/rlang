"""
    Predicate grounding class
        - Represents a factor of state
    author: Benjamin Spiegel (bspiegel@cs.brown.edu), Jennifer Wang
    date: August 2021
"""
from __future__ import annotations
from typing import Callable

from grounding.groundings import state
from rlang.src.grounding.groundings.grounding_function import GroundingFunction
from rlang.src.grounding.utils.domain import Domain

class Predicate(GroundingFunction):
    def __init__(self, function: Callable, name: str = None):
        self._function = function
        super().__init__(domain=Domain.STATE, codomain=Domain.BOOLEAN, name=name)

    def __call__(self, *args, **kwargs):
        return self._function(*args, **kwargs)     # TODO: it's unclear whether we need to support keywords

# TODO: Implement __and__, __or__, and __not__ composition
# TODO: Implement __repr__, __eq__, __lt__, etc.

    def __and__(self, other):
        if isinstance(other, Predicate):
            return Predicate(function=lambda *args, **kwargs: self(*args, **kwargs) and other(*args, **kwargs))
        if isinstance(other, bool):
            return Predicate(function=lambda *args, **kwargs: self(*args, **kwargs) and bool)
        #TODO: raise error
        
    
    def __or__(self, other):
        pass




    
    ### CONSTANTS #####
BOOL_TRUE = Predicate(function=lambda *args, **kwargs: True)
BOOL_FALSE = Predicate(function=lambda *args, **kwargs: False)

if __name__ == "__main__":
    from rlang.src.grounding import State
    x = Predicate(function=lambda state: state == State(3))
    s1 = State(3)
    print(x(s1))
    test1 = Predicate(lambda *args, **kwargs: 1 != 1)
    print(test1())
    # false_and_false = BOOL_FALSE & (BOOL_FALSE)
    # true_and_false = BOOL_TRUE & (BOOL_FALSE)
    # false_and_true = BOOL_FALSE & (BOOL_TRUE)
    # true_and_true = BOOL_TRUE & (BOOL_TRUE)
    # print((true_and_true & False)())
    # print(false_and_false())
    # print(true_and_false())
    # print(false_and_true())
    # print(true_and_true())

class Goal(Predicate):
    pass    # A Goal is simply a Predicate. We may want to add a constructor which accepts a Predicate