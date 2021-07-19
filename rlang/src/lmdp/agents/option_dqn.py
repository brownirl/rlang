from torch.optim import Adam
from all.agents import DQN
from all.approximation import QNetwork, FixedTarget
from all.logging import DummyWriter
from all.memory import ExperienceReplayBuffer
from all.optim import LinearScheduler
from all.policies import GreedyPolicy
from all.presets.classic_control.models import fc_relu_q
from lmdp.grounding.states.StateClass import State
import numpy as np
import torch

import dill
from all.approximation.checkpointer import PeriodicCheckpointer


class DillPeriodicCheckpointer(PeriodicCheckpointer):
    def __call__(self):
        if self._updates % self.frequency == 0:
            torch.save(self._model, self._filename, pickle_module=dill)
        self._updates += 1


def dqn(
        # Common settings
        device="cpu",
        discount_factor=0.99,
        # Adam optimizer settings
        lr=1e-3,
        # Training settings
        minibatch_size=64,
        update_frequency=1,
        target_update_frequency=100,
        # Replay buffer settings
        replay_start_size=1000,
        replay_buffer_size=10000,
        # Exploration settings
        initial_exploration=1.,
        final_exploration=0.,
        final_exploration_frame=10000,
        # Model construction
        model_constructor=fc_relu_q
):
    """
    DQN classic control preset.

    Args:
        device (str): The device to load parameters and buffers onto for this agent.
        discount_factor (float): Discount factor for future rewards.
        lr (float): Learning rate for the Adam optimizer.
        minibatch_size (int): Number of experiences to sample in each training update.
        update_frequency (int): Number of timesteps per training update.
        target_update_frequency (int): Number of timesteps between updates the target network.
        replay_start_size (int): Number of experiences in replay buffer when training begins.
        replay_buffer_size (int): Maximum number of experiences to store in the replay buffer.
        initial_exploration (int): Initial probability of choosing a random action,
            decayed until final_exploration_frame.
        final_exploration (int): Final probability of choosing a random action.
        final_exploration_frame (int): The frame where the exploration decay stops.
        model_constructor (function): The function used to construct the neural model.
    """

    def _dqn(env, writer=DummyWriter()):
        model = model_constructor(env).to(device)
        optimizer = Adam(model.parameters(), lr=lr)
        q = QNetwork(
            model,
            optimizer,
            target=FixedTarget(target_update_frequency),
            writer=writer,
            checkpointer=DillPeriodicCheckpointer(200)
        )
        policy = OptionGreedyPolicy(
            q,
            env.action_space.actions,
            epsilon=LinearScheduler(
                initial_exploration,
                final_exploration,
                replay_start_size,
                final_exploration_frame,
                name="epsilon",
                writer=writer
            )
        )
        replay_buffer = ExperienceReplayBuffer(
            replay_buffer_size, device=device)
        return DQN(
            q,
            policy,
            replay_buffer,
            discount_factor=discount_factor,
            minibatch_size=minibatch_size,
            replay_start_size=replay_start_size,
            update_frequency=update_frequency,
        )

    return _dqn


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
        active = torch.Tensor([o._id for o in self._options if o.initiation(State(state.observation)).squeeze()]).long()
        return active

    def __random_action(self, state):
        active_opts = self.__get_active_options(state)
        return np.random.choice(active_opts)


__all__ = ["dqn"]
