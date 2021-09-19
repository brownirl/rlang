from __future__ import annotations
from typing import Callable, Any, Union

import numpy as np
from rlang.src.grounding.internals import Domain, State, Action
from rlang.src.exceptions import RLangGroundingError


class Grounding(object):
    """Parent class for all grounded objects."""
    def __init__(self, name=None):
        self._name = name

    @property
    def name(self):
        return self._name

    def __hash__(self):
        return self._name.__hash__()

    def __repr__(self):
        return self._name


class GroundingFunction(Grounding):
    """Parent class for groundings which are functions.

    GroundingFunctions have a specified domain and codomain.
    They are typically invoked with keyword arguments corresponding
    to their domain:

    .. code-block:: python

        door_closed(state=s)

    Args:
        domain: Domain of the function.
        codomain: Codomain of the function.
        function: the actual function.
        name (optional): the name of the Grounding.
    """
    def __init__(self, domain: Union[str, Domain], codomain: Union[str, Domain], function: Callable, name: str = None):
        if isinstance(domain, str):
            domain = Domain.from_name(domain)

        if isinstance(codomain, str):
            codomain = Domain.from_name(codomain)

        super().__init__(name)
        self.domain = domain
        self.codomain = codomain
        self._function = function

    def __call__(self, *args, **kwargs):
        if 'state' in kwargs.keys():
            if not isinstance(kwargs['state'], State):
                kwargs.update({'state': State(kwargs['state'])})
        if 'action' in kwargs.keys():
            if not isinstance(kwargs['action'], State):
                kwargs.update({'action': Action(kwargs['action'])})
        if 'next_state' in kwargs.keys():
            if not isinstance(kwargs['next_state'], State):
                kwargs.update({'next_state': State(kwargs['next_state'])})
        return self._function(*args, **kwargs)

    def __eq__(self, other):
        if isinstance(other, GroundingFunction):
            return Predicate(function=lambda *args, **kwargs: self(*args, **kwargs) == other(*args, **kwargs),
                             domain=self.domain + other.domain)
        if isinstance(other, Callable):
            # TODO: We must know the domain of Callable to properly track the domain
            return Predicate(function=lambda *args, **kwargs: self(*args, **kwargs) == other(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Predicate(function=lambda *args, **kwargs: self(*args, **kwargs) == other, domain=self.domain)
        raise RLangGroundingError(message=f"Cannot '==' a {type(self)} and a {type(other)}")

    def __ne__(self, other):
        if isinstance(other, GroundingFunction):
            return Predicate(function=lambda *args, **kwargs: self(*args, **kwargs) != other(*args, **kwargs),
                             domain=self.domain + other.domain)
        if isinstance(other, Callable):
            # TODO: We must know the domain of Callable to properly track the domain
            return Predicate(function=lambda *args, **kwargs: self(*args, **kwargs) != other(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Predicate(function=lambda *args, **kwargs: self(*args, **kwargs) != other, domain=self.domain)
        raise RLangGroundingError(message=f"Cannot '!=' a {type(self)} and a {type(other)}")

    def __mul__(self, other):
        if isinstance(other, GroundingFunction):
            new_domain = self.domain + other.domain
            if new_domain.value == Domain.ANY:
                return PrimitiveGrounding(codomain=Domain.REAL_VALUE, value=self()*other())
            else:
                return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) * other(*args, **kwargs),
                               domain=new_domain)
        if isinstance(other, Callable):
            # TODO: We must know the domain of Callable to properly track the domain
            return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) * other(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) * other, domain=self.domain)
        raise RLangGroundingError(message=f"Cannot '*' a {type(self)} and a {type(other)}")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, GroundingFunction):
            new_domain = self.domain + other.domain
            if new_domain.value == Domain.ANY:
                return PrimitiveGrounding(codomain=Domain.REAL_VALUE, value=self()/other())
            else:
                return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) / other(*args, **kwargs),
                               domain=new_domain)
        if isinstance(other, Callable):
            # TODO: We must know the domain of Callable to properly track the domain
            return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) / other(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) / other, domain=self.domain)
        raise RLangGroundingError(message=f"Cannot '/' a {type(self)} and a {type(other)}")

    def __rtruediv__(self, other):
        if isinstance(other, Callable):
            # TODO: We must know the domain of Callable to properly track the domain
            return Feature(function=lambda *args, **kwargs: other(*args, **kwargs) / self(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Feature(function=lambda *args, **kwargs: other / self(*args, **kwargs), domain=self.domain)
        raise RLangGroundingError(message=f"Cannot '/' a {type(other)} and a {type(self)}")

    def __sub__(self, other):
        if isinstance(other, GroundingFunction):
            new_domain = self.domain + other.domain
            if new_domain.value == Domain.ANY:
                return PrimitiveGrounding(codomain=Domain.REAL_VALUE, value=self()-other())
            else:
                return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) - other(*args, **kwargs),
                               domain=new_domain)
        if isinstance(other, Callable):
            # TODO: We must know the domain of Callable to properly track the domain
            return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) - other(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) - other, domain=self.domain)
        raise RLangGroundingError(message=f"Cannot '-' a {type(self)} and a {type(other)}")

    def __rsub__(self, other):
        if isinstance(other, (np.ndarray, int, float)):
            return Feature(function=lambda *args, **kwargs: other - self(*args, **kwargs), domain=self.domain)
        raise RLangGroundingError(message=f"Cannot '-' a {type(other)} and a {type(self)}")

    def __add__(self, other):
        if isinstance(other, GroundingFunction):
            new_domain = self.domain + other.domain
            if new_domain.value == Domain.ANY:
                return PrimitiveGrounding(codomain=Domain.REAL_VALUE, value=self()+other())
            else:
                return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) + other(*args, **kwargs),
                               domain=self.domain + other.domain)
        if isinstance(other, (GroundingFunction, Callable)):
            # TODO: We must know the domain of Callable to properly track the domain
            return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) + other(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) + other, domain=self.domain)
        raise RLangGroundingError(message=f"Cannot '+' a {type(self)} and a {type(other)}")

    def __radd__(self, other):
        self.__add__(other)


class PrimitiveGrounding(GroundingFunction):
    """Represents a GroundingFunction with domain Domain.ANY."""
    def __init__(self, codomain: Domain, value: Any, name: str = None):
        if isinstance(value, (int, float, list)):
            value = np.array(value)
        self._value = value
        super().__init__(domain=Domain.ANY, codomain=codomain,
                         function=lambda *args, **kwargs: self._value, name=name)


class ActionReference(PrimitiveGrounding):
    """Represents a reference to a specified action.

    Args:
        action: the action.
        name (optional): name of the action.
    """
    def __init__(self, action: Any, name: str = None):
        # TODO: Integrate Action object into this constructor
        if isinstance(action, (int, float, list)):
            action = np.array(action)
        elif isinstance(action, GroundingFunction):
            if action.domain == Domain.ANY:
                action = np.array(action())
            else:
                raise RLangGroundingError(f"Actions cannot be functions of {action.domain}")
        super().__init__(codomain=Domain.ACTION, value=action, name=name)


class IdentityGrounding(GroundingFunction):
    """Represents S, A, and S'

    Args:
        domain: 'state', 'action', or 'next_state'
    """
    def __init__(self, domain: Union[str, Domain]):
        if not isinstance(domain, str):
            domain = domain.name.lower()
        super().__init__(domain=domain, codomain=domain,
                         function=lambda *args, **kwargs: kwargs[domain])


class Factor(GroundingFunction):
    """Represents a factor of the state space.

    Args:
        state_indexer: the indices or slice of the state space.
        name (optional): the name of the grounding.
        domain (optional [str]): the domain of the Factor.
    """
    def __init__(self, state_indexer: Any, name: str = None, domain: Union[str, Domain] = Domain.STATE):
        if isinstance(domain, Domain):
            domain_arg = domain.name.lower()
        elif isinstance(domain, str):
            domain_arg = domain
            domain = Domain.from_name(domain)
        else:
            raise RLangGroundingError(f"Invalid domain argument for Factor: {type(domain)}")

        if domain is not Domain.STATE and domain is not Domain.NEXT_STATE:
            raise RLangGroundingError(f"Factor cannot have domain of type {domain.name}")

        if type(state_indexer) == int:
            state_indexer = [state_indexer]
        self._state_indexer = state_indexer
        super().__init__(function=lambda *args, **kwargs: kwargs[domain_arg].__getitem__(self._state_indexer),
                         codomain=Domain.REAL_VALUE, domain=domain, name=name)

    def __getitem__(self, item):
        if isinstance(self._state_indexer, slice):
            print("This is weird")
        if isinstance(item, list):
            return Factor([self._state_indexer[i] for i in item], domain=self.domain)
        return Factor(self._state_indexer[item], domain=self.domain)

    def __repr__(self):
        return f"<Factor ({self.domain.name}): {str(self._state_indexer)}>"


class Feature(GroundingFunction):
    """Represents a feature of the state space.

    Can represent any function of the state space.

    Args:
        function: a function of state.
        name (optional): the name of the grounding.
        domain (optional [str]): the domain of the Feature.
    """
    def __init__(self, function: Callable, name: str = None, domain: Union[str, Domain] = Domain.STATE):
        super().__init__(function=function, codomain=Domain.REAL_VALUE, domain=domain, name=name)

    @classmethod
    def from_Factor(cls, factor: Factor, name: str = None):
        return cls(function=factor.__call__, name=name, domain=factor.domain)


class Predicate(GroundingFunction):
    """Represents a function which has a truth value.

    A Predicate is a feature with a codomain restricted to True or False.

    Args:
        function: a function of state that evaluates to a bool.
        name (optional): the name of the grounding.
        domain (optional [str]): the domain of the Predicate.
    """
    def __init__(self, function: Callable, name: str = None, domain: Union[str, Domain] = Domain.STATE):
        super().__init__(function=function, codomain=Domain.BOOLEAN, domain=domain, name=name)

    @classmethod
    def from_PrimitiveGrounding(cls, primitive_grounding: PrimitiveGrounding):
        if primitive_grounding.codomain != Domain.BOOLEAN:
            raise RLangGroundingError(f"Cannot cast PrimitiveGrounding with codomain {primitive_grounding.codomain} to Predicate")
        return cls(function=lambda *args, **kwargs: primitive_grounding(), domain=Domain.ANY)

    def __and__(self, other) -> Predicate:
        if isinstance(other, Predicate):
            return Predicate(function=lambda *args, **kwargs: self(*args, **kwargs) & other(*args, **kwargs),
                             domain=self.domain + other.domain)
        if isinstance(other, Callable):
            # TODO: We must know the domain of Callable to properly track the domain
            return Predicate(function=lambda *args, **kwargs: self(*args, **kwargs) & other(*args, **kwargs))
        if isinstance(other, bool):
            return self if other else Predicate(function=lambda *args, **kwargs: False, domain=Domain.ANY)
        raise RLangGroundingError(message=f"Cannot & a Predicate with a {type(other)}")

    def __rand__(self, other):
        return self.__and__(other)

    def __or__(self, other) -> Predicate:
        if isinstance(other, Predicate):
            return Predicate(function=lambda *args, **kwargs: self(*args, **kwargs) | other(*args, **kwargs),
                             domain=self.domain + other.domain)
        if isinstance(other, (Predicate, Callable)):
            # TODO: We must know the domain of Callable to properly track the domain
            return Predicate(function=lambda *args, **kwargs: self(*args, **kwargs) | other(*args, **kwargs))
        if isinstance(other, bool):
            return self if not other else Predicate(function=lambda *args, **kwargs: True, domain=Domain.ANY)
        raise RLangGroundingError(message=f"Cannot | a Predicate with a {type(other)}")

    def __ror__(self, other):
        return self.__or__(other)

    def __invert__(self) -> Predicate:
        return Predicate(function=lambda *args, **kwargs: bool(~ self(*args, **kwargs)), domain=self.domain)

    def __repr__(self):
        return f"<Predicate ({self.domain.name})>"


class Policy(GroundingFunction):
    """Represents a policy function

    Args:
        function: the policy function from states to actions.
        name (optional): the name of the grounding.
    """
    def __init__(self, function: Callable, name: str = None, domain: Union[str, Domain] = Domain.STATE):
        super().__init__(function=function, codomain=Domain.ACTION, domain=domain, name=name)


class Option(Grounding):
    """Grounding object for an option.

    Args:
        initiation: A Predicate capturing the initiation set of the option.
        policy: A Policy capturing the policy of the option.
        termination: A Predicate capturing the termination set of the option.
        name (optional): the name of the grounding.
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
            state: A State object.

        Returns:
            bool: True iff the option can be executed in the given state.
        """
        return self._initiation(*args, **kwargs)
