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
        self.store = dict()
        self._reward_function = RewardFunction(reward=0)
        self._transition_function = TransitionFunction()
        self._predictions = dict()
        self._mdp_metadata = None

    # def parse(self, rlang: str):
    #     self = parse(rlang, prior_knowledge=self)
    #
    # def parse_file(self, rlang_fname: str):
    #     self = parse_file(rlang_fname, prior_knowledge=self)

    @property
    def reward_function(self):
        return self._reward_function

    @reward_function.setter
    def reward_function(self, function: RewardFunction):
        self._reward_function = function

    @property
    def transition_function(self):
        return self._transition_function

    @transition_function.setter
    def transition_function(self, function: TransitionFunction):
        self._transition_function = function

    @property
    def predictions(self):
        return self._predictions

    @predictions.setter
    def predictions(self, new_predictions: dict):
        self._predictions = new_predictions

    @property
    def mdp_metadata(self):
        return self._mdp_metadata

    @mdp_metadata.setter
    def mdp_metadata(self, mdp_metadata: MDPMetadata):
        self._mdp_metadata = mdp_metadata

    def full_predictions(self, *args, **kwargs):
        """

        Args:
            state: State, optional
            action: Action, optional

        Returns:
            dict: A dictionary containing all GroundingFunctions which can be predicted for the next state
        """
        # TODO: This breaks after migrating to probabilistic functions. Fix this somehow.
        next_state = self._transition_function(*args, **kwargs)
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
            return self._predictions

    def __getitem__(self, key: str):
        return self.store[key]

    def __setitem__(self, key: str, value: Grounding):
        self.store[key] = value

    def __delitem__(self, key: str):
        del self.store[key]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

    def factors(self):
        # TODO: I don't understand why this doesn't work
        return dict(tuple(filter(lambda a: isinstance(a[1], Factor), self.__iter__())))
