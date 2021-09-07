import unittest
import numpy as np
from rlang.src.grounding import Factor, State


class FactorTest(unittest.TestCase):
    def test_instantiation(self):
        x = Factor(0, "x")
        y = Factor([0, 1], "y")
        z = Factor([0, 2, 3], "z")

        s1 = State([4, 5, 6, 7])

        self.assertTrue(np.array_equal(z(state=s1), State([4, 6, 7])))
        self.assertTrue(np.array_equal(x(state=s1), State(4)))


if __name__ == '__main__':
    unittest.main()
