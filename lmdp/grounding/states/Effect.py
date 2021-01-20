'''
    Effect Class:
        Effect Expression implementation.
        args:
            -Boolean expresion in SxA to determine if the effect is applicable
            -Effect Expression among:
                - List of States
                - Symbol
                - Dictionary of Factor name to expression

    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: January 2021
'''

from lmdp.grounding.expressions.ExpressionsClass import Expression
from lmdp.grounding.booleans.BooleanFunClass import BooleanExpression
from lmdp.grounding.states.EffectSymbolClass import EffectSymbol
from lmdp.grounding.states.SymbolClass import Symbol
from lmdp.utils.expression_utils import Domain
from functools import partial

class Effect(Expression):

    def __init__(self, boolean_expression_sa, effect):
        self._effect = effect 
        self._domain_sa = boolean_expression_sa
        Expression.__init__(self, self.effect, domain=["state", "action"], codomain=["set_of_states"])

    def effect(self, state, action):
        if (isinstance(self._effect, list)):
            f = lambda state, action, next_state: self._domain_sa(state, action) and (next_state in self._effect)
        elif(isinstance(self._effect, BooleanExpression) and self._effect.domain <= Domain(["state", "action", "next_state"])):
            f = lambda state, action, next_state: self._domain_sa(state, action) and self._effect(state=state, action=action, next_state=next_state)
        # elif(isinstance(self._effect, dict)):
        #     f = lambda state, action, next_state: self._domain_sa(state, action) and __verify_transformation(self._effect, )
        else:
            raise "Error: Unexpected Effect Expression"
        return EffectSymbol(f)(state, action)

def __verify_transformation(effect, vocabulary, state, action, next_state):
    verify = True
    vocab = vocabulary
    for (factor_name, factor_transformation) in effect.items():
         verify = verify and vocab[factor_name](next_state) == factor_transformation(state, action) 
    return verify

if __name__=="__main__":
    from simple_rl.mdp.StateClass import State
    from lmdp.grounding.states.NextStateGroundingClass import next_state
    from lmdp.grounding import StateFactor
    from lmdp.grounding.booleans.BooleanFunClass import any_state, any_action
    import numpy as np
    
    x = StateFactor(0, "x")
    s = State(data=np.array([1,0]))
    s_prime = State(data= np.array([2,1]))
    s_prime_1 = State(data=np.array([1, 1]))
    up = Effect(any_state and any_action, next_state(x) == x + 1)
    # up = EffectSymbol(next_state(x) == x + 1)(s, "up")
    print(f"{up(s, 'up')(s_prime)} == True")