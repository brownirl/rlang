"""
    State Functions:
        - State Factor
        - State Features
    N.B.: These classes assume Simple RL MDP States, whose underlying data structure is a numpy array.

    Author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    Date: August 2020
"""

import sys, os

sys.path.append(os.path.abspath("/"))

import numpy as np
from functools import reduce, partial
from collections.abc import Iterable, Sequence
from collections import Counter

from lmdp.grounding.GroundingClass import Grounding
from lmdp.grounding.booleans.BooleanFunClass import BooleanExpression
from lmdp.grounding.real.RealExpressionClass import RealExpression
from lmdp.grounding.states.StateClass import State, BatchedState


class StateFactor(Grounding, RealExpression):
    counter = 0

    def __init__(self, feature_positions, name=None):
        """
        Initializes StateFactor

        Args:
            feature_positions (list, tuple or np.array): an array-like of indices
            name (String, optional): [description]. Defaults to "state-factor-" + counter
        """
        if (name is None):
            name = "state-factor-" + str(StateFactor.counter)
        if isinstance(feature_positions, int):
            feature_positions = [feature_positions, ]
        self.feature_positions = feature_positions
        Grounding.__init__(self, name)
        RealExpression.__init__(self, self.executor, len(self.feature_positions), domain=["state"], name=name)
        StateFactor.counter += 1
        self._rest = None

    def number_of_features(self):
        return len(self.feature_positions)

    def variables(self):
        return [self, ]

    def executor(self, state):
        """
        This takes in the state from MDP and returns the value of the
        state variable to which is grounded

        Args:
            state ([type]): the state from MDP

        Returns:
            [type]: the value of the state variable grounded to state
         """
        # print(type(state))
        # print(state)
        if isinstance(state, np.ndarray):
            if len(state.shape) > 1:
                state = BatchedState(state)
            else:
                state = State(state)
        # print(type(state))
        return state.features()[self.feature_positions]

    # def rest(self, state_dim):
    #     if (self._rest is None):
    #         feature_positions = [i for i in range(state_dim) if i not in self.feature_positions]
    #         self._rest = StateFactor(feature_positions, name=self.name + "-rest") # cache it
    #     return self._rest

    def concat(self, *others, name=None):
        if name is None:
            names = list(map(lambda x: x.name, others))
            name = '(' + self.name + ',' + ','.join(names) + ')'
        feature_positions = set(
            self.feature_positions + reduce(lambda x, y: x + y, map(lambda x: x.feature_positions, others)))
        return StateFactor(sorted(list(feature_positions)), name=name)

    def real_expression(self):
        return self

    def __add__(self, other):
        variables = []
        if (isinstance(other, StateFactor) or isinstance(other, StateFeature)):
            variables = other.variables() + self.variables()
            return StateFeature(super().__add__(other), self.number_of_features(), variables, operator='+')
        elif (isinstance(other, RealExpression) or isinstance(other, (float, int, Sequence))):
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
            return StateFeature(f, self.number_of_features(), variables, operator='-')
        elif (isinstance(other, (float, int, np.ndarray, RealExpression, Sequence))):
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
            return StateFeature(f, self.number_of_features(), variables, operator='*')
        elif (isinstance(other, (float, int, np.ndarray, RealExpression, Sequence))):
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
            return StateFeature(f, self.number_of_features(), variables, operator='/')
        elif (isinstance(other, (float, int, np.ndarray, RealExpression, Sequence))):
            return super().__truediv__(other)
        else:
            return NotImplemented

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    def __getitem__(self, idx):
        if isinstance(idx, (list, tuple, np.ndarray)):
            if not self.__indices_within_bounds(idx, self.number_of_features()):
                raise ValueError("Indices out of bounds")
        elif isinstance(idx, slice):
            idx = slice(idx.start, min(idx.stop, self.number_of_features()), idx.step)
            idx = np.mgrid[idx].astype(int)
        elif idx >= self.number_of_features():
            raise ValueError("Index out of bounds")

        n_features = 1 if isinstance(idx, int) else len(idx)
        # return StateFeature(RealExpression.__getitem__(self, idx), n_features, self.variables(), operator='[]')
        return _cast_real_exp_to_state_feature(RealExpression.__getitem__(self, idx))

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

    def __indices_within_bounds(self, array_like, dim):
        for i in range(len(array_like)):
            if array_like[i] >= dim or array_like[i] < 0:
                return False
        return True

    def dim(self):
        return self.number_of_features()

    def in_(self, l):
        def __in(seq, **args):
            s = self.__call__(**args)

            t = []
            for e in seq:
                t.append((s == e))
            return reduce(lambda x, y: x | y, t)

        return partial(__in, l)


class StateFeature(StateFactor):
    _id = 0

    def __init__(self, function, number_of_features, variables=None, name=None, operator=None):
        if name is None:
            name = "state-feature-" + str(StateFeature._id)
        self._operator = operator
        StateFeature._id += 1
        StateFactor.__init__(self, list(range(number_of_features)), name=name)
        self._variables = variables
        self.__function = function
        self.number_features = number_of_features
        RealExpression.__init__(self, self.executor,
                                dimension=self.number_features,
                                domain=['state'],
                                name=name,
                                operator=operator,
                                operands=self._variables)

    def executor(self, state):
        return self.__function(state)

    def number_of_features(self):
        return self.number_features

    def variables(self):
        return self._variables

    def __repr__(self):
        return RealExpression.__repr__(self)


def _cast_real_exp_to_state_feature(real_exp):
    if (real_exp.domain.is_s()):
        return StateFeature(real_exp, number_of_features=real_exp.dim(), variables=real_exp._operands,
                            operator=real_exp._operator)
    return None


if __name__ == '__main__':
    import numpy as np
    from lmdp.grounding.states.StateClass import BatchedState
    from lmdp.grounding.booleans.BooleanFunClass import bool_and, bool_not

    s1 = State(data=np.array([1, 1]))
    s2 = State(data=np.array([0, 1]))
    x = StateFactor(0, "x")
    y = StateFactor(1, "y")
    position = StateFactor([0, 1], "position")
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
    print((position + (0, 1))(s1))

    s3 = BatchedState(data=np.random.rand(4, 2))
    print(s3)
    print(y(s3))
    print((y + 1)(s3))
    print(bool_and((y < 1.5), bool_not(x < 3))(s3))
