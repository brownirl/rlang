class ExperimentRunner:
    def __call__(self, agents, envs, **experiment_params):
        pass


class RLangExperiment:
    def __init__(self, rlang_programs=[], rlang_agents=[], agents=[], experiment_runner=None):
        self.rlang_programs = rlang_programs
        self.rlang_agents = rlang_agents
        self.agents = agents
        self.experiment_runner = experiment_runner

    def run(self, envs, experiment_params=None):
        agents = [ragent.inform(lmdp) for ragent in self.rlang_agents for lmdp in self.rlang_programs] + self.agents
        self.experiment_runner(agents, envs, **experiment_params) 