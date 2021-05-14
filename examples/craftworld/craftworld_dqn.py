import sys, os
sys.path.append(os.path.abspath("./"))

from envs.craftworld.craftworld_gym import Craftworld
from networks import dqn_q_head
from experiments.all_experiment import allExperimentRunner
from experiments.rlang_experiment import RLangExperiment

import lmdp.agents.dqn as dqn

import argparse

parser = argparse.ArgumentParser(description='Craftworld-RLang Arguments', add_help=False)
parser.add_argument('--device', type=str, default='cpu', help='Device to run: cpu or gpu')

# Experiment params
exp_parser = argparse.ArgumentParser(parents=[parser], description='Craftworld-RLang Experiment Arguments')
exp_parser.add_argument('--nruns', type=int, default=1, help='Number of Runs')
exp_parser.add_argument('--frames', type=int, default=1000, help='Max number of timesteps')
exp_parser.add_argument('--test_episodes', type=int, default=100, help='Episodes to evaluate Agent')
exp_parser.add_argument('--seed', type=int, default=argparse.SUPPRESS, help='Random Generator seed')
exp_parser.add_argument('--logdir', type=str, default='results/craftworld/runs', help='Result logging directory')
exp_parser.add_argument('--name', type=str, default='craft-ppo')

# Agent params
agent_parser = argparse.ArgumentParser(parents=[parser], description='Craftworld-RLang Agent Arguments')
agent_parser.add_argument('--state_feature_dim', type=int, default=256, help='Final feature dimension')
for k, v in dqn.default_cli_args.items():
    agent_parser.add_argument(f"--{k}", type=type(v), default=v)

# Environment params
env_parser = argparse.ArgumentParser(parents=[parser], description='Craftworld-RLang Environment Arguments')
env_parser.add_argument('--goal', type=str, default='gold', help='Craftworld Goal')

# params dicts
exp_params = vars(exp_parser.parse_args())
agent_params = vars(agent_parser.parse_args())
env_params = vars(env_parser.parse_args())

# Environment Setup
craft = Craftworld(**env_params)
envs = [craft]

# Agents setup
agents = []
w, h, elements = craft.get_grid_params()
q_model = dqn_q_head(w, h, elements, agent_params['state_feature_dim'])
_dqn = dqn.dqn('craft-flat-dqn', dqn.dqn_hyperparameters(**agent_params, model_constructor=q_model))

# Experiment Setup and Run!
runner = allExperimentRunner()
experiment = RLangExperiment(agents=[_dqn], experiment_runner=runner)
for _ in range(exp_params['nruns']):
    experiment.run(envs, exp_params)