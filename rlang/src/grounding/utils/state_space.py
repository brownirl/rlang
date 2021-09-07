"""
    State util class
        -
    author: Benjamin Spiegel (bspiegel@cs.brown.edu)
    date: August 2021
"""

from typing import Any
import numpy as np


class State(np.ndarray):
    def __new__(cls, input_array: Any):
        # All States are batched automatically
        obj = np.array(input_array, ndmin=2).view(cls)
        return obj

    def __getitem__(self, item):
        # This should abstract away batched states
        if type(item) != tuple:
            item = (slice(None, None, None), item)
        return State(super().__getitem__(item))

    def __eq__(self, other):
        # print(self.shape)
        # print(other.shape)
        # TODO: This fails due to logical and, need to check array dimension
        # TODO: Consider implementing two separate eq methods
        # Try State(0) == State([[1, 0], [0, 0]). Returns [[False],[True]] instead of [[False],[False]]
        return np.asarray(np.all(super().__eq__(other), axis=1, keepdims=True))

    def __ne__(self, other):
        return np.bitwise_not(self.__eq__(other))


class StateSpace:
    def __init__(self, dtype: np.dtype, shape: tuple):
        self.dtype = dtype
        self.shape = shape


class MDPMetadata:
    def __init__(self, state_space: StateSpace):
        self.state_space = state_space
