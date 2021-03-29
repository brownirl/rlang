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
    def __init__(self, fun, domain=[], codomain=[], name=None):
        self._fun = fun
        self._domain = Domain(domain)
        self._codomain = Codomain(codomain)    
        self._name = name
    
    def __call__(self, *args, **kwargs):
        fun_args = self.__get_arguments(args, kwargs)
        return self._fun(**fun_args)

    def __verify_arguments(self, kwords):
        return self.domain == kwords.keys()

    def __get_arguments(self, args, kwords):
        matched_args = []
        args_names = self.domain()
        if len(self.domain()) <= len(args):
            return dict(zip(self.domain(), args))
        elif len(args) > 0:
           for i in range(len(args)):
               matched_args.append((args_names[i], args[i])) # match positional arguments
        for i in range(len(args), len(args_names)): # search for remaining arguments in kwords
            if(kwords[args_names[i]] is not None):
                matched_args.append((args_names[i], kwords[args_names[i]]))
            else:
                raise ValueError("Missing Function Argument: " + args_names[i])
        return dict(matched_args)

    def __matmul__(self, expression): # function composition operator
        if(isinstance(expression, Expression)):
            return self.__compose__(expression)

    def __eq__(self, expression):
        if(isinstance(expression, Expression) and expression.codomain == self.codomain):
            return Expression(lambda **args: expression(**args) == self.__call__(**args), 
                                        domain=self.domain()+expression.domain(),
                                        codomain=["boolean"])
        else:
            return Expression(lambda **args: expression == self.__call__(**args), 
                                        domain=self.domain(),
                                        codomain=["boolean"])

    def __compose__(self, expression):

        if(self.domain >= expression.codomain): #composable
            def composed_function(*args, **kwargs):
                args = expression.__get_arguments(args, kwargs)
                new_args = expression(**args)
                if len(expression.codomain()) == 1:
                    new_args = [new_args]
                new_named_args = dict(zip(expression.codomain(), new_args))

                for a in (self.domain - expression.codomain):
                    new_named_args[a] = args[a]
                return self.__call__(**new_named_args)

            # return Expression(lambda **args: self.__call__(expression(**args)), domain=expression.domain(), codomain=self.codomain())
            return Expression(composed_function, domain = set(self.domain()+expression.domain()) , codomain=self.codomain())
        else:
            return NotImplemented

    @property
    def domain(self):
        return self._domain
    @property
    def codomain(self):
        return self._codomain

    def __repr__(self):
        if self._name is None:
            return "(exp: " + repr(self.domain) + "->" + repr(self.codomain) + ")"
        else: 
            return self._name

def rlang_exp(domain, codomain):
    def __rlang_exp(func):
        return Expression(func, domain=domain, codomain=codomain, name=func.__name__)
    return __rlang_exp

S = Expression(lambda state: state, domain=["state"], codomain=["state"], name="s")
A = Expression(lambda action: action, domain=["action"], codomain=["action"], name="a")
S_prime = Expression(lambda next_state: next_state, domain=["next_state"], codomain=["state"], name="s'")
