from __future__ import annotations
from typing import Callable, Any, Union
import numpy as np
from rlang.src.grounding.base import Domain, Grounding, GroundingFunction
from rlang.src.grounding.internals import State
from rlang.src.exceptions import RLangGroundingError
# from rlang.src.grounding.utils.domain import Domain
# from rlang.src.grounding.utils.state_action_implementation import State
# from rlang.src.grounding.utils.grounding_errors import RLangGroundingError


class StateGroundingFunction(GroundingFunction):
    """
        StateGroundingFunction class
            - Represents a GroundingFunction which is a function of State
        author: Benjamin Spiegel (bspiegel@cs.brown.edu), Jennifer Wang
        date: August 2021
    """
    def __init__(self, codomain: Domain, function: Callable, name: str = None):
        self._function = function
        super().__init__(domain=Domain.STATE, codomain=codomain, function=function, name=name)

    def __eq__(self, other):
        if isinstance(other, (StateGroundingFunction, Callable)):
            return Predicate(function=lambda *args, **kwargs: self(*args, **kwargs) == other(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Predicate(function=lambda *args, **kwargs: self(*args, **kwargs) == other)
        raise RLangGroundingError(message=f"Cannot '==' a {type(self)} and a {type(other)}")

    def __ne__(self, other):
        if isinstance(other, (StateGroundingFunction, Callable)):
            return Predicate(function=lambda *args, **kwargs: self(*args, **kwargs) != other(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Predicate(function=lambda *args, **kwargs: self(*args, **kwargs) != other)
        raise RLangGroundingError(message=f"Cannot '!=' a {type(self)} and a {type(other)}")

    def __mul__(self, other):
        if isinstance(other, (StateGroundingFunction, Callable)):
            return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) * other(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) * other)
        raise RLangGroundingError(message=f"Cannot '*' a {type(self)} and a {type(other)}")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, (StateGroundingFunction, Callable)):
            return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) / other(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) / other)
        raise RLangGroundingError(message=f"Cannot '/' a {type(self)} and a {type(other)}")

    def __rtruediv__(self, other):
        if isinstance(other, Callable):
            return Feature(function=lambda *args, **kwargs: other(*args, **kwargs) / self(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Feature(function=lambda *args, **kwargs: other / self(*args, **kwargs))
        raise RLangGroundingError(message=f"Cannot '/' a {type(other)} and a {type(self)}")

    def __sub__(self, other):
        if isinstance(other, (StateGroundingFunction, Callable)):
            return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) - other(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) - other)
        raise RLangGroundingError(message=f"Cannot '-' a {type(self)} and a {type(other)}")

    def __rsub__(self, other):
        if isinstance(other, (np.ndarray, int, float)):
            return Feature(function=lambda *args, **kwargs: other - self(*args, **kwargs))
        raise RLangGroundingError(message=f"Cannot '-' a {type(other)} and a {type(self)}")

    def __add__(self, other):
        if isinstance(other, (StateGroundingFunction, Callable)):
            return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) + other(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) + other)
        raise RLangGroundingError(message=f"Cannot '+' a {type(self)} and a {type(other)}")

    def __radd__(self, other):
        self.__add__(other)


# Leaving this at the bottom of the file for circular import issue. Don't move it.
# from rlang.src.grounding.groundings.state.predicate import Predicate
# from rlang.src.grounding.groundings.state.feature import Feature

class Factor(StateGroundingFunction):
    """
        Factor grounding class
            - Represents a factor of state
        author: Benjamin Spiegel (bspiegel@cs.brown.edu), Jennifer Wang
        date: August 2021
    """
    def __init__(self, state_indexer: Any, name: str = None, state_arg: str = 'state'):
        if type(state_indexer) == int:
            state_indexer = [state_indexer]
        self._state_indexer = state_indexer
        super().__init__(function=lambda *args, **kwargs: kwargs[state_arg].__getitem__(self._state_indexer),
                         codomain=Domain.REAL_VALUE, name=name)

    def __getitem__(self, item):
        if isinstance(self._state_indexer, slice):
            print("This is weird")
        if isinstance(item, list):
            return Factor([self._state_indexer[i] for i in item])
        return Factor(self._state_indexer[item])

    def __repr__(self):
        return f"<Factor: {str(self._state_indexer)}>"


class Feature(StateGroundingFunction):
    """
        Feature grounding class
            - Represents a feature
        author: Benjamin Spiegel (bspiegel@cs.brown.edu), Jennifer Wang
        date: August 2021
    """
    def __init__(self, function: Callable, name: str = None):
        super().__init__(function=function, codomain=Domain.REAL_VALUE, name=name)

    @classmethod
    def from_Factor(cls, factor: 'Factor', name: str = None):
        return cls(function=factor.__call__, name=name)


class Predicate(StateGroundingFunction):
    """
        Predicate grounding class
            - Represents a factor of state
        author: Benjamin Spiegel (bspiegel@cs.brown.edu), Jennifer Wang
        date: August 2021
    """
    def __init__(self, function: Callable, name: str = None):
        super().__init__(function=function, codomain=Domain.BOOLEAN, name=name)

    def __and__(self, other) -> Predicate:
        if isinstance(other, (Predicate, Callable)):
            return Predicate(function=lambda *args, **kwargs:
                             self(*args, **kwargs) & other(*args, **kwargs))
        if isinstance(other, bool):
            return self if other else Predicate(function=lambda *args, **kwargs: False)
        raise RLangGroundingError(message=f"Cannot & a Predicate with a {type(other)}")

    def __rand__(self, other):
        self.__and__(other)

    def __or__(self, other) -> Predicate:
        if isinstance(other, (Predicate, Callable)):
            return Predicate(function=lambda *args, **kwargs:
                             self(*args, **kwargs) | other(*args, **kwargs))
        if isinstance(other, bool):
            return self if not other else Predicate(function=lambda *args, **kwargs: True)
        raise RLangGroundingError(message=f"Cannot | a Predicate with a {type(other)}")

    def __invert__(self) -> Predicate:
        return Predicate(function=lambda *args, **kwargs: bool(~ self(*args, **kwargs)))

    def __repr__(self):
        return "<Predicate>"


class Policy(StateGroundingFunction):
    def __init__(self, function: Callable, name: str = None):
        super().__init__(function=function, codomain=Domain.ACTION, name=name)


class Option(Grounding):
    """Grounding object for an option.

    Args:
        initiation: A Predicate capturing the initiation set of the option
        policy: A Policy capturing the policy of the option
        termination: A Predicate capturing the termination set of the option
        name (optional): A name for the Option grounding
    """

    def __init__(self, initiation: Predicate, policy: Policy, termination: Predicate, name: str = None):
        self._initiation = initiation
        self._policy = policy
        self._termination = termination
        super().__init__(name)

    def __call__(self, *args, **kwargs) -> Union[None, State]:
        if self._termination(*args, **kwargs):
            return None
        else:
            return self._policy(*args, **kwargs)

    def can_execute(self, *args, **kwargs) -> bool:
        """Determines whether the option can be executed in a given state.

        Args:
            state: A State object

        Returns:
            bool
        """
        return self._initiation(*args, **kwargs)
