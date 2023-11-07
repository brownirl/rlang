from __future__ import annotations
from collections import defaultdict
import numpy as np
from .utils.grounding_exceptions import RLangGroundingError

class StateResolver:
    """For reconstructing a state given partial information (e.g. a list of Factors)"""

    def __init__(self, info_dict: dict = None, state_type: object = np.ndarray) -> None:
        self.state_guess = {}
        self.state_mask = defaultdict(lambda: False)
        self.state_type = state_type
        if info_dict:
            self.add_info(info_dict)
    
    def add_info(self, info_dict: dict) -> None:
        """Add information to the state guess.
            Args:
                info_dict: A dictionary of {Factors: values} or {indices (tuple): values}
        """
        for key, value in info_dict.items():
            from .groundings import Factor
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
                raise RLangGroundingError(f"Invalid key type ({type(key)}) when trying to reconstruct state. Expected Factor or tuple of indices.")
    
    def get_state(self, default_value_for_unknown_indices: object = 0, state_length: int = None):
        """Get the reconstructed state
            Args:
                default_value_for_unknown_indices: The value to use for indices that are not in the state guess
            Returns:
                The reconstructed state
        """
        # If state_length is not provided, use the max index+1 in state_guess keys
        if not(state_length):
            state_length = max(self.state_guess.keys())+1

        if self.state_type == np.ndarray:
            # Construct a numpy array based on the state_guess
            reconstructed_state = np.full((state_length), default_value_for_unknown_indices)
            for index, value in self.state_guess.items():
                reconstructed_state[index] = value
            return reconstructed_state

        elif self.state_type == list:
            # Construct a list based on the state_guess
            reconstructed_state = [default_value_for_unknown_indices]*state_length
            for index, value in self.state_guess.items():
                reconstructed_state[index] = value
            return reconstructed_state
        
        else:
            raise RLangGroundingError(f"Invalid state type when trying to reconstruct state. Expected np.ndarray or list. Got {self.state_type}")

