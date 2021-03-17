'''
    Adaptor for RLang Agents to SimpleRL agents
'''

import simple_rl.agents.AgentClass as simple_rl_agent

class SimpleRLAgent(simple_rl_agent.Agent):
    def __init__(self, rlang_agent, actions, name="", gamma=0.99):
        simple_rl_agent.Agent.__init__(self, name, actions, gamma=gamma)
        self._agent = rlang_agent

    def act(self, state, reward):
        return self._agent.act({'observation': state, 'reward': reward, 'done': state.is_terminal()})
    
    def policy(self, state):
        return self._agent.eval({'observation': state, 'reward': 0, 'done': state.is_terminal()})
    
    def reset(self):
        self._agent.reset()