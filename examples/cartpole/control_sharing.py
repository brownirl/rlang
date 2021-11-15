

import torch
from torch import nn 
from torch.distributions import Categorical
from torch.distributions.utils import lazy_property

class ControlSharingActionDistribution(Categorical, nn.Module):

    def __init__(self, beta, logits_1, logits_2):
        nn.Module.__init__(self)
        Categorical.__init__(self, logits=logits_1)
        
        self.beta = torch.Tensor([beta])
        self.logits_1 = logits_1
        self.logits_2 = logits_2
        assert (logits_2.size() == logits_1.size())
        self.categorical_1 = Categorical(logits=logits_1)
        self.categorical_2 = Categorical(logits=logits_2)
        

    def entropy(self):
        log_probs = self.log_prob(torch.arange(self._num_events))
        probs = torch.exp(log_probs)
        entropy = probs * log_probs
        return -entropy.sum(-1)

    def sample(self, sample_shape=torch.Size()):
        policy = torch.bernoulli(torch.ones(sample_shape) * self.beta)
        _sample = policy * self.categorical_1.sample(sample_shape=sample_shape) + \
                (1-policy) * self.categorical_2.sample(sample_shape=sample_shape)
        return _sample.int()

    def log_prob(self, value):
        prob_1 = self.categorical_1.log_prob(value) + torch.log(self.beta)
        prob_2 = self.categorical_2.log_prob(value) + torch.log(1-self.beta)
        probs = torch.stack([prob_1.unsqueeze(0), prob_2.unsqueeze(0)], dim=0)
        return torch.logsumexp(probs, dim=0)

    @lazy_property
    def logits(self):
        return self.log_prob(torch.arange(self._num_events))

    @lazy_property
    def probs(self):
        return torch.exp(self.log_prob(torch.arange(self._num_events)))


class ControlSharingPolicy(nn.Module):
    def __init__(self, learning_policy_model, advice_policy, beta_scheduler):
        nn.Module.__init__(self)
        self.policy_model = learning_policy_model
        self.advice_policy = advice_policy
        self.beta = beta_scheduler
        

    def forward(self, state):
        logits_1 = self.advice_policy(state)
        logits_2 = self.policy_model(state)
        beta = self.beta()
        return ControlSharingActionDistribution(beta, logits_1=logits_1, logits_2=logits_2)

if __name__=="__main__":
    a = torch.log(torch.Tensor([0.5, 0.5]))
    b = torch.log(torch.Tensor([0.25, 0.75]))
    beta = 0.75

    dist = ControlSharingActionDistribution(beta, a, b)

    samples = dist.sample(sample_shape=torch.Size([10000]))
    prob_0 = (samples == 0).sum()/samples.size(-1)
    prob_1 = (samples == 1).sum()/samples.size(-1)

    print(f"ApproxProb0: {prob_0}, ApproxProb1: {prob_1}")
    print(f"Entropy: {dist.entropy()}")
    print(f"Entropy(emp): {-prob_0 * torch.log(prob_0) - prob_1 * torch.log(prob_1)}")
    print(f"Prob0: {torch.exp(dist.log_prob(torch.Tensor([0])))}, Prob1: {torch.exp(dist.log_prob(torch.Tensor([1])))}")
    print(f"Prob0: {beta * torch.exp(a[0]) + (1-beta)*torch.exp(b[0])}, Prob1: {beta * torch.exp(a[1]) + (1-beta)*torch.exp(b[1])}")
    assert (beta * torch.exp(a) + (1-beta)*torch.exp(b) == torch.exp(dist.log_prob(torch.arange(a.size()[-1])))).all()