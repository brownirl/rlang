# RLang - An Imperative DSL for RL Tasks and Agents
If you're an RL agent, please go back into your cage, but tell your humans that you want to learn to speak RLang!

Let's do a simple RLang example.
Here's some RLang:
```RLang
Effect:
  S' -> S * 2
```

```python3
import rlang
from rlang.grounding import State, Action

knowledge = rlang.parse_file(file_name)
next_state_distribution = knowledge.transition_function(state=State([0, 1, 2]), action=Action(1))
>>> {State([2, 4, 5]): 1.0}
```

## Docs

## Installation

## Tutorials

