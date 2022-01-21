************************
RLang Language Reference
************************

.. contents:: Table of Contents

Goals of this page:
 1. Describe the format of an RLang program
 2. Describe the different kinds of expressions (boolean and arithmetic expression) and statements (Execute, ->)
 3. Describe the reserved keywords (S, A, S')


Format of an RLang Program
==========================

An RLang program takes the following form:

.. productionlist::
   program: import* NEWLINE declaration*

It is an optional list of imports followed by an optional list of RLang object declarations. Users can import additional
RLang groundings from a vocabulary file.

RLang Syntax and Semantics
==========================

Special Variables
-----------------

``S``, ``A``, ``S'`` are reserved keywords referring to the current state, the current action, and the next state, respectively.
Depending on the type an RLang object, one or more of these keywords can be referenced in the definition of the object.

.. code-block:: text

    S   # Current state - Used in Factors and Features
    A   # Current action - Used in Effects
    S'  # Next state - Used most often in MarkovFeatures
