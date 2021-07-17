from lmdp.grounding.states.StateGroundingClass import StateFeature
from lmdp.grounding.states.SymbolClass import Predicate, any_state
from lmdp.grounding.states.Effect import PredictiveEffect
from lmdp.grounding.booleans.BooleanFunClass import bool_true


def symbol(name=None):
    def __symbol(func):
        return Predicate(func, name=func.__name__ if name is None else name)

    return __symbol


def effect(func):
    return PredictiveEffect(bool_true, func)


def state_feature(dim=1):
    def __state_feature(func):
        return StateFeature(func, dim, name=func.__name__)

    return __state_feature
