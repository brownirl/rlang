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

sys.path.append(os.path.abspath("./lmdp"))
from collections import deque, namedtuple
from functools import reduce
from lmdp.grounding.expressions.ExpressionsClass import Expression
from lmdp.grounding.states.PredicateClass import any_state
from lmdp.grounding.booleans.BooleanFunClass import BooleanExpression, any_action, bool_not, bool_and, bool_or
from lmdp.grounding.actions.SubpolicyClass import Subpolicy
from lmdp.grounding.states.Effect import Effect
from lmdp.grounding import *
from lmdp.grounding.booleans.BooleanFunClass import bool_true

WHEN_CTX = True
OTHERWISE_CTX = False
Context = namedtuple('Context', ['is_when', 'boolean', 'outer_ctx'])


def empty_stack(stack):
    while (stack):
        yield stack.pop()


class Conditional:
    def __init__(self, boolean_expression, lmdp=None):
        self._boolean_expression = boolean_expression
        self._curr_boolean = boolean_expression
        self.lmdp = lmdp
        # self.conditional_stack = deque([boolean_expression])
        self.contexts = list()
        self.current_context = Context(WHEN_CTX, boolean_expression, bool_true)

        # definitions
        self.subpolicies = []
        self.state_features = []
        self.symbols = []
        self.markov = []

        # partial functions
        self.transition_elements = []
        self.reward_elements = []
        self.value_elements = []
        self.ex_policy_elements = []
        self.not_ex_policy_elements = []

        self.__is_otherwise_available = False

    #### Context Handling
    def __enter__(self):

        return self

    def __exit__(self, type, value, traceback):

        self._boolean_expression = self.current_context.outer_ctx  # back to the outer context
        self.__is_otherwise_available = self.current_context.is_when
        if (self.lmdp is not None):
            self.__update_lmdp()

    def when(self, boolean_expression):
        self.contexts.append(self.current_context)
        self.current_context = Context(WHEN_CTX, boolean_expression, self._boolean_expression)  # current context
        self._boolean_expression = self.current_context.outer_ctx & boolean_expression  # boolean expression to use within the context
        return self

    def otherwise(self):
        if (self.__is_otherwise_available):
            self.current_context = Context(OTHERWISE_CTX, bool_not(self.current_context.boolean),
                                           self.current_context.outer_ctx)
            self._boolean_expression = self.current_context.boolean.__and__(self.current_context.outer_ctx)
            self.__is_otherwise_available = False
        else:
            raise ValueError("Otherwise Statement does not correspond to a When Statement")
        return self

    def __update_lmdp(self):
        [self.lmdp.add_subpolicy(opt) for opt in empty_stack(self.subpolicies)]
        [self.lmdp.transition.add(boolean_sa, effect=effect) for (boolean_sa, effect) in
         empty_stack(self.transition_elements)]
        [self.lmdp.reward.add(boolean_sas, effect) for (boolean_sas, effect) in empty_stack(self.reward_elements)]
        [self.lmdp.value.add(boolean_sa, effect) for (boolean_sa, effect) in empty_stack(self.value_elements)]
        [self.lmdp.policy.execute(boolean_s, action) for (boolean_s, action) in empty_stack(self.ex_policy_elements)]

    def __close_context(self):
        if (self.__is_otherwise_available):
            self.current_context = self.contexts.pop()
            self.__is_otherwise_available = False

    def subpolicy(self, policy=None, until=any_state, initiation=any_state, name=None):
        self.__close_context()
        if (self._boolean_expression.domain.is_s()):
            opt = Subpolicy(initiation & self._boolean_expression, policy, termination_symbol=until, name=name)
            self.subpolicies.append(opt)
        else:
            raise ValueError("Boolean Expression must be a function of State s")

    def symbol(self, expression=any_state, name=None):
        self.__close_context()
        if (self._boolean_expression.domain.is_s() and expression.domain.is_s()):  # only a set of state
            ss = Predicate(expression & self._boolean_expression, name=name)
            self.symbols.append(ss)
        else:
            raise ValueError("Boolean Expression must be a function of the State")

    def execute(self, action=None):
        self.__close_context()
        if (self._boolean_expression.domain.is_s()):
            self.ex_policy_elements.append((self._boolean_expression, action))
        else:
            raise ValueError("Boolean Expression must be a function of the State")

    def do_not_execute(self, action=None):
        self.__close_context()
        if (self._boolean_expression.domain.is_s()):
            self.not_ex_policy_elements.append((self._boolean_expression, action))
        else:
            raise ValueError("Boolean Expression must be a function of the State")

    def policy(self, action=None, boolean_expression_s=any_state):
        self.__close_context()
        if (boolean_expression_s.domain.is_s() and self._boolean_expression.domain.is_s()):
            self.policy_elements.append((boolean_expression_s & self._boolean_expression, action))
        else:
            raise ValueError("Boolean Expression must be a function of the State")

    def reward(self, real_sas_expression):
        self.__close_context()
        self.reward_elements.append((self._boolean_expression, real_sas_expression))

    def value(self, sa_expression):
        self.__close_context()
        if (not self._boolean_expression.domain.is_sas() or not self._boolean_expression.domain.is_ss()):
            self.value_elements.append((self._boolean_expression, sa_expression))

    def effect(self, effect_expression=None, boolean_expression_sa=(any_state & any_action)):
        self.__close_context()
        if (not boolean_expression_sa.domain.is_sas() and not self._boolean_expression.domain.is_ss()
                and not self._boolean_expression.domain.is_sas() and not self._boolean_expression.domain.is_ss()):
            b = boolean_expression_sa & self._boolean_expression
            self.transition_elements.append((b, Effect(b, effect_expression)))
        else:
            raise ValueError("Boolean Expression must be a function of the State-Action")


if __name__ == "__main__":
    from simple_rl.mdp.StateClass import State
    from lmdp.grounding.states.NextStateGroundingClass import next_state
    from lmdp.grounding import StateFactor
    from lmdp.grounding.booleans.BooleanFunClass import any_state, any_action
    from lmdp.grounding.actions.DiscreteActionGroundingClass import DiscreteActionGrounding
    from lmdp.grounding.expressions.ExpressionsClass import S, A, S_prime
    import numpy as np

    x = StateFactor(0, "x")
    s = State(data=np.array([1, 0]))
    s_prime = State(data=np.array([2, 1]))
    s_prime_1 = State(data=np.array([1, 1]))
    up_effect = Effect(any_state and any_action, next_state(x) == x + 1)
    up = DiscreteActionGrounding("up")
    # up = EffectSymbol(next_state(x) == x + 1)(s, "up")
    with Conditional(any_state) as c:
        c.subpolicy(name="option1")
        with c.when(A == up):
            c.effect(next_state(x) == x + 1)
        with c.otherwise().when(any_action):
            c.effect(next_state(x) == x)

    print(f"{c.transition_elements[0][0](s, 'down')} == False")
    print(f"{c.transition_elements[0][1](s, 'up')(s_prime)} == True")
