from __future__ import annotations
from enum import Enum, auto
from typing import Callable
# from rlang.src.grounding.utils.domain import Domain
from collections.abc import MutableMapping


class Domain(Enum):
    """
        Domain Enum
            - Represents function domains and co-domains
        author: Benjamin Spiegel (bspiegel@cs.brown.edu)
        date: August 2021
    """
    STATE = auto()
    ACTION = auto()
    STATE_ACTION = auto()
    STATE_ACTION_NEXTSTATE = auto()
    REAL_VALUE = auto()
    REWARD = auto()
    BOOLEAN = auto()
    ANY = auto() # Constant grounding_functions don't care what is passed to them


class Grounding(object):
    """
        Abstract class for all groundings
        author: Benjamin Spiegel (bspiegel@cs.brown.edu), Jennifer Wang (plz put ur email here)
        Date: August 2021
    """
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
    """
        Grounded Function Specification Class
            - Represents function specification, with a given domain-codomain,
            in the form of a function by parts.
            - Implemented as Pairs of (boolean expressions, function).
        author: Rafael Rodriguez-Sanchez (rrs@brown.edu), Benjamin Spiegel
        (bspiegel@cs.brown.edu)
        date: January 2021, August 2021
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
