import numpy as np
import torch
from collections import deque
from tqdm import tqdm



def supervised_init(model, rlang_policy, state_space, batchsize=32, iters=40000, lr=1e-5, beta=0.8, n_actions=4):
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    log_freq = 1000
    for i in tqdm(range(iters)):
        # generate sample
        batch = torch.Tensor([state_space.sample() for _ in range(batchsize)])
        labels = rlang_policy(batch) * beta + (1-beta)/n_actions
        # compute models
        actions = torch.nn.functional.softmax(model(batch), dim=-1)
        # print(torch.log(labels))
        loss = (-labels * actions).sum(dim=-1).mean()
        loss.backward()
        optimizer.step()
        if i % log_freq == 0:
            print(f"Loss: {loss} at iteration {i}")


def evaluate_policy(policy, value_network, env, epochs=100, n_trajectories=5000, batchsize=64, gamma=0.99):

    ## Collect trajectories.
    trajectories = []

    for t in tqdm(range(n_trajectories)):
        done = False
        obs = env.reset()
        actions = []
        obss = []
        next_obss = []
        dones = []
        rewards = []
        prev_loss = deque([], maxlen=5)
        while not done:
            action = policy(torch.from_numpy(obs).unsqueeze(0)).sample()
            next_obs, reward, done, _ = env.step(action.item())
            obss.append(obs)
            actions.append(action)
            next_obss.append(next_obs)
            rewards.append(reward)
            dones.append(done)            
            if done:
                trajectories.append((torch.Tensor(obss),
                                     torch.Tensor(actions),
                                     torch.Tensor(rewards),
                                     torch.Tensor(next_obss),
                                     torch.Tensor(dones)))
    ## Prepare dataset
    
    dataset = []
    _ins = []
    _returns = []
    
    for trajectory in trajectories:
        _ins.append(trajectory[0]) # obss
        _rewards = trajectory[2] ## rewards
        _returns.append(torch.flip(torch.flip(_rewards, dims=(0,)).cumsum(dim=-1), dims=(0,)))


    _ins = torch.cat(_ins)
    _returns = torch.cat(_returns)
    n_data = _ins.size()[0]
    ## Initialize value network
    optimizer = torch.optim.Adam(value_network.parameters(), lr=1e-5)
    for e in range(epochs):
        loss = 0.
        losses = []
        for i in tqdm(range(0, n_data, batchsize)):
            values = value_network(_ins[i:i + batchsize])
            target = _returns[i:i + batchsize]
            loss = ((values - target) ** 2).mean()
            loss.backward()
            optimizer.step()
            losses.append(loss)
        _loss = sum(losses)/len(losses)
        print(f"Epoch {e}: Loss {_loss}")
        prev_loss.append(_loss)
        if prev_loss[-1] - prev_loss[0] > 0:
            break




