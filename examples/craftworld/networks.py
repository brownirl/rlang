import torch
import torch.nn as nn
from all.nn import Linear0


cnns = [32, 64, 96, 128]
kernel_size = 3
stride = 2

def gridCNN(in_channels=10):
    return nn.Sequential(
                nn.Conv2d(in_channels, cnns[0], kernel_size, stride, padding=(6,6)),
                nn.ReLU(),
                nn.Conv2d(cnns[0], cnns[1], kernel_size, stride, padding=(6,6)),
                nn.ReLU(),
                nn.Conv2d(cnns[1], cnns[2], kernel_size, stride, padding=(6,6)),
                nn.ReLU(),
                nn.Conv2d(cnns[2], cnns[3], kernel_size, stride, padding=(6,6)),
                nn.ReLU(),
                nn.Flatten()
            )
def invMLP(in_features=10):
    return nn.Sequential(
                nn.Linear(in_features, 32),
                nn.ReLU(),
                nn.Linear(32, 32)   
    )


def fc_policy_head(in_features=256):
    def _head(env):
        return nn.Sequential(
            nn.Linear(in_features, 128),
            nn.ReLU(),
            Linear0(128, env.action_space.n)
        )
    return _head

def fc_value_head(in_features=256):
    def _head():
        return nn.Sequential(
            nn.Linear(in_features, 128),
            nn.ReLU(),
            nn.Linear(128, 1)
        )
    return _head



class CraftFeature(nn.Module):
    def __init__(self, width, height, elements, out=256):
        nn.Module.__init__(self)
        self.grid_feats = gridCNN(elements + 1)
        self.inv_feats = invMLP(elements)
        self.affine = nn.Linear(100*128+32, 256)
        self._elements = elements
        self._width = width
        self._height = height

    def forward(self, state):
        batch_dims = state.shape[:-1]
        grid = state[..., :-self._elements].reshape((*batch_dims, self._elements+1, self._width, self._height))
        grid = self.grid_feats(grid)
        inv = self.inv_feats(state[..., -self._elements:])
        return self.affine(torch.cat((grid, inv), dim=-1))

class CraftFeatureNetwork(nn.Module):
    feats = None
    def __init__(self, width, height, elements, out=256):
        nn.Module.__init__(self)
        if CraftFeatureNetwork.feats is None:
            CraftFeatureNetwork.feats = CraftFeature(width, height, elements, out)
    
    def __call__(self, *args):
        return CraftFeatureNetwork.feats

    def forward(self, state):
        if CraftFeatureNetwork.feats is not None:
            return CraftFeatureNetwork.feats.forward(state)
        raise ValueError("CraftNetwork not initialized!")