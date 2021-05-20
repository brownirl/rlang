from lmdp.grounding.states.StateGroundingClass import StateFeature
from lmdp.grounding.states.SymbolClass import Symbol, any_state
from lmdp.grounding.states.Effect import PredictiveEffect
from lmdp.grounding.booleans.BooleanFunClass import bool_true

def symbol(func):
    return Symbol(func, name=func.__name__)

def effect(func):
    return PredictiveEffect(bool_true, func)

def state_feature(dim=1):
    def __state_feature(func):
        return StateFeature(func, dim, name=func.__name__)
    return __state_feature