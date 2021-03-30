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
from lmdp.utils.expression_utils import Domain
from lmdp.utils.space import BatchedVector, BatchedTuple
from collections.abc import Sequence

class RealExpression(Expression):
    _id = 0
    def __init__(self, expression_fun, dimension=1, domain=[], codomain=["real"], name=None, operator=None, operands=None):
        self.__dim = dimension
        self._operator = operator
        self._operands = operands

        if name is None:
            name = "real-exp-" + str(RealExpression._id)
            RealExpression._id += 1
        Expression.__init__(self, expression_fun, domain, codomain, name=name)
    
    def dim(self):
        return self.__dim

    def __add__(self, other):
        domain = self.domain()
        operands = [self, other]
        if (isinstance(other, RealExpression)):
            if(other.dim() == self.dim()):
                domain += other.domain()
                f = lambda **args: self.__call__(**args) + other(**args)
            else:
                raise "Shapes are not compatible"
        elif (isinstance(other, (float, int))):
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
        return RealExpression(f, dimension=self.dim(), domain=domain, operator='+', operands=operands)

    def __sub__(self, other):
        domain = self.domain()
        operands = [self, other]
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
        return RealExpression(f, self.dim(), domain=domain, operator='-', operands=operands)

    def __mul__(self, other):
        domain = self.domain()
        operands=[self, other]
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
        return RealExpression(f, self.dim(), domain=domain, operator='*', operands=operands)

    def __truediv__(self, other):
        domain = self.domain()
        operands=[self, other]
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
        return RealExpression(f, self.dim(), domain=domain, operator='/', operands=operands)

    def __lt__(self, other):
        operands = [self, other]
        if (self.dim() == 1):
            if (isinstance(other, RealExpression)):
                if(other.dim() == self.dim()):
                    return BooleanExpression(lambda **args: self.__call__(**args) < other(**args), domain=self.domain()+other.domain(), operator='<', operands=operands)
                else:
                    raise "Comparison not defined"
            elif (isinstance(other, float) or isinstance(other, int)):
                return BooleanExpression(lambda **args: self.__call__(**args) < other, domain=self.domain(), operator='<', operands=operands)
            else:
                return NotImplemented
        else:
            raise "Comparison not defined for vector groundings"

    def __le__(self, other):
        operands=[self, other]
        if (self.dim() == 1):
            if (isinstance(other, RealExpression)):
                if(other.dim() == self.dim()):
                    return BooleanExpression(lambda **args: self.__call__(**args) <= other(**args), 
                                                domain=self.domain()+other.domain(), 
                                                operator='<=', operands=operands)
                else:
                    raise "Comparison not defined"
            elif (isinstance(other, float) or isinstance(other, int)):
                return BooleanExpression(lambda **args: self.__call__(**args) <= other, 
                                        domain=self.domain(), 
                                        operator='<', operands=operands)
            else:
                return NotImplemented
        else:
            raise "Comparison not defined for vector groundings"

    def __eq__(self, other):
        operands = [self, other]
        if (isinstance(other, RealExpression)):
            if(other.dim() == self.dim()):
                return BooleanExpression(lambda **args: np.array_equal(self.__call__(**args), other(**args)), 
                                        domain=self.domain()+other.domain(), 
                                        operator='==', operands=operands)
            else:
                raise "Length must be equal"
        elif (isinstance(other, float) or isinstance(other, int)):
            if (self.dim() == 1):
                return BooleanExpression(lambda **args: self.__call__(**args) == other,
                                         domain=self.domain(), 
                                         operator='==', operands=operands)
            else:
                raise "Length must be equal"
        elif (isinstance(other, np.ndarray)):
            if(other.shape == (self.dim(),)):
                return BooleanExpression(lambda **args: np.array_equal(self.__call__(**args), other), 
                                         domain=self.domain(),
                                         operator='==', operands=operands)
            else:
                raise "Length must be equal"
        elif (isinstance(other, (list,tuple))):
            if(len(other) == self.dim()):
                return BooleanExpression(lambda **args: np.array_equal(self.__call__(**args), other),
                                         domain=self.domain(),
                                         operator='==', operands=operands)
            else:
                raise "Length must be equal"
        else:
            return NotImplemented

    def __ne__(self, other):
        operands = [self, other]
        if (isinstance(other, RealExpression)):
            if(other.dim() == self.dim()):
                return BooleanExpression(lambda **args: not np.array_equal(self.__call__(**args), other(**args)), 
                                         domain=self.domain()+other.domain(),
                                         operator='!=', operands=operands)
            else:
                raise "Length must be equal"
        elif (isinstance(other, float) or isinstance(other, int)):
            if (self.dim() == 1):
                return BooleanExpression(lambda **args: self.__call__(**args) == other, domain=self.domain())
            else:
                raise "Length must be equal"
        elif (isinstance(other, np.ndarray)):
            if(other.shape == (self.dim(),)):
                return BooleanExpression(lambda **args: not np.array_equal(self.__call__(**args), other), 
                                         domain=self.domain(),
                                         operator='!=', operands=operands)
            else:
                raise "Length must be equal"
        elif (isinstance(other, (tuple, list))):
            if(len(other) == self.dim()):
                return BooleanExpression(lambda **args: not np.array_equal(self.__call__(**args), other),
                                         domain=self.domain(),
                                         operator='!=', operands=operands)
            else:
                raise "Length must be equal"
        else:
            return NotImplemented

    def __gt__(self, other):
        operands = [self, other]
        if (self.dim() == 1):
            if (isinstance(other, RealExpression)):
                if(other.dim() == self.dim()):
                    return BooleanExpression(lambda **args: self.__call__(**args) > other(**args), 
                                            domain=self.domain()+other.domain(),
                                            operator='>', operands=operands)
                else:
                    raise "Comparison not defined"
            elif (isinstance(other, float) or isinstance(other, int)):
                return BooleanExpression(lambda **args: self.__call__(**args) > other,
                                         domain=self.domain(),
                                         operator='>', operands=operands)
            else:
                return NotImplemented
        else:
            raise "Comparison not defined for vector groundings"

    def __ge__(self, other):
        operands = [self, other]
        if (self.dim() == 1):
            if (isinstance(other, RealExpression)):
                if(other.dim() == self.dim()):
                    return BooleanExpression(lambda **args: self.__call__(**args) >= other(**args), 
                                             domain=self.domain()+other.domain(),
                                             operator='>=', operands=operands)
                else:
                    raise "Comparison not defined"
            elif (isinstance(other, float) or isinstance(other, int)):
                return BooleanExpression(lambda **args: self.__call__(**args) >= other, 
                                         domain=self.domain(),
                                         operator='>=', operands=operands)
            else:
                return NotImplemented
        else:
            raise "Comparison not defined for vector groundings"
    
    def __getitem__(self, idx):
        operands = [self, idx]
        if isinstance(idx, (list, tuple, np.ndarray)):
            if not self.__indices_within_bounds(idx, self.dim()):
                raise ValueError("Indices out of bounds")
        elif isinstance(idx, slice):
            idx = slice(idx.start, min(idx.stop, self.dim()), idx.step)
            idx = np.mgrid[idx].astype(int)
        elif idx >= self.dim():
            raise ValueError("Index out of bounds")
        
        n_features = 1 if isinstance(idx, int) else len(idx)
        return RealExpression(lambda **args: self.__call__(**args)[idx], 
                              dimension=n_features, 
                              domain=self.domain(),
                              operator='[]', operands=operands)

    def __compose__(self, expression):
        if(self.domain == expression.codomain): #composable
            return RealExpression(lambda **args: self.__call__(expression(**args)), domain=expression.domain(), dimension=self.dim())
        else:
            return NotImplemented

    def __indices_within_bounds(self, array_like, dim):
        for i in range(len(array_like)):
            if array_like[i] >= dim or  array_like[i] < 0:
                return False
        return True

    def __repr__(self):
        if (self._operator is not None):
            if self._operator == '[]':
                return self._operands[0]._name + "[" + str(self._operands[1]) + ']'
            else:
                return "(" + repr(self._operands[0]) + f" {self._operator} " + repr(self._operands[1]) + ")" 
        return self._name


class RealConstant(RealExpression):
    def __init__(self, constant, domain=[]):
        self._constant = constant
        _dim = 1 if isinstance(constant, (int, float)) else len(constant) 
        RealExpression.__init__(self, self.__f, _dim, domain=domain)
    
    def __f(self, **kwargs):
        batch_size = 1
        if (Domain(["state"]) <= self.domain):
            if isinstance(kwargs["state"], BatchedVector):
                batch_size = len(kwargs["state"])
        elif (Domain(["action"]) <= self.domain):
            if isinstance(kwargs["action"], (BatchedVector, BatchedTuple)):
                batch_size = len(kwargs["action"])
        if batch_size > 1:
            return np.array((self._constant,)*batch_size)
        return self._constant

    def __repr__(self):
        return f"{self._name} = {self._constant}"

def real_exp(dim=1, domain=[]):
    def __real_exp(func):
        if not isinstance(func, (int, float, tuple, list, np.ndarray)):
            return RealExpression(func, dimension=dim, domain=domain, name=func.__name__)
        else:
            return RealConstant(func, domain=domain)
    return __real_exp


if __name__ == "__main__":
    constant = RealExpression(lambda **args: 1.0)

    @real_exp(domain=['state'])
    def distance(state):
        return state[0] + state[1]
    print(distance + 1)