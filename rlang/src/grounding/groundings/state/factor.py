"""
    Factor grounding class
        - Represents a factor of state
    author: Benjamin Spiegel (bspiegel@cs.brown.edu), Jennifer Wang
    date: August 2021
"""

from typing import Any
from rlang.src.grounding.groundings.grounding_function import GroundingFunction
from rlang.src.grounding import Domain
from rlang.src.grounding.groundings.state.predicate import Predicate


class Factor(GroundingFunction):
    def __init__(self, state_indices: Any, name: str = None):
        if type(state_indices) == int:
            state_indices = [state_indices]
        self._state_indices = state_indices
        super().__init__(domain=Domain.STATE, codomain=Domain.REAL_VALUE, name=name)

    def __call__(self, *args, **kwargs):
        return kwargs['state'].__getitem__(self._state_indices)

    def __eq__(self, other):
        return Predicate(function=lambda *args, **kwargs: self(*args, **kwargs) == other(*args, **kwargs))

    def __repr__(self):
        return f"<Factor: {str(self._state_indices)}>"
