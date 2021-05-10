'''
    simple_rl Wrapper for Craftworld (https://github.com/jacobandreas/psketch)

    author: Rafael Rodriguez-Sanchez
    date: February 2021
'''
import numpy as np
from collections import namedtuple

from simple_rl.mdp.StateClass import State
from simple_rl.mdp.MDPClass import MDP

from envs.craftworld.craft import CraftScenario, CraftStateGrid, CraftWorld, UP, DOWN, LEFT, RIGHT, USE

config = namedtuple("config", ["recipes"])
Transition = namedtuple("Transition", ["s1", "m1", "a", "s2", "m2", "r"])
ModelState = namedtuple("ModelState", ["action", "arg", "remaining", "task", "step"])

def CraftworldStateFactory(self, scenario, grid, pos, dir, inventory):
    s = CraftStateGrid(scenario, grid, pos, dir, inventory)
    return CraftworldState(s)

class CraftworldState(State):

    def __init__(self, craft_state):
        self.state = craft_state
        State.__init__(self, data=self.state.features())
        self.hash = None

    def features(self):
        return self.state.features()
    
    def get_craftstate(self):
        return self.state

    def __hash__(self):
        if self.hash is None:
            self.hash = hash(tuple(self.data))
        return self.hash

    def __eq__(self, other):
        if other is not None:
            return  (other.data == self.data).all()
        return False

class Craftworld(MDP):
    ACTIONS = {"down": DOWN, "up": UP, "left" : LEFT, "right": RIGHT, "use": USE}
    def __init__(self, goal, path_to_recipes='recipes.yaml', gamma=0.99, random_seed=0):
        self.random_seed = random_seed
        np.random.seed(random_seed)
        
        self.goal = goal
        self.config = config(path_to_recipes)
        self.craft_world = CraftWorld(self.config)
        self.craft_scenario = self.craft_world.sample_scenario_with_goal(self.craft_world.cookbook.index[goal])
        self.transitions = []
        MDP.__init__(self, actions=list(Craftworld.ACTIONS.keys()), 
                           transition_func=self._transition_func, 
                           reward_func=self._reward_func, 
                           init_state=CraftworldState(self.craft_scenario.init()), 
                           gamma=gamma)

    def get_parameters(self):
        param_dict = {}
        param_dict["gamma"] = self.gamma
        param_dict["random_seed"] = self.random_seed
        param_dict["goal"] = self.goal
        param_dict["path_to_recipes"] = self.config.recipes
        return param_dict

    def _reward_func(self, state, action, next_state):
        goal_achieved = next_state.get_craftstate().satisfies("make/get", self.craft_world.cookbook.index[self.goal])
        if goal_achieved:
            next_state._is_terminal = True
        return float(goal_achieved)

    def _transition_func(self, state, action):
        _, next_state = self.cur_state.get_craftstate().step(Craftworld.ACTIONS[action])
        return CraftworldState(next_state)

    def execute_agent_action(self, action):
        m = ModelState(None, None, None, None, None)
        curr_s = self.cur_state.get_craftstate()
        r, next_state = super().execute_agent_action(action)
        t = Transition(curr_s, m, action, next_state.get_craftstate(), m, r)
        self.transitions.append(t)
        return r, next_state
    
    def get_transitions(self):
        return self.transitions

    def reset(self):
        super().reset()
        self.transitions = []
    
    def vis(self):
        self.craft_world.visualize(self.transitions)