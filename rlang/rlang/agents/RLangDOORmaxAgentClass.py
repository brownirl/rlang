from efficient_rl.agents import DOORmax
import time


class RLangDOORmaxAgent(DOORmax):
    """Implementation for a DOORmax agent that utilizes RLang hints"""

    def __init__(self, actions, flat_states, base_oo_state, flat_state_to_oo_state, knowledge, nS, nA, r_max, gamma, env_name, k, eff_types, num_atts, delta, oo_mdp_dict):
        self.actions = actions
        self.knowledge = knowledge
        self.flat_states = flat_states
        self.base_oo_state = base_oo_state
        self.flat_state_to_oo_state = flat_state_to_oo_state

        super().__init__(nS, nA, r_max, gamma, env_name, k, eff_types, num_atts, delta, oo_mdp_dict)

    def main(self, env, max_steps=100, deterministic=False):
        # some metrics
        rewards, step_times = [], []
        # start training episode
        state = env.s
        for step in range(max_steps):
            start = time.time()
            # step agent
            action = self.step(state, deterministic)
            # step environment
            new_state, reward, done, _ = env.step(action)
            # add experience to transition learner (only when no predictions can be made)
            if not self.transition_learner_can_predict(state, action):
                self.add_experience_to_transition_learner(state, action, new_state)
            # add experience to reward learner (only when no predictions can be made)
            if not self.reward_learner_can_predict(state, action):
                self.add_experience_to_reward_learner(state, action, reward)
            # update empirical MDP model if possible, otherwise fall back to init
            self.update_emp_MDP(state, action)
            # keep track of metrics
            rewards.append(reward)
            step_times.append(time.time() - start)
            if done:
                break
            state = new_state
        return rewards, step_times

    def reset(self):
        super().reset()

        reward_func = self.knowledge.reward_function
        transition_func = self.knowledge.transition_function

        for flat_state in self.flat_states:
            oo_state = self.flat_state_to_oo_state(flat_state, self.base_oo_state)
            for action in self.actions:
                reward = reward_func(state=oo_state, action=action).unwrap()[0]
                next_state_dist = transition_func(state=oo_state, action=action)
                if next_state_dist != {}:
                    # next_state, prob = next_state.items()
                    next_state = list(next_state_dist.keys())[0]
                    # print(oo_state == next_state)
                    if oo_state == next_state:
                        self.add_experience_to_transition_learner((None, flat_state), action, (None, flat_state))
                self.add_experience_to_reward_learner((None, flat_state), action, reward)
                # self.add_experience_to_transition_learner()
