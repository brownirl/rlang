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

    def test_eq(self):

        #TODO: Add more multidimensional arrays + 1d array
        arr1 = np.array([[1, 2, 3], [4, 5, 6]])
        bp = BatchedPrimitive(arr1)
        self.assertTrue(((bp == arr1) == [[True],[True]]).all())
        self.assertTrue(((arr1 == bp) == [[True],[True]]).all())
        self.assertEqual((bp == arr1).shape, (2, 1))
        arr2 = np.array([[1, 2, 3], [4, 6, 6]])
        self.assertTrue(((bp == arr2) == [[True],[False]]).all())

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

        

if __name__ == '__main__':
    unittest.main()