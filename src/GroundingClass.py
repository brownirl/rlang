"""
    Abstract class for grounding names to MDPs
    Author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    Date: August 2020
"""

class Grounding(object):
    def __init__(self, name=None):
        self.__name = name

    @property
    def name(self):
        return self.__name