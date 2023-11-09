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

        #Test that feature can be instantiated based on other features

        #Test that feature can be instantiated base a factor and a feature

        #Test that feature is instantiated with operation on existing feature

        #Test different operations on feature instantiation (addition, multiplication, etc.)

        #Test that feature instantiation generates name if name is not provided


    def test_arithmetic(self):
        s1 = State(np.array([2, 3]))
        pos = Factor([0, 1], "position")
        x = Feature(pos[0], 1)
        y = Feature(pos[1], 1)
        x_y_sum = x + y
        x_y_prod = x * y
        x_y_div = x / y
        x_y_diff = x - y
        self.assertEqual(x_y_sum(state=s1), 5)
        self.assertEqual(x_y_prod(state=s1), 6)
        self.assertEqual(x_y_div(state=s1), 2/3)
        self.assertEqual(x_y_diff(state=s1), -1)
    
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
