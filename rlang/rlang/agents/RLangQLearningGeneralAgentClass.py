from collections import defaultdict

from simple_rl.agents import QLearningAgent
import numpy as np

from ..grounding.utils.primitives import VectorState


class RLangQLearningGeneralAgent(QLearningAgent):
    """Implementation for a Q Learning agent that utilizes RLang hints"""

    def __init__(self, actions, states, knowledge, name="RLang-Q-learning", use_transition=False, use_policy=False,
                 alpha=0.1, gamma=0.99, epsilon=0.1, explore="uniform", anneal=False, default_q=0, policy_epsilon=0.9,
                 state_wrapper=None, state_hash_func=None):
        """
        Args:
            actions (list): Contains strings denoting the actions.
            states (list): A list of all possible states.
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
        self.knowledge = knowledge
        self.state_wrapper = state_wrapper
        self.state_hash_func = state_hash_func

        def weighted_reward(r_func, state_dict):
            reward = 0
            for k, v in state_dict.items():
                reward += r_func(state=VectorState(k)) * v
            return reward

        def weighted_value(q_func, state_dict):
            reward = 0
            for k, v in state_dict.items():
                maxx = q_func[k][actions[0]]
                for a in actions:
                    val = q_func[k][a]
                    if val > maxx:
                        maxx = val
                reward += maxx * v
            return reward

        q_func = defaultdict(lambda: defaultdict(lambda: default_q))

        if knowledge:
            reward_function = knowledge.reward_function

            if reward_function:
                for s in states:
                    for i in range(len(actions)):
                        a = actions[i]
                        q_func[s][a] = reward_function(state=VectorState(s), action=i)

            transition_function = knowledge.transition_function

            if use_transition and transition_function and reward_function:
                for s in states:
                    for i in range(len(actions)):
                        a = actions[i]
                        s_primei = transition_function(state=VectorState(s), action=i)
                        if s_primei:
                            # Q learning Update
                            r_prime = weighted_reward(reward_function, s_primei)
                            v_s_prime = weighted_value(q_func, s_primei)
                            q_func[s][a] += alpha * (r_prime + gamma * v_s_prime)

        super().__init__(actions, name=name, alpha=alpha, gamma=gamma,
                         epsilon=epsilon, explore=explore, anneal=anneal, custom_q_init=q_func, default_q=default_q)

    def epsilon_greedy_q_policy(self, state):
        '''
        Args:
            state (State)

        Returns:
            action.
        '''

        if self.use_policy and np.random.random() < self.policy_epsilon:
            return self.knowledge.policy(state=VectorState(state))
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

        # Update the Q Function.
        max_q_curr_state = self.get_max_q_value(next_state)
        prev_q_val = self.get_q_value(state, action)

        self.q_func[state if self.state_hash_func is None else self.state_hash_func(state)][action] = \
            (1 - self.alpha) * prev_q_val + self.alpha * (reward + self.gamma * max_q_curr_state)

    def get_q_value(self, state, action):
        '''
        Args:
            state (State)
            action (str)

        Returns:
            (float): denoting the q value of the (@state, @action) pair.
        '''
        return self.q_func[state if self.state_hash_func is None else self.state_hash_func(state)][action]
