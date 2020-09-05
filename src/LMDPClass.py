'''

'''

from simple_rl.mdp.MDPClass import MDP
from collections import defaultdict
class LMDP:

    def __init__(self, mdp):
        self.__mdp = mdp
        self.__reward = lambda **args: None
        self.__transition = lambda **args : None
        self.__symbols = defaultdict(lambda: None)
        self.__policy = lambda **args: None
        self.__subpolicies = defaultdict(lambda: None)
        self.__actions = defaultdict(lambda: None)
        
    @property
    def reward(self):
        return self.__reward
    @property
    def transition(self):
        return self.__transition
    @property
    def policy(self):
        return self.__policy
   
    # ----- In case of unknown method for a more specialized MDP class
    
    def __getattr__(self, method_name):
        def method(*args, **kwargs):
            print("Handling unknown method: '{}'".format(method_name))
            return getattr(self.__mdp, method_name)(*args, **kwargs)
        return method

    # ----- Implementation the MDP interface
    def get_parameters(self):
        return self.__mdp.param_dict

    def get_init_state(self):
        return self.__mdp.init_state

    def get_curr_state(self):
        return self.__mdp.cur_state

    def get_actions(self):
        return self.__mdp.actions

    def get_gamma(self):
        return self.__mdp.gamma

    def get_reward_func(self):
        return self.__mdp.reward_func

    def get_transition_func(self):
        return self.__mdp.transition_func

    def get_num_state_feats(self):
        return self.__mdp.init_state.get_num_feats()

    def get_slip_prob(self):
        return self.__mdp.get_slip_prob()

    def get_name(self):
        return str(self.__mdp)

    # --------------
    # -- Mutators --
    # --------------

    def set_gamma(self, new_gamma):
        self.__mdp.set_gamma(new_gamma)

    def set_step_cost(self, new_step_cost):
        self.__mdp.set_step_cost(new_step_cost)

    def set_slip_prob(self, slip_prob):
        self.__mdp.set_slip_prob(slip_prob)

    def set_init_state(self, new_init_state):
        self.__mdp.set_init_state(new_init_state)

    # ----------
    # -- Core --
    # ----------

    def execute_agent_action(self, action):
        return self.__mdp.execute_agent_action(action)

    def reset(self):
        self.__mdp.reset()

    def end_of_instance(self):
        self.__mdp.end_of_instance()