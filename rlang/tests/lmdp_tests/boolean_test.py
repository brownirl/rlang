import sys, os

import numpy as np
import torch
sys.path.append(os.path.abspath("../"))
from rlang.src.lmdp.grounding.booleans.BooleanFunClass import BOOL_FALSE, BOOL_TRUE, BooleanExpression, bool_and, bool_not, bool_or, cast_to_boolean, grounded_and
from rlang.src.lmdp.grounding.expressions.ExpressionsClass import Expression

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
        self.assertFalse(true_and_true.and_(False)())
        self.assertFalse(false_and_false())
        self.assertFalse(true_and_false())
        self.assertFalse(false_and_true())
        self.assertTrue(true_and_true())

    def test_or(self):
        false_or_false = BOOL_FALSE.or_(BOOL_FALSE)
        true_or_false = BOOL_TRUE.or_(BOOL_FALSE)
        false_or_true = BOOL_FALSE.or_(BOOL_TRUE)
        true_or_true = BOOL_TRUE.or_(BOOL_TRUE)
        self.assertTrue(true_or_false.or_(1 != 1)())
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
        false_or_true = BOOL_FALSE.or_(BOOL_TRUE)
        self.assertFalse(false_or_true.not_()())

    def test_grounded_or(self):
        pass

    def test_grounded_and(self):
        pass
        # test = np.array([[1, 2, 3], [4, 5, 6]], int)
        # print(grounded_and(BOOL_FALSE, test)())

    def test_bool_or(self):
        test1 = Expression(lambda **args: 1 == 1, [], ["boolean"])
        test2 = Expression(lambda **args: 1 + 1 < 1, [], ["boolean"])
        test3 = BOOL_FALSE
        test4 = Expression(lambda **args: 1 != 1, [], ["boolean"])
        true_and_false = BOOL_TRUE.and_(BOOL_FALSE)
        true_and_true = BOOL_TRUE.and_(BOOL_TRUE)
        true_or_false = BOOL_TRUE.or_(BOOL_FALSE)

        self.assertTrue(bool_or(test1, test2, test3)())
        self.assertTrue(bool_or(test1, true_and_false, test3)())
        self.assertFalse(bool_or(test4, test3, true_and_false)())
        self.assertTrue(bool_or(test2, test3, true_or_false)())

    def test_bool_and(self):
        test1 = Expression(lambda **args: 1 == 1, [], ["boolean"])
        test2 = Expression(lambda **args: 1 + 1 > 1, [], ["boolean"])
        test3 = BOOL_TRUE
        test4 = Expression(lambda **args: 1 != 1, [], ["boolean"])
        true_and_false = BOOL_TRUE.and_(BOOL_FALSE)
        true_and_true = BOOL_TRUE.and_(BOOL_TRUE)
        true_or_false = BOOL_TRUE.or_(BOOL_FALSE)

        self.assertTrue(bool_and(test1, test2, test3)())
        self.assertFalse(bool_and(test1, true_and_false, test3)())
        self.assertFalse(bool_and(test4, test1, test2, true_and_true)())
        self.assertTrue(bool_and(test1, test2, test3, true_or_false)())

    def test_bool_not(self):
        test1 = BooleanExpression(lambda **args: 1 == 1, [], ["boolean"])
        test2 = Expression(lambda **args: 1 + 1 > 1, [], ["boolean"])
        test3 = BOOL_TRUE
        test4 = Expression(lambda **args: 1 != 1, [], ["boolean"])
        true_and_false = BOOL_TRUE.and_(BOOL_FALSE)
        true_and_true = BOOL_TRUE.and_(BOOL_TRUE)
        true_or_false = BOOL_TRUE.or_(BOOL_FALSE)

        self.assertFalse(bool_not(test1)())
        self.assertFalse(bool_not(bool_or(test1, true_and_false, test3))())
        self.assertTrue(bool_not(true_and_false)())
        self.assertFalse(bool_not(bool_and(test2, test3, true_or_false))())

    def test_cast_to_boolean(self):
        test1 = Expression(lambda **args: 1 == 1, [], ["boolean"])
        test2 = BooleanExpression(lambda **args: 1 + 1 > 1, [], ["boolean"])

        self.assertTrue(cast_to_boolean(test1)())
        self.assertTrue(cast_to_boolean(test2)())
    
if __name__ == "__main__":
    unittest.main()