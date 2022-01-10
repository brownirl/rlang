****************
Intro / Tutorial
****************

Flesh this out based on `Python Tutorial`_

.. _`Python Tutorial`: https://docs.python.org/3/tutorial/index.html

RLang is a Domain-Specific Language for specifying information to Decision-Making agents about MDPs and policies. Using
RLang, you can specify information about policies, options, transition dynamics, and features of state. The full list of
RLang objects can be seen here: :doc:`language_reference`

Diagram of RLang and how it fits into Python here. Or rather, how it fits into the agent-environment cycle.


In this tutorial, we'll first look at a toy elevator environment:

Elevator
--------

Let's imagine an agent is controlling an elevator. A typical environment


Let's look at a simple RLang Program that provides information regarding:

.. code-block:: text

    Action up := 1
    Action down := -1

    Factor floor := S[0]

    Effect elevator_movement_effect:
        if A == up:
            floor' -> floor + 1
        elif A == down:
            floor' -> floor - 1

    Effect main:
        -> elevator_movement_effect


