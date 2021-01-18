'''
    Grounding for symbols to Rewards
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: v0 August 2020
          v1 January 2021 (Partial Function)
'''

from lmdp.grounding.GroundingClass import Grounding
from lmdp.grounding.PartialFunctionClass import PartialFunction
from lmdp.grounding.real.RealExpressionClass import RealExpression


class ValueGrounding(Grounding, PartialFunction):
    id = 0
    def __init__(self, symbols_values=[], name=None):
        '''
            Args:
                symbols_values: iterable of pairs of (symbols, values)
        '''
        if (name is None):
            name = "value-" + str(ValueGrounding.id)
        Grounding.__init__(self, name)
        PartialFunction.__init__(self, domain=["State"], codomain=["Real"])
        for spec in symbols_values:
            self.add(*spec)

    def __call__(self, state):
        '''
            Args:
                - state from MDP
            return:
                - list of rewards for all symbol matches
        '''
        return super().__call__(state)
    
    def add(self, symbol, value):
        '''
            Add a reward to the dictionary. Overrides if it already exists.        
            Args:
                - symbol 
                - reward
        '''
        if (isinstance(value, float) or isinstance(value, int)):
            v = RealExpression(lambda *args: value, domain=["State", "Action", "Next State"])
        else:
            v = value
        self.add_specification(symbol, v)