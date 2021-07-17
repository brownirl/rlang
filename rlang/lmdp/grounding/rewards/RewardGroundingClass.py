'''
    Grounding for symbols to Rewards
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: v0 August 2020
          v1 January 2021 (Partial Function)
'''
import sys, os

sys.path.append(os.path.abspath("/"))
from lmdp.grounding.GroundingClass import Grounding
from lmdp.grounding.PartialFunctionClass import PartialFunction
from lmdp.grounding.real.RealExpressionClass import RealExpression, real_exp
from lmdp.grounding.states.StateClass import BatchedState
import numpy as np


class RewardGrounding(Grounding, PartialFunction):
    id = 0

    def __init__(self, symbols_rewards=[], name=None):
        '''
            Args:
                symbols_rewards: iterable of pairs of (symbols, reward)
        '''
        if (name is None):
            name = "reward-" + str(RewardGrounding.id)
        Grounding.__init__(self, name)
        PartialFunction.__init__(self, domain=["state", "action", "next_state"], codomain=["real"])
        for p in symbols_rewards:
            self.add(*p)

    def __call__(self, state, action, next_state):
        '''
            Args:
                - MDP Transition tuple
            return:
                - list of rewards for all symbol matches
        '''
        return super().__call__(state, action, next_state)

    def __matmul__(self, s_a_s):
        return self.__call__(*s_a_s)

    def add(self, symbol, reward):
        '''
            Add a reward to the dictionary. Overrides if it already exists.        
            Args:
                - symbol 
                - reward
        '''
        if (isinstance(reward, (float, int))):
            r = real_exp(domain=["state", "action", "next_state"])(reward)
        else:
            r = reward

        self.add_specification(symbol, r)


if __name__ == "__main__":
    from lmdp.grounding.states.SymbolClass import Symbol
    from lmdp.grounding.states.StateGroundingClass import StateFactor
    from simple_rl.mdp.StateClass import State
    import numpy as np

    s1 = State(data=np.array([1, 1]))
    s2 = State(data=np.array([0, 1]))
    x = StateFactor(0, "x")
    y = StateFactor(1, "y")
    s = StateFactor([0, 1], "s1")
    start = Symbol(s == np.array([0, 0]))
    not_goal = Symbol(s != np.array([1, 1]))
    diag = Symbol(x == y, "diag")
    r = RewardGrounding([(start, 0.0), (diag, 1.0)])
    print(f"{r.name} for {diag.name} symbol: {r(s1, 'up', s1)} == 1")
    print(f"{r.name} for {diag.name} symbol: {r(s2, 'up', s2)} == []")
