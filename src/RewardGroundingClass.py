'''
    Grounding for symbols to Rewards
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: August 2020
'''
from GroundingClass import Grounding
class RewardGrounding(Grounding):
    id = 0
    def __init__(self, symbols_rewards=[], name=None):
        '''
            Args:
                symbols_rewards: iterable of pairs of (symbols, reward)
        '''
        if (name is None):
            name = "reward-" + str(RewardGrounding.id)
        Grounding.__init__(self, name)
        self.__rewards = dict(symbols_rewards)

    def __call__(self, state):
        '''
            Args:
                - state from MDP
            return:
                - list of rewards for all symbol matches
        '''
        symbols = [s for s in self.__rewards.keys() if s(state)]
        r = [self.__rewards[s] for s in symbols]
        if len(r) == 1:
            return r[0]
        return r
    
    def add(self, symbol, reward):
        '''
            Add a reward to the dictionary. Overrides if it already exists.        
            Args:
                - symbol 
                - reward
        '''
        self.__rewards[symbol] = reward


if __name__ == "__main__":
    from SymbolClass import Symbol
    from StateGroundingClass import StateGrounding
    from simple_rl.mdp.StateClass import State
    import numpy as np

    s1 = State(data=np.array([1, 1]))
    s2 = State(data=np.array([0, 1]))
    x = StateGrounding(0, "x")
    y = StateGrounding(1, "y")
    s = StateGrounding([0,1], "s1")
    start = Symbol(s == np.array([0,0]))
    not_goal = Symbol(s != np.array([1,1]))
    diag = Symbol(x == y, "diag")
    r = RewardGrounding([(start, 0), (diag, 1)])
    print(f"{r.name} for {diag.name} symbol: {r(s1)}")
    print(f"{r.name} for {diag.name} symbol: {r(s2)}")