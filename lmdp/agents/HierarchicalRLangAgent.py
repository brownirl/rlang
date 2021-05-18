from lmdp.grounding.states.StateClass import State as RLangState
from lmdp.agents.RLangAgent import RLangAgent
from lmdp.agents.all_hierarchical_dqn import HDQN, InnerAgent, SubgoalHierarchicalAgent

from all.presets import PresetBuilder
from all.logging import DummyWriter

from functools import partial
from collections import Iterable

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
    

class RLangInnerAgent(InnerAgent):
    def __init__(self, options, agent_factory):
        super().__init__(self, [], options['learnable'], agent_factory)
        self._option_agents.update(dict([(o._id, NonLearnableOptionAgent(o)) for o in options['non_learnable']]))

class HDQN_RLangAgent(HDQN):
    def __init__(self, env, device, name, hyperparams):
        self.env = env
        self.device = device
        self.name = name
        self.outer_agent_params = hyperparams['outer']
        self.inner_agent_params = hyperparams['inner']
        self._options = {}

    def inform(self, lmdp):
        self._options['learnable'] = self.__get_learnable_options(lmdp)
        self._options['non_learnable'] = self.__get_non_learnable_options(lmdp)
        super().__init__(self, self.env, self.device, self.name, self.discount_factor, self.outer_parameters, self.inner_agent_params)

    def agent(self, writer=DummyWriter(), train_steps=float('inf')):
        outer = self.outer_preset.agent(writer=writer, train_steps=train_steps)
        inner_factory = partial(self.inner_preset.agent, writer=DummyWriter(), train_steps=train_steps)
        inner = RLangInnerAgent(self._options, inner_factory)
        options = list(self._options.values())
        return SubgoalHierarchicalAgent(options[0]+options[1], outer, inner, self.discount_factor)

    def __get_learnable_options(self, lmdp):
        opts = [s.to_option() for s in lmdp.get_subpolicies()]
        return [o for o in opts if o.is_learnable()]

    def __get_non_learnable_options(self, lmdp):
        opts = [s.to_option() for s in lmdp.get_subpolicies()]
        return [o for o in opts if not o.is_learnable()]

rlang_hdqn = partial(PresetBuilder, constructor=HDQN_RLangAgent)