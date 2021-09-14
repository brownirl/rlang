from typing import Callable
from rlang.src.grounding.utils.domain import Domain
from rlang.src.grounding.groundings.state_action.state_action_grounding_function import StateActionGroundingFunction


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
