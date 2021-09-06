"""
    Grounded Function Specification Class
        - Represents function specification, with a given domain-codomain,
        in the form of a function by parts.
        - Implemented as Pairs of (boolean expressions, function).
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu), Benjamin Spiegel
    (bspiegel@cs.brown.edu)
    date: January 2021, August 2021
"""

from rlang.src.grounding.knowledge_grounding import Grounding
from rlang.src.grounding.utils.domain import Domain


class GroundingFunction(Grounding):

    def __init__(self, domain: Domain, codomain: Domain, name: str = None):
        super().__init__(name)
        self._domain = domain
        self._codomain = codomain
