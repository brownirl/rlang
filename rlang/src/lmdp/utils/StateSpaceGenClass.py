'''
    Generator Class for the State Space of Discrete MDPs.
    State variables domain are integer numbers.

    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: October 2020
'''
import numpy as np
from collections import OrderedDict
from simple_rl.mdp.StateClass import State


class StateSpaceGen:

    def __init__(self, **kwords):
        '''
            Args:
                -State factory: Constructor for the state vector class
                -actions: actions available
                -kwords: must be variable name_variable=(min_value, max_value) (>= 1)
        '''

        if len(kwords) == 0:
            raise "At least one state variable specification is necessary"

        self.state_variables = OrderedDict(kwords)
        self.state_constructor = State
        self.generators = None
        self.curr_variable = None
        self.svars = tuple(self.state_variables.keys())

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr_variable is not None and self.curr_variable < 0:
            self.generators = None
            self.curr_variable = None
            raise StopIteration
        else:
            self.curr_variable = len(self.svars) - 1

        if self.generators is None or self.curr_variable is None:
            self.generators = OrderedDict({s: r[0] for s, r in self.state_variables.items()})
            self.curr_variable = len(self.state_variables) - 1
        current_state = np.array(tuple(self.generators.values()))
        self.generators[self.svars[self.curr_variable]] += 1
        while self.curr_variable >= 0 and self.generators[self.svars[self.curr_variable]] > \
                self.state_variables[self.svars[self.curr_variable]][1]:
            self.generators[self.svars[self.curr_variable]] = self.state_variables[self.svars[self.curr_variable]][
                0]  # restart variable
            self.curr_variable -= 1
            self.generators[self.svars[self.curr_variable]] += 1

        return self.state_constructor(data=current_state)


if __name__ == "__main__":
    from simple_rl.tasks.grid_world.GridWorldStateClass import GridWorldState

    g = StateSpaceGen(x=(0, 9), y=(0, 4))
    for s in g:
        print(s)
