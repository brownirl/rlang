from lmdp.utils.expression_utils import Domain, Codomain


class Expression:
    def __init__(self, fun, domain=[], codomain=[]):
        self._fun = fun
        self._domain = Domain(domain)
        self._codomain = Codomain(codomain)    
    
    def __call__(self, *args, **kwargs):
        # if(not self.is_in_domain(args)):
        #     raise "Error: Wrong Arguments. Domain: " + str(self._domain)
        if(len(kwargs) != 0):
            fun_args = dict([(d, kwargs[d]) for d in self.domain()])
        else:
            fun_args = dict(zip(self.domain(), args))
        return self._fun(**fun_args)
    
    @property
    def domain(self):
        return self._domain
    @property
    def codomain(self):
        return self._codomain
