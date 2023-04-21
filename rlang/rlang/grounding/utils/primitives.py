import numpy as np
from typing import Any

from .grounding_exceptions import RLangGroundingError


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
            # TODO: investigate deprecation cause - include version
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
    """Represents a state that is a vector.

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
    """Represents an action that is a vector.

    Args:
        input_array: a numpy array or list representing an action or set of actions.

    Examples:
        .. code-block:: python

            s1 = Action(3)
            >> Action([3])
            s2 = Action([3, 4])
            >> Action([3, 4])
    """
    pass


class MDPObject:
    """Represents an object in an Object-Oriented MDP.

    Inherit this class to create a new object class.
    """
    attr_list = ['name']

    def __init__(self, name: str):
        """

        Args:
            name: the name for this object class.
        """
        self.name = name

    def __eq__(self, other):
        if type(self) == type(other):
            if self.attr_list != other.attr_list:
                return False
            for k in self.attr_list:
                if k == 'name':  # Ignoring name
                    continue
                if getattr(self, k) != getattr(other, k):
                    return False
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.__repr__())

    def __repr__(self):
        subclass_str = f"[{type(self).__name__}]" if type(self).__name__ is not "MDPObject" else ""
        return f"<MDPObject{subclass_str} {self.__dict__}>"


class ObjectOrientedState(State):
    """Represents a state for an object-oriented MDP.

    Examples:
        .. code-block:: python

            color = MDPObject(name="color")
            color.red = 256
            oo_state = ObjectOrientedState(objects={color})
            >> <ObjectOrientedState {<MDPObject {'name': 'color', 'red': 256}>}>
    """
    def __init__(self, objects: set):
        """

        Args:
            objects: a set of objects, which should be instances of subclasses of MDPObject.
        """
        self.objects = objects

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()
        # if isinstance(other, ObjectOrientedState):
        #     # TODO: Need to compare all objects and their attributes
        #     pass
        # else:
        #     return False

    def __getitem__(self, item):
        for obj in self.objects:
            if obj.name == item:
                return obj
        raise AttributeError(f"State does not contain attribute {item}")

    def __getattr__(self, item):
        if item == 'objects':
            return self.objects
        else:
            return self.__getitem__(item)

    def __repr__(self):
        return f"<ObjectOrientedState {str(self.objects)}>"

    def __mul__(self, other):
        raise RLangGroundingError("An ObjectOrientedState cannot be used arithmetically")

    def __add__(self, other):
        raise RLangGroundingError("An ObjectOrientedState cannot be used arithmetically")

    def __sub__(self, other):
        raise RLangGroundingError("An ObjectOrientedState cannot be used arithmetically")

    def __hash__(self):
        return hash(self.__repr__())

