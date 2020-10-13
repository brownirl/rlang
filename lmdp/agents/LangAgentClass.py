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


    # def _init_from_lmdp(self):
    #     pass

    # def get_parameters(self):
    #     '''
    #     Returns:
    #         (dict) key=param_name (str) --> val=param_val (object).
    #     '''
    #     return self._base_agent.get_parameters()

    # def act(self, state, reward):
    #     '''
    #     Args:
    #         state (State): see StateClass.py
    #         reward (float): the reward associated with arriving in state @state.

    #     Returns:
    #         (str): action.
    #     '''
    #     return self._base_agent.act(state, reward)

    # def policy(self, state):
    #     return self._base_agent.policy(state)

    # def reset(self):
    #     '''
    #     Summary:
    #         Resets the agent back to its tabula rasa config.
    #     '''
    #     self._base_agent.reset()

    # def end_of_episode(self):
    #     '''
    #     Summary:
    #         Resets the agents prior pointers.
    #     '''
    #     self._base_agent.end_of_episode()

    # def set_name(self, name):
    #     self._base_agent.set_name(name)

    # def get_name(self):
    #     return self._base_agent.get_name()

    # def __str__(self):
    #     return str(self._base_agent.get_name())

if __name__=="__main__":
    from simple_rl.agents.RMaxAgentClass import RMaxAgent
    langrmax = LangAgent(RMaxAgent({"up", "down"}, name='lang-rmax'))
    print(langrmax.get_name())
    print(langrmax.get_parameters())