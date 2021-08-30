"""
    RewardEffect grounding class
        -
    author: Benjamin Spiegel (bspiegel@cs.brown.edu), Jennifer Wang
    date: August 2021
"""

from typing import Callable
from effect import Effect
from grounding.utils.domain import Domain


class RewardEffect(Effect):
    def __init__(self, function: Callable, name: str):
        super().__init__(codomain=Domain.REWARD, function=function, name=name)
