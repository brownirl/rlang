'''
    Grounding for symbols to Rewards
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: August 2020
'''

from lmdp.grounding.GroundingClass import Grounding

class ValueGrounding(Grounding):
    id = 0
    def __init__(self, symbols_values=[], name=None):
        '''
            Args:
                symbols_values: iterable of pairs of (symbols, values)
        '''
        if (name is None):
            name = "value-" + str(ValueGrounding.id)
        Grounding.__init__(self, name)
        self.__values = dict(symbols_values)

    def __call__(self, state):
        '''
            Args:
                - state from MDP
            return:
                - list of rewards for all symbol matches
        '''
        symbols = [s for s in self.__values.keys() if s(state)]
        v = [self.__values[s] for s in symbols]
        if len(v) == 1: # return scalar if only one value available.
            return v[0]
        return v
    
    def add(self, symbol, value):
        '''
            Add a reward to the dictionary. Overrides if it already exists.        
            Args:
                - symbol 
                - reward
        '''
        self.__values[symbol] = value