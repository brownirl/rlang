from collections import defaultdict

from simple_rl.agents import QLearningAgent

from ..grounding.utils.primitives import VectorState


class RLangQLearningAgent(QLearningAgent):
    """Implementation for a Q Learning agent that utilizes RLang hints"""

    def __init__(self, actions, states, knowledge, name="RLang-Q-learning", use_transition=False, alpha=0.1, gamma=0.99,
                 epsilon=0.1, explore="uniform", anneal=False, default_q=0):
        """
        Args:
            actions (list): Contains strings denoting the actions.
            name (str): Denotes the name of the agent.
            alpha (float): Learning rate.
            gamma (float): Discount factor.
            epsilon (float): Exploration term.
            explore (str): One of {softmax, uniform}. Denotes explore policy.
            custom_q_init (defaultdict{state, defaultdict{action, float}}): a dictionary of dictionaries storing the
             initial q-values. Can be used for potential shaping (Wiewiora, 2003)
            default_q (float): the default value to initialize every entry in the q-table with [by default, set to 0.0]
        """

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
