from collections import defaultdict

from simple_rl.agents import QLearningAgent
from simple_rl.tasks.gym.GymMDPClass import GymState
import numpy as np

from ..grounding.utils.primitives import VectorState


class RLangQLearningGeneralAgent(QLearningAgent):
    """Implementation for a Q Learning agent that utilizes RLang hints, amenable to Minigrid"""

    def __init__(self, actions, get_knowledge, name="RLang-Q-learning-general", use_transition=False, use_policy=False,
                 alpha=0.1, gamma=0.99, epsilon=0.1, explore="uniform", anneal=False, default_q=0, policy_epsilon=0.9,
                 state_unwrapper=None, state_hash_func=None):
        """
        Args:
            actions (list): Contains strings denoting the actions.
            states (dict): A dictionary of hashed states to unwrapped states
            knowledge (list): An RLangKnowledge object.
            name (str): Denotes the name of the agent.
            alpha (float): Learning rate.
            gamma (float): Discount factor.
            epsilon (float): Exploration term.
            explore (str): One of {softmax, uniform}. Denotes explore policy.
            default_q (float): the default value to initialize every entry in the q-table with [by default, set to 0.0]
        """

        self.use_transition = use_transition
        self.use_policy = use_policy
        self.policy_epsilon = policy_epsilon
        self.get_knowledge = get_knowledge
        self.state_unwrapper = state_unwrapper
        self.state_hash_func = state_hash_func

        self.was_reset = True

        def weighted_reward(r_func, state_dict):
            reward = 0
            for k, v in state_dict.items():
                # This is going to be well-formed states, no need to modify here
                reward += r_func(state=VectorState(k)) * v
            return reward

        def weighted_value(q_func, state_dict):
            reward = 0
            for k, v in state_dict.items():
                # TODO: verify that self.state_hash_func(k) is hashing properly! Might need to unwrap into numpy array first and then hash
                maxx = q_func[self.state_hash_func(k)][actions[0]]
                for a in actions:
                    val = q_func[self.state_hash_func(k)][a]
                    if val > maxx:
                        maxx = val
                reward += maxx * v
            return reward

        q_func = None
        # if knowledge:
        #     q_func = defaultdict(lambda: defaultdict(lambda: default_q))
        #     reward_function = knowledge.reward_function

        #     # For now I'll assume I have good states, I'll get back to this.
        #     # I'm gonna do a new solution where I periodically update the Q function with the RLang rewards and transition function when more and more states are discovered
        #     # This means I'll need to keep track of new states so I can iterate over them! Yikes, could be a lot of memory.
        #     # Anyway, I'll cross that bridge when I get to it.

        #     hashed_states = list(states.keys())

        #     if reward_function:
        #         for hashed_s in hashed_states:
        #             for i in range(len(actions)):
        #                 a = actions[i]
        #                 q_func[hashed_s][a] = reward_function(state=VectorState(states[hashed_s]), action=i)

        #     transition_function = knowledge.transition_function

        #     if use_transition and transition_function and reward_function:
        #         for hashed_s in hashed_states:
        #             for i in range(len(actions)):
        #                 a = actions[i]
        #                 s_primei = transition_function(state=VectorState(states[hashed_s]), action=i)
        #                 if s_primei:
        #                     # Q learning Update
        #                     r_prime = weighted_reward(reward_function, s_primei)
        #                     v_s_prime = weighted_value(q_func, s_primei)
        #                     q_func[hashed_s][a] += alpha * (r_prime + gamma * v_s_prime)

        super().__init__(actions, name=name, alpha=alpha, gamma=gamma,
                         epsilon=epsilon, explore=explore, anneal=anneal, custom_q_init=q_func, default_q=default_q)

    def populate_knowledge(self):
        pass

    def act(self, state, reward, learning=True):
        if self.was_reset:
            if isinstance(state, GymState):
                init_state = state.data
            if isinstance(init_state, tuple):
                init_state = init_state[0]
            self.knowledge = self.get_knowledge(self.state_unwrapper(init_state))
            self.was_reset = False
        # print(self.knowledge['goal'](state=VectorState(self.state_unwrapper(state))))
        return super().act(state, reward, learning)

    def epsilon_greedy_q_policy(self, state):
        '''
        Args:
            state (State)

        Returns:
            action.
        '''

        if isinstance(state, GymState):
            state = state.data
        if isinstance(state, tuple):
            state = state[0]

        # print(self.knowledge['goal'](state=VectorState(self.state_unwrapper(state))))

        if self.use_policy and np.random.random() < self.policy_epsilon:
            action = self.knowledge.policy(state=VectorState(self.state_unwrapper(state)))
            if action:
                action = int(list(action.keys())[0])
                # print(state)
                # print(action)
                return action
            else:
                return super().epsilon_greedy_q_policy(state)
        else:
            return super().epsilon_greedy_q_policy(state)

    # ---------------------------------
    # ---- Q VALUES AND PARAMETERS ----
    # ---------------------------------

    def update(self, state, action, reward, next_state):
        '''
        Args:
            state (State)
            action (str)
            reward (float)
            next_state (State)

        Summary:
            Updates the internal Q Function according to the Bellman Equation. (Classic Q Learning update)
        '''
        # If this is the first state, just return.
        if state is None:
            self.prev_state = next_state
            return

        
        if isinstance(state, GymState):
            state = state.data
        if isinstance(state, tuple):
            state = state[0]

        if isinstance(next_state, GymState):
            next_state = next_state.data
        if isinstance(next_state, tuple):
            next_state = next_state[0]

        # Update the Q Function.
        max_q_curr_state = self.get_max_q_value(next_state)
        prev_q_val = self.get_q_value(state, action)

        # print(self.state_hash_func(self.state_unwrapper(state)))
        self.q_func[self.state_hash_func(self.state_unwrapper(state))][action] = \
            (1 - self.alpha) * prev_q_val + self.alpha * (reward + self.gamma * max_q_curr_state)

    def get_q_value(self, state, action):
        '''
        Args:
            state (State)
            action (str)

        Returns:
            (float): denoting the q value of the (@state, @action) pair.
        '''
        if isinstance(state, GymState):
            state = state.data
        if isinstance(state, tuple):
            state = state[0]

        # print(self.state_hash_func(self.state_unwrapper(state)))
        return self.q_func[self.state_hash_func(self.state_unwrapper(state))][action]

    def reset(self):
        self.was_reset = True
        super().reset()
    