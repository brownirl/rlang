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


class State:
    pass


class VectorState(State, Primitive):
    """Represents a VectorState object.

    Args:
        input_array: a numpy array or list representing a state or set of states.

    Examples:
        .. code-block:: python

            s1 = VectorState(3)
            >> VectorState([3])
            s2 = VectorState([3, 4])
            >> VectorState([3, 4])
    """
    pass


class Action(Primitive):
    pass


class MDPObject:
    attr_list = ['name']

    def __init__(self, name: str):
        self.name = name

    def __eq__(self, other):
        # TODO implement this by checking the value of each attribute! Iterate through and compare. Verify that no attribute is a GroundingFunction!
        # We assume that the attributes for this and other MDPObjects are already calculated for us!
        # Iterate through, but don't check name? Maybe check name? I don't know.
        if isinstance(other, MDPObject):
            return self.__hash__() == other.__hash__()
        else:
            return False

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f"<MDPObject[{type(self)}] {self.__dict__}>"


class ObjectOrientedState(State):
    def __init__(self, objects: set):
        self.objects = objects

    def __eq__(self, other):
        if isinstance(other, ObjectOrientedState):
            # TODO: Need to compare all objects and their attributes
            pass
        else:
            return False

    def __getitem__(self, item):
        for obj in self.objects:
            if obj.name == item:
                return obj
        return None

    def __getattr__(self, item):
        if item == 'objects':
            return self.objects
        else:
            return self.__getitem__(item)

    # TODO: Adding or multiplying this kind of state does not make sense. Need to figure this out in the listener.
