import unittest
import numpy as np
from context import rlang

from rlang.grounding import Factor, Feature

class FactorTest(unittest.TestCase):

    def test_instantiation(self):
        return
        """Test that factors can be instantiated with different types of indices, and verifies that they work on example states"""
        # TODO: Arjan, figure out all the things that should be tested and make some comment sections.
        x = Factor(0, "x")
        y = Factor([0, 1], "y")
        z = Factor([0, 2, 3], "z")

        z(state=np.array([4, 5, 6, 7]))

        # s1 = State([4, 5, 6, 7])

        # self.assertTrue(np.array_equal(z(state=s1), State([4, 6, 7])))
        # self.assertTrue(np.array_equal(x(state=s1), State(4)))

        #Test instantiation of factor with int

        #Test instantiation of factor with tuple

        #Test instantiation of factor with tuple where start and end are the same

        #Test instantiation of factor with list

        #Test instantiation of factor with list all indices same

        #Test instantiation of factor with list in non-ascending order

        #Test instantiation of factor with list with size greater than state space

        #TESTS THAT SHOULD THROW ERRORS
        #Test instantiation of factor int: negative

        #Test instantiation of factor int: indexing out of state space

        #Test instantiation of factor with tuple: negative start or end

        #Test instantiation of factor with tuple: start greater than end

        #Test instantiation of factor with tuple: more than two parameters

        #Test instantiation of factor with list: empty

        #Test instantiation of factor with list: negative number included

        #Test instantiation of factor with non int, tuple, list data structure

    
    def test_indexing(self):
        return
        """Test that factors can be indexed using [] syntax and get_factor_from_indexer"""
        # TODO: Arjan, figure out all the things that should be tested and make some comment sections.
        

        # Test that indexed factors have the proper indices
        x = Factor([0, 1], "x")
        y = x[0]

        self.assertEqual(y.indices, [0])

        # Test that indexed factors function properly
        self.assertEqual(y(state=np.array([4, 5, 6, 7])), 4)

        #USING [] syntax
        #Test indexing using slice without step

        #Test indexing using slice with step

        #Test indexing where slice start is greater than slice end

        #Test indexing where slice start, end, or step is negative

        #Test indexing where slice start equals slice end

        #Test indexing where slice start equals slice end with larger step

        #Test slicing factors of factors of factors

        #Test with int, negative int, and int out of bounds

        #Test using non-slice, int data structure

        #USING get_factor_from_indexer
        #Test using int, out of range int (check when indexing at length of factor), and negative int

        #Test using list regular

        #Test using list with repeated indices

        #Test using list with indices greater than factor indices but smaller than state space

        #Test using list with index less than 0

        #Test using malformed tuple (more than 2 indices)

        #Test using tuple with negative start, end, greater start than end, or out of bounds start, end

        #Test using regular tuple

        #Test with neither int, tuple, list


    def test_domain_resolver(self):

        x = Factor([2, 3], name='x')
        y = x[0].nameit('y')
        z = y[0].nameit('z')
        print(x.name)
        print(y.name)   # We want this to be y

        # Predict y from x
        self.assertEqual(y(state=np.array([4, 5, 6, 7])), y(x=[6, 7]))
        self.assertEqual(y(state=np.array([4, 5, 6, 7])), y(x=np.array([6, 7])))

        # Predict z from y
        self.assertEqual(z(state=np.array([4, 5, 6, 7])), z(y=[6], x=[6, 7]))


    def test_feature(self):

        a = Feature(function = lambda state: state[0]* 3, name='a')
        b = 2*a
        b.nameit('b')
        c = a*b
        c.nameit('c')
        d = 2*b
        d.nameit('d')

        self.assertEqual(a(state=np.array([4, 5, 6, 7])), 12)
        self.assertEqual(b(state=np.array([4, 5, 6, 7])), 24)
        self.assertEqual(b(state=np.array([4, 5, 6, 7])), 2*a(state=np.array([4, 5, 6, 7])))
        self.assertEqual(b(state=np.array([4, 5, 6, 7])), b(a=12))
        self.assertEqual(c(state=np.array([4, 5, 6, 7])), 288)
        self.assertEqual(c(state=np.array([4, 5, 6, 7])), c(a=12, b=24))
        self.assertEqual(c(state=np.array([4, 5, 6, 7])), c(a=12))
        self.assertEqual(d(state=np.array([4, 5, 6, 7])), 48)
        self.assertEqual(d(state=np.array([4, 5, 6, 7])), d(a=12))
        
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
