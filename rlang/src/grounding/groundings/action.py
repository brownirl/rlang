"""
    Action grounding class
        - Represents a reference to an action
    author: Benjamin Spiegel (bspiegel@cs.brown.edu), Jennifer Wang
    date: August 2021
"""

from typing import Any
import numpy as np
from rlang.src.grounding.groundings.grounding_function import GroundingFunction
from rlang.src.grounding.utils.domain import Domain


class Action(GroundingFunction):
    def __init__(self, action: Any, name: str = None):
        if isinstance(action, (int, float)):
            action = np.array(action)
        self._action = action
        super().__init__(domain=Domain.ANY, codomain=Domain.ACTION, name=name)

    def __call__(self, *args, **kwargs):
        return self._action
