from lmdp.grounding.actions.PolicyGroundingClass import PolicyGrounding
from lmdp.grounding.actions.PolicyFromDictClass import PolicyFromDict

class PolicyFromDictGrounding(PolicyGrounding):
    def __init__(self, policy=[]):
        self.policy_dict = PolicyFromDict(policy)
        PolicyGrounding.__init__(self, self.policy_dict)

    def update(self, symbol, action):
        self.policy_dict.update(symbol, action)


if __name__ == "__main__":
    from StateGroundingClass import StateGrounding
    from SymbolClass import Symbol
    from DiscreteActionGroundingClass import DiscreteActionGrounding
    
    import numpy as np
    from simple_rl.tasks import GridWorldMDP
    from simple_rl.tasks import GridWorldState
    
    # 2-dimension state vector in gridworld
    x = StateGrounding(0, "x")
    y = StateGrounding(1, "y")
    position = StateGrounding([0, 1], "position")
    diagonal = Symbol(x == y, "diagonal")
    goal = Symbol(position == np.array([10, 10]), "goal")
    not_goal = Symbol(position != np.array([10, 10]))


    # Actions in gridworld
    up = DiscreteActionGrounding("up", "up")
    down = DiscreteActionGrounding("up", "up")
    right = DiscreteActionGrounding("right", 'right')
    left = DiscreteActionGrounding("left", "left")

    policy = PolicyFromDictGrounding([(not_goal, up)])
    policy.update(diagonal, up)


    s1 = GridWorldState(1, 1)
    s2 = GridWorldState(0, 1)

    print(policy.name)
    print( list(map(lambda a: a.name, policy(s1))))
