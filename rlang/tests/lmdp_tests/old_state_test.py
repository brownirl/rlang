import unittest
import numpy as np
from lmdp.grounding.states.StateClass import BatchedState, State, state_builder
from lmdp.grounding.states.StateGroundingClass import StateFactor, StateFeature

class TestState(unittest.TestCase):
    
    def test_state(self):
        pass
        s = state_builder(np.array([[1, 2, 3], [1, 2, 3]]))
        s[:2] = np.array([-1, -1])
        self.assertTrue((s == np.array([[-1, -1, 3], [-1, -1, 3]])).all())

        ndarr = np.random.rand(*(3, 2))
        s = BatchedState(ndarr)
        self.assertEqual(s.dim(), (2, ))
        self.assertEqual(s.shape, (2, ))
    
    def test_state_factor(self):
        state1 = State(data=np.array([2, 3]))
        state2 = State(data=np.array([2, 2]))

        mat = np.random.rand(4, 3)
        batched_s = BatchedState(data=mat)

        x = StateFactor(0, "x")
        y = StateFactor(1, "y")
        z = StateFactor(2, "z")

        pos = StateFactor([0, 1], "position")

        x_1 = x + 1
        diag = x == y

        self.assertEqual(x(state1), 2)
        self.assertEqual(x_1(state1), 3)
        self.assertFalse(diag(state1))
        self.assertTrue(diag(state2))
        self.assertEqual(pos(state1), (2, 3))
        self.assertRaises(IndexError, lambda: z(state1))
        self.assertTrue((x(state1) in pos(state1)))
        self.assertTrue((z(batched_s) == mat[:,2:3]).all())
    
    def test_state_feature(self):
        state1 = State(data=np.array([2, 3]))
        pos = StateFactor([0, 1], "position")
        x = StateFeature(pos[0], 1)
        y = StateFactor(1, "y")
        self.assertEqual(x(state1), 2)

        test = StateFeature((lambda s: x(s) + 1), 1)
        test2 = StateFeature((lambda s: x(s) + y(s)), 1)
        self.assertEqual(test(state1), 3)
        self.assertEqual(test2(state1), 5)

if __name__ == "__main__":
    unittest.main()