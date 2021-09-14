"""
    StateActionGroundingFunction class
        - Represents a GroundingFunction which is a function of State and Action
    author: Benjamin Spiegel (bspiegel@cs.brown.edu)
    date: September 2021
"""

from typing import Callable
from rlang.src.grounding import Domain
from rlang.src.grounding.groundings.grounding_function import GroundingFunction


class StateActionGroundingFunction(GroundingFunction):
    def __init__(self, codomain: Domain, function: Callable, name: str = None):
        super().__init__(domain=Domain.STATE_ACTION, codomain=codomain, function=function, name=name)
