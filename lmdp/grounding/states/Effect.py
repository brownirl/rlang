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

from lmdp.grounding.ExpressionsClass import Expression
from lmdp.grounding.booleans.BooleanFunClass import BooleanExpression
from lmdp.grounding.states.SymbolClass import Symbol

class Effect(Expression):

    def __init__(self, boolean_expression_sa, effect):
        self._effect = effect
        self._domain_sa = boolean_expression_sa
        Expression.__init__(self, self.__boolean_expression, domain=["State", "Action"], codomain=["Set of States"])

    def __boolean_expression(self):
        if (isinstance(self._effect, list)):
            f = BooleanExpression(lambda *args: self._domain_sa(*args) and (args[2] in self._effect), domain=["State", "Action", "Next State"])
        elif(isinstance(self._effect, Symbol)):
            f = BooleanExpression(lambda *args: self._domain_sa(*args) and self._effect(args[2]), domain=["State", "Action", "Next State"])
        elif(isinstance(self._effect, dict)):
            f= BooleanExpression(lambda *args: self._domain_sa(*args) and __verify_transformation(self._effect, *args), domain=["State", "Action", "Next State"])
        else:
            raise "Error: Unexpected Effect Expression"
        return f

def __verify_transformation(effect, *args):
    verify = True
    vocab = args[-1]
    for (factor_name, factor_transformation) in effect.items():
         verify = verify and vocab[factor_name](args[2]) == factor_transformation(*args) 
    return verify