"""Every RLang program (including any vocabulary files) grounds to an :py:class:`.RLangKnowledge` object."""

from __future__ import annotations
from typing import Dict, Any
from collections.abc import MutableMapping

from .grounding.utils.utils import Domain
from .grounding.utils.primitives import MDPObjectClass
from .grounding import MDPObjectGrounding


class RLangKnowledge(MutableMapping):
    """Provides an interface for accessing stored RLang information. Behaves similarly to a Python dictionary.

    .. note::
        In typical usage, an :py:class:`.RLangKnowledge` object is not instantiated by the user
        but is instead returned from a call to :py:func:`.parse_file` or :py:func:`.parse`.

    Examples::

        base = RLangKnowledge()
        base['x_location'] = Factor([1])

    """

    def __init__(self):
        self.rlang_variables = dict()
        self.policy = None
        """A :py:class:`.Policy` object"""
        self.reward_function = None
        """A :py:class:`.RewardFunction` object"""
        self.transition_function = None
        """A :py:class:`.TransitionFunction` object"""
        self.proto_predictions = list()
        self.mdp_metadata = None

    def predictions(self, *args, **kwargs) -> Dict[Grounding, Any]:
        """Get a dictionary of :py:class:`.Grounding` objects whose value for the next state
        can be predicted using the keyword arguments provided.

        Args:
            state (Optional[State]): a given current state
            action (Optional[Action]): a given action

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
            next_state = self.get_next_state(*args, **kwargs)
            if next_state:
                domain += Domain.NEXT_STATE
                kwargs['next_state'] = next_state

        predictables = list(filter(lambda x: x.domain <= domain, self.proto_predictions))

        predictions = dict()
        for p in predictables:
            predictions[p.grounding] = p(*args, **kwargs)

        return predictions

    def get_next_state(self, *args, **kwargs):
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
        """:meta private:"""
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

    def classes(self):
        return {k: v for (k, v) in self.rlang_variables.items() if isinstance(v, type) and issubclass(v, MDPObjectClass)}

    def objects(self):
        return self.rlang_variables_of_type(MDPObjectGrounding)
