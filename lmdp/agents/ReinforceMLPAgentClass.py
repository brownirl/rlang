''' ReinforceAgentClass.py: Class for a REINFORCE agent, from:

    Williams, Ronald J. "Simple statistical gradient-following algorithms for
    connectionist reinforcement learning." Machine learning 8.3-4 (1992): 229-256.

    Function Approximator Multilayer Perceptron

    Implemented by:
    Rafael Rodriguez-Sanchez (July 2020) rrs@brown.edu
'''

# Python imports.
from collections import defaultdict

# Other imports
import numpy as np
import torch
from simple_rl.agents.ReinforceAgentClass import ReinforceAgent

class ReinforceMLPAgent(ReinforceAgent):
    ''' Class for REINFORCE agent
        MLP with softmax probs
        with Baseline
    '''

    def __init__(self, actions, state_dim=1, name="", gamma=0.95, alpha=0.01, N=5, hidden_size=16, n_hidden_layers=1):
        name = "reinforce" if name is "" else name
        ReinforceAgent.__init__(self, name=name, actions=actions)    
        self._gamma = gamma
        self._alpha = alpha
        self._N = N
        self.trajectories = []
        self.curr_trajectory = []
        self.action_idx = dict(zip(actions, list(range(0, len(self.actions)))))
        self.hidden_size = hidden_size
        self.n_hidden_layers = n_hidden_layers
        layers = [torch.nn.Linear(state_dim, hidden_size), torch.nn.ReLU()] + [torch.nn.Linear(hidden_size, hidden_size), torch.nn.ReLU()]*n_hidden_layers + [torch.nn.Linear(hidden_size, len(self.actions)),]
        self.policy_params = torch.nn.Sequential(*layers)
        self.optimizer = torch.optim.Adam(self.policy_params.parameters(), lr=self._alpha)

    def get_parameters(self):
        param_dict = defaultdict(int)
        param_dict["gamma"] = self._gamma
        param_dict["alpha"] = self._alpha
        param_dict["N"] = self._N
        param_dict["n_hidden_layers"] = self.n_hidden_layers
        param_dict["hidden_size"] = self.hidden_size
        return param_dict

    def policy(self, state, training=True):
        '''
        Args:
            state (simple_rl.State)

        Returns:
            (str)
        '''
        pmf = torch.nn.functional.softmax(self.policy_params(torch.FloatTensor(state)), dim=-1)
        if training:
            # try:
                #action = self.actions[np.random.multinomial(1, pmf).tolist().index(1)]
            action = self.actions[torch.multinomial(pmf, 1)]
            # except ValueError:
            #     print(pmf)
        else: 
            action = self.actions[pmf.argmax()]
        return action


    def act(self, state, reward):
        '''
        Args:
            state (State)
            reward (float)

        Returns:
            (str)
        '''
        with torch.no_grad():
            action = self.policy(state)
        if self.prev_state is not None:
            self.curr_trajectory.append((self.prev_state, self.prev_action_idx, reward))
        self.prev_action = action
        self.prev_action_idx = self.action_idx[action]
        self.prev_state = state
        return action

    def update(self, state, action, reward, next_state):
        '''
        Args:
            state (State)
            action (str)
            reward (float)
            next_state (State)

        Summary:
            Perform an update of policy gradient.
        '''
        pass

    def end_of_episode(self):
        '''
            Overrides end_of_episode to compute part of the gradient
        '''
        self.trajectories.append(self.curr_trajectory)
        self.curr_trajectory = []
        self.prev_action = None
        self.prev_state = None
        if len(self.trajectories) >= self._N:
            self._take_grad()
            self.trajectories = []

    def _take_grad(self):
        self.optimizer.zero_grad()
        loss = self._loss()
        loss.backward()
        self.optimizer.step()

    def _loss(self):
        loss = 0.0
        for t in self.trajectories:
            states, actions, rewards = list(zip(*t))
            states = torch.from_numpy(np.array(states)).float()
            actions = torch.from_numpy(np.array(actions)).unsqueeze(1)
            G_t = torch.from_numpy(self._discouted_rewards(rewards, self._gamma))
            logprob = torch.gather(torch.log(torch.nn.functional.softmax(self.policy_params(states), dim=-1)), -1, actions).squeeze() 
            loss += torch.sum(logprob * G_t)
        return -loss/len(self.trajectories)

    def _discouted_rewards(self, rewards, gamma):
        R = np.array(rewards)
        exp = np.arange(0,len(rewards))[np.newaxis] - np.arange(0,len(rewards))[:, np.newaxis]
        discount = np.triu(gamma ** exp)
        discounted = R[np.newaxis] * discount
        return np.sum(discounted, axis=1) - np.mean(discount, axis=1)

if __name__=='__main__':
    reinforce_agent = ReinforceAgent(actions=['up', 'down'])
    print(reinforce_agent.get_parameters())