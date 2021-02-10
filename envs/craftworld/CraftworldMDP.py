'''
    simple_rl Wrapper for Craftworld (https://github.com/jacobandreas/psketch)

    author: Rafael Rodriguez-Sanchez
    date: February 2021
'''
import numpy as np
from collections import namedtuple

from simple_rl.mdp.StateClass import State
from simple_rl.mdp.MDPClass import MDP

from envs.craftworld.craft import CraftScenario, CraftState, CraftWorld, UP, DOWN, LEFT, RIGHT, USE

config = namedtuple("config", ["recipes"])

def CraftworldStateFactory(self, scenario, grid, pos, dir, inventory):
    s = CraftState(scenario, grid, pos, dir, inventory)
    return CraftworldState(s)

class CraftworldState(State):

    def __init__(self, craft_state):
        self.state = craft_state
        State.__init__(self, data=self.state.features())

    def features(self):
        return self.state.features()

class Craftworld(MDP):
    ACTIONS = (DOWN, UP, LEFT, RIGHT, USE)
    def __init__(self, goal, path_to_recipes='./recipes.yaml', gamma=0.99, random_seed=0):
        self.random_seed = random_seed
        np.random.set_state(random_seed)
        
        self.goal = goal
        self.config = config(path_to_recipes)
        self.craft_world = CraftWorld(self.config)
        self.craft_scenario = self.craft_world.sample_scenario_with_goal(self.craft_world.cookbook.index[goal])
        MDP.__init__(self, actions=Craftworld.ACTIONS, 
                           transition_func=self._transition_func, 
                           reward_func=self._reward_func, 
                           init_state=self.craft_scenario.init(), 
                           gamma=gamma)

    def __state__(self, craftworld_state):
        return CraftworldState(craftworld_state)

    def get_parameters(self):
        param_dict = {}
        param_dict["gamma"] = self.gamma
        param_dict["random_seed"] = self.random_seed
        param_dict["goal"] = self.goal
        param_dict["path_to_recipes"] = self.config.recipes
        return param_dict

    def _reward_func(self, state, action, next_state):
        return float(next_state.satisfy("make/get", self.craft_world.cookbook.index[self.goal]))

    def _transition_func(self, state, action):
        _, next_state = self.cur_state.step(action)
        return next_state

    def get_init_state(self):
        return CraftworldState(self.init_state)

    def get_curr_state(self):
        return CraftworldState(self.cur_state)