from lmdp.agents.Agent import Agent
from abc import abstractmethod
class RLangAgent(Agent):
    @abstractmethod
    def init(self, rlang_program):
        pass