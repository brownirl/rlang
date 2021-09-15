from typing import Callable
from rlang.src.grounding import Domain, GroundingFunction


class StateActionGroundingFunction(GroundingFunction):
    """Parent class for a Grounding that is a function of (state, action)."""
    def __init__(self, codomain: Domain, function: Callable, name: str = None):
        super().__init__(domain=Domain.STATE_ACTION, codomain=codomain, function=function, name=name)


class RewardFunction(StateActionGroundingFunction):
    """Represents a reward function."""
    def __init__(self, function: Callable, name: str):
        super().__init__(codomain=Domain.REWARD, function=function, name=name)


class TransitionFunction(StateActionGroundingFunction):
    """Represents a transition function."""
    def __init__(self, function: Callable, name: str):
        super().__init__(codomain=Domain.STATE, function=function, name=name)


class PartialTransitionFunction(StateActionGroundingFunction):
    """Represents a transition function that does not return the entire state.

    Can be used to specify partial knowledge of the transition function, including
    the value of a Factor of the next state.
    """
    def __init__(self, function: Callable, name: str):
        super().__init__(codomain=Domain.REAL_VALUE, function=function, name=name)
