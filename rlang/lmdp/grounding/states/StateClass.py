'''
    This wrapper creates a flexible factory for State Objects
    that can be initialized for the particular class of MDP

    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: v0 January 2021
          v1 March 2021
'''
import sys, os
sys.path.append(os.path.abspath("/"))
import numpy as np
from lmdp.utils.space import Vector, BatchedVector


class State(Vector):
    '''
        State Object for RLang/LMDP implementations
        States are real vectors of 1 dimension.
    '''
    def __init__(self, data, dim=None):
        '''
            data: single dimension array-like object
            dim: dimension of the state vector. 
        '''
        
        Vector.__init__(self, data, dim) 

    def features(self):
        return self
    
    def numpy(self):
        return self.data

    def __hash__(self):
        return hash(str(self.data))


class BatchedState(BatchedVector, State):
    def __init__(self, data):
        BatchedVector.__init__(self, data)
    
   
class StateSpace:
    def __init__(self, generator, state_factory):
        self.state_factory = state_factory
        self.generator = generator

    def __call__(self):
        return self.generator()
    
    def build(self, state): # TODO iterate over the batching dimensions.
        return self.state_factory(state)

def state_builder(state):
    if len(state.shape) > 1:
        return BatchedState(state)
    else:
        return State(state)

if __name__=="__main__":
    s = State([0,1,4])
    print(s)

    print(s[:-1])
    s[:2] = np.array([-1,-1])
    print(s)


    s = BatchedState(np.random.rand(*(3,2)))
    print(s)
    print(s[1])
    s[1] = 3
    print(s.numpy() + 1)

