'''
    LMDP (Language for MDP) class.
    This class holds prior (deterministic) information:
        - Policy/Sub-policies
        - Rewards/Values
        - Dynamics
        - State Abstractions (symbols)
    For Discrete MDPs

    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: v0 September 2020
          v1 January 2021
'''
from .grounding.transitions.TransitionGroundingClass import TransitionGrounding
from .grounding.states.StateGroundingClass import StateFactor
from .grounding import *
from .grounding.expressions.ConditionalExpressionClass import Conditional
from .grounding.VocabularyClass import Vocabulary
from simple_rl.mdp.MDPClass import MDP
from collections import defaultdict
from collections.abc import Iterable
import random


class LMDP:
    id = 0
    LMDPs = dict()

    def __init__(self, mdp=None, factor_names=None, domain_name=None):
        if domain_name is None:
            domain_name = "LMDP_" + str(LMDP.id)
            LMDP.id += 1
        self.domain_name = domain_name
        self._vocabulary = Vocabulary()

        if mdp is not None and factor_names is not None and len(factor_names) > 0:
            self.bind(mdp, factor_names=factor_names)
        if mdp is not None:
            for a in mdp.get_actions():
                self.add(DiscreteActionGrounding(a))

        self.__reward = RewardGrounding()
        self.__value_function = ValueGrounding()
        self.__transition = TransitionGrounding()
        self.__policy = PolicyElements()
        self.__goals = []

        LMDP.LMDPs[self.domain_name] = self

    def __call__(self, name):
        return self._vocabulary(name)

    def add(self, element):
        self._vocabulary.add(element.name, element)
        return element

    def state_feature(self, name):
        return self.__call__(name)

    def add_state_feature(self, state_grounding):
        self.add(state_grounding)

    def symbol(self, name):
        return self._vocabulary(name)

    def add_symbol(self, symbol_object):
        if isinstance(symbol_object, Iterable):
            for s in symbol_object:
                self.add(s)
        else:
            self.add(symbol_object)

    def get_symbols(self):
        return list(self._vocabulary._symbols.values())

    def subpolicy(self, name):
        return self.__call__(name)

    def get_subpolicies(self):
        return list(
            self._vocabulary._subpolicies.values())  # +[Subpolicy.primitive_to_subpolicy(a) for a in self.get_actions()]

    def add_subpolicy(self, subpolicy):
        self.add(subpolicy)

    def action(self, name):
        return self.__call__(name)

    def add_actions(self, actions_list):
        for a in actions_list:
            self.add(a)

    def get_actions(self):
        return list(self._vocabulary._actions.values())

    @property
    def reward(self):
        return self.__reward

    @property
    def value(self):
        return self.__value_function

    @property
    def transition(self):
        return self.__transition

    @property
    def policy(self):
        return self.__policy

    def goal(self, symbol):
        if isinstance(symbol, str):
            if symbol in self._vocabulary:
                self.__goals.append(self.__call__(symbol))
            else:
                raise "Predicate " + symbol + " not defined"
        elif isinstance(symbol, Predicate):
            self.__goals.append(symbol)

    def state_groundings(self, state_groundings_list):
        for state in state_groundings_list:
            self.add(state)

    def bind(self, mdp, factor_names=None):
        self.add_actions(list(map(lambda a: DiscreteActionGrounding(a, name=str(a)), mdp.get_actions())))
        state_seq = list(range(mdp.get_num_state_feats()))
        if factor_names is None:
            factor_names = list(map(lambda state: "state-var-" + str(state), state_seq))
        self.state_groundings(list(map(lambda i: StateFactor(i, factor_names[i]), state_seq)))

    def when(self, boolean_expression):
        self._conditional = Conditional(boolean_expression, self)
        return self._conditional  # context manager

    def build_state(self, *args, **kwargs):
        return self.__state_constructor(*args, **kwargs)


if __name__ == '__main__':
    from lmdp.grounding import *

    import numpy as np
    from simple_rl.tasks import GridWorldMDP
    from simple_rl.tasks import GridWorldState

    # test
    s1 = GridWorldState(1, 1)
    s2 = GridWorldState(0, 1)
    s1_up = GridWorldState(1, 2)
    mdp = GridWorldMDP(10, 10, goal_locs=[(10, 10)])

    lmdp = LMDP(mdp, factor_names=["x", "y"])

    # 2-dimension state vector in gridworld
    position = StateFactor([0, 1], "position")
    lmdp.add_state_feature(position)

    diagonal = Predicate(lmdp('x') + 1 == lmdp('y'), "diagonal")
    goal = Predicate(position == np.array([10, 10]), "goal")
    not_goal = Predicate(position != np.array([10, 10]))
    lmdp.add_symbol([diagonal, goal, not_goal])

    # transitions (deterministic)
    with lmdp.when(any_state & (A == lmdp.action("up")())) as c:
        # c.effect((next_state(lmdp.state("y")) == lmdp.state("y") + 1) & (lmdp.state("x") == next_state(lmdp.state("x"))))
        c.effect({lmdp("y"): lmdp("y") + 1, lmdp('x'): lmdp("x")})

    print(f"next_state_symbol:{lmdp.transition(s1, lmdp.action('up'))[0](s1_up)}")
