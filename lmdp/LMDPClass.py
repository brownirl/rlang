'''
    LMDP (Language-MDP) class.
    Wrapper class for MDPs that holds prior (deterministic) informationon:
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

    def __init__(self, mdp):
        self.__mdp = mdp
        self.__reward = RewardGrounding()
        self.__value_function = ValueGrounding()
        self.__transition = TransitionGrounding()
        self.__symbols = defaultdict(lambda: None)
        self.__policy = PolicyGrounding(lambda *args: random.choice(mdp.get_actions()))
        self.__subpolicies = defaultdict(lambda: None)
        self.__actions = defaultdict(lambda: None)
        self.__state_groundings = defaultdict(lambda : None)

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
    
    @property
    def symbol(self):
        return self.__symbols
    @symbol.setter
    def symbol(self, symbol_object):
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

    # ----- In case of unknown method for a more specialized MDP class
    
    def __getattr__(self, method_name):
        def method(*args, **kwargs):
            print("Handling unknown method: '{}'".format(method_name))
            return getattr(self.__mdp, method_name)(*args, **kwargs)
        return method

    # ----- Implementation the MDP interface
    def get_parameters(self):
        return self.__mdp.param_dict

    def get_init_state(self):
        return self.__mdp.init_state

    def get_curr_state(self):
        return self.__mdp.cur_state

    def get_actions(self):
        return self.__mdp.actions

    def get_gamma(self):
        return self.__mdp.gamma

    def get_reward_func(self):
        return self.__mdp.reward_func

    def get_transition_func(self):
        return self.__mdp.transition_func

    def get_num_state_feats(self):
        return self.__mdp.init_state.get_num_feats()

    def get_slip_prob(self):
        return self.__mdp.get_slip_prob()

    def get_name(self):
        return str(self.__mdp)

    # --------------
    # -- Mutators --
    # --------------

    def set_gamma(self, new_gamma):
        self.__mdp.set_gamma(new_gamma)

    def set_step_cost(self, new_step_cost):
        self.__mdp.set_step_cost(new_step_cost)

    def set_slip_prob(self, slip_prob):
        self.__mdp.set_slip_prob(slip_prob)

    def set_init_state(self, new_init_state):
        self.__mdp.set_init_state(new_init_state)

    # ----------
    # -- Core --
    # ----------

    def execute_agent_action(self, action):
        return self.__mdp.execute_agent_action(action)

    def reset(self):
        self.__mdp.reset()

    def end_of_instance(self):
        self.__mdp.end_of_instance()

if __name__=='__main__':
    from lmdp.grounding import *
    
    import numpy as np
    from simple_rl.tasks import GridWorldMDP
    from simple_rl.tasks import GridWorldState
    
    #test
    s1 = GridWorldState(1, 1)
    s2 = GridWorldState(0, 1)
    s1_up = GridWorldState(1, 2)

    # 2-dimension state vector in gridworld
    x = StateGrounding(0, "x")
    y = StateGrounding(1, "y")
    position = StateGrounding([0, 1], "position")
    diagonal = Symbol(x + 1 == y, "diagonal")
    goal = Symbol(position == np.array([10, 10]), "goal")
    not_goal = Symbol(position != np.array([10, 10]))
    anywhere = Symbol(lambda *args: True)


    # Actions in gridworld
    up = DiscreteActionGrounding("up", "up")
    down = DiscreteActionGrounding("down", "down")
    right = DiscreteActionGrounding("right", 'right')
    left = DiscreteActionGrounding("left", "left")
    
    lmdp = LMDP(GridWorldMDP(10, 10, goal_locs=[(10, 10)]))
    lmdp.symbol = anywhere # adds symbol to lmdp
    lmdp.symbols([diagonal, goal]) # register symbols to lmdp
    lmdp.actions([up, down, right, left])

    # transitions (deterministic)
    up_effect = NextSymbol((next_state(y) == y + 1) & (x == next_state(x)))
    lmdp.transition.add(anywhere, up, up_effect)
    print(f"next_state_symbol:{lmdp.transition(s1, lmdp.action('up'))(s1, s1_up)}")
    
    # rewards
    lmdp.reward.add(anywhere, -0.01)
    
    # policy 
    lmdp.policy.update_policy(lambda *args: "up")

  
    
    

    print(f"s1 in diagonal: {lmdp.symbol['diagonal'](s1)}")
    print(f"s1 is goal state: {lmdp.symbol['goal'](s1)}")

    print(f"policy at s1: {lmdp.policy(s1)}")
    print(f"reward at s1: {lmdp.reward(s1)}")