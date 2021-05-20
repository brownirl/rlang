from torch.optim import Adam
from all.agents import DQN
from all.approximation import QNetwork, FixedTarget
from all.logging import DummyWriter
from all.memory import ExperienceReplayBuffer
from all.optim import LinearScheduler
from all.policies import GreedyPolicy
from all.presets.classic_control.models import fc_relu_q
from all.approximation.checkpointer import PeriodicCheckpointer
from all.presets import PresetBuilder, Preset

from lmdp.agents.dqn import DQNPreset
from lmdp.grounding.states.StateClass import state_builder as RLangState
import numpy as np
import torch
import torch.nn as nn

from functools import partial
from collections import namedtuple

class OptionInitMask(nn.Module):
    def __init__(self, options):
        super(OptionInitMask, self).__init__()
        self._options = options

    def forward(self, states):
        s = RLangState(states)
        _m = [o.initiation(s) for o in self._options]
        mask = torch.Tensor(_m)
        return mask.transpose(1,0)


class masked_q(nn.Module):
    def __init__(self, p_model, options):
        super(masked_q, self).__init__()
        self._option_mask = OptionInitMask(options).requires_grad_(False)
        self._policy = p_model

    def forward(self, states):
        mask = self._option_mask(states).to(states.get_device())
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
        return torch.argmax(self.q(state)).item()

    def no_grad(self, state):
        if np.random.rand() < self.epsilon:
            return self.__random_action(state)
        return torch.argmax(self.q.no_grad(state)).item()

    def __get_active_options(self, state):
        active = torch.Tensor([o._id for o in self._options if o.initiation(RLangState(state['observation']))]).long()
        return active
    
    def __random_action(self, state):
        active_opts = self.__get_active_options(state)
        return np.random.choice(active_opts)


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

option_dqn = partial(PresetBuilder, constructor=OptionDQNPreset)

__all__ = ["option_dqn"]
