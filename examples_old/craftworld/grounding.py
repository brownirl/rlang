import sys, os
# from grounding.groundings.state.factor import Factor
# from grounding.groundings.state.predicate import Predicate

# sys.path.append(os.path.abspath("./"))

import yaml
import numpy as np
import torch
# from lmdp.grounding import *
from .craftworld.cookbook import Cookbook
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

# -----factors
end_map_idx = (n_objects + 1) * WIDTH * HEIGHT
grid_map = Factor(list(range(end_map_idx)), "grid_map")
inventory = Factor(list(range(end_map_idx, end_map_idx + n_objects)), "inventory")
delta_inventory = Factor(list(range(end_map_idx + n_objects, end_map_idx + 2 * n_objects)), name='delta_inventory')

end_inv = end_map_idx + 2 * n_objects
position = Factor(list(range(end_inv, end_inv + 2)), 'position')
direction = Factor(list(range(end_inv + 2, end_inv + 6)), 'direction')


# -----features

# x, y = position[0], position[1]  

@state_feature(dim=n_objects + 1)
def elements_to_use(state):
    _map = grid_map(state).reshape(((n_objects + 1), WIDTH, HEIGHT))
    _m = _map[n_objects]
    _at_view = _map[n_objects].nonzero()
    return _map[:, _at_view[0], _at_view[1]]


materials = {}
delta_elements = []
for p in primitives_elements + built_elements:
    materials.update({p: inventory[objects_to_idx[p]]})
    materials.update({"delta_" + p: delta_inventory[objects_to_idx[p]]})
    delta_elements += ["delta_" + p]

locals().update(materials)  # add variables for element features such as gold, iron, etc.

# -----symbols

# workbenches, water, boundary, stone
environment_elements = {}
for p in recipes['environment']:
    environment_elements.update({"at_" + p: Predicate(elements_to_use[objects_to_idx[p]] > 0)})

environment_predicates = list(environment_elements.keys())
locals().update(environment_elements)


# resource availability
def primitive_available(object):
    @predicate(name=f'there_is_{object}')
    def _there_is(state):
        _map = grid_map(state).reshape(((n_objects + 1), WIDTH, HEIGHT))
        _m = _map[objects_to_idx[object]].data.sum()
        return _m > 0

    return _there_is


elements = {}
for p in recipes['primitives']:
    elements.update({'there_is_' + p: primitive_available(p)})
availability_predicates = list(elements.keys())
locals().update(elements)


# -----subpolicies

# primitive actions
# actions = ["down", "up", "left", "right", "use"]
# down = DiscreteActionGrounding(0, name='down')
# up = DiscreteActionGrounding(1, name='up')
# left = DiscreteActionGrounding(2, name='left')
# right = DiscreteActionGrounding(3, name='right')
# use = DiscreteActionGrounding(4, name='use')


# go to cell

def go_to_cell(state, x, y):
    d = position(state) - np.array((x, y))  # manhattan distance
    if (abs(d[0]) + abs(d[1]) > 0):
        if (d[0] != 0):
            return right() if d[0] < 0 else left()
        else:
            return up() if d[1] < 0 else down()


# ======== clean up
vocab_terms = ['grid_map', 'inventory', 'delta_inventory', 'position',
               'elements_to_use'] + built_elements + delta_elements + primitives_elements \
              + environment_predicates + availability_predicates + actions
l = locals()
vocab = [l[p] for p in vocab_terms]
__all__ = vocab_terms + ['vocab']


def main(device='cpu'):
    from envs.craftworld.craftworld_gym import Craftworld
    from lmdp.grounding import State, BatchedState
    from envs.craftworld.craft import neighbors
    from all.environments.gym import GymEnvironment as allgym
    import random

    def direction_offset(direction):
        offset = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        idx = direction.nonzero()[0]
        return torch.Tensor(offset[int(idx)])

    craft = Craftworld('gold')
    index = craft.world.cookbook.index
    craft = allgym(craft, device=device)
    for obj in built_elements + primitives_elements + recipes['environment']:
        assert (objects_to_idx[obj] == index[obj])

    # batch test
    batch = []
    for _ in range(100):
        s = craft.step(random.randint(0, 4))
        batch.append(s['observation'])

    batch_state = BatchedState(batch)
    elements = elements_to_use(batch_state)
    assert elements.data.shape == (batch_state.data.shape[0], n_objects + 1)
    w = at_workshop2(batch_state)
    assert w.shape == (batch_state.data.shape[0],)

    for i in range(3):  # for all workshop
        for _ in range(1000):
            _st = craft.step(random.randint(0, 4))
            info = {'craft_state': _st['craft_state'], 'craft_next_state': _st['craft_next_state']}
            s = State(_st['observation'])

            _m = grid_map(s).reshape(((n_objects + 1), WIDTH, HEIGHT))
            _grid = _m[:-1].data.transpose(1, 2, 0) if isinstance(_m[:-1].data, np.ndarray) else _m[:-1].data.permute(1,
                                                                                                                      2,
                                                                                                                      0)
            inv = inventory(s)
            delta_inv = delta_inventory(s)
            _pos = position(s)

            assert torch.equal(_pos.data, torch.Tensor(info['craft_next_state'].pos).to(device))
            assert torch.equal(torch.Tensor(info['craft_next_state'].grid).to(device), _grid.data)
            assert torch.equal(inv.data, torch.Tensor(info['craft_next_state'].inventory).to(device))
            assert torch.equal(delta_inv.data, torch.Tensor(
                info['craft_next_state'].inventory - info['craft_next_state'].prev_inventory).to(device))

            pos = position(s).data + direction_offset(direction(s)).to(device)
            _n = neighbors(info['craft_next_state'].pos, info['craft_next_state'].dir)
            assert torch.equal(pos, torch.Tensor(_n[0]).to(device))

            _available = elements_to_use(s)
            nx, ny = _n[0]
            _true_available = info['craft_next_state'].grid[nx, ny]
            assert torch.equal(_available[:-1].data.squeeze(), torch.Tensor(_true_available).to(device))

            workshop_pos = _m[index[f"workshop{i}"]].nonzero()
            assert (pos[0] == workshop_pos[0] and pos[1] == workshop_pos[1]) == globals()[f'at_workshop{i}'](s)

            for env in recipes['environment']:
                t = _true_available[index[env]] > 0
                _t = globals()[f"at_{env}"](s)
                assert _t == t
                # assert (_true_available[index[env]] > 0) == globals()[f"at_{env}"](s)

            for env in recipes['primitives']:
                t = info['craft_next_state'].grid[:, :, index[env]].sum() > 0
                _t = globals()[f"there_is_{env}"](s).item()
                assert t == _t
                # assert (info['craft_next_state'].grid[:,:,index[env]].sum() > 0) == globals()[f"there_is_{env}"](s)


if __name__ == "__main__":
    main()
