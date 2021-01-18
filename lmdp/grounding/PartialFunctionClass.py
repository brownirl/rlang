'''
    Partial Function Specification Class
        - Represents function specification, with a given domain-codomain, 
        in the form of a function by parts. 
        - Implemented as Pairs of (boolean expressions, function).
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: January 2021
'''
from lmdp.utils.expression_utils import Domain, Codomain

class PartialFunction:

    def __init__(self, domain=[], codomain=[]):
        self.specification = [] # list of (boolean, function) specification
        self.domain = Domain(domain)
        self.codomain = Codomain(codomain)

    def __call__(self, *args):
        r = []
        for spec in self.specification:
            if spec[0](*args):
                r.append(spec[2](*args))
        return r

    def add_specification(self, boolean_cond, function):
        if (boolean_cond.domain <= self.domain  and self.codomain == function.codomain and function.domain <= self.domain):
            self.specification.append((boolean_cond, function))
        elif (self.domain == boolean_cond.domain):
            raise "Domains are not compatible: " + str(self.domain) + "~=" + str(boolean_cond.domain)
        else:
            raise "Codomains are not compatible: " + str(self.codomain) + "~=" + str(boolean_cond.codomain) + " or " + str(self.codomain) + "~=" + str(function.codomain)