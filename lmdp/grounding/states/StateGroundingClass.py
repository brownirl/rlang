"""
    State Variables Grounding
    Author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    Date: August 2020
"""

from lmdp.grounding.GroundingClass import Grounding
from lmdp.grounding.BooleanFunClass import BooleanFun
from simple_rl.mdp.StateClass import State
import numpy as np


class StateGrounding(Grounding):
    counter = 0
    def __init__(self, feature_positions, name=None):
        '''
            Args: feature_positions is an array-like of indices (list or np.array)
        '''
        if(name is None):
            name = "state-var-" + str(StateGrounding.counter)
        if (isinstance(feature_positions, int)):
            feature_positions = [feature_positions, ]
        self.__feature_positions = feature_positions
        Grounding.__init__(self, name)
        StateGrounding.counter += 1
        self._rest = None
    
    def number_of_features(self):
        return len(self.__feature_positions)

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
            return args[0].features()[self.__feature_positions]
        else:
            raise "First argument must be MDP State Class"

    def rest(self, state_dim):
        if (self._rest is None):
            feature_positions = [i for i in range(state_dim) if i not in self.__feature_positions]
            self._rest = StateGrounding(feature_positions, name=self.name + "-rest") # cache it
        return self._rest

    def __add__(self, other):
        if (isinstance(other, StateGrounding)):
            if(other.number_of_features() == self.number_of_features()):
                f = lambda *args: self.__call__(*args) + other(*args)
            else:
                raise "Shapes are not compatible"
        elif (isinstance(other, float) or isinstance(other, int)):
            f = lambda *args: self.__call__(*args) + other
        elif (isinstance(other, np.ndarray)):
            if(other.shape == (self.number_of_features(),)):
                f = lambda *args: self.__call__(*args) + other
            else:
                raise "Shapes are not compatible"
        else:
            raise NotImplementedError

        return DerivedStateGrounding(f, self.number_of_features())

    def __sub__(self, other):
        if (isinstance(other, StateGrounding)):
            if(other.number_of_features() == self.number_of_features()):
                f = lambda *args: self.__call__(*args) - other(*args)
            else:
                raise "Shapes are not compatible"
        elif (isinstance(other, float) or isinstance(other, int)):
            f = lambda *args: self.__call__(*args) - other
        elif (isinstance(other, np.ndarray)):
            if(other.shape == (self.number_of_features(),)):
                f = lambda *args: self.__call__(*args) - other
            else:
                raise "Shapes are not compatible"
        else:
            raise NotImplementedError
        return DerivedStateGrounding(f, self.number_of_features())

    def __mul__(self, other):
        if (isinstance(other, StateGrounding)):
            if(other.number_of_features() == self.number_of_features()):
                f = lambda *args: self.__call__(*args) * other(*args)
            else:
                raise "Shapes are not compatible"
        elif (isinstance(other, float) or isinstance(other, int)):
            f = lambda *args: self.__call__(*args) * other
        elif (isinstance(other, np.ndarray)):
            if(other.shape == (self.number_of_features(),)):
                f = lambda *args: self.__call__(*args) *  other
            else:
                raise "Shapes are not compatible"
        else:
            raise NotImplementedError
        return DerivedStateGrounding(f, self.number_of_features())

    def __truediv__(self, other):
        if (isinstance(other, StateGrounding)):
            if(other.number_of_features() == self.number_of_features()):
                f = lambda *args: self.__call__(*args) / other(*args)
            else:
                raise "Shapes are not compatible"
        elif (isinstance(other, float) or isinstance(other, int)):
            f =  lambda *args: self.__call__(*args) / other
        elif (isinstance(other, np.ndarray)):
            if(other.shape == (self.number_of_features(),)):
                f = lambda *args: self.__call__(*args) / other
            else:
                raise "Shapes are not compatible"
        else:
            raise NotImplementedError
        return DerivedStateGrounding(f, self.number_of_features())

    def __lt__(self, other):
        if (self.number_of_features() == 1):
            if (isinstance(other, StateGrounding)):
                if(other.number_of_features() == self.number_of_features()):
                    return BooleanFun(lambda *args: self.__call__(*args) < other(*args))
                else:
                    raise "Comparison not defined"
            elif (isinstance(other, float) or isinstance(other, int)):
                return BooleanFun(lambda *args: self.__call__(*args) < other)
            else:
                raise NotImplementedError
        else:
            raise "Comparison not defined for vector groundings"
        return DerivedStateGrounding(f, self.number_of_features())

    def __le__(self, other):
        if (self.number_of_features() == 1):
            if (isinstance(other, StateGrounding)):
                if(other.number_of_features() == self.number_of_features()):
                    return BooleanFun(lambda *args: self.__call__(*args) <= other(*args))
                else:
                    raise "Comparison not defined"
            elif (isinstance(other, float) or isinstance(other, int)):
                return BooleanFun(lambda *args: self.__call__(*args) <= other)
            else:
                raise NotImplementedError
        else:
            raise "Comparison not defined for vector groundings"

    def __eq__(self, other):
        if (isinstance(other, StateGrounding)):
            if(other.number_of_features() == self.number_of_features()):
                return BooleanFun(lambda *args: np.array_equal(self.__call__(*args), other(*args)))
            else:
                raise "Length must be equal"
        elif (isinstance(other, float) or isinstance(other, int)):
            if (self.number_of_features() == 1):
                return BooleanFun(lambda *args: self.__call__(*args) == other)
            else:
                raise "Length must be equal"
        elif (isinstance(other, np.ndarray)):
            if(other.shape == (self.number_of_features(),)):
                return BooleanFun(lambda *args: np.array_equal(self.__call__(*args), other))
            else:
                raise "Length must be equal"
        else:
            raise NotImplementedError

    def __ne__(self, other):
        if (isinstance(other, StateGrounding)):
            if(other.number_of_features() == self.number_of_features()):
                return BooleanFun(lambda *args: not np.array_equal(self.__call__(*args), other(*args)))
            else:
                raise "Length must be equal"
        elif (isinstance(other, float) or isinstance(other, int)):
            if (self.number_of_features() == 1):
                return BooleanFun(lambda *args: self.__call__(*args) == other)
            else:
                raise "Length must be equal"
        elif (isinstance(other, np.ndarray)):
            if(other.shape == (self.number_of_features(),)):
                return BooleanFun(lambda *args: not np.array_equal(self.__call__(*args), other))
            else:
                raise "Length must be equal"
        else:
            raise NotImplementedError

    def __gt__(self, other):
        if (self.number_of_features() == 1):
            if (isinstance(other, StateGrounding)):
                if(other.number_of_features() == self.number_of_features()):
                    return BooleanFun(lambda *args: self.__call__(*args) > other(*args))
                else:
                    raise "Comparison not defined"
            elif (isinstance(other, float) or isinstance(other, int)):
                return BooleanFun(lambda *args: self.__call__(*args) > other)
            else:
                raise NotImplementedError
        else:
            raise "Comparison not defined for vector groundings"

    def __ge__(self, other):
        if (self.number_of_features() == 1):
            if (isinstance(other, StateGrounding)):
                if(other.number_of_features() == self.number_of_features()):
                    return BooleanFun(lambda *args: self.__call__(*args) >= other(*args))
                else:
                    raise "Comparison not defined"
            elif (isinstance(other, float) or isinstance(other, int)):
                return BooleanFun(lambda *args: self.__call__(*args) >= other)
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

class DerivedStateGrounding(StateGrounding):
    def __init__(self, function, number_of_features):
        self.__function = function
        self.number_features = number_of_features
    
    def __call__(self, *args):
        return self.__function(*args)
    
    def number_of_features(self):
        return self.number_features


if __name__ == '__main__':
    import numpy as np
    s1 = State(data=np.array([1, 1]))
    s2 = State(data=np.array([0, 1]))
    x = StateGrounding(0, "x")
    y = StateGrounding(1, "y")
    diag = x == y
    x_0 = x == 0 
    x_1 = x + 1

    print(f"s1 in diag: {diag(s1)}")
    print(f"s2 in diag: {diag(s2)}")
    print(f"s1 in x_0: {x_0(s1)}")
    print(f"s2 in x_0: {x_0(s2)}")
    print(f"s1.x + 1:  {x_1(s1)}")
    print(f"s2.x + 1:  {x_1(s2)}")