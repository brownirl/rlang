import yaml
import numpy as np
from lmdp.grounding import *

import sys, os
sys.path.append(os.path.abspath("./"))

HEIGHT, WIDTH = 10, 10

recipes_path = 'envs/craftworld/recipes.yaml'

### Inventory Coding
with open(recipes_path) as recipes_f:
    recipes = yaml.load(recipes_f)

idx = 0
objects_to_idx = {}
idx_to_objects = {}
for t in ('environment', 'primitives', 'recipes'):
    l = recipes[t] if isinstance(recipes[t], (list, tuple)) else list(recipes[t].keys())
    idx_to_objects.update(dict(zip(range(idx, idx+len(l)), l))) 
    objects_to_idx.update(dict(zip(l, range(idx, idx+len(l)))))
    idx += len(recipes[t])

n_objects = idx+1
primitives_elements = recipes['primitives']
built_elements = list(recipes['recipes'].keys())

#### VOCABULARY

#-----factors
end_map_idx = (n_objects+1) * WIDTH * HEIGHT
grid_map = StateFactor(list(range(end_map_idx)), "grid_map")
inventory = StateFactor(list(range(end_map_idx, end_map_idx + n_objects)), "inventory")


#-----features 
@state_feature(dim=2)  # state feature 'position'
def position(state):
    _map = grid_map(state).reshape(((n_objects+1), WIDTH, HEIGHT))
    _agent_pos = _map[n_objects] # position map
    row, col = np.nonzero(_agent_pos) # position indices
    return np.array((col, row))

x, y = position[0], position[1]  

@state_feature(dim=n_objects+1)
def elements_at_position(state):
    _map = grid_map(state).reshape(((n_objects+1), WIDTH, HEIGHT))
    return _map[:, y(state), x(state)]

materials = {}
for p in primitives_elements + built_elements:
    materials.update({p: inventory[objects_to_idx[p]]})

locals().update(materials) # add variables for element features such as gold, iron, etc.    

#-----symbols 

# workbenches, water, boundary, stone
environment_elements = {}
for p in recipes['environment']:
    environment_elements.update({"at_"+p: Symbol(elements_at_position[objects_to_idx[p]] > 0, name="at_"+p)})

environment_symbols = list(environment_elements.keys())
locals().update(environment_elements)

# resource availability
elements = {}
for p in recipes['primitives']:
    elements.update({'there_is_' + p: Symbol(elements_at_position[objects_to_idx[p]] > 0, name='there_is_' + p)})
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
vocab_terms = ['grid_map', 'inventory', 'position', 'elements_at_position'] + built_elements + primitives_elements   \
        + environment_symbols + availability_symbols + actions
l = locals()
vocab = [l[p] for p in vocab_terms]
__all__ = vocab_terms + ['vocab']
