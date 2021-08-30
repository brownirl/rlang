"""
    Predicate grounding class
        - Represents a factor of state
    author: Benjamin Spiegel (bspiegel@cs.brown.edu), Jennifer Wang
    date: August 2021
"""

from typing import Callable
from grounding.grounding_function import GroundingFunction
from grounding.utils.domain import Domain


class Predicate(GroundingFunction):
    def __init__(self, function: Callable, name: str = None):
        self._function = function
        super().__init__(domain=Domain.STATE, codomain=Domain.BOOLEAN, name=name)

    def __call__(self, *args, **kwargs):
        return self._function(args, kwargs)     # TODO: it's unclear whether we need to support keywords

# TODO: Implement __and__, __or__, and __not__ composition


class Goal(Predicate):
    pass    # A Goal is simply a Predicate. We may want to add a constructor which accepts a Predicate