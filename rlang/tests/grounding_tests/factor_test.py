import unittest
import numpy as np
from context import rlang
from rlang.grounding import Factor
from rlang.grounding.utils.grounding_exceptions import RLangGroundingError as RLangGroundingError

class FactorTest(unittest.TestCase):
    def test_instantiation(self):
        """Test that factors can be instantiated with different types of indices, and verifies that they work on example states"""

        state =  [-1,0,1,-2,4,3,8]

        # Test instantiation of factor with int
        factor_ind0 = Factor(0, "factor")
        self.assertEqual(-1, factor_ind0(state=state))

        # Test instantiation of factor with tuple
        factor_ind2to5 = Factor((2,5), "factor")
        self.assertEqual([1,-2,4], factor_ind2to5(state=state))
        
        # Test instantiation of factor with tuple where start and end are the same
        factor_ind4to4 = Factor((4,4), "factor")
        self.assertEqual([], factor_ind4to4(state=state))

        # Test instantiation of factor with list
        factor_ind345 = Factor([3,4,5], "factor")
        self.assertEqual([-2,4,3], factor_ind345(state=state))

        # Test instantiation of factor with list all indices same
        factor_ind3s = Factor([3,3,3,3,3], "factor")
        self.assertEqual([-2,-2,-2,-2,-2], factor_ind3s(state=state))

        # Test instantiation of factor with list in non-ascending order
        factor_ind0314 = Factor([0,3,1,4],"factor")
        self.assertEqual([-1,-2,0,4], factor_ind0314(state=state))

        # Test instantiation of factor with list with size greater than state space
        factor_indrandom = Factor([3,1,0,5,6,3,1,2], "factor")
        self.assertEqual([-2,0,-1,3,8,-2,0,1], factor_indrandom(state=state))

        # TESTS THAT SHOULD THROW ERRORS
        # Test instantiation of factor int: negative
        with self.assertRaises(RLangGroundingError):
            factor_indnegative3 = Factor(-3, "factor")

        # Test instantiation of factor int: indexing out of state space
        with self.assertRaises(RLangGroundingError):
            factor_ind7 = Factor(7, "factor")
            factor_ind7(state=state) # Should throw an error, right?

        # Test instantiation of factor with tuple: negative start or end
        with self.assertRaises(RLangGroundingError):
            factor_indnegative2to3 = Factor((-2,3), "factor")
        
        with self.assertRaises(RLangGroundingError):
            factor_ind_pos_neg = Factor((3,-1), "factor")

        with self.assertRaises(RLangGroundingError):
            factor_negative_1_negative_3 = Factor((-1,-3), "factor")
        # Test instantiation of factor with tuple: start greater than end
        with self.assertRaises(RLangGroundingError):
            factor_ind_start_ge_end = Factor((4,1), "factor")


        # Test instantiation of factor with tuple: more than two parameters
        with self.assertRaises(RLangGroundingError):
            factor_ind_many_tuple = Factor((1,2,3), "factor")

        # Test instantiation of factor with list: empty
        with self.assertRaises(RLangGroundingError):
            factor_empty = Factor([], "factor")

        # Test instantiation of factor with list: negative number included
        with self.assertRaises(RLangGroundingError):
            factor_neg_with_pos = Factor([-2,4,1,2,3,6], "factor")

        # Test instantiation of factor with non int, tuple, list data structure
        with self.assertRaises(RLangGroundingError):
            factor_slice_2_3 = Factor(slice(2,3), "factor")

    
    def test_indexing(self):
        """Test that factors can be indexed using [] syntax and get_factor_from_indexer"""

        state = [-1,2,6,3,-5,7,-3]

        factor_0_7 = Factor((0,7), "factor")
        # USING [] syntax
        # Test indexing using slice without step
        sliced_factor_2_4 = factor_0_7[2:4]
        self.assertEqual(sliced_factor_2_4.indices, [2,3])

        # Test indexing using slice with step
        sliced_factor_0_5_2 = factor_0_7[0:5:2]
        self.assertEqual(sliced_factor_0_5_2.indices, [0,2,4])

        # Test indexing where slice start is greater than slice end
        with self.assertRaises(RLangGroundingError):
            sliced_factor_3_1 = factor_0_7[3:1]

        # Test indexing where slice start, end, or step is negative
        with self.assertRaises(RLangGroundingError):
            sliced_factor = factor_0_7[-2:3]

        with self.assertRaises(RLangGroundingError):
            sliced_factor = factor_0_7[3:-2]

        with self.assertRaises(RLangGroundingError):
            sliced_factor = factor_0_7[1:3:-2]

        # Test indexing where slice start equals slice end
        with self.assertRaises(RLangGroundingError):
            sliced_factor = factor_0_7[2:2]

        # Test indexing where slice start equals slice end with larger step
        sliced_factor = factor_0_7[3:6:4]
        self.assertEqual(sliced_factor.indices, [3])

        # Test slicing factors of factors of factors
        sliced_factor = factor_0_7[2:7]
        double_sliced_factor = sliced_factor[2:4]
        self.assertEqual(double_sliced_factor.indices, [4,5])

        # Test with int, negative int, and int out of bounds
        with self.assertRaises(RLangGroundingError):
            sliced_factor = factor_0_7[-3]

        with self.assertRaises(RLangGroundingError):
            sliced_factor = factor_0_7[9]

        sliced_factor = factor_0_7[3]
        self.assertEqual(sliced_factor.indices, [3])

        # Test using int, out of range int (check when indexing at length of factor), and negative int
        sliced_factor = factor_0_7.get_factor_from_indexer(3)
        self.assertEqual(sliced_factor.indices, [3])

        with self.assertRaises(RLangGroundingError):
            sliced_factor = factor_0_7.get_factor_from_indexer(-3)

        with self.assertRaises(RLangGroundingError):
            sliced_factor = factor_0_7.get_factor_from_indexer(9)

        # Test using list regular
        sliced_factor = factor_0_7.get_factor_from_indexer([3,1,5,4])
        self.assertEqual(sliced_factor.indices, [3,1,5,4])

        # Test using list with repeated indices
        sliced_factor = factor_0_7.get_factor_from_indexer([3,3,3,3])
        self.assertEqual(sliced_factor.indices, [3,3,3,3])

        # Test using list with indices greater than factor indices but smaller than state space
        with self.assertRaises(RLangGroundingError):
            sliced_factor = factor_0_7.get_factor_from_indexer([0,1,2,3])
            double_sliced_factor = sliced_factor.get_factor_from_indexer(4)

        # Test using list with index less than 0
        with self.assertRaises(RLangGroundingError):
            sliced_factor = factor_0_7.get_factor_from_indexer([3,1,5,9])

        # Test using malformed tuple (more than 2 indices)
        with self.assertRaises(RLangGroundingError):
            sliced_factor = factor_0_7.get_factor_from_indexer((2,4,6))

        # Test using tuple with negative start, end, greater start than end, or out of bounds start, end
        with self.assertRaises(RLangGroundingError):
            sliced_factor = factor_0_7.get_factor_from_indexer((-2,5))

        with self.assertRaises(RLangGroundingError):
            sliced_factor = factor_0_7.get_factor_from_indexer((3,-4))

        with self.assertRaises(RLangGroundingError):
            sliced_factor = factor_0_7.get_factor_from_indexer((5,2))

        # Test using regular tuple
        sliced_factor = factor_0_7.get_factor_from_indexer((2,4))
        self.assertEqual(sliced_factor.indices, [2,3])

    def test_arithmetic_op(self):
        """Test that factors can be added, subtracted, multiplied, and divided by other factors"""
        state1 = np.array([2, 3])

        x = Factor(0, "x")
        z = Factor(2, "z")

        pos = Factor([0, 1], "position")

        x_1 = x + 1
        x_2 = x * 5
        x_3 = x_1 / 5
        x_4 = x_2 - 10

        self.assertEqual(x(state=state1), 2)
        self.assertEqual(x_1(state=state1), 3)
        self.assertEqual(x_2(state=state1), 10)
        self.assertEqual(x_3(state=state1), 3 / 5)
        self.assertEqual(x_4(state=state1), 0)
        self.assertRaises(RLangGroundingError, lambda: z(state=state1))

    def test_equality(self):
        """Test that factors can be compared to other factors using == and !="""
        state1 = np.array([2, 3])
        state2 = np.array([2, 2])
        x = Factor(0, "x")
        y = Factor(1, "y")

        x_2 = x * 5
        x_3 = x_2 / 5
        x_4 = x_2 - 8
        y_2 = y * 5

        eq = x == y
        eq2 = x_3 == x_4
        eq3 = x == y and x_2 != x_3
        eq4 = x == y and x_2 == x_3
        eq5 = x_2 == y_2

        self.assertFalse(eq(state=state1))
        self.assertTrue(eq(state=state2))
        self.assertTrue(eq2(state=state1))
        self.assertTrue(eq3(state=state2))
        self.assertFalse(eq4(state=state2))
        self.assertTrue(eq5(state=state2))

    def test_comparison(self):
        """Test that factors can be compared to other factors using <, >, <=, and >="""
        state1 = np.array([2, 3])
        state2 = np.array([2, 2])

        x = Factor(0, "x")
        y = Factor(1, "y")

        self.assertTrue(x(state=state1) < y(state=state1))
        self.assertFalse(y(state=state1) < x(state=state1))
        self.assertTrue(y(state=state1) > x(state=state1))
        self.assertFalse(x(state=state1) > y(state=state1))

        a = Factor((0, 2), "a")
        b = Factor((0, 2), "b")

        self.assertFalse((a(state=state1) > b(state=state2))[0])
        self.assertTrue((a(state=state1) > b(state=state2))[1])

        self.assertTrue((a(state=state1) >= b(state=state2))[0])
        self.assertTrue((a(state=state1) >= b(state=state2))[1])


if __name__ == '__main__':
    unittest.main()
