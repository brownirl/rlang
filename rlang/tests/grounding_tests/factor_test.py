import unittest
import numpy as np
from context import rlang
from rlang.grounding import Factor, Feature, StateResolver
from rlang.grounding.utils.primitives import State
from rlang.grounding.utils.grounding_exceptions import RLangGroundingError as RLangGroundingError

class FactorTest(unittest.TestCase):
    def test_instantiation(self):
        """Test that factors can be instantiated with different types of indices, and verifies that they work on example states"""
        # TODO: Arjan, figure out all the things that should be tested and make some comment sections.
        x = Factor(0, "x")
        y = Factor([0, 1], "y")
        z = Factor([0, 2, 3], "z")

        #z(state=np.array([4, 5, 6, 7]))

        # s1 = State([4, 5, 6, 7])

        # self.assertTrue(np.array_equal(z(state=s1), State([4, 6, 7])))
        # self.assertTrue(np.array_equal(x(state=s1), State(4)))


        state =  [-1,0,1,-2,4,3,8]

        #Test instantiation of factor with int
        factor = Factor(0, "factor")
        self.assertEqual([-1], factor(state=state))

        #Test instantiation of factor with tuple
        factor = Factor((2,5), "factor")
        self.assertEqual([1,-2,4], factor(state=state))
        
        #Test instantiation of factor with tuple where start and end are the same
        factor = Factor((4,4), "factor")
        self.assertEqual([], factor(state=state))

        #Test instantiation of factor with list
        factor = Factor([3,4,5], "factor")
        self.assertEqual([-2,4,3], factor(state=state))

        #Test instantiation of factor with list all indices same
        factor = Factor([3,3,3,3,3], "factor")
        self.assertEqual([-2,-2,-2,-2,-2], factor(state=state))

        #Test instantiation of factor with list in non-ascending order
        factor = Factor([0,3,1,4],"factor")
        self.assertEqual([-1,-2,0,4], factor(state=state))

        #Test instantiation of factor with list with size greater than state space
        factor = Factor([3,1,0,5,6,3,1,2], "factor")
        self.assertEqual([-2,0,-1,3,8,-2,0,1], factor(state=state))

        #TESTS THAT SHOULD THROW ERRORS
        #Test instantiation of factor int: negative
        with self.assertRaises(RLangGroundingError):
            factor = Factor(-3, "factor")

        #Test instantiation of factor int: indexing out of state space
       # with self.assertRaises(RLangGroundingError):
       #     factor = Factor(7, "factor")
       #     factor(state=state) #Should throw an error, right?

        #Test instantiation of factor with tuple: negative start or end
        with self.assertRaises(RLangGroundingError):
            factor = Factor((-2,3), "factor")
        
        with self.assertRaises(RLangGroundingError):
            factor = Factor((3,-1), "factor")

        with self.assertRaises(RLangGroundingError):
            factor = Factor((-1,-3), "factor")
        #Test instantiation of factor with tuple: start greater than end
        with self.assertRaises(RLangGroundingError):
            factor = Factor((4,1), "factor")


        #Test instantiation of factor with tuple: more than two parameters
        with self.assertRaises(RLangGroundingError):
            factor = Factor((1,2,3), "factor")

        #Test instantiation of factor with list: empty
        with self.assertRaises(RLangGroundingError):
            factor = Factor([], "factor")

        #Test instantiation of factor with list: negative number included
        with self.assertRaises(RLangGroundingError):
            factor = Factor([-2,4,1,2,3,6], "factor")

        #Test instantiation of factor with non int, tuple, list data structure
        with self.assertRaises(RLangGroundingError):
            factor = Factor(slice(2,3), "factor")

    
    def test_indexing(self):
        """Test that factors can be indexed using [] syntax and get_factor_from_indexer"""
        # TODO: Arjan, figure out all the things that should be tested and make some comment sections.
        

        # Test that indexed factors have the proper indices
        x = Factor([0, 1], "x")
        y = x[0]

        self.assertEqual(y.indices, [0])

        # Test that indexed factors function properly
        self.assertEqual(y(state=np.array([4, 5, 6, 7])), 4)


        state = [-1,2,6,3,-5,7,-3]

        factor = Factor((0,7), "factor")
        #USING [] syntax
        #Test indexing using slice without step
        sliced_factor = factor[2:4]
        self.assertEqual(sliced_factor.indices, [2,3])

        #Test indexing using slice with step
        sliced_factor = factor[0:5:2]
        self.assertEqual(sliced_factor.indices, [0,2,4])

        #Test indexing where slice start is greater than slice end
        with self.assertRaises(RLangGroundingError):
            sliced_factor = factor[3:1]

        #Test indexing where slice start, end, or step is negative
        with self.assertRaises(RLangGroundingError):
            sliced_factor = factor[-2:3]

        with self.assertRaises(RLangGroundingError):
            sliced_factor = factor[3:-2]

        with self.assertRaises(RLangGroundingError):
            sliced_factor = factor[1:3:-2]

        #Test indexing where slice start equals slice end
        with self.assertRaises(RLangGroundingError):
            sliced_factor = factor[2:2]

        #Test indexing where slice start equals slice end with larger step
        sliced_factor = factor[3:6:4]
        self.assertEqual(sliced_factor.indices, [3])


        #Test slicing factors of factors of factors
        sliced_factor = factor[2:7]
        double_sliced_factor = sliced_factor[2:4]
        self.assertEqual(double_sliced_factor.indices, [4,5])

        #Test with int, negative int, and int out of bounds
        with self.assertRaises(RLangGroundingError):
            sliced_factor = factor[-3]

        with self.assertRaises(RLangGroundingError):
            sliced_factor = factor[9]

        sliced_factor = factor[3]
        self.assertEqual(sliced_factor.indices, [3])

        #Test using int, out of range int (check when indexing at length of factor), and negative int
        sliced_factor = factor.get_factor_from_indexer(3)
        self.assertEqual(sliced_factor.indices, [3])

        with self.assertRaises(RLangGroundingError):
            sliced_factor = factor.get_factor_from_indexer(-3)

        with self.assertRaises(RLangGroundingError):
            sliced_factor = factor.get_factor_from_indexer(9)

        #Test using list regular
        sliced_factor = factor.get_factor_from_indexer([3,1,5,4])
        self.assertEqual(sliced_factor.indices, [3,1,5,4])

        #Test using list with repeated indices
        sliced_factor = factor.get_factor_from_indexer([3,3,3,3])
        self.assertEqual(sliced_factor.indices, [3,3,3,3])

        #Test using list with indices greater than factor indices but smaller than state space
        with self.assertRaises(RLangGroundingError):
            sliced_factor = factor.get_factor_from_indexer([0,1,2,3])
            double_sliced_factor = sliced_factor.get_factor_from_indexer(4)

        #Test using list with index less than 0
        with self.assertRaises(RLangGroundingError):
            sliced_factor = factor.get_factor_from_indexer([3,1,5,9])

        #Test using malformed tuple (more than 2 indices)
        with self.assertRaises(RLangGroundingError):
            sliced_factor = factor.get_factor_from_indexer((2,4,6))

        #Test using tuple with negative start, end, greater start than end, or out of bounds start, end
        with self.assertRaises(RLangGroundingError):
            sliced_factor = factor.get_factor_from_indexer((-2,5))

        with self.assertRaises(RLangGroundingError):
            sliced_factor = factor.get_factor_from_indexer((3,-4))

        with self.assertRaises(RLangGroundingError):
            sliced_factor = factor.get_factor_from_indexer((5,2))

        #Test using regular tuple
        sliced_factor = factor.get_factor_from_indexer((2,4))
        self.assertEqual(sliced_factor.indices, [2,3])

        #Test with neither int, tuple, list
        #with self.assertRaises(RLangGroundingError):
        #    sliced_factor = factor.get_factor_from_indexer(["rlang"])

'''
    def test_domain_resolver(self):

        x = Factor([2, 3], name='x')
        y = x[0].nameit('y')
        z = y[0].nameit('z')
        print(x.name)
        print(y.name)   # We want this to be y

        # self.assertEqual(y(state=np.array([4, 5, 6, 7])), y(x=np.array([6, 7])))
        # self.assertEqual(y(state=np.array([4, 5, 6, 7])), y(x=np.array([6, 7])))

        
        
        # We need to explicitly instantiate a stateresolver here
        
        # self.assertEqual(y(state=np.array([4, 5, 6, 7])), ))
    
        # Predict z from y
        self.assertEqual(z(state=np.array([4, 5, 6, 7])), z(y=[6], x=[6, 7]))

        # We want to test a factor that is S[0,1,2,3] by giving two factors: S[0,1] and S[2,3]
        sr = StateResolver({x: [6, 7], y: [8, 9]})   # This is basically what we want the syntax to look like
        state = sr.get_state()
        y(state=state)
'''

    #def test_feature(self):

        #a = Feature(function = lambda state: state[0]* 3, name='a')
        #b = 2*a
        #b.nameit('b')
        #c = a*b
        #c.nameit('c')
        #d = 2*b
        #d.nameit('d')

        #self.assertEqual(a(state=np.array([4, 5, 6, 7])), 12)
        #self.assertEqual(b(state=np.array([4, 5, 6, 7])), 24)
        #self.assertEqual(b(state=np.array([4, 5, 6, 7])), 2*a(state=np.array([4, 5, 6, 7])))
        #self.assertEqual(b(state=np.array([4, 5, 6, 7])), b(a=12))
        #self.assertEqual(c(state=np.array([4, 5, 6, 7])), 288)
        #self.assertEqual(c(state=np.array([4, 5, 6, 7])), c(a=12, b=24))
        #self.assertEqual(c(state=np.array([4, 5, 6, 7])), c(a=12))
        #self.assertEqual(d(state=np.array([4, 5, 6, 7])), 48)
        #self.assertEqual(d(state=np.array([4, 5, 6, 7])), d(a=12))
        
        # b(a=3)
        # b(state=s)


        # Predict z from x
        # self.assertEqual(z(state=np.array([4, 5, 6, 7])), z(x=[6, 7]))

        # self.assertEqual(y(state=np.array([4, 5, 6, 7])), y(kwargs={(2, 3)=[6, 7]}))   # This is supposed to be indices, but idek how to do this in Python
        # self.assertEqual(y(state=np.array([4, 5, 6, 7])), y(stateresolver))



#     def test_arithmetic_op(self):
#         state1 = State(np.array([2, 3]))

#         x = Factor(0, "x")
#         z = Factor(2, "z")

#         pos = Factor([0, 1], "position")

#         x_1 = x + 1
#         x_2 = x * 5
#         x_3 = x_1 / 5
#         x_4 = x_2 - 10

#         self.assertEqual(x(state=state1), 2)
#         self.assertEqual(x_1(state=state1), 3)
#         self.assertEqual(x_2(state=state1), 10)
#         self.assertEqual(x_3(state=state1), 3 / 5)
#         self.assertEqual(x_4(state=state1), 0)
#         self.assertEqual(pos(state=state1), (2, 3))
#         self.assertRaises(IndexError, lambda: z(state=state1))

#     def test_equality(self):
#         state1 = State(np.array([2, 3]))
#         state2 = State(np.array([2, 2]))
#         x = Factor(0, "x")
#         y = Factor(1, "y")

#         x_2 = x * 5
#         x_3 = x_2 / 5
#         x_4 = x_2 - 8
#         y_2 = y * 5

#         eq = x == y
#         eq2 = x_3 == x_4
#         eq3 = x == y and x_2 != x_3
#         eq4 = x == y and x_2 == x_3
#         eq5 = x_2 == y_2

#         self.assertFalse(eq(state=state1))
#         self.assertTrue(eq(state=state2))
#         self.assertTrue(eq2(state=state1))
#         self.assertTrue(eq3(state=state2))
#         self.assertFalse(eq4(state=state2))
#         self.assertTrue(eq5(state=state2))

#     def test_comparison(self):
#         state1 = State(np.array([2, 3]))
#         state2 = State(np.array([2, 2]))

#         x = Factor(0, "x")
#         y = Factor(1, "y")

#         self.assertTrue(x(state=state1) < y(state=state1))
#         self.assertFalse(y(state=state1) < x(state=state1))
#         self.assertTrue(y(state=state1) > x(state=state1))
#         self.assertFalse(x(state=state1) > y(state=state1))

#         a = Factor(slice(0, 2), "a")
#         b = Factor(slice(0, 2), "b")

#         assert (a(state=state1) > b(state=state2)) == [[False, True]]
#         assert (b(state=state2) < a(state=state1)) == [[False, True]]
#         assert (a(state=state1) >= b(state=state2)) == [[True, True]]
#         assert (b(state=state2) <= a(state=state1)) == [[True, True]]

#         assert (x(state=state1) < a(state=state1)) == [[False, True]]
#         assert (a(state=state1) > x(state=state1)) == [[False, True]]

#     # def test_contains(self):
#     #     x = Factor([0], "x")
#     #     y = Factor([0, 1], "y")
#     #     z = Factor([0, 2, 3], "z")
#     #
#     #     s1 = State([4, 5, 6, 7])
#     #     pred1 = y.contains(x)
#     #     pred2 = z.contains(y)
#     #
#     #     # TODO: unexpected behavior
#     #     print(x(state=s1))
#     #     print(y(state=s1))
#     #     print(pred1(state=s1))

#     def test_getitem(self):
#         pos = Factor([0, 1], "pos")
#         factor = Factor([0, 1, 2, 3])
#         s1 = State([4, 5, 6, 7])
#         item = pos[1]
#         item1 = pos[-1]
#         # print("item 2")
#         item2 = factor[1:3]
#         # self.assertEqual(item1(state=s1), 5)
#         # self.assertEqual(item(state=s1), 5)
#         # print(item2(state=s1))
#         # self.assertEqual(item2(state=s1), [4, 5, 6, 7])


if __name__ == '__main__':
    unittest.main()
