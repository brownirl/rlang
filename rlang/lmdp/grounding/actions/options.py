from lmdp.grounding.states.SymbolClass import any_state
from lmdp.grounding.actions.ActionGroundingClass import ActionGrounding
class Option:
    id = 0
    def __init__(self, initiation, policy, termination,  name=""):
        self._initiation = initiation
        self._policy = policy
        self._termination = termination
        self._id = Option.id 
        self._name = name
        self._learnable = True if policy is None else False
        Option.id += 1
    
    @property
    def initiation(self):
        return self._initiation
    @property
    def policy(self):
        return self._policy
    @property
    def termination(self):
        return self._termination
    
    def get_id(self):
        return self._id

    def is_executable(self, state):
        return self._initiation(state)

    def terminated(self, state):
        return self._termination(state)

    def is_learnable(self):
        return self._learnable
        
    def __hash__(self):
        return self._id.__hash__()

    def __repr__(self):
        return self._name

    @classmethod
    def primitive_to_option(self, action):
        if isinstance(action, ActionGrounding):
            return Option(any_state, lambda **args: action, termination=any_state, name=action.name)
        return Option(any_state, lambda **args: action, termination=any_state, name="a-"+str(action))
