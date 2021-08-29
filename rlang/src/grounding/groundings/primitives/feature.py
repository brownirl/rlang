"""
    Feature grounding_function class
        - Represents a feature
    author: Benjamin Spiegel (bspiegel@cs.brown.edu)
    date: August 2021
"""

from typing import Callable
from grounding.grounding_function import GroundingFunction
from grounding.domain import Domain


class Feature(GroundingFunction):
    def __init__(self, codomain: Domain, function: Callable, name: str):
        self._function = function
        super().__init__(domain=Domain.STATE, codomain=codomain, name=name)

    def __call__(self, *args, **kwargs):
        return self._function(args, kwargs)

# TODO: Override equality operator functions __eq__, etc.
