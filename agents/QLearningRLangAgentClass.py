from simple_rl.agents.QLearningAgentClass import QLearningAgent
from collections import namedtuple
import numpy as np
import copy, time
from tqdm import tqdm

indices = namedtuple("SAIndex", ["state_space", "action_space"])


# def _indices(state_space_gen, action_space):
#     return indices(Index(state_space_gen()), Index(action_space))


class QLearningRLangAgent:
    DEFAULT_Q = 0
    MAX_Q = 1

    def __init__(self, actions, name="RLang-qlearning", rlang=None, alpha=0.1, gamma=0.99,
                 epsilon=0.1, explore="uniform", anneal=False,
                 custom_q_init=None, default_q=0):
        self.epsilon_one = 0.99
        self.q_func = None
        q_agent = QLearningAgent(actions, name=name, alpha=alpha, gamma=gamma, epsilon=epsilon, explore=explore,
                                 anneal=anneal, custom_q_init=custom_q_init, default_q=default_q)
        self.base_agent = q_agent
        self.rlang = rlang

    def reset(self):
        self.base_agent.reset()
        if self.q_func is None:
            # TODO: Not sure what these are
            self.indices = _indices(self.state_space, self.base_agent.actions)
            self.transitions = ArrayDict(len(self.indices.state_space), len(self.indices.action_space),
                                         len(self.indices.state_space),
                                         index=self.indices + (self.indices.state_space,))

            self.rewards = ArrayDict(len(self.indices.state_space), len(self.indices.action_space),
                                     len(self.indices.state_space),
                                     index=self.indices + (self.indices.state_space,))
            self.q_func = ArrayDict(len(self.indices.state_space), len(self.indices.action_space),
                                    index=self.indices)

            self.__init_functions()
            self.q_func.data = self.initialize_q_function()

        self.base_agent.q_func = copy.deepcopy(self.q_func)

    def __init_functions(self):
        # TODO: I'm not sure what this function does
        # from lmdp.grounding.states.StateClass import BatchedState

        t = list(self.indices.state_space.objects())
        s_ = BatchedState(t)
        s, s_prime = _cartesian(s_.numpy(), s_.numpy())
        s, s_prime = BatchedState(s), BatchedState(s_prime)

        r = self.rewards.numpy()
        t = self.transitions.numpy()
        q = self.q_func.numpy()
        for a, i in tqdm(self.indices.action_space.elems()):
            print("Init rewards...")
            n_states = s_.batch_size()
            r[:, i] = self.default_rewards(s, a, s_prime).reshape(n_states, n_states)
            print("Init transitions...")
            t[:, i] = self.default_transition(s, a, s_prime).reshape(n_states, n_states)
            print("Init values...")
            q[:, i] = self.default_q_func(s_, a).reshape(n_states)

    def default_transition(self, state, action, state_prime):
        # TODO: This can return multiple next states? Is that because it's batched?
        next_states = self.lmdp.transition(state, action)
        t = np.zeros(state.batch_size(), dtype=bool)
        if len(next_states) > 0:
            for bs, ns in next_states:
                ns = ns(state_prime)
                t = t | (bs & ns)   # TODO: What is this operation?
        return t

    def default_rewards(self, state, action, s_prime):
        rewards = self.lmdp.reward(state, action, s_prime)
        n_states = state.batch_size()
        r = np.zeros(n_states)  # return zero by default
        if len(rewards) > 0:
            n = np.zeros(n_states)
            b = np.zeros(n_states, dtype=bool)
            for bs, fs in rewards:
                n += bs
                b = b | np.logical_not(bs)
                r[bs] += fs[bs]
            n[b] = 1
            return r / b
        return r

    def default_q_func(self, state, action):  # default q_function is the same value for all actions
        values = self.lmdp.value(state)
        n_states = state.batch_size()
        if len(values) > 0:
            r = np.zeros(n_states)  # return zero by default
            n = np.zeros(n_states)
            b = np.zeros(n_states, dtype=bool)
            for bs, fs in values:  # boolean function, function to get reward
                n += bs
                b = b | np.logical_not(bs)
                r[bs] += fs[bs]
            n[b] = 1
            return r / b
        return np.zeros(n_states)

    def initialize_q_function(self):  # Value iteration initialization
        q_function = self.q_func.numpy()
        lim = int(np.log(1 / (self.epsilon_one * (1 - self.base_agent.gamma))) / (1 - self.base_agent.gamma))
        start = time.clock()
        for _ in range(1, lim):
            v = q_function.max(-1, keepdims=1).transpose()[np.newaxis]
            p = self.transitions.numpy()
            q_function = self.rewards.numpy().mean(-1) + self.base_agent.gamma * (p * v).mean(-1)

        end = time.clock()
        print(f"{end - start}s")
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
