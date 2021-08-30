"""
    MarkovFeature grounding class
        - Represents a feature
    author: Benjamin Spiegel (bspiegel@cs.brown.edu), Jennifer Wang
    date: August 2021
"""

from typing import Callable
from grounding.grounding_function import GroundingFunction
from grounding.utils.domain import Domain


class MarkovFeature(GroundingFunction):
    def __init__(self, function: Callable, name: str):
        self._function = function
        super().__init__(domain=Domain.STATE_ACTION_NEXTSTATE, codomain=Domain.REAL_VALUE, name=name)

    def __call__(self, *args, **kwargs):
        return self._function(args, kwargs)

# TODO: Override equality operator functions __eq__, etc.
