'''
    Conditional Expression Class:
        - It allows to create a statement of the form 
        when (Boolean Expression) then:
            <expressions>
        otherwise:
            <expressions>

    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: January 2021
'''

import sys, os
sys.path.append(os.path.abspath("./"))
from collections import deque
from functools import reduce
from lmdp.grounding.expressions.ExpressionsClass import Expression
from lmdp.grounding.booleans.BooleanFunClass import BooleanExpression, any_state, any_action
from lmdp.grounding.actions.SubpolicyClass import Subpolicy
from lmdp.grounding.states.Effect import Effect
from lmdp.grounding import *

class Conditional:
    def __init__(self, boolean_expression, lmdp=None):
        self._boolean_expression = boolean_expression
        self.lmdp = lmdp
        self.conditional_stack = deque([boolean_expression])
        self.contexts = deque()
        # definitions
        self.subpolicies = {}
        self.state_features = {}
        self.symbols = {}
        self.markov = {}

        # partial functions
        self.transition_elements = []
        self.reward_elements = []
        self.value_elements = []
        self.policy_elements = []

    def __enter__(self):  
        self._boolean_expression = reduce(lambda a, b: a & b, self.conditional_stack)
        self.contexts.append(self._boolean_expression)
        return self

    def __exit__(self, type, value, traceback):
        self._boolean_expression = self.contexts.pop()
        # if (len(self.conditional_stack) > 0):
        #     self.conditional_stack.pop()
        if(len(self.contexts) == 0 and self.lmdp is not None):
            [self.lmdp.add_subpolicy(opt) for opt in self.subpolicies.values()]
            
            [self.lmdp.transition.add(boolean_sa, effect=effect) for (boolean_sa, effect) in self.transition_elements]
            [self.lmdp.reward.add(boolean_sas, effect) for (boolean_sas, effect) in self.reward_elements]
            [self.lmdp.value.add(boolean_sa, effect) for (boolean_sa, effect) in self.value_elements]
        

    def when(self, boolean_expression):
        self.conditional_stack.append(boolean_expression)
        return self

    def otherwise(self):
        condition = self.conditional_stack.pop() 
        self.conditional_stack.append(condition.not_())
        return self

    
    # def state_feature(self, expression=None, name=None):
    #     pass

    # def markov_feature(self, expression=None, name=None):
    #     pass
    
    # def goal(self, symbol=None, name=None):
    #     pass

    def subpolicy(self, policy=None, until=any_state, initiation=any_state, name=None):
        if(self._boolean_expression.domain.is_s()):
            opt = Subpolicy(initiation & self._boolean_expression, policy, termination_symbol=until, name=name)
            self.subpolicies[opt.name] = opt
        else:
            raise "Boolean Expression must be a function of State s"

    def symbol(self, expression=any_state, name=None):
        if(self._boolean_expression.domain.is_s() and expression.domain.is_s()): # only a set of state
            ss = Symbol(expression & self._boolean_expression, name=name)
            self.symbols[ss.name] = ss
        else:
            raise "Boolean Expression must be a function of the State"

    def policy(self, action=None, boolean_expression_s=any_state):
        if (boolean_expression_s.domain.is_s() and self._boolean_expression.domain.is_s()):
            self.policy_elements.append((boolean_expression_s & self._boolean_expression, action))
        else:
            raise "Boolean Expression must be a function of the State"

    def reward(self, real_sas_expression):
        self.reward_elements.append((self._boolean_expression, real_sas_expression))

    def value(self, sa_expression):
        if (not self._boolean_expression.domain.is_sas() or not self._boolean_expression.domain.is_ss()):
            self.value_elements.append((self._boolean_expression, sa_expression))

    def effect(self, effect_expression=None, boolean_expression_sa=(any_state & any_action)):
        if (not boolean_expression_sa.domain.is_sas() and not self._boolean_expression.domain.is_ss() 
            and not self._boolean_expression.domain.is_sas() and not self._boolean_expression.domain.is_ss()):
            b = boolean_expression_sa & self._boolean_expression
            self.transition_elements.append((b, Effect(b, effect_expression)))
        else:
            raise "Boolean Expression must be a function of the State-Action"

if __name__=="__main__":

    from simple_rl.mdp.StateClass import State
    from lmdp.grounding.states.NextStateGroundingClass import next_state
    from lmdp.grounding import StateFactor
    from lmdp.grounding.booleans.BooleanFunClass import any_state, any_action
    from lmdp.grounding.actions.DiscreteActionGroundingClass import DiscreteActionGrounding
    from lmdp.grounding.expressions.ExpressionsClass import state, action, state_prime
    import numpy as np
    
    x = StateFactor(0, "x")
    s = State(data=np.array([1,0]))
    s_prime = State(data= np.array([2,1]))
    s_prime_1 = State(data=np.array([1, 1]))
    up_effect = Effect(any_state and any_action, next_state(x) == x + 1)
    up = DiscreteActionGrounding("up")
    # up = EffectSymbol(next_state(x) == x + 1)(s, "up")
    with Conditional(any_state) as c:
        c.subpolicy(name="option1")
        with c.when(action == up):
            c.effect(next_state(x) == x + 1)
            
    print(f"{c.transition_elements[0][0](s, 'down')} == False")
    print(f"{c.transition_elements[0][1](s, 'up')(s_prime)} == True")

        