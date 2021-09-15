from typing import Callable
from rlang.src.grounding import Domain, GroundingFunction


class MarkovFeature(GroundingFunction):
    """Represents a Grounding that is a function of (state, action, next_state)

    Args:
        function: a function of (state, action, next_state)
    """
    def __init__(self, function: Callable, name: str):
        self._function = function
        super().__init__(domain=Domain.STATE_ACTION_NEXTSTATE, codomain=Domain.REAL_VALUE, name=name)

# TODO: Write classmethods
# TODO: Override equality operator functions __eq__, etc.
