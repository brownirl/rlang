"""
    Factor grounding class
        - Represents a factor of state
    author: Benjamin Spiegel (bspiegel@cs.brown.edu), Jennifer Wang
    date: August 2021
"""

from groundings.grounding_function import GroundingFunction
from grounding.utils.domain import Domain


class Factor(GroundingFunction):
    def __init__(self, state_indices: [int], name: str = None):
        self._state_indices = state_indices
        super().__init__(domain=Domain.STATE, codomain=Domain.REAL_VALUE, name=name)

    def __call__(self, *args, **kwargs):
        return kwargs['state'][self._state_indices]     # TODO: it's unclear whether we need to support keywords
