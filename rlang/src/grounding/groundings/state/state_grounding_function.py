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
        if isinstance(other, GroundingFunction):
            return Predicate(function=lambda *args, **kwargs: self(*args, **kwargs) == other(*args, **kwargs))
        if isinstance(other, np.ndarray):
            return Predicate(function=lambda *args, **kwargs: self(*args, **kwargs) == other)
        raise RLangGroundingError(message=f"Cannot == a {type(self)} and a {type(other)}")

    def __ne__(self, other):
        if isinstance(other, GroundingFunction):
            return Predicate(function=lambda *args, **kwargs: self(*args, **kwargs) != other(*args, **kwargs))
        if isinstance(other, np.ndarray):
            return Predicate(function=lambda *args, **kwargs: self(*args, **kwargs) != other)
        raise RLangGroundingError(message=f"Cannot != a {type(self)} and a {type(other)}")


# Leaving this at the bottom of the file for circular import issue. Don't move it.
from rlang.src.grounding.groundings.state.predicate import Predicate
