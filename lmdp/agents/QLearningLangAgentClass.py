'''
    Language-informed Q-Learning Agent
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: v0 September 2020
          v1 February 2021
'''
from simple_rl.agents.QLearningAgentClass import QLearningAgent
from lmdp.agents.LangAgentClass import LangAgent
from lmdp.utils.collections import defaultdict
from functools import reduce
import numpy as np

import time 


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
        
        self.transitions = defaultdict(lambda state: defaultdict(lambda action: defaultdict(lambda state_prime: self.default_transition(state, action, state_prime))))
        self.rewards = defaultdict(lambda state: defaultdict(lambda action: self.default_rewards(state, action)))
        self.q_func = self.initialize_q_function(self.state_space, self.base_agent.actions) # value iteration with q_func default
        self.base_agent.q_func = self.q_func



    # def lang_q_func(self, state, action):
    #     '''
    #         Priority-based implementation: 1. value for (s,a) specified; 2. Reward for (s,a) specified 3. action specified.
    #         TODO: abstract this function away from the class to allow easy integration with an "interpreter"
    #     '''

    #     value = self.lmdp.value(state)
    #     reward = self.lmdp.reward(state)
    #     rec_action = self.lmdp.policy(state)

    #     if len(value) > 0:
    #         return sum(value)/len(value) # mean value.
    #     elif len(reward) > 0:
    #         return sum(reward)/len(reward) # mean reward.
    #     elif action is not None and rec_action == action:
    #         return QLearningLangAgent.MAX_Q
    #     else:
    #         return QLearningLangAgent.DEFAULT_Q
            
  
    def default_transition(self, state, action, state_prime):
        next_states = self.lmdp.transition(state, action)
        if (next_states is not None and len(next_states) > 0):
            transitions = reduce(lambda x, y: x or y, map(lambda n_state: n_state(state_prime), next_states), False)
            return int(transitions)
        return int(0)

    def default_rewards(self, state, action):
        r = self.lmdp.reward(state, action, state)
        if len(r) <= 0:
            r = []
        return r

    def default_q_func(self, state, action):  # default q_function is the same value for all actions
        v = self.lmdp.value(state)
        if len(v) <= 0:
            return 0
        return sum(v)/len(v) # return mean

    def initialize_q_function(self, state_space, action_space): # Value iteration initialization
        q_function = defaultdict(lambda state: defaultdict(lambda action: self.default_q_func(state, action)))
        lim = 10#int(np.log(1/(self.epsilon_one * (1 - self.base_agent.gamma))) / (1 - self.base_agent.gamma))
        for _ in range(1, lim):
            start = time.clock()
            for s in state_space():
                for a in action_space:
                    r = self.rewards[s][a]
                    if (self.rewards[s][a] is not None and len(r) > 0):
                        q_function[s][a] =  float(sum(r))/len(r)
                        s_primes = [s_prime for s_prime in state_space() if self.transitions[s][a][s_prime] != 0]
                        if len(s_primes) > 0:
                            q_function[s][a] += self.base_agent.gamma *  sum(map(lambda s_prime: self.__get_max_q(q_function, s_prime), s_primes))/len(s_primes)
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