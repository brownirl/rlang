from simple_rl.run_experiments import run_agents_on_mdp, run_single_agent_on_mdp
from simple_rl.tasks import TaxiOOMDP
from simple_rl.agents import QLearningAgent, RandomAgent

import context
import rlang


# from rlang.agents import RLangQLearningAgent


def main(open_plot=True):
    # Taxi initial state attributes..
    agent = {"x": 1, "y": 1, "has_passenger": 0}
    passengers = [{"x": 3, "y": 2, "dest_x": 2, "dest_y": 3, "in_taxi": 0}]
    walls = []
    mdp = TaxiOOMDP(width=4, height=4, agent=agent, walls=walls, passengers=passengers)

    # Agents.
    ql_agent = QLearningAgent(actions=mdp.get_actions())
    rand_agent = RandomAgent(actions=mdp.get_actions())

    viz = False
    if viz:
        # Visualize Taxi.
        run_single_agent_on_mdp(ql_agent, mdp, episodes=200, steps=1000)
        mdp.visualize_agent(ql_agent)
    else:
        # Run experiment and make plot.
        run_agents_on_mdp([ql_agent, rand_agent], mdp, instances=10, episodes=20, steps=500, reset_at_terminal=True,
                          open_plot=open_plot)


if __name__ == '__main__':
    main()
