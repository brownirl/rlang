'''
    Subpolicy Class (based on options)

    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: September 2020
'''
import sys, os

sys.path.append(os.path.abspath("/"))
from lmdp.grounding.actions.ActionGroundingClass import ActionGrounding
from lmdp.grounding.actions.PolicyGroundingClass import Policy
from lmdp.grounding.states.SymbolClass import any_state


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

    def __call__(self, *args, **kwargs):
        return self.to_option()

    def is_executable(self, state):
        return self._init(state)

    def is_executing(self):
        return self.__executing

    def __rshift__(self, subpolicy):
        if (isinstance(subpolicy, SubpolicyChain)):
            return SubpolicyChain([self, ] + subpolicy.subpolicies)
        return SubpolicyChain([self, subpolicy])

    def to_option(self):
        return self.to_option2()

    def to_option2(self):
        import lmdp.grounding.actions.options as options
        return options.Option(self._init, self.policy_fun, self._termination, self.name)

    @classmethod
    def primitive_to_subpolicy(self, action):
        if isinstance(action, ActionGrounding):
            return Subpolicy(any_state, action, any_state, name=action.name)
        return Subpolicy(any_state, lambda **args: action, any_state, name="a-" + str(action))

    def __repr__(self):
        return f"(at: {repr(self.init_symbol)}, {repr(self.policy_fun)}, until: {repr(self.termination_symbol)})"


class SubpolicyChain(Subpolicy):
    def __init__(self, subpolicies):
        self.subpolicies = subpolicies
        self.executing_policy = None
        self._init = subpolicies[0]._init
        self._termination = subpolicies[-1]._termination

    def is_executing(self):
        return self.executing_policy is None

    def __rshift__(self, subpolicy):
        if (isinstance(subpolicy, SubpolicyChain)):
            return SubpolicyChain(self.subpolicies + subpolicy.subpolicies)
        return SubpolicyChain(self.subpolicies + [subpolicy])


if __name__ == "__main__":
    from lmdp.grounding import *
    import numpy as np
    from simple_rl.tasks import GridWorldMDP
    from simple_rl.tasks import GridWorldState

    # test
    s1 = GridWorldState(1, 1)
    s2 = GridWorldState(0, 1)
    s1_up = GridWorldState(1, 2)

    # 2-dimension state vector in gridworld
    x = StateFactor(0, "x")
    y = StateFactor(1, "y")
    position = StateFactor([0, 1], "position")
    diagonal = Predicate(x + 1 == y, "diagonal")
    goal = Predicate(position == np.array([10, 10]), "goal")
    not_goal = Predicate(position != np.array([10, 10]))

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
