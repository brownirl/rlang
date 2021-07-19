from lmdp.grounding.states.StateGroundingClass import StateFeature
from lmdp.grounding.states.PredicateClass import Predicate, any_state
from lmdp.grounding.states.Effect import PredictiveEffect
from lmdp.grounding.booleans.BooleanFunClass import bool_true


def predicate(name=None):
    def __predicate(func):
        return Predicate(func, name=func.__name__ if name is None else name)

    return __predicate


def effect(func):
    return PredictiveEffect(bool_true, func)


def state_feature(dim=1):
    def __state_feature(func):
        return StateFeature(func, dim, name=func.__name__)

    return __state_feature
