'''
    Language-informed Q-Learning Agent
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: v0 September 2020
          v1 February 2021
'''
from simple_rl.agents.QLearningAgentClass import QLearningAgent
from lmdp.agents.LangAgentClass import LangAgent
from lmdp.utils.collections import defaultdict, arraydict, Index
from functools import reduce
from collections import namedtuple
import numpy as np

import time 


indices = namedtuple("SAIndex", ["state_space", "action_space"])
def _indices(state_space_gen, action_space):
    return indices(Index(state_space_gen()), Index(action_space))

class QLearningLangAgent(LangAgent):
    DEFAULT_Q = 0
    MAX_Q = 1
    def __init__(self, actions, name="lang-qlearning", lmdp=None, alpha=0.1, gamma=0.99,
                 epsilon=0.1, explore="uniform", anneal=False,
                 custom_q_init=None, default_q=0):
        self.epsilon_one = 0.99
        q_agent = QLearningAgent(actions, name=name, alpha=alpha, gamma=gamma, epsilon=epsilon, explore=explore, anneal=anneal, custom_q_init=custom_q_init, default_q=default_q)
        LangAgent.__init__(self, base_agent=q_agent, lmdp=lmdp)


    def reset(self):
        self.base_agent.reset()
        
        # self.transitions = defaultdict(lambda state: defaultdict(lambda action: defaultdict(lambda state_prime: self.default_transition(state, action, state_prime))))
        # self.rewards = defaultdict(lambda state: defaultdict(lambda action: self.default_rewards(state, action)))
        # self.q_func = self.initialize_q_function(self.state_space, self.base_agent.actions) # value iteration with q_func default
        self.indices = _indices(self.state_space, self.base_agent.actions)
        self.transitions = arraydict(len(self.indices.state_space), len(self.indices.action_space), len(self.indices.state_space), 
                                     index=self.indices + (self.indices.state_space,))
        
        self.rewards = arraydict(len(self.indices.state_space), len(self.indices.action_space), len(self.indices.state_space), 
                                     index=self.indices + (self.indices.state_space,))
        self.q_func = arraydict(len(self.indices.state_space), len(self.indices.action_space), 
                                     index=self.indices)

        self.__init_functions()
        self.q_func.data = self.initialize_q_function(self.state_space, self.base_agent.actions)
        self.base_agent.q_func = self.q_func
            
    def __init_functions(self):
        for s in self.indices.state_space.elems():
            for a in self.indices.action_space.elems():
                self.q_func[s,a] = self.default_q_func(s,a)
                for s_prime in self.indices.state_space.elems():
                    self.rewards[s,a,s_prime] = self.default_rewards(s, a, s_prime)
                    self.transitions[s,a,s_prime] = self.default_transition(s, a, s_prime)

    def default_transition(self, state, action, state_prime):
        next_states = self.lmdp.transition(state, action)
        if (next_states is not None and len(next_states) > 0):
            transitions = reduce(lambda x, y: x or y, map(lambda n_state: n_state(state_prime), next_states), False)
            return int(transitions)
        return int(0)

    def default_rewards(self, state, action, s_prime):
        r = self.lmdp.reward(state, action, s_prime)
        if len(r) <= 0:
            r = [0]
        return sum(r)/len(r) # return mean

    def default_q_func(self, state, action):  # default q_function is the same value for all actions
        v = self.lmdp.value(state)
        if len(v) <= 0:
            return [0]
        return sum(v)/len(v) # return mean

    def initialize_q_function(self, state_space, action_space): # Value iteration initialization
        q_function = self.q_func.numpy()
        lim = int(np.log(1/(self.epsilon_one * (1 - self.base_agent.gamma))) / (1 - self.base_agent.gamma))
        start = time.clock()
        for _ in range(1, lim):
            
            value_function = q_function[:, :, np.newaxis].max(axis=1, keepdims=True).transpose((2,1,0))
            q_function = self.rewards.numpy().mean(-1) + self.base_agent.gamma * (self.transitions.numpy() * value_function).mean(-1)
            # for s in state_space():
            #     for a in action_space:
            #         r = self.rewards[s][a]
            #         if (self.rewards[s][a] is not None and len(r) > 0):
            #             q_function[s][a] =  float(sum(r))/len(r)
            #             s_primes = [s_prime for s_prime in state_space() if self.transitions[s][a][s_prime] != 0]
            #             if len(s_primes) > 0:
            #                 q_function[s][a] += self.base_agent.gamma *  sum(map(lambda s_prime: self.__get_max_q(q_function, s_prime), s_primes))/len(s_primes)
            
            
        end = time.clock()
        print(f"{end-start}s")
        return q_function

    def __get_max_q(self, q, s):
        q_values = q[s].values()
        if len(q_values) > 0:
            return max(q_values)
        return 0

    def update_from_lang(self, state_space=None):
        '''
            Update rewards table with information and transition table from language
        '''
        self.state_space = state_space
        self.reset()


