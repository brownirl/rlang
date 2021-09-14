"""
    Primitive class
        - Represents a primitive
    author: Benjamin Spiegel (bspiegel@cs.brown.edu)
    date: August 2021
"""

from typing import Any
import numpy as np
from rlang.src.grounding.groundings.grounding_function import GroundingFunction
from rlang.src.grounding.utils.domain import Domain


class Primitive(GroundingFunction):
    def __init__(self, codomain: Domain, value: Any, name: str = None):
        if isinstance(value, (int, float, list)):
            value = np.array(value)
        self._value = value
        super().__init__(domain=Domain.ANY, codomain=codomain,
                         function=lambda *args, **kwargs: self._value, name=name)
