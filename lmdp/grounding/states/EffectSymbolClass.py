'''
    Effect Symbol class 
        - This class defines a set of states parameterized by another state
          vector.
    author: Rafael Rodriguez-Sanchez
    date: September 2020
'''

from lmdp.grounding.states.SymbolClass import Symbol
from functools import partial

class EffectSymbol(Symbol):
    def __init__(self, boolean_fun, name=None, current_state=None):
        if (name is None):
            name = "effect-symbol-" + str(Symbol.counter)
        Symbol.__init__(self, boolean_fun, name)
        self.__fun = boolean_fun
    

    def __call__(self, curr_state):
        return partial(self.__fun, curr_state)


if __name__ == '__main__':
    from simple_rl.mdp.StateClass import State
    from lmdp.grounding.states.NextStateGroundingClass import next_state
    from lmdp.grounding import StateFactor

    import numpy as np
    
    x = StateFactor(0, "x")
    s = State(data=np.array([1,0]))
    s_prime = State(data= np.array([2,1]))
    s_prime_1 = State(data=np.array([1, 1]))
    
    up = EffectSymbol(next_state(x) == x + 1)(s)
    print(up(s_prime))
