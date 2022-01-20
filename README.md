# RLang v1 (In Progress)

## Getting Started

> **Requires** Python 3.7
- Create virtual environment (conda or venv)
- Activate environment and Pip install dependencies 
    ```pip install -r requirements.txt```
- Clone this [simple_rl](https://github.com/rafarodsa/simple_rl)) fork and pip-install it.
    ```pip install path/to/simple_rl/.```

## Directory structure

- `envs/`: (custom) environments for examples
- `examples/`: example RLang programs and RLang-informed agents. 
- `experiments/`: experiments classes for handling RLang experiments (for paper)
- `rlang/`: contains grounding and language packages.
  - `src/`: contains the source code for RLang
    - `api_functions.py`: contains the primary functions a user would use.
    - `language/`: contains the python files for lexing/parsing/listening. Most of these files are generated by Antlr4.
    - `grounding/`: contains all the RLang groundings.
  - `docs/`
  - `tests/`
    
    
## Building the Lexer and Parser with Antlr4

- Run `mvn compile` from the root directory to run Antlr4.
- Clean with `mvn clean`, though it should do it automatically in each build cycle.
- Run tests with `mvn test`.
- Check out `antlr/README.md` and `antlr/pom.xml` for more info on grammar development.

## Building the documentation with Sphinx

- You can easily generate html files by running `make clean` and `make html` from `sphinx/`
- If you add or remove a module, run `export SPHINX_APIDOC_OPTIONS=members,show-inheritance`, then `sphinx-apidoc -t templates/ -o source/ ../rlang/rlang ../rlang/rlang/language` from `sphinx/` (and then run `rst2myst convert **/*.rst` to convert to markdown (actually don't do this)).
