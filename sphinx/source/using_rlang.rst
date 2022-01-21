***********
Using RLang
***********

Goals of this section:
 1. To describe the various ways RLang can be used in a project:
  a. Using RLang and a pre-made agent
  b. Integrating RLang into a custom agent

RLang is a DSL for specifying world knowledge to reinforcement learning agents. It can be used in many different ways.


There are different ways to use RLang. You can use it and a pre-made RLang agent directly in your code or you can
integrate RLang in your own learning algorithm.


Using RLang and a Pre-built Agent
=================================


RLang provides a way of supplying grounded world knowledge to learning agents.

An RLang program should reside inside a ``.rlang`` file. Vocabulary files are in ``json`` format. Grounding files are Python ``.py`` files.

.. code-block:: text

   \dir


Integrating RLang into a custom agent
=====================================

In the case that you'd like to do something more interesting with the information that RLang supplies, you can integrate
RLang into a custom agent.