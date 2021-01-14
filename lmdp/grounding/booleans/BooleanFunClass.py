'''
    Boolean Expression Class
        Boolean Functions 
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: January 2021
'''

from lmdp.grounding.ExpressionsClass import Expression

class BooleanExpression(Expression):
    def __init__(self, fun, domain):
        Expression.__init__(self, fun, domain=domain, codomain=["Boolean"])
        
    def and_(self, other):
        if(isinstance(other, BooleanExpression)):
            return BooleanExpression(lambda *args: self.__call__(*args) and other(*args), domain=self.domain() + other.domain())
        elif (isinstance(other, bool)):
            return BooleanExpression(lambda *args: self.__call__(*args) or other, domain=self.domain()) 
        else:
            raise other.__name__() + " must be a Boolean Expression or bool"
   
    def or_(self, other):
        if(isinstance(other, BooleanExpression)):
            return BooleanExpression(lambda *args: self.__call__(*args) or other(*args), domain=self.domain() + other.domain())
        elif (isinstance(other, bool)):
            return BooleanExpression(lambda *args: self.__call__(*args) or other, domain=self.domain())
        else:
            raise other.__name__() + " must be a Boolean Expression or bool"
    
    def not_(self):
         return BooleanExpression(lambda *args: not self.__call__(*args), domain=self.domain())