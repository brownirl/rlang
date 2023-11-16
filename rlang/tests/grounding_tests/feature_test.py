import unittest
import numpy as np
from context import rlang
from rlang.grounding import StateResolver, Factor, Feature

class FeatureTest(unittest.TestCase): 

    def test_instantiation(self):
        #state1 = State(np.array([2, 3]))
       # state1 = [2,3]
       # pos = Factor([0, 1], "position")
       # x = Feature(pos[0], "feature")
       # y = Factor(1, "y")
       # self.assertEqual(x(state=state1), [2])
        state1 = np.array([2, 3])
        pos = Factor([0, 1], "position")
        x = Feature(pos[0], 1)
        y = Factor(1, "y")
        self.assertEqual(x(state=state1), 2)

       # test = Feature(lambda s: x(state=s) + 1, "test")
       # test2 = Feature(lambda s: x(state=s) + y(state=s), "test2")
       # self.assertEqual(test(state1), [3])
       # self.assertEqual(test2(state1), [5])


       # #Test that feature can be instantiated based on other features
        feature = Feature(lambda state: state[0], "feature")
        feature2 = Feature(lambda state: state[1]*3, "feature2")
        feature3 = feature*feature2
        feature4 = feature*3
        feature3.nameit("feature3")
        self.assertEqual(feature(state=np.array([-2,5,1,0,3,7])), -2)
        self.assertEqual(feature2(state=np.array([-2,5,1,0,3,7])), 15)
        self.assertEqual(feature3(state=np.array([-2,5,1,0,3,7])), -30)
        self.assertEqual(feature4(state=np.array([-2,5,1,0,3,7])), -6)
        self.assertEqual(feature4(state=np.array([-2,5,1,0,3,7])), 3*feature(state=np.array([-2,5,1,0,3,7])))
        self.assertEqual(feature4(state=np.array([-2,5,1,0,3,7])), feature4(feature=-2))


        #Test that feature can be instantiated base a factor and a feature
        feature = Feature(lambda state: state[1]*4, "feature")
        factor = Factor((2,4), "factor")
        feature2 = feature*factor(state=np.array([1,2,3,4,5,6]))
        feature3 = Feature(lambda state: feature(state=state)*factor, "feature3")
        feature2.nameit("feature2")
        #self.assertEqual(feature2(state=np.array([1,2,3,4,5,6])), 16)
        
        #Test different operations on feature instantiation (addition, multiplication, etc.)
        state = np.array([2,3,1,0,-4,5])
        feature = Feature(lambda state: state[0]*3, "feature")
        feature2 = Feature(lambda state: state[1]+5, "feature2")
        feature3 = feature+feature2
        feature3.nameit("feature3")
        self.assertEqual(feature3(state=state), 14)

        feature3 = feature*feature2
        self.assertEqual(feature3(state=state), 48)

        feature3 = feature2-feature
        self.assertEqual(feature3(state=state), 2)

        feature3 = feature2/feature
        self.assertEqual(feature3(state=state), 4/3)

        #Test that feature instantiation generates name if name is not provided
        feature = Feature(lambda state: state[3])
        self.assertEqual(feature.name[:8], "feature_")
        self.assertTrue(len(feature.name[8:]) > 0)

# All python operations should have their own testing function
    def test_numpy_operations(self):
        state = np.array([2,4,1,-2,4,4,1])
        feature = Feature(lambda state: np.dot(state[0], state[2]), "feature")
        self.assertEqual(feature(state=state), 2)

        new_state = np.array([1,2,3,4,5,6,7])
        feature = Feature(lambda state: np.dot(state, new_state), "feature")
        self.assertEqual(feature(state=state), 56)

        feature = Feature(lambda state: np.mean(state), "feature")
        self.assertEqual(feature(state=state), 2)

        feature = Feature(lambda state: np.max(state), "feature")
        self.assertEqual(feature(state=state), 4)

        feature = Feature(lambda state: np.min(state), "feature")
        self.assertEqual(feature(state=state), -2)

        feature = Feature(lambda state: np.sum(state), "feature")
        self.assertEqual(feature(state=state), 14)

        feature = Feature(lambda state: np.exp(state[2]), "feature")
        self.assertEqual(feature(state=state), np.exp(1))

        feature = Feature(lambda state: np.median(state))
        self.assertEqual(feature(state=state), 2)

        two_dimen_state = np.array([[3,4,5], [6,7,8]])
        feature = Feature(lambda state: np.transpose(state))
        self.assertEqual(feature(state=two_dimen_state).shape[0], 3)
        self.assertEqual(feature(state=two_dimen_state).shape[1], 2)

        feature = Feature(lambda state: np.sqrt(state[1]))
        self.assertEqual(feature(state=state), 2)

        state_mul1 = np.array([[2,2],[3,3]])
        state_mul2 = np.array([[1,1],[3,2]])
        feature = Feature(lambda state: np.matmul(state,state_mul2), "feature")
        self.assertTrue(np.array_equal(feature(state=state_mul1), np.array([[8,6], [12,9]])))





    def test_arithmetic(self):
        s1 = [2,3]
        pos = Factor([0, 1], "position")
        x = Feature(lambda state: pos[0], "x")
        y = Feature(lambda state: pos[1], "y")
        x_y_sum = x + y
        x_y_prod = x * y
        x_y_div = x / y
        x_y_diff = x - y
        self.assertEqual(x_y_sum(state=s1), 5)
        self.assertEqual(x_y_prod(state=s1), 6)
        self.assertEqual(x_y_div(state=s1), 2/3)
        self.assertEqual(x_y_diff(state=s1), -1)
    
    #def test_equality(self):
    #    #state1 = State(np.array([2, 3]))
    #    state1 = [2,3]
    #    pos = Factor([0, 1], "position")
    #    x = Feature(pos[0], "x")
    #    y = Factor(1, "y")
    #    self.assertEqual(x(state=state1), [2])

    #    test1 = Feature((lambda s: x(state=s) + 3), 1)
    #    test2 = Feature((lambda s: x(state=s) + y(state=s)), 1)

    #    self.assertEqual(test1(state1), test2(state1))

if __name__ == '__main__':
    unittest.main()
