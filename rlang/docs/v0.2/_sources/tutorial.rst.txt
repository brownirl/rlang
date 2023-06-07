***************
Getting Started
***************

RLang is a Domain-Specific Language for communicating domain knowledge to an RL agent. Using RLang, you can specify
information about policies, options, transition dynamics, and state factors and features. [*]_ Using the RLang Python
package, you can parse RLang programs into algorithm-agnostic Python objects. This page provides a quick tutorial on
getting set up with RLang and writing an RLang program.

.. figure:: RLang_AEC.svg
   :alt: RLange Agent-Environment Diagram

   The RLang pipeline


Installing RLang
----------------

RLang is *not* on PyPi yet. The repo is `on github`_.

Check the readme_ for the latest installation instructions, which might be the following:

.. _on github: https://github.com/brownirl/rlang/
.. _readme: https://github.com/brownirl/rlang/tree/master/rlang

.. code-block:: console

    $ brew install swig (on mac)
    $ python -m pip install rlang/rlang/dist/rlang-0.2.1-py3-none-any.whl

Full Example
------------

In this example, we'll take a look at how RLang can be used to provide domain knowledge about a gridworld environment
that can be used to speed up the learning of an RL agent. This example is pulled directly from the RLang package:

.. code-block:: text

   examples/gridworld/
       main.py           \\ Python code for running the project
       gridworld.rlang   \\ RLang program containing world information
       vocab.json        \\ Holds metadata and can reference additional groundings

The project files are included below:

.. raw:: html

   <details open="true">
   <summary><code class="docutils literal notranslate"><span class="pre">main.py</span></code></summary>
   <br />

.. literalinclude:: ../../rlang/examples/gridworld/main.py
   :linenos:

.. raw:: html

   </details>
   <br />

.. raw:: html

   <details open="true">
   <summary><code class="docutils literal notranslate"><span class="pre">gridworld.rlang</span></code></summary>
   <br />

.. literalinclude:: ../../rlang/examples/gridworld/gridworld.rlang
   :language: text
   :linenos:

.. raw:: html

   </details>
   <br />

.. raw:: html

   <details open="true">
   <summary><code class="docutils literal notranslate"><span class="pre">vocab.json</span></code></summary>
   <br />

.. literalinclude:: ../../rlang/examples/gridworld/vocab.json
   :language: json

.. raw:: html

   </details>
   <br />


.. [*] For a full list of groundings, see :doc:`language_reference`.