from __future__ import annotations
from typing import Any
from enum import Enum
from functools import total_ordering
import numpy as np
from rlang.src.exceptions import RLangGroundingError


@total_ordering
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
    STATE_VALUE = 13
    FACTOR_STATE = 17
    REWARD = 19

    @classmethod
    def from_name(cls, name: str) -> Domain:
        return Domain[name.upper()]

    def __add__(self, other) -> Domain:
        if isinstance(other, Domain):
            # You can think of domain values as being multiples of prime numbers.
            # If STATE is 3 and ACTION is 2, STATE_ACTION is 3*2 = 6.
            if self.value > other.value:
                larger = self
                smaller = other
            else:
                larger = other
                smaller = self
            if larger.value % smaller.value == 0:
                return larger
            else:
                enum_value = self.value * other.value
                if enum_value in set(item.value for item in Domain):
                    return Domain(enum_value)
                else:
                    raise RLangGroundingError(f"The ({self.name}, {other.name}) Domain/Codomain is not supported")
        else:
            raise RLangGroundingError(f"Can't add a Domain enum to a {type(other)}")

    def __lt__(self, other) -> bool:
        if isinstance(other, Domain):
            if self.value == other.value:
                return False
            elif other.value % self.value == 0:
                return True
            else:
                return False
        else:
            raise RLangGroundingError(f"Can't compare a Domain enum to a {type(other)}")

    def __gt__(self, other) -> bool:
        if isinstance(other, Domain):
            if self.value == other.value:
                return False
            elif self.value % other.value == 0:
                return True
            else:
                return False
        else:
            raise RLangGroundingError(f"Can't compare a Domain enum to a {type(other)}")


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
        obj_arr = np.array(input_array, ndmin=2)
        if obj_arr.ndim != 2:
            raise RLangGroundingError(f"Cannot construct a {str(cls)} with input array of shape {input_array.shape}.")
        obj = obj_arr.view(cls)
        obj.primitive_size = obj.shape[1]
        return obj

    def as_tuple(self):
        s = self.view(np.ndarray)
        s_tuple = tuple(map(tuple, s))
        if s.shape[0] == 1:
            return s_tuple[0]
        else:
            return s_tuple

    def __getitem__(self, item):
        # This should abstract away batched variables
        if type(item) != tuple:
            item = (slice(None, None, None), item)
        return State(super().__getitem__(item))

    def __eq__(self, other):
        if not isinstance(other, np.ndarray):
            other = np.array(other)

        if len(other.shape) == 0:
            other = np.array(other, ndmin=1)

        if other.shape[-1] != self.shape[-1]:
            return BatchedPrimitive(np.full((self.shape[0], 1), False))
            # Should this take the shape of self or other?
        #  Try BatchedPrimitive(0) == BatchedPrimitive([[1, 0], [0, 0]]).
        #  Returns [[False],[True]] instead of [[False],[False]]
        #  UPDATE: Now returns [[False]], but should it return [[False],[False]]?
        return BatchedPrimitive(np.asarray(np.all(super().__eq__(other), axis=1, keepdims=True)))

    def unbatched_eq(self, other):
        if isinstance(other, BatchedPrimitive):
            #TODO: investigate deprecation cause - include version 
            return np.all(super().__eq__(other))
        else:
            return False

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
