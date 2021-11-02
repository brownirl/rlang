from collections import defaultdict
from simple_rl.agents import QLearningAgent
from rlang.src.grounding import State


class RLangQLearningAgent(QLearningAgent):
    """Implementation for a Q Learning agent which utilized RLang hints"""

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

        q_func = defaultdict(lambda: defaultdict(lambda: default_q))

        for s in states:
            for i in range(len(actions)):
                a = actions[i]
                q_func[s][a] = knowledge.reward_function(state=State(s), action=i)

        if use_transition:
            for s in states:
                for i in range(len(actions)):
                    a = actions[i]
                    s_primei = knowledge.transition_function(state=State(s), action=i)
                    if s_primei is not None:
                        # We may know enough to do a TD update
                        s_prime = s_primei.as_tuple()
                        if q_func[s_prime]:
                            q_func[s][a] = (1 - alpha) * q_func[s][a] + alpha * \
                                           (knowledge.reward_function(state=State(s), action=i, next_state=s_primei) +
                                            gamma * max(q_func[s_prime].values()))

        # for w in range(width):
        #     for h in range(height):
        #         for a, ai in {'up': 1, 'down': 2, 'left': 3, 'right': 4}.items():
        #             s = (w, h)
        #             si = State([w, h])
        #             predictions = knowledge.full_predictions(state=si, action=ai)
        #             print(predictions)
        #             for p in predictions.values():
        #                 print(p, p(state=si, action=ai))

        super().__init__(actions, name, alpha, gamma, epsilon, explore, anneal, q_func, default_q)
