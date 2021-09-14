from __future__ import annotations
from enum import Enum, auto
from typing import Callable
from collections.abc import MutableMapping


class Domain(Enum):
    """Enum representing the domain or codomain of a GroundingFunction"""
    ACTION = auto()
    ANY = auto()
    BOOLEAN = auto()
    REAL_VALUE = auto()
    REWARD = auto()
    STATE = auto()
    STATE_ACTION = auto()
    STATE_ACTION_NEXTSTATE = auto()


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
        self._domain = domain
        self._codomain = codomain
        self._function = function

    def __call__(self, *args, **kwargs):
        return self._function(*args, **kwargs)


class RLangKnowledge(MutableMapping):
    """
        Knowledge class
            - stores groundings for retrieval by user
            - this is the base-level knowledge class
        author: Benjamin Spiegel (bspiegel@cs.brown.edu), Jennifer Wang (plz put ur email here)
        date: September 2021
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
