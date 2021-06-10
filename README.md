# RLang v1 (In Progress)

## Getting Started

> **Requires** Python 3.7
- Create virtual environment (conda or venv)
- Activate environment and Pip install dependencies 
    ```pip install -r requirements.txt```
- Clone this [simple_rl](https://github.com/rafarodsa/simple_rl)) fork and pip-install it.
    ```pip install path/to/simple_rl/.```

## Directory structure

- envs: (custom) environments for examples
- examples: example RLang programs and RLang-informed agents. 
- experiments: experiments classes for handling RLang experiments (for paper)
- lmdp (probably to be renamed to rlang): contains all main classes for RLang parsing.
    - LMDPClass.py: contains LMDP (Language-informed MDP) that encapsulates all the information derived from an RLang program (**to refactor**)
    - agents: module containing rlang-informed agent implementations and supporting classes (**to refactor** and to move outside lmdp directory)
    - grounding: contains relevant modules to support expressions for RLang
    - utils: supporting classes and functions for __lmdp.grounding__