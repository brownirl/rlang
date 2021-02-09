'''
    Boolean Expression Class
        Boolean Functions 
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: January 2021
'''

from lmdp.grounding.expressions.ExpressionsClass import Expression

class BooleanExpression(Expression):
    def __init__(self, fun, domain):
        Expression.__init__(self, fun, domain=domain, codomain=["boolean"])
        
    def and_(self, other):
        if(isinstance(other, BooleanExpression) or isinstance(other, Expression)):
            return BooleanExpression(lambda **args: self.__call__(**args) and other(**args), domain=self.domain() + other.domain())
        elif (isinstance(other, bool)):
            return BooleanExpression(lambda **args: self.__call__(**args) or other, domain=self.domain()) 
        else:
            raise other.__name__() + " must be a Boolean Expression or bool"
   
    def or_(self, other):
        if(isinstance(other, BooleanExpression)):
            return BooleanExpression(lambda **args: self.__call__(**args) or other(**args), domain=self.domain() + other.domain())
        elif (isinstance(other, bool)):
            return BooleanExpression(lambda **args: self.__call__(**args) or other, domain=self.domain())
        else:
            raise other.__name__() + " must be a Boolean Expression or bool"
    
    def not_(self):
         return BooleanExpression(lambda **args: not self.__call__(**args), domain=self.domain())

    def __and__(self, other):
        return self.and_(other)
    
    def __or__(self, other):
        return self.or_(other)
    
    def __not__(self, other):
        return self.not_()


    def __compose__(self, expression):
        if(self.domain == expression.codomain): #composable
            return BooleanExpression(lambda **args: self.__call__(expression(**args)), domain=expression.domain())
        else:
            return NotImplemented

any_state = BooleanExpression(lambda **args: True, domain=["state"])
any_action = BooleanExpression(lambda **args: True, domain=["action"])
any_next_state = BooleanExpression(lambda **args: True, domain=["next_state"])
TrueBooleanExp = BooleanExpression(lambda **args: True,  domain=[])