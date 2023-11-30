"""Module containing all RLang groundings."""

from __future__ import annotations

from collections.abc import MutableMapping
from collections import defaultdict
from typing import Callable, Any, Union, List

import numpy as np
import string
import random
from numpy.random import default_rng
from .utils.utils import Domain
from .utils.primitives import MDPObject, VectorState, ObjectOrientedState, Action, Primitive
from .utils.grounding_exceptions import RLangGroundingError
from .StateResolverClass import StateResolver   # Unsure if this is ever used


DEFAULT_STATE_TYPE = np.ndarray # Unsure if this is ever used

def fast_uuid(length: int = 4):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))


class Grounding(object):
    """Parent class for all groundings.

    For all intents and purposes, this is an abstract class.

    """

    def __init__(self, name: str = None):
        self.name = name

    def equals(self, other: Grounding):
        return self.__hash__() == other.__hash__()

    def __hash__(self):
        return self.name.__hash__()

    def __repr__(self):
        return f"<Grounding name={self.name}>"
    
    def __str__(self):
        return self.__repr__()


class GroundingFunction(Grounding):
    """Parent class for groundings that are functions representing MDP components.
    In general, only the children of this class should be used.

    All GroundingFunctions are invoked using keyword arguments that correspond to their domain::

        def can_move_fun(*args, **kwargs):
            return not kwargs['state'] in pit_states and kwargs['action'] in move_actions

        can_move = Proposition(function=can_move_fun, name="can_move")
        can_move(state=0, action=1)
        >> True
    
    They may also be invoked using arguments from the constituency tree that generated the grounding (namewrapped functionality)::

        can_move = Proposition(function=can_move_fun, name="can_move")
        can_move_without_dying = can_move & ~is_pit
        can_move_without_dying(can_move=True, is_pit=False)
        >> True

    """

    def __init__(self, function: Callable, name: str = None):
        """Initialize a GroundingFunction.

        Args:
            function: the function.
            name: the name of the Grounding.
        """

        super().__init__(name if name else f"grounding-function_{fast_uuid()}")
        self.function = function

    def nameit(self, name: str):
        if not isinstance(name, str):
            raise RLangGroundingError(f"Grounding name must be a string, got {type(name)}") # It's also possible we could extract the name of the variable here I think.
        self.name = name
        return self
    
    def namewrapped_function(self, *args, **kwargs):
        """This is a wrapper function for each GroundingFunction that checks whether
        the user has already specified the value for this function in the arguments.
        It enables the namewrapped functionality of GroundingFunctions."""
        if self.name in kwargs:
            return kwargs[self.name]
        return self.function(*args, **kwargs)

    # def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
    #     if ufunc == np.multiply:
    #         return self.__rmul__(inputs[0])
    #     if ufunc == np.true_divide:
    #         return self.__rtruediv__(inputs[0])
    #     if ufunc == np.add:
    #         return self.__radd__(inputs[0])
    #     if ufunc == np.subtract:
    #         return self.__rsub__(inputs[0])

    # def __contains__(self, item):
    #     def contains(*args, **kwargs):
    #         return item(*args, **kwargs) in self(*args, **kwargs)

    #     return Proposition(function=contains, domain=self.domain + item.domain)

    def __call__(self, *args, **kwargs):
        return self.namewrapped_function(*args, **kwargs)

    def __lt__(self, other):
        if isinstance(other, GroundingFunction):
            return Proposition(function=lambda *args, **kwargs: self.namewrapped_function(*args, **kwargs) < other.namewrapped_function(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Proposition(function=lambda *args, **kwargs: self.namewrapped_function(*args, **kwargs) < other)
        raise RLangGroundingError(message=f"Cannot '<' a {type(self)} and a {type(other)}")

    def __le__(self, other):
        if isinstance(other, GroundingFunction):
            return Proposition(function=lambda *args, **kwargs: self.namewrapped_function(*args, **kwargs) <= other.namewrapped_function(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Proposition(function=lambda *args, **kwargs: self.namewrapped_function(*args, **kwargs) <= other)
        raise RLangGroundingError(message=f"Cannot '<=' a {type(self)} and a {type(other)}")
        
    def __gt__(self, other):
        if isinstance(other, GroundingFunction):
            return Proposition(function=lambda *args, **kwargs: self.namewrapped_function(*args, **kwargs) > other.namewrapped_function(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Proposition(function=lambda *args, **kwargs: self.namewrapped_function(*args, **kwargs) > other)
        raise RLangGroundingError(message=f"Cannot '>' a {type(self)} and a {type(other)}")

    def __ge__(self, other):
        if isinstance(other, GroundingFunction):
            return Proposition(function=lambda *args, **kwargs: self.namewrapped_function(*args, **kwargs) >= other.namewrapped_function(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Proposition(function=lambda *args, **kwargs: self.namewrapped_function(*args, **kwargs) >= other)
        raise RLangGroundingError(message=f"Cannot '>=' a {type(self)} and a {type(other)}")

    def __eq__(self, other):
        if isinstance(other, GroundingFunction):
            return Proposition(function=lambda *args, **kwargs: self.namewrapped_function(*args, **kwargs) == other.namewrapped_function(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Proposition(function=lambda *args, **kwargs: self.namewrapped_function(*args, **kwargs) == other)
        raise RLangGroundingError(message=f"Cannot '==' a {type(self)} and a {type(other)}")

    def __ne__(self, other):
        if isinstance(other, GroundingFunction):
            return Proposition(function=lambda *args, **kwargs: self.namewrapped_function(*args, **kwargs) != other.namewrapped_function(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Proposition(function=lambda *args, **kwargs: self.namewrapped_function(*args, **kwargs) != other)
        raise RLangGroundingError(message=f"Cannot '!=' a {type(self)} and a {type(other)}")
    
    def __mul__(self, other):
        if isinstance(other, GroundingFunction):
            return Feature(function=lambda *args, **kwargs: self.namewrapped_function(*args, **kwargs) * other.namewrapped_function(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Feature(function=lambda *args, **kwargs: self.namewrapped_function(*args, **kwargs) * other)
        raise RLangGroundingError(message=f"Cannot '*' a {type(self)} and a {type(other)}")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, GroundingFunction):
            return Feature(function=lambda *args, **kwargs: self.namewrapped_function(*args, **kwargs) / other.namewrapped_function(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Feature(function=lambda *args, **kwargs: self.namewrapped_function(*args, **kwargs) / other)
        raise RLangGroundingError(message=f"Cannot '/' a {type(self)} and a {type(other)}")

    def __rtruediv__(self, other):
        if isinstance(other, (np.ndarray, int, float)):
            return Feature(function=lambda *args, **kwargs: other / self.namewrapped_function(*args, **kwargs))
        raise RLangGroundingError(message=f"Cannot '/' a {type(other)} and a {type(self)}")

    def __sub__(self, other):
        if isinstance(other, GroundingFunction):
            return Feature(function=lambda *args, **kwargs: self.namewrapped_function(*args, **kwargs) - other.namewrapped_function(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Feature(function=lambda *args, **kwargs: self.namewrapped_function(*args, **kwargs) - other)
        raise RLangGroundingError(message=f"Cannot '-' a {type(self)} and a {type(other)}")

    def __rsub__(self, other):
        if isinstance(other, (np.ndarray, int, float)):
            return Feature(function=lambda *args, **kwargs: other - self.namewrapped_function(*args, **kwargs))
        raise RLangGroundingError(message=f"Cannot '-' a {type(other)} and a {type(self)}")

    def __add__(self, other):
        if isinstance(other, GroundingFunction):
            return Feature(function=lambda *args, **kwargs: self.namewrapped_function(*args, **kwargs) + other.namewrapped_function(*args, **kwargs))
        if isinstance(other, (np.ndarray, int, float)):
            return Feature(function=lambda *args, **kwargs: self.namewrapped_function(*args, **kwargs) + other)
        raise RLangGroundingError(message=f"Cannot '+' a {type(self)} and a {type(other)}")
    
    def __getitem__(self, item):
        # If item is a slice, we convert it to a list or tuple, otherwise we just pass it through to get_factor_from_indexer
        if isinstance(item, slice):
            # Error checking if the slice has negative values
            if item.start < 0 or item.stop < 0 or (item.step and item.step < 0):
                raise RLangGroundingError(f"Cannot slice factor with negative parameter, {item}")

            if item.step: # slice case with step, we need to return a list of factors
                return Factor(list(range(item.start, item.stop, item.step)))
            else: # slice case without step, we return a start and end index
                return Factor((item.start, item.stop))
       
        elif isinstance(item, int):
            return Factor(item)

        else:
            #Maybe not a ValueError
            raise ValueError(f"Cannot slice GroundingFunction with given type {type(item)}") 

        if not isinstance(item, (int, slice)):
            raise RLangGroundingError(f"Cannot index {type(self)} with type {type(item)}")
        
        return Feature(function=lambda *args, **kwargs: self.namewrapped_function(*args, **kwargs)[item])

    def __radd__(self, other):
        return self.__add__(other)
    
    # We may need to test this empirically to see if we should be using 'and' or '&' (bitwise)
    def __and__(self, other):
        if isinstance(other, GroundingFunction):
            return Proposition(function=lambda *args, **kwargs: self.namewrapped_function(*args, **kwargs) and other.namewrapped_function(*args, **kwargs))
        if isinstance(other, bool):
            return Proposition(function=lambda *args, **kwargs: self.namewrapped_function(*args, **kwargs)) if other else Proposition.FALSE
        raise RLangGroundingError(message=f"Cannot 'and' a {type(self)} with a {type(other)}")

    def __rand__(self, other):
        return self.__and__(other)

    def __or__(self, other):
        if isinstance(other, GroundingFunction):
            print("This is called", self, other)
            def smart_or_function(*args, **kwargs):
                try:
                    r1 = self.namewrapped_function(*args, **kwargs)
                    if r1:
                        return True
                except TypeError as e:
                    try:
                        return other.namewrapped_function(*args, **kwargs)
                    except TypeError:
                        raise e
                if not r1:
                    return other.namewrapped_function(*args, **kwargs)
            return Proposition(function=lambda *args, **kwargs: smart_or_function(*args, **kwargs))
        if isinstance(other, bool):
            print("This other is called", self, other)
            return Proposition(function=lambda *args, **kwargs: self.namewrapped_function(*args, **kwargs)) if not other else Proposition.TRUE
        raise RLangGroundingError(message=f"Cannot 'or' a {type(self)} with a {type(other)}")

    def __ror__(self, other):
        return self.__or__(other)
    
    # We may need to test this empirically to see if we should be using '!=' or '^' (bitwise)
    def __xor__(self, other):
        if isinstance(other, GroundingFunction):
            return Proposition(function=lambda *args, **kwargs: self.namewrapped_function(*args, **kwargs) != other.namewrapped_function(*args, **kwargs))
        if isinstance(other, bool):
            return Proposition(function=lambda *args, **kwargs: self.namewrapped_function(*args, **kwargs) != other)
        raise RLangGroundingError(message=f"Cannot '^' a {type(self)} with a {type(other)}")

    def __rxor__(self, other):
        return self.__xor__(other)

    def __invert__(self):
        return Proposition(function=lambda *args, **kwargs: not self(*args, **kwargs))

    def __hash__(self):
        return hash((str(self), self.function))


class Factor(GroundingFunction):
    """Represents a factor of the state space. The state is assumed to be a vector."""

    def __init__(self, state_indexer: Union[int, tuple, list], name: str = None):
        """
        Args:
            state_indexer (optional [int, tuple, list]): the index, tuple, or indices of the *state space*. Must be non-negative. If a tuple, the first element is the start index and the second element is the end index (exclusive).
            name (optional): the name of the grounding.
        """

        # Check whether the state_indexer is valid.
        if isinstance(state_indexer, int):
            if state_indexer < 0:
                raise RLangGroundingError(f"Factor state_indexer must be non-negative, got {state_indexer}")
        elif isinstance(state_indexer, tuple):
            if len(state_indexer) != 2:
                raise RLangGroundingError(f"Factor state_indexer must be a tuple of length 2, got length {len(state_indexer)}")
            elif state_indexer[0] < 0 or state_indexer[1] < 0:
                raise RLangGroundingError(f"Factor state_indexer must be non-negative, got {state_indexer}")
            elif state_indexer[0] > state_indexer[1]:
                raise RLangGroundingError(f"Factor state_indexer must be in increasing order, got {state_indexer}")
        elif isinstance(state_indexer, list):
            if len(state_indexer) == 0:
                raise RLangGroundingError("Factor state_indexer must have length > 0, got empty list")
            elif any([i < 0 for i in state_indexer]):
                raise RLangGroundingError(f"Factor state_indexer must be non-negative, got {state_indexer}")
        else:
            raise RLangGroundingError(f"Invalid state_indexer for Factor (expecting int, tuple, or list): {type(state_indexer).__name__}")
        

        # Convert the state_indexer into a list of indices
        if isinstance(state_indexer, int):
            self.indices = [state_indexer]
        elif isinstance(state_indexer, tuple):
            self.indices = list(range(state_indexer[0], state_indexer[1]))
        else:
            self.indices = state_indexer
    
        super().__init__(function=self.internal_function, name=name if name else f"factor_{fast_uuid()}")
                   

    def internal_function(self, *args, **kwargs):
        if "state" in kwargs:
            state = kwargs["state"]
        else:
            raise RLangGroundingError(f"Factor {self.name} requires a state argument.")
                
        # Create a numpy array or list (based on the type of state) from state given a list of indices
        # This is the meat of the function!
        if any([i >= len(state) for i in self.indices]):
            raise RLangGroundingError(f"Factor {self.name} cannot index state of length {len(state)} with out-of-range indices {self.indices}")
        if isinstance(state, np.ndarray):
            factor_values = state[self.indices]
            if len(factor_values) == 1:
                return factor_values[0]
            else:
                return factor_values
        elif isinstance(state, list):
            factor_values = [state[i] for i in self.indices]
            if len(factor_values) == 1:
                return factor_values[0]
            else:
                return factor_values
                    
    def get_factor_from_indexer(self, item):
        """Helper function for indexing a Factor.
        Args:
            item: the index, tuple, or list to index the Factor with.
        Returns:
            A new Factor with the appropriate indices.
        """
        if isinstance(item, int):
            if item >= len(self.indices) or item < 0:
                raise RLangGroundingError(f"Indexing factor of length {len(self.indices)} with out-of-range index {item}")
            # Probably at this point we pass in another function to the Factor constructor that is a function of its variable names.
            # We want to get the item index of the name of this function
            return Factor(state_indexer=self.indices[item])
        elif isinstance(item, tuple):
            if item[0] > item[1] or item[1] > len(self.indices) or item[0] < 0 or len(item) != 2:
                raise RLangGroundingError(f"Indexing factor with ill-formed Tuple, got {item}")
            return Factor(state_indexer=[self.indices[i] for i in range(item[0], item[1])])
        elif isinstance(item, list):
            if len(item) > len(self.indices) or any([i > len(self.indices) or i < 0 for i in item]):
                raise RLangGroundingError(f"Indexing factor of length {len(self.indices)} with out-of-range index in list {[i for i in item if i > len(self.indices) or i < 0]}")
            return Factor(state_indexer=[self.indices[i] for i in item])
        else:
            raise RLangGroundingError(f"Cannot index factor with given object: {type(item).__name__}")

    def __getitem__(self, item):
        # If item is a slice, we convert it to a list or tuple, otherwise we just pass it through to get_factor_from_indexer
        if isinstance(item, slice):
            # Error checking if the slice has negative values
            if item.start < 0 or item.stop < 0 or (item.step and item.step < 0):
                raise RLangGroundingError(f"Cannot slice factor with negative parameter, {item}")

            if item.step: # slice case with step, we need to return a list of factors
                return self.get_factor_from_indexer(list(range(item.start, item.stop, item.step)))
            else: # slice case without step, we return a start and end index
                return self.get_factor_from_indexer((item.start, item.stop))
        
        return self.get_factor_from_indexer(item)

    def __hash__(self):
        return hash(("Factor", self.name, tuple(self.indices))) # Factors referencing the same indices will be hashed together

    def __repr__(self):
        return f"<Factor (\"{self.name}\"): S{self.indices}>"


class Feature(GroundingFunction):
    """Represents a feature of the state space, i.e. any function of the state."""

    def __init__(self, function: Callable, name: str = None):
        """
        Args:
            function: a function of state.
            name (optional): the name of the feature.
        """
        super().__init__(function=function, name=name if name else f"feature_{fast_uuid()}")

    def __hash__(self):
        return hash(("Feature", self.name))

    def __repr__(self):
        return f"<Feature \"{self.name}\">"
    

class MarkovFeature(GroundingFunction):
    """Represents a Grounding that is a function of (state, action, next_state)"""

    def __init__(self, function: Callable, name: str):
        """
        Args:
            function: a function of (state, action, next_state)
            name (optional): the name of the feature.
        """
        super().__init__(function=function, name=name if name else f"markov_feature_{fast_uuid()}")
    
    def __repr__(self):
        return f"<MarkovFeature \"{self.name}\">"


class Proposition(GroundingFunction):
    """Represents a function which has a truth value.

    A Proposition is a feature with a codomain of True or False.
    """

    def __init__(self, function: Callable, name: str = None):
        """
        Args:
            function: a function of state that evaluates to a bool.
            name (optional): the name of the proposition.
        """
        super().__init__(function=function, name=name if name else f"proposition_{fast_uuid()}")

    @classmethod
    def TRUE(cls):
        return cls(function=lambda *args, **kwargs: True)

    @classmethod
    def FALSE(cls):
        return cls(function=lambda *args, **kwargs: False)

    def __hash__(self):
        return hash((str(self), self.function))

    def __repr__(self):
        return f"<Proposition \"{self.name}\">"
    

class Goal(GroundingFunction):
    """Represents a Goal."""

    def __init__(self, function: Callable, name: str = None):
        """
        Args:
            function: a function of state that evaluates to a bool, i.e. whether the goal is reached.
            name (optional): the name of the goal.
        """
        super().__init__(function=function, name=name if name else f"goal_{fast_uuid()}")

    def __hash__(self):
        return hash((str(self), self.function))

    def __repr__(self):
        return f"<Goal \"{self.name}\">"
    

class Predicate(GroundingFunction):
    """Represents a boolean-valued function of an argument (and state [optionally])."""

    def __init__(self, function: Callable, name: str = None):
        """
        Args:
            function: a function of state and an argument that evaluates to a bool.
            name (optional): the name of the predicate.
        """
        super().__init__(function=function, name=name if name else f"predicate_{fast_uuid()}")

    def __repr__(self):
        return f"<Predicate \"{self.name}\">"
    

class ParameterizedSkill(GroundingFunction):
    """Represents a parameterized skill.
    The input would be some task parameter, and the output would be a policy parameter or a primitive action.
    """

    def __init__(self, function: Callable, name: str = None):
        super().__init__(function, name=name if name else f"parameterized-skill_{fast_uuid()}")
    
    def __repr__(self):
        return f"<ParameterizedSkill \"{self.name}\">"
    

class Policy(GroundingFunction):
    """Represents a closed-loop policy function"""

    def __init__(self, function: Callable, name: str = None):
        """
        Args:
            function: a function from states to action distributions.
            name (optional): the name of the policy.
        """
        super().__init__(function=function, name=name if name else f"policy_{fast_uuid()}")

    def __repr__(self):
        return f"<Policy \"{self.name}\">"


class Option(Grounding):
    """Grounding object for an option."""

    def __init__(self, initiation: GroundingFunction, policy: Policy, termination: GroundingFunction, name: str = None):
        # TODO: Re-write documentation here
        """
        Args:
            initiation: A GroundingFunction capturing the initiation set of the option. E.g. Proposition, Goal.
            policy: A Policy capturing the policy of the option.
            termination: A GroundingFunction capturing the termination set of the option. E.g. Proposition, Goal.
            name (optional): the name of the option.
        """
        self.initiation = initiation
        self.termination = termination
        self.policy = policy
        super().__init__(name=name if name else f"option_{fast_uuid()}")

    def __call__(self, *args, **kwargs):
        """Executes the option. It is up to the user to determine whether the option should be terminated."""
        return self.policy(*args, **kwargs)

    def can_initiate(self, *args, **kwargs):
        """Determines whether the option can be executed in a given state.
        Args:
            state: The state.

        Returns:
            bool: True iff the option can be executed in the given state.
        """
        return self.initiation(*args, **kwargs)
    
    def will_terminate(self, *args, **kwargs):
        """Determines whether the option will terminate in a given state.
        Args:
            state: The state.

        Returns:
            bool: True iff the option will terminate in the given state.
        """
        return self.termination(*args, **kwargs)

    def __hash__(self):
        return hash((self.name, self.initiation, self.policy, self.termination))

    def __repr__(self):
        return f"<Option \"{self.name}\" (i:{self.initiation}, pi:{self.policy}, b:{self.termination})>"
    

# class Plan(Grounding):
#     """Represents an open-loop policy"""
#     def __init__(self, function: Callable = None, name: str = None):
#         self.function = function
#         super().__init__(name=name)

#     def reset(self):
#         pass

#     def __call__(self, *args, **kwargs):
#         if self.function is None:
#             raise RLangGroundingError("Plan function is not defined")
#         return self.function(*args, **kwargs)

#     def __repr__(self):
#         if self.name:
#             return f"<Plan \"{self.name}\">"
#         else:
#             return f"<Plan unnamed>"


# class IteratedPlan(Plan):
#     """One kind of plan implementation"""

#     def __init__(self, plan_steps, name: str = None):
#         self.plan_steps = plan_steps
#         super().__init__(function=self.__call__, name=name)
#         self.i = 0

#     def reset(self):
#         self.i = 0
#         for p in self.plan_steps:
#             if isinstance(p, PlanExecution):
#                 p.plan.reset()
#             elif isinstance(p, IteratedPlan):
#                 p.reset()

#     def __call__(self, *args, **kwargs):
#         if self.i >= len(self.plan_steps):
#             return None
#         action = self.plan_steps[self.i]
#         # print(action)
#         if isinstance(action, PlanExecution):
#             next_action = action(*args, **kwargs)
#             if next_action is None:
#                 action.plan.reset()
#                 self.i += 1
#                 return self(*args, **kwargs)
#             else:
#                 return next_action
#         else:
#             # print(action)
#             # print(type(action))
#             # print(self.i)
#             # print(action(*args, **kwargs))
#             self.i += 1
#             # if isinstance(action, ActionDistribution):
#             #     print("returning")
#             #     return action
#             # else:
#             return action(*args, **kwargs)

#     def __repr__(self):
#         if self.name:
#             return f"<IteratedPlan \"{self.name}\">"
#         else:
#             return f"<IteratedPlan unnamed>"


# class PlanExecution(GroundingFunction):
#     def __init__(self, plan, arguments: List[GroundingFunction]=None):
#         self.plan = plan
#         if arguments is None:
#             arguments = []
#         self.arguments = arguments

#         domain = Domain.ANY
#         for arg in arguments:
#             domain = domain + arg.domain

#         argnames = ", ".join([arg.name if arg.name is not None else "unk" for arg in arguments])

#         super().__init__(domain=domain, codomain=Domain.ACTION,
#                          function=lambda *args, **kwargs:
#                          self.plan(*[arg(*args, **kwargs) for arg in self.arguments], **kwargs),
#                          name=plan.name + "(" + argnames + ")")

#     def __repr__(self):
#         return f"<PlanExecution of {self.plan} with {self.arguments}>"

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


class TransitionFunction(GroundingFunction):
    """Represents a transition function."""

    def __init__(self, function: Callable, name: str = None):
        """
        Args:
            function: a function of state and action that returns a (distribution over) next states.
            name (optional): the name of the transition function.
        """
        super().__init__(function=function, name=name if name else f"transition-function_{fast_uuid()}")

    def __repr__(self):
        return f"<TransitionFunction \"{self.name}\">"
    

class RewardFunction(GroundingFunction):
    """Represents a reward function."""

    def __init__(self, function: Callable, name: str = None):
        """
        Args:
            function: a function of state and action that returns a (distribution over) rewards.
            name (optional): the name of the reward function.
        """
        super().__init__(function=function, name=name if name else f"reward-function_{fast_uuid()}")

    def __repr__(self):
        return f"<RewardFunction \"{self.name}\">"
    
class ValueFunction(GroundingFunction):
    """Represents a value function."""
    # TODO: We may want to include a marker to indicate whether the value function is a state value function or a state-action value function

    def __init__(self, function: Callable, name: str = None):
        """
        Args:
            function: a function of state (and action [optionally]) that returns a (distribution over) values.
            name (optional): the name of the value function.
        """
        super().__init__(function=function, name=name if name else f"value-function_{fast_uuid()}")

    def __repr__(self):
        return f"<ValueFunction \"{self.name}\">"


class Prediction(GroundingFunction):
    """Represents a prediction of the value of another GroundingFunction.

    Used to express the predicted value of another RLang object.
    Limited to GroundingFunctions with a domain of (S) or (S, A).
    """

    def __init__(self, grounding: GroundingFunction, function: Callable, name: str = None):
        """
        Args:
            grounding (GroundingFunction): the grounding whom's value we are predicting
            function: a function that predicts the value of grounding
            name (Optional[str]): the name of the prediction
        """
        self.grounding = grounding
        super().__init__(function=function, name=name if name else f"prediction_{fast_uuid()}")

    def __repr__(self):
        return f"<Prediction \"{self.name}\" for Grounding \"{self.grounding.name}\">"


class Effect(Grounding):
    """Represents the effect of an action.

    Contains an optional list of RewardFunctions, ValueFunctions, TransitionFunctions, and Predictions.
    """

    def __init__(self, reward_functions: List[RewardFunction] = [], value_functions: List[ValueFunction] = [], transition_functions: List[TransitionFunction] = [],
                 predictions: List[Prediction] = [], name: str = None):
        """
        Args:
            reward_functions: a list of RewardFunctions.
            value_functions: a list of ValueFunctions.
            transition_functions: a list of TransitionFunctions.
            predictions: a list of Predictions.
            name (optional): the name of the effect.
        """
        self.reward_functions = reward_functions
        self.value_functions = value_functions
        self.transition_functions = transition_functions
        self.predictions = predictions
        super().__init__(name=name if name else f"effect_{fast_uuid()}")

    # def compose_probabilities(self, probability: float):
    #     self.probability = self.probability * probability
    #     if self.reward_function:
    #         self.reward_function = RewardFunction.from_reward_distribution(
    #             RewardDistribution({self.reward_function: probability}))
        # if self.transition_function:
        #     self.transition_function = TransitionFunction.from_state_distribution(
        #         StateDistribution({self.transition_function: probability}))
    #     new_predictions = list()
    #     for p in self.predictions:
    #         new_predictions.append(
    #             Prediction.from_grounding_distribution(p.grounding,
    #                                                    GroundingDistribution(p.grounding, {p: probability}),
    #                                                    complete=p.complete))
    #     self.predictions = new_predictions

    # @property
    # def prediction_dict(self):
    #     prediction_dict = defaultdict(list)
    #     for p in self.predictions:
    #         # print(prediction_dict[p.grounding.name])
    #         prediction_dict[p.grounding.name].append(p)
    #     return dict(prediction_dict)

    def __repr__(self):
        return f"<Effect \"{self.name}\">"



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
