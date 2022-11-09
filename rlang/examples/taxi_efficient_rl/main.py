from efficient_rl.environment.oo_mdp import OOTaxi
from efficient_rl.agents import DOORmax
from prettytable import PrettyTable
import numpy as np

import context
import rlang
from rlang.grounding import ObjectOrientedState
from grounding import TaxiClass, PassengerClass


def create_oomdp_and_agents():
    # initialization of agents and environments
    agent_names = ['DOORmax']
    envs = [OOTaxi()]
    agents = [DOORmax(nS=500, nA=6, r_max=20, gamma=0.95, delta=0.01,
                      env_name='gym-Taxi', k=5, num_atts=envs[0].num_atts,
                      eff_types=['assignment', 'addition'],
                      oo_mdp_dict=envs[0].oo_mdp_dict)]  # alpha/epsilon p.33/34 Diuks Diss
    return agents, envs, agent_names


def run_experiment(agents, envs, agent_names, n_repetitions, max_episodes, max_steps):
    statistics = {}
    for agent, env, agent_name in zip(agents, envs, agent_names):
        all_step_times = []
        for i_rep in range(n_repetitions):  # repeat agent training n_repetitions times
            print('Start Agent: ', agent_name, ' current repetition: ', i_rep + 1, '/', n_repetitions)
            _, step_times = agent.train(env, max_episodes=max_episodes, max_steps=max_steps,
                                        show_intermediate=False)
            print('steps total: {}, avg step time: {}'.format(len(step_times), np.mean(step_times)))
            agent.reset()

            all_step_times.extend(step_times)

        print('steps total:{}, step time:{}, total time:{}'.format(len(all_step_times)/n_repetitions,
                                                                   np.mean(all_step_times),
                                                                   sum(all_step_times)/n_repetitions))
        statistics[agent_name] = {'avg steps total': len(all_step_times)/n_repetitions,
                                  'avg step time': np.mean(all_step_times),
                                  'avg total time': sum(all_step_times)/n_repetitions}
    return statistics


def plot_results(statistics):
    print('\n Results: \n')
    table = PrettyTable(['Agent', 'avg steps total', 'avg step time', 'avg total time'])
    for name_of_agent, data_agent in statistics.items():
        table.add_row([name_of_agent,
                       data_agent['avg steps total'],
                       np.round(data_agent['avg step time'], 5),
                       np.round(data_agent['avg total time'], 2)])
    print(table)


def main():
    n_repetitions = 1
    max_episodes = 5000
    max_steps = 100

    agents, envs, agent_names = create_oomdp_and_agents()
    statistics = run_experiment(agents, envs, agent_names, n_repetitions, max_episodes, max_steps)

    plot_results(statistics)


def oomdp_probe():
    env = OOTaxi()
    initial_state = env.reset()
    print(initial_state)
    print(env.convert_gym_state_into_OO_MDP_state())
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
    rlang_object_probe()
