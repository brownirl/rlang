"""
    Effect grounding class
        - Abstract class for effects
    author: Benjamin Spiegel (bspiegel@cs.brown.edu), Jennifer Wang
    date: August 2021
"""

from typing import Callable
from rlang.src.grounding.groundings.grounding_function import GroundingFunction
from rlang.src.grounding.utils.domain import Domain


class Effect(GroundingFunction):
    def __init__(self, codomain: Domain, function: Callable, name: str):
        self._function = function
        super().__init__(domain=Domain.STATE_ACTION, codomain=codomain, name=name)
