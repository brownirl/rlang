class Domain:
    DOMAINS = {0: "state", 1: "action", 2: "next_state"}
    DOMAINS_repr = {0: "S", 1: "A", 2: "S'"}
    INV_DOMAINS = dict(zip(DOMAINS.values(), DOMAINS.keys()))

    def __init__(self, domain):
        self._domain = set([Domain.INV_DOMAINS[d] for d in domain])

    def __call__(self):
        return [Domain.DOMAINS[d] for d in self._domain]

    def __str__(self):
        if len(self._domain) == 0:
            return "[]"
        else:
            d = [Domain.DOMAINS[d] for d in sorted(list(self._domain))]
            return ",".join(d)

    def __eq__(self, other):
        if isinstance(other, Domain):
            return (self._domain <= other._domain) and (other._domain <= self._domain)
        elif isinstance(other, Codomain):
            return (self._domain <= other._codomain) and (other._codomain <= self._domain)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Domain):
            return self._domain <= other._domain
        elif isinstance(other, Codomain):
            return self._domain <= other._codomain
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Domain):
            return self._domain >= other._domain
        elif isinstance(other, Codomain):
            return self._domain >= other._codomain
        return NotImplemented

    def __len__(self):
        return len(self._domain)

    def __sub__(self, other):
        return set(self.__call__()) - set(other.__call__())

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

    def __repr__(self):
        if len(self._domain) == 0:
            return ""
        else:
            d = [Domain.DOMAINS_repr[d] for d in sorted(list(self._domain))]
            return " x ".join(d)


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
    CODOMAINS_repr = {0: "S",
                      1: "A",
                      2: "S'",
                      3: "2^S",
                      4: "2^A",
                      5: "R",
                      6: "T",
                      7: "Rew",
                      8: "V",
                      9: "pi",
                      10: "{T, F}"}

    INV_CODOMAINS = dict(zip(CODOMAINS.values(), CODOMAINS.keys()))

    def __init__(self, codomain):
        self._codomain = set([Codomain.INV_CODOMAINS[d] for d in codomain])

    def __str__(self):
        if len(self._codomain) == 0:
            return "[]"
        else:
            d = [Codomain.CODOMAINS[d] for d in sorted(list(self._codomain))]
            return ", ".join(d)

    def __call__(self):
        return [Codomain.CODOMAINS[d] for d in self._codomain]

    def __eq__(self, other):
        if isinstance(other, Codomain):
            return self._codomain <= other._codomain and other._codomain <= self._codomain
        elif isinstance(other, Domain):
            return self._codomain <= other._domain and other._domain <= self._codomain
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, Codomain):
            return self._codomain <= other._codomain
        elif isinstance(other, Domain):
            return self._codomain <= other._domain
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Codomain):
            return self._codomain >= other._codomain
        elif isinstance(other, Domain):
            return self._codomain >= other._domain
        else:
            return NotImplemented

    def __len__(self):
        return len(self._codomain)

    def __repr__(self):
        if len(self._codomain) == 0:
            return ""
        else:
            d = [Codomain.CODOMAINS_repr[d] for d in sorted(list(self._codomain))]
            return " x ".join(d)


if __name__ == "__main__":
    d1 = Domain(["state", "action"])
    d2 = Domain(["state", "next_state", "action"])
    d3 = Domain(["state", "action", "next_state"])

    print(repr(d1))
    print(repr(d2))
    print(repr(d3))

    assert (d2 == d3)
    assert not d2 == d1
    assert d1 <= d2
