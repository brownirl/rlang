from __future__ import annotations
from typing import Any
from enum import Enum
import numpy as np
from rlang.src.exceptions import RLangGroundingError


class Domain(Enum):
    """Enum representing the domain or codomain of a OldGroundingFunction

    Domain enums can be automatically combined using an addition operation:

    .. code-block:: python

        Domain.STATE + Domain.ACTION == Domain.STATE_ACTION

    """
    ANY = 1
    ACTION = 2
    STATE = 3
    STATE_ACTION = 6
    NEXT_STATE = 5
    STATE_NEXT_STATE = 15
    STATE_ACTION_NEXT_STATE = 30
    BOOLEAN = 7
    REAL_VALUE = 11
    REWARD = 13

    def __add__(self, other) -> Domain:
        if isinstance(other, Domain):
            # You can think of domain values as being multiples of prime numbers.
            # If STATE is 3 and ACTION is 2, STATE_ACTION is 3*2 = 6.
            if self.value % other.value == 0:
                return self
            else:
                enum_value = self.value * other.value
                if enum_value in set(item.value for item in Domain):
                    return Domain(enum_value)
                else:
                    raise RLangGroundingError(f"The ({self.name}, {other.name}) Domain/Codomain is not supported")
        else:
            raise RLangGroundingError(f"Can't add a Domain enum to a {type(other)}")

    @classmethod
    def from_name(cls, name: str) -> Domain:
        return Domain[name.upper()]


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
    """Represents important parameters of the MDP like the state space and action space."""
    def __init__(self, state_space: StateSpace, action_space: ActionSpace):
        self.state_space = state_space
        self.action_space = action_space

    @classmethod
    def from_state_action(cls, state: np.ndarray, action: np.ndarray):
        return cls(state_space=StateSpace.from_state(state), action_space=ActionSpace.from_action(action))


class BatchedPrimitive(np.ndarray):
    """Represents a batched real-valued object.

    States and Actions should be easily batchable. This takes care of that.
    """

    def __new__(cls, input_array: Any):
        # All BatchablePrimitives are batched automatically
        obj = np.array(input_array, ndmin=2).view(cls)
        return obj

    def __getitem__(self, item):
        # This should abstract away batched variables
        if type(item) != tuple:
            item = (slice(None, None, None), item)
        return State(super().__getitem__(item))

    def __eq__(self, other):
        # print(self.shape)
        # print(other.shape)
        # TODO: This fails due to 'logical and', need to check array dimension and & with result?
        # TODO: Consider implementing two separate eq methods
        # Try BatchedPrimitive(0) == BatchedPrimitive([[1, 0], [0, 0]). Returns [[False],[True]] instead of [[False],[False]]
        return BatchedPrimitive(np.asarray(np.all(super().__eq__(other), axis=1, keepdims=True)))

    def __ne__(self, other):
        return np.bitwise_not(self.__eq__(other))


class State(BatchedPrimitive):
    """Represents a State object.

    RLang expects MDP states to always be of a single dimension. This class makes
    it easy to batch single-dimensional states together.

    Args:
        input_array: a numpy array or list representing a state or set of states.

    Examples:
        .. code-block:: python

            s1 = State(3)
            >> State([[3]])
            s2 = State([3, 4])
            >> State([[3, 4]]})
            s3 = State([[3, 4], [5, 6]])
            Factor([0])(state=s3)
            >> State([[3], [5]])

    """
    pass


class Action(BatchedPrimitive):
    pass