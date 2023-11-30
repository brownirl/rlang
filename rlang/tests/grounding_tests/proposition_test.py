import unittest
import numpy as np
from context import rlang

from rlang.grounding import Factor, Feature, StateResolver, Proposition
from rlang.grounding.utils.grounding_exceptions import RLangGroundingError

class PropositionTest(unittest.TestCase):
    def test_instantiation(self):
        state = [4,2,5,1,6,3,7]

        factor_ind3 = Factor(3, "factor_ind3")
        factor_ind4 = Factor(4, "factor_ind4")

        #Initialize Proposition with a valid function
        proposition_factors = factor_ind3 < factor_ind4
        self.assertEqual(factor_ind3(state=state) < factor_ind4(state=state), proposition_factors)

        #Initialize Proposition with custom name
        proposition_factors = Proposition(factor_ind3(state=state) < factor_ind4(state=state), name="proposition_factors")
        self.assertEqual(factor_ind3(state=state) < factor_ind4(state=state), proposition_factors)

        #Initialize Proposition using TRUE class method
        proposition_true = Proposition.TRUE()
        self.assertEqual(True, proposition_true)

        #Initialize Proposition using FALSE class method
        proposition_false = Proposition.FALSE()
        self.assertEqual(False, proposition_false)

        #Functions that should throw errors:
        #Initialize Proposition without a function
        with self.assertRaises(TypeError):
            proposition_factors = Proposition()


        # I'm not really sure what this means
        self.assertEqual(type(factor_ind3 >= factor_ind4), Proposition)
        some_prop = factor_ind3 >= factor_ind4
        self.assertFalse(some_prop(state=state))
        
    def test_namewrapped(self):
        state = [2,2,5,2,2,3,7,8,16]

        # Tests the name wrapping functionality of Proposition with 'or' operator
        factor_ind3 = Factor(3, "factor_ind3")
        factor_ind4 = Factor(4, "factor_ind4")
        proposition1 = Proposition(lambda state: state[0] == 1, name="proposition1")

        proposition2 = proposition1 | (factor_ind3 == factor_ind4)

        self.assertEqual(proposition2(state=state), True)
        self.assertEqual(proposition2(state=state), proposition2(proposition1=False, factor_ind3=5, factor_ind4=5))
        self.assertEqual(proposition2(state=state), proposition2(proposition1=True))
        self.assertEqual(proposition2(state=state), proposition2(factor_ind3=5, factor_ind4=5))


        # Tests the name wrapping functionality of Proposition with 'and' operator
        feature_ind0 = Feature(lambda state: state[0]*3, "feature_ind0")
        feature_ind5 = Feature(lambda state: state[5]*2, "feature_ind5")
        proposition1 = Proposition(lambda state: state[1]+state[3]+state[4] == 6, name="proposition1")

        proposition2 = proposition1 & (feature_ind0 == feature_ind5)

        self.assertTrue(proposition2(state=state))
        self.assertFalse(proposition2(proposition1=True, feature_ind0=3, feature_ind5=2))
        self.assertFalse(proposition2(proposition1=False, feature_ind0=6, feature_ind5=6))


        # Tests the name wrapping functionality of Proposition with '<' operator
        # feature_ind0 = Feature(lambda state: state[0]*3, "feature_ind0")
        # factor_ind7 = Factor(7, "factor_ind7")

        # proposition = feature_ind0 < factor_ind7
        # self.assertTrue(proposition(state=state))

        # Tests the name wrapping functionality of Proposition with '>' operator
        # feature_ind0 = Feature(lambda state: state[2]*4, "feature_ind0")
        
        # proposition = feature_ind0 > 12
        # self.assertTrue(proposition(state=state))

        # Tests the name wrapping functionality of Proposition with '<=' operator
        factor_ind4 = Factor(4, "factor_ind4")
        factor_ind1 = Factor(1, "factor_ind1")
        factor_ind5 = Factor(5, "factor_ind5")

        proposition = factor_ind4 <= factor_ind1 & factor_ind4 <= factor_ind5
        self.assertTrue(proposition(state=state))

        # Tests the name wrapping functionality of Proposition with '>' operator
        factor_ind7 = Factor(7, "factor_ind7")
        factor_ind0 = Factor(0, "factor_ind0")

        proposition = factor_ind7 > factor_ind0

        self.assertTrue(proposition(state=state))

        # Tests the name wrapping functionality of Proposition with '>=' operator
        # factor_ind7 = Factor(7, "factor_ind7")
        # factor_ind8 = Factor(8, "factor_ind8")
        # feature_ind0mul = Feature(lambda state: state[0]*8, "feature_ind0mul")

        # proposition = feature_ind0mul >= factor_ind7 & feature_ind0mul >= factor_ind8
        # self.assertTrue(proposition(state=state))

        # Tests the name wrapping functionality of Proposition with '!=' operator
        factor_ind2 = Factor(2, "factor_ind2")
        factor_ind1 = Factor(1, "factor_ind1")

        proposition = factor_ind2 != factor_ind1
        self.assertTrue(proposition(state=state))


if __name__ == '__main__':
    unittest.main()
