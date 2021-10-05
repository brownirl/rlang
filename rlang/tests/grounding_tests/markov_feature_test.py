import unittest
from grounding.groundings import MarkovFeature
import numpy as np
from rlang.src.grounding import Factor, Feature, State

class MarkovFeatureTest(unittest.TestCase):
    def test_from_Factor(self):
        s = State([[0, 1, 2, 3], [4, 5, 6, 7]])
        factor = Factor([0, 1])
        mf = MarkovFeature.from_Factor(factor)
        self.assertTrue((mf(state=s), factor(state=s).all()))


if __name__ == '__main__':
    unittest.main()