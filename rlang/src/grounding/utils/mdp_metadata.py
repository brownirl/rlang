import numpy as np


class StateSpace:
    def __init__(self, dtype: np.dtype, shape: tuple):
        self.dtype = dtype
        self.shape = shape


class MDPMetadata:
    def __init__(self, state_space: StateSpace):
        self.state_space = state_space
