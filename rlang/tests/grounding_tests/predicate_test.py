import unittest
from rlang.src.grounding import Predicate, State, BOOL_FALSE, BOOL_TRUE


class PredicateTest(unittest.TestCase):
    def test_instantiation(self):
        x = Predicate(function=lambda state: state == State(3))
        s1 = State(3)
        self.assertTrue(x(s1))
    
    def test_true(self):
        test1 = Predicate(lambda state: 1 == 1, [])
        self.assertTrue(test1())
        test2 = Predicate(lambda state: 1 + 1 > 1, [])
        self.assertTrue(test2())
        self.assertTrue(BOOL_TRUE())

    def test_false(self):
        test1 = Predicate(lambda **args: 1 != 1, [])
        test2 = Predicate(lambda **args: 1 + 1 < 1, [])
        self.assertFalse(test1())
        self.assertFalse(test2())
        self.assertFalse(BOOL_FALSE())
    
    def test_and(self):
        false_and_false = BOOL_FALSE & (BOOL_FALSE)
        true_and_false = BOOL_TRUE & (BOOL_FALSE)
        false_and_true = BOOL_FALSE & (BOOL_TRUE)
        true_and_true = BOOL_TRUE & (BOOL_TRUE)
        self.assertFalse(true_and_true & (False)())
        self.assertFalse(false_and_false())
        self.assertFalse(true_and_false())
        self.assertFalse(false_and_true())
        self.assertTrue(true_and_true())

    def test_or(self):
        false_or_false = BOOL_FALSE | (BOOL_FALSE)
        true_or_false = BOOL_TRUE | (BOOL_FALSE)
        false_or_true = BOOL_FALSE | (BOOL_TRUE)
        true_or_true = BOOL_TRUE | (BOOL_TRUE)
        self.assertTrue(true_or_false | (1 != 1)())
        self.assertFalse(false_or_false())
        self.assertTrue(true_or_false())
        self.assertTrue(false_or_true())
        self.assertTrue(true_or_true())
    
    def test_not(self):
        self.assertTrue((not BOOL_FALSE)())
        self.assertFalse((not BOOL_TRUE)())
        false1 = Predicate(lambda state: 1 != 1, [])
        self.assertTrue((not false1)())   
        true1 = Predicate(lambda state: 1 + 1 > 1, [])
        self.assertFalse((not true1)())
        false_or_true = BOOL_FALSE.or_(BOOL_TRUE)
        self.assertFalse((not false_or_true)())

if __name__ == '__main__':
    unittest.main()
