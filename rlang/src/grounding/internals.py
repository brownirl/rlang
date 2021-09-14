from typing import Any
import numpy as np


class ActionSpace:
    def __init__(self, dtype: np.dtype, shape: tuple):
        self.dtype = dtype
        self.shape = shape

    @classmethod
    def from_action(cls, action: np.ndarray):
        return cls(dtype=action.dtype, shape=action.shape)


class StateSpace:
    def __init__(self, dtype: np.dtype, shape: tuple):
        self.dtype = dtype
        self.shape = shape

    @classmethod
    def from_state(cls, state: np.ndarray):
        return cls(dtype=state.dtype, shape=state.shape)


class MDPMetadata:
    def __init__(self, state_space: StateSpace, action_space: ActionSpace):
        self.state_space = state_space
        self.action_space = action_space

    @classmethod
    def from_state_action(cls, state: np.ndarray, action: np.ndarray):
        return cls(state_space=StateSpace.from_state(state), action_space=ActionSpace.from_action(action))


class State(np.ndarray):
    """
        State util class
            -
        author: Benjamin Spiegel (bspiegel@cs.brown.edu)
        date: August 2021
    """
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


class Action(np.ndarray):
    """
        Action util class
            -
        author: Benjamin Spiegel (bspiegel@cs.brown.edu)
        date: September 2021
    """
    def __new__(cls, input_array: Any):
        # All Actions are batched automatically
        obj = np.array(input_array, ndmin=2).view(cls)
        return obj

    def __getitem__(self, item):
        # This should abstract away batched states
        if type(item) != tuple:
            item = (slice(None, None, None), item)
        return Action(super().__getitem__(item))

    def __eq__(self, other):
        # print(self.shape)
        # print(other.shape)
        # TODO: This fails due to logical and, need to check array dimension
        # TODO: Consider implementing two separate eq methods
        # Try Action(0) == Action([[1, 0], [0, 0]). Returns [[False],[True]] instead of [[False],[False]]
        return np.asarray(np.all(super().__eq__(other), axis=1, keepdims=True))

    def __ne__(self, other):
        return np.bitwise_not(self.__eq__(other))
