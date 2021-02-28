import sys, time
from simple_rl.experiments import Experiment
from collections import defaultdict

def experiment_params():
    return {"instances":3, 
            "episodes": 100, 
            "steps":100,
            "clear_old_results":True,
            "rew_step_count":1,
            "track_disc_reward":False,
            "open_plot":True,
            "verbose":False,
            "reset_at_terminal":False,
            "cumulative_plot":False,
            "dir_for_plot":"results",
            "experiment_name_prefix":"",
            "track_success":False,
            "success_reward":None}


def _make_step_progress_bar():
    '''
    Summary:
        Prints a step progress bar for experiments.
    Returns:
        (int): Length of the progress bar (in characters).
    '''
    progress_bar_width = 20
    sys.stdout.write("\t\t[%s]" % (" " * progress_bar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (progress_bar_width+1)) # return to start of line, after '['
    return progress_bar_width

def _increment_bar():
    sys.stdout.write("-")
    sys.stdout.flush()


def run_single_agent_on_mdp(agent, mdp, episodes, steps, experiment=None,
                            verbose=False, track_disc_reward=False,
                            reset_at_terminal=False,
                            resample_at_terminal=False):
    '''
    Summary:
        Main loop of a single MDP experiment.
    Returns:
        (tuple): (bool:reached terminal, int: num steps taken, list: cumulative discounted reward per episode)
    '''
    if reset_at_terminal and resample_at_terminal:
        raise ValueError("(simple_rl) ExperimentError: Can't have \
        reset_at_terminal and resample_at_terminal set to True.")

    value_per_episode = [0] * episodes
    gamma = mdp.get_gamma()

    # For each episode.
    for episode in range(1, episodes + 1):

        cumulative_episodic_reward = 0

        if verbose:
            # Print episode numbers out nicely.
            sys.stdout.write("\tEpisode %s of %s" % (episode, episodes))
            sys.stdout.write("\b" * len("\tEpisode %s of %s" % (episode,
                                                                episodes)))
            sys.stdout.flush()

        # Compute initial state/reward.
        state = mdp.get_init_state()
        reward = 0
        episode_start_time = time.clock()

        # Extra printing if verbose.
        if verbose:
            print()
            sys.stdout.flush()
            prog_bar_len = _make_step_progress_bar()

        for step in range(1, steps + 1):
            if verbose and int(prog_bar_len*float(step) / steps) > int(
                    prog_bar_len*float(step-1) / steps):
                _increment_bar()

            # step time
            step_start = time.clock()

            # Compute the agent's policy.
            
            action = agent.act(state, reward)
            # Terminal check.
            if state.is_terminal():

                if verbose:
                    sys.stdout.write("x")

                if episodes == 1 and not reset_at_terminal and experiment \
                        is not None and action != "terminate":
                    # Self loop if we're not episodic or resetting and in a terminal state.
                    experiment.add_experience(agent, state, action, 0, state,
                                              time_taken=time.clock()-step_start)
                    continue
                break

            # Execute in MDP.
            reward, next_state = mdp.execute_agent_action(action)
            # print("@r: reward, next state", reward, next_state)

            # Track value.
            value_per_episode[episode - 1] += reward * gamma ** step
            cumulative_episodic_reward += reward

            # Record the experience.
            if experiment is not None:
                reward_to_track = mdp.get_gamma()**(
                        step + 1 + episode*steps) * reward if \
                    track_disc_reward else reward
                reward_to_track = round(reward_to_track, 5)
                experiment.add_experience(agent, state, action,
                                          reward_to_track, next_state,
                                          time_taken=time.clock() - step_start)

            if next_state.is_terminal():
                if reset_at_terminal:
                    # Reset the MDP.
                    next_state = mdp.get_init_state()
                    mdp.reset()
                elif resample_at_terminal and step < steps:
                    mdp.reset()
                    return True, step, value_per_episode

            # Update pointer.
            state = next_state

        # Process experiment info at end of episode.
        if experiment is not None:
            experiment.end_of_episode(agent)
            print

        # Reset the MDP, tell the agent the episode is over.
        mdp.reset()
        agent.end_of_episode()

        if verbose:
            print("\n")

    # Process that learning instance's info at end of learning.
    if experiment is not None:
        experiment.end_of_instance(agent)

    # Only print if our experiment isn't trivially short.
    if verbose:
        print("\tLast episode reward:", cumulative_episodic_reward)

    return False, steps, value_per_episode
    
def run_agents(agents, mdp, exp_params=None):
    exp_params = experiment_params() if exp_params is None else exp_params
    params = {"instances": exp_params["instances"],
              "episodes": exp_params["episodes"],
              "steps": exp_params["steps"]}

    experiment = Experiment(
        agents=agents,
        mdp=mdp,
        params=params,
        is_episodic= exp_params["episodes"] > 1,
        clear_old_results=exp_params["clear_old_results"],
        track_disc_reward=exp_params["track_disc_reward"],
        count_r_per_n_timestep=exp_params["rew_step_count"],
        cumulative_plot=exp_params["cumulative_plot"],
        dir_for_plot=exp_params["dir_for_plot"],
        experiment_name_prefix=exp_params["experiment_name_prefix"],
        track_success=exp_params["track_success"],
        success_reward=exp_params["success_reward"])

    time_dict = defaultdict(float)
    instances = exp_params["instances"]
    for agent in agents:
        print(str(agent) + " is learning.")

        times = defaultdict(float)
        for instance in range(1, instances + 1):
            start = time.clock()
            print("  Instance " + str(instance) + " of " + str(instances) + ".")
            sys.stdout.flush()
            run_single_agent_on_mdp(
                agent, mdp,
                episodes=exp_params["episodes"],
                steps=exp_params["steps"],
                experiment=experiment, verbose=exp_params["verbose"],
                track_disc_reward=exp_params["track_disc_reward"],
                reset_at_terminal=True)
            if "fixed" in agent.name:
                break

            # Reset the agent.
            agent.reset()
            mdp.end_of_instance()
            end = time.clock()
            times[instance] = end-start
            print(f"{instance}: {times[instance]}")

        
    print("\n--- TIMES ---")
    for agent in time_dict.keys():
        print(str(agent) + " agent took " + str(round(time_dict[agent], 2)) \
              + " seconds.")
    print("-------------\n")

    ### make experiment plots
    experiment.make_plots(open_plot=exp_params["open_plot"])