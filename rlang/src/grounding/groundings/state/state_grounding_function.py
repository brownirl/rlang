"""
    StateGroundingFunction class
        - Represents a GroundingFunction which is a function of State
    author: Benjamin Spiegel (bspiegel@cs.brown.edu), Jennifer Wang
    date: August 2021
"""

from typing import Callable
import numpy as np
from rlang.src.grounding import Domain
from rlang.src.grounding.groundings.grounding_function import GroundingFunction
from rlang.src.grounding.utils.grounding_errors import RLangGroundingError


class StateGroundingFunction(GroundingFunction):
    def __init__(self, codomain: Domain, function: Callable, name: str = None):
        self._function = function
        super().__init__(domain=Domain.STATE, codomain=codomain, name=name)

    def __call__(self, *args, **kwargs):
        return self._function(*args, **kwargs)

    def __eq__(self, other):
        if isinstance(other, (StateGroundingFunction, Callable)):
            return Predicate(function=lambda *args, **kwargs: self(*args, **kwargs) == other(*args, **kwargs))
        if isinstance(other, np.ndarray):
            return Predicate(function=lambda *args, **kwargs: self(*args, **kwargs) == other)
        raise RLangGroundingError(message=f"Cannot '==' a {type(self)} and a {type(other)}")

    def __ne__(self, other):
        if isinstance(other, (StateGroundingFunction, Callable)):
            return Predicate(function=lambda *args, **kwargs: self(*args, **kwargs) != other(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Predicate(function=lambda *args, **kwargs: self(*args, **kwargs) != other)
        raise RLangGroundingError(message=f"Cannot '!=' a {type(self)} and a {type(other)}")

    def __mul__(self, other):
        if isinstance(other, (StateGroundingFunction, Callable)):
            return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) * other(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) * other)
        raise RLangGroundingError(message=f"Cannot '*' a {type(self)} and a {type(other)}")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, (StateGroundingFunction, Callable)):
            return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) / other(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) / other)
        raise RLangGroundingError(message=f"Cannot '/' a {type(self)} and a {type(other)}")

    def __rtruediv__(self, other):
        if isinstance(other, (np.ndarray, int, float)):
            return Feature(function=lambda *args, **kwargs: other / self(*args, **kwargs))
        raise RLangGroundingError(message=f"Cannot '/' a {type(other)} and a {type(self)}")

    def __sub__(self, other):
        if isinstance(other, (StateGroundingFunction, Callable)):
            return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) - other(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) - other)
        raise RLangGroundingError(message=f"Cannot '-' a {type(self)} and a {type(other)}")

    def __rsub__(self, other):
        if isinstance(other, (np.ndarray, int, float)):
            return Feature(function=lambda *args, **kwargs: other - self(*args, **kwargs))
        raise RLangGroundingError(message=f"Cannot '-' a {type(other)} and a {type(self)}")

    def __add__(self, other):
        if isinstance(other, (StateGroundingFunction, Callable)):
            return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) + other(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) + other)
        raise RLangGroundingError(message=f"Cannot '+' a {type(self)} and a {type(other)}")

    def __radd__(self, other):
        self.__add__(other)


# Leaving this at the bottom of the file for circular import issue. Don't move it.
from rlang.src.grounding.groundings.state.predicate import Predicate
from rlang.src.grounding.groundings.state.feature import Feature
