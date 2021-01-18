from lmdp.utils.expression_utils import Domain, Codomain


class Expression:
    def __init__(self, fun, domain=[], codomain=[]):
        self._fun = fun
        self._domain = Domain(domain)
        self._codomain = Codomain(codomain)    
    def __call__(self, *args):
        # if(not self.is_in_domain(args)):
        #     raise "Error: Wrong Arguments. Domain: " + str(self._domain)
        return self._fun(*args)
    
    @property
    def domain(self):
        return self._domain
    @property
    def codomain(self):
        return self._codomain
