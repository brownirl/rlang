'''
    Language-informed Sarsa Agent
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: September 2020
'''
from lmdp.agents.SarsaAgentClass import SarsaAgent
from lmdp.agents.LangAgentClass import LangAgent
from lmdp.utils.collections import defaultdict

class SarsaLangAgent(LangAgent):
    DEFAULT_Q = 0
    MAX_Q = 1
    def __init__(self, actions, name="lang-sarsa", lmdp=None, alpha=0.1, gamma=0.99,
                 epsilon=0.1, explore="uniform", anneal=False,
                 custom_q_init=None, default_q=0):
        
        sarsa_agent = SarsaAgent(actions, name=name, alpha=alpha, gamma=gamma, epsilon=epsilon, explore=explore, anneal=anneal, custom_q_init=custom_q_init, default_q=default_q)
        LangAgent.__init__(self, base_agent=sarsa_agent, lmdp=lmdp)


    def lang_q_func(self, state, action):
        '''
            Priority-based implementation: 
            1. value for (s,a) specified; 
            2. Reward for (s,a) specified;
            3. action specified.

            returns the average value over the symbols the state belongs to.
        '''

        value = self._lmdp.value(state)
        reward = self._lmdp.reward(state)
        rec_action = self._lmdp.policy(state)

        if value is not None:
            return sum(value)/len(value)
        elif reward is not None:
            return sum(reward)/len(reward)
        elif action is not None and rec_action == action:
            return SarsaLangAgent.MAX_Q
        else:
            return SarsaLangAgent.DEFAULT_Q
            
    def update_from_language(self):
        self._base_agent.q_func = defaultdict(lambda state: defaultdict(lambda action: self.lang_q_func(state, action)))