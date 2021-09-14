from typing import Callable
from rlang.src.grounding import Domain, GroundingFunction


class StateActionGroundingFunction(GroundingFunction):
    """
        StateActionGroundingFunction class
            - Represents a GroundingFunction which is a function of State and Action
        author: Benjamin Spiegel (bspiegel@cs.brown.edu)
        date: September 2021
    """
    def __init__(self, codomain: Domain, function: Callable, name: str = None):
        super().__init__(domain=Domain.STATE_ACTION, codomain=codomain, function=function, name=name)


class RewardFunction(StateActionGroundingFunction):
    def __init__(self, function: Callable, name: str):
        super().__init__(codomain=Domain.REWARD, function=function, name=name)


class TransitionFunction(StateActionGroundingFunction):
    """
        TransitionFunction grounding class
            -
        author: Benjamin Spiegel (bspiegel@cs.brown.edu)
        date: September 2021
    """
    def __init__(self, function: Callable, name: str):
        super().__init__(codomain=Domain.STATE, function=function, name=name)


class PartialTransitionFunction(StateActionGroundingFunction):
    """
        PartialTransitionFunction grounding class
            -
        author: Benjamin Spiegel (bspiegel@cs.brown.edu)
        date: September 2021
    """
    def __init__(self, function: Callable, name: str):
        super().__init__(codomain=Domain.REAL_VALUE, function=function, name=name)
