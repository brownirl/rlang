'''
    Effect Class:
        Effect Expression implementation.
        args:
            -Boolean expresion in SxA to determine if the effect is applicable
            -Effect Expression among:
                - List of States
                - Predicate
                - Dictionary of Factor name to expression

    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: January 2021
'''

from rlang.src.lmdp.grounding.expressions.ExpressionsClass import Expression
from rlang.src.lmdp.grounding.booleans.BooleanFunClass import BooleanExpression, BOOL_TRUE, BOOL_FALSE
from rlang.src.lmdp.grounding.states.EffectSymbolClass import EffectSymbol
from rlang.src.lmdp.grounding.states.PredicateClass import Predicate
from rlang.src.lmdp.grounding.states.StateGroundingClass import StateFactor
from rlang.src.lmdp.utils.expression_utils import Domain, Codomain
from functools import partial


class Effect(Expression):

    def __init__(self, boolean_expression_sa, effect):
        self._effect = effect
        self._domain_sa = boolean_expression_sa
        Expression.__init__(self, self.effect, domain=["state", "action"], codomain=["set_of_states"])

    def effect(self, state, action):
        if (isinstance(self._effect, (list, tuple))):  # state enumerations
            f = lambda state, action, next_state: self._domain_sa(state, action) & (next_state in self._effect)
        elif (isinstance(self._effect, Expression) and self._effect.codomain == Codomain(
                ["boolean"]) and self._effect.domain <= Domain(
            ["state", "action", "next_state"])):  # set of states as symbols
            f = lambda state, action, next_state: self._domain_sa(state, action) & self._effect(state=state,
                                                                                                action=action,
                                                                                                next_state=next_state)
        elif (isinstance(self._effect, dict)):  # factored effects
            f = lambda state, action, next_state: self._domain_sa(state, action) & self.__verify_transformation(
                self._effect, state, action, next_state)
        elif (isinstance(self._effect, Expression) and Codomain(
                ["state"]) == self._effect.codomain):  # predictive effect
            f = lambda state, action, next_state: self._domain_sa(state, action) & (
                (self._effect(state=state, action=action) == next_state).all(-1))
        else:
            raise ValueError("Error: Unexpected Effect Expression")
        return partial(EffectSymbol(f), state, action)

    def __verify_transformation(self, effect, state, action, next_state):
        verify = True
        for (factor, factor_transformation) in effect.items():
            verify = verify and factor(next_state) == factor_transformation(state, action)
        return verify


class PredictiveEffect(Effect):
    def __init__(self, boolean_expression_sa, effect, state_dim=None):
        Effect.__init__(self, boolean_expression_sa, effect)
        self._codomain = Codomain(["state"])
        self.state_dim = state_dim

    def effect(self, state, action):
        return self._effect(state, action)

    def __create_effect_from_dict(self, d):
        '''
            Dictionary of StateFactor -> Expression(S, A) -> Real
            Return: state vector
        '''

        missing, overlapping = StateFactor.check_concat(d.keys(), self.state_dim)

        error = ""
        if len(missing) > 0:
            error += "State Underspecified. "
        if len(overlapping) > 0:
            error += "Effect ambiguous."
        if len(error) > 0:
            raise ValueError(error)


if __name__ == "__main__":
    from simple_rl.mdp.StateClass import State
    from lmdp.grounding.states.NextStateGroundingClass import next_state
    from lmdp.grounding import StateFactor
    from lmdp.grounding.booleans.BooleanFunClass import any_state, any_action
    import numpy as np

    x = StateFactor(0, "x")
    s = State(data=np.array([1, 0]))
    s_prime = State(data=np.array([2, 1]))
    s_prime_1 = State(data=np.array([1, 1]))
    up = Effect(BOOL_TRUE, next_state(x) == x + 1)
    # up = EffectSymbol(next_state(x) == x + 1)(s, "up")
    print(f"{up(s, 'up')(s_prime)} == True")
