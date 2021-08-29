"""
    Factor grounding_function class
        - Represents a factor of state
    author: Benjamin Spiegel (bspiegel@cs.brown.edu)
    date: August 2021
"""

from feature import Feature
from grounding.domain import Domain


class Factor(Feature):
    def __init__(self, state_indices: [int], name: str = None):
        self._state_indices = state_indices
        super(Factor, self).__init__(codomain=Domain.MULTIPLE_VALUES, function=self.__call__, name=name)

    def __call__(self, *args, **kwargs):
        return kwargs['state'][self._state_indices]     # TODO: it's unclear whether we need to support keywords
