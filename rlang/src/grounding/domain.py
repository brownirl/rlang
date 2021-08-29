"""
    Domain Enum
        - Represents function domains and co-domains
    author: Benjamin Spiegel (bspiegel@cs.brown.edu)
    date: August 2021
"""

from enum import Enum, auto


class Domain(Enum):
    STATE = auto()
    STATE_ACTION = auto()
    STATE_ACTION_NEXTSTATE = auto()
    REAL_VALUE = auto()
    BOOLEAN = auto()
    MULTIPLE_VALUES = auto()
    ANY = auto() # Constant grounding_functions don't care what is passed to them