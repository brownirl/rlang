import sys, os
sys.path.append(os.path.abspath("./"))

from envs.craftworld.craftworld_gym import Craftworld
from agents.models import dqn_q_head
from experiments.all_experiment import allExperimentRunner
from experiments.rlang_experiment import RLangExperiment

from lmdp.agents.rlang_hdqn import RLangHDQNFactory as rlang_hdqn, hdqn_hyperparameters, default_outer_cli_parameters, default_inner_cli_parameters
import lmdp.agents.dqn as dqn

from craft_subpolicies import program

import argparse

#====== AUX functions ==========================

def _get_args(args, dict_args):
    r = {}
    for arg in args:
        if arg in dict_args:
            r[arg] = dict_args[arg]
    return r
 
# ==============================================


parser = argparse.ArgumentParser(description='Craftworld-RLang Arguments', add_help=False)
parser.add_argument('--device', type=str, default='cpu', help='Device to run: cpu or cuda')
parser.add_argument('--tag', type=str, default='cpu', help='Device to run: cpu or gpu')

# Experiment params
experiment_params = ['nruns', 'frames', 'test_episodes', 'seed', 'logdir', 'name', 'device', 'max_frames_per_episode']

parser.add_argument('--nruns', type=int, default=1, help='Number of Runs')
parser.add_argument('--frames', type=int, default=100000, help='Max number of timesteps')
parser.add_argument('--test_episodes', type=int, default=10, help='Episodes to evaluate Agent')
parser.add_argument('--seed', type=int, default=argparse.SUPPRESS, help='Random Generator seed')
parser.add_argument('--logdir', type=str, default='results/craftworld/runs', help='Result logging directory')
parser.add_argument('--name', type=str, default='craft-dqn')
parser.add_argument('--max_frames_per_episode', type=int, default=10)

# Agent params
parser.add_argument('--outer_state_feature_dim', type=int, default=10, help='Final feature dimension')
parser.add_argument('--inner_state_feature_dim', type=int, default=256, help='Final feature dimension')
inner_agent_params = ['inner_state_feature_dim']
outer_agent_params = ['outer_state_feature_dim']

for k, v in default_outer_cli_parameters.items():
    parser.add_argument(f"--outer_{k}", type=type(v), default=v)
    outer_agent_params.append(f"outer_{k}")
for k, v in default_inner_cli_parameters.items():
    parser.add_argument(f"--inner_{k}", type=type(v), default=v)
    inner_agent_params.append(f"inner_{k}")

# Environment params
environment_params = ['goal']
parser.add_argument('--goal', type=str, default='bridge', help='Craftworld Goal')

# params dicts
params = vars(parser.parse_args())
params['logdir'] += '_' + params['tag']
exp_params = _get_args(experiment_params, params)

inner_agent_params = _get_args(inner_agent_params, params)
outer_agent_params = _get_args(outer_agent_params, params)

env_params = _get_args(environment_params, params)

# Environment Setup
craft = Craftworld(**env_params)
envs = [craft]

# Agents setup
agents = []
w, h, elements = craft.get_grid_params()
q_model_outer = dqn_q_head(w, h, elements, outer_agent_params['outer_state_feature_dim'])
q_model_inner= dqn_q_head(w, h, elements, inner_agent_params['inner_state_feature_dim'])

outer_agent_params['outer_model_constructor'] = q_model_outer  # outer q network constructor
inner_agent_params['inner_model_constructor'] = q_model_inner  # inner q network constructor

_dqn = dqn.dqn('craft-dqn', dqn.dqn_hyperparameters(**outer_agent_params))
_hdqn = rlang_hdqn(
                    'craft-hdqn', 
                    hdqn_hyperparameters(**{'discount_factor': outer_agent_params['outer_discount_factor'],
                                        'outer_dqn_params': outer_agent_params,
                                        'inner_dqn_params': inner_agent_params })
                )

# Experiment Setup and Run!
runner = allExperimentRunner()
experiment = RLangExperiment(rlang_programs=[program()],
                             rlang_agents=[_hdqn], 
                             agents=[], 
                             experiment_runner=runner)
for _ in range(exp_params['nruns']):
    experiment.run(envs, exp_params)