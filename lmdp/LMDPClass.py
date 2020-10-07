'''
    LMDP (Language for MDP) class.
    This class holds prior (deterministic) information:
        - Policy/Sub-policies
        - Rewards/Values
        - Dynamics
        - State Abstractions (symbols)
    For Discrete MDPs

    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: September 2020
'''
import sys, os
sys.path.append(os.path.abspath("./"))

from lmdp.grounding import *
from simple_rl.mdp.MDPClass import MDP
from collections import defaultdict
from collections.abc import Iterable
import random 

class LMDP:

    def __init__(self, mdp=None, state_names=None):
        self.__actions = defaultdict(lambda: None)
        self.__symbols = defaultdict(lambda: None)
        self.__state_groundings = defaultdict(lambda : None)

        if(mdp is not None):
            self.bind(mdp, state_names=state_names)
        
        self.__reward = RewardGrounding()
        self.__value_function = ValueGrounding()
        self.__transition = TransitionGrounding()
        self.__policy = PolicyGrounding(lambda *args: random.choice(self.__actions.keys()))
        self.__subpolicies = defaultdict(lambda: None)
        

    @property
    def reward(self):
        return self.__reward

    @reward.setter
    def reward(self, reward_grounding):
        if (isinstance(reward_grounding, RewardGrounding)):
            self.__reward = reward_grounding
        else:
            raise "Argument must be a RewardGrounding instance"
    
    @property
    def value(self):
        return self.__value_function

    @value.setter  
    def value(self, value_grounding):
        if (isinstance(value_grounding, ValueGrounding)):
            self.__value_function = value_grounding
        else:
            raise "Argument must be a RewardGrounding instance"
    

    @property
    def transition(self):
        return self.__transition

    @transition.setter
    def transition(self, transition_grounding):
        if (isinstance(transition_grounding, TransitionGrounding)):
            self.__transition = transition_grounding
        else:
            raise "Argument must be a TransitionGrounding instance"

    @property
    def policy(self):
        return self.__policy
    
    @policy.setter
    def policy(self, policy_grounding):
        if (isinstance(policy_grounding, PolicyGrounding)):
            self.__policy = policy_grounding
        else:
            raise "Argument must be a PolicyGrounding instance"
    
    def symbol(self, name):
        return self.__symbols[name]
        
    def add_symbol(self, symbol_object):
        if (isinstance(symbol_object, Iterable)):
            self.symbols(symbol_object)
        else:
            self.__symbols[symbol_object.name] = symbol_object

    def symbols(self, symbols_iterable):
        for symbol in symbols_iterable:
            self.__symbols[symbol.name] = symbol

    def subpolicy(self, name):
        return self.__subpolicies[name]
    
    def action(self, name):
        return self.__actions[name]
    
    def actions(self, actions_list):
        for a in actions_list:
            self.__actions[a.name] = a

    def state(self, name):
        return self.__state_groundings[name]
    
    def add_state_var(self, state_grounding):
        self.__state_groundings[state_grounding.name] = state_grounding
    
    def state_groundings(self, state_groundings_list):
        for state in state_groundings_list:
            self.__state_groundings[state.name] = state

    def bind(self, mdp, state_names=None):
        self.actions(list(map(lambda a: DiscreteActionGrounding(a, name=str(a)), mdp.get_actions())))
        state_seq = list(range(mdp.get_num_state_feats()))
        if state_names is None:
            state_names = list(map(lambda state: "state-var-" + str(state), state_seq))
        self.state_groundings(list(map(lambda i: StateGrounding(i, state_names[i]), state_seq)))
        


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
    
    lmdp = LMDP(mdp, state_names=["x", "y"])

    # 2-dimension state vector in gridworld
    position = StateGrounding([0, 1], "position")
    lmdp.add_state_var(position)

    diagonal = Symbol(lmdp.state('x') + 1 == lmdp.state('y'), "diagonal")
    goal = Symbol(position == np.array([10, 10]), "goal")
    not_goal = Symbol(position != np.array([10, 10]))
    lmdp.add_symbol([diagonal, goal, not_goal])
    
    # transitions (deterministic)
    up_effect = NextSymbol((next_state(lmdp.state("y")) == lmdp.state("y") + 1).and_(lmdp.state("x") == next_state(lmdp.state("x"))) )
    lmdp.transition.add(Any, lmdp.action("up"), up_effect)
    print(f"next_state_symbol:{lmdp.transition(s1, lmdp.action('up'))(s1, s1_up)}")
    
    # rewards
    lmdp.reward.add(Any, -0.01)
    
    # policy 
    lmdp.policy.update_policy(lambda *args: "up")

    print(f"s1 in diagonal: {lmdp.symbol('diagonal')(s1)}")
    print(f"s1 is goal state: {lmdp.symbol('goal')(s1)}")

    print(f"policy at s1: {lmdp.policy(s1)}")
    print(f"reward at s1: {lmdp.reward @ s1}")