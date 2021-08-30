"""
    Action grounding class
        - Represents a reference to an action
    author: Benjamin Spiegel (bspiegel@cs.brown.edu), Jennifer Wang
    date: August 2021
"""

from groundings.grounding_function import GroundingFunction
from grounding.utils.domain import Domain


class Action(GroundingFunction):
    def __init__(self, action, name: str = None):   # TODO: action should be type hinted eventually
        self._action = action
        super().__init__(domain=Domain.ANY, codomain=Domain.STATE, name=name)

    def __call__(self, *args, **kwargs):
        return self._action
