'''
    Expression Class
        This is a wrapper for functions with domain and codomains
        pertinent to MDPs
        - It allows to verify domains and to map arguments correctly
        - It allows function composition
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: January 2021
'''

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
        if(len(args) == 1 and isinstance(args[0], Expression)):
            return self.__compose__(args[0])

        if(len(kwargs) != 0):
            fun_args = dict([(d, kwargs[d]) for d in self.domain()])
        else:
            fun_args = dict(zip(self.domain(), args))
        return self._fun(**fun_args)
    
    def __compose__(self, expression):
        if(self.domain == expression.codomain): #composable
            return Expression(lambda **args: self.__call__(expression(**args)), domain=expression.domain(), codomain=self.codomain())
        else:
            return NotImplemented

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


S = Expression(lambda state: state, domain=["state"], codomain=["state"])
A = Expression(lambda action: action, domain=["action"], codomain=["action"])
S_prime = Expression(lambda next_state: next_state, domain=["next_state"], codomain=["state"])
