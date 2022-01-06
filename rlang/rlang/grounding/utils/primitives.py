import numpy as np
from typing import Any


class Primitive(np.ndarray):
    """Represents a batched real-valued object.

    States and Actions should be easily batchable. This takes care of that.
    """

    def __new__(cls, input_array: Any):
        obj_arr = np.array(input_array, ndmin=1)
        obj = obj_arr.view(cls)
        return obj

    def as_tuple(self):
        s = self.view(np.ndarray)
        s_tuple = tuple(map(tuple, s))
        if s.shape[0] == 1:
            return s_tuple[0]
        else:
            return s_tuple

    def __getitem__(self, item):
        val = super().__getitem__(item)
        if isinstance(val, np.ndarray):
            return val.view(Primitive)
        else:
            return Primitive(val)

    def __eq__(self, other):
        return super().__eq__(other).all().view(Primitive)

    def unbatched_eq(self, other):
        if isinstance(other, Primitive):
            #TODO: investigate deprecation cause - include version
            return np.all(super().__eq__(other))
        else:
            return False

    def unwrap(self):
        return self.view(np.ndarray)

    def __hash__(self):
        return hash(str(self))

    def __ne__(self, other):
        return np.bitwise_not(self.__eq__(other))


class State(Primitive):
    """Represents a State object.

    Args:
        input_array: a numpy array or list representing a state or set of states.

    Examples:
        .. code-block:: python

            s1 = State(3)
            >> State([3])
            s2 = State([3, 4])
            >> State([3, 4])
    """
    pass


class Action(Primitive):
    pass
