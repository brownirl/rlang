import unittest
import numpy as np
from rlang.src.grounding import Factor, Feature, State
class FeatureTest(unittest.TestCase): 

    def test_instantiation(self):
        state1 = State(np.array([2, 3]))
        pos = Factor([0, 1], "position")
        x = Feature(pos[0], 1)
        y = Factor(1, "y")
        self.assertEqual(x(state=state1), 2)

        test = Feature((lambda s: x(state=s) + 1), 1)
        test2 = Feature((lambda s: x(state=s) + y(state=s)), 1)
        self.assertEqual(test(state1), 3)
        self.assertEqual(test2(state1), 5)

    def test_arithmetic(self):
        pass
    
    def test_equality(self):
        state1 = State(np.array([2, 3]))
        pos = Factor([0, 1], "position")
        x = Feature(pos[0], 1)
        y = Factor(1, "y")
        self.assertEqual(x(state=state1), 2)

        test1 = Feature((lambda s: x(state=s) + 3), 1)
        test2 = Feature((lambda s: x(state=s) + y(state=s)), 1)

        self.assertEqual(test1(state1), test2(state1))

if __name__ == '__main__':
    unittest.main()