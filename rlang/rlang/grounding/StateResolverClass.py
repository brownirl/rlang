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
    
    def add_info(self, info_dict: dict, no_regrets: bool = True, ignore_invalid_indices: bool = True) -> None:
        """Add information to the state guess.
            Args:
                info_dict: A dictionary of {Factors: values} or {indices (tuple): values}
                no_regrets: If True, the state guess will be updated with any indices retrieved from the input, regardless of any malformed inputs, which will be ignored. If False, the state guess will not be updated if there are any errors.
                ignore_invalid_indices: If True, indices that are negative or out of bounds will be ignored. If False, an error will be thrown if any indices are negative or out of bounds.
        """

        partial_state_guess = {}
        error_messages_from_bad_input = []

        for key, value in info_dict.items(): #Should we reset state_guess when an error is thrown?
            from .groundings import Factor
            if isinstance(key, Factor):
                if len(key.indices) != len(value): #Prediction object may not have length property?
                    error_messages_from_bad_input.append(f"Factor length and value length do not match when trying to reconstruct state, got {len(key.indices)} and {len(value)}")
                    continue
                
                for index_value, val in zip(key.indices, value):
                    partial_state_guess[index_value] = val # Prediction object will need some unwrapping

            elif isinstance(key, tuple):
                if len(key) != len(value):
                    error_messages_from_bad_input.append(f"Indices tuple length and value length do not match when trying to reconstruct state, got {len(key)} and {len(value)}")
                    continue
                
                for index_value, val in zip(key, value):
                    if index_value < 0:
                        error_messages_from_bad_input.append(f"Invalid index ({index_value}) when trying to reconstruct state. Index must be greater than or equal to 0.")
                        continue
                    partial_state_guess[index_value] = val

            elif isinstance(key, int):
                if key < 0:
                    error_messages_from_bad_input.append(f"Invalid index ({key}) when trying to reconstruct state. Index must be greater than or equal to 0.")
                    continue
                partial_state_guess[key] = value
            
            else:
                error_messages_from_bad_input.append(f"Invalid key type ({type(key)}) when trying to reconstruct state. Expected Factor or tuple of indices.")
                continue
        
        if no_regrets or len(error_messages_from_bad_input) == 0:
            # Merge partial_state_guess into state_guess
            self.state_guess.update(partial_state_guess)
        
        elif len(error_messages_from_bad_input) > 0 and not ignore_invalid_indices:
            raise RLangGroundingError("\n".join(error_messages_from_bad_input))
    
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

