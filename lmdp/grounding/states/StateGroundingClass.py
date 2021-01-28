"""
    State Functions:
        - State Factor
        - State Features
    N.B.: These classes assume Simple RL MDP States, whose underlying data structure is a numpy array.

    Author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    Date: August 2020
"""

import sys, os
sys.path.append(os.path.abspath("./"))

import numpy as np
from simple_rl.mdp.StateClass import State
from functools import reduce
from collections.abc import Iterable, Sequence
from collections import Counter

from lmdp.grounding.GroundingClass import Grounding
from lmdp.grounding.booleans.BooleanFunClass import BooleanExpression
from lmdp.grounding.real.RealExpressionClass import RealExpression

class StateFactor(Grounding, RealExpression):
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
        Grounding.__init__(self, name)
        RealExpression.__init__(self, self.executor, len(self.feature_positions), domain=["state"])
        StateFactor.counter += 1
        self._rest = None
    
    def number_of_features(self):
        return len(self.feature_positions)
    
    def variables(self):
        return [self,]

    def executor(self, state):
        '''
            This takes in the state from MDP and returns the value of the
            state variable to which is grounded
            Args:
                - args[0] must be the state from MDP
        '''

        if (isinstance(state, State)):
            return state.features()[self.feature_positions]
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
        return self

    def __add__(self, other):
        variables = []
        if (isinstance(other, StateFactor) or isinstance(other, StateFeature)):
            variables = other.variables() + self.variables()
            return StateFeature(super().__add__(other), self.number_of_features(), variables)
        elif(isinstance(other, RealExpression) or isinstance(other, (float, int, Sequence))):
            return super().__add__(other)
        else:
            return NotImplemented
    
    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        variables = []
        if (isinstance(other, StateFactor) or isinstance(other, StateFeature)):
            f = super().__sub__(other)
            variables = other.variables() + self.variables()
            return StateFeature(f, self.number_of_features(), variables)
        elif(isinstance(other, (float, int, np.ndarray, RealExpression, Sequence))):
            return super().__sub__(other)
        else:
            return NotImplemented

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        variables = []
        if (isinstance(other, StateFactor) or isinstance(other, StateFeature)):
            f = super().__mul__(other)
            variables = other.variables() + self.variables()
            return StateFeature(f, self.number_of_features(), variables)
        elif(isinstance(other, (float, int, np.ndarray, RealExpression, Sequence))):
            return super().__mul__(other)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        variables = []
        if (isinstance(other, StateFactor) or isinstance(other, StateFeature)):
            f = super().__truediv__(other)
            variables = other.variables() + self.variables()
            return StateFeature(f, self.number_of_features(), variables)
        elif(isinstance(other, (float, int, np.ndarray, RealExpression, Sequence))):
            return super().__truediv__(other)
        else:
            return NotImplemented

    def __rtruediv__(self, other):
        return self.__truediv__(other)
    
    @classmethod
    def check_concat(self, sequence, state_dim):
        '''
            Check factors concatanation:

            returns:
                missing_elements: list of elements that are not included
                overlapping: list of elements and number of times included.

        '''
        features = reduce(lambda x, y: x + y, map(lambda f: f.feature_positions, sequence))
        count = Counter(features)
        if len(count.keys()) < state_dim:
            missing_elements = set(range(state_dim)) - count.keys()
        else:
            missing_elements = []
        overlapping = [(feature, number) for (feature, number) in count.items() if number > 1]
        return missing_elements, overlapping

class StateFeature(StateFactor):
    def __init__(self, function, number_of_features, variables):
        self._variables = variables
        self.__function = function
        self.number_features = number_of_features
    
    def executor(self, state):
        return self.__function(state)
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
    position = StateFactor([0,1], "position")
    diag = x == y
    x_0 = x == 0 
    x_1 = x + 1

    print(f"s1 in diag: {diag(s1)} == True")
    print(f"s2 in diag: {diag(s2)} == False")
    print(f"s1 in x_0: {x_0(s1)} == False")
    print(f"s2 in x_0: {x_0(s2)} == True")
    print(f"s1.x + 1:  {x_1(s1)} == 2")
    print(f"s2.x + 1:  {x_1(s2)} == 1")

    print(StateFactor.check_concat([x, y, position], 2))
    print((position + (0,1))(s1))