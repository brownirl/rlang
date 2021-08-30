"""
    Grounded Function Specification Class
        - Represents function specification, with a given domain-codomain,
        in the form of a function by parts.
        - Implemented as Pairs of (boolean expressions, function).
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu), Benjamin Spiegel (bspiegel@cs.brown.edu)
    date: January 2021, August 2021
"""

from grounding.knowledge_grounding import Grounding
from grounding.utils.domain import Domain


class GroundingFunction(Grounding):

    def __init__(self, domain: Domain, codomain: Domain, name: str = None):
        super().__init__(name)
        self._domain = domain
        self._codomain = codomain

        # self.specification = []  # list of (boolean, expression) specification

    # def __call__(self, *args):
    #     r = []
    #     for spec in self.specification:
    #         bs, fs = spec[0](*args), spec[1](*args)
    #         r.append((bs, fs))
    #     return r
    #
    # def add_specification(self, boolean_cond, function):
    #     if (
    #             boolean_cond.domain <= self.domain and self.codomain == function.codomain and function.domain <= self.domain):
    #         self.specification.append((boolean_cond, function))
    #     elif self.domain == boolean_cond.domain:
    #         raise "Domains are not compatible: " + str(self.domain) + "~=" + str(boolean_cond.domain)
    #     else:
    #         raise "Codomains are not compatible: " + str(self.codomain) + "~=" + str(
    #             boolean_cond.codomain) + " or " + str(self.codomain) + "~=" + str(function.codomain)
