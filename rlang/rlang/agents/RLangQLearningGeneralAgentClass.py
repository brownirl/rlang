from collections import defaultdict
import time

from simple_rl.agents import QLearningAgent
from simple_rl.tasks.gym.GymMDPClass import GymState
import numpy as np

from ..grounding.utils.primitives import VectorState


class RLangQLearningGeneralAgent(QLearningAgent):
    """Implementation for a Q Learning agent that utilizes RLang hints, amenable to Minigrid"""

    def __init__(self, actions, get_knowledge, name="RLang-Q-learning-general", use_transition=False, use_policy=False, use_plan=False, use_effects=False,
                 alpha=0.1, gamma=0.99, epsilon=0.1, explore="uniform", anneal=False, default_q=0.0, policy_epsilon=0.9,
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
        self.use_plan = use_plan
        self.use_effects = use_effects
        self.policy_epsilon = policy_epsilon
        self.get_knowledge = get_knowledge
        self.state_unwrapper = state_unwrapper
        self.state_hash_func = state_hash_func
        self.state_featurizer = None

        self.was_reset = True
        self.knowledge = None

        super().__init__(actions, name=name, alpha=alpha, gamma=gamma,
                         epsilon=epsilon, explore=explore, anneal=anneal, custom_q_init=None, default_q=default_q)

    def populate_knowledge(self):
        # Okay, so we need to keep track of the states we've seen so far. Maybe we actually want to pop knowledge in the q learning methods

        # def weighted_reward(r_func, state_dict):
        #     reward = 0
        #     for k, v in state_dict.items():
        #         # This is going to be well-formed states, no need to modify here
        #         reward += r_func(state=VectorState(k)) * v
        #     return reward

        # def weighted_value(q_func, state_dict):
        #     reward = 0
        #     for k, v in state_dict.items():
        #         # TODO: verify that self.state_hash_func(k) is hashing properly! Might need to unwrap into numpy array first and then hash
        #         maxx = q_func[self.state_hash_func(k)][self.actions[0]]
        #         for a in self.actions:
        #             val = q_func[self.state_hash_func(k)][a]
        #             if val > maxx:
        #                 maxx = val
        #         reward += maxx * v
        #     return reward


        # if self.knowledge:
        #     q_func = defaultdict(lambda: defaultdict(lambda: self.default_q))
        #     reward_function = self.knowledge.reward_function

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
        pass

    def act(self, state, reward, learning=True):
        # start_time = time.perf_counter()
        if self.was_reset:
            if isinstance(state, GymState):
                init_state = state.data
            if isinstance(init_state, tuple):
                init_state = init_state[0]
            # self.knowledge, self.knowledge2, self.state_featurizer = self.get_knowledge(self.state_unwrapper(init_state))
            self.knowledge, self.state_featurizer = self.get_knowledge(self.state_unwrapper(init_state))
            self.populate_knowledge()
            self.knowledge.memoized_reward_function.cache_clear()
            self.was_reset = False
        # print(self.knowledge.reward_function(state=VectorState(self.state_unwrapper(state))))
        # print(self.knowledge['goal'](state=VectorState(self.state_unwrapper(state))))
        # print(self.knowledge['at_any_lava'](state=VectorState(self.state_unwrapper(state))))
        if self.state_featurizer:
            self.state_featurizer.update_objects(self.state_unwrapper(state))
        # return super().act(state, reward, learning)
    
        if learning:
            self.update(self.prev_state, self.prev_action, reward, state)

            # Before choosing an action, let's cycle through the next actions, next transtions, and update q values
            if self.use_effects and self.knowledge:
                # start_time = time.perf_counter()
                
                rlang_state = VectorState(self.state_unwrapper(state))
                hashed_state = self.state_hash_func(self.state_unwrapper(state))
                for a in self.actions:
                    # Before doing the below, check to see if a value update has already been done for this state-action pair
                    potential_reward = int(self.knowledge.memoized_reward_function(state=rlang_state, action=a))
                    if potential_reward != 0:
                        partial_q = self.q_func[hashed_state]
                        if partial_q[a] == self.default_q:
                            # max_q_curr_state = reward
                            partial_q[a] = (1 - self.alpha) * self.default_q + self.alpha * potential_reward#(potential_reward + self.gamma * max_q_curr_state)
                

                # partial_q = self.q_func[self.state_hash_func(self.state_unwrapper(state))]
                # for a in self.actions:
                #     if partial_q[a] == self.default_q:
                #         potential_reward = int(self.knowledge.reward_function(state=rlang_state, action=a))
                #         if potential_reward != 0:
                #             # max_q_curr_state = reward
                #             partial_q[a] = (1 - self.alpha) * self.default_q + self.alpha * potential_reward#(reward + self.gamma * max_q_curr_state)

                # print(time.perf_counter() - start_time)


        if self.explore == "softmax":
            # Softmax exploration
            action = self.soft_max_policy(state)
        else:
            # Uniform exploration
            action = self.epsilon_greedy_q_policy(state)

        self.prev_state = state
        self.prev_action = action
        self.step_number += 1

        # Anneal params.
        if learning and self.anneal:
            self._anneal()

        # print(time.perf_counter() - start_time)
        return action

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

        if (self.use_policy or self.use_plan) and np.random.random() < self.policy_epsilon:
            if self.use_plan:
                action = self.knowledge.plan(state=VectorState(self.state_unwrapper(state)))
                # action2 = self.knowledge2.plan(state=VectorState(self.state_unwrapper(state)))
            else:
                action = self.knowledge.policy(state=VectorState(self.state_unwrapper(state)))
                
            if action:
                # print(state)
                # print(f"Action1: {action} at index {self.knowledge.plan.i}")
                # print(f"Action2: {action2} at index {self.knowledge2.plan.i}")
                # print(self.knowledge['yellow_door'](state=VectorState(self.state_unwrapper(state))))
                # print(self.knowledge2['yellow_door'](state=VectorState(self.state_unwrapper(state))))
                # print(self.knowledge['agent'](state=VectorState(self.state_unwrapper(state))))
                # print(self.knowledge2['agent'](state=VectorState(self.state_unwrapper(state))))


                if isinstance(action, int):
                    return action
                action = int(list(action.keys())[0])
                return action
            else:
                # if action2:
                    # print(state)
                    # print("Action2 found but no Action1")
                    # print(f"Action2: {action2} at index {self.knowledge2.plan.i}")
                    # print(self.knowledge['yellow_door'](state=VectorState(self.state_unwrapper(state))))
                    # print(self.knowledge2['yellow_door'](state=VectorState(self.state_unwrapper(state))))
                    # print(self.knowledge['agent'](state=VectorState(self.state_unwrapper(state))))
                    # print(self.knowledge2['agent'](state=VectorState(self.state_unwrapper(state))))
                    # pass
                
                # if self.use_plan:
                #     print("No action found, reverting to epsilon greedy")
                # print(self.knowledge.plan.i)
                # if self.use_plan:
                #     self.knowledge.plan.reset()
                return super().epsilon_greedy_q_policy(state)
        else:
            return super().epsilon_greedy_q_policy(state)

    # ---------------------------------
    # ---- Q VALUES AND PARAMETERS ----
    # ---------------------------------

    def rlang_q_update(self, state, action, reward):
        '''
        Args:
            state (State)
            action (str)
            reward (float)

        Summary:
            Updates the internal Q Function according to the Bellman Equation. (Classic Q Learning update)
        '''
        # If this is the first state, just return.
        if state is None:
            self.prev_state = None
            return
        
        if isinstance(state, GymState):
            state = state.data
        if isinstance(state, tuple):
            state = state[0]

        # Update the Q Function.
        max_q_curr_state = reward
        prev_q_val = self.get_q_value(state, action)

        # print(self.state_hash_func(self.state_unwrapper(state)))
        self.q_func[self.state_hash_func(self.state_unwrapper(state))][action] = \
            (1 - self.alpha) * prev_q_val + self.alpha * (reward + self.gamma * max_q_curr_state)


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

        # if not self.state_hash_func(self.state_unwrapper(state)) in self.q_func:
        #     print("Not Seen")

        # print(self.state_hash_func(self.state_unwrapper(state)))
        return self.q_func[self.state_hash_func(self.state_unwrapper(state))][action]

    def reset(self):
        self.was_reset = True
        if self.use_plan:
            self.knowledge.plan.reset()
            # self.knowledge2.plan.reset()
        super().reset()
    
    def end_of_episode(self):
        if self.use_plan:
            self.knowledge.plan.reset()
            # self.knowledge2.plan.reset()
        super().end_of_episode()