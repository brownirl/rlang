import numpy as np
import itertools


class FourierBasis:
    def __init__(self, n_dims, ranges, order=3):
        self.ranges = np.array(ranges)
        self.n_terms = (order + 1) ** n_dims
        self._features_c = list(map(lambda x: np.array(x), itertools.product(range(order + 1), repeat=n_dims)))
        self._features_c = np.array(self._features_c)  # turn to matrix with rows being the c coefficients
        self._scale = np.linalg.norm(self._features_c, ord=2, axis=-1)
        self._scale[0] = 1
        self.NAME = "Fourier-" + str(order)

    def __call__(self, states):
        coeffs = np.einsum('ij, ...j->...i', self._features_c, states / self.ranges)
        return np.cos(np.pi * coeffs) / self._scale

    def num_features(self):
        return self._features_c.shape[0]

    def get_features(self, inputs):
        return self.__call__(inputs)


if __name__ == '__main__':
    f = FourierBasis(2, [1, 1])
    s = np.random.rand(3, 4, 2)
    fs = f(s)
    print(fs.shape)
    print(fs)
    print(f.num_features())
