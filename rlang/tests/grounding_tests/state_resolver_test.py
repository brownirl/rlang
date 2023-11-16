import unittest
import numpy as np
from context import rlang
from rlang.grounding import StateResolver, Factor
from rlang.grounding.utils.grounding_exceptions import RLangGroundingError as RLangGroundingError

class StateResolverTest(unittest.TestCase):

    def test_instantiation(self):
        """Test that StateResolvers can be instantiated with different types of indices, and verifies that they work on example states"""
        
        # Testing instantiation is not different from testing add_info, except when the input dictionary is empty

        #Test instantiation of StateResolver with empty dictionary
        sr = StateResolver({}, list)
        self.assertEqual(sr.get_state(), [])

        #Test instantiation of StateResolver with dictionary of Factors
        factor_ind3 = Factor(3, "factor_ind3")
        factor_ind1 = Factor(1, "factor_ind1")
        factor_ind5 = Factor(5, "factor_ind5")
        sr = StateResolver({factor_ind3:5, factor_ind1:4, factor_ind5:7}, list)
        self.assertEqual(sr.get_state(), [0,4,0,5,0,7])


        sr = StateResolver({Factor(8, "factor_ind8"): 8}, list)
        self.assertEqual(sr.get_state(), [0,0,0,0,0,0,0,0,8])

        #Test instantiation of StateResolver with dictionary of tuples
        # sr = StateResolver({(0, 3): [3,4,5]}, list)
        # self.assertEqual(sr.get_state(), [3,4,5])
        # sr = StateResolver({(0,2):[3,4], (1,3):[5,6]}, list)
        # self.assertEqual(sr.get_state(), [3,5,6])

        #ERROR Test Cases
        #Test instantiation of StateResolver with Factors and state representations of different lengths
        #When state resolver is instantiated, add_info does not include anything about the flags
        with self.assertRaises(RLangGroundingError):
            factor_ind1to3 = Factor([0,1,2], "factor_ind1to3")
            sr = StateResolver({factor_ind1to3: [4,16]})
        
        with self.assertRaises(RLangGroundingError):
            factor_ind0to4 = Factor((0,4), "factor_int0to4")
            sr = StateResolver({factor_ind0to4: [1]})
        
        with self.assertRaises(RLangGroundingError):
            factor_indnegative = Factor(-3, "factor_indnegative")
            sr = StateResolver({factor_indnegative: [4,3]})

        with self.assertRaises(RLangGroundingError):
            sr = StateResolver({-3: [4,3]})

        # with self.assertRaises(RLangGroundingError):
        #     sr = StateResolver({(0,4): [1,2]})


    def test_add_info(self):
        """Test that StateResolvers can maintain a reconstructed portion of the state given functions of the state and their corresponding predictions"""
        pass
        # sr = StateResolver({})
        # self.assertEqual(sr.state_guess, {})

        #Test instantiation of StateResolver with dictionary of Factors
        sr = StateResolver({Factor(0, "x"): 1, Factor(1, "y"): 2})
        self.assertEqual(sr.state_guess, {0: 1, 1: 2})

        sr = StateResolver({}, list)
        sr.add_info({1:2})
        self.assertEqual(sr.get_state(), [0,2])

        # sr = StateResolver({}, list)
        # sr.add_info({(0,3):[1,2,3]})
        # self.assertEqual(sr.get_state(), [1,2,3])

        sr = StateResolver({}, list)
        sr.add_info({1:2, 0:3, 1:4})
        self.assertEqual(sr.get_state(), [3,4])

        sr = StateResolver({}, list)
        with self.assertRaises(RLangGroundingError):
            sr.add_info({-3:4}, no_regrets=False)

        # sr.add_info({-3:4, Factor(4, "factor"): 2})
        # self.assertEqual(sr.get_state(), [0,0,0,0,2])

        #Test adding info where length of Factor does not equal length of prediction

        #Test adding info where length of Tuple does not equal length of prediction

        #Test adding info of a single integer

        #Test adding Factors that are constructed from other Factors

        #ERROR Test Cases
        #Test instantiation of StateResolver with Factors and state representations of different lengths

        #Test instantiation of StateResolver with tuples of different lengths



    def test_get_state(self):
        """Test that the StateResolvers return a reconstructed portion of the state based on the information they are given"""

        #Test that length of reconstructed state is as large as biggest index predicted
        #Test that if state type is numpy array, get_state returns a numpy array with the appropriate indices populated

        #Test that if state type is list, get_state returns a list with the appropriate length and indices populated

        #Test that any non-list/numpy array throws an error when reconstructing the state

        #Test that get_state returns desired outcome (either empty or not) when invalid Factor or Tuple is provided to add_info
        pass
