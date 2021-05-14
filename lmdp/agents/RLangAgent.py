from lmdp.agents.Agent import Agent
from abc import abstractmethod

class RLangAgent(Agent):
    @abstractmethod
    def inform(self, rlang_program):
        pass