import sys, os
sys.path.append(os.path.abspath("./"))

from envs.craftworld.craftworld_gym import Craftworld
from agents.models import dqn_q_head
from experiments.all_experiment import allExperimentRunner
from experiments.rlang_experiment import RLangExperiment

import lmdp.agents.dqn as dqn

import argparse

def _get_args(args, dict_args):
    r = {}
    for arg in args:
        if arg in dict_args:
            r[arg] = dict_args[arg]
    return r


parser = argparse.ArgumentParser(description='Craftworld-RLang Arguments', add_help=False)
parser.add_argument('--device', type=str, default='cpu', help='Device to run: cpu or gpu')
parser.add_argument('--tag', type=str, default='cpu', help='Device to run: cpu or gpu')

# Experiment params
experiment_params = ['nruns', 'frames', 'test_episodes', 'seed', 'logdir', 'name', 'device', 'max_frames_per_episode']

parser.add_argument('--nruns', type=int, default=1, help='Number of Runs')
parser.add_argument('--frames', type=int, default=1000, help='Max number of timesteps')
parser.add_argument('--test_episodes', type=int, default=10, help='Episodes to evaluate Agent')
parser.add_argument('--seed', type=int, default=argparse.SUPPRESS, help='Random Generator seed')
parser.add_argument('--logdir', type=str, default='results/craftworld/runs', help='Result logging directory')
parser.add_argument('--name', type=str, default='craft-dqn')
parser.add_argument('--max_frames_per_episode', type=int, default=10000)

# Agent params
parser.add_argument('--state_feature_dim', type=int, default=256, help='Final feature dimension')
agent_params = list(dqn.default_cli_args.keys()) + ['state_feature_dim']
for k, v in dqn.default_cli_args.items():
    parser.add_argument(f"--{k}", type=type(v), default=v)

# Environment params
environment_params = ['goal']
parser.add_argument('--goal', type=str, default='gold', help='Craftworld Goal')

# params dicts
params = vars(parser.parse_args())
params['logdir'] += params['tag']
exp_params = _get_args(experiment_params, params)
agent_params = _get_args(agent_params, params)
env_params = _get_args(environment_params, params)

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