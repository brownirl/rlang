from torch.optim import Adam
from all.core import StateArray
from all.agents import DDQN as DQN
from all.approximation import QNetwork, FixedTarget
from all.logging import DummyWriter
from all.memory import ExperienceReplayBuffer
from all.optim import LinearScheduler
from all.policies import GreedyPolicy
from all.presets import PresetBuilder, Preset

from lmdp.grounding.states.StateClass import State, BatchedState
from lmdp.grounding.states.StateClass import state_builder as RLangState
import numpy as np
import torch
import torch.nn as nn

from functools import partial
from collections import namedtuple


def state_builder(state):
    if isinstance(state, StateArray):
        return BatchedState(state.observation)
    else:
        return State(state.observation)


class OptionInitMask(nn.Module):
    def __init__(self, options):
        super(OptionInitMask, self).__init__()
        self._options = options

    def forward(self, states):
        s = RLangState(states)
        _m = [o.initiation(s) for o in self._options]
        mask = torch.stack(_m)
        return mask.transpose(1, 0)


class masked_q(nn.Module):
    def __init__(self, p_model, options):
        super(masked_q, self).__init__()
        self._option_mask = OptionInitMask(options).requires_grad_(False)
        self._policy = p_model

    def forward(self, states):
        device = states.get_device()
        if device > 0:
            mask = self._option_mask(states).to(device)
        else:
            mask = self._option_mask(states)
        return mask * self._policy(states)


class OptionGreedyPolicy(GreedyPolicy):
    def __init__(
            self,
            q,
            options,
            epsilon=0.,
    ):
        super(OptionGreedyPolicy, self).__init__(q, len(options), epsilon)
        self._options = options

    def __call__(self, state):
        if np.random.rand() < self.epsilon:
            return self.__random_action(state)
        active = self.get_active_options_mask(state)
        q_values = self.q(state)
        min_q = torch.min(q_values)
        q_values = q_values * active + (min_q - 1) * ~active
        return torch.argmax(q_values).item()

    def no_grad(self, state):
        if np.random.rand() < self.epsilon:
            return self.__random_action(state)

        active = self.get_active_options_mask(state)
        q_values = self.q.no_grad(state)
        min_q = q_values.min()
        q_values = q_values * active + (min_q - 1) * ~active
        return torch.argmax(q_values).item()

    def __get_active_options(self, state):
        s = State(state['observation'])
        active = torch.Tensor([idx for idx, o in enumerate(self._options) if o.initiation(s) & ~o.terminated(s)]).long()
        device = state['observation'].get_device()
        if device > 0:
            active.to(device)
        return active

    def get_active_options_mask(self, states):
        s = state_builder(states)
        active = [o.initiation(s) & ~o.terminated(s) for o in self._options]  # (batch x 1)
        return torch.stack(active)  # batch x action

    def __random_action(self, state):
        active_opts = self.__get_active_options(state)
        return active_opts[torch.randint(len(active_opts), (1,))].item()


class OptionDQNPreset(Preset):
    def __init__(self, env, name, device, options, **hyperparameters):
        if options is None:
            raise ValueError("Options needed!")
        _env_type = namedtuple('env', ['action_space'])
        _action_space = namedtuple('action_space', ['n'])
        _env = _env_type(_action_space(len(options)))
        self.n_options = len(options)
        self.options = options
        self.model = hyperparameters['model_constructor'](env).to(device)

    def agent(self, writer=DummyWriter(), train_steps=float('inf')):
        optimizer = Adam(self.model.parameters(), lr=self.hyperparameters['lr'])

        q = QNetwork(
            masked_q(self.model, self.options),
            optimizer,
            target=FixedTarget(self.hyperparameters['target_update_frequency']),
            writer=writer
        )

        policy = OptionGreedyPolicy(
            q,
            self.options,
            epsilon=LinearScheduler(
                self.hyperparameters['initial_exploration'],
                self.hyperparameters['final_exploration'],
                self.hyperparameters['replay_start_size'],
                self.hyperparameters['final_exploration_step'] - self.hyperparameters['replay_start_size'],
                name="exploration",
                writer=writer
            )
        )

        replay_buffer = ExperienceReplayBuffer(
            self.hyperparameters['replay_buffer_size'],
            device=self.device
        )

        return DQN(
            q,
            policy,
            replay_buffer,
            discount_factor=self.hyperparameters['discount_factor'],
            minibatch_size=self.hyperparameters['minibatch_size'],
            replay_start_size=self.hyperparameters['replay_start_size'],
            update_frequency=self.hyperparameters['update_frequency'],
        )


class OptionDDQN(DQN):

    def __init__(self, options, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._options = options

    def _train(self):
        if self._should_train():
            # sample transitions from buffer
            (states, actions, rewards, next_states, weights) = self.replay_buffer.sample(self.minibatch_size)
            # forward pass
            values = self.q(states, actions)  # batch x action
            # compute targets
            _q_values = self.q.no_grad(next_states)
            active_mask = self._get_active_options(next_states)
            min_q_values, _ = torch.min(_q_values, dim=1, keepdim=True)
            next_actions = torch.argmax(~active_mask * (min_q_values - 1) + _q_values * active_mask, dim=1)
            done_mask = next_states['done']
            targets = rewards + self.discount_factor * self.q.target(next_states, next_actions) * ~done_mask
            # compute loss
            loss = self.loss(values, targets, weights)
            # backward pass
            self.q.reinforce(loss)
            # update replay buffer priorities
            td_errors = targets - values
            self.replay_buffer.update_priorities(td_errors.abs())

    def _get_active_options(self, states):
        s = state_builder(states)
        active = [o.initiation(s) & ~o.terminated(s) for o in self._options]  # (batch x 1)
        return torch.stack(active).transpose(1, 0)  # batch x action

    def _train_step(self, curr_state, action, next_state):
        self.replay_buffer.store(curr_state, action, next_state)
        self._train()


option_dqn = partial(PresetBuilder, constructor=OptionDQNPreset)

__all__ = ["option_dqn"]
