import unittest
import numpy as np
from rlang.src.grounding import StateSpace

class StateSpaceTest(unittest.TestCase):
    def test_from_state(self):
        ss = StateSpace(float, (1, 2))
        ss1 = StateSpace.from_state(state=np.ndarray([1, 2]))
        self.assertEqual(ss.dtype, ss1.dtype)
        self.assertEqual(ss.shape, ss1.shape)

if __name__ == '__main__':
    unittest.main()