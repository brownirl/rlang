'''
    Grounding for (deterministic) Transitions specifications
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: August 2020
'''
from lmdp.grounding.GroundingClass import Grounding
from lmdp.grounding.PartialFunctionClass import PartialFunction
from lmdp.grounding.booleans.BooleanFunClass import BooleanExpression
from collections import defaultdict

class TransitionGrounding(Grounding, PartialFunction):
    
    def __init__(self, transitions=[], name=None):
        '''
            Args:
                -transitions: list of triples (symbol, action, EffectSymbol) 
        '''
        if (name is None):
            name = 'transitions'
        Grounding.__init__(self, name)
        PartialFunction.__init__(self, domain=["State", "Action"], codomain=["Set of States"])
        for t in transitions:
            self.add(*t)        # initialize transitions
    
    def __call__(self, state, action):
        '''
            Given a (state, action) pair, it returns a symbol corresponding 
            to the next state (list)
        '''
        return super().__call__(state, action)

    
    def add(self, symbol, action, effect):
        '''
            add a new transition
            Args:
                - symbol (starting symbol)
                - action 
                - Effect Symbol
        '''

        boolean_cond = BooleanExpression(lambda *args: symbol(*args) and args[1] == action, domain=["State", "Action"])
        self.add_specification(boolean_cond, effect)

    def __create_dict(self, transitions):
        self.__transitions = defaultdict(lambda: defaultdict())
        for (symbol, action, symbol_next) in transitions:
            self.__transitions[symbol][action] = symbol_next