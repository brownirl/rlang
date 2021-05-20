import numpy as np
import torch 
from collections import UserList

class DiscreteSpace:
    def __init__(self, domains, dim=None):
        if dim is not None:
            assert dim == 1 or (dim == len(domains) or len(domains) == 1)
        self.domains = domains
        self.dim = len(self.domains) if dim is None or dim == 1 else dim

    def __len__(self):
        return self.dim

    def generate(self):
        pass
    
    def __getitem__(self, *keys):
        pass


class Vector:
    '''
        Numpy based Vectorial representation
    '''
    def __init__(self, data, dim=None):
        '''
            data: single dimension array-like
            dim: dimension of the state vector. 
        '''
        
        self.data = data.squeeze() if isinstance(data, (np.ndarray, torch.Tensor)) else np.array(data).squeeze()
        assert len(self.data.shape) == 1 # number of dimensions
        self._dim = dim if dim is not None else len(self.data)

    def __len__(self):
        return 1
    def __getitem__(self, *args):
        return self.data.__getitem__(*args)
    def __setitem__(self, *args):
         self.data.__setitem__(*args)
    def __repr__(self):
        return self.data.__repr__()
    def dim(self):
        return self._dim

class BatchedVector(Vector):

    def __init__(self, data):
        self.data = data if isinstance(data, (np.ndarray, torch.Tensor)) else np.array(data)
        self._dim = self.data.shape[-1] # assume last dimension to be the state dimension and all other batch_dimensions

    def __len__(self):
        return len(self.data)

    @property
    def shape(self):
        return self.data.shape
    def __len__(self):
        return len(self.data)
    def __getitem__(self, idx):
        return BatchedVector(self.data[..., idx])
    def __setitem__(self, idx, value):
         self.data[..., idx] = value

    def __add__(self, other):
        return self.data.__add__(other)
    def __sub__(self, other):
        return self.data.__sub__(other)
    def __mul__(self, other):
        return self.data.__mul__(other)
    def __truediv__(self, other):
        return self.data.__truediv__(other)

    def __lt__(self, other):
        return self.data.__lt__(other)
    def __le__(self, other):
        return self.data.__le__(other)
    def __gt__(self, other):
        return self.data.__gt__(other)
    def __ge__(self, other):
        return self.data.__ge__(other)
    def __eq__(self, other):
        return (self.data == other).all(-1)
    def __ne__(self, other):
        return self.data != other

class BatchedTuple(tuple):

    def __init__(self, data=[], dim=None, dtype=str):
        self.data = tuple(data) # first dimension is batch dimension.
        self._dim = dim if dim is not None else len(self.data) # dimension of the data
        self._dtype = type(data[0]) if len(self.data) > 0 else dtype

    def __len__(self):
        return len(self.data)
    def __eq__(self, other):
        if(isinstance(other, (tuple, list)) and len(other) == len(self)): # elementwise comparison
            return tuple(map(lambda t: t[0] == t[1], zip(self.data, other)))
        else:
            return tuple(map(lambda x: x == other, self.data))

    def __getitem__(self, key):
        return self.data[key]

    def __repr__(self):
        return self.data.__repr__()

if __name__=="__main__":
    t = BatchedTuple(["up", "down", "left", "right"])
    print(t)
    print(t == 4)
    print(t == "up")
    print(t == ["up", "down", "g", "t"])
