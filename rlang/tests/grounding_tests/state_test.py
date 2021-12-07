import unittest
import numpy as np
from rlang.src.grounding import State

# just test batched primitives

class StateTest(unittest.TestCase):
    def test_instantiation(self):
        s1 = State(1)
        s2 = State([1])
        s3 = State([0, 1, 2])
        s3b = State([0, 1, 2])
        s4 = State([[1, 1, 1], [1, 1, 1]])
        s5 = State(np.array([1]))
        s6 = State(np.array([[1]]))
        s7 = State(np.ones((2, 3)))

        self.assertEqual(s1, s2)
        self.assertEqual(s1, s5)
        self.assertEqual(s1, s6)
        self.assertEqual(s3, s3b)
        # self.assertTrue(np.all(s4 == s7))
        # self.assertTrue(np.all(s1 != s7))
        # self.assertFalse(np.all(s1 == s7))

    def test_batched_state(self):
        s1 = State(1)
        s2 = State([1])
        s3 = State([0, 1, 2])
        s3b = State([0, 1, 2])
        s4 = State([[1, 1, 1], [1, 1, 1]])

        # QUESTION: is this allowed?
        # batched = State([s1, s2, s3])
        # batched1 = State([s2, s1, s3])
        # print(batched == batched1)

        


if __name__ == '__main__':
    unittest.main()
