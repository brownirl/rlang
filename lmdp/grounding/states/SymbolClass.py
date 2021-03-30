'''
    Symbol Base Class
    author: Rafael Rodriguez-Sanchez
    date: v0 August 2020
          v1 January 2021 
'''
import sys, os
sys.path.append(os.path.abspath("./"))

from lmdp.grounding.GroundingClass import Grounding
from lmdp.grounding.booleans.BooleanFunClass import BooleanExpression, bool_or, bool_and, bool_not

class Symbol(Grounding, BooleanExpression):
    counter = 0
    def __init__(self, boolean_fun, name=None, operator=None, operands=None):
        if (name is None):
            name = "symbol-" + str(Symbol.counter)
        Grounding.__init__(self, name)
        BooleanExpression.__init__(self, boolean_fun, domain=["state"], 
                                  name=name, operator=operator, operands=operands)
        Symbol.counter += 1
    
    def and_(self, other):
        if(isinstance(other, Symbol)):
            return Symbol(super().and_(other), operator='and', operands=[self, other])
        elif (isinstance(other, bool)):
            return super().and_(other)
        else:
            return NotImplemented
   
    def or_(self, other):
        if(isinstance(other, Symbol)):
            return Symbol(super().or_(other), operator='and', operands=[self, other])
        elif (isinstance(other, bool)):
            return super().or_(other)
        else:
            return NotImplemented
    
    def not_(self):
        return Symbol(super().not_(), operator='not', operands=[self])
    
    def __repr__(self):
        return BooleanExpression.__repr__(self)

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
    diag_not_start = bool_and(bool_not(start), diag)
    d = diag & bool_not(start)
    print(repr(d))
    print(f"Boolean ops: True == {diag_not_start(s1)}")
    print(f"Boolean ops: False == {diag_not_start(s2)}")
    print(f"s1 belongs to {diag.name}: {diag(s1)} == True")
    print(f"s2 belongs to {diag.name}: {diag(s2)} == False")
    x_0 = x == 0 
    x_1 = x + 1
    print(f"z is start: {start(State(data=np.array([0,0])))} == True")
    print(f"s1 is start: {start(s1)} == False")
    print(f"s2 is not goal: {not_goal(s2)} == True")
    print(f"s1 is not goal: {not_goal(s1)} == False")