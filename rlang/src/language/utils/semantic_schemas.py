"""These functions are used by the listener during the construction of Policy, Option, and Effect objects"""
from grounding import PolicyComplete


def policy_generator_function(statements):
    for stat in statements:
        # print(stat)
        if len(stat) > 1:
            # TODO: This may need to change
            # for s in stat:
            #     print("dd")
            #     yield lambda *args, **kwargs: s(*args, **kwargs)
            yield stat
            # def unwrap_policy_generator(policy, *args, **kwargs):
            #     to_yield = policy(*args, **kwargs)
            #     while not isinstance(to_yield, PolicyComplete):
            #         yield to_yield
            #         to_yield = policy(*args, **kwargs)
            # yield lambda s=stat, *args, **kwargs: unwrap_policy_generator(s, *args, **kwargs)
            # try
            # print(stat)
            # to_yield = lambda s=stat, *args, **kwargs: s(*args, **kwargs)
            # print(to_yield)
            # while not isinstance(to_yield, PolicyComplete):
            #     to_yield
        else:
            yield lambda s=stat, *args, **kwargs: s(*args, **kwargs)


def conditional_policy_function(if_condition, if_subpolicy, elif_conditions=None, elif_subpolicies=None, else_subpolicy=None,
                                *args, **kwargs):
    if if_condition(*args, **kwargs) == True:
        if len(if_subpolicy) == 1:
            return {list(if_subpolicy(*args, **kwargs).keys())[0]: 1.0}
        else:
            return {if_subpolicy: 1.0}
    else:
        for i in range(len(elif_conditions)):
            if elif_conditions[i](*args, **kwargs) == True:
                if len(elif_subpolicies[i]) == 1:
                    return {list(elif_subpolicies[i](*args, **kwargs).keys())[0]: 1.0}
                else:
                    return {elif_subpolicies[i]: 1.0}
        if else_subpolicy is not None:
            if len(else_subpolicy) == 1:
                return {list(else_subpolicy(*args, **kwargs).keys())[0]: 1.0}
            else:
                return {else_subpolicy: 1.0}
        else:
            return 'no_action'


def subpolicy_dict_function(subpolicies, *args, **kwargs):
    subpolicy_dict = dict()
    for sp in subpolicies:
        if len(sp) == 1:
            subpolicy_dict.update({list(sp(*args, **kwargs).keys())[0]: sp.probability})
        else:
            subpolicy_dict.update({sp: sp.probability})
    return subpolicy_dict


def effect_transition_dict_function(transitions, *args, **kwargs):
    transition_dict = dict()
    for sp in transitions:
        for k, v in sp(*args, **kwargs).items():
            if k in transition_dict:
                transition_dict.update({k: transition_dict[k] + v * sp.probability})
            else:
                transition_dict.update({k: v * sp.probability})
    return transition_dict


def conditional_reward_function(if_condition, if_reward, elif_conditions=None, elif_rewards=None, else_reward=None,
                                *args, **kwargs):
    if if_condition(*args, **kwargs) == True:
        return if_reward(*args, **kwargs)
    else:
        for i in range(len(elif_conditions)):
            if elif_conditions[i](*args, **kwargs) == True:
                return elif_rewards[i](*args, **kwargs)
        if else_reward is not None:
            return else_reward(*args, **kwargs)
        else:
            return None


def conditional_transition_function(if_condition, if_transition, elif_conditions=None, elif_transitions=None,
                                    else_transition=None, *args, **kwargs):
    if if_condition(*args, **kwargs) == True:
        return if_transition(*args, **kwargs)
    else:
        for i in range(len(elif_conditions)):
            if elif_conditions[i](*args, **kwargs) == True:
                return elif_transitions[i](*args, **kwargs)
        if else_transition is not None:
            return else_transition(*args, **kwargs)
        else:
            return None


def conditional_prediction_function(if_condition, if_prediction, elif_conditions=None, elif_predictions=None,
                                    else_prediction=None, *args, **kwargs):
    if if_condition(*args, **kwargs) == True:
        if if_prediction:
            return if_prediction(*args, **kwargs)
        else:
            return None
    else:
        for i in range(len(elif_conditions)):
            if elif_conditions[i](*args, **kwargs) == True:
                if elif_predictions[i]:
                    return elif_predictions[i](*args, **kwargs)
                else:
                    return None
        if else_prediction:
            return else_prediction(*args, **kwargs)
        else:
            return None
