"""
    TransitionEffect grounding class
        -
    author: Benjamin Spiegel (bspiegel@cs.brown.edu), Jennifer Wang
    date: August 2021
"""

from typing import Callable
from .effect import Effect
from rlang.src.grounding.utils.domain import Domain


class TransitionEffect(Effect):
    def __init__(self, function: Callable, name: str):
        super().__init__(codomain=Domain.STATE, function=function, name=name)
        # TODO: What if the effect isn't a state, but a factor?
