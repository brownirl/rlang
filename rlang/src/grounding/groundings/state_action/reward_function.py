"""
    RewardFunction grounding class
        -
    author: Benjamin Spiegel (bspiegel@cs.brown.edu)
    date: September 2021
"""

from typing import Callable
from rlang.src.grounding.utils.domain import Domain
from rlang.src.grounding.groundings.state_action.state_action_grounding_function import StateActionGroundingFunction


class RewardFunction(StateActionGroundingFunction):
    def __init__(self, function: Callable, name: str):
        super().__init__(codomain=Domain.REWARD, function=function, name=name)
