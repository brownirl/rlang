from efficient_rl.environment.oo_mdp import OOTaxi
from efficient_rl.agents import DOORmax
from prettytable import PrettyTable
import numpy as np

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
    agent_names = ['RLangDOORmax', 'DOORmax']
    envs = [OOTaxi(), OOTaxi()]
    agents = [RLangDOORmaxAgent(actions=actions, flat_states=flat_states, base_oo_state=state,
                                flat_state_to_oo_state=flat_state_to_oo_state,
                                knowledge=knowledge, nS=500, nA=6, r_max=20, gamma=0.95, delta=0.01,
                                env_name='gym-Taxi', k=5, num_atts=envs[1].num_atts,
                                eff_types=['assignment', 'addition'],
                                oo_mdp_dict=envs[1].oo_mdp_dict),
              DOORmax(nS=500, nA=6, r_max=20, gamma=0.95, delta=0.01,
                      env_name='gym-Taxi', k=5, num_atts=envs[0].num_atts,
                      eff_types=['assignment', 'addition'],
                      oo_mdp_dict=envs[0].oo_mdp_dict)
              ]  # alpha/epsilon p.33/34 Diuks Diss
    return agents, envs, agent_names


def run_experiment(agents, envs, agent_names, n_repetitions, max_episodes, max_steps):
    statistics = {}
    for agent, env, agent_name in zip(agents, envs, agent_names):
        all_step_times = []
        all_rewards = []
        for i_rep in range(n_repetitions):  # repeat agent training n_repetitions times
            print('Start Agent: ', agent_name, ' current repetition: ', i_rep + 1, '/', n_repetitions)
            agent.reset()
            rewards, step_times = agent.train(env, max_episodes=max_episodes, max_steps=max_steps,
                                              show_intermediate=False)
            print('steps total: {}, avg step time: {}, sum reward: {}'.format(len(step_times), np.mean(step_times),
                                                                              sum(rewards)))
            agent.reset()

            all_step_times.extend(step_times)
            all_rewards.append(rewards)
            print(rewards)

        print(
            'steps total: {}, step time: {}, total time: {}, total reward: {}'.format(
                len(all_step_times) / n_repetitions,
                np.mean(all_step_times),
                sum(all_step_times) / n_repetitions,
                sum(map(sum, all_rewards))))
        statistics[agent_name] = {'avg steps total': len(all_step_times) / n_repetitions,
                                  'avg step time': np.mean(all_step_times),
                                  'avg total time': sum(all_step_times) / n_repetitions,
                                  'avg reward': sum(map(sum, all_rewards)) / n_repetitions,
                                  'all reward': all_rewards}
    return statistics


def plot_results(statistics, agents, envs):
    def calc_cum_rewards(rewards):
        cum_rewards = list()
        for reward in rewards:
            cum_rewards.append(reward + cum_rewards[-1])
        return cum_rewards

    print('\n Results: \n')
    table = PrettyTable(['Agent', 'avg steps total', 'avg step time', 'avg total time', 'avg reward'])
    for name_of_agent, data_agent in statistics.items():
        table.add_row([name_of_agent,
                       np.round(data_agent['avg steps total'], 4),
                       np.round(data_agent['avg step time'], 5),
                       np.round(data_agent['avg total time'], 2),
                       np.round(data_agent['avg reward'], 2)])
    print(table)

    print(statistics)

    # for agent, env, name_of_agent, data_agent in zip(agents, envs, *list(statistics.items()):
    #     agent.plot_rewards(data_agent['all reward'], env)
    # for name_of_agent, data_agent in statistics.items():
    #     all_cum_rewards = list()
    #     for all_rewards in data_agent['all reward']:
    #         for run_rewards in all_rewards:
    #             cum_rewards = calc_cum_rewards(run_rewards)
    #             all_cum_rewards.append(cum_rewards)
    #     print(all_cum_rewards)
    #     print(len(all_cum_rewards))
    #     print(len(all_cum_rewards[0]))







def main():
    n_repetitions = 2
    max_episodes = 5000
    max_steps = 200

    agents, envs, agent_names = create_oomdp_and_agents()
    statistics = run_experiment(agents, envs, agent_names, n_repetitions, max_episodes, max_steps)

    plot_results(statistics, agents, envs)



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
