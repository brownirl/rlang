import sys, os
sys.path.append(os.path.abspath("./"))

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

    # def __eq__(self, other):
    #     if(isinstance(other, Expression)):
    #         return Expression(lambda **args: self.__call__(*args) == other(**args), domain=self.domain() + other.domain(), codomain=["boolean"])
    #     else:
    #         return NotImplemented


state = Expression(lambda state: state, domain=["state"], codomain=["state"])
action = Expression(lambda action: action, domain=["action"], codomain=["action"])
state_prime = Expression(lambda next_state: next_state, domain=["next_state"], codomain=["state"])
 