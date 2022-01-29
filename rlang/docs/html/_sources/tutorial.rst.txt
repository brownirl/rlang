***************
Getting Started
***************

RLang is a Domain-Specific Language for communicating domain knowledge to an RL agent. Using RLang, you can specify
information about policies, options, transition dynamics, and state factors and features. [*]_ Using the RLang Python
package, you can parse RLang programs into algorithm-agnostic Python objects. This page provides a quick tutorial on
getting set up with RLang and writing an RLang program.

Diagram of RLang and how it fits into Python here. Or rather, how it fits into the agent-environment cycle.

Installing RLang
----------------

Installation instructions here once uploaded to pypi.

.. code-block:: console

    $ pip install rlang

Gridworld Example
-----------------

In this tutorial, we'll look at an example using a gridworld environment. Here is the directory structure of the
example:

.. code-block:: text

   gridworld/
       main.py           \\ Python code for running the project
       gridworld.rlang   \\ RLang program containing world information
       vocab.json        \\ Holds metadata and can reference additional groundings

Here is ``main.py``:

.. literalinclude:: ../../rlang/examples/gridworld/main.py
   :linenos:

Here is ``gridworld.rlang``:

.. literalinclude:: ../../rlang/examples/gridworld/gridworld.rlang
   :language: text
   :linenos:

Here is ``vocab.json``:

.. literalinclude:: ../../rlang/examples/gridworld/vocab.json
   :language: json

.. [*] For a full list of groundings, see :doc:`language_reference`.