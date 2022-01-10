
import torch
from torch import nn


class ProductPolicy(nn.Module):

    def __init__(self, model_1, model_2):
        super().__init__()
        self.model_1 = model_1
        self.model_2 = model_2
        

    def forward(self, state):
        logits = torch.log(nn.functional.softmax(self.model_1(state), dim=-1) * nn.functional.softmax(self.model_2(state), dim=-1))
        return torch.distributions.Categorical(logits=logits)