from typing import Callable
from rlang.src.grounding import Factor, Domain, GroundingFunction

# TODO: Migrate this to groundings.py


class MarkovFeature(GroundingFunction):
    """Represents a Grounding that is a function of (state, action, next_state)

    Args:
        function: a function of (state, action, next_state)
    """
    def __init__(self, function: Callable, name: str):
        self._function = function
        super().__init__(domain=Domain.STATE_ACTION_NEXT_STATE, codomain=Domain.REAL_VALUE, name=name)

    @classmethod
    def from_Factor(cls, factor: Factor, name: str = None):
        return cls(function=factor.__call__, name=name)

# TODO: Write classmethods
# TODO: Override equality operator functions __eq__, etc.
