******************
Working with RLang
******************

There are many ways RLang can be integrated into a project. The simplest involves using a pre-existing RLang-enabled
reinforcement learning agent that utilizes RLang information in a predefined manner. In this scenario, it is up to the
user to provide a written RLang program which can be parsed using :py:func:`.parse` or :py:func:`.parse_file` if the
program resides in a ``.rlang`` file.

It is also possible to write your own RLang-enabled agent that can utilize the information stored in an RLang program
(accessible via the :py:class:`.RLangKnowledge` class). This route requires a more thorough understanding of the RLang
Python :py:mod:`.groundings` module.

.. contents::


Using a Pre-built RLang Agent
=============================

An RLang project using a pre-built agent might have the following directory structure:

.. code-block:: text

   gridworld/
       main.py           \\ Python code for running the project
       gridworld.rlang   \\ RLang program containing world information
       vocab.json        \\ An optional (but useful) file that holds metadata and can reference additional groundings
       groundings.py     \\ An optional file that can store RLang grounding defined in Python

where ``main.py`` could be as simple as::

    from simple_rl.run_experiments import run_agents_on_mdp
    from simple_rl.agents import QLearningAgent

    import rlang
    from rlang.agents import RLangQLearningAgent

    mdp, states = create_mdp()
    agent = QLearningAgent(mdp.get_actions())     # Create a baseline Q-Learning agent

    knowledge = rlang.parse_file("gridworld.rlang")  # Parse RLang program into knowledge object
    rlang_agent = RLangQLearningAgent(mdp.get_actions(), states, knowledge) # Create RLang Q-Learning agent

    run_agents_on_mdp([agent, rlang_agent], mdp)  # Compare performance of agents on mdp


For help on how to write an RLang program, see :doc:`language_reference`.

Creating a Custom RLang Agent using :py:class:`.RLangKnowledge`
===============================================================

To get the most out of RLang, users should implement their own RLang-enabled reinforcement learning agents. Doing so
requires becoming familiar with RLang's :py:mod:`.groundings` module and most importantly the
:py:class:`.RLangKnowledge` object, which holds all RLang groundings parsed from an RLang program. See the source for
the :py:class:`.RLangQLearningAgent` for a good example on how to integrate RLang knowledge into an RL agent.

This section should perhaps discuss the knowledge object in more detail and provide examples.

Importing Python Groundings using a Vocabulary File
===================================================

Where should this section go? What file?

How does a vocabulary file work? How to import groundings



`Q Learning`_

.. _`Q Learning`: https://en.wikipedia.org/wiki/Q-learning