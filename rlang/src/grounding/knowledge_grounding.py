"""
    Abstract class for all groundings
    author: Benjamin Spiegel (bspiegel@cs.brown.edu), Jennifer Wang (plz put ur email here)
    Date: August 2021
"""


class Grounding(object):
    def __init__(self, name=None):
        self._name = name

    @property
    def name(self):
        return self._name

    def __hash__(self):
        return self._name.__hash__()

    def __repr__(self):
        return self._name
