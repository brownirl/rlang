import copy
from torch.optim import Adam
from all.agents import DQN, DQNTestAgent
from all.approximation import QNetwork, FixedTarget
from all.logging import DummyWriter
from all.memory import PrioritizedReplayBuffer as ExperienceReplayBuffer
from all.optim import LinearScheduler
from all.policies import GreedyPolicy
from all.presets.builder import PresetBuilder
from all.presets.preset import Preset
from all.presets.classic_control.models import fc_relu_q

from functools import partial

default_hyperparameters = {
    # Common settings
    "discount_factor": 0.99,
    # Adam optimizer settings
    "lr": 1e-3,
    # Training settings
    "minibatch_size": 64,
    "update_frequency": 1,
    "target_update_frequency": 100,
    # Replay buffer settings
    "replay_start_size": 100,
    "replay_buffer_size": 10000,
    # Explicit exploration
    "initial_exploration": 1.,
    "final_exploration": 0.,
    "final_exploration_step": 10000,
    "test_exploration": 0.001,
    # Model construction
    "model_constructor": fc_relu_q
    }

default_cli_args = {
    # Common settings
    "discount_factor": 0.99,
    # Adam optimizer settings
    "lr": 1e-3,
    # Training settings
    "minibatch_size": 64,
    "update_frequency": 1,
    "target_update_frequency": 100,
    # Replay buffer settings
    "replay_start_size": 1000,
    "replay_buffer_size": 10000,
    # Explicit exploration
    "initial_exploration": 1.,
    "final_exploration": 0.,
    "final_exploration_step": 10000,
    "test_exploration": 0.001,
    }


def dqn_hyperparameters(**hyperparameters):
    h = copy.deepcopy(default_hyperparameters)
    for k in h.keys():
        h[k] = hyperparameters[k] if k in hyperparameters else h[k]
    return h


class DQNPreset(Preset):
    """
    Deep Q-Network (DQN) Classic Control Preset.

    Args:
        env (all.environments.AtariEnvironment): The environment for which to construct the agent.
        name (str): A human-readable name for the preset.
        device (torch.device): The device on which to load the agent.

    Keyword Args:
        discount_factor (float, optional): Discount factor for future rewards.
        lr (float): Learning rate for the Adam optimizer.
        minibatch_size (int): Number of experiences to sample in each training update.
        update_frequency (int): Number of timesteps per training update.
        target_update_frequency (int): Number of timesteps between updates the target network.
        replay_start_size (int): Number of experiences in replay buffer when training begins.
        replay_buffer_size (int): Maximum number of experiences to store in the replay buffer.
        initial_exploration (float): Initial probability of choosing a random action,
            decayed over course of training.
        final_exploration (float): Final probability of choosing a random action.
        final_exploration_step (int): The step at which exploration decay is finished
        test_exploration (float): The exploration rate of the test Agent
        model_constructor (function): The function used to construct the neural model.
    """

    def __init__(self, env, name, device, **hyperparameters):
        super().__init__(name, device, hyperparameters)
        self.model = hyperparameters['model_constructor'](env).to(device)
        self.n_actions = env.action_space.n

    def agent(self, writer=DummyWriter(), train_steps=float('inf')):
        optimizer = Adam(self.model.parameters(), lr=self.hyperparameters['lr'])

        q = QNetwork(
            self.model,
            optimizer,
            target=FixedTarget(self.hyperparameters['target_update_frequency']),
            writer=writer
        )

        policy = GreedyPolicy(
            q,
            self.n_actions,
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
        

    def test_agent(self):
        q = QNetwork(copy.deepcopy(self.model))
        return DQNTestAgent(q, self.n_actions, exploration=self.hyperparameters['test_exploration'])

    def save(self, filename):
        del self.hyperparameters['model_constructor']
        super().save(filename)

dqn = partial(PresetBuilder, constructor=DQNPreset)