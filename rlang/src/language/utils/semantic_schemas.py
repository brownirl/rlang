"""These functions are used by the listener during the construction of PolicyOld, Option, and Effect objects"""


def policy_generator_function(statements):
    for stat in statements:
        if len(stat) > 1:
            # This may need to change
            yield stat
        else:
            yield lambda s=stat, *args, **kwargs: s(*args, **kwargs)
            # yield lambda s=stat, *args, **kwargs: s(*args, **kwargs)


def conditional_policy_function(if_condition, if_subpolicy, elif_conditions=None, elif_subpolicies=None, else_subpolicy=None,
                                *args, **kwargs):
    if if_condition(*args, **kwargs) == True:
        return if_subpolicy(*args, **kwargs)
    else:
        for i in range(len(elif_conditions)):
            if elif_conditions[i](*args, **kwargs) == True:
                return elif_subpolicies[i](*args, **kwargs)
        if else_subpolicy is not None:
            return else_subpolicy(*args, **kwargs)


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
