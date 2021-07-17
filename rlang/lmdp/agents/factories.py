from lmdp.agents.Agent import AgentFactory
from all.presets.classic_control.models import fc_relu_q
from lmdp.grounding.states.StateClass import BatchedState as RLangState
from lmdp.grounding.states.StateClass import State as RLState
import torch.nn as nn
import random
import numpy as np

# from lmdp.agents.ReinforceMLPAgentClass import ReinforceMLPAgent

# class ReinforceFactory(AgentFactory):
#     def __init__(self, actions, state_dim=1, name="", gamma=0.95, alpha=0.01, 
#                                 N=5, hidden_size=16, n_hidden_layers=1):
#         self._agent = ReinforceAgent(actions, state_dim=1, name="", gamma=0.95, alpha=0.01, 
#                                 N=5, hidden_size=16, n_hidden_layers=1)


# class ReinforceAgent(ReinforceMLPAgent):

#     def act(self, state):
#         action = super().act(state['observation'], state['reward'])
#         return action

#     def eval(self, state):
#         return super().act(state['observation'], state['reward'])

#     def stop(self, state):
#         self.end_of_episode()

# =================================================================
from simple_rl.agents.QLearningAgentClass import QLearningAgent
from simple_rl.agents import LinearQAgent
from simple_rl.abstraction import FeatureWrapper


class QLearningFactory(AgentFactory):
    def __init__(self,
                 actions, name="qlearning", alpha=0.1, gamma=0.99,
                 epsilon=0.1, explore="uniform", anneal=False,
                 custom_q_init=None, default_q=0):
        self._agent = QLearning(actions,
                                name=name,
                                alpha=alpha,
                                gamma=gamma,
                                epsilon=epsilon,
                                explore=explore,
                                anneal=anneal,
                                custom_q_init=custom_q_init,
                                default_q=default_q)


class QLearning(QLearningAgent):
    def __init__(self, *args, beta=0.2, **kwargs):
        self._beta = beta
        QLearningAgent.__init__(self, *args, **kwargs)

    def act(self, state, timestep=1, learning=True):
        if learning:
            self.update(self.prev_state, self.prev_action, state['reward'], state)
        if self.explore == "softmax":
            # Softmax exploration
            action = self.soft_max_policy(state['observation'])
        else:
            # Uniform exploration
            action = self.epsilon_greedy_q_policy(state['observation'])

        self.prev_state = state['observation']
        self.prev_action = action
        self.step_number += 1

        # Anneal params.
        if learning and self.anneal:
            self._anneal()

        return action

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
            self.prev_state = next_state['observation']
            return

        # Update the Q Function.
        prev_q_val = self.get_q_value(state, action)
        max_q_curr_state = self.get_max_q_value(next_state['observation'])
        if not next_state['done']:
            self.q_func[state][action] = (1 - self.alpha) * prev_q_val + self.alpha * (
                        reward + self.gamma * max_q_curr_state)
        else:
            self.q_func[state][action] = (1 - self.alpha) * prev_q_val + self.alpha * reward

    def eval(self, state):
        return super().act(state['observation'], state['reward'], learning=False)

    def stop(self, state):
        self.end_of_episode()

    def get_action_distr(self, state):
        '''
        Args:
            state (State)
            beta (float): Softmax temperature parameter.

        Returns:
            (list of floats): The i-th float corresponds to the probability
            mass associated with the i-th action (indexing into self.actions)
        '''
        beta = self._beta
        all_q_vals = []
        for _, action in enumerate(self.actions):
            all_q_vals.append(self.get_q_value(state, action))

        # Softmax distribution.
        total = sum([np.exp(np.logaddexp(beta * qv)) for qv in all_q_vals])
        softmax = [np.exp(np.logaddexp(beta * qv)) / total for qv in all_q_vals]

        return softmax

    def __repr__(self):
        r = []
        for s in self.q_func.keys():
            r.append(f"Q[{s}]= [{list(self.q_func[s].items())}]")
        return '\n'.join(r)


class OptQLearning(QLearning):
    def act(self, state, learning=True, timestep=1):
        if learning:
            self.update(self.prev_state, self.prev_action, state['reward'], state, timestep=timestep)
        if not state['done']:
            if self.explore == "softmax":
                # Softmax exploration
                action = self.soft_max_policy(state['observation'])
            else:
                # Uniform exploration
                action = self.epsilon_greedy_q_policy(state['observation'])
        else:
            action = self.actions[0]

        self.prev_state = state['observation']
        self.prev_action = action
        self.step_number += 1

        # Anneal params.
        if learning and self.anneal:
            self._anneal()

        return action

    def update(self, state, action, reward, next_state, timestep=1):
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
        prev_q_val = self.get_q_value(state, action)
        if not next_state['done']:
            max_q_curr_state = self.get_max_q_value(next_state['observation'])
            self.q_func[state][action] = (1 - self.alpha) * prev_q_val + self.alpha * (
                        reward + (self.gamma ** timestep) * max_q_curr_state)
        else:
            self.q_func[state][action] = (1 - self.alpha) * prev_q_val + self.alpha * reward

    def epsilon_greedy_q_policy(self, state):
        '''
        Args:
            state (State)

        Returns:
            (str): action.
        '''
        # Policy: Epsilon of the time explore, otherwise, greedyQ.
        if np.random.random() > self.epsilon:
            # Exploit.
            action = self.get_max_q_action(state)
        else:
            # Explore
            actions = self._get_active_options(state)
            action = np.random.choice(actions)

        return action

    def _compute_max_qval_action_pair(self, state):
        '''
        Args:
            state (State)

        Returns:
            (tuple) --> (float, str): where the float is the Qval, str is the action.
        '''
        # Grab random initial action in case all equal
        actions = self._get_active_options(state)
        best_action = random.choice(actions)
        max_q_val = float("-inf")
        shuffled_action_list = actions[:]
        random.shuffle(shuffled_action_list)

        # Find best action (action w/ current max predicted Q value)
        for action in shuffled_action_list:
            q_s_a = self.get_q_value(state, action)

            if q_s_a > max_q_val:
                max_q_val = q_s_a
                best_action = action

        return max_q_val, best_action

    def _get_active_options(self, state):
        return [o for o in self.actions if o.initiation(RLState(state.features()))]


class OptQLearningFactory(AgentFactory):
    def __init__(self,
                 actions, name="option-qlearning", alpha=0.1, gamma=0.99,
                 epsilon=0.1, explore="uniform", anneal=False,
                 custom_q_init=None, default_q=0):
        self._agent = OptQLearning(actions,
                                   name=name,
                                   alpha=alpha,
                                   gamma=gamma,
                                   epsilon=epsilon,
                                   explore=explore,
                                   anneal=anneal,
                                   custom_q_init=custom_q_init,
                                   default_q=default_q)


class LinearQLearningFactory(AgentFactory):
    def __init__(self, actions, features, rand_init=True, name="Linear-Q", alpha=0.2, gamma=0.99, epsilon=0.2,
                 explore="uniform", anneal=True):
        params = {"actions": actions,
                  "name": name,
                  "num_features": features.num_features(),
                  "rand_init": rand_init,
                  "alpha": alpha,
                  "gamma": gamma,
                  "epsilon": epsilon,
                  "explore": explore,
                  "anneal": anneal}
        self._agent = LinearQLearning(LinearQAgent, agent_params=params, feature_mapper=features)


class LinearQLearning(FeatureWrapper):
    def act(self, state):
        action = super().act(state['observation'], state['reward'])
        return action

    def eval(self, state):
        return super().act(state['observation'], state['reward'])

    def stop(self, state):
        self.end_of_episode()


# =====================================================================
from lmdp.agents.Agent import Agent
from all.presets.classic_control import vqn
from all.core.state import State
from collections import namedtuple
from copy import deepcopy
import torch

action_space = namedtuple('action_space', ['n', 'actions'])
state_space = namedtuple('state_space', ['shape'])
environment = namedtuple('environment', ['action_space', 'state_space'])


class QN(Agent):
    def __init__(self, actions, state_s, gamma=0.99, alpha=0.1, epsilon=0.1):
        envs = [environment(action_space(len(actions), actions), state_space(state_s))]
        self._vqn = vqn(discount_factor=gamma, lr=alpha, epsilon=epsilon, n_envs=1)[0](envs)
        self._actions = dict(enumerate(actions))

    def act(self, state):
        state = _all_state_wrapper(state)
        action = self._vqn.act(state).item()
        return self._actions[action]

    def eval(self, state):
        state = _all_state_wrapper(state)
        action = self._vqn.eval(state).item()
        return self._actions[action]

    def stop(self, state):
        pass


def _all_state_wrapper(state):
    state = deepcopy(state)
    state['observation'] = torch.from_numpy(state['observation'].features()).float()
    state['reward'] = torch.Tensor([state['reward']]).squeeze()
    state['done'] = torch.Tensor([state['done']]).squeeze()
    return State(state)


class QNFactory(AgentFactory):
    def __init__(self, actions, state_space, gamma=0.99, alpha=0.1, epsilon=0.1):
        AgentFactory.__init__(self, QN(actions, state_space, gamma, alpha, epsilon))


# ===================================================================================================
from all.presets.classic_control import dqn
from lmdp.agents.option_dqn import dqn as odqn


class DQN(Agent):
    def __init__(self, actions, state_s, gamma=0.99,
                 alpha=0.1, epsilon=0.1, replay_start_size=1000,
                 replay_buffer_size=2000, final_exploration_frame=5000,
                 target_update_frequency=10, model=fc_relu_q):
        envs = [environment(action_space(len(actions), actions), state_space(state_s))]
        self._dqn = dqn(discount_factor=gamma,
                        lr=alpha,
                        replay_start_size=replay_start_size,
                        replay_buffer_size=replay_buffer_size,
                        final_exploration_frame=final_exploration_frame,
                        model_constructor=model)(envs[0])
        self._actions = dict(enumerate(actions))

    def act(self, state):
        state = _all_state_wrapper(state)
        action = self._dqn.act(state)
        return self._actions[action]

    def eval(self, state):
        state = _all_state_wrapper(state)
        action = self._dqn.eval(state)
        return self._actions[action]

    def stop(self, state):
        pass


class OptDQN(DQN):
    def __init__(self, actions, state_s, gamma=0.99, alpha=0.1,
                 epsilon=0.1, replay_start_size=7000,
                 final_exploration_frame=10000, replay_buffer_size=2000,
                 target_update_frequency=5, model=fc_relu_q):
        envs = [environment(action_space(len(actions), actions), state_space(state_s))]
        self._dqn = odqn(discount_factor=gamma,
                         lr=alpha,
                         replay_start_size=replay_start_size,
                         replay_buffer_size=replay_buffer_size,
                         final_exploration_frame=final_exploration_frame,
                         model_constructor=model,
                         target_update_frequency=target_update_frequency)(envs[0])
        self._actions = dict(enumerate(actions))


class OptDQNFactory(AgentFactory):
    def __init__(self, actions, state_space,
                 gamma=0.99,
                 alpha=0.1,
                 epsilon=0.1,
                 replay_start_size=1000,
                 replay_buffer_size=2000,
                 final_exploration_frame=10000,
                 model_constructor=fc_relu_q,
                 target_update_frequency=5,
                 model=fc_relu_q):
        AgentFactory.__init__(self, OptDQN(actions, state_space,
                                           gamma,
                                           alpha,
                                           epsilon,
                                           model=model,
                                           replay_start_size=replay_start_size,
                                           replay_buffer_size=replay_buffer_size,
                                           final_exploration_frame=final_exploration_frame,
                                           target_update_frequency=target_update_frequency))


class DQNFactory(AgentFactory):
    def __init__(self, actions, state_space,
                 gamma=0.99, alpha=0.1, epsilon=0.1,
                 replay_start_size=1000,
                 replay_buffer_size=2000,
                 final_exploration_frame=5000,
                 model_constructor=fc_relu_q,
                 target_update_frequency=10,
                 model=fc_relu_q):
        AgentFactory.__init__(self, DQN(actions,
                                        state_space, gamma, alpha, epsilon,
                                        model=model,
                                        replay_start_size=replay_start_size,
                                        replay_buffer_size=replay_buffer_size,
                                        final_exploration_frame=final_exploration_frame,
                                        target_update_frequency=target_update_frequency))


class OptionInitMask(nn.Module):
    def __init__(self, options):
        super(OptionInitMask, self).__init__()
        self._options = options

    def forward(self, states):
        mask = torch.from_numpy(np.array([o.initiation(RLangState(states)) for o in self._options]))
        return mask.transpose(1, 0)


class masked_q(nn.Module):
    def __init__(self, p_model, options):
        super(masked_q, self).__init__()
        self._option_mask = OptionInitMask(options).requires_grad_(False)
        self._policy = p_model

    def forward(self, states):
        mask = self._option_mask(states)
        return mask * self._policy(states)


def masked_fc_relu_q(options):
    def _q(env):
        return masked_q(fc_relu_q(env), options)

    return _q
