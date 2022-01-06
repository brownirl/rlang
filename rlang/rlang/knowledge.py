from __future__ import annotations
from typing import Callable
from collections.abc import MutableMapping

from .grounding.utils.utils import Domain
from .grounding.groundings import *


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
        self.policy = None
        self.reward_function = None
        self.transition_function = None
        self.proto_predictions = list()
        self.mdp_metadata = None

    def predictions(self, *args, **kwargs):
        """

        Args:
            state: State, optional
            action: Action, optional

        Returns:
            dict: A dictionary containing all GroundingFunctions which can be predicted for the next state
        """
        # TODO: This breaks after migrating to probabilistic functions. Fix this somehow.

        domain = Domain.ANY
        if 'state' in kwargs.keys():
            domain += Domain.STATE
        if 'action' in kwargs.keys():
            domain += Domain.ACTION
        if 'next_state' in kwargs.keys():
            domain += Domain.NEXT_STATE
        else:
            next_state = self.next_state(*args, **kwargs)
            if next_state:
                domain += Domain.NEXT_STATE
                kwargs['next_state'] = next_state

        predictables = list(filter(lambda x: x.domain <= domain, self.proto_predictions))

        predictions = dict()
        for p in predictables:
            predictions[p.grounding] = p(*args, **kwargs)

        return predictions

    def next_state(self, *args, **kwargs):
        if self.transition_function:
            return self.transition_function(*args, **kwargs)
        else:
            return dict()

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

    def rlang_variables_of_type(self, grounding_type):
        return {k: v for (k, v) in self.rlang_variables.items() if isinstance(v, grounding_type)}

    def factors(self):
        return self.rlang_variables_of_type(Factor)

    def features(self):
        return self.rlang_variables_of_type(Feature)

    def propositions(self):
        return self.rlang_variables_of_type(Proposition)

    def policies(self):
        return self.rlang_variables_of_type(Policy)

    def effects(self):
        return self.rlang_variables_of_type(Effect)
