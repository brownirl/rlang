'''
    This wrapper creates a flexible factory for State Objects
    that can be initialized for the particular class of MDP

    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: January 2021
'''

class State:
    def __init__(self, factor_names, state_constructor):
        self.factory = StateFactory(state_constructor)
        self.factor_names = factor_names

    def __call__(self, *factors, **kwords):
        self.state = self.factory(*factors, **kwords)
        return self.state

class NumericState(State):
    def __init__(self, factor_names, state_constructor, feature_getter):
        State.__init__(self, factor_names, state_constructor)
        self.feature_getter = feature_getter
    
    def features(self):
        return self.feature_getter(self.state)

class StateFactory:
    def __init__(self, state_constructor):
        self.state_constructor = state_constructor

    def __call__(self, *args, **kwargs):
        return self.state_constructor(*args, **kwargs)


if __name__ == "__main__":
    from simple_rl.tasks.grid_world.GridWorldStateClass import GridWorldState
    import inspect
    s_factory = StateFactory(GridWorldState)
    print(s_factory(3,4))