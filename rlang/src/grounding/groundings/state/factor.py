"""
    Factor grounding class
        - Represents a factor of state
    author: Benjamin Spiegel (bspiegel@cs.brown.edu), Jennifer Wang
    date: August 2021
"""

from typing import Any
from rlang.src.grounding.groundings.state.state_grounding_function import StateGroundingFunction
from rlang.src.grounding import Domain


class Factor(StateGroundingFunction):
    def __init__(self, state_indices: Any, name: str = None):
        if type(state_indices) == int:
            state_indices = [state_indices]
        self._state_indices = state_indices
        super().__init__(function=lambda *args, **kwargs: kwargs['state'].__getitem__(self._state_indices),
                         codomain=Domain.REAL_VALUE, name=name)

    def __getitem__(self, item):
        return Factor(self._state_indices[item])

    def __repr__(self):
        return f"<Factor: {str(self._state_indices)}>"
