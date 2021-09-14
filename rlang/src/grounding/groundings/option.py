"""
    Option Class
        -
    author: Benjamin Spiegel (bspiegel@cs.brown.edu)
    date: September 2021
"""

from typing import Union
from rlang.src.grounding.knowledge_grounding import Grounding
from rlang.src.grounding.utils.state_action_implementation import State
from rlang.src.grounding.groundings.state.policy import Policy
from rlang.src.grounding.groundings.state.predicate import Predicate


class Option(Grounding):

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
        return self._initiation(*args, **kwargs)
