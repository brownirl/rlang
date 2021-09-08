"""
    Knowledge class
        - stores groundings for retrieval by user
        - this is the base-level knowledge class
    author: Benjamin Spiegel (bspiegel@cs.brown.edu), Jennifer Wang (plz put ur email here)
    date: September 2021
"""

from rlang.src.grounding.knowledge_grounding import Grounding
from rlang.src.grounding.groundings.state import Factor
from collections.abc import MutableMapping


class RLangKnowledge(MutableMapping):

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
