from __future__ import annotations

from collections.abc import MutableMapping
from collections import defaultdict
from typing import Callable, Any, Union

import numpy as np
from numpy.random import default_rng
from .utils.utils import Domain
from .utils.primitives import State, Action, Primitive
from .utils.grounding_exceptions import RLangGroundingError


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

    def equals(self, other):
        return self.name == other.name

    def __hash__(self):
        return self._name.__hash__()

    def __repr__(self):
        return self._name


class GroundingFunction(Grounding):
    """Parent class for groundings which are functions.

    GroundingFunctions have a specified domain and codomain.
    They are invoked using keyword arguments for their domain:

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

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        if ufunc == np.multiply:
            return self.__rmul__(inputs[0])
        if ufunc == np.true_divide:
            return self.__rtruediv__(inputs[0])
        if ufunc == np.add:
            return self.__radd__(inputs[0])
        if ufunc == np.subtract:
            return self.__rsub__(inputs[0])

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

    def __contains__(self, item):
        def contains(*args, **kwargs):
            return item(*args, **kwargs) in self(*args, **kwargs)

        return Proposition(function=contains, domain=self.domain + item.domain)

    # def contains(self, item):
    #     # TODO: ALERT: This is not actually being used right now. Hopefully we can discard it eventually
    #     # Cannot override __contains__ and return a non-boolean
    #     list_cast = lambda x: x.tolist() if isinstance(x, np.ndarray) else x
    #     # TODO: Fix this! 'in' only works for singleton batch items!
    #     unbatch_cast = lambda x, j: np.asarray(x)[j] if isinstance(x, Primitive) else x
    #     unbatch_size = lambda x: len(x) if isinstance(x, Primitive) else 1
    #     if isinstance(item, GroundingFunction):
    #         return Proposition(function=lambda *args, **kwargs: [
    #             [list_cast(unbatch_cast(item(*args, **kwargs), i)) in list_cast(self(*args, **kwargs))] for i in
    #             range(unbatch_size(item))],
    #                            domain=self.domain + item.domain)
    #     elif isinstance(item, Primitive):
    #         return Proposition(function=lambda *args, **kwargs: [
    #             [list_cast(unbatch_cast(item(*args, **kwargs), i)) in list_cast(self(*args, **kwargs))] for i in
    #             range(unbatch_size(item))],
    #                            domain=self.domain)
    #     if isinstance(item, (int, float, np.ndarray)):
    #         return Proposition(function=lambda *args, **kwargs: [list_cast(item) in list_cast(self(*args, **kwargs))],
    #                            domain=self.domain)
    #     raise RLangGroundingError(message=f"Object of type {type(item)} cannot be in a GroundingFunction")

    def __call__(self, *args, **kwargs):
        if 'state' in kwargs.keys():
            if not isinstance(kwargs['state'], State):
                kwargs.update({'state': State(kwargs['state'])})
        if 'action' in kwargs.keys():
            if not isinstance(kwargs['action'], Action):
                kwargs.update({'action': Action(kwargs['action'])})
        if 'next_state' in kwargs.keys():
            if not isinstance(kwargs['next_state'], State):
                kwargs.update({'next_state': State(kwargs['next_state'])})
        return self._function(*args, **kwargs)

    # TODO: write leq/geq

    def __lt__(self, other):
        if isinstance(other, GroundingFunction):
            return Proposition(function=lambda *args, **kwargs: self(*args, **kwargs) < other(*args, **kwargs),
                               domain=self.domain + other.domain)
        # if isinstance(other, Callable):
        #     return Proposition(function=lambda *args, **kwargs: self(*args, **kwargs) < other(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Proposition(function=lambda *args, **kwargs: self(*args, **kwargs) < other, domain=self.domain)
        raise RLangGroundingError(message=f"Cannot '<' a {type(self)} and a {type(other)}")

    def __le__(self, other):
        if isinstance(other, GroundingFunction):
            return Proposition(function=lambda *args, **kwargs: self(*args, **kwargs) <= other(*args, **kwargs),
                               domain=self.domain + other.domain)
        # if isinstance(other, Callable):
        #     # TODO: The new listener will never run this code
        #     # TODO: [OLD] We must know the domain of Callable to properly track the domain
        #     return Proposition(function=lambda *args, **kwargs: self(*args, **kwargs) <= other(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Proposition(function=lambda *args, **kwargs: self(*args, **kwargs) <= other, domain=self.domain)
        raise RLangGroundingError(message=f"Cannot '<=' a {type(self)} and a {type(other)}")

    def __eq__(self, other):
        if isinstance(other, GroundingFunction):
            return Proposition(function=lambda *args, **kwargs: self(*args, **kwargs) == other(*args, **kwargs),
                               domain=self.domain + other.domain)
        # if isinstance(other, Callable):
        #     # TODO: The new listener will never run this code
        #     # TODO: [OLD] We must know the domain of Callable to properly track the domain
        #     return Proposition(function=lambda *args, **kwargs: self(*args, **kwargs) == other(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Proposition(function=lambda *args, **kwargs: self(*args, **kwargs) == other, domain=self.domain)
        raise RLangGroundingError(message=f"Cannot '==' a {type(self)} and a {type(other)}")

    def __ne__(self, other):
        if isinstance(other, GroundingFunction):
            return Proposition(function=lambda *args, **kwargs: self(*args, **kwargs) != other(*args, **kwargs),
                               domain=self.domain + other.domain)
        # if isinstance(other, Callable):
        #     # TODO: The new listener will never run this code
        #     # TODO: We must know the domain of Callable to properly track the domain
        #     return Proposition(function=lambda *args, **kwargs: self(*args, **kwargs) != other(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Proposition(function=lambda *args, **kwargs: self(*args, **kwargs) != other, domain=self.domain)
        raise RLangGroundingError(message=f"Cannot '!=' a {type(self)} and a {type(other)}")

    def __mul__(self, other):
        if isinstance(other, GroundingFunction):
            new_domain = self.domain + other.domain
            if new_domain.value == Domain.ANY:
                return PrimitiveGrounding(codomain=Domain.REAL_VALUE, value=self() * other())
            else:
                return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) * other(*args, **kwargs),
                               domain=new_domain)
        # if isinstance(other, Callable):
        #     # TODO: The new listener will never run this code
        #     # TODO: We must know the domain of Callable to properly track the domain
        #     return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) * other(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) * other, domain=self.domain)
        raise RLangGroundingError(message=f"Cannot '*' a {type(self)} and a {type(other)}")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, GroundingFunction):
            new_domain = self.domain + other.domain
            if new_domain.value == Domain.ANY:
                return PrimitiveGrounding(codomain=Domain.REAL_VALUE, value=self() / other())
            else:
                return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) / other(*args, **kwargs),
                               domain=new_domain)
        # if isinstance(other, Callable):
        #     # TODO: The new listener will never run this code
        #     # TODO: We must know the domain of Callable to properly track the domain
        #     return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) / other(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) / other, domain=self.domain)
        raise RLangGroundingError(message=f"Cannot '/' a {type(self)} and a {type(other)}")

    def __rtruediv__(self, other):
        # if isinstance(other, Callable):
        #     # TODO: The new listener will never run this code
        #     # TODO: We must know the domain of Callable to properly track the domain
        #     return Feature(function=lambda *args, **kwargs: other(*args, **kwargs) / self(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Feature(function=lambda *args, **kwargs: other / self(*args, **kwargs), domain=self.domain)
        raise RLangGroundingError(message=f"Cannot '/' a {type(other)} and a {type(self)}")

    def __sub__(self, other):
        if isinstance(other, GroundingFunction):
            new_domain = self.domain + other.domain
            if new_domain.value == Domain.ANY:
                return PrimitiveGrounding(codomain=Domain.REAL_VALUE, value=self() - other())
            else:
                return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) - other(*args, **kwargs),
                               domain=new_domain)
        # if isinstance(other, Callable):
        #     # TODO: The new listener will never run this code
        #     # TODO: We must know the domain of Callable to properly track the domain
        #     return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) - other(*args, **kwargs))
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
                return PrimitiveGrounding(codomain=Domain.REAL_VALUE, value=self() + other())
            else:
                return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) + other(*args, **kwargs),
                               domain=self.domain + other.domain)
        # if isinstance(other, Callable):
        #     # TODO: The new listener will never run this code
        #     # TODO: We must know the domain of Callable to properly track the domain
        #     return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) + other(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) + other, domain=self.domain)
        raise RLangGroundingError(message=f"Cannot '+' a {type(self)} and a {type(other)}")

    def __radd__(self, other):
        return self.__add__(other)

    def __hash__(self):
        return hash((str(self), self.function, self.domain, self.codomain))


class PrimitiveGrounding(GroundingFunction):
    """GroundingFunction which requires no arguments, i.e. domain=Domain.ANY"""

    def __init__(self, codomain: Domain, value: Any, name: str = None):
        # TODO: What about lists? Should lists be cast? Only non-jagged ones?
        # TODO: Probably need to cast `value` to a Primitive
        if isinstance(value, (int, float)):
            value = np.array(value)
        self.value = value
        super().__init__(domain=Domain.ANY, codomain=codomain,
                         function=lambda *args, **kwargs: self.value, name=name)

    def __repr__(self):
        if self.name:
            return f"<PrimitiveGrounding \"{self.name}\": {self()}>"
        else:
            return f"<PrimitiveGrounding: {self()}>"

    def __hash__(self):
        return hash((str(self), str(self.value)))


class ConstantGrounding(PrimitiveGrounding):
    """GroundingFunction for defined RLang Constants"""

    def __repr__(self):
        return f"<Constant \"{self.name}\" = {self()}>"


class ActionReference(GroundingFunction):
    """Represents a reference to a specified action.

    Args:
        action: the action.
        name (optional): name of the action.
    """
    def __init__(self, action: Any, name=None, *args, **kwargs):
        if isinstance(action, (int, float, list)):
            function = lambda *sargs, **skwargs: Action(np.array(action))
            domain = Domain.ANY
        elif isinstance(action, GroundingFunction):
            function = action.__call__
            domain = action.domain
        else:
            raise RLangGroundingError(f"Actions cannot be of type {type(action)}")
        super().__init__(domain=domain, codomain=Domain.ACTION, function=function, name=name, *args, **kwargs)

    def __hash__(self):
        return hash(self.function)

    def __repr__(self):
        if self.name:
            return f"<ActionReference \"{self.name}\">"
        else:
            return f"<ActionReference>"


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

        if isinstance(state_indexer, int):
            state_indexer = [state_indexer]
        self.state_indexer = state_indexer
        super().__init__(function=lambda *args, **kwargs: kwargs[domain_arg].__getitem__(self.state_indexer),
                         codomain=Domain.REAL_VALUE, domain=domain, name=name)

    @property
    def indexer(self):
        return self.state_indexer

    @indexer.setter
    def indexer(self, new_indexer):
        self.state_indexer = new_indexer

    def __getitem__(self, item):
        if isinstance(item, int):
            item = [item]
        if isinstance(self.state_indexer, slice):
            if self.state_indexer.stop is None:
                raise RLangGroundingError("We don't know enough about the state space")
            else:
                old_indexer = list(range(*self.state_indexer.indices(self.state_indexer.stop)))
                new_indexer = [old_indexer[i] for i in item]
                return Factor(state_indexer=new_indexer, domain=self.domain)
        if isinstance(self.state_indexer, list):
            if isinstance(item, list):
                return Factor([self.state_indexer[i] for i in item], domain=self.domain)
            elif isinstance(item, slice):
                new_indexer = self.state_indexer[item]
                return Factor(state_indexer=new_indexer, domain=self.domain)

    def __hash__(self):
        return hash((str(self), str(self.state_indexer), self.name))

    def __repr__(self):
        additional_info = ""
        if self.name:
            additional_info += f" \"{self.name}\" ="
        return f"<Factor [{self.domain.name}]->[{self.codomain.name}]:{additional_info} S[{str(self.state_indexer)[1:-1] if isinstance(self.state_indexer, list) else str(self.state_indexer)}]>"


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

    def __hash__(self):
        return hash((str(self), self.function, self.domain, self.codomain))

    def __repr__(self):
        return f"<Feature [{self.domain.name}]->[{self.codomain.name}] \"{self.name}\">"


class MarkovFeature(GroundingFunction):
    """Represents a Grounding that is a function of (state, action, next_state)

    Args:
        function: a function of (state, action, next_state)
    """

    def __init__(self, function: Callable, name: str):
        super().__init__(domain=Domain.STATE_ACTION_NEXT_STATE, function=function, codomain=Domain.REAL_VALUE,
                         name=name)

    @classmethod
    def from_Factor(cls, factor: Factor, name: str = None):
        return cls(function=factor.__call__, name=name)

    def __repr__(self):
        return f"<MarkovFeature [{self.domain.name}]->[{self.codomain.name}] \"{self.name}\">"


class Proposition(GroundingFunction):
    """Represents a function which has a truth value.

    A Proposition is a feature with a codomain restricted to True or False.

    Args:
        function: a function of state that evaluates to a bool.
        name (optional): the name of the grounding.
        domain (optional [str]): the domain of the Proposition.
    """

    def __init__(self, function: Callable, name: str = None, domain: Union[str, Domain] = Domain.STATE):
        super().__init__(function=function, codomain=Domain.BOOLEAN, domain=domain, name=name)

    @classmethod
    def from_PrimitiveGrounding(cls, primitive_grounding: PrimitiveGrounding):
        if primitive_grounding.codomain != Domain.BOOLEAN:
            raise RLangGroundingError(
                f"Cannot cast PrimitiveGrounding with codomain {primitive_grounding.codomain} to Proposition")
        return cls(function=lambda *args, **kwargs: primitive_grounding(), domain=Domain.ANY)

    @classmethod
    def TRUE(cls):
        return cls(function=lambda *args, **kwargs: True, domain=Domain.ANY)

    @classmethod
    def FALSE(cls):
        return cls(function=lambda *args, **kwargs: False, domain=Domain.ANY)

    def __and__(self, other) -> Proposition:
        if isinstance(other, Proposition):
            return Proposition(function=lambda *args, **kwargs: self(*args, **kwargs) & other(*args, **kwargs),
                               domain=self.domain + other.domain)
        if isinstance(other, Callable):
            # TODO: We must know the domain of Callable to properly track the domain
            return Proposition(function=lambda *args, **kwargs: self(*args, **kwargs) & other(*args, **kwargs))
        if isinstance(other, bool):
            return self if other else Proposition(function=lambda *args, **kwargs: False, domain=Domain.ANY)
        raise RLangGroundingError(message=f"Cannot & a Proposition with a {type(other)}")

    def __rand__(self, other):
        return self.__and__(other)

    def __or__(self, other) -> Proposition:
        if isinstance(other, Proposition):
            return Proposition(function=lambda *args, **kwargs: self(*args, **kwargs) | other(*args, **kwargs),
                               domain=self.domain + other.domain)
        if isinstance(other, (Proposition, Callable)):
            # TODO: We must know the domain of Callable to properly track the domain
            return Proposition(function=lambda *args, **kwargs: self(*args, **kwargs) | other(*args, **kwargs))
        if isinstance(other, bool):
            return self if not other else Proposition(function=lambda *args, **kwargs: True, domain=Domain.ANY)
        raise RLangGroundingError(message=f"Cannot | a Proposition with a {type(other)}")

    def __ror__(self, other):
        return self.__or__(other)

    def __invert__(self) -> Proposition:
        return Proposition(function=lambda *args, **kwargs: bool(not self(*args, **kwargs)), domain=self.domain)

    def __hash__(self):
        return hash((str(self), self.function))

    def __repr__(self):
        return f"<Proposition [{self.domain.name}]->[{self.codomain.name}] \"{self.name}\">"


class Goal(Proposition):
    def __repr__(self):
        return f"<Goal [{self.domain.name}]->[{self.codomain.name}] \"{self.name}\">"


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

    def compose_probability(self, probability: float):
        self._probability = self._probability * probability


class ProbabilityDistribution(MutableMapping):
    def __init__(self, distribution=None):
        if distribution is None:
            distribution = dict()
        # for k, v in distribution.items():
        #     if v < 0.0 or v > 1.0:
        #         raise RLangGroundingError(f"Must be bounded between 0.0 and 1.0, got {v}")

        self.domain = Domain.ANY
        self.distribution = distribution
        self.rng = default_rng()
        self.update_metadata()
        self.arg_store = list()
        self.kwarg_store = dict()
        self.true_distribution = dict()
        self.calculated = False

    def calculate_true_distribution(self):
        pass

    @classmethod
    def from_single(cls, k, *args, **kwargs):
        return cls({k: 1.0})

    @classmethod
    def from_list_eq(cls, ks, *args, **kwargs):
        sd_dict = dict()
        for k in ks:
            sd_dict[k] = 1.0
        return cls(sd_dict)

    def update_metadata(self):
        self.calculate_domain()

    def calculate_domain(self):
        self.domain = Domain.ANY
        for k, v in self.distribution.items():
            self.domain += k.domain

    def sample(self):
        random_variable = self.rng.uniform()
        offset = 0.0
        for k, v in self.true_distribution.items():
            offset += v
            if random_variable < offset:
                return k

    def join(self, new_distribution):
        for k, v in new_distribution.items():
            if k in self.distribution:
                self.distribution[k] += v
            else:
                self.distribution[k] = v
                self.domain += k.domain

    def compose_probabilities(self, probability):
        for k, v in self.distribution.items():
            self.distribution[k] = v * probability

    def __call__(self, *args, **kwargs):
        self.arg_store = args
        self.kwarg_store = kwargs
        self.calculate_true_distribution()
        return self

    def __getitem__(self, key: Grounding):
        if self.calculated:
            return self.true_distribution[key]
        else:
            return self.distribution[key]

    def __setitem__(self, key: Grounding, value: float):
        self.distribution[key] = value
        self.update_metadata()

    def __delitem__(self, key: Grounding):
        del self.distribution[key]
        self.update_metadata()

    def __iter__(self):
        if self.calculated:
            return iter(self.true_distribution)
        else:
            return iter(self.distribution)

    def __repr__(self):
        if self.calculated:
            return str(self.true_distribution)
        else:
            return str(self.distribution)

    def __len__(self):
        if self.calculated:
            return len(self.true_distribution)
        else:
            return len(self.distribution)

    def __hash__(self):
        return hash(frozenset(self))


class ActionDistribution(ProbabilityDistribution):
    """Represents a distribution of possible next actions, options, or policies

    Args:
        distribution: a dictionary of the form {Action/Option/Policy: probability,}
    """

    def calculate_true_distribution(self):
        # TODO: Might be able to change all isinstance(k__, Action) calls to isinstance(k__, PrimitiveGrounding)
        def update_dictionary(k_, v_):
            if isinstance(k_, (dict, ProbabilityDistribution)):
                for k__, v__ in k_.items():
                    if isinstance(k__, Action):
                        update_dictionary(k__, v_*v__)
                    else:
                        update_dictionary(k__(*self.arg_store, **self.kwarg_store), v_*v__)
            elif k_ is not None:
                if isinstance(k_, Action):
                    a = k_
                else:
                    a = Action(k_)
                if a in true_distribution:
                    true_distribution[a] += v_
                else:
                    true_distribution[a] = v_

        true_distribution = dict()
        update_dictionary(self.distribution, 1.0)
        self.true_distribution = true_distribution
        self.calculated = True


class StateDistribution(ProbabilityDistribution):
    def __init__(self, distribution=None):
        if distribution:
            pass
            # ensure that everything is a State or function of state or something
        super().__init__(distribution=distribution)

    def calculate_true_distribution(self):
        def update_dictionary(k_, v_):
            if isinstance(k_, (dict, ProbabilityDistribution)):
                for k__, v__ in k_.items():
                    if isinstance(k__, State):
                        update_dictionary(k__, v_*v__)
                    else:
                        update_dictionary(k__(*self.arg_store, **self.kwarg_store), v_*v__)
            elif k_ is not None:
                if isinstance(k_, State):
                    a = k_
                else:
                    a = State(k_)
                if a in true_distribution:
                    true_distribution[a] += v_
                else:
                    true_distribution[a] = v_

        true_distribution = dict()
        update_dictionary(self.distribution, 1.0)
        self.true_distribution = true_distribution
        self.calculated = True


class RewardDistribution(ProbabilityDistribution):
    def __init__(self, distribution=None):
        if distribution:
            pass
            # ensure that everything is a Reward or something
        super().__init__(distribution=distribution)

    def calculate_true_distribution(self):
        def update_dictionary(k_, v_):
            if isinstance(k_, (dict, ProbabilityDistribution)):
                for k__, v__ in k_.items():
                    if isinstance(k__, Primitive):
                        update_dictionary(k__, v_*v__)
                    else:
                        update_dictionary(k__(*self.arg_store, **self.kwarg_store), v_*v__)
            elif k_ is not None:
                if isinstance(k_, Primitive):
                    a = k_
                else:
                    a = Primitive(k_)
                if a in true_distribution:
                    true_distribution[a] += v_
                else:
                    true_distribution[a] = v_

        true_distribution = dict()
        update_dictionary(self.distribution, 1.0)

        # print(true_distribution.keys())

        self.true_distribution = true_distribution
        self.calculated = True

    def expected(self):
        expected_reward = 0.0
        for k, v in self.true_distribution.items():
            expected_reward += k * v

        return expected_reward

    @classmethod
    def from_list_eq(cls, ks, *args, **kwargs):
        numeric_reward = 0.0
        sd_dict = dict()
        for k in ks:
            if isinstance(k, int):
                numeric_reward += k
            else:
                if k in sd_dict:
                    sd_dict[k] += 1.0
                else:
                    sd_dict[k] = 1.0
        # sd_dict[RewardFunction(lambda *args, **kwargs: numeric_reward, domain=Domain.ANY)] = 1.0
        return cls(sd_dict)

    def __call__(self, *args, **kwargs):
        super().__call__(*args, **kwargs)
        return self.expected()


class GroundingDistribution(ProbabilityDistribution):
    def __init__(self, grounding: Grounding, distribution=None):
        if distribution:
            pass
            # ensure that everything is a groundingfunction or something
        self.grounding = grounding
        super().__init__(distribution=distribution)

    def calculate_true_distribution(self):
        def update_dictionary(k_, v_):
            if isinstance(k_, (dict, ProbabilityDistribution)):
                for k__, v__ in k_.items():
                    if isinstance(k__, Primitive):
                        update_dictionary(k__, v_*v__)
                    else:
                        update_dictionary(k__(*self.arg_store, **self.kwarg_store), v_*v__)
            elif k_ is not None:
                if isinstance(k_, Primitive):
                    a = k_
                else:
                    a = State(k_)
                if a in true_distribution:
                    true_distribution[a] += v_
                else:
                    true_distribution[a] = v_

        true_distribution = dict()
        update_dictionary(self.distribution, 1.0)
        self.true_distribution = true_distribution
        self.calculated = True

    @classmethod
    def from_single(cls, k, *args, **kwargs):
        return cls(kwargs['g'], {k: 1.0})

    @classmethod
    def from_list_eq(cls, ks, *args, **kwargs):
        sd_dict = dict()
        for k in ks:
            sd_dict[k] = 1.0
        return cls(args[0], sd_dict)


class Policy(ProbabilisticFunction):
    """Represents a closed-loop policy function

    Args:
        function: a function from states to action distributions.
    """
    def __init__(self, function: Callable, domain: Domain = Domain.STATE, *args, **kwargs):
        super().__init__(function=function, domain=domain, codomain=Domain.ACTION, *args, **kwargs)

    @classmethod
    def from_action_distribution(cls, k):
        if not isinstance(k, ActionDistribution):
            raise RLangGroundingError(f"Expecting an ActionDistribution, got {type(k)}")
        return cls(function=k.__call__, domain=k.domain)

    def __repr__(self):
        additional_info = ""
        if self.name:
            additional_info += f" \"{self.name}\""
        return f"<Policy [{self.domain.name}]->[{self.codomain.name}]{additional_info}>"


class Plan(ProbabilisticFunction):
    """THIS DOES NOT WORK YET

    Represents an open-loop policy

    Args:
        distribution_list: a list of ActionDistributions
    """
    def __init__(self, distribution_list: [ActionDistribution]):
        domain = Domain.ANY
        length = None
        for d in distribution_list:
            domain += d.domain
            if length:
                if len(d) != length:
                    length = 0
                    break
            else:
                length = len(d)

        self.i = 0
        self.plan = distribution_list
        self.length = length
        super().__init__(function=lambda *args, **kwargs: self, domain=domain)

    def append(self, distribution):
        if not isinstance(distribution, ActionDistribution):
            raise RLangGroundingError(f"Expecting {str(ActionDistribution)}, got {type(distribution)}")
        self.plan.append(distribution)
        self.domain += distribution.domain
        if self.length != 0 and len(distribution) != 0:
            self.length += len(distribution)
        else:
            self.length = 0

    def extend(self, distribution_list):
        domain = Domain.ANY
        for d in distribution_list:
            if not isinstance(d, ActionDistribution):
                raise RLangGroundingError(f"Expecting {str(ActionDistribution)}, got {type(d)}")
            domain += d.domain
            if self.length != 0 and len(d) != 0:
                self.length += len(d)
            else:
                self.length = 0
        self.plan.extend(distribution_list)
        self.domain += domain

    def reset(self):
        self.i = 0

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i >= len(self.plan):
            raise StopIteration
        else:
            i = self.i
            self.i += 1
            return self.plan[i]


class OptionTermination:
    def __repr__(self):
        return "<OptionTermination>"

    def __eq__(self, other):
        return isinstance(other, OptionTermination)


class Option(Grounding):
    """Grounding object for an option.

    Args:
        initiation: A Proposition capturing the initiation set of the option.
        policy: A PolicyOld capturing the policy of the option.
        termination: A Proposition capturing the termination set of the option.
        name (optional): the name of the grounding.
    """

    def __init__(self, initiation: Proposition, policy: Policy, termination: Proposition, name: str = None):
        self.initiation = initiation
        self.termination = termination
        self.policy = policy
        super().__init__(name)

    def __call__(self, *args, **kwargs):
        if self.termination(*args, **kwargs):
            return OptionTermination()
        else:
            return self.policy(*args, **kwargs)

    def can_initiate(self, *args, **kwargs) -> bool:
        """Determines whether the option can be executed in a given state.

        Args:
            state: A State object.

        Returns:
            bool: True iff the option can be executed in the given state.
        """
        return self.initiation(*args, **kwargs)

    def __hash__(self):
        return hash((self.initiation, self.policy, self.termination))

    def __repr__(self):
        return f"<Option \"{self.name}\">"


class TransitionFunction(ProbabilisticFunction):
    """Represents a transition function."""

    def __init__(self, function: Callable = None, domain: Domain = Domain.STATE_ACTION, *args, **kwargs):
        if function is None:
            function = StateDistribution().__call__
        super().__init__(function=function, domain=domain, codomain=Domain.STATE, *args, **kwargs)

    @classmethod
    def from_state_distribution(cls, k):
        if not isinstance(k, StateDistribution):
            raise RLangGroundingError(f"Expecting a StateDistribution, got {type(k)}")
        return cls(function=k.__call__, domain=k.domain)

    def __repr__(self):
        additional_info = ""
        if self.name:
            additional_info += f" \"{self.name}\""
        return f"<TransitionFunction [{self.domain.name}]->[{self.codomain.name}]{additional_info}>"


class RewardFunction(ProbabilisticFunction):
    """Represents function of expected reward."""

    def __init__(self, function: Callable = None, domain: Domain = Domain.ANY, *args, **kwargs):
        if function is None:
            function = RewardDistribution().__call__
        super().__init__(function=function, domain=domain, codomain=Domain.REWARD, *args, **kwargs)

    @classmethod
    def from_reward_distribution(cls, k):
        if not isinstance(k, RewardDistribution):
            raise RLangGroundingError(f"Expecting a RewardDistribution, got {type(k)}")
        return cls(function=k.__call__, domain=k.domain)

    def __repr__(self):
        additional_info = ""
        if self.name:
            additional_info += f" \"{self.name}\""
        return f"<RewardFunction [{self.domain.name}]->[{self.codomain.name}]{additional_info}>"


class Prediction(ProbabilisticFunction):
    """GroundingFunction for an RLang Prediction object.

    Used to express the predicted value of another RLang object.
    Limited to GroundingFunctions with a domain of (S) or (S, A).

    Args:
        grounding (Grounding): the grounding whom's value we are predicting
        function (:obj:`Callable`, optional): a function that predicts the value of grounding; can use a GroundingFunction
    """

    def __init__(self, grounding: Grounding, function: Callable = None, domain: Domain = Domain.STATE_ACTION, *args, **kwargs):
        if function is None:
            function = GroundingDistribution(grounding).__call__
        self.grounding = grounding
        super().__init__(function=function, domain=domain, codomain=Domain.REAL_VALUE, *args, **kwargs)

    @classmethod
    def from_grounding_distribution(cls, g, k):
        if not isinstance(k, GroundingDistribution):
            raise RLangGroundingError(f"Expecting a GroundingDistribution, got {type(k)}")
        return cls(grounding=g, function=k.__call__, domain=k.domain)

    def __repr__(self):
        additional_info = ""
        if self.name:
            additional_info += f" \"{self.name}\""
        return f"<Prediction [{self.domain.name}]->[{self.codomain.name}]{additional_info} for Grounding: {self.grounding.name}>"


class Effect(Grounding):
    """GroundingFunction for an RLang Effect object.

    Contains an optional RewardFunction, TransitionFunction,
    and list of Predictions.

    Args:
        reward_function (:obj:`RewardFunction`, optional): a RewardFunction
        transition_function (:obj:`TransitionFunction`, optional): a TransitionFunction
        predictions (:obj:`list[Prediction]`, optional): a list of Predictions
        name (:obj:`str`, optional): name of the Effect
        probability (:obj:`float`, optional): probability of this effect occurring; default: 1

    """
    def __init__(self, reward_function: RewardFunction = None, transition_function: TransitionFunction = None,
                 predictions: list = None, name: str = None, probability: float = 1.0):
        if predictions is None:
            predictions = list()
        self.reward_function = reward_function
        self.transition_function = transition_function
        self.predictions = predictions
        self.probability = probability
        super().__init__(name=name)

    def shallow_copy(self):
        return Effect(reward_function=self.reward_function, predictions=self.predictions,
                      transition_function=self.transition_function)

    def compose_probabilities(self, probability: float):
        self.probability = self.probability * probability
        if self.reward_function:
            self.reward_function = RewardFunction.from_reward_distribution(
                RewardDistribution({self.reward_function: probability}))
        if self.transition_function:
            self.transition_function = TransitionFunction.from_state_distribution(
                StateDistribution({self.transition_function: probability}))
        new_predictions = list()
        for p in self.predictions:
            new_predictions.append(
                Prediction.from_grounding_distribution(p.grounding, GroundingDistribution(p.grounding, {p: probability})))
        self.predictions = new_predictions

    @property
    def prediction_dict(self):
        prediction_dict = defaultdict(list)
        for p in self.predictions:
            # print(prediction_dict[p.grounding.name])
            prediction_dict[p.grounding.name].append(p)
        return dict(prediction_dict)

    def __repr__(self):
        if self.name:
            return f"<Effect \"{self.name}\" with P({self.probability})>"
        else:
            return f"<Effect with P({self.probability})>"
