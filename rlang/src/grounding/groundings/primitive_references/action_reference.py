"""
    Action grounding class
        - Represents a reference to an action
    author: Benjamin Spiegel (bspiegel@cs.brown.edu)
    date: September 2021
"""

from typing import Any
import numpy as np
from rlang.src.grounding.groundings.grounding_function import GroundingFunction
from rlang.src.grounding.utils.domain import Domain


class ActionReference(GroundingFunction):
    def __init__(self, action: Any, name: str = None):
        if isinstance(action, (int, float, list)):
            action = np.array(action)
        self._action = action
        super().__init__(domain=Domain.ANY, codomain=Domain.ACTION,
                         function=lambda *args, **kwargs: self._action, name=name)
