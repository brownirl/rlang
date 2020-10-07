'''
    Symbol Base Class
    author: Rafael Rodriguez-Sanchez
    date: August 2020
'''
from lmdp.grounding.GroundingClass import Grounding

class Symbol(Grounding):
    counter = 0
    def __init__(self, boolean_fun, name=None):
        if (name is None):
            name = "symbol-" + str(Symbol.counter)
        Grounding.__init__(self, name)
        self.__symbol = boolean_fun

    def __call__(self, *args):
        '''
            This takes in the state from MDP.
            Args:
                - args[0] must be the state from MDP
            return:
                - bool: state belongs to the symbol (set)
        '''
        return self.__symbol(args[0])
    
    def and_(self, other):
        if(isinstance(other, Symbol)):
            return lambda *args: self.__call__(*args) and other(*args)
        elif (isinstance(other, bool)):
            return lambda *args: self.__call__(*args) and other 
        else:
            raise other.__name__() + " must be a Boolean Fun or bool"
   
    def or_(self, other):
        if(isinstance(other, Symbol)):
            return lambda *args: self.__call__(*args) or other(*args)
        elif (isinstance(other, bool)):
            return lambda *args: self.__call__(*args) or other 
        else:
            raise other.__name__() + " must be a Boolean Fun or bool"
    
    def not_(self):
        return lambda *args: not self.__call__(*args)
    


Any = Symbol(lambda *args: True, name='any-symbol') 
None_ = Symbol(lambda  *args: False, name='none-symbol')

        
if __name__ == "__main__":
    import numpy as np
    from simple_rl.mdp.StateClass import State
    from StateGroundingClass import StateGrounding
    
    s1 = State(data=np.array([1, 1]))
    s2 = State(data=np.array([0, 1]))
    x = StateGrounding(0, "x")
    y = StateGrounding(1, "y")
    s = StateGrounding([0,1], "s1")
    start = Symbol(s == np.array([0,0]))
    not_goal = Symbol(s != np.array([1,1]))
    diag = Symbol(x == y, "diag")
    print(f"s1 belongs to {diag.name}: {diag(s1)}")
    print(f"s2 belongs to {diag.name}: {diag(s2)}")
    x_0 = x == 0 
    x_1 = x + 1
    print(f"z is start: {start(State(data=np.array([0,0])))}")
    print(f"s1 is start: {start(s1)}")
    print(f"s2 is not goal: {not_goal(s2)}")
    print(f"s1 is not goal: {not_goal(s1)}")