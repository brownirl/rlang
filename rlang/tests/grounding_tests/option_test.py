import unittest
from grounding.internals import Action
import numpy as np
from rlang.src.grounding import Action, Option, State, Factor, Proposition, Policy

class OptionTest(unittest.TestCase):
    def test_termination(self):
        a = Action([0, 1])
        s = State([0, 1, 2, 3])
        pos = Factor([0, 1])
        x = pos[0]
        y = pos[1]
        termincation_func = x + 1 == y
        initiation = Proposition(termincation_func)
        policy = Policy(lambda: a)
        termination = Proposition(termincation_func)
        option = Option(initiation, policy, termination)
        self.assertEqual(option(state=s), None)

    def test_can_execute(self):
        a = Action([0, 1])
        s = State([0, 1, 2, 3])
        pos = Factor([0, 1])
        x = pos[0]
        y = pos[1]
        initiation = Proposition(x + 1 == y)
        policy = Policy(lambda: a)
        termination = Proposition(x + 1 == y)
        option = Option(initiation, policy, termination)
        self.assertTrue(option.can_initiate(state=s))

        initiation2 = Proposition(x == y)
        option2 = Option(initiation2, policy, termination)
        self.assertFalse(option2.can_initiate(state=s))


if __name__ == '__main__':
    unittest.main()