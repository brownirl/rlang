
import yaml
import numpy as np
from lmdp.grounding import *

GRID_HEIGHT, GRID_WIDTH = 5, 5
recipes_path = 'lmdp/envs/craftworld/recipes.yaml'

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

## Utils
def ravel_idx(x, y, z):
    if (isinstance(x, int)):
        x = slice(x, x+1)
    if (isinstance(y, int)):
        y = slice(y, y+1)
    if (isinstance(z, int)):
        z = slice(z, z+1)
    
    indices = np.mgrid[z, x, y].reshape(3, -1).astype(int)
    return np.ravel_multi_index(indices, (idx, GRID_WIDTH, GRID_HEIGHT))

#### VOCABULARY

#-----factors
grid_view = StateFactor(list(range(GRID_HEIGHT*GRID_HEIGHT*idx)), "grid_view")
grid_big_view = StateFactor(list(range(GRID_HEIGHT*GRID_HEIGHT*idx, 2*GRID_HEIGHT*GRID_HEIGHT*idx)), "grid_big_view")
inventory = StateFactor(list(range(2*GRID_HEIGHT*GRID_HEIGHT*idx, 2*GRID_HEIGHT*GRID_HEIGHT*idx + idx)), "inventory")
position = StateFactor(list(range(2*GRID_HEIGHT*GRID_HEIGHT*idx + idx+ 4, 2*GRID_HEIGHT*GRID_HEIGHT*idx + idx+ 4+2)), "position")
x = position[0]
y = position[1]

#-----features 
elements = {}
for p in recipes['primitives']:
    elements.update({p: inventory[objects_to_idx[p]]})

locals().update(elements) # add variables for element features such as gold, iron, etc.    

# current-position elements
# current_elements = grid_view[ravel_idx(int(GRID_WIDTH/2), int(GRID_HEIGHT/2), slice(0,idx))] 
current_elements = StateFeature(lambda state: grid_view(state)[ravel_idx(x, y, slice(idx))], idx, "current_elements")
mid_position = (int(GRID_WIDTH/2), int(GRID_HEIGHT/2))
# elements in neighboring directions.
down_left = grid_big_view[ravel_idx(mid_position[0], mid_position[1], slice(0,idx))]
down_right = grid_big_view[ravel_idx(mid_position[0]+1, mid_position[1], slice(0,idx))]
up_left = grid_big_view[ravel_idx(mid_position[0], mid_position[1]+1, slice(0,idx))]
up_right = grid_big_view[ravel_idx(mid_position[0]+1, mid_position[1]+1, slice(0,idx))]

#-----symbols 

# workbenches, water, boundary, stone
environment_elements = {}
for p in recipes['environment']:
    environment_elements.update({"at_"+p: Symbol(current_elements[objects_to_idx[p]] > 0, name="at_"+p)})

locals().update(environment_elements)
# resource availability
elements = {}
for p in recipes['primitives']:
    elements.update({'there_is_' + p: Symbol(current_elements[objects_to_idx[p]] > 0, name='there_is_' + p)})

locals().update(elements) 

#-----subpolicies

# primitive actions
actions = ("down", "up", "left", "right", "use")
actions = dict(zip(actions, range(len(actions))))
locals().update(actions)

# go to cell

def go_to_cell(state, x, y):
    d = position(state) - np.array((x, y)) # manhattan distance
    if(abs(d[0]) + abs(d[1]) > 0):
        if(d[0] != 0):
            return actions["right"] if d[0] < 0 else actions["left"]
        else:
            return actions["up"] if d[1] < 0 else actions["down"]

# collect material
