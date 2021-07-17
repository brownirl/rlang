'''
    RLang Vocabulary Class
    author: Rafael Rodriguez-Sanchez
    date: January 2021
'''
import os
import sys

sys.path.append(os.path.abspath("/"))
from collections import defaultdict
from lmdp.grounding import *


class Vocabulary:

    def __init__(self):
        self._vocabulary = defaultdict(lambda: None)
        self._state_factors = defaultdict(lambda: None)
        self._state_features = defaultdict(lambda: None)
        self._symbols = defaultdict(lambda: None)
        self._actions = defaultdict(lambda: None)
        self._subpolicies = defaultdict(lambda: None)
        self._markov_features = defaultdict(lambda: None)
        self.TYPES_TO_LIST = (
            (StateFactor, self._state_factors),
            (StateFeature, self._state_features),
            (Predicate, self._symbols),
            (ActionGrounding, self._actions),
            (Subpolicy, self._subpolicies),
            (MarkovFeature, self._markov_features)
        )

    def __call__(self, name):
        return self._vocabulary[name]

    def add(self, name, elem):
        d = self.__type_map(elem)
        if d is not None:
            d[name] = elem
        self._vocabulary[name] = elem

    def __type_map(self, elem):
        for k in self.TYPES_TO_LIST:
            if isinstance(elem, k[0]):
                return k[1]

    def __contains__(self, name):
        return name in self._vocabulary


if __name__ == "__main__":
    import numpy as np
    from simple_rl.tasks import GridWorldMDP
    from simple_rl.tasks import GridWorldState

    # test
    s1 = GridWorldState(1, 1)
    s2 = GridWorldState(0, 1)
    s1_up = GridWorldState(1, 2)
    mdp = GridWorldMDP(10, 10, goal_locs=[(10, 10)])

    # 2-dimension state vector in gridworld
    position = StateFactor([0, 1], "position")

    goal = Predicate(position == np.array([10, 10]), "goal")
    not_goal = Predicate(position != np.array([10, 10]))
    up = DiscreteActionGrounding("up")
    v = Vocabulary()
    v.add("position", position)
    v.add("up", up)
    print(v("position"))
