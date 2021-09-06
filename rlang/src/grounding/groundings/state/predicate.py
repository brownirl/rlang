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
from rlang.src.grounding.utils.grounding_errors import RLangGroundingError


class Predicate(GroundingFunction):
    def __init__(self, function: Callable, name: str = None):
        self._function = function
        super().__init__(domain=Domain.STATE, codomain=Domain.BOOLEAN,
                         name=name)

    def __call__(self, *args, **kwargs):
        return self._function(*args, **kwargs)

    def __and__(self, other) -> Predicate:
        if isinstance(other, Predicate):
            return Predicate(function=lambda *args, **kwargs:
                             self(*args, **kwargs) and other(*args, **kwargs))
        if isinstance(other, bool):
            return self if other else Predicate(function=lambda *args, **kwargs: False)
        raise RLangGroundingError(message=f"Cannot & a Predicate with a {type(other)}")

    def __or__(self, other) -> Predicate:
        if isinstance(other, Predicate):
            return Predicate(function=lambda *args, **kwargs:
                             self(*args, **kwargs) or other(*args, **kwargs))
        if isinstance(other, bool):
            return Predicate(function=lambda *args, **kwargs:
                             self(*args, **kwargs) or bool)
        raise RLangGroundingError(message=f"Cannot | a Predicate with a {type(other)}")

    def __invert__(self) -> Predicate:
        return Predicate(function=lambda *args, **kwargs:
                         not self(*args, **kwargs))

    def __repr__(self):
        return "<Predicate>"


class Goal(Predicate):
    pass    # A Goal is simply a Predicate.
    # We may want to add a constructor which accepts a Predicate
