from copy import deepcopy
from lmdp.agents.LangAgentClass import LangAgent
from lmdp.agents.HierarchicalAgent import IntraoptionQAgent, SMDPQAgent

class RLangSMDPQAgent(SMDPQAgent, LangAgent):
    def __init__(self, actions, lmdp, *args, **kwargs):
        self.primitive_actions = actions
        self.learnable_options = self.__get_learnable_options(lmdp)
        self.non_learnable_options = self.__get_non_learnable_options(lmdp) 
        SMDPQAgent.__init__(self, actions, self.learnable_options, *args, **kwargs)
        self._inner_agent._option_agents.update([NonLearnableOptionAgent(o) for o in self.non_learnable_options])
        self._outer_agent._agent.actions = self.learnable_options + self.non_learnable_options
        self._inner = deepcopy(self._inner_agent)
        self._outer = deepcopy(self._outer_agent)

    def __get_learnable_options(self, lmdp):
        opts = [s.to_option() for s in lmdp.get_subpolicies()]
        return [o for o in opts if o.is_learnable()]

    def __get_non_learnable_options(self, lmdp):
        opts = [s.to_option() for s in lmdp.get_subpolicies()]
        return [o for o in opts if not o.is_learnable()]
    
    def get_options(self):
        return self.primitive_actions

    def __repr__(self):
        return repr(self._outer_agent)

class RLangIntraoptionQAgent(IntraoptionQAgent, LangAgent):
    def __init__(self, actions, lmdp, *args, **kwargs):
        self.primitive_actions = actions
        self.learnable_options = self.__get_learnable_options(lmdp)
        self.non_learnable_options = self.__get_non_learnable_options(lmdp) 
        IntraoptionQAgent.__init__(self, actions, self.learnable_options, *args, **kwargs)
        self._inner_agent._option_agents.update([NonLearnableOptionAgent(o) for o in self.non_learnable_options])
        self._outer_agent._agent.actions = self.learnable_options + self.non_learnable_options
        self._inner = deepcopy(self._inner_agent)
        self._outer = deepcopy(self._outer_agent)

    def __get_learnable_options(self, lmdp):
        opts = [s.to_option() for s in lmdp.get_subpolicies()]
        return [o for o in opts if o.is_learnable()]

    def __get_non_learnable_options(self, lmdp):
        opts = [s.to_option() for s in lmdp.get_subpolicies()]
        return [o for o in opts if not o.is_learnable()]
    
    def get_options(self):
        return self.primitive_actions

from lmdp.grounding.states.StateClass import State as RLangState
from collections.abc import Iterable

class NonLearnableOptionAgent(Iterable):
    def __init__(self, non_learnable_option):
        self.option = non_learnable_option

    def act(self, state):
        return self.option.policy(RLangState(state['observation']))

    def eval(self, state):
        return self.option.policy(RLangState(state['observation']))
    
    def stop(self, state):
        pass
    
    def __getitem__(self, key):
        if key == 0:
            return self.option.get_id()
        elif key == 1:
            return self

    def __iter__(self):
        return iter((self.option.get_id(), self))
    