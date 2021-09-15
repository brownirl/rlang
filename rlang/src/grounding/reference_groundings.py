from typing import Any
import numpy as np
from rlang.src.grounding import Domain, GroundingFunction


# TODO: I'm not sure these are needed. They may be used in tandem with internals.py objects
class Reference(GroundingFunction):
    def __init__(self, codomain: Domain, value: Any, name: str = None):
        if isinstance(value, (int, float, list)):
            value = np.array(value)
        self._value = value
        super().__init__(domain=Domain.ANY, codomain=codomain,
                         function=lambda *args, **kwargs: self._value, name=name)


class ActionReference(Reference):
    def __init__(self, action: Any, name: str = None):
        if isinstance(action, (int, float, list)):
            action = np.array(action)
        super().__init__(codomain=Domain.ACTION, value=action, name=name)
