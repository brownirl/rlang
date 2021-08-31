# TODO: This class should contain information about the state space

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
        return super().__getitem__(item)
