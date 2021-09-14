"""
    MarkovFeature grounding class
        - Represents a feature
    author: Benjamin Spiegel (bspiegel@cs.brown.edu), Jennifer Wang
    date: August 2021
"""

from typing import Callable
from rlang.src.grounding import Domain, GroundingFunction


class MarkovFeature(GroundingFunction):
    def __init__(self, function: Callable, name: str):
        self._function = function
        super().__init__(domain=Domain.STATE_ACTION_NEXTSTATE, codomain=Domain.REAL_VALUE, name=name)

# TODO: Write classmethods
# TODO: Override equality operator functions __eq__, etc.
