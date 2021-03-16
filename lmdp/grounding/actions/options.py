
class Option:
    id = 0
    def __init__(self, initiation, policy, termination, name=""):
        self._initiation = initiation
        self._policy = policy
        self._termination = termination
        self._id = Option.id 
        self._name = name
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
    
    def is_executable(self, state):
        return self._initiation(state)

    def terminated(self, state):
        return self._termination(state)

    def __hash__(self):
        return self._id.__hash__()