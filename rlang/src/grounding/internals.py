from __future__ import annotations
from typing import Any
from enum import Enum
from functools import total_ordering

import gym.spaces
import numpy as np
from rlang.src.exceptions import RLangGroundingError
from gym.spaces import Space


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


class MDPMetadata:
    """Represents important parameters of the MDP like the state space and action space."""
    def __init__(self, state_space: Space, action_space: Space):
        self.state_space = state_space
        self.action_space = action_space

    @classmethod
    def from_state_action(cls, state: np.ndarray, action: np.ndarray):
        return cls(state_space=gym.spaces.Box(low=np.inf, high=np.inf, shape=state.shape),
                   action_space=gym.spaces.Box(low=np.inf, high=np.inf, shape=action.shape))


class Primitive(np.ndarray):
    """Represents a batched real-valued object.

    States and Actions should be easily batchable. This takes care of that.
    """

    def __new__(cls, input_array: Any):
        obj_arr = np.array(input_array, ndmin=1)
        obj = obj_arr.view(cls)
        return obj

    def as_tuple(self):
        s = self.view(np.ndarray)
        s_tuple = tuple(map(tuple, s))
        if s.shape[0] == 1:
            return s_tuple[0]
        else:
            return s_tuple

    def __getitem__(self, item):
        return super().__getitem__(item).view(Primitive)

    def __eq__(self, other):
        return super().__eq__(other).all().view(Primitive)

    def unbatched_eq(self, other):
        if isinstance(other, Primitive):
            #TODO: investigate deprecation cause - include version
            return np.all(super().__eq__(other))
        else:
            return False

    def __hash__(self):
        return hash(str(self))

    def __ne__(self, other):
        return np.bitwise_not(self.__eq__(other))


class State(Primitive):
    """Represents a State object.

    Args:
        input_array: a numpy array or list representing a state or set of states.

    Examples:
        .. code-block:: python

            s1 = State(3)
            >> State([3])
            s2 = State([3, 4])
            >> State([3, 4])
    """
    pass


class Action(Primitive):
    pass
