from lmdp.grounding import Grounding

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
        r = [self.__values[s] for s in symbols]
        if len(r) == 1:
            return r[0]
        return r
    
    def add(self, symbol, value):
        '''
            Add a reward to the dictionary. Overrides if it already exists.        
            Args:
                - symbol 
                - reward
        '''
        self.__values[symbol] = value