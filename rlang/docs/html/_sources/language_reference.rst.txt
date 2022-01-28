************************
RLang Language Reference
************************

This page covers the core syntax and semantics of the RLang language.

.. contents::


Structure of an RLang Program
-----------------------------

An RLang program has the following structure:

.. productionlist::
   program: import* declaration*

where each import statement imports a local vocabulary file (e.g. ``import vocab.json``) and each declaration is the
instantiation of an RLang grounding:

.. productionlist::
   declaration: constant NL+
    : | action NL+
    : | factor NL+
    : | proposition NL+
    : | goal NL+
    : | feature NL+
    : | markov_feature NL+
    : | option
    : | policy
    : | effect


Syntax of RLang Groundings
--------------------------

Every RLang grounding is a function with a domain in :math:`\mathcal{S}\times\mathcal{A}\times\mathcal{S}`
and a co-domain in :math:`\mathcal{S}, \mathcal{A}, \mathbb{R}^n` where :math:`n\in \mathbb{N}`, or
:math:`\{\top, \bot\}`, depending on the grounding’s type. Each grounding declared in an RLang program grounds to one
or more Python RLang objects which are in the :py:mod:`.groundings` module and are accessible to the user after
parsing using the :py:class:`.RLangKnowledge` class.

.. Important:: Put a table here mapping groundings to their Python objects.

=====  =====  ======
   Inputs     Output
------------  ------
  A      B    A or B
=====  =====  ======
False  False  False
True   False  True
False  True   True
True   True   True
=====  =====  ======

.. Note:: Every RLang grounding declared in an program is static. Groundings cannot be re-bound.

Constants
^^^^^^^^^

.. productionlist::
   constant: "Constant" IDENTIFIER ":=" (arithmetic_exp | boolean_exp)

Constants can be defined and used later in other RLang groundings:

.. code-block:: text

    Constant lava_positions := [[0, 1], [5, 2]]
    Constant step_cost := -0.1

Constants ground to :py:class:`.ConstantGrounding`.

Factors
^^^^^^^

.. productionlist::
   factor: "Factor" IDENTIFIER ":=" any_bound_var

Factors are used to reference independent state variables.
They represent portions of the state space and can be defined using Python's slicing syntax ``[start?:end?]`` on the
current state variable ``S``:

.. code-block:: text

    Factor x_position := S[0]
    Factor y_position := S[1]
    Factor inventory := S[2:]

Factors ground to :py:class:`.Factor`.

Features
^^^^^^^^

.. productionlist::
   feature: "Feature" IDENTIFIER ":=" arithmetic_exp

Features are used to define more complex functions of state. They can be defined using arithmetic operations
(+, -, :math:`*`, /), numeric literals, function compositions.

.. code-block:: text

    Feature distance_to_gold := abs([0,4] - position)

Features ground to :py:class:`.Feature`.

Propositions
^^^^^^^^^^^^

.. productionlist::
   proposition: "Proposition" IDENTIFIER ":=" boolean_exp

Propositions are functions of the form :math:`\mathcal{S} \rightarrow \{\top, \bot\}`, generating a boolean value.
They can be defined using logical operators (``and``, ``or``, ``not``) and order relations of the real numbers
(<, <= , >, >=, =, !=)

.. code-block:: text

    Proposition at_workbench := position in workbench_locations
    Proposition have_bridge_material := iron >= 1 and wood >= 1

Propositions ground to :py:class:`.Proposition`.

Goals
^^^^^

.. productionlist::
   goal: "Goal" IDENTIFIER ":=" boolean_exp

Goals are used to specify goal states given by a proposition.

.. code-block:: text

    Goal get_gold := gold >= 1

Goals ground to :py:class:`.Goal`.


Markov Features
^^^^^^^^^^^^^^^

.. productionlist::
   markov_feature: "MarkovFeature" IDENTIFIER ":=" arithmetic_exp

Markov Features allow users to compute features on an (:math:`s,a,s'`) experience tuple and can be then used to define
partial specification of functions related to the task, such as action-value functions and transition functions.

The prime operator (``'``) can be used to reference the value of an RLang grounding on the next state.

.. code-block:: text

    Markov Feature inventory_change := inventory' - inventory

MarkovFeatures ground to :py:class:`.MarkovFeature`.

Policies
^^^^^^^^

.. productionlist::
    policy: "Policy" IDENTIFIER ":" INDENT policy_statement NL* DEDENT

Policies prompt the agent to perform an action/subpolicy in a given situation.
The keyword ``Execute`` is used to perform an action or call another policy. Policies can be specified in RLang using
conditional expressions using the keywords ``if``, ``elif``, and ``else``.


The following policy instructs the agent to craft iron tools at a workbench by first collecting iron and then
navigating to the workbench.

.. code-block:: text

    Policy main:
        if iron >= 2:
            if at_workbench:
                Execute Use # Use is an action
            else:
                Execute go_to_workbench # go_to_workbench is a policy
        else:
            Execute collect_iron

.. note:: Naming a policy ``main`` recognizes it as the main policy, which accessed from a :py:class:`.RLangKnowledge` object with ``knowledge.policy``. There can only be one `main` policy.


Policies can be made probabilistic using ``with P(float)``:

.. code-block:: text

    Policy random_move:
        with P(0.5):
            Execute up
        or with P(0.5):
            Execute down

    Policy random_move_syntax_sugar:
        Execute up with P(0.5)
        or Execute down with P(0.5)

Policies ground to :py:class:`.Policy`.

Options
^^^^^^^

.. productionlist::
    option: "Option" IDENTIFIER ":" INDENT "init" option_condition
          :  INDENT policy_statement NL* DEDENT
          :  "until" option_condition NL* DEDENT

Temporally-extended abstract actions can be specified using Options, which include initiation and termination
propositions. Initiation propositions are denoted using the keyword ``init``, and termination propositions are denoted
using ``until``:

.. code-block:: text

    Option build_bridge:
        init have_bridge_material and at_workbench
            Execute craft_bridge
        until bridge in inventory

.. note:: ``Any`` can also be specified in place of both the ``init`` and ``until`` propositions and functions the same as ``True``.

Options ground to :py:class:`.Option`.

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

.. productionlist::
    effect: "Effect" IDENTIFIER ":" INDENT effect_statement* DEDENT
    effect_statement: reward | prediction | effect_reference


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

Effects ground to :py:class:`.Effect`, which holds a :py:class:`.TransitionFunction`, a :py:class:`.RewardFunction`,
and a list of :py:class:`.Prediction`.

Expressions and Keywords
------------------------

Arithmetic Expressions
^^^^^^^^^^^^^^^^^^^^^^

Arithmetic expressions are the most common expression used in defining RLang groundings.

.. productionlist::
   arithmetic_exp: L_PAR arithmetic_exp R_PAR
    : | arithmetic_exp (TIMES | DIVIDE) arithmetic_exp
    : | arithmetic_exp (PLUS | MINUS) arithmetic_exp
    : | any_number
    : | any_array
    : | any_bound_var

Some examples of arithmetic expressions:

.. code-block:: text

   some text here

Boolean Expressions
^^^^^^^^^^^^^^^^^^^

Boolean expressions are also commonly used in Propositions, Goals, Effects, Options, and Policies.

.. productionlist::
   boolean_exp: L_PAR boolean_exp R_PAR
    : | boolean_exp AND boolean_exp
    : | boolean_exp OR boolean_exp
    : | NOT boolean_exp
    : | arithmetic_exp IN arithmetic_exp
    : | boolean_exp (EQ_TO | NOT_EQ) boolean_exp
    : | arithmetic_exp (EQ_TO | LT | GT |
    :    LT_EQ | GT_EQ | NOT_EQ) arithmetic_exp
    : | any_bound_var
    : | (TRUE | FALSE)

Some examples of boolean expressions:

.. code-block:: text

   some text here

Conditional Expressions
^^^^^^^^^^^^^^^^^^^^^^^

The statements usable in a conditional expression differ between Policies and Effects.

.. productionlist::
   conditional_exp: IF boolean_exp COL INDENT statement NL* DEDENT
   : (ELIF boolean_exp COL INDENT statement NL* DEDENT)*
   : (ELSE COL INDENT statement NL* DEDENT)?;

Some examples of conditional expressions:

.. code-block:: text

   some text here

Probabilistic Expressions
^^^^^^^^^^^^^^^^^^^^^^^^^


Special Variables
^^^^^^^^^^^^^^^^^

``S``, ``A``, ``S'`` are reserved keywords referring to the current state, the current action, and the next state, respectively.
Depending on the type an RLang object, one or more of these keywords can be referenced in the definition of the object.

.. code-block:: text

    S   # Current state - Used in Factors and Features
    A   # Current action - Used in Effects
    S'  # Next state - Used most often in MarkovFeatures