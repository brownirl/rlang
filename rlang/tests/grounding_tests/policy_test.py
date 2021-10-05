import unittest
from grounding.groundings import Policy
from grounding.internals import Action
import numpy as np
from rlang.src.grounding import Factor, Feature, State

class PolicyTest(unittest.TestCase):
    def test_instantiation(self):
        a = Action([0, 1])
        s = State([0, 1, 2, 3])
        pos = Factor([0, 1])
        x = pos[0]
        y = pos[1]
        func = lambda state: a if x + 1 == y else None
        policy = Policy(function=func)
        self.assertEqual(policy(state=s), a)

if __name__ == '__main__':
    unittest.main()