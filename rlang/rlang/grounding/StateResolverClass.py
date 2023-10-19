from __future__ import annotations
from collections import defaultdict
from .groundings import Factor
from .utils.grounding_exceptions import RLangGroundingError

class StateResolver:
    """For reconstructing a state given partial information (e.g. a list of Factors)"""

    def __init__(self, info_dict: dict = None) -> None:
        self.state_guess = {}
        self.state_mask = defaultdict(lambda: False)
        if info_dict:
            self.add_info(info_dict)
    
    def add_info(self, info_dict: dict) -> None:
        """Add information to the state guess.
            Args:
                info_dict: A dictionary of {Factors: values} or {indices: values}
        """
        # TODO: Arjan, make a note of the places we'll need to come back to in the case that we have predictions instead of values.
        for key, value in info_dict.items():
            if isinstance(key, Factor):
                if len(key.indices) != len(value):
                    raise RLangGroundingError(f"Factor length and value length do not match, got {len(key.indices)} and {len(value)}")
                
                for index, index_value in enumerate(key.indices):
                    self.state_guess[key.indices[index]] = index_value
                    self.state_mask[key.indices[index]] = True

            elif isinstance(key, (list, tuple)):    # TODO: Implement this, Arjan. Write good error messages.
                for index in key:
                    self.state_guess[index] = value
                    self.state_mask[index] = 1
            else:
                raise ValueError("Invalid key type. Expected Factor or list/tuple of indices.")
