'''
    Grounding for (deterministic) Transitions specifications
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: August 2020
'''
from lmdp.grounding.GroundingClass import Grounding
from collections import defaultdict

class TransitionGrounding(Grounding):
    
    def __init__(self, transitions=[], name=None):
        '''
            Args:
                -transitions: list of triples (symbol, action, next_symbol) 
        '''
        if (name is None):
            name = 'transitions'
        Grounding.__init__(self, name)
        self.__create_dict(transitions)
    
    def __call__(self, state, action):
        '''
            Given a (state, action) pair, it returns a symbol corresponding 
            to the next state (list)
        '''
        next_symbols = []
        for s in [symbol for symbol in self.__transitions.keys() if symbol(state)]:
            next_symbols.append(self.__transitions[s][action])
        if (len(next_symbols) == 1):
            next_symbols = next_symbols[0]
        return next_symbols

    
    def add(self, symbol, action, symbol_next):
        '''
            add a new transition
            Args:
                - symbol (starting symbol)
                - action 
                - symbol (next-state symbol)
        '''
        self.__transitions[symbol][action] = symbol_next

    def __create_dict(self, transitions):
        self.__transitions = defaultdict(lambda: defaultdict())
        for (symbol, action, symbol_next) in transitions:
            self.__transitions[symbol][action] = symbol_next