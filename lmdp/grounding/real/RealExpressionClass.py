'''
    Real Expression:
        Real Vector Functions 
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: January 2021
'''
import sys, os
sys.path.append(os.path.abspath("./"))
import numpy as np
from lmdp.grounding.expressions.ExpressionsClass import Expression
from lmdp.grounding.booleans.BooleanFunClass import BooleanExpression
from collections.abc import Sequence

class RealExpression(Expression):
    def __init__(self, expression_fun, dimension=1, domain=[], codomain=["real"]):
        # if(isinstance(expression_fun, Expression)):
        #     domain.append(expression_fun.domain())
        self.__dim = dimension
        Expression.__init__(self, expression_fun, domain, codomain)

    
    def dim(self):
        return self.__dim

    def __add__(self, other):
        domain = self.domain()
        if (isinstance(other, RealExpression)):
            if(other.dim == self.dim()):
                domain += other.domain()
                f = lambda **args: self.__call__(**args) + other(**args)
            else:
                raise "Shapes are not compatible"
        elif (isinstance(other, float) or isinstance(other, int)):
            f = lambda **args: self.__call__(**args) + other
        elif (isinstance(other, np.ndarray)):
            if(other.shape == (self.dim(),)):
                f = lambda **args: self.__call__(**args) + other
            else:
                raise "Shapes are not compatible"
        elif (isinstance(other, Sequence)):
            if(len(other) == self.dim()):
                f = lambda **args: self.__call__(**args) + np.array(other)
            else:
                raise "Shapes are not compatible"
        else:
            return NotImplemented
        return RealExpression(f, dimension=self.dim(), domain=domain)

    def __sub__(self, other):
        domain = self.domain()
        if (isinstance(other, RealExpression)):
            if(other.dim() == self.dim()):
                domain += other.domain()
                f = lambda **args: self.__call__(**args) - other(**args)
            else:
                raise "Shapes are not compatible"
        elif (isinstance(other, float) or isinstance(other, int)):
            f = lambda **args: self.__call__(**args) - other
        elif (isinstance(other, np.ndarray)):
            if(other.shape == (self.dim(),)):
                f = lambda **args: self.__call__(**args) - other
            else:
                raise "Shapes are not compatible"
        elif (isinstance(other, Sequence)):
            if(len(other) == self.dim()):
                f = lambda **args: self.__call__(**args) - np.array(other)
            else:
                raise "Shapes are not compatible"
        else:
            return NotImplemented
        return RealExpression(f, self.dim(), domain=domain)

    def __mul__(self, other):
        domain = self.domain()
        if (isinstance(other, RealExpression)):
            if(other.dim() == self.dim()):
                domain += other.domain()
                f = lambda **args: self.__call__(**args) * other(**args)
            else:
                raise "Shapes are not compatible"
        elif (isinstance(other, float) or isinstance(other, int)):
            f = lambda **args: self.__call__(**args) * other
        elif (isinstance(other, np.ndarray)):
            if(other.shape == (self.dim(),)):
                f = lambda **args: self.__call__(**args) *  other
            else:
                raise "Shapes are not compatible"
        elif (isinstance(other, Sequence)):
            if(len(other) == self.dim()):
                f = lambda **args: self.__call__(**args) * np.array(other)
            else:
                raise "Shapes are not compatible"
        else:
            return NotImplemented
        return RealExpression(f, self.dim(), domain=domain)

    def __truediv__(self, other):
        domain = self.domain()
        if (isinstance(other, RealExpression)):
            if(other.dim() == self.dim()):
                domain += other.domain()
                f = lambda **args: self.__call__(**args) / other(**args)
            else:
                raise "Shapes are not compatible"
        elif (isinstance(other, float) or isinstance(other, int)):
            f =  lambda **args: self.__call__(**args) / other
        elif (isinstance(other, np.ndarray)):
            if(other.shape == (self.dim(),)):
                f = lambda **args: self.__call__(**args) / other
            else:
                raise "Shapes are not compatible"
        elif (isinstance(other, Sequence)):
            if(len(other) == self.dim()):
                f = lambda **args: self.__call__(**args) / np.array(other)
            else:
                raise "Shapes are not compatible"
        else:
            return NotImplemented
        return RealExpression(f, self.dim(), domain=domain)

    def __lt__(self, other):
        if (self.dim() == 1):
            if (isinstance(other, RealExpression)):
                if(other.dim() == self.dim()):
                    return BooleanExpression(lambda **args: self.__call__(**args) < other(**args), domain=self.domain()+other.domain())
                else:
                    raise "Comparison not defined"
            elif (isinstance(other, float) or isinstance(other, int)):
                return BooleanExpression(lambda **args: self.__call__(**args) < other, domain=self.domain())
            else:
                return NotImplemented
        else:
            raise "Comparison not defined for vector groundings"

    def __le__(self, other):
        if (self.dim() == 1):
            if (isinstance(other, RealExpression)):
                if(other.dim() == self.dim()):
                    return BooleanExpression(lambda **args: self.__call__(**args) <= other(**args), domain=self.domain()+other.domain())
                else:
                    raise "Comparison not defined"
            elif (isinstance(other, float) or isinstance(other, int)):
                return BooleanExpression(lambda **args: self.__call__(**args) <= other, domain=self.domain())
            else:
                return NotImplemented
        else:
            raise "Comparison not defined for vector groundings"

    def __eq__(self, other):
        if (isinstance(other, RealExpression)):
            if(other.dim() == self.dim()):
                return BooleanExpression(lambda **args: np.array_equal(self.__call__(**args), other(**args)), domain=self.domain()+other.domain())
            else:
                raise "Length must be equal"
        elif (isinstance(other, float) or isinstance(other, int)):
            if (self.dim() == 1):
                return BooleanExpression(lambda **args: self.__call__(**args) == other, domain=self.domain())
            else:
                raise "Length must be equal"
        elif (isinstance(other, np.ndarray)):
            if(other.shape == (self.dim(),)):
                return BooleanExpression(lambda **args: np.array_equal(self.__call__(**args), other), domain=self.domain())
            else:
                raise "Length must be equal"
        elif (isinstance(other, (list,tuple))):
            if(len(other) == self.dim()):
                return BooleanExpression(lambda **args: np.array_equal(self.__call__(**args), other), domain=self.domain())
            else:
                raise "Length must be equal"
        else:
            return NotImplemented

    def __ne__(self, other):
        if (isinstance(other, RealExpression)):
            if(other.dim() == self.dim()):
                return BooleanExpression(lambda **args: not np.array_equal(self.__call__(**args), other(**args)), domain=self.domain()+other.domain())
            else:
                raise "Length must be equal"
        elif (isinstance(other, float) or isinstance(other, int)):
            if (self.dim() == 1):
                return BooleanExpression(lambda **args: self.__call__(**args) == other, domain=self.domain())
            else:
                raise "Length must be equal"
        elif (isinstance(other, np.ndarray)):
            if(other.shape == (self.dim(),)):
                return BooleanExpression(lambda **args: not np.array_equal(self.__call__(**args), other), domain=self.domain())
            else:
                raise "Length must be equal"
        elif (isinstance(other, (tuple, list))):
            if(len(other) == self.dim()):
                return BooleanExpression(lambda **args: not np.array_equal(self.__call__(**args), other), domain=self.domain())
            else:
                raise "Length must be equal"
        else:
            return NotImplemented

    def __gt__(self, other):
        if (self.dim() == 1):
            if (isinstance(other, RealExpression)):
                if(other.dim() == self.dim()):
                    return BooleanExpression(lambda **args: self.__call__(**args) > other(**args), domain=self.domain()+other.domain())
                else:
                    raise "Comparison not defined"
            elif (isinstance(other, float) or isinstance(other, int)):
                return BooleanExpression(lambda **args: self.__call__(**args) > other, domain=self.domain())
            else:
                return NotImplemented
        else:
            raise "Comparison not defined for vector groundings"

    def __ge__(self, other):
        if (self.dim() == 1):
            if (isinstance(other, RealExpression)):
                if(other.dim() == self.dim()):
                    return BooleanExpression(lambda **args: self.__call__(**args) >= other(**args), domain=self.domain()+other.domain())
                else:
                    raise "Comparison not defined"
            elif (isinstance(other, float) or isinstance(other, int)):
                return BooleanExpression(lambda **args: self.__call__(**args) >= other, domain=self.domain())
            else:
                return NotImplemented
        else:
            raise "Comparison not defined for vector groundings"
    
    def __compose__(self, expression):
        if(self.domain == expression.codomain): #composable
            return RealExpression(lambda **args: self.__call__(expression(**args)), domain=expression.domain())
        else:
            return NotImplemented

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

if __name__ == "__main__":
    constant = RealExpression(lambda **args: 1.0)
    print(f"{constant()} == 1.0")