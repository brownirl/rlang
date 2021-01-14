'''
    Real Expression:
        Real Vector Functions 
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: January 2021
'''

import numpy as np
from lmdp.grounding.ExpressionsClass import Expression
from lmdp.grounding.booleans.BooleanFunClass import BooleanExpression

class RealExpression(Expression):
    def __init__(self, expression_fun, dimension=1, domain=[], codomain=["Real"]):
        if(isinstance(expression_fun, Expression)):
            domain.append(expression_fun.domain())
        self._dim = dimension
        Expression.__init__(self, expression_fun, domain, codomain)

    def __add__(self, other):
        domain = self.domain()
        if (isinstance(other, RealExpression)):
            if(other._dim == self._dim):
                domain += other.domain()
                f = lambda *args: self.__call__(*args) + other(*args)
            else:
                raise "Shapes are not compatible"
        elif (isinstance(other, float) or isinstance(other, int)):
            f = lambda *args: self.__call__(*args) + other
        elif (isinstance(other, np.ndarray)):
            if(other.shape == (self._dim,)):
                f = lambda *args: self.__call__(*args) + other
            else:
                raise "Shapes are not compatible"
        else:
            raise NotImplementedError
        return RealExpression(f, dimension=self._dim(), domain=domain)

    def __sub__(self, other):
        domain = self.domain()
        if (isinstance(other, RealExpression)):
            if(other.dim() == self._dim()):
                domain += other.domain()
                f = lambda *args: self.__call__(*args) - other(*args)
            else:
                raise "Shapes are not compatible"
        elif (isinstance(other, float) or isinstance(other, int)):
            f = lambda *args: self.__call__(*args) - other
        elif (isinstance(other, np.ndarray)):
            if(other.shape == (self._dim(),)):
                f = lambda *args: self.__call__(*args) - other
            else:
                raise "Shapes are not compatible"
        else:
            raise NotImplementedError
        return RealExpression(f, self._dim(), domain=domain)

    def __mul__(self, other):
        domain = self.domain()
        if (isinstance(other, RealExpression)):
            if(other._dim() == self._dim()):
                domain += other.domain()
                f = lambda *args: self.__call__(*args) * other(*args)
            else:
                raise "Shapes are not compatible"
        elif (isinstance(other, float) or isinstance(other, int)):
            f = lambda *args: self.__call__(*args) * other
        elif (isinstance(other, np.ndarray)):
            if(other.shape == (self._dim(),)):
                f = lambda *args: self.__call__(*args) *  other
            else:
                raise "Shapes are not compatible"
        else:
            raise NotImplementedError
        return RealExpression(f, self._dim(), domain=domain)

    def __truediv__(self, other):
        domain = self.domain()
        if (isinstance(other, RealExpression)):
            if(other._dim() == self._dim()):
                domain += other.domain()
                f = lambda *args: self.__call__(*args) / other(*args)
            else:
                raise "Shapes are not compatible"
        elif (isinstance(other, float) or isinstance(other, int)):
            f =  lambda *args: self.__call__(*args) / other
        elif (isinstance(other, np.ndarray)):
            if(other.shape == (self._dim(),)):
                f = lambda *args: self.__call__(*args) / other
            else:
                raise "Shapes are not compatible"
        else:
            raise NotImplementedError
        return RealExpression(f, self._dim(), domain=domain)

    def __lt__(self, other):
        if (self._dim() == 1):
            if (isinstance(other, RealExpression)):
                if(other._dim() == self._dim()):
                    return BooleanExpression(lambda *args: self.__call__(*args) < other(*args), domain=self.domain()+other.domain())
                else:
                    raise "Comparison not defined"
            elif (isinstance(other, float) or isinstance(other, int)):
                return BooleanExpression(lambda *args: self.__call__(*args) < other, domain=self.domain())
            else:
                raise NotImplementedError
        else:
            raise "Comparison not defined for vector groundings"

    def __le__(self, other):
        if (self._dim() == 1):
            if (isinstance(other, RealExpression)):
                if(other._dim() == self._dim()):
                    return BooleanExpression(lambda *args: self.__call__(*args) <= other(*args), domain=self.domain()+other.domain())
                else:
                    raise "Comparison not defined"
            elif (isinstance(other, float) or isinstance(other, int)):
                return BooleanExpression(lambda *args: self.__call__(*args) <= other, domain=self.domain())
            else:
                raise NotImplementedError
        else:
            raise "Comparison not defined for vector groundings"

    def __eq__(self, other):
        if (isinstance(other, RealExpression)):
            if(other._dim() == self._dim()):
                return BooleanExpression(lambda *args: np.array_equal(self.__call__(*args), other(*args)), domain=self.domain()+other.domain())
            else:
                raise "Length must be equal"
        elif (isinstance(other, float) or isinstance(other, int)):
            if (self._dim() == 1):
                return BooleanExpression(lambda *args: self.__call__(*args) == other, domain=self.domain())
            else:
                raise "Length must be equal"
        elif (isinstance(other, np.ndarray)):
            if(other.shape == (self._dim(),)):
                return BooleanExpression(lambda *args: np.array_equal(self.__call__(*args), other), domain=self.domain)
            else:
                raise "Length must be equal"
        else:
            raise NotImplementedError

    def __ne__(self, other):
        if (isinstance(other, RealExpression)):
            if(other._dim() == self._dim()):
                return BooleanExpression(lambda *args: not np.array_equal(self.__call__(*args), other(*args)), domain=self.domain()+other.domain())
            else:
                raise "Length must be equal"
        elif (isinstance(other, float) or isinstance(other, int)):
            if (self._dim() == 1):
                return BooleanExpression(lambda *args: self.__call__(*args) == other, domain=self.domain())
            else:
                raise "Length must be equal"
        elif (isinstance(other, np.ndarray)):
            if(other.shape == (self._dim(),)):
                return BooleanExpression(lambda *args: not np.array_equal(self.__call__(*args), other), domain=self.domain())
            else:
                raise "Length must be equal"
        else:
            raise NotImplementedError

    def __gt__(self, other):
        if (self._dim() == 1):
            if (isinstance(other, RealExpression)):
                if(other._dim() == self._dim()):
                    return BooleanExpression(lambda *args: self.__call__(*args) > other(*args), domain=self.domain()+other.domain())
                else:
                    raise "Comparison not defined"
            elif (isinstance(other, float) or isinstance(other, int)):
                return BooleanExpression(lambda *args: self.__call__(*args) > other, domain=self.domain())
            else:
                raise NotImplementedError
        else:
            raise "Comparison not defined for vector groundings"

    def __ge__(self, other):
        if (self._dim() == 1):
            if (isinstance(other, RealExpression)):
                if(other._dim() == self._dim()):
                    return BooleanExpression(lambda *args: self.__call__(*args) >= other(*args), domain=self.domain()+other.domain())
                else:
                    raise "Comparison not defined"
            elif (isinstance(other, float) or isinstance(other, int)):
                return BooleanExpression(lambda *args: self.__call__(*args) >= other, domain=self.domain())
            else:
                raise NotImplementedError
        else:
            raise "Comparison not defined for vector groundings"
    
    def __floordiv__(self, other):
        raise NotImplementedError
    def __mod__(self, other):
        raise NotImplementedError
    def __divmod__(self, other):
        raise NotImplementedError
    def __pow__(self, other):
        raise NotImplementedError
    def __lshift__(self, other):
        raise NotImplementedError
    def __rshift__(self, other):
        raise NotImplementedError
    def __and__(self, other):
        raise NotImplementedError
    def __xor__(self, other):
        raise NotImplementedError
    def __or__(self, other):
        raise NotImplementedError
    def __matmul__(self, other):
        raise NotImplementedError