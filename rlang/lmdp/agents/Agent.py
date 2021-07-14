'''
    Base Agent class
    Agent Factory (Given an initialized agent, it create copies)
    author: Rafael Rodriguez-Sanchez

    TODO: to refactor 
'''

from abc import abstractmethod
from copy import deepcopy

class Agent:
    @abstractmethod
    def act(self, state):
        pass
    @abstractmethod
    def eval(self, state):
        pass

class AgentFactory:
    def __init__(self, agent):
        self._agent = agent
    def __call__(self, option):
        agent = deepcopy(self._agent)
        return agent

