import unittest
import numpy as np
from context import rlang

from rlang.grounding import StateResolver

class StateResolverTest(unittest.TestCase):

    def test_instantiation(self):
        """Test that StateResolvers can be instantiated with different types of indices, and verifies that they work on example states"""
    # TODO: Arjan, figure out all the things that should be tested and make some comment sections.
        
        #Test instantiation of StateResolver with empty dictionary
        #Method for comparing two SRs?
        sr = StateResolver({}, list)
        self.assertEqual(sr.get_state(), [])

        #Test instantiation of StateResolver with dictionary of Factors
        state = [3,2,1,5,-3]
        factor = Factor(3, "factor")
        factor2 = Factor(1, "factor2")
        factor3 = Factor(5, "factor3")
        sr = StateResolver({factor(state=state):5, factor2(state=state):4, factor3(state=state):7}, [])
        self.assertEqual(sr.get_state(), [3,4,1,5,-3,7])

        sr = StateResolver({Factor(8, "factor4")(state=state): 8}, list)
        self.assertEqual(sr.get_state(), [3,2,1,5,-3,0,0,0,8])

        #Test instantiation of StateResolver with dictionary of tuples
        state = [4,1,-1,4,5,-8,12]
        sr = StateResolver({(0,2):[3,4], (1,3):[5,6]}, list)
        self.assertEqual(sr.get_state(), [3,5,6,4,5,-8,12])

        #ERROR Test Cases
        #Test instantiation of StateResolver with Factors and state representations of different lengths

        #Test instantiation of StateResolver with tuples of different lengths

    def test_add_info(self):
        """Test that StateResolvers can maintain a reconstructed portion of the state given functions of the state and their corresponding predictions"""

        #Test adding info to empty StateResolver of type tuple

        #Test adding info to empty StateResolver of type Factor

        #Test adding info of same state index replaces prediction of the state

        #Test adding info where length of Factor does not equal length of prediction

        #Test adding info where length of Tuple does not equal length of prediction

        #Test adding info of a single integer

        #Test adding Factors that are constructed from other Factors


    def test_get_state(self):
        """Test that the StateResolvers return a reconstructed portion of the state based on the information they are given"""

        #Test that length of reconstructed state is as large as biggest index predicted
        #Test that if state type is numpy array, get_state returns a numpy array with the appropriate indices populated

        #Test that if state type is list, get_state returns a list with the appropriate length and indices populated

        #Test that any non-list/numpy array throws an error when reconstructing the state

        #Test that get_state returns desired outcome (either empty or not) when invalid Factor or Tuple is provided to add_info
