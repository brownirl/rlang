'''
    Policy Grounding Class:
     - Distribution over a discrete action space
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: August 2020
'''
from GroundingClass import Grounding

class PolicyGrounding(Grounding):

    def __init__(self, policy, name="policy"):
        self.__policy_fun = policy
        Grounding.__init__(self, name=name)
    
    def __call__(self, *args):
        '''
            Args:
                -args[0] must be a state from the MDP
            return:
                - probabilities over the action space
        '''
        return self.__policy_fun(args[0])