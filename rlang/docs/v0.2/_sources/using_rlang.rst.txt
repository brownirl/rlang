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


and ``gridworld.rlang`` could look like this:

.. code-block:: text

    import "vocab.json"

    Constant lava_locs := [[3, 2], [1, 4], [2, 4], [2, 5]]

    Factor position := S[0, 1]
    Factor x := position[0]
    Factor y := position[1]

    Proposition reached_goal := x == 5 and y == 1
    Proposition reached_wall := x == 3 and y == 1
    Proposition in_lava := position in lava_locs

    Effect main:
        if in_lava:
            Reward -1
        if reached_goal:
            Reward 1
        if reached_wall:
            S' -> S

For help on how to write an RLang program, see :doc:`language_reference`.

Using a Vocabulary File
-----------------------

While optional, vocabulary files allow for extremely powerful functionality. A minimal ``vocabulary.json`` file might
contain metadata on the MDP that's being interfaced with like the size of the state and action space:

.. code-block:: json

    {
      "domain": "gridworld",
      "mdp_metadata": {
        "state_space": {
          "size": 2,
          "dtype": "int"
        },
        "action_space": {
          "shape": 1,
          "dtype": "int"
        }
      }
    }

A more powerful vocabulary file can be used to reference additional RLang groundings declared inside an auxiliary
Python file. This vocabulary file includes two :py:mod:`.feature` groundings (``angle_target`` and ``hover_target``)
from an auxiliary module called ``grounding.py``:

.. raw:: html

   <details open="true">
   <summary>Example <code class="docutils literal notranslate"><span class="pre">vocab.json</span></code> with additional groundings</summary>
   <br />

.. code-block:: json

    {
      "domain": "lunarlander",
      "mdp_metadata": {
        "state_space": {
          "size": 8,
          "dtype": "float"
        },
        "action_space": {
          "shape": 1,
          "dtype": "int"
        }
      },
      "modules": [
        {
          "module_name": "grounding",
          "file_name": "examples/lunar_lander/grounding.py"
        }
      ],
      "vocabulary": {
        "features": [
          {
            "name": "angle_target",
            "grounding": "grounding.angle_target"
          },
          {
            "name": "hover_target",
            "grounding": "grounding.hover_target"
          }
        ]
      }
    }

.. raw:: html

   </details>
   <br />

.. raw:: html

   <details open="true">
   <summary>An accompanying grounding file <code class="docutils literal notranslate"><span class="pre">grounding.py</span></code></summary>
   <br />

.. code-block:: python

    from rlang.grounding import Feature

    def _angle_target(state):
        position = state[0:2]
        velocity = state[2:4]
        angle_targ = position[0] * 0.5 + velocity[0] * 1.0  # angle should point towards center
        if angle_targ > 0.4:
            angle_targ = 0.4  # more than 0.4 radians (22 degrees) is bad
        if angle_targ < -0.4:
            angle_targ = -0.4
        return angle_targ

    def _hover_target(state):
        position = state[0:2]
        hover_targ = 0.55 * abs(
            position[0]
        )
        return hover_targ


    angle_target = Feature(_angle_target)
    hover_target = Feature(_hover_target)

.. raw:: html

   </details>
   <br />

``angle_target`` and ``hover_target`` can now be referenced in an RLang program like any other grounding.

.. note:: It is possible to use more than one Python module to supply additional groundings

Creating a Custom RLang Agent using :py:class:`.RLangKnowledge`
===============================================================

To get the most out of RLang, users should implement their own RLang-enabled reinforcement learning agents. Doing so
requires becoming familiar with RLang's :py:mod:`.groundings` module and most importantly the
:py:class:`.RLangKnowledge` object, which holds all RLang groundings parsed from an RLang program.
:py:class:`.RLangQLearningAgent` is a good example on how to integrate RLang knowledge into an RL agent:

.. raw:: html

   <details open="true">
   <summary><code class="docutils literal notranslate"><span class="pre">RLangQLearningAgentClass.py</span></code></summary>
   <br />

.. literalinclude:: ../../rlang/rlang/agents/RLangQLearningAgentClass.py
   :linenos:

.. raw:: html

   </details>
   <br />

This section should perhaps discuss the knowledge object in more detail and provide examples.
