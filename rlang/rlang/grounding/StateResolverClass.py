from __future__ import annotations
from collections import defaultdict
import numpy as np
from .groundings import Factor
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
    
    def get_state(self, default_value_for_unknown_indices: object = 0, state_length: int = None):
        """Get the reconstructed state
            Args:
                default_value_for_unknown_indices: The value to use for indices that are not in the state guess
            Returns:
                The reconstructed state
        """
        #Not really sure how to get the correct state_length, maybe this is correct(?)
        if not(state_length):
            min_index = 0
            max_index = 0
            for key in self.state_guess:
                max_index = max(max_index, max(key))
                min_index = min(min_index, min(key))
            state_length = max_index-min_index+1

        if self.state_type == np.ndarray:
            # Construct a numpy array based on the state_guess
            reconstructed_state = np.full((state_length), default_value_for_unknown_indices)
            for index, value in self.state_guess.items():
                reconstructed_state[index] = value
            return reconstructed_state

        elif self.state_type == list:
            # Construct a list based on the state_guess using self.statetype to instantiate
            reconstructed_state = [default_value_for_unknown_indices]*state_length
            for index, value in self.state_guess.items():
                reconstructed_state[index] = value
            return reconstructed_state
        else:
            raise ValueError("Invalid state type when trying to reconstruct state. Expected np.ndarray or list.")

