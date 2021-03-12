'''
    Boolean Expression Class
        Boolean Functions 
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: January 2021
'''

from lmdp.grounding.expressions.ExpressionsClass import Expression
from functools import reduce, partial




class BooleanExpression(Expression):
    def __init__(self, fun, domain):
        Expression.__init__(self, fun, domain=domain, codomain=["boolean"])
        
    def and_(self, other):
        if(isinstance(other, BooleanExpression) or isinstance(other, Expression)):
            return BooleanExpression(partial(_conj, self, other), domain=self.domain() + other.domain())
        elif (isinstance(other, bool)):
            if not other:
                return bool_false
            return self
        else:
            raise other.__name__() + " must be a Boolean Expression or bool"
   
    def or_(self, other):
        if(isinstance(other, BooleanExpression)):
            return BooleanExpression(partial(_disj, self, other), domain=self.domain() + other.domain())
        elif (isinstance(other, bool)):
            if other:
                return bool_true
            return self
        else:
            raise other.__name__() + " must be a Boolean Expression or bool"
    
    def not_(self):
         return BooleanExpression(partial(_neg, self), domain=self.domain())

    def __and__(self, other):
        return self.and_(other)
    
    def __or__(self, other):
        return self.or_(other)
    
    def __not__(self):
        return self.not_()



    # def __compose__(self, expression):
    #     if(self.domain == expression.codomain): #composable
    #         return BooleanExpression(lambda **args: self.__call__(expression(**args)), domain=expression.domain())
    #     else:
    #         return NotImplemented

def _disj(f1, f2, **args):
    return f1(**args) or f2(**args)

def _conj(f1, f2, **args):
    return f1(**args) and f2(**args)

def _neg(f, **args):
    return not f(**args)

def bool_and(*exps):
    b_exps = map(cast_to_boolean, exps)
    return reduce(lambda a, b: a.__and__(b), b_exps)
    # exp1 = cast_to_boolean(exp1)
    # exp2 = cast_to_boolean(exp2)
    # return exp1.__and__(exp2)

def bool_or(*exps):
    b_exps = map(cast_to_boolean, exps)
    return reduce(lambda a, b: a.__or__(b), b_exps)

def bool_not(exp):
    exp = cast_to_boolean(exp)
    return exp.not_()

def cast_to_boolean(expression):
    assert "boolean" in expression.codomain()
    return BooleanExpression(expression, domain=expression.domain()) if not isinstance(expression, BooleanExpression) else expression


### CONSTANTS #####
any_state = BooleanExpression(lambda **args: True, domain=["state"])
any_action = BooleanExpression(lambda **args: True, domain=["action"])
any_next_state = BooleanExpression(lambda **args: True, domain=["next_state"])
bool_true = BooleanExpression(lambda **args: True,  domain=[])
bool_false = BooleanExpression(lambda **args: False, domain=[])
