import unittest
import numpy as np
from context import rlang
from rlang.grounding import Proposition, Factor, Feature

class GroundingFunctionTest(unittest.TestCase): 
    def test_lt_and_le(self):
        """Test that < works on grounding functions"""
        # Test that < works on a feature and a factor
        feature_ind0 = Feature(lambda state: state[0]*3, "feature_ind0")
        factor_ind0 = Factor(0, "factor_ind0")
        prop_lt = feature_ind0 < factor_ind0
        prop_lt.nameit("prop_lt")
        self.assertEqual(type(prop_lt), Proposition)

        # Test that < works on a feature and a feature
        feature_ind1 = Feature(lambda state: state[1]+5, "feature_ind1")
        feature_ind3 = Feature(lambda state: state[3]*3, "feature_ind3")
        prop_lt = feature_ind3 <= feature_ind1
        prop_lt.nameit("prop_lt")
        self.assertEqual(type(prop_lt), Proposition)

        # Test that < works on a factor and a factor
        factor_ind1 = Factor(1, "factor_ind1")
        factor_ind3 = Factor(3, "factor_ind3")
        prop_lt = factor_ind3 <= factor_ind1
        prop_lt.nameit("prop_lt")
        self.assertEqual(type(prop_lt), Proposition)
    
    def test_gt_and_ge(self):
        """Test that > works on grounding functions"""
        # Test that > works on a feature and a factor
        feature_ind0 = Feature(lambda state: state[0]*3, "feature_ind0")
        factor_ind0 = Factor(0, "factor_ind0")
        prop_gt = feature_ind0 >= factor_ind0
        prop_gt.nameit("prop_gt")
        self.assertEqual(type(prop_gt), Proposition)

        # Test that > works on a feature and a feature
        feature_ind1 = Feature(lambda state: state[1]+5, "feature_ind1")
        feature_ind3 = Feature(lambda state: state[3]*3, "feature_ind3")
        prop_gt = feature_ind3 > feature_ind1
        prop_gt.nameit("prop_gt")
        self.assertEqual(type(prop_gt), Proposition)

        # Test that > works on a factor and a factor
        factor_ind1 = Factor(1, "factor_ind1")
        factor_ind3 = Factor(3, "factor_ind3")
        prop_gt = factor_ind3 >= factor_ind1
        prop_gt.nameit("prop_gt")
        self.assertEqual(type(prop_gt), Proposition)
    
    def test_eq(self):
        """Test that == works on grounding functions"""
        # Test that == works on a feature and a factor
        feature_ind0 = Feature(lambda state: state[0]*3, "feature_ind0")
        factor_ind0 = Factor(0, "factor_ind0")
        prop_eq = feature_ind0 == factor_ind0
        prop_eq.nameit("prop_eq")
        self.assertEqual(type(prop_eq), Proposition)

        # Test that == works on a feature and a feature
        feature_ind1 = Feature(lambda state: state[1]+5, "feature_ind1")
        feature_ind3 = Feature(lambda state: state[3]*3, "feature_ind3")
        prop_eq = feature_ind3 == feature_ind1
        prop_eq.nameit("prop_eq")
        self.assertEqual(type(prop_eq), Proposition)

        # Test that == works on a factor and a factor
        factor_ind1 = Factor(1, "factor_ind1")
        factor_ind3 = Factor(3, "factor_ind3")
        prop_eq = factor_ind3 == factor_ind1
        prop_eq.nameit("prop_eq")
        self.assertEqual(type(prop_eq), Proposition)

    def test_ne(self):
        """Test that != works on grounding functions"""
        # Test that != works on a feature and a factor
        feature_ind0 = Feature(lambda state: state[0]*3, "feature_ind0")
        factor_ind0 = Factor(0, "factor_ind0")
        prop_ne = feature_ind0 != factor_ind0
        prop_ne.nameit("prop_ne")
        self.assertEqual(type(prop_ne), Proposition)

        # Test that != works on a feature and a feature
        feature_ind1 = Feature(lambda state: state[1]+5, "feature_ind1")
        feature_ind3 = Feature(lambda state: state[3]*3, "feature_ind3")
        prop_ne = feature_ind3 != feature_ind1
        prop_ne.nameit("prop_ne")
        self.assertEqual(type(prop_ne), Proposition)

        # Test that != works on a factor and a factor
        factor_ind1 = Factor(1, "factor_ind1")
        factor_ind3 = Factor(3, "factor_ind3")
        prop_ne = factor_ind3 != factor_ind1
        prop_ne.nameit("prop_ne")
        self.assertEqual(type(prop_ne), Proposition)
    
    def test_and(self):
        """Test that & works on grounding functions"""
        # Test that & works on a feature and a factor
        feature_ind0 = Feature(lambda state: state[0]*3, "feature_ind0")
        factor_ind0 = Factor(0, "factor_ind0")
        prop_and = feature_ind0 & factor_ind0
        prop_and.nameit("prop_and")
        self.assertEqual(type(prop_and), Proposition)

        # Test that & works on a feature and a feature
        feature_ind1 = Feature(lambda state: state[1]+5, "feature_ind1")
        feature_ind3 = Feature(lambda state: state[3]*3, "feature_ind3")
        prop_and = feature_ind3 & feature_ind1
        prop_and.nameit("prop_and")
        self.assertEqual(type(prop_and), Proposition)

        # Test that & works on a factor and a factor
        factor_ind1 = Factor(1, "factor_ind1")
        factor_ind3 = Factor(3, "factor_ind3")
        prop_and = factor_ind3 & factor_ind1
        prop_and.nameit("prop_and")
        self.assertEqual(type(prop_and), Proposition)
    
    def test_or(self):
        """Test that | works on grounding functions"""
        # Test that | works on a feature and a factor
        feature_ind0 = Feature(lambda state: state[0]*3, "feature_ind0")
        factor_ind0 = Factor(0, "factor_ind0")
        prop_or = feature_ind0 | factor_ind0
        prop_or.nameit("prop_or")
        self.assertEqual(type(prop_or), Proposition)

        # Test that | works on a feature and a feature
        feature_ind1 = Feature(lambda state: state[1]+5, "feature_ind1")
        feature_ind3 = Feature(lambda state: state[3]*3, "feature_ind3")
        prop_or = feature_ind3 | feature_ind1
        prop_or.nameit("prop_or")
        self.assertEqual(type(prop_or), Proposition)

        # Test that | works on a factor and a factor
        factor_ind1 = Factor(1, "factor_ind1")
        factor_ind3 = Factor(3, "factor_ind3")
        prop_or = factor_ind3 | factor_ind1
        prop_or.nameit("prop_or")
        self.assertEqual(type(prop_or), Proposition)
    
    def test_mul(self):
        """Test that * works on grounding functions"""
        # Test that * works on a feature and a factor
        feature_ind0 = Feature(lambda state: state[0]*3, "feature_ind0")
        factor_ind0 = Factor(0, "factor_ind0")
        prop_mul = feature_ind0 * factor_ind0
        prop_mul.nameit("prop_mul")
        self.assertEqual(type(prop_mul), Feature)

        # Test that * works on a feature and a feature
        feature_ind1 = Feature(lambda state: state[1]+5, "feature_ind1")
        feature_ind3 = Feature(lambda state: state[3]*3, "feature_ind3")
        prop_mul = feature_ind3 * feature_ind1
        prop_mul.nameit("prop_mul")
        self.assertEqual(type(prop_mul), Feature)

        # Test that * works on a factor and a factor
        factor_ind1 = Factor(1, "factor_ind1")
        factor_ind3 = Factor(3, "factor_ind3")
        prop_mul = factor_ind3 * factor_ind1
        prop_mul.nameit("prop_mul")
        self.assertEqual(type(prop_mul), Feature)

    def test_add(self):
        """Test that + works on grounding functions"""
        # Test that + works on a feature and a factor
        feature_ind0 = Feature(lambda state: state[0]*3, "feature_ind0")
        factor_ind0 = Factor(0, "factor_ind0")
        prop_add = feature_ind0 + factor_ind0
        prop_add.nameit("prop_add")
        self.assertEqual(type(prop_add), Feature)

        # Test that + works on a feature and a feature
        feature_ind1 = Feature(lambda state: state[1]+5, "feature_ind1")
        feature_ind3 = Feature(lambda state: state[3]*3, "feature_ind3")
        prop_add = feature_ind3 + feature_ind1
        prop_add.nameit("prop_add")
        self.assertEqual(type(prop_add), Feature)

        # Test that + works on a factor and a factor
        factor_ind1 = Factor(1, "factor_ind1")
        factor_ind3 = Factor(3, "factor_ind3")
        prop_add = factor_ind3 + factor_ind1
        prop_add.nameit("prop_add")
        self.assertEqual(type(prop_add), Feature)

    def test_sub(self):
        """Test that - works on grounding functions"""
        # Test that - works on a feature and a factor
        feature_ind0 = Feature(lambda state: state[0]*3, "feature_ind0")
        factor_ind0 = Factor(0, "factor_ind0")
        prop_sub = feature_ind0 - factor_ind0
        prop_sub.nameit("prop_sub")
        self.assertEqual(type(prop_sub), Feature)

        # Test that - works on a feature and a feature
        feature_ind1 = Feature(lambda state: state[1]+5, "feature_ind1")
        feature_ind3 = Feature(lambda state: state[3]*3, "feature_ind3")
        prop_sub = feature_ind3 - feature_ind1
        prop_sub.nameit("prop_sub")
        self.assertEqual(type(prop_sub), Feature)

        # Test that - works on a factor and a factor
        factor_ind1 = Factor(1, "factor_ind1")
        factor_ind3 = Factor(3, "factor_ind3")
        prop_sub = factor_ind3 - factor_ind1
        prop_sub.nameit("prop_sub")
        self.assertEqual(type(prop_sub), Feature)
    
    def test_div(self):
        """Test that / works on grounding functions"""
        # Test that / works on a feature and a factor
        feature_ind0 = Feature(lambda state: state[0]*3, "feature_ind0")
        factor_ind0 = Factor(0, "factor_ind0")
        prop_div = feature_ind0 / factor_ind0
        prop_div.nameit("prop_div")
        self.assertEqual(type(prop_div), Feature)

        # Test that / works on a feature and a feature
        feature_ind1 = Feature(lambda state: state[1]+5, "feature_ind1")
        feature_ind3 = Feature(lambda state: state[3]*3, "feature_ind3")
        prop_div = feature_ind3 / feature_ind1
        prop_div.nameit("prop_div")
        self.assertEqual(type(prop_div), Feature)

        # Test that / works on a factor and a factor
        factor_ind1 = Factor(1, "factor_ind1")
        factor_ind3 = Factor(3, "factor_ind3")
        prop_div = factor_ind3 / factor_ind1
        prop_div.nameit("prop_div")
        self.assertEqual(type(prop_div), Feature)

if __name__ == '__main__':
    unittest.main()
