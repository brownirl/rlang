"""
    Predicate grounding class
        - Represents a factor of state
    author: Benjamin Spiegel (bspiegel@cs.brown.edu), Jennifer Wang
    date: August 2021
"""

from __future__ import annotations
from typing import Callable
from rlang.src.grounding.groundings.state.state_grounding_function import StateGroundingFunction
from rlang.src.grounding.utils.domain import Domain
from rlang.src.grounding.utils.grounding_errors import RLangGroundingError


class Predicate(StateGroundingFunction):
    def __init__(self, function: Callable, name: str = None):
        super().__init__(function=function, codomain=Domain.BOOLEAN, name=name)

    def __and__(self, other) -> Predicate:
        if isinstance(other, Predicate):
            return Predicate(function=lambda *args, **kwargs:
                             self(*args, **kwargs) & other(*args, **kwargs))
        if isinstance(other, bool):
            return self if other else Predicate(function=lambda *args, **kwargs: False)
        raise RLangGroundingError(message=f"Cannot & a Predicate with a {type(other)}")

    def __rand__(self, other):
        self.__and__(other)

    def __or__(self, other) -> Predicate:
        if isinstance(other, Predicate):
            return Predicate(function=lambda *args, **kwargs:
                             self(*args, **kwargs) | other(*args, **kwargs))
        if isinstance(other, bool):
            return self if not other else Predicate(function=lambda *args, **kwargs: True)
        raise RLangGroundingError(message=f"Cannot | a Predicate with a {type(other)}")

    def __invert__(self) -> Predicate:
        return Predicate(function=lambda *args, **kwargs: bool(~ self(*args, **kwargs)))

    def __repr__(self):
        return "<Predicate>"


class Goal(Predicate):
    pass    # A Goal is simply a Predicate.
    # We may want to add a constructor which accepts a Predicate
