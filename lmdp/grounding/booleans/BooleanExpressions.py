from lmdp.grounding.booleans.BooleanFunClass import BooleanExpression


class BooleanState(BooleanExpression):
    '''
        Boolean Expression: S->{True, False}
    '''
    def __call__(self, state):
        return self._fun(state)

class BooleanStateAction(BooleanExpression):
    '''
        Boolean Expression: SxA->{True, False}
    '''
    def __call__(self, state, action):
        return self._fun(state, action)

class BooleanStateActionState(BooleanExpression):
    '''
        Boolean Expression: SxAxS->{True, False}
        State-Action-NextState
    '''
    def __call__(self, state, action, next_state):
        return self._fun(state, action, next_state)