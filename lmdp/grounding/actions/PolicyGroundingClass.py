'''
    Policy Grounding Class
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: August 2020
'''
from lmdp.grounding.GroundingClass import Grounding

class PolicyGrounding(Grounding):

    def __init__(self, policy, name="policy"):
        self.policy_fun = policy
        Grounding.__init__(self, name=name)
    
    def __call__(self, *args):
        '''
            Args:
                -args[0] must be a state from the MDP
            return:
                - probabilities over the action space
        '''
        return self.policy_fun(args[0])
    
    def update_policy(self, function):
        self.policy_fun = function