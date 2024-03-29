"""Module containing all RLang groundings."""

from __future__ import annotations

from collections.abc import MutableMapping
from collections import defaultdict
from typing import Callable, Any, Union, List

import numpy as np
from numpy.random import default_rng
from .utils.utils import Domain
from .utils.primitives import MDPObject, VectorState, ObjectOrientedState, Action, Primitive, DictState
from .utils.grounding_exceptions import RLangGroundingError


class Grounding(object):
    """Parent class for all groundings.

    For all intents and purposes, this is an abstract class.

    """

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
    """Parent class for groundings that are callable. In general, only the children of this class should be used.

    All GroundingFunctions have a specified domain and codomain.
    They are invoked using keyword arguments that correspond to their domain::

        from rlang import Domain

        def can_move_fun(*args, **kwargs):
            return not kwargs['state'] in pit_states and kwargs['action'] in move_actions

        can_move = GroundingFunction(domain=Domain.STATE_ACTION, codomain=Domain.BOOLEAN, function=can_move_fun)
        can_move(state=0, action=1)
        >> True

    """

    def __init__(self, domain: Union[str, Domain], codomain: Union[str, Domain], function: Callable, name: str = None):
        """Initialize a GroundingFunction.

        Args:
            domain: Domain of the function.
            codomain: Codomain of the function.
            function: the function.
            name: the name of the Grounding.
        """
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

    # TODO: Contains should really only be used in sets. We should make a formal distinction between lists and sets in RLang
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
            if not isinstance(kwargs['state'], (VectorState, ObjectOrientedState, DictState)):
                kwargs.update({'state': VectorState(kwargs['state'])})
        if 'action' in kwargs.keys():
            if not isinstance(kwargs['action'], Action):
                kwargs.update({'action': Action(kwargs['action'])})
        if 'next_state' in kwargs.keys():
            if not isinstance(kwargs['next_state'], (VectorState, ObjectOrientedState, DictState)):
                kwargs.update({'next_state': VectorState(kwargs['next_state'])})
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
        if isinstance(other, (np.ndarray, int, float)):
            return Proposition(function=lambda *args, **kwargs: self(*args, **kwargs) <= other, domain=self.domain)
        raise RLangGroundingError(message=f"Cannot '<=' a {type(self)} and a {type(other)}")

    def __eq__(self, other):
        if isinstance(other, GroundingFunction):
            return Proposition(function=lambda *args, **kwargs: self(*args, **kwargs) == other(*args, **kwargs),
                               domain=self.domain + other.domain)
        if isinstance(other, (np.ndarray, int, float)):
            return Proposition(function=lambda *args, **kwargs: self(*args, **kwargs) == other, domain=self.domain)
        raise RLangGroundingError(message=f"Cannot '==' a {type(self)} and a {type(other)}")

    def __ne__(self, other):
        if isinstance(other, GroundingFunction):
            return Proposition(function=lambda *args, **kwargs: self(*args, **kwargs) != other(*args, **kwargs),
                               domain=self.domain + other.domain)
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
        if isinstance(other, (np.ndarray, int, float)):
            return Feature(function=lambda *args, **kwargs: self(*args, **kwargs) / other, domain=self.domain)
        raise RLangGroundingError(message=f"Cannot '/' a {type(self)} and a {type(other)}")

    def __rtruediv__(self, other):
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
    """GroundingFunction for defined RLang Constants
    """

    def __repr__(self):
        return f"<Constant \"{self.name}\" = {self()}>"


class ParameterizedAction:
    def __init__(self, function, name=None):
        self.function = function
        self.name = name if name else function.__name__

    def __call__(self, *args, **kwargs):
        return self.function(*args, **kwargs)


class ParameterizedActionExecution(GroundingFunction):
    def __init__(self, parameterized_action, arguments: List[GroundingFunction]):
        self.parameterized_action = parameterized_action
        self.arguments = arguments

        domain = Domain.ANY
        for arg in arguments:
            domain = domain + arg.domain

        argnames = ", ".join([arg.name if arg.name is not None else "unk" for arg in arguments])

        super().__init__(domain=domain, codomain=Domain.ACTION,
                         function=lambda *args, **kwargs:
                         parameterized_action(*[arg(*args, **kwargs) for arg in self.arguments], **kwargs),
                         name=parameterized_action.name + "(" + argnames + ")")


class ActionReference(GroundingFunction):
    """Represents a reference to a specified action."""

    def __init__(self, action: Any, name=None):
        """
        Args:
            action: the action.
            name (optional): name of the action.

        """
        if isinstance(action, (int, float, list)):
            function = lambda *sargs, **skwargs: Action(np.array(action))
            domain = Domain.ANY
        elif isinstance(action, GroundingFunction):
            function = action.__call__
            domain = action.domain
        else:
            raise RLangGroundingError(f"Actions cannot be of type {type(action)}")
        super().__init__(domain=domain, codomain=Domain.ACTION, function=function, name=name)

    def __hash__(self):
        return hash(self.function)

    def __repr__(self):
        if self.name:
            return f"<ActionReference \"{self.name}\">"
        else:
            return f"<ActionReference>"


class IdentityGrounding(GroundingFunction):
    """Grounding for representing S, A, and S'."""

    def __init__(self, domain: Union[str, Domain]):
        """Initialize a new IdentityGrounding."""
        if not isinstance(domain, str):
            domain = domain.name.lower()
        # Does this work properly?
        super().__init__(domain=domain, codomain=domain,
                         function=lambda *args, **kwargs: kwargs[domain])

    def __repr__(self):
        return f"<IdentityGrounding {self.codomain.name}>"


class MDPClassGrounding(GroundingFunction):
    def __init__(self, cls):
        self.cls = cls
        super().__init__(domain=Domain.ANY, codomain=Domain.ANY,
                         function=lambda *args, **kwargs: self.cls, name=f"{cls.__name__}_class_grounding")


class MDPObjectGrounding(GroundingFunction):
    """For representing objects, which may have properties that are functions of state."""

    def __init__(self, obj: MDPObject, name: str = None, domain=Domain.ANY):
        """Initialize an abstract object grounding.

        Args:
            obj: the MDPObject.
            name (optional): the name of the object.
        """
        self.obj = obj
        self.true_obj = None
        self.calculated = False

        super().__init__(function=self.calculate_true_obj, codomain=Domain.OBJECT_VALUE,
                         domain=domain, name=obj.name+"_grounding" if name is None else name)

    def calculate_true_obj(self, *args, **kwargs):
        def calculate_attr(attr):
            if isinstance(attr, GroundingFunction):
                return attr(*args, **kwargs)
            else:
                return attr

        attrs = list(map(lambda x: getattr(self.obj, x), self.obj.attr_list))
        calculated_attrs = list(map(calculate_attr, attrs))
        # print(calculated_attrs)

        self.true_obj = type(self.obj)(*calculated_attrs)
        self.calculated = True
        return self.true_obj

    def __getattr__(self, item):
        if self.calculated:
            return getattr(self.true_obj, item)
        else:
            return getattr(self.obj, item)

    def __eq__(self, other):
        if isinstance(other, MDPObject):
            return Proposition(function=lambda *args, **kwargs: self(*args, **kwargs) == other, domain=self.domain)
        else:
            return super().__eq__(other)

    def __hash__(self):
        return self.obj.__hash__()

    def __repr__(self):
        return f"<MDPObjectGrounding({self.name})[{self.obj.__repr__()}]>"


class MDPObjectAttributeGrounding(GroundingFunction):
    """For referencing attributes of abstract objects that are *not* in the state."""

    def __init__(self, grounding: GroundingFunction, attribute_chain: List):
        """Initialize a grounding for referencing abstract object attributes.

        Args:
            grounding: the MDPObjectGrounding whose attribute you are referencing.
            attribute_chain: a list of attribute/sub-attributes (e.g. `["color", "red_value"]`)
        """
        self.attribute_chain = attribute_chain
        self.grounding = grounding

        # [assert isinstance(attr, str) for attr in attribute_chain]
        # for attr in attribute_chain:
        #     assert isinstance(attr, str)
        # print(self.grounding)
        # assert self.grounding.name is not None

        def object_attribute_unwrap(obj, attr_chain):
            if not hasattr(obj, attr_chain[0]):
                raise RLangGroundingError(f"Object {obj} does not have attribute {attr_chain[0]}")
            one_layer_deeper = getattr(obj, attr_chain[0])
            if len(attr_chain) == 1:
                return one_layer_deeper
            else:
                return object_attribute_unwrap(one_layer_deeper, attr_chain[1:])

        super().__init__(
            function=lambda *args, **kwargs: object_attribute_unwrap(grounding(*args, **kwargs), self.attribute_chain),
            codomain=Domain.OBJECT_VALUE, domain=grounding.domain, name=self.grounding.name + '.' + '.'.join(self.attribute_chain))

    def equals(self, other):
        # print(self.grounding, other.grounding, self.attribute_chain, other.attribute_chain)
        # print(type(other))
        if isinstance(other, MDPObjectAttributeGrounding):
            gdeq = self.grounding.equals(other.grounding)
            atrseq = self.attribute_chain == other.attribute_chain
            # print(gdeq, atrseq)
            return gdeq and atrseq
        else:
            return False

    def __hash__(self):
        return hash((str(self), self.grounding, str(self.attribute_chain)))


class Predicate:
    def __init__(self, function, name=None):
        self.function = function
        self.name = name if name else function.__name__

    def __call__(self, *args, **kwargs):
        return self.function(*args, **kwargs)


class PredicateEvaluation(GroundingFunction):
    def __init__(self, predicate, arguments: List[GroundingFunction]):
        self.parameterized_action = predicate
        self.arguments = arguments

        domain = Domain.ANY
        for arg in arguments:
            if isinstance(arg, GroundingFunction):
                domain = domain + arg.domain

        argnames = ", ".join([arg.name if arg.name is not None else "unk" for arg in arguments])

        super().__init__(domain=domain, codomain=Domain.REAL_VALUE+Domain.BOOLEAN,
                         function=lambda *args, **kwargs:
                         predicate(*[arg(*args, **kwargs) for arg in self.arguments], **kwargs),
                         name=predicate.name + "(" + argnames + ")")


class StateObjectAttributeGrounding(GroundingFunction):
    """For referencing attributes of objects in the state when the state is object-oriented."""

    def __init__(self, attribute_chain: List, domain: Union[str, Domain] = Domain.STATE):
        """Initialize a grounding for referencing object attributes, when those objects are in the state.

        Args:
            attribute_chain: a list of attribute/sub-attributes (e.g. `["ball", "color", "red_value"]`)
            domain: either "state" or "next_state".
        """
        self.attribute_chain = attribute_chain

        if isinstance(domain, Domain):
            domain_arg = domain.name.lower()
        elif isinstance(domain, str):
            domain_arg = domain
            domain = Domain.from_name(domain)
        else:
            raise RLangGroundingError(f"Invalid domain argument for StateObjectAttributeGrounding: {type(domain)}")

        if domain is not Domain.STATE and domain is not Domain.NEXT_STATE:
            raise RLangGroundingError(f"StateObjectAttributeGrounding cannot have domain of type {domain.name}")

        def state_object_attribute_unwrap(state_or_obj, attr_chain):
            if not hasattr(state_or_obj, attr_chain[0]):
                raise RLangGroundingError(f"Object {state_or_obj} does not have attribute {attr_chain[0]}")
            one_layer_deeper = getattr(state_or_obj, attr_chain[0])
            if len(attr_chain) == 1:
                return one_layer_deeper
            else:
                return state_object_attribute_unwrap(one_layer_deeper, attr_chain[1:])

        super().__init__(
            function=lambda *args, **kwargs: state_object_attribute_unwrap(kwargs[domain_arg], self.attribute_chain),
            codomain=Domain.OBJECT_VALUE, domain=domain, name="S." + '.'.join(self.attribute_chain))

    def __hash__(self):
        return hash(self.__repr__())

    def __repr__(self):
        return f"<StateObjectAttributeGrounding [S.{'.'.join(self.attribute_chain)}]>"


class Factor(GroundingFunction):
    """Represents a factor of the state space."""

    def __init__(self, state_indexer: Any, name: str = None, domain: Union[str, Domain] = Domain.STATE):
        """

        Args:
            state_indexer: the indices or slice of the state space.
            name (optional): the name of the grounding.
            domain (optional [str]): the domain of the Factor.
        """
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
    """

    def __init__(self, function: Callable, name: str = None, domain: Union[str, Domain] = Domain.STATE):
        """
        Args:
            function: a function of state.
            name (optional): the name of the grounding.
            domain (optional [str]): the domain of the Feature.
        """
        super().__init__(function=function, codomain=Domain.REAL_VALUE, domain=domain, name=name)

    @classmethod
    def from_Factor(cls, factor: Factor, name: str = None):
        return cls(function=factor.__call__, name=name, domain=factor.domain)

    def __hash__(self):
        return hash((str(self), self.function, self.domain, self.codomain))

    def __repr__(self):
        return f"<Feature [{self.domain.name}]->[{self.codomain.name}] \"{self.name}\">"


class MarkovFeature(GroundingFunction):
    """Represents a Grounding that is a function of (state, action, next_state)"""

    def __init__(self, function: Callable, name: str):
        """
        Args:
            function: a function of (state, action, next_state)
        """
        super().__init__(domain=Domain.STATE_ACTION_NEXT_STATE, function=function, codomain=Domain.REAL_VALUE,
                         name=name)

    @classmethod
    def from_Factor(cls, factor: Factor, name: str = None):
        return cls(function=factor.__call__, name=name)

    def __repr__(self):
        return f"<MarkovFeature [{self.domain.name}]->[{self.codomain.name}] \"{self.name}\">"


class QuantifierSpecification:
    def __init__(self, cls, quantifier, dot_exp=None):
        self.cls = cls
        self.quantifier = quantifier
        self.dot_exp = dot_exp
        self.name = f"{self.quantifier} {self.cls.__name__}"

    def __repr__(self):
        return f"<QuantifierSpecification {self.name}{'.'.join(self.dot_exp) if self.dot_exp else ''}>"


class Proposition(GroundingFunction):
    """Represents a function which has a truth value.

    A Proposition is a feature with a codomain restricted to True or False.
    """

    def __init__(self, function: Callable, name: str = None, domain: Union[str, Domain] = Domain.STATE):
        """
        Args:
            function: a function of state that evaluates to a bool.
            name (optional): the name of the grounding.
            domain (optional [str]): the domain of the Proposition.
        """
        super().__init__(function=function, codomain=Domain.BOOLEAN, domain=domain, name=name)

    @classmethod
    def from_PrimitiveGrounding(cls, primitive_grounding: PrimitiveGrounding):
        if primitive_grounding.codomain != Domain.BOOLEAN:
            raise RLangGroundingError(
                f"Cannot cast PrimitiveGrounding with codomain {primitive_grounding.codomain} to Proposition")
        return cls(function=lambda *args, **kwargs: primitive_grounding(), domain=Domain.ANY)

    # TODO: Eventually just work this logic into the Proposition class
    @classmethod
    def from_QuantifierSpecification(cls, quantifier_specification: QuantifierSpecification, grounding: GroundingFunction, operation):
        def unwrap_and_quantify(*args, **kwargs):
            items = list(kwargs['knowledge'].objects_of_type(quantifier_specification.cls).values())
            if quantifier_specification.dot_exp is not None:
                items = [MDPObjectAttributeGrounding(g, quantifier_specification.dot_exp) for g in items]
            if quantifier_specification.quantifier == 'all':
                for item in items:
                    if not operation(grounding(*args, **kwargs), item(*args, **kwargs)):
                        return False
                return True
            elif quantifier_specification.quantifier == 'any':
                for item in items:
                    if operation(grounding(*args, **kwargs), item(*args, **kwargs)):
                        return True
                return False
            else:
                raise RLangGroundingError(f"Unknown quantifier: {quantifier_specification.quantifier}")

        return cls(function=lambda *args, **kwargs: unwrap_and_quantify(*args, **kwargs), domain=Domain.STATE_KNOWLEDGE)

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
    """Represents a function that provides stochastic output.

    """

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
    """
    
    """

    def __init__(self, distribution=None):
        if distribution is None:
            distribution = dict()
        # for function, v in distribution.items():
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
                    if isinstance(k__, (Action, str)):
                        update_dictionary(k__, v_ * v__)
                    else:
                        update_dictionary(k__(*self.arg_store, **self.kwarg_store), v_ * v__)
            elif k_ is not None:
                if isinstance(k_, Action):
                    a = k_
                elif isinstance(k_, str):
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
                    if isinstance(k__, (VectorState, ObjectOrientedState, DictState)):
                        update_dictionary(k__, v_ * v__)
                    else:
                        update_dictionary(k__(*self.arg_store, **self.kwarg_store), v_ * v__)
            elif k_ is not None:
                if isinstance(k_, (VectorState, ObjectOrientedState, DictState)):
                    a = k_
                else:
                    a = VectorState(k_)
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
                        update_dictionary(k__, v_ * v__)
                    else:
                        update_dictionary(k__(*self.arg_store, **self.kwarg_store), v_ * v__)
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
    def __init__(self, grounding: Grounding, distribution=None, complete=False):
        if distribution:
            pass
            # ensure that everything is a groundingfunction or something
        self.grounding = grounding
        self.complete = complete
        super().__init__(distribution=distribution)

    def calculate_true_distribution(self):
        def update_dictionary(k_, v_):
            if isinstance(k_, (dict, ProbabilityDistribution)):
                for k__, v__ in k_.items():
                    if isinstance(k__, (Primitive, MDPObject)):
                        update_dictionary(k__, v_ * v__)
                    else:
                        update_dictionary(k__(*self.arg_store, **self.kwarg_store), v_ * v__)
            elif k_ is not None:
                if isinstance(k_, (Primitive, MDPObject)):
                    a = k_
                else:
                    a = Primitive(k_)
                if a in true_distribution:
                    true_distribution[a] += v_
                else:
                    true_distribution[a] = v_

        true_distribution = dict()
        update_dictionary(self.distribution, 1.0)
        self.true_distribution = true_distribution
        self.calculated = True

    @classmethod
    def from_list_eq(cls, ks, *args, **kwargs):
        sd_dict = dict()
        for k in ks:
            sd_dict[k] = 1.0
        return cls(args[0], sd_dict)


class Policy(ProbabilisticFunction):
    """Represents a closed-loop policy function"""

    def __init__(self, function: Callable, domain: Domain = Domain.STATE, *args, **kwargs):
        """
        Args:
            function: a function from states to action distributions.
        """
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


class Plan(Grounding):
    """Represents an open-loop policy"""
    def __init__(self, function: Callable = None, name: str = None):
        self.function = function
        super().__init__(name=name)

    def reset(self):
        pass

    def __call__(self, *args, **kwargs):
        if self.function is None:
            raise RLangGroundingError("Plan function is not defined")
        return self.function(*args, **kwargs)

    def __repr__(self):
        if self.name:
            return f"<Plan \"{self.name}\">"
        else:
            return f"<Plan unnamed>"


class IteratedPlan(Plan):
    """One kind of plan implementation"""

    def __init__(self, plan_steps, name: str = None):
        self.plan_steps = plan_steps
        super().__init__(function=self.__call__, name=name)
        self.i = 0

    def reset(self):
        self.i = 0
        for p in self.plan_steps:
            if isinstance(p, PlanExecution):
                p.plan.reset()
            elif isinstance(p, IteratedPlan):
                p.reset()

    def __call__(self, *args, **kwargs):
        if self.i >= len(self.plan_steps):
            return None
        action = self.plan_steps[self.i]
        # print(action)
        if isinstance(action, PlanExecution):
            next_action = action(*args, **kwargs)
            if next_action is None:
                action.plan.reset()
                self.i += 1
                return self(*args, **kwargs)
            else:
                return next_action
        else:
            # print(action)
            # print(type(action))
            # print(self.i)
            # print(action(*args, **kwargs))
            self.i += 1
            # if isinstance(action, ActionDistribution):
            #     print("returning")
            #     return action
            # else:
            return action(*args, **kwargs)

    def __repr__(self):
        if self.name:
            return f"<IteratedPlan \"{self.name}\">"
        else:
            return f"<IteratedPlan unnamed>"


class PlanExecution(GroundingFunction):
    def __init__(self, plan, arguments: List[GroundingFunction]=None):
        self.plan = plan
        if arguments is None:
            arguments = []
        self.arguments = arguments

        domain = Domain.ANY
        for arg in arguments:
            domain = domain + arg.domain

        argnames = ", ".join([arg.name if arg.name is not None else "unk" for arg in arguments])

        super().__init__(domain=domain, codomain=Domain.ACTION,
                         function=lambda *args, **kwargs:
                         self.plan(*[arg(*args, **kwargs) for arg in self.arguments], **kwargs),
                         name=plan.name + "(" + argnames + ")")

    def __repr__(self):
        return f"<PlanExecution of {self.plan} with {self.arguments}>"

# class Plan(ProbabilisticFunction):
#     """THIS DOES NOT WORK YET
#
#     Represents an open-loop policy
#
#     Args:
#         distribution_list: a list of ActionDistributions
#
#
#     """
#
#     def __init__(self, distribution_list: [ActionDistribution]):
#         domain = Domain.ANY
#         length = None
#         for d in distribution_list:
#             domain += d.domain
#             if length:
#                 if len(d) != length:
#                     length = 0
#                     break
#             else:
#                 length = len(d)
#
#         self.i = 0
#         self.plan = distribution_list
#         self.length = length
#         super().__init__(function=lambda *args, **kwargs: self, domain=domain)
#
#     def append(self, distribution):
#         if not isinstance(distribution, ActionDistribution):
#             raise RLangGroundingError(f"Expecting {str(ActionDistribution)}, got {type(distribution)}")
#         self.plan.append(distribution)
#         self.domain += distribution.domain
#         if self.length != 0 and len(distribution) != 0:
#             self.length += len(distribution)
#         else:
#             self.length = 0
#
#     def extend(self, distribution_list):
#         domain = Domain.ANY
#         for d in distribution_list:
#             if not isinstance(d, ActionDistribution):
#                 raise RLangGroundingError(f"Expecting {str(ActionDistribution)}, got {type(d)}")
#             domain += d.domain
#             if self.length != 0 and len(d) != 0:
#                 self.length += len(d)
#             else:
#                 self.length = 0
#         self.plan.extend(distribution_list)
#         self.domain += domain
#
#     def reset(self):
#         self.i = 0
#
#     def __iter__(self):
#         self.i = 0
#         return self
#
#     def __next__(self):
#         if self.i >= len(self.plan):
#             raise StopIteration
#         else:
#             i = self.i
#             self.i += 1
#             return self.plan[i]


class OptionTermination:
    """
    
    """

    def __repr__(self):
        return "<OptionTermination>"

    def __eq__(self, other):
        return isinstance(other, OptionTermination)


class Option(Grounding):
    """Grounding object for an option."""

    def __init__(self, initiation: Proposition, policy: Policy, termination: Proposition, name: str = None):
        """
        Args:
            initiation: A Proposition capturing the initiation set of the option.
            policy: A PolicyOld capturing the policy of the option.
            termination: A Proposition capturing the termination set of the option.
            name (optional): the name of the grounding.
        """
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
    """

    def __init__(self, grounding: Grounding, function: Callable = None, domain: Domain = Domain.STATE_ACTION, complete=False, *args,
                 **kwargs):
        """
        Args:
            grounding (Grounding): the grounding whom's value we are predicting
            function (:obj:`Callable`, optional): a function that predicts the value of grounding; can use a GroundingFunction
        """
        if function is None:
            function = GroundingDistribution(grounding).__call__
        self.grounding = grounding
        self.complete = complete
        super().__init__(function=function, domain=domain, codomain=Domain.REAL_VALUE, *args, **kwargs)

    @classmethod
    def from_grounding_distribution(cls, grounding: Grounding, function: GroundingDistribution, complete=False):
        """
        Args:
            grounding: The grounding that is predicted
            function: The prediction function
        """
        if not isinstance(function, GroundingDistribution):
            raise RLangGroundingError(f"Expecting a GroundingDistribution, got {type(function)}")
        return cls(grounding=grounding, function=function.__call__, domain=function.domain, complete=complete)

    def __repr__(self):
        additional_info = ""
        if self.name:
            additional_info += f" \"{self.name}\""
        return f"<Prediction [{self.domain.name}]->[{self.codomain.name}]{additional_info} for Grounding: {self.grounding.name}>"


class Effect(Grounding):
    """GroundingFunction for an RLang Effect object.

    Contains an optional RewardFunction, TransitionFunction,
    and list of Predictions.
    """

    def __init__(self, reward_function: RewardFunction = None, transition_function: TransitionFunction = None,
                 predictions: List[Prediction] = None, name: str = None, probability: float = 1.0):
        """
        Args:
            reward_function: a RewardFunction
            transition_function: a TransitionFunction
            predictions: a list of Predictions
            name: name of the Effect
            probability (Optional[float]): probability of this effect occurring; default: 1

        """
        if predictions is None:
            predictions = list()
        self.reward_function = reward_function
        self.transition_function = transition_function
        self.predictions = predictions
        self.probability = probability
        super().__init__(name=name)

    def shallow_copy(self):
        """"""
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
                Prediction.from_grounding_distribution(p.grounding,
                                                       GroundingDistribution(p.grounding, {p: probability}),
                                                       complete=p.complete))
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
