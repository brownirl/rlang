import unittest
import numpy as np
from rlang.src.grounding import ActionSpace

class ActionSpaceTest(unittest.TestCase):
    def test_from_action(self):
        acts = ActionSpace(float, (0, 2))
        acts1 = ActionSpace.from_action(action=np.ndarray([0, 2]))
        self.assertEqual(acts.dtype, acts1.dtype)
        self.assertEqual(acts.shape, acts1.shape)

if __name__ == '__main__':
    unittest.main()