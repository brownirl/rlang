'''
    Wrapper Class for Language Initialized agents
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: September 2020
'''
from simple_rl.agents.AgentClass import Agent

class LangAgent(object):

    def __init__(self, base_agent, lmdp):
        self.lmdp = lmdp
        self.base_agent = base_agent

    def __getattr__(self, method_name):
        def method(*args, **kwargs):
            return getattr(self.base_agent, method_name)(*args, **kwargs)
        return method

    def set_lmdp(self, lmdp):
        self.lmdp = lmdp
    
    def __str__(self):
        return self.get_name()
    
    @property
    def name(self):
        return str(self)

if __name__=="__main__":
    from simple_rl.agents.RMaxAgentClass import RMaxAgent
    langrmax = LangAgent(RMaxAgent({"up", "down"}, name='lang-rmax'))
    print(langrmax.get_name())
    print(langrmax.get_parameters())