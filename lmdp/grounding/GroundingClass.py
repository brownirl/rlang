"""
    Abstract class for grounding names to MDPs
    Author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    Date: August 2020
"""

class Domain:
    DOMAINS = {0: "State", 1: "Action", 2: "Next State"}
    INV_DOMAINS = dict(zip(DOMAINS.values(), DOMAINS.keys()))
    def __init__(self, domain):
        self._domain = set([Domain.INV_DOMAINS[d] for d in domain])

    def __str__(self):
        if (len(self._domain) == 0):
            return "[]"
        else:
            d = [Domain.DOMAINS[d] for d in sorted(list(self._domain))]
            return ",".join(d)

    def domain(self):
        return [Domain.DOMAINS[d] for d in self._domain]



class Grounding(object):
    def __init__(self, name=None, domain=[]):
        self._name = name
        self._domain = set(domain)

    @property
    def name(self):
        return self._name
    

    # def __hash__(self):
    #     return self.name.__hash__()