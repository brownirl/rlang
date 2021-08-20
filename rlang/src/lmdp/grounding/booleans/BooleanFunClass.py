'''
    Boolean Expression Class
        Boolean Functions 
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: January 2021
'''
import sys, os

sys.path.append(os.path.abspath("../rlang/src/"))

from lmdp.grounding.expressions.ExpressionsClass import Expression
from functools import reduce, partial
import numpy as np
import torch


class BooleanExpression(Expression):
    _id = 0

    #REVIEW: find out if fun needs to return a boolean
    def __init__(self, fun, domain, name=None, operator=None, operands=None):
        """
        Initializes a Boolean Expression

        Args:
            fun (function): 
            domain (list of string): state, action, next-state
            name (string, optional): name of the Boolean Expression. Defaults to 'boolean-f-' + the class id.
            operator (string, optional): represents the logical operator connecting operands. Defaults to None.
            operands (a list of Boolean Expressions, optional): a list of Boolean Expressions joined by the operator. Defaults to None.
        """
        self._operator = operator
        self._operands = operands
        if name is None:
            name = 'boolean-f-' + str(BooleanExpression._id)
        BooleanExpression._id += 1
        Expression.__init__(self, fun, domain=domain, codomain=["boolean"], name=name)

    def and_(self, other):
        """ 
        Represents the logical operator 'and' to join two boolean expressions

        Args:
            other (Expression): any BooleanExpression, Expression, or bool

        Raises:
            other.__name__: if other is not a boolean, BooleanExpression or Expression, raise other.__name__()

        Returns:
            BooleanExpression: fun is a partial function that applies _conj to self and other; 
                                domain is the combination of the domains of self and other;
                                operator is 'and';
                                operands is a list of self and other
        """
        # Short-circuiting
        # if (self == BOOL_TRUE or other == BOOL_TRUE):
        #     return self
        # if (self == BOOL_FALSE or other == BOOL_FALSE):
        #     return BOOL_FALSE
        # generate function 
        if isinstance(other, BooleanExpression) or isinstance(other, Expression):
            # TODO: This breaks when self is False and other is True
            return BooleanExpression(partial(_conj, self, other),
                                     domain=self.domain() + other.domain(),
                                     operator='and',
                                     operands=[self, other])
        elif isinstance(other, bool):
            if not other:
                return BOOL_FALSE
            return self
        else:
            raise other.__name__() + " must be a Boolean Expression or bool"

    def or_(self, other):
        """ 
        Represents the logical operator 'or' to join two boolean expressions

        Args:
            other (Expression): any BooleanExpression, Expression, or bool

        Raises:
            other.__name__: if other is not a boolean, BooleanExpression or Expression, raise other.__name__()

        Returns:
            BooleanExpression: fun is a partial function that applies _disj to self and other; 
                                domain is the combination of the domains of self and other;
                                operator is 'or';
                                operands is a list of self and other
        """
        # Short-circuiting
        # if (self == BOOL_TRUE or other == BOOL_TRUE):
        #     return BOOL_TRUE
        # if (self == BOOL_FALSE or other == BOOL_FALSE):
        #     return self
        # generate function 
        if isinstance(other, BooleanExpression):
            return BooleanExpression(partial(_disj, self, other),
                                     domain=self.domain() + other.domain(),
                                     operator='or',
                                     operands=[self, other])
        elif isinstance(other, bool):
            if other:
                return BOOL_TRUE
            return self
        else:
            raise other.__name__() + " must be a Boolean Expression or bool"

    def not_(self):
        """
        Represents the logic operator "not" to negate an Boolean Expression

        Returns:
            BooleanExpression: fun is a partial function that applies _neg to self; 
                                domain is self.domain();
                                operator is 'not';
                                operands is a list of self
        """
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

    # Python's "and" is not intuitive: https://docs.python.org/3.7/library/stdtypes.html#boolean-operations-and-or-not
    def __bool__(self):
        if self._name == 'True':
            return True
        elif self._name == 'False':
            return False

    def __repr__(self):
        if self._operator is not None:  # derived boolean function
            if self._operator != 'not':
                return f"({repr(self._operands[0])} {self._operator} {repr(self._operands[1])})"
            else:
                return f"{self._operator} {repr(self._operands[0])}"
        return self._name


def grounded_or(result_1, result_2):
    """[summary]

    Args:
        result_1 (bool, or (np.ndarray, torch.Tensor)): [description]
        result_2 (bool, or (np.ndarray, torch.Tensor)): [description]

    Returns:
        bool or Boolean Expression: [description]
    """
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
    """
    Joins multiple Expressions or Boolean Expression using the logical operator "and"

    Returns:
        Boolean Expression: from Expressions joined with "and"
    """
    b_exps = map(cast_to_boolean, exps)
    return reduce(lambda a, b: a.__and__(b), b_exps)


def bool_or(*exps):
    """
    Joins multiple Expressions or Boolean Expression using the logical operator "or"

    Returns:
        Boolean Expression: from Expressions joined with "or"
    """
    b_exps = map(cast_to_boolean, exps)
    return reduce(lambda a, b: a.__or__(b), b_exps)


def bool_not(exp):
    """
    Negates an Expression using the logical operator "not"

    Returns:
        Boolean Expression: negated Expression
    """
    exp = cast_to_boolean(exp)
    return exp.not_()


def cast_to_boolean(expression):
    """
    Casts an Expression to a Boolean Expression

    Args:
        expression (Expresssion): Expression with "boolean" in its codomain

    Returns:
        Boolean Expression: expression as a Boolean Expression
    """
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
