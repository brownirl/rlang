from typing import Any, List, Optional, Sequence, Tuple

import pfrl

from rlang.src.grounding import State, Action


class TestAgent(pfrl.agent.Agent):
    """
        Given a policy function, it creates an PFRL agent.
    """
    def __init__(self, policy):
        '''
            policy (rlang.grounding.PolicyGrounding)
        '''
        self._policy = policy

    def act(self, obs: Any) -> Any:
        """Select an action.
        Returns:
            ~object: action
        """ 

        return int(self._policy(obs))


    def observe(self, obs: Any, reward: float, done: bool, reset: bool) -> None:
        """Observe consequences of the last action.
        Returns:
            None
        """
        self._last_obs = (obs, reward, done, reset)

    def save(self, dirname: str) -> None:
        """Save internal states.
        Returns:
            None
        """
        pass

    def load(self, dirname: str) -> None:
        """Load internal states.
        Returns:
            None
        """
        pass

    def get_statistics(self) -> List[Tuple[str, Any]]:
        """Get statistics of the agent.
        Returns:
            List of two-item tuples. The first item in a tuple is a str that
            represents the name of item, while the second item is a value to be
            recorded.
            Example: [('average_loss', 0), ('average_value', 1), ...]
        """
        return []

