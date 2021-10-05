import unittest
import numpy as np
from rlang.src.grounding import Factor, Feature, State


class FactorTest(unittest.TestCase):
    def test_instantiation(self):
        x = Factor(0, "x")
        y = Factor([0, 1], "y")
        z = Factor([0, 2, 3], "z")

        s1 = State([4, 5, 6, 7])

        self.assertTrue(np.array_equal(z(state=s1), State([4, 6, 7])))
        self.assertTrue(np.array_equal(x(state=s1), State(4)))
    
    def test_arithmetic_op(self):
        state1 = State(np.array([2, 3]))

        x = Factor(0, "x")
        z = Factor(2, "z")

        pos = Factor([0, 1], "position")

        x_1 = x + 1
        x_2 = x * 5
        x_3 = x_1 / 5
        x_4 = x_2 - 10

        self.assertEqual(x(state=state1), 2)
        self.assertEqual(x_1(state=state1), 3)
        self.assertEqual(x_2(state=state1), 10)
        self.assertEqual(x_3(state=state1), 3/5)
        self.assertEqual(x_4(state=state1), 0)
        self.assertEqual(pos(state=state1), (2, 3))
        self.assertRaises(IndexError, lambda: z(state=state1))

    def test_equality(self):
        state1 = State(np.array([2, 3]))
        state2 = State(np.array([2, 2]))
        x = Factor(0, "x")
        y = Factor(1, "y")

        x_2 = x * 5
        x_3 = x_2 / 5
        x_4 = x_2 - 8
        y_2 = y * 5

        eq = x == y
        eq2 = x_3 == x_4
        eq3 = x == y and x_2 != x_3
        eq4 = x == y and x_2 == x_3
        eq5 = x_2 == y_2

        self.assertFalse(eq(state=state1))
        self.assertTrue(eq(state=state2))
        self.assertTrue(eq2(state=state1))
        self.assertTrue(eq3(state=state2))
        self.assertFalse(eq4(state=state2))
        self.assertTrue(eq5(state=state2))
        

if __name__ == '__main__':
    unittest.main()
