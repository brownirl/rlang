import all.experiments as allexp
from all.environments.gym import GymEnvironment as allgym
from experiments.rlang_experiment import ExperimentRunner

class allExperimentRunner(ExperimentRunner):
    def __call__(self, agents, envs, device='cpu', **experiments_params):
        '''
            agents: all.agent (list)
            envs: gym.Env (list)
        '''
        envs = list(map(lambda e: allgym(e, device=device), envs))
        allexp.run_experiment(agents, 
                              envs,
                              **experiments_params
                             )