"""
    State Functions:
        - State Factor
        - State Features
    Author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    Date: August 2020
"""

import sys, os
sys.path.append(os.path.abspath("./"))

import numpy as np
from simple_rl.mdp.StateClass import State
from functools import reduce

from lmdp.grounding.GroundingClass import Grounding
from lmdp.grounding.booleans.BooleanFunClass import BooleanExpression
from lmdp.grounding.real.RealExpressionClass import RealExpression

class StateFactor(Grounding):
    counter = 0
    def __init__(self, feature_positions, name=None):
        '''
            Args: feature_positions is an array-like of indices (list or np.array)
        '''
        if(name is None):
            name = "state-feature-" + str(StateFactor.counter)
        if (isinstance(feature_positions, int)):
            feature_positions = [feature_positions, ]
        self.feature_positions = feature_positions
        Grounding.__init__(self, name, domain=["State"])
        StateFactor.counter += 1
        self._rest = None
    
    def number_of_features(self):
        return len(self.feature_positions)
    
    def variables(self):
        return [self,]

    def __call__(self, *args):
        '''
            This takes in the state from MDP and returns the value of the
            state variable to which is grounded
            Args:
                - args[0] must be the state from MDP
        '''
        if (len(args) < 1):
            raise "State from MDP is needed"

        if (isinstance(args[0], State)):
            return args[0].features()[self.feature_positions]
        else:
            raise "First argument must be MDP State Class"

    def rest(self, state_dim):
        if (self._rest is None):
            feature_positions = [i for i in range(state_dim) if i not in self.feature_positions]
            self._rest = StateFactor(feature_positions, name=self.name + "-rest") # cache it
        return self._rest
    
    def concat(self, *others, name=None):
        if name is None:
            names = list(map(lambda x: x.name, others))
            name = '(' + self.name +',' + ','.join(names) + ')'
        feature_positions = set(self.feature_positions + reduce(lambda x, y: x + y, map(lambda x: x.feature_positions, others)))
        return StateFactor(sorted(list(feature_positions)), name=name)

    def real_expression(self):
        return RealExpression(self, dimension=self.number_of_features(), domain=["State"])    

    def __add__(self, other):
        variables = []
        if (isinstance(other, StateFactor) or isinstance(other, StateFeature)):
            f = self.real_expression() + other.real_expression()
            variables = other.variables() + self.variables()
            return StateFeature(f, self.number_of_features(), variables)
        elif(isinstance(other, RealExpression) or isinstance(other, float) or isinstance(other, int)):
            return self.real_expression() + other
        else:
            return NotImplemented
    
    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        variables = []
        if (isinstance(other, StateFactor) or isinstance(other, StateFeature)):
            f = self.real_expression() - other.real_expression()
            variables = other.variables() + self.variables()
            return StateFeature(f, self.number_of_features(), variables)
        elif(isinstance(other, RealExpression) or isinstance(other, float) or isinstance(other, int)):
            return self.real_expression() - other
        else:
            return NotImplemented

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        variables = []
        if (isinstance(other, StateFactor) or isinstance(other, StateFeature)):
            f = self.real_expression() * other.real_expression()
            variables = other.variables() + self.variables()
            return StateFeature(f, self.number_of_features(), variables)
        elif(isinstance(other, RealExpression) or isinstance(other, float) or isinstance(other, int)):
            return self.real_expression() * other
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        variables = []
        if (isinstance(other, StateFactor) or isinstance(other, StateFeature)):
            f = self.real_expression() / other.real_expression()
            variables = other.variables() + self.variables()
            return StateFeature(f, self.number_of_features(), variables)
        elif(isinstance(other, RealExpression) or isinstance(other, float) or isinstance(other, int)):
            return self.real_expression() / other
        else:
            return NotImplemented

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    def __lt__(self, other):
        if (isinstance(other, StateFactor) or isinstance(other, StateFeature)):
            return self.real_expression() < other.real_expression()
        return self.real_expression() < other

    def __rlt__(self, other):
        return self.__lt__(other)

    def __le__(self, other):
        if (isinstance(other, StateFactor) or isinstance(other, StateFeature)):
            return self.real_expression() <= other.real_expression()
        return self.real_expression() <= other

    def __rle__(self, other):
        return self.__le__(other)

    def __eq__(self, other):
        if (isinstance(other, StateFactor) or isinstance(other, StateFeature)):
            return self.real_expression() == other.real_expression()
        return self.real_expression() == other

    def __req__(self, other):
        return self.__eq__(other)

    def __ne__(self, other):
        if (isinstance(other, StateFactor) or isinstance(other, StateFeature)):
            return self.real_expression() != other.real_expression()
        return self.real_expression() != other

    def __rne__(self, other):
        return self.__ne__(other)

    def __gt__(self, other):
        if (isinstance(other, StateFactor) or isinstance(other, StateFeature)):
            return self.real_expression() > other.real_expression()
        return self.real_expression() > other
    def __rgt__(self, other):
        return self.__gt__(other)

    def __ge__(self, other):
        if (isinstance(other, StateFactor) or isinstance(other, StateFeature)):
            return self.real_expression() >= other.real_expression()
        return self.real_expression() >= other

    def __rge__(self, other):
        return self.__rge__(other)
    
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

class StateFeature(StateFactor):
    def __init__(self, function, number_of_features, variables):
        self._variables = variables
        self.__function = function
        self.number_features = number_of_features
    
    def __call__(self, *args):
        return self.__function(*args)
    def number_of_features(self):
        return self.number_features
    def variables(self):
        return self._variables


if __name__ == '__main__':
    import numpy as np
    s1 = State(data=np.array([1, 1]))
    s2 = State(data=np.array([0, 1]))
    x = StateFactor(0, "x")
    y = StateFactor(1, "y")
    diag = x == y
    x_0 = x == 0 
    x_1 = x + 1

    print(f"s1 in diag: {diag(s1)} == True")
    print(f"s2 in diag: {diag(s2)} == False")
    print(f"s1 in x_0: {x_0(s1)} == False")
    print(f"s2 in x_0: {x_0(s2)} == True")
    print(f"s1.x + 1:  {x_1(s1)} == 2")
    print(f"s2.x + 1:  {x_1(s2)} == 1")