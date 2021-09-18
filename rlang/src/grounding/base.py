from __future__ import annotations
from enum import Enum, auto
from typing import Callable
from collections.abc import MutableMapping
from rlang.src.exceptions import RLangGroundingError
from rlang.src.grounding.internals import State


class Domain(Enum):
    """Enum representing the domain or codomain of a GroundingFunction

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
                    raise RLangGroundingError(f"The ({self.name}, {other.name}) Domain or Codomain is not supported")
        else:
            raise RLangGroundingError(f"Can't add a Domain enum to a {type(other)}")

    @classmethod
    def from_name(cls, name: str) -> Domain:
        return Domain[name.upper()]


class Grounding(object):
    """Parent class for all grounded objects."""
    def __init__(self, name=None):
        self._name = name

    @property
    def name(self):
        return self._name

    def __hash__(self):
        return self._name.__hash__()

    def __repr__(self):
        return self._name


class GroundingFunction(Grounding):
    """Parent class for groundings which are functions.

    GroundingFunctions have a specified domain and codomain.
    They are typically invoked with keyword arguments corresponding
    to their domain, i.e. door_closed(state=s).

    Args:
        domain: Domain of the function.
        codomain: Codomain of the function.
        function: the actual function.
        name (optional): the name of the Grounding.
    """

    def __init__(self, domain: Domain, codomain: Domain, function: Callable, name: str = None):
        super().__init__(name)
        self.domain = domain
        self.codomain = codomain
        self._function = function

    def __call__(self, *args, **kwargs):
        if 'state' in kwargs.keys():
            if not isinstance(kwargs['state'], State):
                kwargs.update({'state': State(kwargs['state'])})
        if 'next_state' in kwargs.keys():
            if not isinstance(kwargs['next_state'], State):
                kwargs.update({'next_state': State(kwargs['next_state'])})
        return self._function(*args, **kwargs)


class RLangKnowledge(MutableMapping):
    """Acts as a container for Groundings.

    Acts just like a Python dictionary.

    Examples:
        .. code-block:: python

            base = RLangKnowledge()
            base['x_location'] = Factor([1])

    """

    def __init__(self):
        self.store = dict()

    def __getitem__(self, key: str):
        return self.store[key]

    def __setitem__(self, key: str, value: Grounding):
        self.store[key] = value

    def __delitem__(self, key: str):
        del self.store[key]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

    def factors(self):
        # TODO: I don't understand why this doesn't work
        return dict(tuple(filter(lambda a: isinstance(a[1], Factor), self.__iter__())))
