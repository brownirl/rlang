import unittest
from grounding.internals import BatchedPrimitive
import numpy as np

class BatchedPrimitiveTest(unittest.TestCase):

    def test_new(self):
        arr1 = np.array([[1, 2, 3], [4, 5, 6]])
        bp = BatchedPrimitive(arr1)
        self.assertEqual(bp.primitive_size, 3)
        arr2 = np.ndarray((4, 5))
        bp2 = BatchedPrimitive(arr2)
        self.assertEqual(bp2.primitive_size, 5)

    
    def test_getitem(self):
        arr1 = np.array([[1, 2, 3], [4, 5, 6]])
        bp = BatchedPrimitive(arr1)
        self.assertEqual(bp[0], [[1, 4]])
        self.assertEqual(bp[-1], [[3, 6]])
        self.assertEqual(bp[1:2].shape, (2, 1))
        self.assertTrue((bp[:] == arr1).all())
        self.assertTrue((bp[1:2] == np.array([[2],[5]])).all())

        arr2 = np.ndarray((4, 5))
        bp2 = BatchedPrimitive(arr2)
        self.assertEqual(bp2[0].shape, (1, 4))
        self.assertEqual(bp2[:2].shape, (4, 2))
        self.assertEqual(bp2[::-1].shape, bp2.shape)

        arr1d = np.array([1, 2, 3])
        bp1d = BatchedPrimitive(arr1d)
        self.assertEqual(bp1d[0], arr1d[0])
        self.assertEqual(bp1d[-1], arr1d[-1])
        self.assertTrue((bp1d[:] == arr1d))
        self.assertTrue((bp1d[::-1] == arr1d[::-1]))

    def test_eq(self):

        #TODO: Add more multidimensional arrays
        arr1 = np.array([[1, 2, 3], [4, 5, 6]])
        bp = BatchedPrimitive(arr1)
        self.assertTrue(((bp == arr1) == [[True],[True]]).all())
        self.assertTrue(((arr1 == bp) == [[True],[True]]).all())
        self.assertEqual((bp == arr1).shape, (2, 1))
        arr2 = np.array([[1, 2, 3], [4, 6, 6]])
        self.assertTrue(((bp == arr2) == [[True],[False]]).all())

        arr1d = np.array([1, 2, 3])
        bp1d = BatchedPrimitive(arr1d)
        self.assertEqual((bp1d == arr1d), [True])
        self.assertEqual((arr1d == bp1d), [True])
        arr1d2 = np.array([1, 2, 3, 4])
        self.assertEqual((bp1d == arr1d2), [False])

        self.assertTrue(((bp1d == bp) == [[True], [False]]).all())
        self.assertTrue(((bp == bp1d) == [[True], [False]]).all())

        # bp3 = BatchedPrimitive([[1, 0], [0, 0]])
        # bp4 = BatchedPrimitive(0)
        # # print(BatchedPrimitive([[1, 0], [0, 0]]) == BatchedPrimitive(0))
        # print(bp4 == bp3)
        # self.assertFalse((BatchedPrimitive([[1, 0], [0, 0]]) == BatchedPrimitive(0)).all())
        # self.assertFalse(BatchedPrimitive(0) == (BatchedPrimitive([[1, 0], [0, 0]])).all())
    
    def test_unbatched_eq(self):
        arr1 = np.array([[1, 2, 3], [4, 5, 6]])
        arr2 = np.array([[1, 2, 3], [4, 6, 6]])
        bp = BatchedPrimitive(arr1)
        bp1 = BatchedPrimitive(arr2)
        self.assertTrue(bp.unbatched_eq(bp))
        self.assertFalse(bp.unbatched_eq(bp1))

        arr1d = np.array([1, 2, 3])
        bp1d = BatchedPrimitive(arr1d)
        self.assertTrue(bp1d.unbatched_eq(bp1d))
        arr1d2 = np.array([1, 2, 3, 4])
        bp2d = BatchedPrimitive(arr1d2)
        self.assertFalse(bp1d.unbatched_eq(arr1d2))
        self.assertFalse(bp2d.unbatched_eq(arr1d2))

        self.assertFalse(bp1.unbatched_eq(bp1d))
        # QUESTION: why is bp2d.unbatched_eq(bp1d) NotImplemented?
        print(bp2d.unbatched_eq(bp1d))
        # self.assertFalse(bp2d.unbatched_eq(bp1d))

        # QUESTION: deprecation warning
        print(bp1.unbatched_eq(bp1d))
        self.assertFalse(bp1.unbatched_eq(bp1d))

        arr3 = np.array([[1, 2], [3, 4], [5, 6]])
        #TODO: test on arrays of different sizes



    def test_ne(self):
        arr1 = np.array([[1, 2, 3], [4, 5, 6]])
        arr2 = np.array([[1, 2, 3], [4, 6, 6]])
        bp = BatchedPrimitive(arr1)
        bp1 = BatchedPrimitive(arr2)
        self.assertTrue(((bp != arr1) == [[False],[False]]).all())
        self.assertEqual((bp != arr1).shape, (2, 1))
        arr2 = np.array([[1, 2, 3], [4, 6, 6]])
        self.assertTrue(((bp != arr2) == [[False],[True]]).all())
        self.assertTrue(((bp != bp1) == [[False],[True]]).all())

        arr1d = np.array([1, 2, 3])
        bp1d = BatchedPrimitive(arr1d)
        self.assertEqual((bp1d != arr1d), [False])
        self.assertEqual((arr1d != bp1d), [False])
        arr1d2 = np.array([1, 2, 3, 4])
        self.assertEqual((bp1d != arr1d2), [True])

        self.assertTrue(((bp1d != bp) == [[False], [True]]).all())
        self.assertTrue(((bp != bp1d) == [[False], [True]]).all())

        

if __name__ == '__main__':
    unittest.main()