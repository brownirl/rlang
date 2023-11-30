import unittest
import numpy as np
from context import rlang
from rlang.grounding import StateResolver, Factor, Feature

class FeatureTest(unittest.TestCase): 

    def test_instantiation(self):
        """Test that features can be instantiated with different types of indices, and verifies that they work on example states"""
        feature_ind0 = Feature(lambda state: state[0], "feature_ind0")
        feature_ind1_mul3 = Feature(lambda state: state[1]*3, "feature_ind1_mul3")
        feature_mul_feature = feature_ind0*feature_ind1_mul3
        feature_mul_const = feature_ind0*3
        feature_mul_feature.nameit("feature_mul_feature")
        self.assertEqual(feature_ind0(state=np.array([-2,5,1,0,3,7])), -2)
        self.assertEqual(feature_ind1_mul3(state=np.array([-2,5,1,0,3,7])), 15)
        self.assertEqual(feature_mul_feature(state=np.array([-2,5,1,0,3,7])), -30)
        self.assertEqual(feature_mul_const(state=np.array([-2,5,1,0,3,7])), -6)
        self.assertEqual(feature_mul_const(state=np.array([-2,5,1,0,3,7])), 3*feature_ind0(state=np.array([-2,5,1,0,3,7])))
        self.assertEqual(feature_mul_const(state=np.array([-2,5,1,0,3,7])), feature_mul_const(feature_ind0=-2))

        # Test that feature can be instantiated base a factor and a feature
        feature_ind1 = Feature(lambda state: state[1]*4, "feature_ind1")
        factor_ind2 = Factor(2, "factor_2to4")
        feature_mul_factor = feature_ind1*factor_ind2(state=np.array([1,2,3,4,5,6]))
        feature_mul_factor.nameit("feature_mul_factor")
        feature_mul_factor2 = Feature(lambda state: feature_ind1(state=state)*factor_ind2, "feature_mul_factor2")
        self.assertEqual(feature_mul_factor(state=np.array([1,2,3,4,5,6])), feature_mul_factor2(state=np.array([1,2,3,4,5,6])))
        self.assertEqual(feature_mul_factor(state=np.array([1,2,3,4,5,6])), 24)
        
        # Test different operations on feature instantiation (addition, multiplication, etc.)
        state = np.array([2,3,1,0,-4,5])
        feature_ind0 = Feature(lambda state: state[0]*3, "feature_ind0")
        feature_ind1 = Feature(lambda state: state[1]+5, "feature_ind1")
        feature_sum = feature_ind0+feature_ind1
        feature_sum.nameit("feature_sum")
        self.assertEqual(feature_sum(state=state), 14)

        feature_mul = feature_ind0*feature_ind1
        self.assertEqual(feature_mul(state=state), 48)

        feature_sub = feature_ind1-feature_ind0
        self.assertEqual(feature_sub(state=state), 2)

        feature_div = feature_ind1/feature_ind0
        self.assertEqual(feature_div(state=state), 4/3)

        # Test that feature instantiation generates name if name is not provided
        feature_ind3 = Feature(lambda state: state[3])
        self.assertEqual(feature_ind3.name[:8], "feature_")
        self.assertTrue(len(feature_ind3.name[8:]) > 0)

    def test_numpy_operations(self):
        """Test that numpy operations work on features"""
        state = np.array([2,4,1,-2,4,4,1])
        feature_dot_product = Feature(lambda state: np.dot(state[0], state[2]), "dot_product_feature")
        self.assertEqual(feature_dot_product(state=state), 2)

        new_state = np.array([1,2,3,4,5,6,7])
        feature_dot_state = Feature(lambda state: np.dot(state, new_state), "feature_dot_state")
        self.assertEqual(feature_dot_state(state=state), 56)

        feature_mean = Feature(lambda state: np.mean(state), "feature_mean")
        self.assertEqual(feature_mean(state=state), 2)

        feature_max = Feature(lambda state: np.max(state), "feature_max")
        self.assertEqual(feature_max(state=state), 4)

        feature_min = Feature(lambda state: np.min(state), "feature_min")
        self.assertEqual(feature_min(state=state), -2)

        feature_sum = Feature(lambda state: np.sum(state), "feature_sum")
        self.assertEqual(feature_sum(state=state), 14)

        feature_exp = Feature(lambda state: np.exp(state[2]), "feature_exp")
        self.assertEqual(feature_exp(state=state), np.exp(1))

        feature_median = Feature(lambda state: np.median(state), "feature_median")
        self.assertEqual(feature_median(state=state), 2)

        two_dimen_state = np.array([[3,4,5], [6,7,8]])
        feature_transpose = Feature(lambda state: np.transpose(state))
        self.assertEqual(feature_transpose(state=two_dimen_state).shape[0], 3)
        self.assertEqual(feature_transpose(state=two_dimen_state).shape[1], 2)

        feature_sqrt = Feature(lambda state: np.sqrt(state[1]), "feature_sqrt")
        self.assertEqual(feature_sqrt(state=state), 2)

        state_mul1 = np.array([[2,2],[3,3]])
        state_mul2 = np.array([[1,1],[3,2]])
        feature_matmul = Feature(lambda state: np.matmul(state,state_mul2), "feature_matmul")
        self.assertTrue(np.array_equal(feature_matmul(state=state_mul1), np.array([[8,6], [12,9]])))

    def test_arithmetic(self):
        """Test that arithmetic operations work on features"""
        s1 = [2,3]
        position_factor = Factor([0, 1], "position")
        x_feature = Feature(lambda state: position_factor[0], "x")
        y_feature = Feature(lambda state: position_factor[1], "y")
        x_y_sum = x_feature + y_feature
        x_y_prod = x_feature * y_feature
        x_y_div = x_feature / y_feature
        x_y_diff = x_feature - y_feature
        self.assertEqual(x_y_sum(state=s1), 5)
        self.assertEqual(x_y_prod(state=s1), 6)
        self.assertEqual(x_y_div(state=s1), 2/3)
        self.assertEqual(x_y_diff(state=s1), -1)
        
    def test_equality(self):
        """Test that features can be compared to other features using == and !="""
        feature_ind0 = Feature(lambda state: state[0], "feature_ind0")
        feature_ind4 = Feature(lambda state: state[4], "feature_ind4")
        self.assertTrue(feature_ind0 == feature_ind4)

        feature_ind2 = Feature(lambda state: state[2], "feature_ind2")
        feature_ind3 = Feature(lambda state: state[3], "feature_ind3")
        feature_2mul3 = feature_ind2*feature_ind3
        feature_of_state = Feature(lambda state: state[2]+state[3], "feature_of_state")
        self.assertTrue(feature_2mul3 == feature_of_state)

        feature_factor = Feature(lambda state: Factor(0, "factor_ind0"), "feature_factor")
        feature_ind0 = Feature(lambda state: state[0], "feature_ind0")
        self.assertTrue(feature_factor == feature_ind0)

        feature_ind4 = Feature(lambda state: state[4], "feature_ind4")
        feature_ind5 = Feature(lambda state: state[5], "feature_ind5")
        self.assertTrue(feature_ind4 != feature_ind5)

    if __name__ == '__main__':
        unittest.main()
