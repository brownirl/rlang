
import argparse

import gym
import gym.spaces
import torch
from torch import nn

import pfrl
from pfrl import experiments, utils
from pfrl.policies import GaussianHeadWithFixedCovariance, SoftmaxCategoricalHead

import numpy as np
import logging, os, json

def parse_args(seed, output_dir, steps, lr, demo):
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
    parser.add_argument("--demo", action="store_true", default=demo)
    parser.add_argument("--load", type=str, default="")
    parser.add_argument("--log-level", type=int, default=logging.INFO)
    parser.add_argument("--monitor", action="store_true")
    parser.add_argument("--exp-id", type=str, default='')
    args, _ = parser.parse_known_args()
    return args

def train_reinforce(model, anneal=False, beta=0.75, name="", seed=0, output_dir='policy_pg_1', lr=1e-3, steps=10 ** 5, demo=False):

    args = parse_args(seed, output_dir, steps, lr, demo)

    logging.basicConfig(level=args.log_level)

    # Set a random seed used in PFRL.
    utils.set_random_seed(args.seed)

    args.outdir = experiments.prepare_output_dir(args, args.outdir, exp_id=args.exp_id)

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

    opt = torch.optim.Adam(model.parameters(), lr=args.lr)
    agent_type = pfrl.agents.REINFORCE if not anneal else betaREINFORCE
    agent = agent_type(
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
    if demo:
        args.outdir += "/init_eval"
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
        demo_outdir = args.outdir + "/random_init_performance"
        os.makedirs(demo_outdir, exist_ok=True)
        with open(os.path.join(demo_outdir, "demo_scores.json"), "w") as f:
            json.dump(eval_stats, f)
    else:
        experiments.train_agent_with_evaluation(
            agent=agent,
            env=train_env,
            eval_env=eval_env,
            outdir=f"{args.outdir}/{args.exp_id}",
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


    def _act_train(self, obs):
        ret = super()._act_train(obs)
        self._beta = self.model._beta
        return ret

    def accumulate_grad(self):
        if self.n_backward == 0:
            self.optimizer.zero_grad()
        # Compute losses
        losses = []
        for r_seq, log_prob_seq, ent_seq in zip(
            self.reward_sequences, self.log_prob_sequences, self.entropy_sequences
        ):
            assert len(r_seq) - 1 == len(log_prob_seq) == len(ent_seq)
            # Convert rewards into returns (=sum of future rewards)
            R_seq = np.cumsum(list(reversed(r_seq[1:])))[::-1]
            for R, log_prob, entropy in zip(R_seq, log_prob_seq, ent_seq):
                loss = -R * log_prob - self.beta * entropy
                losses.append(loss)
        total_loss = torch.stack(losses).sum() / self.batchsize
        total_loss.backward()
        self.reward_sequences = [[]]
        self.log_prob_sequences = [[]]
        self.entropy_sequences = [[]]
        self.n_backward += 1

        self.model.anneal()

    def batch_update(self):
        super().batch_update()
        self.model.anneal()

    def update_with_accumulated_grad(self):
        super().update_with_accumulated_grad()
        self.model.anneal()

    def get_statistics(self):
        ret = super().get_statistics()
        ret.append(("last_beta", self.model._beta))
        return ret
