from __future__ import annotations
import warnings
from typing import Callable, Any, Union

import numpy as np
from rlang.src.grounding.internals import Domain, State, Action, BatchedPrimitive
from rlang.src.exceptions import RLangGroundingError


class Grounding(object):
    """Parent class for all grounded objects."""
    def __init__(self, name=None):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

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
        self._domain = domain
        self._codomain = codomain
        self._function = function

    @property
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, domain: Domain):
        self._domain = domain

    @property
    def codomain(self):
        return self._codomain

    @codomain.setter
    def codomain(self, codomain: Domain):
        self._codomain = codomain

    @property
    def function(self):
        return self._function

    @function.setter
    def function(self, function: Callable):
        self._function = function

    def contains(self, item):
        # Cannot override __contains__ and return a non-boolean
        list_cast = lambda x: x.tolist() if isinstance(x, np.ndarray) else x
        # TODO: Fix this! 'in' only works for singleton batch items!
        unbatch_cast = lambda x, j: np.asarray(x)[j] if isinstance(x, BatchedPrimitive) else x
        unbatch_size = lambda x: len(x) if isinstance(x, BatchedPrimitive) else 1
        if isinstance(item, GroundingFunction):
            return Predicate(function=lambda *args, **kwargs: [[list_cast(unbatch_cast(item(*args, **kwargs), i)) in list_cast(self(*args, **kwargs))] for i in range(unbatch_size(item))],
                             domain=self.domain + item.domain)
        elif isinstance(item, BatchedPrimitive):
            return Predicate(function=lambda *args, **kwargs: [
                [list_cast(unbatch_cast(item(*args, **kwargs), i)) in list_cast(self(*args, **kwargs))] for i in
                range(unbatch_size(item))],
                             domain=self.domain)
        if isinstance(item, (int, float, np.ndarray)):
            return Predicate(function=lambda *args, **kwargs: [list_cast(item) in list_cast(self(*args, **kwargs))],
                             domain=self.domain)
        raise RLangGroundingError(message=f"Object of type {type(item)} cannot be in a GroundingFunction")

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
        # TODO: What about lists? Should lists be cast? Only non-jagged ones?
        if isinstance(value, (int, float)):
            value = np.array(value)
        self._value = value
        super().__init__(domain=Domain.ANY, codomain=codomain,
                         function=lambda *args, **kwargs: self._value, name=name)

    def __repr__(self):
        return f"<PrimitiveGrounding \"{self.name}\" = {self()}>"


class ConstantGrounding(PrimitiveGrounding):
    """GroundingFunction for constants"""

    def __repr__(self):
        return f"<Constant \"{self.name}\" = {self()}>"


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
                raise RLangGroundingError(f"Actions cannot be functions of {action.domain.name}")
        super().__init__(codomain=Domain.ACTION, value=action, name=name)

    def __repr__(self):
        return f"<ActionReference \"{self.name}\" = {self()}>"


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

    def __repr__(self):
        return f"<IdentityGrounding {self.codomain.name}>"


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

        elif isinstance(state_indexer, int):
            state_indexer = [state_indexer]
        self._state_indexer = state_indexer
        super().__init__(function=lambda *args, **kwargs: kwargs[domain_arg].__getitem__(self._state_indexer),
                         codomain=Domain.REAL_VALUE, domain=domain, name=name)

    @property
    def indexer(self):
        return self._state_indexer

    @indexer.setter
    def indexer(self, new_indexer):
        self._state_indexer = new_indexer


    def __getitem__(self, item):
        if isinstance(self._state_indexer, slice):
            if self._state_indexer.stop is None:
                raise RLangGroundingError("We don't know enough about the state space")
            else:
                new_indexer = list(range(*self._state_indexer.indices(self._state_indexer.stop)))
                return Factor(state_indexer=new_indexer, domain=self.domain)
        if isinstance(self._state_indexer, list):
            if isinstance(item, int):
                item = [item]
            if isinstance(item, list):
                return Factor([self._state_indexer[i] for i in item], domain=self.domain)
            elif isinstance(item, slice):
                new_indexer = self._state_indexer[item]
                return Factor(state_indexer=new_indexer, domain=self.domain)


    def __repr__(self):
        return f"<Factor [{self.domain.name}]->[{self.codomain.name}]: S[{str(self._state_indexer)[1:-1] if isinstance(self._state_indexer, list) else str(self._state_indexer)}]>"


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

    def __repr__(self):
        return f"<Feature [{self.domain.name}]->[{self.codomain.name}] \"{self.name}\">"


class MarkovFeature(GroundingFunction):
    """Represents a Grounding that is a function of (state, action, next_state)

    Args:
        function: a function of (state, action, next_state)
    """
    def __init__(self, function: Callable, name: str):
        super().__init__(domain=Domain.STATE_ACTION_NEXT_STATE, function=function, codomain=Domain.REAL_VALUE, name=name)

    @classmethod
    def from_Factor(cls, factor: Factor, name: str = None):
        return cls(function=factor.__call__, name=name)

    def __repr__(self):
        return f"<MarkovFeature [{self.domain.name}]->[{self.codomain.name}] \"{self.name}\">"


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
        return Predicate(function=lambda *args, **kwargs: bool(not self(*args, **kwargs)), domain=self.domain)

    def __repr__(self):
        return f"<Predicate [{self.domain.name}]->[{self.codomain.name}] \"{self.name}\">"

class Policy(GroundingFunction):
    """Represents a policy function

    Args:
        function: the policy function from states to actions.
        name (optional): the name of the grounding.
    """
    def __init__(self, function: Callable, name: str = None, domain: Union[str, Domain] = Domain.STATE):
        super().__init__(function=function, codomain=Domain.ACTION, domain=domain, name=name)

    def __repr__(self):
        return f"<Policy [{self.domain.name}]->[{self.codomain.name}] \"{self.name}\">"


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

    def __repr__(self):
        return f"<Option \"{self.name}\">"


class ValueFunction(GroundingFunction):
    """Represents a value function."""
    def __init__(self, function: Callable):
        super().__init__(domain=Domain.STATE, codomain=Domain.STATE_VALUE, function=function)


class ProbabilisticFunction(GroundingFunction):
    """Represents a function which provides stochastic output."""
    def __init__(self, probability: float = 1.0, *args, **kwargs):
        self._probability = probability
        super().__init__(*args, **kwargs)

    @property
    def probability(self):
        return self._probability

    @probability.setter
    def probability(self, probability: float):
        self._probability = probability

#TODO: test
class TransitionFunction(ProbabilisticFunction):
    """Represents a transition function."""
    def __init__(self, function: Any = lambda *args, **kwargs: None, name: str = None, probability: float = 1.0):
        if isinstance(function, GroundingFunction):
            if not function.domain <= Domain.STATE_ACTION:
                raise RLangGroundingError(f"TransitionFunction must not be a function of {function.domain.name}")
            elif function.codomain != Domain.STATE and function.codomain != Domain.REAL_VALUE:
                # TODO: Need to check the dimension of the output in case its a REAL_VALUE domain
                raise RLangGroundingError(f"TransitionFunction must return a state, not a {function.codomain.name}")
        super().__init__(domain=Domain.STATE_ACTION, codomain=Domain.STATE, function=function, name=name, probability=probability)

    def __repr__(self):
        return f"<TransitionFunction [{self.domain.name}]->[{self.codomain.name}] \"{self.name}\" with P={self.probability}>"

#TODO: test
class RewardFunction(ProbabilisticFunction):
    """Represents a reward function."""
    def __init__(self, reward: Any, name: str = None, probability: float = 1.0):
        if isinstance(reward, (int, float, np.ndarray)):
            function = lambda *args, **kwargs: np.array(reward)
            domain = Domain.ANY
            if isinstance(reward, np.ndarray) and reward.dtype == np.bool:
                raise RLangGroundingError(f"Rewards must be real-valued, not {reward.dtype}")
        elif isinstance(reward, GroundingFunction):
            if reward.domain <= Domain.STATE_ACTION:
                function = reward
                domain = reward.domain
            else:
                raise RLangGroundingError(f"Rewards cannot be functions of {reward.domain.name}")
            if reward.codomain != Domain.REAL_VALUE:
                raise RLangGroundingError(f"Rewards must return real values, not values of type {reward.codomain.name}")
        elif isinstance(reward, Callable):
            function = reward
            domain = Domain.STATE_ACTION
        else:
            raise RLangGroundingError(f"Cannot construct a Reward from a {type(reward)}")

        super().__init__(domain=domain, codomain=Domain.REWARD, function=function, name=name, probability=probability)

    def __repr__(self):
        return f"<RewardFunction [{self.domain.name}]->[{self.codomain.name}] \"{self.name}\" with P={self.probability}>"


#TODO: test
class Prediction(ProbabilisticFunction):
    """GroundingFunction for a prediction for the value of a GroundingFunction.

    This should be used for Factors, Features, and Predicates
    which are limited to functions of (state) or (state, action).

    Args:
        grounding_function: a GroundingFunction
        value: the predicted value of the GroundingFunction (can also be a GroundingFunction)
    """

    def __init__(self, grounding_function: GroundingFunction, value: Any, name: str = None, probability: float = 1.0):
        if isinstance(value, (bool, int, float, np.ndarray)):
            function = lambda *args, **kwargs: np.array(value)
            domain = Domain.ANY
            if isinstance(value, bool) or (isinstance(value, np.ndarray) and value.dtype == np.bool):
                codomain = Domain.BOOLEAN
            else:
                codomain = Domain.REAL_VALUE
        elif isinstance(value, GroundingFunction):
            if value.domain <= Domain.STATE_ACTION:
                function = value
                domain = value.domain
                codomain = value.codomain
            else:
                raise RLangGroundingError(f"Cannot construct a Prediction based on a {value.domain.name}")
        elif isinstance(value, Callable):
            function = value
            domain = Domain.STATE_ACTION
            codomain = grounding_function.codomain
        else:
            raise RLangGroundingError(f"Cannot construct a Prediction from value of type {type(value)}")

        if grounding_function.domain > Domain.STATE_ACTION:
            raise RLangGroundingError(f"Cannot predict the value of a GroundingFunction with domain {grounding_function.domain.name}")

        if grounding_function.codomain != codomain:
            raise RLangGroundingError(f"Prediction value type ({codomain.name}) does not match grounding function type ({grounding_function.codomain.name})")

        self._grounding_function = grounding_function
        super().__init__(codomain=codomain, function=function, domain=domain, name=name, probability=probability)

    @property
    def grounding_predicted(self):
        return self._grounding_function

    @property
    def probability(self):
        return self._probability

    @probability.setter
    def probability(self, probability: float):
        self._probability = probability

    def __repr__(self):
        return f"<Prediction [{self.domain.name}]->[{self.codomain.name}] for \"{self._grounding_function.name}\" with P={self.probability}>"


class Effect(Grounding):
    def __init__(self, reward_functions: list, transition_functions: list, predictions: list, name: str = None, probability: float = 1.0):
        self.reward_functions = reward_functions
        self.transition_functions = transition_functions
        self.predictions = predictions
        self._probability = probability
        super().__init__(name)

    @property
    def probability(self):
        return self._probability

    @probability.setter
    def probability(self, probability: float):
        for s in [*self.reward_functions, *self.transition_functions, *self.predictions]:
            s.probability = s.probability * probability

    def __repr__(self):
        return f"<Effect \"{self.name}\" with P={self.probability}>"
