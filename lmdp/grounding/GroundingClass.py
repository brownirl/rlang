"""
    Abstract class for grounding names to MDPs
    Author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    Date: August 2020
"""
from lmdp.utils.expression_utils import Domain, Codomain

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
