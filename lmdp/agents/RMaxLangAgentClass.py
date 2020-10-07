import random
import numpy as np
from simple_rl.agents.AgentClass import Agent
from simple_rl.agents.RMaxAgentClass import RMaxAgent

from lmdp.agents.LangAgentClass import LangAgent
from lmdp.utils.collections import defaultdict



class RMaxLangAgent(LangAgent):
    def __init__(self, actions, gamma=0.95, s_a_threshold=2, epsilon_one=0.99,
                        max_reward=1.0, lmdp=None, name="LangRMax", custom_q_init=None):
        rmax_agent = RMaxAgent(actions, gamma=gamma, s_a_threshold=s_a_threshold, epsilon_one=epsilon_one,
                                max_reward=max_reward, name=name, custom_q_init=custom_q_init)
        LangAgent.__init__(self, base_agent=rmax_agent, lmdp=lmdp)

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
                    self.transitions[state][action][state_prime] = 1
                    self.t_s_a_counts[state][action] += 1


    def default_transition(self, state, action):
        self.t_s_a_counts[state][action] += 1
        return self.lmdp.transition(state, action)

    def default_rewards(self, state, action):
        return self.lmdp.rewards(state)
    
    def update_from_lang(self):
        '''
            Update rewards table with information and transition table from language
        '''
        self.transitions = defaultdict(lambda state: defaultdict(lambda action: self.default_transition(state, action)))
        self.rewards = defaultdict(lambda state: defaultdict(lambda action: self.default_rewards(state, action)))
        
        
        

