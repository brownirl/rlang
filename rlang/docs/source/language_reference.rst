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

An RLang program consists mainly of RLang object declarations.


Reserved Keywords
-----------------

.. code-block:: text

    S   # Current state
    A   # Current action
    S'  # Next state



RLang Object Definition Syntax
------------------------------

Factors
^^^^^^^

These represent portions of the state space. Can be defined using Python-like array slicing syntax on ``S``.

.. code-block:: text

    Factor x_position := S[1]
    Factor inventory := S[2:]


