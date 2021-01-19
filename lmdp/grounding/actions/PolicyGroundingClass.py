'''
    Policy Grounding Class
    author: Rafael Rodriguez-Sanchez (rrs@brown.edu)
    date: v0 August 2020
          v1 January 2021
'''
from lmdp.grounding.actions.ActionGroundingClass import ActionGrounding

class PolicyGrounding(ActionGrounding):

    def __init__(self, policy, name="policy"):
        self.policy_fun = policy
        ActionGrounding.__init__(self, self.policy_fun, policy)
        
    # def __call__(self, *args):
    #     '''
    #         Args:
    #             -args[0] must be a state from the MDP
    #         return:
    #             - probabilities over the action space
    #     '''
    #     return self.policy_fun(args[0])
    
    # def update_policy(self, function):
    #     self.policy_fun = function