************************
RLang Language Reference
************************

To be filled out. Based on this page on Python's documentation: `Python Language Reference`_

.. _`Python Language Reference`: https://docs.python.org/3/reference/index.html#reference-index

This reference describes the core syntax and semantics of RLang.


Format of an RLang Program
--------------------------
.. productionlist::
   program: import* declaration*

Reserved Keywords
-----------------

An RLang program consists of a set of object declarations, 
where each object grounds to one or more elements of an :math:`(\mathcal{S}, \mathcal{A}, O, R, T, \pi)` tuple.  
More specifically, every RLang object is a function with a domain in :math:`\mathcal{S}\times\mathcal{A}\times\mathcal{S}`
and a co-domain in :math:`\mathcal{S}, \mathcal{A}, \mathbb{R}^n` where :math:`n\in \mathbb{N}`, or :math:`\{\top, \bot\}` dependingon the object’s type.


``S``, ``A``, ``S'`` are reserved keywords referring to the current state, current action and the next state, respectively.

.. code-block:: text

    S   # Current state
    A   # Current action
    S'  # Next state



RLang Object Definition Syntax
------------------------------

Factors
^^^^^^^

Factors are used to reference independent state variables. 
They represent portions of the state space and can be defined using the slicing syntax ``[start:end]`` on ``S``.

.. code-block:: text

    Factor x_position := S[1]
    Factor inventory := S[2:]


Features
^^^^^^^^

Features are used to define more complex functions of state. They can be derived using arithmetic operations (+, -, :math:`*`, /), numeric literals, function compositions.

.. code-block:: text

    Feature distance_to_gold := abs([0,4] - position)


Propositions
^^^^^^^^^^^^

Propositions are functions of the form :math:`\mathcal{S} \rightarrow \{\top, \bot\}`, generating a boolean value.
They can be defined using logical operators (``and``, ``or``, ``not``) and order relations of the real numbers (<, <= , >, >=, =, !=)

.. code-block:: text

    Constant workbench_locations := [[1, 0], [1, 3]]
    Proposition at_workbench := position in workbench_locations
    Proposition have_bridge_material := iron >= 1 and wood >= 1


Goals
^^^^^

Goals are used to specify goal states given by a proposition.

.. code-block:: text

    Goal get_gold := gold >= 1


Markov Features
^^^^^^^^^^^^^^^

Markov Features allow users to compute features on an (:math:`s,a,s'`) experience tuple
and can be then used to define partial specification of functions related to the task, such as action-value functions and transition functions.
**Note:** the prime operator (``'``) can be used to reference the valueof an RLang object on the next state.

.. code-block:: text

    Markov Feature inventory_change := inventory' -inventory


Policies
^^^^^^^^

Policies prompt the agent to perform an action/subpolicy in a given situation.
The keyword ``Execute`` is used to perform an action or call another policy and 
*provides a prior probability for the action to be executed*.

Policies can be specified in RLang using conditional or probabilistic expressions.
Conditional expressions are written using the keywords ``if`` and ``else``, and 
probability expressions can be written using the keywords ``with P(float)`` and ``or`` to specify probability values.


The following policy instructs the agent to craft iron tools at a workbench by first collecting ironand then navigating to the workbench.

.. code-block:: text

    Policy main:
    if iron >= 2:
        if at_workbench:
            Execute Use # Use is an action
        else:
            Execute go_to_workbench # go_to_workbench is a policy
    else:
        Execute collect_iron
    

Here is an example of a probabilistic policy. *Note that for the probabilities to be correct their sum must be equal to
1.*

.. code-block:: text

    Policy random_move:
        Execute up with P(0.25)
        or Execute down with P(0.25)
        or Execute left with P(0.25)
        or Execute right with P(0.25)
    

Options
^^^^^^^

Temporally-extended abstract actions can be specified using Options, which include initiation and termination propositions.
Initiation propositions are defined using the keyword ``init``, and termination propositions are written using the keyword ``until``.

.. code-block:: text

    Option build_bridge:
    init have_bridge_material and at_workbench
        Execute craft_bridge
    until bridge in inventory


Action Restrictions
^^^^^^^^^^^^^^^^^^^

Action Restrictions are used to specify constraints on the set of possible actions an agent can take in a given circumstance.
The keyword ``Restrict`` removes an action from consideration in the given situation, *meaning that the action will have
probability zero even after learning.*

.. code-block:: text

    ActionRestriction dont_get_burned:
        if (position + [0, 1]) in lava_locations:
            Restrict up


Effects
^^^^^^^

Effects provide an interface for specifying partial information about the transition and reward functions,
allowing users to denote the consequences of an action when performed in a given state.

The following effect captures the predicted consequence of moving left on the ``x_position`` factor, 
stating that the ``x_position`` of the agent in the next state will be less than in the current state.
This Effect also specifies a -0.1 step penalty regardless of the current state or action.

.. code-block:: text

    Effect movement_effect:
        if x_position >= 1 and A == left:
            x_position' -> x_position - 1
        Reward -0.1

When using a factored MDP, Effects can also be used to specify factored transition functions, 
i.e. transition functions for individual factors, which we call **predictions**:

Here is a prediction made about the full transition function:

.. code-block:: text

    Effect tic_tac_toe:
        if three_in_a_row:
            S' -> empty_board # Board is reset
