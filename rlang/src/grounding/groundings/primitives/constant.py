"""
    Constant grounding_function class
        - Represents constants
    author: Benjamin Spiegel (bspiegel@cs.brown.edu)
    date: August 2021
"""

from typing import Any
from grounding.grounding_function import GroundingFunction
from grounding.domain import Domain


class Constant(GroundingFunction):
    def __init__(self, value: Any, name: str):
        super().__init__(domain=Domain.ANY, codomain=Domain.REAL_VALUE, name=name)
        self._value = value

    def __call__(self, *args, **kwargs):
        return self._value
