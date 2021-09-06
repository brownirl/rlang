"""
    Feature grounding class
        - Represents a feature
    author: Benjamin Spiegel (bspiegel@cs.brown.edu), Jennifer Wang
    date: August 2021
"""

from typing import Callable
from rlang.src.grounding.groundings.state.state_grounding_function import StateGroundingFunction
from rlang.src.grounding.utils.domain import Domain


class Feature(StateGroundingFunction):
    def __init__(self, function: Callable, name: str = None):
        super().__init__(function=function, codomain=Domain.REAL_VALUE, name=name)
