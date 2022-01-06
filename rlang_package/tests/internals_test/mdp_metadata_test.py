import unittest
import numpy as np
from rlang.src.grounding import MDPMetadata, StateSpace, ActionSpace

class MDP_Metadata_Test(unittest.TestCase):
    def test_from_state_action(self):
        ss = StateSpace(dtype=float, shape=(1,3))
        acts = ActionSpace(dtype=float, shape=(1,1))
        mdp1 = MDPMetadata(state_space=ss, action_space=acts)
        mdp2 = MDPMetadata.from_state_action(action=np.ndarray([1, 1]), state=np.ndarray([1, 3]))
        self.assertEqual(mdp1.state_space.shape, mdp2.state_space.shape)
        self.assertEqual(mdp1.action_space.shape, mdp2.action_space.shape)
        self.assertEqual(mdp1.state_space.dtype, mdp2.state_space.dtype)
        self.assertEqual(mdp1.action_space.dtype, mdp2.action_space.dtype)

if __name__ == '__main__':
    unittest.main()