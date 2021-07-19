from lmdp.agents.rlang_agent_builder import RLangBuilderFactory
from lmdp.agents.all_hierarchical_dqn import HDQNPreset

from all.presets import PresetBuilder
from all.presets.classic_control.models import fc_relu_q

import copy
import re

default_inner_cli_parameters = {
    # Common settings
    "discount_factor": 0.99,
    # Adam optimizer settings
    "lr": 1e-4,
    # Training settings
    "minibatch_size": 128,
    "update_frequency": 1,
    "target_update_frequency": 100,
    # Replay buffer settings
    "replay_start_size": 200,
    "replay_buffer_size": 10000,
    # Explicit exploration
    "initial_exploration": 1.,
    "final_exploration": 0.001,
    "final_exploration_step": 40000,
    "test_exploration": 0.001,
    "timeout": 100
}

default_outer_cli_parameters = {
    # Common settings
    "discount_factor": 0.99,
    # Adam optimizer settings
    "lr": 1e-5,
    # Training settings
    "minibatch_size": 32,
    "update_frequency": 1,
    "target_update_frequency": 100,
    # Replay buffer settings
    "replay_start_size": 10,
    "replay_buffer_size": 10000,
    # Explicit exploration
    "initial_exploration": 1.,
    "final_exploration": 0.,
    "final_exploration_step": 60000,
    "test_exploration": 0.001
}

default_inner_params = {
    # Common settings
    "discount_factor": 0.99,
    # Adam optimizer settings
    "lr": 1e-4,
    # Training settings
    "minibatch_size": 128,
    "update_frequency": 1,
    "target_update_frequency": 100,
    # Replay buffer settings
    "replay_start_size": 200,
    "replay_buffer_size": 10000,
    # Explicit exploration
    "initial_exploration": 1.,
    "final_exploration": 0.01,
    "final_exploration_step": 5000,
    "test_exploration": 0.001,
    # Model construction
    "model_constructor": fc_relu_q,
    "timeout": 100
}

default_outer_params = {
    # Common settings
    "discount_factor": 0.99,
    # Adam optimizer settings
    "lr": 1e-4,
    # Training settings
    "minibatch_size": 64,
    "update_frequency": 1,
    "target_update_frequency": 100,
    # Replay buffer settings
    "replay_start_size": 10,
    "replay_buffer_size": 10000,
    # Explicit exploration
    "initial_exploration": 1.,
    "final_exploration": 0.,
    "final_exploration_step": 500,
    "test_exploration": 0.001,
    # Model construction
    "model_constructor": fc_relu_q,
}

default_hyperparameters = {
    'discount_factor': 0.99,
    'outer_dqn_params': default_outer_params,
    'inner_dqn_params': default_inner_params
}


def adapt_hyperparams(default_hyperparams, hyperparameters):
    pattern = re.compile('^(inner|outer)?')
    prefix = pattern.match(list(hyperparameters.keys())[0]).group(0)
    if len(prefix) > 0:
        prefix += '_'
    h = copy.deepcopy(default_hyperparams)
    for k in h.keys():
        k_ = prefix + k
        h[k] = hyperparameters[k_] if k_ in hyperparameters else h[k]
    return h


def hdqn_hyperparameters(**hyperparameters):
    h = copy.deepcopy(default_hyperparameters)
    for k, v in h.items():
        if isinstance(v, dict):
            if k in hyperparameters:
                h[k] = adapt_hyperparams(v, hyperparameters[k])
        else:
            h[k] = hyperparameters[k] if k in hyperparameters else h[k]
    return h


class RLangHDQNFactory(RLangBuilderFactory):
    def __init__(self, name, hyperparams=default_hyperparameters):
        self._options = {}
        self.name = name
        self.hyperparams = hyperparams

    def inform(self, lmdp):
        # returns a Preset Builder informed by an RLang Program
        self._options['learnable'] = self.__get_learnable_options(lmdp)
        self._options['non_learnable'] = self.__get_non_learnable_options(lmdp)
        self.hyperparams['options'] = self._options
        return PresetBuilder(
            default_name=self.name,
            default_hyperparameters=self.hyperparams,
            constructor=HDQNPreset
        )

    def __get_learnable_options(self, lmdp):
        opts = [s.to_option() for s in lmdp.get_subpolicies()]
        return [o for o in opts if o.is_learnable()]

    def __get_non_learnable_options(self, lmdp):
        opts = [s.to_option() for s in lmdp.get_subpolicies()]
        return [o for o in opts if not o.is_learnable()]
