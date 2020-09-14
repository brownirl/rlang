'''
    Subpolicy Class (based on options)

    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: September 2020
'''
import sys, os
sys.path.append(os.path.abspath("./"))

from lmdp.grounding.actions.ActionGroundingClass import ActionGrounding
from lmdp.grounding.states.SymbolClass import Any
from simple_rl.abstraction.action_abs.PredicateClass import Predicate
from simple_rl.abstraction.action_abs.OptionClass import Option

class Subpolicy(ActionGrounding):
    id = 0
    def __init__(self, init_symbol, policy_fun, termination_symbol, name=None):
        if (name is None):
            name = "Subpolicy-" + str(Subpolicy.id)
        Subpolicy.id += 1
        self.__init = init_symbol
        self.__termination = termination_symbol
        self.__executing = False
        ActionGrounding.__init__(self, policy_fun, name=name)

    
    def __call__(self, *args):
        if (not self.__executing and self.__init(*args)):
            self.__executing = True
            return super().__call__(*args)
        elif (self.__executing and not self.__termination(*args)):
            return super().__call__(*args)
        elif (self.__termination(*args)):
            self.__executing = False
            return None

    def is_executing(self):
        return self.__executing



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
    x = StateGrounding(0, "x")
    y = StateGrounding(1, "y")
    position = StateGrounding([0, 1], "position")
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

    goal = Subpolicy(Any, p, goal)
    
    print(f"{goal.name}: {goal(s1)}")


