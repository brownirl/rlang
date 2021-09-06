"""
    Predicate grounding class
        - Represents a factor of state
    author: Benjamin Spiegel (bspiegel@cs.brown.edu), Jennifer Wang
    date: August 2021
"""

from __future__ import annotations
from typing import Callable
from rlang.src.grounding.groundings.grounding_function import GroundingFunction
from rlang.src.grounding.utils.domain import Domain


class Predicate(GroundingFunction):
    def __init__(self, function: Callable, name: str = None):
        self._function = function
        super().__init__(domain=Domain.STATE, codomain=Domain.BOOLEAN,
                         name=name)

    def __call__(self, *args, **kwargs):
        return self._function(*args, **kwargs)
        # TODO: it's unclear whether we need to support keywords

# TODO: Implement __and__, __or__, and __not__ composition
# TODO: Implement __repr__, etc.

    def __and__(self, other) -> Predicate:
        if isinstance(other, Predicate):
            return Predicate(function=lambda *args, **kwargs:
                             self(*args, **kwargs) and other(*args, **kwargs))
        if isinstance(other, bool):
            return Predicate(function=lambda *args, **kwargs:
                             self(*args, **kwargs) and bool)
        # TODO: raise error

    def __or__(self, other) -> Predicate:
        if isinstance(other, Predicate):
            return Predicate(function=lambda *args, **kwargs:
                             self(*args, **kwargs) or other(*args, **kwargs))
        if isinstance(other, bool):
            return Predicate(function=lambda *args, **kwargs:
                             self(*args, **kwargs) or bool)
        # TODO: raise error

    def __invert__(self) -> Predicate:
        return Predicate(function=lambda *args, **kwargs:
                         not self(*args, **kwargs))

    def __bool__(self, *args, **kwargs) -> bool:
        if self(*args, **kwargs):
            return True
        return False

    def __repr__(self):
        return "<Predicate>"


class Goal(Predicate):
    pass    # A Goal is simply a Predicate.
    # We may want to add a constructor which accepts a Predicate
