import unittest
import numpy as np

from .context import rlang
from rlang import Factor, Feature, State


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
        self.assertEqual(x_3(state=state1), 3 / 5)
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

    def test_comparison(self):
        state1 = State(np.array([2, 3]))
        state2 = State(np.array([2, 2]))

        x = Factor(0, "x")
        y = Factor(1, "y")

        self.assertTrue(x(state=state1) < y(state=state1))
        self.assertFalse(y(state=state1) < x(state=state1))
        self.assertTrue(y(state=state1) > x(state=state1))
        self.assertFalse(x(state=state1) > y(state=state1))

        a = Factor(slice(0, 2), "a")
        b = Factor(slice(0, 2), "b")

        assert (a(state=state1) > b(state=state2)) == [[False, True]]
        assert (b(state=state2) < a(state=state1)) == [[False, True]]
        assert (a(state=state1) >= b(state=state2)) == [[True, True]]
        assert (b(state=state2) <= a(state=state1)) == [[True, True]]

        assert (x(state=state1) < a(state=state1)) == [[False, True]]
        assert (a(state=state1) > x(state=state1)) == [[False, True]]

    # def test_contains(self):
    #     x = Factor([0], "x")
    #     y = Factor([0, 1], "y")
    #     z = Factor([0, 2, 3], "z")
    #
    #     s1 = State([4, 5, 6, 7])
    #     pred1 = y.contains(x)
    #     pred2 = z.contains(y)
    #
    #     # TODO: unexpected behavior
    #     print(x(state=s1))
    #     print(y(state=s1))
    #     print(pred1(state=s1))

    def test_getitem(self):
        pos = Factor([0, 1], "pos")
        factor = Factor([0, 1, 2, 3])
        s1 = State([4, 5, 6, 7])
        item = pos[1]
        item1 = pos[-1]
        # print("item 2")
        item2 = factor[1:3]
        # self.assertEqual(item1(state=s1), 5)
        # self.assertEqual(item(state=s1), 5)
        # print(item2(state=s1))
        # self.assertEqual(item2(state=s1), [4, 5, 6, 7])


if __name__ == '__main__':
    unittest.main()
