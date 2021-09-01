"""
    Policy grounding class
        - Represents a factor of state
    author: Benjamin Spiegel (bspiegel@cs.brown.edu), Jennifer Wang
    date: August 2021
"""

from typing import Callable
from rlang.src.grounding.utils.domain import Domain
from rlang.src.grounding.groundings.grounding_function import GroundingFunction


class Policy(GroundingFunction):
    def __init__(self, function: Callable, name: str = None):
        self._function = function
        super().__init__(domain=Domain.STATE, codomain=Domain.ACTION, name=name)

    def __call__(self, *args, **kwargs):
        return self._function(args, kwargs)     # TODO: What kind of function do we expect?
