'''
    Conditional Expression Class:
        - It allows to create a statement of the form 
        when (Boolean Expression) then:
            <expressions>
        otherwise:
            <expressions>

    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: January 2021
'''
from lmdp.grounding.expressions.ExpressionsClass import Expression
from lmdp.grounding.booleans.BooleanFunClass import BooleanExpression

class ConditionalExpression(Expression):
    def __init__(self, boolean_expression):
        self._boolean_expression = boolean_expression
    
    def __enter__(self):    
        return self

    def __exit__(self, type, value, traceback):
        pass
    
    def otherwise(self):
        pass

    def subpolicy(self, initiation=None, policy=None, termination=None, name=None):
        pass
    
    def goal(self, symbol=None, name=None):
        pass

    def state_feature(self, expression=None, name=None):
        pass

    def symbol(self, expression=None, name=None):
        pass

    def markov_feature(self, expression=None, name=None):
        pass

    def policy(self, state=None, action=None):
        pass

    def reward(self, sas_expression=None):
        pass

    def value(self, sa_expression=None):
        pass
