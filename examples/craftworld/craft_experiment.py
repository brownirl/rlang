import sys, os
sys.path.append(os.path.abspath("./"))

from envs.craftworld.craftworld_gym import Craftworld
from networks import CraftFeatureNetwork, fc_value_head, fc_policy_head
from experiments.all_experiment import allExperimentRunner
from experiments.rlang_experiment import RLangExperiment

from lmdp.agents.ppo import ppo as PPO

import argparse

parser = argparse.ArgumentParser(description='Craftworld-RLang Arguments', add_help=False)
parser.add_argument('--device', type=str, default='cpu', help='Device to run: cpu or gpu')

# Experiment params
exp_parser = argparse.ArgumentParser(parents=[parser], description='Craftworld-RLang Experiment Arguments')
exp_parser.add_argument('--nruns', type=int, default=1, help='Number of Runs')
exp_parser.add_argument('--frames', type=int, default=1000, help='Max number of timesteps')
exp_parser.add_argument('--test_episodes', type=int, default=100, help='Episodes to evaluate Agent')
exp_parser.add_argument('--seed', type=int, default=argparse.SUPPRESS, help='Random Generator seed')
exp_parser.add_argument('--logdir', type=str, default='results/runs', help='Result logging directory')
exp_parser.add_argument('--name', type=str, default='craft-ppo')

# Agent params
agent_parser = argparse.ArgumentParser(parents=[parser], description='Craftworld-RLang Agent Arguments')
agent_parser.add_argument('--state_feature_dim', type=int, default=256, help='Final feature dimension')
agent_parser.add_argument('--lr', type=float, default=1e-3, help='Learning Rate')
agent_parser.add_argument('--epsilon', type=float, default=0.2, help='Epsilon')
agent_parser.add_argument('--clip_grad', type=float, default=0.1, help='Clip grad')
agent_parser.add_argument('--lam', type=float, default=0.95, help='GAE lambda')
agent_parser.add_argument('--epochs', type=int, default=4, help='Epochs')
agent_parser.add_argument('--minibatches', type=int, default=4, help='# minibatches')
agent_parser.add_argument('--n_envs', type=int, default=1, help='# Parallel Environments')
agent_parser.add_argument('--n_steps', type=int, default=8, help='# Environments Steps')

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
feature_head = CraftFeatureNetwork(w, h, elements, out=agent_params['state_feature_dim'])
policy_head = fc_policy_head(agent_params['state_feature_dim'])
value_head = fc_value_head(agent_params['state_feature_dim'])
ppo, _ = PPO(**agent_params,
        feature_model_constructor=feature_head,
        value_model_constructor=value_head,
        policy_model_constructor=policy_head)

# Experiment Setup and Run!
runner = allExperimentRunner()
experiment = RLangExperiment(agents=[ppo], experiment_runner=runner)
experiments_params = dict(list(map(lambda p: (p,exp_params[p]), ['frames', 'test_episodes', 'logdir'])))
for _ in range(exp_params['nruns']):
    experiment.run(envs, experiments_params)