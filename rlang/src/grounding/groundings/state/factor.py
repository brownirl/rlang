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
    def __init__(self, state_indexer: Any, name: str = None):
        if type(state_indexer) == int:
            state_indexer = [state_indexer]
        self._state_indexer = state_indexer
        super().__init__(function=lambda *args, **kwargs: kwargs['state'].__getitem__(self._state_indexer),
                         codomain=Domain.REAL_VALUE, name=name)

    def __getitem__(self, item):
        if isinstance(self._state_indexer, slice):
            print("This is weird")
        if isinstance(item, list):
            return Factor([self._state_indexer[i] for i in item])
        return Factor(self._state_indexer[item])

    def __repr__(self):
        return f"<Factor: {str(self._state_indexer)}>"
