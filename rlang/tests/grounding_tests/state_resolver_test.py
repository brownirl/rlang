import unittest
import numpy as np
from context import rlang

from rlang.grounding import StateResolver

class StateResolverTest(unittest.TestCase):

    def test_instantiation(self):
        """Test that StateResolvers can be instantiated with different types of indices, and verifies that they work on example states"""
    # TODO: Arjan, figure out all the things that should be tested and make some comment sections.
