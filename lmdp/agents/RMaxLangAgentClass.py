import random
import numpy as np
from simple_rl.agents.AgentClass import Agent
from simple_rl.agents.RMaxAgentClass import RMaxAgent

from lmdp.agents.LangAgentClass import LangAgent
from lmdp.utils.collections import defaultdict

from functools import reduce


class RMaxLangAgent(LangAgent):
    def __init__(self, actions, gamma=0.95, s_a_threshold=2, epsilon_one=0.99,
                        max_reward=1.0, lmdp=None, name="LangRMax", custom_q_init=None):
        rmax_agent = RMaxAgent(actions, gamma=gamma, s_a_threshold=s_a_threshold, epsilon_one=epsilon_one,
                                max_reward=max_reward, name=name, custom_q_init=custom_q_init)
        LangAgent.__init__(self, base_agent=rmax_agent, lmdp=lmdp)
        self.rmax_agent = self.base_agent
        self.r_s_a_counts = defaultdict(lambda *args: defaultdict(lambda *args: int(0)))
        self.t_s_a_counts = defaultdict(lambda *args: defaultdict(lambda *args: int(0)))

    def reset(self):
        self.rmax_agent.reset()
        
        self.transitions = defaultdict(lambda state: defaultdict(lambda action: defaultdict(lambda state_prime: self.default_transition(state, action, state_prime))))
        self.rewards = defaultdict(lambda state: defaultdict(lambda action: self.default_rewards(state, action)))
        self.q_func = self.initialize_q_function(self.state_space, self.rmax_agent.actions)
        self.r_s_a_counts = defaultdict(lambda *args: defaultdict(lambda *args: int(0)))
        self.t_s_a_counts = defaultdict(lambda *args: defaultdict(lambda *args: int(0)))
        self.rmax_agent.q_func = self.q_func


    def _update_transitions_from_lang(self, state_space):
        '''
        Update transition table with information from language
        This function adds the transition specify through language as a single sample (s, a, s').
        Args:
            state_space: Iterable of states of the MDP
        '''
        for state in state_space:
            for action in self.actions:
                next_state_symbol = self.lmdp.transition(state, action)
                for state_prime in [s for s in state_space if next_state_symbol(state_prime)]:
                    self.rmax_agent.transitions[state][action][state_prime] = 1
                    self.rmax_agent.t_s_a_counts[state][action] += 1
    
    def _update_transitions_from_lang(self, state_space):
        '''
        Update transition table with information from language
        This function adds the transition specify through language as a single sample (s, a, s').
        Args:
            state_space: Iterable of states of the MDP
        '''
        for state in state_space:
            for action in self.actions:
                reward = self._lmdp.reward(state)
                self.rmax_agent.rewards[state][action] = reward
                if len(reward) > 0:
                    self.rmax_agent.r_s_a_counts[state][action] += 1


    def default_transition(self, state, action, state_prime):
        next_states = tuple(map(lambda x: x[1], filter(lambda x: x[0], self.lmdp.transition(state, action))))
        if (next_states is not None and len(next_states) > 0):
            transitions = reduce(lambda x, y: x or y, map(lambda n_state: n_state(state_prime), next_states), False)
            if transitions:
                self.t_s_a_counts[state][action] += 1
            return int(transitions)
        return int(0)

    def default_rewards(self, state, action):
        r = tuple(map(lambda x: x[1], filter(lambda x: x[0], self.lmdp.reward(state, action, state))))
        if len(r) > 0:
            self.r_s_a_counts[state][action] += 1
        else:
            r = []
        return r
    

    def initialize_q_function(self, state_space, action_space):
        q_function = defaultdict(lambda *args: defaultdict(lambda *args: self.rmax_agent.rmax))
        lim = int(np.log(1/(self.rmax_agent.epsilon_one * (1 - self.rmax_agent.gamma))) / (1 - self.rmax_agent.gamma))
        for _ in range(1, lim):
            for s in state_space():
                for a in action_space:
                    r = self.rewards[s][a]
                    if (self.rewards[s][a] is not None and len(r) > 0):
                        q_function[s][a] = float(sum(r))/len(r)
                        s_primes = [s_prime for s_prime in state_space() if self.rmax_agent.transitions[s][a][s_prime] != 0]
                        if len(s_primes) > 0:
                            q_function[s][a] += self.rmax_agent.gamma *  sum(map(lambda s_prime: self.__get_max_q(q_function, s_prime), s_primes))/len(s_primes)
        return q_function

    def __get_max_q(self, q, s):
        return max(q[s].values())

    def update_from_lang(self, state_space=None):
        '''
            Update rewards table with information and transition table from language
        '''
        self.state_space = state_space
        self.reset()

