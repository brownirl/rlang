"""
    Abstract class for grounding names to MDPs
    Author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    Date: August 2020
"""

from src.GroundingClass import Grounding

class RealGrounding(Grounding):
    def __init__(self, name=None):
        Grounding.__init__(self, name)