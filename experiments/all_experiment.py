import all.experiments as allexp
from all.environments.gym import GymEnvironment as allgym

import numpy as np
from timeit import default_timer as timer
from experiments.rlang_experiment import ExperimentRunner

all_experiment_params = ['frames', 'test_episodes', 'logdir', 'max_frames_per_episode']

def run_experiment(
        agents,
        envs,
        frames,
        max_frames_per_episode=np.float('inf'),
        logdir='runs',
        quiet=False,
        render=False,
        test_episodes=100,
        write_loss=True,
        writer="tensorboard"
):
    if not isinstance(agents, list):
        agents = [agents]

    if not isinstance(envs, list):
        envs = [envs]

    for env in envs:
        for preset_builder in agents:
            preset = preset_builder.env(env).build()
            experiment = SingleEnvExperiment(
                preset,
                env,
                max_frames_per_episode=max_frames_per_episode,
                train_steps=frames,
                logdir=logdir,
                quiet=quiet,
                render=render,
                write_loss=write_loss,
                writer=writer
            )
            experiment.train(frames=frames)
            experiment.save()
            experiment.test(episodes=test_episodes)
            experiment.close()


class SingleEnvExperiment(allexp.SingleEnvExperiment):
    def __init__(self, *args, max_frames_per_episode=np.float('inf'), **kwargs):
        allexp.SingleEnvExperiment.__init__(self, *args, **kwargs)
        self._max_frames_per_episode = max_frames_per_episode

    def _run_training_episode(self):
        # initialize timer
        start_time = timer()
        start_frame = self._frame

        # loop until the episode is finished
        returns = self.__rollout_episode()

        # stop the timer
        end_time = timer()
        fps = (self._frame - start_frame) #/ (end_time - start_time)

        # log the results
        self._log_training_episode(returns, fps)

        # update experiment state
        self._episode += 1
    
    def __rollout_episode(self):
        state = self._env.reset()
        action = self._agent.act(state)
        returns = 0
        frames = 0
        while not state.done:
            if(frames > self._max_frames_per_episode):
                if (hasattr(self._agent, 'reset')):
                    self._agent.reset()
                break
            if self._render:
                self._env.render()
            state = self._env.step(action)
            action = self._agent.act(state)
            returns += state.reward
            self._frame += 1
            frames += 1
        return returns
    
    def _run_test_episode(self, test_agent):
        # initialize the episode
        state = self._env.reset()
        action = test_agent.act(state)
        returns = 0
        frames = 0
        # loop until the episode is finished
        while not state.done and self._max_frames_per_episode > frames:
            if self._render:
                self._env.render()
            state = self._env.step(action)
            action = test_agent.act(state)
            returns += state.reward
            frames += 1

        return returns

class allExperimentRunner(ExperimentRunner):
    def __call__(self, agents, envs, **experiments_params):
        '''
            agents: all.agent (list)
            envs: gym.Env (list)
        '''
        device = experiments_params['device']
        experiments_params = dict(list(map(lambda p: (p,experiments_params[p]), all_experiment_params)))
        agents = list(map(lambda a: a.device(device), agents))
        envs = list(map(lambda e: allgym(e, device=device, name=e.name), envs))
        run_experiment(
                        agents, 
                        envs,
                        **experiments_params
                    )