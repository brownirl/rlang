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
                info_dict: A dictionary of {Factors: values} or {indices (tuple): values}
        """
        for key, value in info_dict.items():
            if isinstance(key, Factor):
                if len(key.indices) != len(value): #Prediction object may not have length property?
                    raise RLangGroundingError(f"Factor length and value length do not match when trying to reconstruct state, got {len(key.indices)} and {len(value)}")
                
                for index_value, val in zip(key.indices, value):
                    self.state_guess[index_value] = val # Prediction object will need some unwrapping

            elif isinstance(key, tuple):
                if len(key) != len(value):
                    raise RLangGroundingError(f"Indices tuple length and value length do not match when trying to reconstruct state, got {len(key)} and {len(value)}")
                
                for index_value, val in zip(key, value):
                    self.state_guess[index_value] = val
            else:
                raise ValueError("Invalid key type when trying to reconstruct state. Expected Factor or tuple of indices.")
