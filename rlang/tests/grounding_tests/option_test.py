import unittest
from grounding.internals import Action
import numpy as np
from rlang.src.grounding import Action, Option, State, Factor, Predicate, Policy

class OptionTest(unittest.TestCase):
    def test_instantiation(self):
        a = Action([0, 1])
        s = State([0, 1, 2, 3])
        pos = Factor([0, 1])
        x = pos[0]
        y = pos[1]
        func = lambda state: a
        initiation_func = x + 1 == y
        termincation_func = x == y
        initiation = Predicate(initiation_func)
        policy = Policy(function=func)
        termination = Predicate(termincation_func)
        option = Option(initiation, policy, termination)



if __name__ == '__main__':
    unittest.main()