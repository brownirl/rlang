
import sys, os
from typing import Sequence

import numpy as np
sys.path.append(os.path.abspath("../"))
from lmdp.grounding.real.RealExpressionClass import RealExpression
import unittest

class TestRealExpressions(unittest.TestCase):
    
    def test_add(self):
       float_exp = RealExpression(lambda **args: 1.5)
       float_exp += 2.7
       self.assertEqual(float_exp(), 4.2)
       
       arr_exp = RealExpression(lambda **args: [1, 3, 1], dimension=3)
       arr = np.array([1, 2, 3])
       arr_exp += arr
       self.assertTrue((arr_exp() == [2, 5, 4]).all())

    def test_sub(self):
        float_exp = RealExpression(lambda **args: 1.5)
        float_exp -= 2.7
        self.assertAlmostEqual(float_exp(), -1.2)
       
        arr_exp = RealExpression(lambda **args: np.array([1, 3, 1]), dimension=3)
        arr = np.array([1, 2, 3])
        arr_exp -= arr
        self.assertTrue((arr_exp() == [0, 1, -2]).all())

    def test_mul(self):
        float_exp = RealExpression(lambda **args: 1.5)
        float_exp *= 2
        self.assertEqual(float_exp(), 3)

        arr_exp = RealExpression(lambda **args: np.array([1, 3, 1]), dimension=3)
        arr_exp *= 2
        self.assertTrue((arr_exp() == [2, 6, 2]).all())
        arr_exp *= np.array([4, 5, 6])
        self.assertTrue((arr_exp() == [8, 30, 12]).all())

    def test_true_div(self):
        float_exp = RealExpression(lambda **args: 1.5)
        float_exp /= 2
        self.assertEqual(float_exp(), 0.75)

        arr_exp = RealExpression(lambda **args: np.array([4, 6, 8]), dimension=3)
        arr_exp /= 2
        self.assertTrue((arr_exp() == [2, 3, 4]).all())

    def test_lt(self):
        float_exp = RealExpression(lambda **args: 1.5)
        self.assertTrue((float_exp < 2)())
        self.assertFalse((float_exp < 1.5)())

    def test_le(self):
        float_exp = RealExpression(lambda **args: 1.5)
        self.assertTrue((float_exp <= 2)())
        self.assertTrue((float_exp <= 1.5)())

    def test_eq(self):
        float_exp = RealExpression(lambda **args: 1.5)
        self.assertFalse((float_exp == 2)())
        self.assertTrue((float_exp == 1.5)())
        

    def test_neq(self):
        float_exp = RealExpression(lambda **args: 1.5)
        self.assertTrue((float_exp != 2)())
        self.assertFalse((float_exp != 1.5)())

    def test_gt(self):
        float_exp = RealExpression(lambda **args: 1.5)
        self.assertTrue((float_exp > -1)())
        self.assertFalse((float_exp > 1.5)())

    def test_ge(self):
        float_exp = RealExpression(lambda **args: 1.5)
        self.assertTrue((float_exp >= -1)())
        self.assertTrue((float_exp >= 1.5)())

    def test_get_item(self):
        arr_exp = RealExpression(lambda **args: np.array([4, 6, 8]), dimension=3)
        self.assertEqual(arr_exp[1](), 6)

        arr_exp1 = RealExpression(lambda **args: np.array([1, 2, 3, 4, 5, 6]), dimension=6)
        self.assertTrue((arr_exp1[:10:2]() == [1, 3, 5]).all())

        # TODO: can't leave idx.stop blank
        # print(arr_exp1[::-1]())

        ndarr_exp = RealExpression(lambda **args: np.array([[1, 2, 3], [4, 5, 6]]), dimension=(2,3))
        self.assertRaises(IndexError, lambda:ndarr_exp()[(3,2)])
        self.assertEqual(ndarr_exp[(1,2)](), 6)
        self.assertEqual(ndarr_exp[0,2](), 3)

    def test_compose(self):
        pass
    


if __name__ == "__main__":
    unittest.main()
