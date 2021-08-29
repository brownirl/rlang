"""
    Predicate grounding_function class
        - Represents a factor of state
    author: Benjamin Spiegel (bspiegel@cs.brown.edu)
    date: August 2021
"""

from typing import Callable
from feature import Feature
from grounding.domain import Domain


class Predicate(Feature):
    def __init__(self, function: Callable, name: str = None):
        super(Predicate, self).__init__(codomain=Domain.BOOLEAN, function=function, name=name)

# TODO: Implement __and__, __or__, and __not__ composition
