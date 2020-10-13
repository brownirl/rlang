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
        next_states = self.lmdp.transition(state, action)
        transitions = reduce(lambda x, y: x or y, map(lambda next: next(state_prime), next_states), False)
        if transitions:
            self.rmax_agent.t_s_a_counts[state][action] += 1
        return int(transitions)

    def default_rewards(self, state, action):
        r = self.lmdp.reward(state)
        if len(r) > 0:
            self.rmax_agent.r_s_a_counts[state][action] += 1
        return r
    
    def update_from_lang(self, state_space=None):
        '''
            Update rewards table with information and transition table from language
        '''
        self.rmax_agent.transitions = defaultdict(lambda state: defaultdict(lambda action: defaultdict(lambda state_prime: self.default_transition(state, action, state_prime))))
        self.rmax_agent.rewards = defaultdict(lambda state: defaultdict(lambda action: self.default_rewards(state, action)))
       
        # self._update_transitions_from_lang(state_space)
        # self._update_rewards_from_lang(state_space)

