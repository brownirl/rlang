"""
    Option Class
        -
    author: Benjamin Spiegel (bspiegel@cs.brown.edu), Jennifer Wang
    date: August 2021
"""

from grounding.knowledge_grounding import Grounding
from grounding.utils.domain import Domain
from grounding.groundings.state.policy import Policy
from grounding.groundings.state.predicate import Predicate


class Option(Grounding):

    def __init__(self, initiation: Predicate, policy: Policy, termination: Predicate, name: str = None):
        self._initiation = initiation
        self._policy = policy
        self._termination = termination
        super().__init__(name)

