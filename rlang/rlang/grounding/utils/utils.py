from __future__ import annotations
from enum import Enum
from dataclasses import dataclass
from functools import total_ordering
from typing import Type

# import gym.spaces
import numpy as np
from .grounding_exceptions import RLangGroundingError
from .primitives import State
# from gym.spaces import Space


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
    BOOLEAN_REAL_VALUE = 77
    ACTION_BOOLEAN = 14
    STATE_ACTION_BOOLEAN = 42
    STATE_BOOLEAN = 21
    STATE_VALUE = 13
    FACTOR_STATE = 17
    REWARD = 19
    OBJECT_VALUE = 23
    KNOWLEDGE = 29
    STATE_KNOWLEDGE = 87

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
                # if enum_value % 4 == 0: # TODO: This is a hack, need to make sure that enum_value is composed only of primes
                #     enum_value /= 2

                for item in Domain:
                    if enum_value % item.value == 0:
                        enum_value = enum_value / item.value

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


# class OldMDPMetadata:
#     # TODO: Deprecate eventually. I don't know if this is being used
#     """Represents important parameters of the MDP like the state space and action space."""
#     def __init__(self, state_space: Space, action_space: Space):
#         self.state_space = state_space
#         self.action_space = action_space
#
#     @classmethod
#     def from_state_action(cls, state: np.ndarray, action: np.ndarray):
#         return cls(state_space=gym.spaces.Box(low=np.inf, high=np.inf, shape=state.shape),
#                    action_space=gym.spaces.Box(low=np.inf, high=np.inf, shape=action.shape))


@dataclass
class MDPMetadata:
    """Class for holding metadata on an MDP like the state and action representations."""
    state_representation: Type[State]
