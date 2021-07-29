'''
    Boolean Expression Class
        Boolean Functions 
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: January 2021
'''
import sys, os

sys.path.append(os.path.abspath("/"))
from lmdp.grounding.expressions.ExpressionsClass import Expression
from functools import reduce, partial
import numpy as np
import torch


class BooleanExpression(Expression):
    _id = 0

    def __init__(self, fun, domain, name=None, operator=None, operands=None):
        self._operator = operator
        self._operands = operands
        if name is None:
            name = 'boolean-f-' + str(BooleanExpression._id)
        BooleanExpression._id += 1
        Expression.__init__(self, fun, domain=domain, codomain=["boolean"], name=name)

    def and_(self, other):
        # Short-circuiting
        # if (self == BOOL_TRUE or other == BOOL_TRUE):
        #     return self
        # if (self == BOOL_FALSE or other == BOOL_FALSE):
        #     return BOOL_FALSE
        # generate function 
        if (isinstance(other, BooleanExpression) or isinstance(other, Expression)):
            return BooleanExpression(partial(_conj, self, other),
                                     domain=self.domain() + other.domain(),
                                     operator='and',
                                     operands=[self, other])
        elif (isinstance(other, bool)):
            if not other:
                return BOOL_FALSE
            return self
        else:
            raise other.__name__() + " must be a Boolean Expression or bool"

    def or_(self, other):
        # Short-circuiting
        # if (self == BOOL_TRUE or other == BOOL_TRUE):
        #     return BOOL_TRUE
        # if (self == BOOL_FALSE or other == BOOL_FALSE):
        #     return self
        # generate function 
        if (isinstance(other, BooleanExpression)):
            return BooleanExpression(partial(_conj, self, other),
                                     domain=self.domain() + other.domain(),
                                     operator='or',
                                     operands=[self, other])
        elif (isinstance(other, bool)):
            if other:
                return BOOL_TRUE
            return self
        else:
            raise other.__name__() + " must be a Boolean Expression or bool"

    def not_(self):
        if self._operator is not None and self._operator == 'not':
            return self._operands[0]
        return BooleanExpression(partial(_neg, self),
                                 domain=self.domain(),
                                 operator='not',
                                 operands=[self, ])

    def __and__(self, other):
        return self.and_(other)

    def __or__(self, other):
        return self.or_(other)

    def __not__(self):
        return self.not_()

    def __repr__(self):
        if self._operator is not None:  # derived boolean function
            if self._operator != 'not':
                return f"({repr(self._operands[0])} {self._operator} {repr(self._operands[1])})"
            else:
                return f"{self._operator} {repr(self._operands[0])}"
        return self._name


def grounded_or(result_1, result_2):
    if isinstance(result_1, bool) and isinstance(result_2, bool):  # boolean operation
        return result_1 or result_2
    if isinstance(result_1, bool) and isinstance(result_2, (np.ndarray, torch.Tensor)):
        return result_2.__or__(result_1)
    if isinstance(result_2, bool) and isinstance(result_1, (np.ndarray, torch.Tensor)):
        return result_1.__or__(result_2)
    return result_1 | result_2


def grounded_and(result_1, result_2):
    if isinstance(result_1, bool) and isinstance(result_2, bool):  # boolean operation
        return result_1 and result_2
    if isinstance(result_1, bool) and isinstance(result_2, (np.ndarray, torch.Tensor)):
        return result_2.__and__(result_1)
    if isinstance(result_2, bool) and isinstance(result_1, (np.ndarray, torch.Tensor)):
        return result_1.__and__(result_2)
    return result_1 & result_2


def _disj(f1, f2, **args):
    return grounded_or(f1(**args), f2(**args))


def _conj(f1, f2, **args):
    return grounded_and(f1(**args), f2(**args))


def _neg(f, **args):
    import numpy as np
    try:
        return not f(**args)
    except:
        return np.logical_not(f(**args))


def bool_and(*exps):
    b_exps = map(cast_to_boolean, exps)
    return reduce(lambda a, b: a.__and__(b), b_exps)


def bool_or(*exps):
    b_exps = map(cast_to_boolean, exps)
    return reduce(lambda a, b: a.__or__(b), b_exps)


def bool_not(exp):
    exp = cast_to_boolean(exp)
    return exp.not_()


def cast_to_boolean(expression):
    assert "boolean" in expression.codomain()
    return BooleanExpression(expression, domain=expression.domain()) if not isinstance(expression,
                                                                                       BooleanExpression) else expression


### CONSTANTS #####
BOOL_TRUE = BooleanExpression(lambda **args: True, domain=[], name='True')
BOOL_FALSE = BooleanExpression(lambda **args: False, domain=[], name='False')
any_action = BooleanExpression(BOOL_TRUE, domain=["action"], name='any_action')
any_next_state = BooleanExpression(BOOL_TRUE, domain=["next_state"], name='any_next_state')


def boolean(domain=[]):
    def __boolean_dec(fun):
        return BooleanExpression(fun, domain=domain, name=fun.__name__)

    return __boolean_dec
