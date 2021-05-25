import gym
import gym.spaces as spaces
import envs.craftworld.craft as craft
from collections import namedtuple
import torch

PATH_TO_RECIPES = "./envs/craftworld/recipes.yaml"

config = namedtuple("config", ["recipes"])
Transition = namedtuple("Transition", ["s1", "m1", "a", "s2", "m2", "r"])
ModelState = namedtuple("ModelState", ["action", "arg", "remaining", "task", "step"])

class Craftworld(gym.Env):
    spec = "Craftworld"
    metadata = dict()
    metadata['render.modes'] = ['terminal']
    def __init__(self, goal, name=None, **kwargs):
        self.config = config(PATH_TO_RECIPES)
        self.world = craft.CraftWorld(self.config)
        self.goal = self.world.cookbook.index[goal]
        self.scenario = self.world.sample_scenario_with_goal(self.goal)
        self.curr_state = self.scenario.init()
        self.action_space = spaces.Discrete(craft.USE + 1)
        self.observation_space = spaces.Box(0, 100, shape=(craft.WIDTH*craft.HEIGHT*(self.world.cookbook.n_kinds+1)+self.world.cookbook.n_kinds,))
        self.reward_range = (0, 1)
        self.name = name if name is not None else f"craft-{goal}"
    
    def get_grid_params(self):
        return (craft.WIDTH, craft.HEIGHT, self.world.cookbook.n_kinds)

    def step(self, action):
        _, next_state = self.curr_state.step(action)
        goal_achieved = next_state.satisfies("make/get", self.goal)
        reward = float(goal_achieved)
        curr_state = self.curr_state
        self.curr_state = next_state
        return next_state.features(), reward, bool(goal_achieved), {}#{'craft_state': curr_state, 'craft_next_state': next_state}
    
    def reset(self):
        self.curr_state = self.scenario.init()
        self.transitions = []
        return self.curr_state.features()
    
    def render(self):
        pass

    def seed(self, seed=None):
        pass
