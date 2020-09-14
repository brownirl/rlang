'''
    Policy function based on Dictionary

    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: September 2020
'''

from collections.abc import Iterable
class PolicyFromDict:

    def __init__(self, policy=[]):
        '''
            policy: list of tuples (symbol, action) or dict symbol->action
        '''
        if (isinstance(policy, Iterable)):
            self.__policy = dict(policy)
        elif (isinstance(policy, dict)):
            self.__policy = policy
        else:
            raise "Argument must be dict Symbol->Action or list of tuples (symbol, action)"
    
    def __call__(self, state):
        '''
            Args: state (MDP state)
            Returns the actions corresponding to symbols the state belongs to
        '''
        actions = []
        for s in [symbol for symbol in self.__policy.keys() if symbol(state)]:
            actions.append(self.__policy[s])
        return actions

    def add(self, symbol, action):
        '''
            updates the action of a symbol. 
            It adds it if the symbol is in the dict
        '''

        self.__policy[symbol] = action