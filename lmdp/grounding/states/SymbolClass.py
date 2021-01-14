'''
    Symbol Base Class
    author: Rafael Rodriguez-Sanchez
    date: August 2020
'''

from lmdp.grounding.GroundingClass import Grounding
from lmdp.grounding.booleans.BooleanFunClass import BooleanExpression
class Symbol(Grounding):
    counter = 0
    def __init__(self, boolean_fun, name=None):
        if (name is None):
            name = "symbol-" + str(Symbol.counter)
        Grounding.__init__(self, name, domain=["State"])
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
    
    def _boolean_expression(self):
        return BooleanExpression(self.__symbol, domain=self._domain.domain())
    
    def and_(self, other):
        if(isinstance(other, Symbol)):
            return Symbol(self._boolean_expression().and_(other._boolean_expression()))
        elif (isinstance(other, bool)):
            return self._boolean_expression().and_(other)
        else:
            return NotImplemented
   
    def or_(self, other):
        if(isinstance(other, Symbol)):
            return Symbol(self._boolean_expression().and_(other._boolean_expression()))
        elif (isinstance(other, bool)):
            return self._boolean_expression().or_(other)
        else:
            return NotImplemented
    
    def not_(self):
        return Symbol(self._boolean_expression().not_())
    


Any = Symbol(lambda *args: True, name='any-symbol') 
None_ = Symbol(lambda  *args: False, name='none-symbol')

        
if __name__ == "__main__":
    import numpy as np
    from simple_rl.mdp.StateClass import State
    from StateGroundingClass import StateFactor
    
    s1 = State(data=np.array([1, 1]))
    s2 = State(data=np.array([0, 1]))
    x = StateFactor(0, "x")
    y = StateFactor(1, "y")
    s = StateFactor([0,1], "s1")
    start = Symbol(s == np.array([0,0]))
    not_goal = Symbol(s != np.array([1,1]))
    diag = Symbol(x == y, "diag")
    print(f"s1 belongs to {diag.name}: {diag(s1)} == True")
    print(f"s2 belongs to {diag.name}: {diag(s2)} == False")
    x_0 = x == 0 
    x_1 = x + 1
    print(f"z is start: {start(State(data=np.array([0,0])))} == True")
    print(f"s1 is start: {start(s1)} == False")
    print(f"s2 is not goal: {not_goal(s2)} == True")
    print(f"s1 is not goal: {not_goal(s1)} == False")