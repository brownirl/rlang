
import torch
from torch import nn

from rlang import parse_file, parse
from rlang.src.grounding import State, Action


class RLangPolicy(nn.Module):
    def __init__(self, rlang_policy, epsilon=1e-8, n_actions=2, obs_normalizer=None):
        self.rlang_policy = rlang_policy
        self.eps = epsilon
        self.n_actions = n_actions
        self.obs_normalizer = obs_normalizer
        super().__init__()


    def _dict_to_tensor(self, state):
        actions_prob = torch.zeros(self.n_actions, device=state.device)
        actions_mask = torch.zeros(self.n_actions, device=state.device)
        for action, prob in self.rlang_policy(state=state).items():
            actions_prob[action] = prob
            actions_mask[action] = 1
        if len(actions_prob) < self.n_actions: # redistribute the remaining prob uniformly
            remaining_prob = (1. - actions_prob.sum()) / (len(actions_prob)-self.n_actions)
            actions_prob = torch.Tensor(actions_prob)
            actions_prob -= self.eps * (len(actions_prob)-self.n_actions) if remaining_prob == 0 else actions_prob
            remaining_prob = self.eps if remaining_prob == 0 else remaining_prob
            actions_prob += (1-actions_mask) * remaining_prob
        else:
            if (actions_prob == 0).any():
                actions_prob += self.eps
        
        return torch.log(actions_prob/actions_prob.sum()).unsqueeze(0)

    def forward(self, state):
        state = self.obs_normalizer.inverse(state) if self.obs_normalizer is not None else state
        batch = state.size()[0]
        if batch == 1:
            return self._dict_to_tensor(state[0])
        else:
            acts = [self._dict_to_tensor(state[i]) for i in range(batch)]
            return torch.cat(acts, dim=0)
            
    def set_obs_normalizer(self, obs_normalizer):
        self.obs_normalizer = obs_normalizer


if __name__=="__main__":
    knowledge = parse_file("examples/lunar_lander/suboptimal_policy.rlang")

    s = State([[0.1, 0.2, 0.4, 0.2, 0.005, 0.03, 0, 0], [0.1, 0.2, 0.4, 0.2, 0.05, 0.03, 0, 0]])

    policy = RLangPolicy(knowledge['fall_in_place'], n_actions=4)

    print(torch.exp(policy(torch.from_numpy(s))))