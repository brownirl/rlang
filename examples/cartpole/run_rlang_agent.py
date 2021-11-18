
import argparse

import gym
import gym.spaces
import torch
from torch import nn

import pfrl
from pfrl import experiments, utils
from pfrl.policies import GaussianHeadWithFixedCovariance, SoftmaxCategoricalHead

import numpy as np

def train_agent_eval_agent(model, beta=0.75, name="", seed=0, output_dir='policy_pg_1', lr=1e-3, steps=10 ** 5):
    import logging

    parser = argparse.ArgumentParser()
    parser.add_argument("--env", type=str, default="CartPole-v0")
    parser.add_argument("--seed", type=int, default=seed, help="Random seed [0, 2 ** 32)")
    parser.add_argument("--gpu", type=int, default=-1)
    parser.add_argument(
        "--outdir",
        type=str,
        default=output_dir,
        help=(
            "Directory path to save output files."
            " If it does not exist, it will be created."
        ),
    )
    parser.add_argument("--beta", type=float, default=1e-4)
    parser.add_argument("--batchsize", type=int, default=10)
    parser.add_argument("--steps", type=int, default=steps)
    parser.add_argument("--eval-interval", type=int, default=10 ** 4)
    parser.add_argument("--eval-n-runs", type=int, default=100)
    parser.add_argument("--reward-scale-factor", type=float, default=1e-2)
    parser.add_argument("--render", action="store_true", default=False)
    parser.add_argument("--lr", type=float, default=lr)
    parser.add_argument("--demo", action="store_true", default=False)
    parser.add_argument("--load", type=str, default="")
    parser.add_argument("--log-level", type=int, default=logging.INFO)
    parser.add_argument("--monitor", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(level=args.log_level)

    # Set a random seed used in PFRL.
    utils.set_random_seed(args.seed)

    args.outdir = experiments.prepare_output_dir(args, args.outdir)

    def make_env(test):
        env = gym.make(args.env)
        # Use different random seeds for train and test envs
        env_seed = 2 ** 32 - 1 - args.seed if test else args.seed
        env.seed(env_seed)
        # Cast observations to float32 because our model uses float32
        env = pfrl.wrappers.CastObservationToFloat32(env)
        if args.monitor:
            env = pfrl.wrappers.Monitor(env, args.outdir)
        if not test:
            # Scale rewards (and thus returns) to a reasonable range so that
            # training is easier
            env = pfrl.wrappers.ScaleReward(env, args.reward_scale_factor)
        if args.render and not test:
            env = pfrl.wrappers.Render(env)
        return env

    train_env = make_env(test=False)
    timestep_limit = train_env.spec.max_episode_steps
    obs_space = train_env.observation_space
    action_space = train_env.action_space

    obs_size = obs_space.low.size
    hidden_size = 200
    
    # model = nn.Sequential(
    #     nn.Linear(obs_size, hidden_size),
    #     nn.LeakyReLU(0.2),
    #     nn.Linear(hidden_size, hidden_size),
    #     nn.LeakyReLU(0.2),
    #     nn.Linear(hidden_size, action_space.n),
    #     SoftmaxCategoricalHead(),
    # )

    opt = torch.optim.Adam(model.parameters(), lr=args.lr)

    agent = pfrl.agents.REINFORCE(
        model,
        opt,
        gpu=args.gpu,
        beta=args.beta,
        batchsize=args.batchsize,
        max_grad_norm=1.0,
    )
    if args.load:
        agent.load(args.load)

    eval_env = make_env(test=True)

    if args.demo:
        eval_stats = experiments.eval_performance(
            env=eval_env,
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
    else:
        experiments.train_agent_with_evaluation(
            agent=agent,
            env=train_env,
            eval_env=eval_env,
            outdir=f"{args.outdir}/{name}",
            steps=args.steps,
            eval_n_steps=None,
            eval_n_episodes=args.eval_n_runs,
            eval_interval=args.eval_interval,
            train_max_episode_len=timestep_limit,
            use_tensorboard=True
        )


class betaREINFORCE(pfrl.agents.REINFORCE):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._beta = 1.
        self._beta_seq = [[]]


    def _act_train(self, obs):
        ret = super()._act_train(obs)
        self._beta = self.model._beta
        self._beta_seq[-1].append(1/(1-self._beta))
        return ret

    def _observe_train(self, obs, reward, done, reset):
        if done or reset:
            if not done:
                self._beta_seq[-1] = []
            elif done:
                if not self.backward_separately:
                    if len(self.reward_sequences) != self.batchsize:
                        # Prepare for the next episode
                        self._beta_seq.append([])
        super()._observe_train(obs, reward, done, reset)


    def accumulate_grad(self):
        if self.n_backward == 0:
            self.optimizer.zero_grad()
        # Compute losses
        losses = []
        for r_seq, log_prob_seq, ent_seq, betas in zip(
            self.reward_sequences, self.log_prob_sequences, self.entropy_sequences, self._beta_seq
        ):
            assert len(r_seq) - 1 == len(log_prob_seq) == len(ent_seq)
            # Convert rewards into returns (=sum of future rewards)
            R_seq = np.cumsum(list(reversed(r_seq[1:])))[::-1]
            for R, log_prob, entropy, _beta in zip(R_seq, log_prob_seq, ent_seq, betas):
                loss = -R * _beta * log_prob - self.beta * entropy
                losses.append(loss)
        total_loss = torch.stack(losses).sum() / self.batchsize
        total_loss.backward()
        self.reward_sequences = [[]]
        self.log_prob_sequences = [[]]
        self.entropy_sequences = [[]]
        self._beta_seq = [[]]
        self.n_backward += 1

    def get_statistics(self):
        ret = super().get_statistics()
        ret.append(("last_beta", self._beta))
        return ret