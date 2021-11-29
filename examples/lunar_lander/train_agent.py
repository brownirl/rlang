
import argparse

import gym
import gym.spaces
import torch
from torch import nn

import pfrl
from pfrl import experiments, utils
from pfrl.policies import GaussianHeadWithFixedCovariance, SoftmaxCategoricalHead
from pfrl.agents import PPO
import numpy as np

import functools
import logging

def parse_args(beta=0.75, name="", seed=0, output_dir='policy_pg_1', env="CartPole-v0", lr=3e-4, steps=10**5, render=False, demo=False):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--lr", type=float, default=lr, help="Learning rate"
    )
    parser.add_argument(
        "--gpu", type=int, default=-1, help="GPU to use, set to -1 if no GPU."
    )
    parser.add_argument(
        "--env",
        type=str,
        default=env,
        help="OpenAI Gym MuJoCo env to perform algorithm on.",
    )
    parser.add_argument(
        "--num-envs", type=int, default=1, help="Number of envs run in parallel."
    )
    parser.add_argument("--seed", type=int, default=seed, help="Random seed [0, 2 ** 32)")
    parser.add_argument(
        "--outdir",
        type=str,
        default=output_dir,
        help=(
            "Directory path to save output files."
            " If it does not exist, it will be created."
        ),
    )
    parser.add_argument(
        "--steps",
        type=int,
        default=steps,
        help="Total number of timesteps to train the agent.",
    )
    parser.add_argument(
        "--eval-interval",
        type=int,
        default=10000,
        help="Interval in timesteps between evaluations.",
    )
    parser.add_argument(
        "--eval-n-runs",
        type=int,
        default=100,
        help="Number of episodes run for each evaluation.",
    )
    parser.add_argument(
        "--render", action="store_true", default=render, help="Render env states in a GUI window."
    )
    parser.add_argument(
        "--demo", action="store_true", default=demo, help="Just run evaluation, not training."
    )
    parser.add_argument("--load-pretrained", action="store_true", default=False)
    parser.add_argument(
        "--load", type=str, default="", help="Directory to load agent from."
    )
    parser.add_argument(
        "--log-level", type=int, default=logging.INFO, help="Level of the root logger."
    )
    parser.add_argument(
        "--monitor", action="store_true", help="Wrap env with gym.wrappers.Monitor."
    )
    parser.add_argument(
        "--log-interval",
        type=int,
        default=1000,
        help="Interval in timesteps between outputting log messages during training",
    )
    parser.add_argument(
        "--update-interval",
        type=int,
        default=2048,
        help="Interval in timesteps between model updates.",
    )
    parser.add_argument(
        "--epochs",
        type=int,
        default=10,
        help="Number of epochs to update model for per PPO iteration.",
    )
    parser.add_argument("--batch-size", type=int, default=64, help="Minibatch size")

    parser.add_argument("--exp_id", type=str, default="", help="Experiment tag")

    args, _ = parser.parse_known_args()

    return args

def train_agent_ppo(vf, policy, anneal=False, obs_normalizer=None, args=None, beta=0.75, name="", seed=0, output_dir='policy_pg_1', env="CartPole-v0", lr=3e-4, steps=10**5, render=False, demo=False):
    args = parse_args(beta, name, seed, output_dir, env, lr, steps, render, demo) if args is None else args

    logging.basicConfig(level=args.log_level)

    # Set a random seed used in PFRL
    utils.set_random_seed(args.seed)

    # Set different random seeds for different subprocesses.
    # If seed=0 and processes=4, subprocess seeds are [0, 1, 2, 3].
    # If seed=1 and processes=4, subprocess seeds are [4, 5, 6, 7].
    process_seeds = np.arange(args.num_envs) + args.seed * args.num_envs
    assert process_seeds.max() < 2 ** 32

    args.outdir = experiments.prepare_output_dir(args, args.outdir, exp_id=args.exp_id)

    def make_env(process_idx, test):
        env = gym.make(args.env)
        # Use different random seeds for train and test envs
        process_seed = int(process_seeds[process_idx])
        env_seed = 2 ** 32 - 1 - process_seed if test else process_seed
        env.seed(env_seed)
        # Cast observations to float32 because our model uses float32
        env = pfrl.wrappers.CastObservationToFloat32(env)
        if args.monitor:
            env = pfrl.wrappers.Monitor(env, args.outdir)
        if args.render:
            env = pfrl.wrappers.Render(env)
        return env

    def make_batch_env(test):
        return pfrl.envs.MultiprocessVectorEnv(
            [
                functools.partial(make_env, idx, test)
                for idx, env in enumerate(range(args.num_envs))
            ]
        )

    # Only for getting timesteps, and obs-action spaces
    sample_env = gym.make(args.env)
    timestep_limit = sample_env.spec.max_episode_steps
    obs_space = sample_env.observation_space
    action_space = sample_env.action_space
    print("Observation space:", obs_space)
    print("Action space:", action_space)

    # assert isinstance(action_space, gym.spaces.Box)

    # Normalize observations based on their empirical mean and variance
    obs_normalizer = pfrl.nn.EmpiricalNormalization(
        obs_space.low.size, clip_threshold=5
    ) if obs_normalizer is None else obs_normalizer

    obs_size = obs_space.low.size
    action_size = action_space.n

    # vf = torch.nn.Sequential(
    #     nn.Linear(obs_size, 64),
    #     nn.Tanh(),
    #     nn.Linear(64, 64),
    #     nn.Tanh(),
    #     nn.Linear(64, 1),
    # )

    # While the original paper initialized weights by normal distribution,
    # we use orthogonal initialization as the latest openai/baselines does.
    def ortho_init(layer, gain):
        nn.init.orthogonal_(layer.weight, gain=gain)
        nn.init.zeros_(layer.bias)

    # ortho_init(policy[0], gain=1)
    # ortho_init(policy[2], gain=1)
    # ortho_init(policy[4], gain=1e-2)
    #ortho_init(vf[0], gain=1)
    # ortho_init(vf[2], gain=1)
    # ortho_init(vf[4], gain=1)

    # Combine a policy and a value function into a single model
    model = pfrl.nn.Branched(policy, vf)
    opt = torch.optim.Adam(model.parameters(), lr=args.lr, eps=1e-5)

    agent_type = annealedPPO if anneal else PPO

    agent = agent_type(
        model,
        opt,
        obs_normalizer=obs_normalizer,
        gpu=args.gpu,
        update_interval=args.update_interval,
        minibatch_size=args.batch_size,
        epochs=args.epochs,
        clip_eps_vf=None,
        entropy_coef=0,
        standardize_advantages=True,
        gamma=0.995,
        lambd=0.97,
    )

    if args.load or args.load_pretrained:
        # either load or load_pretrained must be false
        assert not args.load or not args.load_pretrained
        if args.load:
            agent.load(args.load)
        else:
            agent.load(utils.download_model("PPO", args.env, model_type="final")[0])

    if args.demo:
        env = make_batch_env(True)
        eval_stats = experiments.eval_performance(
            env=env,
            agent=agent,
            n_steps=None,
            n_episodes=args.eval_n_runs,
            max_episode_len=timestep_limit,
        )
        print(
            "n_runs: {} mean: {} median: {} stdev {}".format(
                args.eval_n_runs,
                eval_stats["mean"],
                eval_stats["median"],
                eval_stats["stdev"],
            )
        )
        import json
        import os
        demo_outdir = args.outdir + "/random_init_performance"
        os.makedirs(demo_outdir, exist_ok=True)
        with open(os.path.join(demo_outdir, "demo_scores.json"), "w") as f:
            json.dump(eval_stats, f)
    else:
        eval_stats = experiments.train_agent_batch_with_evaluation(
                agent=agent,
                env=make_batch_env(False),
                eval_env=make_batch_env(True),
                outdir=args.outdir,
                steps=args.steps,
                eval_n_steps=None,
                eval_n_episodes=args.eval_n_runs,
                eval_interval=args.eval_interval,
                log_interval=args.log_interval,
                max_episode_len=timestep_limit,
                save_best_so_far_agent=False,
                use_tensorboard=True
            )

class annealedPPO(PPO):
    def _update(self, dataset):
        super()._update(dataset)
        self.model.child_modules[0].anneal()

    def get_statistics(self):
        stats = super().get_statistics()
        stats.append(("beta param", self.model.child_modules[0]._beta))
        return stats