import unittest
from rlang.src.grounding import Predicate, State


class PredicateTest(unittest.TestCase):
    def test_instantiation(self):
        x = Predicate(function=lambda state: state == State(3))
        s1 = State(3)


if __name__ == '__main__':
    unittest.main()
