''' ReinforceMLPLangAgentClass.py: Class for a language-informed REINFORCE agent, from:

    Williams, Ronald J. "Simple statistical gradient-following algorithms for
    connectionist reinforcement learning." Machine learning 8.3-4 (1992): 229-256.

    This implementation allows to initialize the policy table with prior information

    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: October 2020
'''

# Python imports.

# Other imports
import numpy as np
import torch

from agents.LangAgentClass import LangAgent


class ReinforceMLPLangAgent(LangAgent):
    ''' Class for REINFORCE agent
        MLP with softmax probs
    '''

    def __init__(self, actions, lmdp=None, state_dim=1, name="", gamma=0.95, alpha=0.01, N=5, hidden_size=16,
                 n_hidden_layers=1):
        name = "lang-reinforce" if name is "" else name
        reinforce_agent = ReinforceMLPLangAgent(actions, state_dim=state_dim, name=name, gamma=gamma, alpha=alpha, N=N,
                                                hidden_size=hidden_size, n_hidden_layers=n_hidden_layers)
        LangAgent.__init__(self, base_agent=reinforce_agent, lmdp=lmdp)

    def update_from_lang(self, state_space):
        '''
            State and action grounding
        '''
        self._init_policy(state_space)

    def _init_policy(self, state_space, iter=30):
        optim = torch.optim.SGD(self.policy_params.parameters(), lr=0.0001)
        # (state, action) pairs coming from language
        actions_vector = []
        states_vector = []
        for state in state_space:
            a = self.action_idx[self.lmdp.policy(state)]
            a = torch.Tensor([a]).long()
            # actions_vector.append(torch.nn.functional.one_hot(a, len(self.actions)).float())
            actions_vector.append(a)
            states_vector.append(state)

        n_states = len(actions_vector)
        rand = torch.randperm(n_states)
        states = torch.from_numpy(np.array(states_vector)).float()[rand]
        actions = torch.cat(actions_vector)[rand]
        minibatch_size = 2000

        # fit policy network
        for epoch in range(iter):
            for i in range(int(n_states / minibatch_size)):
                optim.zero_grad()
                logits = self.base_agent.policy_params(states[i * minibatch_size: (i + 1) * minibatch_size])
                loss = torch.nn.functional.cross_entropy(logits,
                                                         actions[i * minibatch_size: (i + 1) * minibatch_size]).mean()
                print(f"Epoch {epoch}: {loss}")
                loss.backward()
                optim.step()
