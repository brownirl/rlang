'''
    Language-informed Q-Learning Agent
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: v0 September 2020
          v1 February 2021
'''
from simple_rl.agents.QLearningAgentClass import QLearningAgent
from lmdp.agents.LangAgentClass import LangAgent
from lmdp.utils.collections import defaultdict, arraydict, Index
from functools import reduce
from collections import namedtuple
import numpy as np
import copy, time
import pickle, os.path
from itertools import product
from tqdm import tqdm


def _cartesian(a1, a2):
    r2 = np.tile(a2, (a1.shape[0],1))
    r1 = np.repeat(a1, a2.shape[0], 0) 
    return r1, r2

indices = namedtuple("SAIndex", ["state_space", "action_space"])
def _indices(state_space_gen, action_space):
    return indices(Index(state_space_gen()), Index(action_space))

class QLearningLangAgent(LangAgent):
    DEFAULT_Q = 0
    MAX_Q = 1
    def __init__(self, actions, name="lang-qlearning", lmdp=None, alpha=0.1, gamma=0.99,
                 epsilon=0.1, explore="uniform", anneal=False,
                 custom_q_init=None, default_q=0):
        self.epsilon_one = 0.99
        self.q_func = None
        q_agent = QLearningAgent(actions, name=name, alpha=alpha, gamma=gamma, epsilon=epsilon, explore=explore, anneal=anneal, custom_q_init=custom_q_init, default_q=default_q)
        LangAgent.__init__(self, base_agent=q_agent, lmdp=lmdp)


    def reset(self):
        self.base_agent.reset()
        if self.q_func is None:
            self.indices = _indices(self.state_space, self.base_agent.actions)
            self.transitions = arraydict(len(self.indices.state_space), len(self.indices.action_space), len(self.indices.state_space), 
                                        index=self.indices + (self.indices.state_space,))
            
            self.rewards = arraydict(len(self.indices.state_space), len(self.indices.action_space), len(self.indices.state_space), 
                                        index=self.indices + (self.indices.state_space,))
            self.q_func = arraydict(len(self.indices.state_space), len(self.indices.action_space), 
                                        index=self.indices)

            self.__init_functions()
            self.q_func.data = self.initialize_q_function()

        self.base_agent.q_func = copy.deepcopy(self.q_func)
            
    def __init_functions(self):
        from itertools import product
        from lmdp.grounding.states.StateClass import BatchedState
        from lmdp.utils.space import BatchedTuple


        t = self.indices.state_space.objects()
        # s_ = map(lambda x: x.features(), t)
        s_ = BatchedState(tuple(t))
        # s, s_prime  = zip(*map(lambda t: (t[0].data, t[1].data), t))
        s, s_prime = _cartesian(s_.numpy(), s_.numpy())
        # s, s_prime = zip(*t)
        s, s_prime = BatchedState(s), BatchedState(s_prime)
        

        r = self.rewards.numpy()
        t = self.transitions.numpy()
        q = self.q_func.numpy()
        for a, i  in tqdm(self.indices.action_space.elems()):
            # start = time.clock()
            print("Init rewards...")
            r[:,i] = self.default_rewards(s, a, s_prime).reshape(len(s_), len(s_))     
            # end = time.clock()
            print("Init transitions...")
            t[:,i] = self.default_transition(s, a, s_prime).reshape(len(s_), len(s_))
            print("Init values...")
            q[:,i] = self.default_q_func(s_,a).reshape(len(s_))


    def default_transition(self, state, action, state_prime):
        next_states = self.lmdp.transition(state, action)
        t = np.zeros(len(state), dtype=bool)
        if len(next_states) > 0:
            for bs, ns in next_states:
                ns = ns(state_prime)
                t = t | (bs & ns)
        return t
        
        # if (next_states is not None and len(next_states) > 0):
        #     transitions = reduce(lambda x, y: x or y, map(lambda n_state: n_state(state_prime), next_states), False)
        #     return int(transitions)
        # return int(0)

    def default_rewards(self, state, action, s_prime):
        rewards = self.lmdp.reward(state, action, s_prime)
        r = np.zeros(len(state))  # return zero by default
        if len(rewards) > 0:
            n = np.zeros(len(state))
            b = np.zeros(len(state), dtype=bool)
            for bs, fs in rewards:
                n += bs
                b = b | np.logical_not(bs)
                r[bs] += fs[bs]
            n[b] = 1
            return r / b
        return r

    def default_q_func(self, state, action):  # default q_function is the same value for all actions
        values = self.lmdp.value(state)
        if len(values)>0:
            r = np.zeros(len(state))  # return zero by default
            n = np.zeros(len(state))
            b = np.zeros(len(state), dtype=bool)
            for bs, fs in values:
                n += bs
                b = b | np.logical_not(bs)
                r[bs] += fs[bs]
            n[b] = 1
            return r / b
        return np.zeros(len(state))

    def initialize_q_function(self): # Value iteration initialization
        q_function = self.q_func.numpy()
        lim = int(np.log(1/(self.epsilon_one * (1 - self.base_agent.gamma))) / (1 - self.base_agent.gamma))
        start = time.clock()
        for _ in range(1, lim):
            
            v = q_function.max(-1, keepdims=1).transpose()[np.newaxis]
            p = self.transitions.numpy()
            q_function = self.rewards.numpy().mean(-1) + self.base_agent.gamma * (p * v).mean(-1)
            
        end = time.clock()
        print(f"{end-start}s")
        return q_function

    def __get_max_q(self, q, s):
        q_values = q[s].values()
        if len(q_values) > 0:
            return max(q_values)
        return 0

    def update_from_lang(self, state_space=None):
        '''
            Update rewards table with information and transition table from language
        '''
        self.state_space = state_space
        self.reset()


