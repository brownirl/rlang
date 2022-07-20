import yaml
import numpy as np
from craftworld_env import Cookbook

import context
from rlang.grounding import Factor, Proposition, ActionReference

HEIGHT, WIDTH = 10, 10

recipes_path = 'craftworld_env/recipes.yaml'
cookbook = Cookbook(recipes_path)

with open(recipes_path) as recipes_f:
    recipes = yaml.safe_load(recipes_f)

objects_to_idx = cookbook.index
n_objects = cookbook.n_kinds
primitives_elements = recipes['primitives']
built_elements = list(recipes['recipes'].keys())

end_map_idx = (n_objects + 1) * WIDTH * HEIGHT
end_inv = end_map_idx + 2 * n_objects

"""
Factors
"""

_grid_map = slice(0, end_map_idx)
_inventory = slice(end_map_idx, end_map_idx + n_objects)
_delta_inventory = slice(end_map_idx + n_objects, end_map_idx + 2 * n_objects)
_position = slice(end_inv, end_inv + 2)
_direction = slice(end_inv + 2, end_inv + 6)

grid_map = Factor(_grid_map, 'grid_map')
inventory = Factor(_inventory, 'inventory')
delta_inventory = Factor(_delta_inventory, 'delta_inventory')
position = Factor(_position, 'position')
direction = Factor(_direction, 'direction')

"""
Features
"""


def elements_to_use(state):
    _map = grid_map(state=state).reshape(((n_objects + 1), WIDTH, HEIGHT))
    _m = _map[n_objects]
    _at_view = _map[n_objects].nonzero()
    return _map[:, _at_view[0], _at_view[1]]


materials = {}
delta_elements = []
for p in primitives_elements + built_elements:
    materials.update({p: inventory[objects_to_idx[p]]})
    materials.update({"delta_" + p: delta_inventory[objects_to_idx[p]]})
    materials[p].name = p
    materials["delta_" + p].name = "delta_" + p
    delta_elements += ["delta_" + p]

locals().update(materials)

"""
Propositions
"""

# workbenches, water, boundary, stone
environment_elements = {}
for p in recipes['environment']:
    environment_elements.update({"at_" + p: Proposition(lambda state: elements_to_use(state)[objects_to_idx[p]] > 0, name=f"at_{p}")})

environment_propositions = list(environment_elements.keys())
locals().update(environment_elements)


# resource availability
def primitive_available(obj):
    def _there_is(state):
        _map = grid_map(state).reshape(((n_objects + 1), WIDTH, HEIGHT))
        _m = _map[objects_to_idx[obj]].data.sum()
        return _m > 0

    return _there_is


elements = {}
for p in recipes['primitives']:
    elements.update({'there_is_' + p: primitive_available(p)})
availability_predicates = list(elements.keys())
locals().update(elements)

"""
Actions, Policies, and Options
"""

down = ActionReference(0, name='down')
up = ActionReference(1, name='up')
left = ActionReference(2, name='left')
right = ActionReference(3, name='right')
use = ActionReference(4, name='use')


def go_to_cell(state, x, y):
    d = position(state) - np.array((x, y))  # manhattan distance
    if abs(d[0]) + abs(d[1]) > 0:
        if d[0] != 0:
            return right() if d[0] < 0 else left()
        else:
            return up() if d[1] < 0 else down()


# TODO: Need to make options for building each item in the cookbook
# go_to_cell until the option condition is satisfied for a specific recipe, then execute option policy until termination
