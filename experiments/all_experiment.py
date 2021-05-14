import all.experiments as allexp
from all.environments.gym import GymEnvironment as allgym
from experiments.rlang_experiment import ExperimentRunner

all_experiment_params = ['frames', 'test_episodes', 'logdir']

class allExperimentRunner(ExperimentRunner):
    def __call__(self, agents, envs, **experiments_params):
        '''
            agents: all.agent (list)
            envs: gym.Env (list)
        '''
        device = experiments_params['device']
        experiments_params = dict(list(map(lambda p: (p,experiments_params[p]), all_experiment_params)))
        agents = list(map(lambda a: a.device(device), agents))
        envs = list(map(lambda e: allgym(e, device=device), envs))
        allexp.run_experiment(agents, 
                              envs,
                              **experiments_params
                             )