import sys, os
sys.path.append(os.path.abspath("../"))
from rlang.src.lmdp.grounding.booleans.BooleanFunClass import BOOL_FALSE, BOOL_TRUE, BooleanExpression


import unittest

class TestBoolean(unittest.TestCase):

    def test_true(self):
        test1 = BooleanExpression(lambda **args: 1 == 1, [])
        self.assertTrue(test1())
        test2 = BooleanExpression(lambda **args: 1 + 1 > 1, [])
        self.assertTrue(test2())
        self.assertTrue(BOOL_TRUE())

    def test_false(self):
        test1 = BooleanExpression(lambda **args: 1 != 1, [])
        test2 = BooleanExpression(lambda **args: 1 + 1 < 1, [])
        self.assertFalse(test1())
        self.assertFalse(test2())
        self.assertFalse(BOOL_FALSE())
    
    def test_and(self):
        false_and_false = BOOL_FALSE.and_(BOOL_FALSE)
        true_and_false = BOOL_TRUE.and_(BOOL_FALSE)
        false_and_true = BOOL_FALSE.and_(BOOL_TRUE)
        true_and_true = BOOL_TRUE.and_(BOOL_TRUE)
        self.assertFalse(false_and_false())
        self.assertFalse(true_and_false())
        self.assertFalse(false_and_true())
        self.assertTrue(true_and_true())
        print(true_and_false.__repr__())

    def test_or(self):
        false_or_false = BOOL_FALSE.or_(BOOL_FALSE)
        true_or_false = BOOL_TRUE.or_(BOOL_FALSE)
        false_or_true = BOOL_FALSE.or_(BOOL_TRUE)
        true_or_true = BOOL_TRUE.or_(BOOL_TRUE)
        self.assertFalse(false_or_false())
        self.assertTrue(true_or_false())
        self.assertTrue(false_or_true())
        self.assertTrue(true_or_true())

    def test_not(self):
        self.assertTrue(BOOL_FALSE.not_()())
        self.assertFalse(BOOL_TRUE.not_()())
        false1 = BooleanExpression(lambda **args: 1 != 1, [])
        self.assertTrue(false1.not_()())   
        true1 = BooleanExpression(lambda **args: 1 + 1 > 1, [])
        self.assertFalse(true1.not_()())

    def test_grounded_or(self):
        pass
    
if __name__ == "__main__":
    unittest.main()