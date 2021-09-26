from __future__ import annotations
from typing import Callable
from collections.abc import MutableMapping
from rlang.src.exceptions import RLangGroundingError
from rlang.src.grounding.internals import State
from rlang.src.grounding.groundings import Grounding, Factor, RewardFunction, TransitionFunction


class RLangKnowledge(MutableMapping):
    """Acts as a container for Groundings.

    Acts just like a Python dictionary.

    Examples:
        .. code-block:: python

            base = RLangKnowledge()
            base['x_location'] = Factor([1])

    """

    def __init__(self):
        self.store = dict()
        self._reward_function = RewardFunction(reward=0)
        self._transition_function = TransitionFunction()
        self.predictions = dict()

    @property
    def reward_function(self):
        return self._reward_function

    @reward_function.setter
    def reward_function(self, function: RewardFunction):
        self._reward_function = function

    @property
    def transition_function(self):
        return self._transition_function

    @transition_function.setter
    def transition_function(self, function: TransitionFunction):
        self._transition_function = function

    def __getitem__(self, key: str):
        return self.store[key]

    def __setitem__(self, key: str, value: Grounding):
        self.store[key] = value

    def __delitem__(self, key: str):
        del self.store[key]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

    def factors(self):
        # TODO: I don't understand why this doesn't work
        return dict(tuple(filter(lambda a: isinstance(a[1], Factor), self.__iter__())))
