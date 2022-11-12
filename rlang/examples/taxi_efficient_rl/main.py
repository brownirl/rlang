from efficient_rl.environment.oo_mdp import OOTaxi
from efficient_rl.environment.classical_mdp import ClassicalTaxi
from efficient_rl.environment.factored_mdp import FactoredTaxi
from efficient_rl.agents import Rmax, FactoredRmax, DOORmax, QLearning
from prettytable import PrettyTable
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

import context
import rlang
from rlang.grounding import ObjectOrientedState
from rlang.agents import RLangDOORmaxAgent
from grounding import TaxiClass, PassengerClass


def flat_state_to_oo_state(flat_state, base_oo_state):
    if flat_state[0] == 1:
        base_oo_state.taxi.touch_n = True
    else:
        base_oo_state.taxi.touch_n = False
    if flat_state[1] == 1:
        base_oo_state.taxi.touch_s = True
    else:
        base_oo_state.taxi.touch_s = False
    if flat_state[2] == 1:
        base_oo_state.taxi.touch_e = True
    else:
        base_oo_state.taxi.touch_e = False
    if flat_state[3] == 1:
        base_oo_state.taxi.touch_w = True
    else:
        base_oo_state.taxi.touch_w = False
    if flat_state[4] == 1:
        base_oo_state.taxi.on_passenger = True
    else:
        base_oo_state.taxi.on_passenger = False
    if flat_state[5] == 1:
        base_oo_state.taxi.on_destination = True
    else:
        base_oo_state.taxi.on_destination = False
    if flat_state[6] == 1:
        base_oo_state.passenger.in_taxi = True
    else:
        base_oo_state.passenger.in_taxi = False

    return base_oo_state


def generate_states():
    def pad_bin(state_str):
        if len(state_str) < 7:
            return pad_bin('0' + state_str)
        else:
            return state_str

    flat_states = list()

    for i in range(128):
        bin_state = list(map(int, list(pad_bin(bin(i)[2:]))))
        flat_states.append(np.array(bin_state, dtype=np.float64))

    return flat_states


def test():
    flat_states = generate_states()

    taxi = TaxiClass("taxi", on_passenger=True)
    passenger = PassengerClass("passenger", in_taxi=False)
    state = ObjectOrientedState(objects={taxi, passenger})

    print(flat_state_to_oo_state(flat_states[-1], state))

    env = OOTaxi()

    agent = DOORmax(nS=500, nA=6, r_max=20, gamma=0.95, delta=0.01,
                    env_name='gym-Taxi', k=5, num_atts=env.num_atts,
                    eff_types=['assignment', 'addition'],
                    oo_mdp_dict=env.oo_mdp_dict)

    agent.add_experience_to_reward_learner((None, env.cond()), 0, 5.0)


def create_oomdp_and_agents():
    actions = list(range(6))

    flat_states = generate_states()

    taxi = TaxiClass("taxi", on_passenger=True)
    passenger = PassengerClass("passenger", in_taxi=False)
    state = ObjectOrientedState(objects={taxi, passenger})

    # initialization of agents and environments
    knowledge = rlang.parse_file("taxi.rlang")
    agent_names = ['RLangDOORmax', 'DOORmax', 'Rmax', 'Factored Rmax', 'Q Learning',
               'Q Learning optimistic initalization']
    envs = [OOTaxi(), OOTaxi(), ClassicalTaxi(), FactoredTaxi(), ClassicalTaxi(), ClassicalTaxi()]
    agents = [RLangDOORmaxAgent(actions=actions, flat_states=flat_states, base_oo_state=state,
                                flat_state_to_oo_state=flat_state_to_oo_state,
                                knowledge=knowledge, nS=500, nA=6, r_max=20, gamma=0.95, delta=0.01,
                                env_name='gym-Taxi', k=5, num_atts=envs[0].num_atts,
                                eff_types=['assignment', 'addition'],
                                oo_mdp_dict=envs[0].oo_mdp_dict),
              DOORmax(nS=500, nA=6, r_max=20, gamma=0.95, delta=0.01,
                      env_name='gym-Taxi', k=5, num_atts=envs[0].num_atts,
                      eff_types=['assignment', 'addition'],
                      oo_mdp_dict=envs[1].oo_mdp_dict),
              Rmax(M=1, nS=500, nA=6, r_max=20, gamma=0.95, delta=0.01, env_name='gym-Taxi'),
              FactoredRmax(M=1, nS_per_var=[5, 5, 5, 4], nA=6, r_max=20, gamma=0.95,
                           delta=0.01, DBNs=envs[3].DBNs, factored_mdp_dict=envs[3].factored_mdp_dict,
                           env_name='gym-Taxi'),
              QLearning(nS=500, nA=6, gamma=0.95, alpha=0.1, epsilon=0.6,
                        optimistic_init=False, env_name='gym-Taxi'),
              QLearning(nS=500, nA=6, gamma=0.95, alpha=1, epsilon=0, r_max=20,
                        optimistic_init=True, env_name='gym-Taxi')
              ]
    return agents, envs, agent_names


def calc_cum_rewards(rewards):
    cum_rewards = []
    j = 0
    for reward in rewards:
        j += reward
        cum_rewards.append(j)
    return cum_rewards


def calc_cum_disc_rewards(rewards, gamma):
    multiplier = 1.0
    cum_rewards = []
    j = 0
    for reward in rewards:
        j += multiplier * reward
        cum_rewards.append(j)
        multiplier *= gamma
    return j


def train_agent(agent, env, max_episodes, max_steps, show_intermediate=True):
    aggregate_rewards, all_step_times, complete_rewards = [], [], []
    for i_episode in range(max_episodes):
        env.reset()
        rewards, step_times = agent.main(env, max_steps, deterministic=False)

        complete_rewards.extend(rewards)
        aggregate_rewards.append(calc_cum_disc_rewards(rewards, gamma=0.95))
        all_step_times.extend(step_times)
        if i_episode % 100 == 0 and show_intermediate:
            print('Episode: {}, Reward: {}, Avg_Step: {}'.format(i_episode + 1, aggregate_rewards[-1],
                                                                 np.mean(step_times)))
        # print(len(complete_rewards))
        # optimum_accomplished = agent.evaluate_on_probes(env, max_steps)
        # if optimum_accomplished:
        #     break
    return aggregate_rewards, all_step_times, complete_rewards


def run_experiment(agents, envs, agent_names, n_repetitions, max_episodes, max_steps):
    statistics = {}
    for agent, env, agent_name in zip(agents, envs, agent_names):
        all_aggregate_rewards, all_step_times, all_complete_rewards = [], [], []
        for i_rep in range(n_repetitions):  # repeat agent training n_repetitions times
            print('Start Agent: ', agent_name, ' current repetition: ', i_rep + 1, '/', n_repetitions)
            agent.reset()
            aggregate_rewards, step_times, complete_rewards = train_agent(agent, env, max_episodes=max_episodes,
                                                                          max_steps=max_steps,
                                                                          show_intermediate=False)
            print('steps total: {}, avg step time: {}, sum reward: {}'.format(len(step_times), np.mean(step_times),
                                                                              sum(aggregate_rewards)))
            agent.reset()

            all_step_times.extend(step_times)
            all_aggregate_rewards.append(aggregate_rewards)
            all_complete_rewards.append(complete_rewards)
            # print(aggregate_rewards)
            # print(complete_rewards)

        print(
            'steps total: {}, step time: {}, total time: {}, total reward: {}'.format(
                len(all_step_times) / n_repetitions,
                np.mean(all_step_times),
                sum(all_step_times) / n_repetitions,
                sum(map(sum, all_aggregate_rewards))))
        # print(all_complete_rewards)
        statistics[agent_name] = {'avg steps total': len(all_step_times) / n_repetitions,
                                  'avg step time': np.mean(all_step_times),
                                  'avg total time': sum(all_step_times) / n_repetitions,
                                  'avg reward': sum(map(sum, all_aggregate_rewards)) / n_repetitions,
                                  'agg reward': all_aggregate_rewards,
                                  'all reward': all_complete_rewards}
    return statistics


def plot_results(statistics, discounted=True):
    print('\n Results: \n')
    table = PrettyTable(['Agent', 'avg steps total', 'avg step time', 'avg total time', 'avg reward'])
    runs = []
    for name_of_agent, data_agent in statistics.items():
        table.add_row([name_of_agent,
                       np.round(data_agent['avg steps total'], 4),
                       np.round(data_agent['avg step time'], 5),
                       np.round(data_agent['avg total time'], 2),
                       np.round(data_agent['avg reward'], 2)])

        if discounted:
            for cr in data_agent['agg reward']:
                exp_data = dict()
                exp_data['return'] = np.array(cr)
                exp_data['episode'] = np.arange(len(exp_data['return']))
                exp_data['agent'] = name_of_agent
                runs.append(pd.DataFrame(exp_data))
        else:
            all_rewards = data_agent['all reward']
            cum_rewards = list(map(calc_cum_rewards, all_rewards))
            for cr in cum_rewards:
                exp_data = dict()
                exp_data['reward'] = np.array(cr)
                exp_data['iteration'] = np.arange(len(exp_data['reward']))
                exp_data['agent'] = name_of_agent
                runs.append(pd.DataFrame(exp_data))
    print(table)

    data = pd.concat(runs)
    if discounted:
        ax = sns.lineplot(data=data, x='episode', y='return', hue="agent", alpha=0.8)
        ax.set(xlabel='Episode', ylabel="Return", title="Agent Performance on Taxi")
        plt.show()
    else:
        ax = sns.lineplot(data=data, x='iteration', y='reward', hue="agent", alpha=0.8)
        ax.set(xlabel='Time Step', ylabel="Cumulative Reward", title="Agent Performance on Taxi")
        plt.show()


def main():
    n_repetitions = 5
    max_episodes = 100
    max_steps = 5000

    agents, envs, agent_names = create_oomdp_and_agents()
    statistics = run_experiment(agents, envs, agent_names, n_repetitions, max_episodes, max_steps)

    plot_results(statistics, discounted=False)


def oomdp_probe():
    env = OOTaxi()
    initial_state = env.reset()
    print(initial_state)
    print(env.convert_gym_state_into_OO_MDP_state())
    print(env.cond().dtype)
    env.render()
    env.human_play()


def rlang_object_probe():
    taxi = TaxiClass("taxi", on_passenger=True)
    passenger = PassengerClass("passenger", in_taxi=False)
    state = ObjectOrientedState(objects={taxi, passenger})

    knowledge = rlang.parse_file("taxi.rlang")

    predictions = knowledge.predictions(state=state, action=4)
    # print(predictions)

    taxi = TaxiClass("taxi", on_destination=True)
    passenger = PassengerClass("passenger", in_taxi=True)
    state = ObjectOrientedState(objects={taxi, passenger})

    predictions = knowledge.predictions(state=state, action=5)
    print(predictions)

    rewards = knowledge.reward_function(state=state, action=5)
    print(rewards)  # Should be 20

    rewards = knowledge.reward_function(state=state, action=4)
    print(rewards)  # Should be -10

    rewards = knowledge.reward_function(state=state, action=1)
    print(rewards)  # Should be -1


if __name__ == "__main__":
    # print(generate_states())
    # oomdp_probe()
    main()
    # test()
