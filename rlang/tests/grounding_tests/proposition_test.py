import unittest
import numpy as np
from context import rlang

from rlang.grounding import Factor, Feature, StateResolver
from rlang.grounding.utils.grounding_exceptions import RLangGroundingError

class PropositionTest(unittest.TestCase):
    def test_instantiation(self):
        #Initialize Proposition with a valid function

        #Initialize Proposition with custom name

        #Initialize Proposition using TRUE class method

        #Initialize Proposition using FALSE class method

        #Initialize Proposition without name

        #Functions that should throw errors:
        #Initialize Proposition with non-callable function

        #Initialize Proposition without a function

        #Initialize Proposition with function that does not return a boolean

        #Initialize Proposition with empty string as the name
