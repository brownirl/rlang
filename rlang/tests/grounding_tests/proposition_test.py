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
        proposition_factors = Proposition(factor_ind3(state=state) < factor_ind4(state=state))
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
        # self.assertEqual(type(x >= y), Proposition)
        some_prop = factor_ind3 >= factor_ind4
        self.assertFalse(some_prop(state=state))
        
