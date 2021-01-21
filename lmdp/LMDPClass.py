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
import sys, os
sys.path.append(os.path.abspath("./"))

from lmdp.grounding import *
from lmdp.grounding.expressions.ConditionalExpressionClass import Conditional
from lmdp.grounding.VocabularyClass import Vocabulary
from simple_rl.mdp.MDPClass import MDP
from collections import defaultdict
from collections.abc import Iterable
import random 

class LMDP:

    def __init__(self, mdp=None, factor_names=None):
        self._vocabulary = Vocabulary()

        if(mdp is not None):
            self.bind(mdp, factor_names=factor_names)
        
        self.__reward = RewardGrounding()
        self.__value_function = ValueGrounding()
        self.__transition = TransitionGrounding()
        self.__policy = PolicyElements()
        self.__goals = []

    def __call__(self, name):
        return self._vocabulary(name)

    def add(self, element):
        self._vocabulary.add(element.name, element)

    def state(self, name):
        return self.__call__(name)
    
    def add_state_feature(self, state_grounding):
        self.add(state_grounding)

    def symbol(self, name):
        return self._vocabulary(name)
        
    def add_symbol(self, symbol_object):
        if (isinstance(symbol_object, Iterable)):
            for s in symbol_object:
                self.add(s)
        else:
            self.add(symbol_object)

    # def add_symbols(self, symbols_iterable):
    #     for symbol in symbols_iterable:
    #         self.__symbols[symbol.name] = symbol
    
    def get_symbols(self):
        return list(self._vocabulary._symbols.values())

    def subpolicy(self, name):
        return self.__call__(name)

    def get_subpolicies(self):
        return list(self._vocabulary._subpolicies.values())
    
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

    # @reward.setter
    # def reward(self, reward_grounding):
    #     if (isinstance(reward_grounding, RewardGrounding)):
    #         self.__reward = reward_grounding
    #     else:
    #         raise "Argument must be a RewardGrounding instance"
    
    @property
    def value(self):
        return self.__value_function

    # @value.setter  
    # def value(self, value_grounding):
    #     if (isinstance(value_grounding, ValueGrounding)):
    #         self.__value_function = value_grounding
    #     else:
    #         raise "Argument must be a RewardGrounding instance"
    

    @property
    def transition(self):
        return self.__transition

    # @transition.setter
    # def transition(self, transition_grounding):
    #     if (isinstance(transition_grounding, TransitionGrounding)):
    #         self.__transition = transition_grounding
    #     else:
    #         raise "Argument must be a TransitionGrounding instance"

    @property
    def policy(self):
        return self.__policy
    
    # @policy.setter
    # def policy(self, policy_grounding):
    #     if (isinstance(policy_grounding, PolicyGrounding)):
    #         self.__policy = policy_grounding
    #     else:
    #         raise "Argument must be a PolicyGrounding instance"

    def goal(self, symbol):
        if(isinstance(symbol, str)):
            if(symbol in self._vocabulary):
                self.__goals.append(self.__call__(symbol))
            else:
                raise "Symbol " + symbol + " not defined"
        elif(isinstance(symbol, Symbol)):
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
        return Conditional(boolean_expression, self)


if __name__=='__main__':
    from lmdp.grounding import *
    
    import numpy as np
    from simple_rl.tasks import GridWorldMDP
    from simple_rl.tasks import GridWorldState
    #test
    s1 = GridWorldState(1, 1)
    s2 = GridWorldState(0, 1)
    s1_up = GridWorldState(1, 2)
    mdp = GridWorldMDP(10, 10, goal_locs=[(10, 10)])
    
    lmdp = LMDP(mdp, factor_names=["x", "y"])

    # 2-dimension state vector in gridworld
    position = StateFactor([0, 1], "position")
    lmdp.add_state_feature(position)

    diagonal = Symbol(lmdp.state('x') + 1 == lmdp.state('y'), "diagonal")
    goal = Symbol(position == np.array([10, 10]), "goal")
    not_goal = Symbol(position != np.array([10, 10]))
    lmdp.add_symbol([diagonal, goal, not_goal])
    

    # transitions (deterministic)
    with lmdp.when(any_state & (action == lmdp.action("up")())) as c:
        # c.effect((next_state(lmdp.state("y")) == lmdp.state("y") + 1) & (lmdp.state("x") == next_state(lmdp.state("x"))))
        c.effect({lmdp("y"): lmdp("y") + 1, lmdp('x'): lmdp("x")})
    
    print(f"next_state_symbol:{lmdp.transition(s1, lmdp.action('up'))[0](s1_up)}")
    
    # rewards
    # lmdp.reward.add(Any, -0.01)
    
    # print(f"s1 in diagonal: {lmdp.symbol('diagonal')(s1)}")
    # print(f"s1 is goal state: {lmdp.symbol('goal')(s1)}")

    # print(f"policy at s1: {lmdp.policy(s1)}")
    # print(f"reward at s1: {lmdp.reward @ s1}")