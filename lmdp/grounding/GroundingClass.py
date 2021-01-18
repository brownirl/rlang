"""
    Abstract class for grounding names to MDPs
    Author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    Date: August 2020
"""
from lmdp.utils.expression_utils import Domain, Codomain

class Grounding(object):
    def __init__(self, name=None, domain=[]):
        self._name = name
        self._domain = Domain(domain)

    @property
    def name(self):
        return self._name
    

    # def __hash__(self):
    #     return self.name.__hash__()
