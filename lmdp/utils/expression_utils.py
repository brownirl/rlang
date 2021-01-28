
class Domain:
    DOMAINS = {0: "state", 1: "action", 2: "next_state"}
    INV_DOMAINS = dict(zip(DOMAINS.values(), DOMAINS.keys()))
    def __init__(self, domain):
        self._domain = set([Domain.INV_DOMAINS[d] for d in domain])
    
    def __call__(self):
        return [Domain.DOMAINS[d] for d in self._domain]
    
    def __str__(self):
        if (len(self._domain) == 0):
            return "[]"
        else:
            d = [Domain.DOMAINS[d] for d in sorted(list(self._domain))]
            return ",".join(d)

    def __eq__(self, other):
        if (isinstance(other, Domain)):
            return (self._domain <= other._domain) and (other._domain <= self._domain)
        elif(isinstance(other, Codomain)):
            return (self._domain <= other._codomain) and (other._codomain <= self._domain)
        return NotImplemented

    def __le__(self, other):
        if (isinstance(other, Domain)):
            return (self._domain <= other._domain)
        elif(isinstance(other, Codomain)):
            return (self._domain <= other._codomain)
        return NotImplemented


    def is_sa(self):
        return 0 in self._domain and 1 in self._domain and 2 not in self._domain

    def is_sas(self):
        return 0 in self._domain and 1 in self._domain and 2 in self._domain

    def is_s(self):
        return 0 in self._domain and 1 not in self._domain and 2 not in self._domain

    def is_a(self):
        return 0 not in self._domain and 1 in self._domain and 2 not in self._domain

    def is_ss(self):
        return 0 in self._domain and 1 not in self._domain and 2 in self._domain

class Codomain:
    CODOMAINS = {0: "state", 
                 1: "action", 
                 2: "next_state",
                 3: "set_of_states",
                 4: "set_of_actions",
                 5: "real",
                 6: "transition",
                 7: "reward",
                 8: "value",
                 9: "policy",
                 10: "boolean"}

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

    def __eq__(self, other):
        if(isinstance(other, Codomain)):
            return self._codomain <= other._codomain and other._codomain <= self._codomain
        elif(isinstance(other, Domain)):
            return self._codomain <= other._domain and other._domain <= self._codomain
        else:
            return NotImplemented

    def __leq__(self, other):
        if(isinstance(other, Codomain)):
            return self._codomain <= other._codomain
        elif(isinstance(other, Domain)):
            return self._codomain <= other._domain
        else:
            return NotImplemented

if __name__ == "__main__":
    d1 = Domain(["state", "action"])
    d2 = Domain(["state", "next_state", "action"])
    d3 = Domain(["state", "action", "next_state"])

    print(d1)
    print(d2)
    print(d3)

    assert (d2 == d3)
    assert not d2 == d1
    assert d1 <= d2
