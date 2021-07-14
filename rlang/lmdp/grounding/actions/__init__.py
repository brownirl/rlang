from lmdp.grounding.states.SymbolClass import any_state
from lmdp.grounding.actions.PolicyGroundingClass import Policy
from lmdp.grounding.actions.SubpolicyClass import Subpolicy


def policy(name=None):
    def __policy(policy_func):
        p_name = policy_func.__name__ if name is None else name
        return Policy(policy_func, name=p_name)
    return __policy

def subpolicy(at=any_state, until=any_state):
    def __subpolicy(policy_fun):
        return Subpolicy(init_symbol=at, policy_fun=policy_fun, termination_symbol=until, name=policy_fun.__name__)
    return __subpolicy