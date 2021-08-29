import sys, os
sys.path.append(os.path.abspath("./"))
from lmdp import *
from agents.experiment_runner import run_agents


def experiment_params(**kwargs):
    default_params = {
        "instances":1, 
        "episodes": 3000, 
        "steps":25,
        "clear_old_results":True,
        "rew_step_count":1,
        "track_disc_reward":False,
        "open_plot":True,
        "verbose":False,
        "reset_at_terminal":False,
        "cumulative_plot": False,
        "dir_for_plot":"results",
        "experiment_name_prefix":"",
        "track_success":False,
        "success_reward":None}
    default_params.update(kwargs)
    return default_params

if __name__=="__main__":
    from agents import RLangSMDPQAgent_PriorPolicy as RLangSMDPQAgent
    from agents import QLearningFactory
    from agents import SimpleRLAgent
    from agents import QLearningAgent
    from vocab import *
    
    lmdp = LMDP(four_room_mdp, factor_names=["x", "y"]) # mdp is given to bind factors

    # lmdp.add(position) # add position to lmdp symbols
    # room_1 = Symbol(bool_and(x <= half_width, y <= half_height), "room_1")
    # room_2 = Symbol(bool_and(x > half_width, y < half_height), "room_2")
    # room_3 = Symbol(bool_and(x < half_width, y > half_height), "room_3")
    # room_4 = Symbol(bool_and(x >= half_width, y > half_height-1), "room_4")
    # rooms = (room_1, room_2, room_3, room_4)
    
    # for r in rooms:
    #     lmdp.add(r) # add room symbols to lmdp

    # options to navigate to neighboring rooms
    
    # with lmdp.when(room_1) as c: 
    #     c.subpolicy(until=room_2, name='o-room1-room2')
    #     c.subpolicy(until=room_3, name='o-room1-room3')
    # with lmdp.when(room_2) as c: 
    #     c.subpolicy(until=room_1, name='o-room2-room1')
    #     c.subpolicy(until=room_4, name='o-room2-room4')
    # with lmdp.when(room_3) as c: 
    #     c.subpolicy(until=room_1, name='o-room3-room1')
    #     c.subpolicy(until=room_4, name='o-room3-room4')
    # with lmdp.when(room_4) as c: 
    #     c.subpolicy(until=room_2, name='o-room4-room2')
    #     c.subpolicy(until=room_3, name='o-room4-room3')

    # initial policy
    with lmdp.when(room_1) as c:
        c.execute(lmdp('o-room1-room2'))
    with lmdp.when(room_2) as c:
        c.execute(lmdp('o-room2-room4'))
    with lmdp.when(room_3) as c:
        c.execute(lmdp('o-room3-room4'))
        c.execute(lmdp('o-room3-room1'))
    with lmdp.when(room_4) as c:
        c.execute(lmdp('o-room4-room2'))

    ### Hierarchical Q-Learning
    # options = sorted([sp.to_option2() for sp in lmdp.get_subpolicies()], key=lambda o: o._id)
    # # inner_factory = LinearQLearningFactory(four_room_mdp.get_actions(), features, alpha=0.3, anneal=True, explore="uniform")
    # inner_factory = QLearningFactory(four_room_mdp.get_actions(), alpha=0.1, epsilon=0.2, anneal=True)
    # agent = IntraoptionQAgent(four_room_mdp.get_actions(), options, inner_factory, alpha=0.1, epsilon=0.1)
    # #Flat Q Learning
    # q_learning = QLearningAgent(four_room_mdp.get_actions(), alpha=0.1, epsilon=0.1, anneal=True)


    #### Run agents
    inner_factory = QLearningFactory(four_room_mdp.get_actions(), alpha=0.1, epsilon=0.1, anneal=True)
    rlang_agent = RLangSMDPQAgent(four_room_mdp.get_actions(), lmdp, inner_factory, anneal=True, epsilon=0.01, alpha=0.8)

    #Flat Q Learning
    flat_q_learning = QLearningAgent(four_room_mdp.get_actions(), alpha=0.1, epsilon=0.1, anneal=True, name="Flat-Q-Learning")

    run_agents([SimpleRLAgent(rlang_agent, rlang_agent.get_options(), name="RLang-Option-Q-Agent"), 
                flat_q_learning], 
                four_room_mdp, 
                experiment_params(instances=5, episodes=500, steps=200, cumulative_plot=True))