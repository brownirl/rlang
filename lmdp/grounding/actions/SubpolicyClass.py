'''
    Subpolicy Class (based on options)

    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: September 2020
'''
import sys, os
sys.path.append(os.path.abspath("./"))

from lmdp.grounding.actions.PolicyGroundingClass import Policy
from lmdp.grounding.states.SymbolClass import Any
from simple_rl.abstraction.action_abs.PredicateClass import Predicate
from simple_rl.abstraction.action_abs.OptionClass import Option

class Subpolicy(Policy):
    id = 0
    def __init__(self, init_symbol, policy_fun, termination_symbol, name=None):
        if (name is None):
            name = "Subpolicy-" + str(Subpolicy.id)
        Subpolicy.id += 1
        self._init = init_symbol
        self._termination = termination_symbol
        self.__executing = False
        Policy.__init__(self, policy_fun, name=name)
 
    def __call__(self, state):
        if (not self.__executing and self._init(state)):
            self.__executing = True
            return super().__call__(state)
        elif (self.__executing and not self._termination(state)):
            return super().__call__(state)
        elif (self._termination(state)):
            self.__executing = False
            return None

    def is_executable(self, state):
        return self._init(state)
        
    def is_executing(self):
        return self.__executing

    def __rshift__(self, subpolicy):
        if (isinstance(subpolicy, SubpolicyChain)):
            return SubpolicyChain([self,] + subpolicy.subpolicies)
        return SubpolicyChain([self, subpolicy])

    def to_option(self):
        return Option(Predicate(self._init), Predicate(self._termination), self.policy_fun, name=self.name)


class SubpolicyFromOption(Subpolicy):
    def __init__(self, init_symbol, policy_fun, termination_symbol, name=None):
        Subpolicy.__init__(self, init_symbol, policy_fun, termination_symbol, name=name) 
        self.__option = Option(Predicate(init_symbol), Predicate(termination_symbol), policy_fun, name=self.name)

    def __call__(self):
        '''
            Returns the option to be used by simple_rl agent
        '''
        return self.__option

class GoalSubpolicy(SubpolicyFromOption):
    id = 0
    def __init__(self, policy_fun, goal_symbol, name=None):
        if (name is None):
            name = 'goal-subpolicy-' + str(GoalSubpolicy.id)
        GoalSubpolicy.id += 1
        SubpolicyFromOption.__init__(self, Any, policy_fun, goal_symbol, name=name)

class SubpolicyChain(Subpolicy):
    def __init__(self, subpolicies):
        self.subpolicies = subpolicies
        self.executing_policy = None
        self._init = subpolicies[0]._init
        self._termination = subpolicies[-1]._termination

    def __call__(self, *args):
        if (not self.is_executing):
            if (self._init(*args)):
                self.executing_policy = self.subpolicies[0]
                self.current_policy_idx = 0
                return self.executing_policy(*args)
        else:
            if (self.executing_policy.is_executing()):
                return self.executing_policy(*args)
            else:
                self.current_policy_idx += 1
                if (self.current_policy_idx > len(self.subpolicies)):
                    self.executing_policy = None
                    return None
                self.executing_policy = self.subpolicies[self.current_policy_idx]
                if (not self._termination(*args) and self.executing_policy._init(*args)):
                    return self.executing_policy(*args)
                else:
                    self.executing_policy = None
        return None
    
    def is_executing(self):
        return self.executing_policy is None

    def __rshift__(self, subpolicy):
        if (isinstance(subpolicy, SubpolicyChain)):
            return SubpolicyChain(self.subpolicies + subpolicy.subpolicies)
        return SubpolicyChain(self.subpolicies + [subpolicy])

if __name__== "__main__":
    from lmdp.grounding import *
    import numpy as np
    from simple_rl.tasks import GridWorldMDP
    from simple_rl.tasks import GridWorldState
    #test
    s1 = GridWorldState(1, 1)
    s2 = GridWorldState(0, 1)
    s1_up = GridWorldState(1, 2)

    # 2-dimension state vector in gridworld
    x = StateFactor(0, "x")
    y = StateFactor(1, "y")
    position = StateFactor([0, 1], "position")
    diagonal = Symbol(x + 1 == y, "diagonal")
    goal = Symbol(position == np.array([10, 10]), "goal")
    not_goal = Symbol(position != np.array([10, 10]))

    # Actions in gridworld
    up = DiscreteActionGrounding("up", "up")
    down = DiscreteActionGrounding("down", "down")
    right = DiscreteActionGrounding("right", 'right')
    left = DiscreteActionGrounding("left", "left")

    p = PolicyFromDict()
    p.add(diagonal, up)

    subgoal1 = Subpolicy(Any, p, goal)
    subgoal2 = Subpolicy(Any, p, goal)
    subpolicy = subgoal1 >> subgoal2
    subpolicy2 = subgoal1 >> subpolicy


