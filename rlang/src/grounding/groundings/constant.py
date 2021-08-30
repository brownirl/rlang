"""
    Constant grounding class
        - Represents a constant
    author: Benjamin Spiegel (bspiegel@cs.brown.edu), Jennifer Wang
    date: August 2021
"""

from typing import Any
from grounding.grounding_function import GroundingFunction
from grounding.utils.domain import Domain


class Constant(GroundingFunction):
    def __init__(self, codomain: Domain, value: Any, name: str):
        self._value = value
        super().__init__(domain=Domain.ANY, codomain=codomain, name=name)

    def __call__(self, *args, **kwargs):
        return self._value
