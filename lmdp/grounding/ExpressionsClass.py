from lmdp.grounding.GroundingClass import Domain

class Codomain:
    CODOMAINS = {0: "State", 
                 1: "Action", 
                 2: "Next State",
                 3: "Set of States",
                 4: "Set of Actions/Options",
                 5: "Real",
                 6: "Transitions",
                 7: "Rewards",
                 8: "Values",
                 9: "Policy",
                 10: "Boolean"}

    INV_CODOMAINS = dict(zip(CODOMAINS.values(), CODOMAINS.keys()))
    def __init__(self, codomain):
        self._codomain = set([Codomain.INV_CODOMAINS[d] for d in codomain])

    def __str__(self):
        if (len(self._codomain) == 0):
            return "[]"
        else:
            d = [Codomain.CODOMAINS[d] for d in sorted(list(self._codomain))]
            return ", ".join(d)
    def __call__(self):
        return [Codomain.CODOMAINS[d] for d in self._codomain]


class Expression:
    def __init__(self, fun, domain=[], codomain=[]):
        self._fun = fun
        self._domain = Domain(domain)
        self._codomain = Codomain(codomain)    
    def __call__(self, *args):
        # if(not self.is_in_domain(args)):
        #     raise "Error: Wrong Arguments. Domain: " + str(self._domain)
        return self._fun(*args)
    def domain(self):
        return self._domain.domain()

    def codomain(self):
        return self._codomain()
