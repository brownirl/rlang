import unittest
from rlang.src.grounding import Predicate, State


class PredicateTest(unittest.TestCase):
    def test_true(self):
        BOOL_TRUE = Predicate(function=lambda state: True)
        test1 = Predicate(lambda state: 1 == 1, [])
        self.assertTrue(test1(state=None))
        test2 = Predicate(lambda state: 1 + 1 > 1, [])
        self.assertTrue(test2(state=None))
        self.assertTrue(BOOL_TRUE(state=None))

        test3 = Predicate(function=lambda state: state == State(3))
        s1 = State(3)
        self.assertTrue(test3(state=s1))
        test4 = Predicate(function=lambda state: state != State(4))
        self.assertTrue(test4(state=s1))

    def test_false(self):
        BOOL_FALSE = Predicate(function=lambda state: False)
        test1 = Predicate(lambda **args: 1 != 1, [])
        test2 = Predicate(lambda **args: 1 + 1 < 1, [])
        self.assertFalse(test1(state=None))
        self.assertFalse(test2(state=None))
        self.assertFalse(BOOL_FALSE(state=None))

    def test_and(self):
        BOOL_TRUE = Predicate(function=lambda state: True)
        BOOL_FALSE = Predicate(function=lambda state: False)
        false_and_false = BOOL_FALSE & (BOOL_FALSE)
        true_and_false = BOOL_TRUE & (BOOL_FALSE)
        false_and_true = BOOL_FALSE & (BOOL_TRUE)
        true_and_true = BOOL_TRUE & (BOOL_TRUE)
        self.assertFalse((true_and_true & False)(state=None))
        self.assertFalse(false_and_false(state=None))
        self.assertFalse(true_and_false(state=None))
        self.assertFalse(false_and_true(state=None))
        self.assertTrue(true_and_true(state=None))

    def test_or(self):
        BOOL_TRUE = Predicate(function=lambda state: True)
        BOOL_FALSE = Predicate(function=lambda state: False)
        false_or_false = BOOL_FALSE | (BOOL_FALSE)
        true_or_false = BOOL_TRUE | (BOOL_FALSE)
        false_or_true = BOOL_FALSE | (BOOL_TRUE)
        true_or_true = BOOL_TRUE | (BOOL_TRUE)
        self.assertTrue((true_or_false | False)(state=None))
        self.assertFalse(false_or_false(state=None))
        self.assertTrue(true_or_false(state=None))
        self.assertTrue(false_or_true(state=None))
        self.assertTrue(true_or_true(state=None))

    def test_not(self):
        BOOL_TRUE = Predicate(function=lambda state: True)
        BOOL_FALSE = Predicate(function=lambda state: False)
        self.assertTrue((~BOOL_FALSE)(state=None))
        self.assertFalse((~BOOL_TRUE)(state=None))
        false1 = Predicate(lambda state: 1 != 1, [])
        self.assertTrue((~false1)(state=None))
        true1 = Predicate(lambda state: 1 + 1 > 1, [])
        self.assertFalse((~true1)(state=None))
        false_or_true = BOOL_FALSE | (BOOL_TRUE)
        self.assertFalse((~false_or_true)(state=None))

if __name__ == '__main__':
    unittest.main()
