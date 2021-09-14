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
