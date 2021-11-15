from __future__ import annotations
from typing import Callable
from collections.abc import MutableMapping

from rlang.src.exceptions import RLangGroundingError
from rlang.src.grounding.internals import State, Domain, MDPMetadata
from rlang.src.grounding.groundings import Grounding, GroundingFunction, Factor, RewardFunction, TransitionFunction, \
    Feature, Proposition, ProbabilisticFunction, MarkovFeature


class RLangKnowledge(MutableMapping):
    """Acts as a container for Groundings.

        Acts just like a Python dictionary.

        Attributes:
            reward_function: RewardFunction
                A partial specification of the reward function
            transition_function: TransitionFunction
                A partial specification of the transition function

        Examples:
            .. code-block:: python

                base = RLangKnowledge()
                base['x_location'] = Factor([1])

    """

    def __init__(self):
        self.rlang_variables = dict()
        # self.reward_function = None
        # self.transition_function = None
        # self.predictions = dict()
        self.mdp_metadata = None

    # def parse(self, rlang: str):
    #     self = parse(rlang, prior_knowledge=self)
    #
    # def parse_file(self, rlang_fname: str):
    #     self = parse_file(rlang_fname, prior_knowledge=self)

    @property
    def reward_function(self):
        return self.reward_function

    @reward_function.setter
    def reward_function(self, function: RewardFunction):
        self.reward_function = function

    @property
    def transition_function(self):
        return self.transition_function

    @transition_function.setter
    def transition_function(self, function: TransitionFunction):
        self.transition_function = function

    @property
    def predictions(self):
        return self.predictions

    @predictions.setter
    def predictions(self, new_predictions: dict):
        self.predictions = new_predictions

    def full_predictions(self, *args, **kwargs):
        """

        Args:
            state: State, optional
            action: Action, optional

        Returns:
            dict: A dictionary containing all GroundingFunctions which can be predicted for the next state
        """
        # TODO: This breaks after migrating to probabilistic functions. Fix this somehow.
        next_state = self.transition_function(*args, **kwargs)
        if next_state is not None:
            domain = Domain.NEXT_STATE
            if 'state' in kwargs.keys():
                domain += Domain.STATE
            if 'action' in kwargs.keys():
                domain += Domain.ACTION

            # Collect the variables with the proper domain
            vars = list(filter(lambda x: isinstance(x, (
                Factor, Feature, MarkovFeature, Proposition, ProbabilisticFunction)) and x.domain <= domain,
                               list(self.values())))
            # Augment the function for each GroundingFunction to automatically take next_state
            for v in vars:
                def lambda_generator(function):
                    def the_lambda(*args, **kwargs):
                        if 'next_state' in kwargs:
                            if not kwargs['next_state'].unbatched_eq(next_state):
                                raise RLangGroundingError("Transition function conflict")
                            return function(*args, **kwargs)
                        else:
                            return function(*args, **kwargs, next_state=next_state)
                    return the_lambda
                v.function = lambda_generator(v.function)
            # Construct a dictionary and return it
            var_names = list(map(lambda x: x.name, vars))
            available_variables = dict(zip(var_names, vars))
            return available_variables
        else:
            return self.predictions

    def __getitem__(self, key: str):
        return self.rlang_variables[key]

    def __setitem__(self, key: str, value: Grounding):
        self.rlang_variables[key] = value

    def __delitem__(self, key: str):
        del self.rlang_variables[key]

    def __iter__(self):
        return iter(self.rlang_variables)

    def __len__(self):
        return len(self.rlang_variables)

    def factors(self):
        # TODO: I don't understand why this doesn't work
        return dict(tuple(filter(lambda a: isinstance(a[1], Factor), self.__iter__())))
