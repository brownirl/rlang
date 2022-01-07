************************
RLang Language Reference
************************

To be filled out. Based on this page on Python's documentation: `Python Language Reference`_

.. _`Python Language Reference`: https://docs.python.org/3/reference/index.html#reference-index

This reference describes the core syntax and semantics of RLang.

Much of RLang's syntax is similar to Python's.

Format of an RLang Program
--------------------------
.. productionlist::
   program: import* declaration*

An RLang program contains two optional components:

1. A series of import statements.
2. A series of RLang object declarations.

