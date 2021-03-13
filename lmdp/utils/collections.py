import numpy as np

class defaultdict(dict):
    '''
        Custom defaultdict class that allows to have default values
        be a function of the key.
    '''
    def __init__(self, dict_factory):
        self._dict_factory = dict_factory
    def __missing__(self, key):
        v = self._dict_factory(key)
        self[key] = v
        return v


class Index:
    def __init__(self, iterator=None):
        self.idx_to_obj = {}
        self.obj_to_idx = {}
        self.curr_idx = 0
        if iterator:
            for obj in iterator:
                self.__call__(obj)

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.idx_to_obj[key]
        else:
            return self.obj_to_idx[key]

    def __call__(self, obj):
        self.obj_to_idx[obj] = self.curr_idx
        self.idx_to_obj[self.curr_idx] = obj
        self.curr_idx += 1

    def __contains__(self, key):
        if isinstance(key, int):
            return key in self.idx_to_obj
        else:
            return key in self.obj_to_idx
    
    def __len__(self):
        return len(self.objects())
    
    def objects(self):
        return self.obj_to_idx.keys()
        
    def elems(self):
        return self.obj_to_idx.items()


class arraydict:
    def __init__(self, *dims, iterators=None, default_value=0, data=None, index=None, dtype=np.float):
        self.data = np.zeros(dims) + default_value if data is None else data
        if not index: # index per dimension
            if not iterators:
                self.index = [Index()] * len(dims) 
            else:
                self.index = [Index(i) for i in iterators]
                self.index = self.index + [Index() for _ in range(len(dims)-len(self.index))]
        else:
            self.index = index
    def __len__(self):
        return len(self.data.shape)

    def __get_indices(self, keys):
        if not isinstance(keys, tuple):
            keys = (keys,)
        idx_k = []
        for i, k in enumerate(keys):
            if k not in self.index[i]:
                raise ValueError("Unknown key")
            idx_k.append((self.index[i][k],))
        return keys, tuple(idx_k)

    def __getitem__(self, keys):
        keys, idx_k = self.__get_indices(keys)
        # if all dimensions given then return value
        if len(keys) == len(self):
            return self.data[idx_k]
        else: # if not return slice as arraydict
            d = self.data
            for i in idx_k:
                d = d[i]
            return arraydict(*self.data.shape[len(keys):], data=d, index=self.index[len(keys):])

    def __setitem__(self, keys, value):
        keys, idx_k = self.__get_indices(keys)
        if len(keys) == len(self):
            self.data[idx_k] = value
    
    def __str__(self):
        return str(self.data)
    def numpy(self):
        return self.data


if __name__=="__main__":
    from simple_rl.tasks.grid_world.GridWorldStateClass import GridWorldState

    def gridworld_state_space(width, height): # state space iterator
        for x in range(1,width+1):
            for y in range(1, height+1):
                yield GridWorldState(x, y)

    
    actions = ("up", "down", "left", "right")

    Q = arraydict(4, 4, iterators=[gridworld_state_space(2,2), actions])
    s = GridWorldState(1,1)
    a = "up"
    Q[s][a] = 1
    print(Q[s][a])
    print(Q)
    