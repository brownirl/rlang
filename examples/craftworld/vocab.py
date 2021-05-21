import sys, os
sys.path.append(os.path.abspath("./"))


import yaml
import numpy as np
import torch
from lmdp.grounding import *
from envs.craftworld.cookbook import Cookbook
import sys, os
sys.path.append(os.path.abspath("./"))

HEIGHT, WIDTH = 10, 10

recipes_path = 'envs/craftworld/recipes.yaml'

### Inventory Coding

cookbook = Cookbook(recipes_path)

with open(recipes_path) as recipes_f:
    recipes = yaml.load(recipes_f)

# idx = 1
# objects_to_idx = {}
# idx_to_objects = {}
# for t in ('environment', 'primitives', 'recipes'):
#     l = recipes[t] if isinstance(recipes[t], (list, tuple)) else list(recipes[t].keys())
#     idx_to_objects.update(dict(zip(range(idx, idx+len(l)), l))) 
#     objects_to_idx.update(dict(zip(l, range(idx, idx+len(l)))))
#     idx += len(recipes[t])

objects_to_idx = cookbook.index
n_objects = cookbook.n_kinds
primitives_elements = recipes['primitives']
built_elements = list(recipes['recipes'].keys())

#### VOCABULARY

#-----factors
end_map_idx = (n_objects+1) * WIDTH * HEIGHT
grid_map = StateFactor(list(range(end_map_idx)), "grid_map")
inventory = StateFactor(list(range(end_map_idx, end_map_idx + n_objects)), "inventory")
delta_inventory = StateFactor(list(range(end_map_idx + n_objects, end_map_idx + 2*n_objects)))

end_inv = end_map_idx + 2*n_objects
position = StateFactor(list(range(end_inv, end_inv+2)), 'position')
direction = StateFactor(list(range(end_inv+2, end_inv+6)), 'direction')
#-----features

x, y = position[0], position[1]  

@state_feature(dim=n_objects+1)
def elements_to_use(state):
    _map = grid_map(state).reshape(((n_objects+1), WIDTH, HEIGHT))
    _at_view = _map[n_objects].nonzero() if isinstance(_map, np.ndarray) else _map[n_objects].nonzero(as_tuple=True) 
    return _map[:, _at_view[0], _at_view[1]]

materials = {}
delta_elements = []
for p in primitives_elements + built_elements:
    materials.update({p: inventory[objects_to_idx[p]]})
    materials.update({"delta_"+p: delta_inventory[objects_to_idx[p]]})
    delta_elements += ["delta_"+p]

locals().update(materials) # add variables for element features such as gold, iron, etc.    

#-----symbols 

# workbenches, water, boundary, stone
environment_elements = {}
for p in recipes['environment']:
    environment_elements.update({"at_"+p: Symbol(elements_to_use[objects_to_idx[p]] > 0, name="at_"+p)})

environment_symbols = list(environment_elements.keys())
locals().update(environment_elements)

# resource availability
elements = {}
for p in recipes['primitives']:
    elements.update({'there_is_' + p: Symbol(elements_to_use[objects_to_idx[p]] > 0, name='there_is_' + p)})
availability_symbols = list(elements.keys())
locals().update(elements) 

#-----subpolicies

# primitive actions
actions = ["down", "up", "left", "right", "use"]
down = DiscreteActionGrounding(0, name='down')
up = DiscreteActionGrounding(1, name='up')
left = DiscreteActionGrounding(2, name='left')
right = DiscreteActionGrounding(3, name='right')
use = DiscreteActionGrounding(4, name='use')


# go to cell

def go_to_cell(state, x, y):
    d = position(state) - np.array((x, y)) # manhattan distance
    if(abs(d[0]) + abs(d[1]) > 0):
        if(d[0] != 0):
            return right() if d[0] < 0 else left()
        else:
            return up() if d[1] < 0 else down()


#======== clean up
vocab_terms = ['grid_map', 'inventory', 'delta_inventory', 'position', 'elements_to_use'] + built_elements + delta_elements + primitives_elements   \
        + environment_symbols + availability_symbols + actions
l = locals()
vocab = [l[p] for p in vocab_terms]
__all__ = vocab_terms + ['vocab']


if __name__ == '__main__':
    from envs.craftworld.craftworld_gym import Craftworld
    from lmdp.grounding.states.StateClass import State

    def direction_offset(direction):
        offset = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        idx = direction.nonzero()[0]
        return np.array(offset[int(idx)])


    craft = Craftworld('gold')
    index = craft.world.cookbook.index
    for obj in built_elements + primitives_elements + recipes['environment']:
        # print(f"{obj}: {objects_to_idx[obj]} ?== {index[obj]}")
        assert (objects_to_idx[obj]== index[obj])


    for i in range(3): # for all workshop
        init = craft.reset()
        s = State(init)
        _m = grid_map(s).reshape(((n_objects+1), WIDTH, HEIGHT))
        pos = position(s) + direction_offset(direction(s))
        workshop_pos = _m[index[f"workshop{i}"]].nonzero()

        assert (pos[0] == workshop_pos[0] and pos[1] == workshop_pos[1]) == locals()[f'at_workshop{i}'](s)
        
        # _m = grid_map(s).reshape(((n_objects+1), WIDTH, HEIGHT))
        # _m[-1] = np.zeros((10,10))
        # _m[-1, workshop_pos[0],workshop_pos[1]] = 1
        # _inv = inventory(s)
        # _delta_inv = delta_inventory(s)
        # s_prime = State(np.concatenate((_m.flatten(), _inv, _delta_inv)))

        # pos = position(s_prime)
        # assert (pos[0] == workshop_pos[0] and pos[1] == workshop_pos[1]) == locals()[f'at_workshop{i}'](s_prime)
