import random, os

import gym
import torch
from torch import nn
import pfrl
from pfrl.policies import SoftmaxCategoricalHead

import context
import rlang
from rlang.agents import RLangPolicyAgent
from rlang.agents.utils.supervised_init import supervised_init, evaluate_policy
from rlang.agents.utils.control_sharing import ControlSharingPolicy, beta_scheduler, linear_scheduler
from rlang.agents.utils.ppo_agent import train_agent_ppo
from rlang.agents.utils.product_policy import ProductPolicy

import argparse


def make_advice_policy(rlang_policy, n_actions):
    advice_policy = RLangPolicyAgent(rlang_policy, n_actions=n_actions)
    return advice_policy


def make_uninformed_agent_model(obs_size=4, action_space=2, hidden_size=64):
    model = nn.Sequential(
        nn.Linear(obs_size, hidden_size),
        nn.LeakyReLU(0.2),
        nn.Linear(hidden_size, hidden_size),
        nn.LeakyReLU(0.2),
        nn.Linear(hidden_size, action_space),
    )

    agent_model = nn.Sequential(
        model,
        SoftmaxCategoricalHead()
    )

    value_network = torch.nn.Sequential(
        nn.Linear(8, 64),
        nn.Tanh(),
        nn.Linear(64, 64),
        nn.Tanh(),
        nn.Linear(64, 1),
    )
    return agent_model, model, value_network


def supervised_initialization(model, learning_policy, advice_policy, value_network):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--sup-advice-policy", type=str, default='./lunar_lander_policy', help="Saved Advice Policy path"
    )
    parser.add_argument(
        "--sup-lr", type=float, default=1e-5, help="Supervised init learning rate"
    )
    parser.add_argument(
        "--sup-batchsize", type=int, default=32, help="Supervised init batchsize"
    )

    parser.add_argument(
        "--sup-n-trajectories", type=int, default=1000, help="Supervised init Number of trajectories"
    )

    parser.add_argument(
        "--sup-epochs", type=int, default=100, help="Supervised init Number of Epochs to initialize Value function"
    )

    parser.add_argument(
        "--sup-iters", type=int, default=40000,
        help="Supervised init Number of iterations to initialize Policy function"
    )

    env = "LunarLander-v2"
    args, _ = parser.parse_known_args()
    policy_path = args.sup_advice_policy

    if not os.path.exists(policy_path):
        supervised_init(model, advice_policy, gym.make(env).observation_space, batchsize=args.sup_batchsize,
                        iters=args.sup_iters, lr=args.sup_lr)
        torch.save(learning_policy.state_dict(), policy_path)
    else:
        learning_policy.load_state_dict(torch.load(policy_path))

    evaluate_policy(learning_policy, value_network, gym.make(env), epochs=args.sup_epochs,
                    n_trajectories=args.sup_n_trajectories)

    return learning_policy, value_network


def policy_mixing(policy_model, advice_policy, obs_normalizer=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mix-beta", type=float, default=0.8, help="initial mixing parameter"
    )
    parser.add_argument(
        "--mix-scheduler", type=str, default="exponential", help="exponential, linear or constant"
    )

    parser.add_argument(
        "--mix-decay-rate", type=float, default=0.9999, help="annealing factor"
    )

    parser.add_argument(
        "--steps", type=int, default=5e5, help="annealing factor"
    )

    args, _ = parser.parse_known_args()
    scheduler_type = args.mix_scheduler.strip().lower()
    if scheduler_type == "exponential":
        scheduler = beta_scheduler(args.mix_beta, args.mix_decay_rate)
    elif scheduler_type == "linear":
        scheduler = linear_scheduler(init=args.mix_beta, n_steps=args.steps / 1000)
    elif scheduler_type == "constant":
        scheduler = lambda: args.mix_beta
    else:
        raise ValueError(f"No scheduler of type {scheduler_type}")
    advice_policy.set_obs_normalizer(obs_normalizer)
    return ControlSharingPolicy(policy_model, advice_policy, scheduler)


def product_policy(model, advice_policy):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--product-eps", type=float, default=0.1, help="epsilon-greedy exploration"
    )
    args, _ = parser.parse_known_args()

    return ProductPolicy(model, advice_policy)


def oracle_policy(policy, vf):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--oracle", type=str, default="", help="path to oracle policy"
    )
    args, _ = parser.parse_known_args()

    model = pfrl.nn.Branched(policy, vf)
    opt = torch.optim.Adam(model.parameters(), lr=3e-4, eps=1e-5)
    obs_normalizer = pfrl.nn.EmpiricalNormalization(
        8, clip_threshold=5
    )
    agent = pfrl.agents.PPO(
        model,
        opt,
        obs_normalizer=obs_normalizer,
        gpu=-1,
        update_interval=1,
        minibatch_size=1,
        epochs=1,
        clip_eps_vf=None,
        entropy_coef=0,
        standardize_advantages=True,
        gamma=0.995,
        lambd=0.97,
    )

    agent.load(args.oracle)

    return policy, vf, obs_normalizer


def rlang_experiment():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--experiment", type=str, default="policy-mixing", help="supervised, product policy or policy mixing"
    )

    parser.add_argument(
        "--policy", type=str, default="heuristic", help="heuristic or suboptimal"
    )

    parser.add_argument(
        "--rlang", type=str, default="./near_optimal_policy.rlang", help="Path to RLang policy"
    )

    args, _ = parser.parse_known_args()

    env = "LunarLander-v2"
    learning_policy, model, value_network = make_uninformed_agent_model(action_space=4, obs_size=8)

    knowledge = rlang.parse_file(args.rlang)

    policy = knowledge['land']

    advice_policy = make_advice_policy(policy, n_actions=4)
    obs_normalizer = pfrl.nn.EmpiricalNormalization(
        8, clip_threshold=5
    )
    # obs_normalizer = None
    anneal = False
    experiment = args.experiment.lower().strip()

    if experiment == "supervised":
        print("Supervised initialization experiment")
        learning_policy, value_network = supervised_initialization(model, learning_policy, advice_policy, value_network)
    elif experiment == "policy-mixing":
        print("Policy Mixing experiment")
        learning_policy = policy_mixing(model, advice_policy, obs_normalizer=obs_normalizer)
        anneal = True
    elif experiment == "product-policy":
        print("Product policy experiment")
        learning_policy = product_policy(learning_policy, advice_policy)
    elif experiment == "oracle":
        print("Oracle experiment")
        advice_model = model
        advice_policy, _, obs_normalizer = oracle_policy(learning_policy, value_network)
        learning_policy, learning_model, value_network = make_uninformed_agent_model(action_space=4, obs_size=8)
        model.requires_grad_ = False
        learning_policy = policy_mixing(learning_model, advice_model)
        anneal = True

    train_agent_ppo(value_network, learning_policy, anneal=anneal, obs_normalizer=obs_normalizer, env="LunarLander-v2",
                    steps=5e5, demo=True)  # evaluate at 0.
    train_agent_ppo(value_network, learning_policy, anneal=anneal, obs_normalizer=obs_normalizer,
                    name="rlang-informed",
                    env=env,
                    output_dir='lunar_lander_results',
                    render=False)  # RLang-informed agent


if __name__ == '__main__':
    rlang_experiment()
