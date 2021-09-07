"""
    Policy grounding class
        - Represents a factor of state
    author: Benjamin Spiegel (bspiegel@cs.brown.edu), Jennifer Wang
    date: August 2021
"""

from typing import Callable
from rlang.src.grounding.utils.domain import Domain
from rlang.src.grounding.groundings.state.state_grounding_function import StateGroundingFunction


class Policy(StateGroundingFunction):
    def __init__(self, function: Callable, name: str = None):
        super().__init__(function=function, codomain=Domain.ACTION, name=name)
