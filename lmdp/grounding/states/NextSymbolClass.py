'''
    Next Symbol class 
        - This class defines a set of states parameterized by another state
          vector.
    author: Rafael Rodriguez-Sanchez
    date: September 2020
'''


from lmdp.grounding.states.SymbolClass import Symbol

class NextSymbol(Symbol):
    def __init__(self, boolean_fun, name=None, current_state=None):
        if (name is None):
            name = "next-symbol-" + str(Symbol.counter)
        Symbol.__init__(self, boolean_fun, name)
        self.__fun = boolean_fun
        self.__current_state = current_state
    

    def __call__(self, *args):
        if (len(args) > 2 or (len(args) == 1 and self.__current_state is None)):
            raise "Error: Arguments must (s, s') or you should set current state"
        elif (len(args) == 0):
            raise "Error: missing arguments"
        elif (len(args) == 2):
            self.__current_state = args[0] # current state s
            next_state = args[1] # second argument must be s'
        else:
            next_state = args[0]

        return self.__fun(self.current_state, next_state)

    @property
    def current_state(self):
        return self.__current_state

    @current_state.setter
    def current_state(self, state):
        self.__current_state = state

if __name__ == '__main__':
    from simple_rl.mdp.StateClass import State
    from lmdp.grounding.states.NextStateGroundingClass import next_state
    from lmdp.grounding import StateGrounding

    import numpy as np
    
    x = StateGrounding(0, "x")
    s = State(data=np.array([1,0]))
    s_prime = State(data= np.array([2,1]))
    s_prime_1 = State(data=np.array([1, 1]))
    
    up = NextSymbol(next_state(x) == x + 1)
    up.current_state = s
    print(up(s_prime))
