from rlang.src.grounding import *
from rlang.src.exceptions import RLangGroundingError

"""These functions are used by the listener during the construction of Policy, Option, and Transition-type objects"""


def policy_generator_function(statements):
    for stat in statements:
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


def default_stat_collection(stats, *args, **kwargs):
    possibilities = dict()
    for stat in stats:
        stat_val = stat(*args, **kwargs)
        if stat_val is not None:
            if isinstance(stat_val, dict):
                for k, v in stat_val.items():
                    # Add to dict or update existing entry
                    if k in possibilities:
                        possibilities[k] += v * stat.probability
                    else:
                        possibilities.update({k: v * stat.probability})
            else:
                # Add to dict or update existing entry
                if stat_val in possibilities:
                    possibilities[stat_val] = possibilities[stat_val] + stat.probability
                else:
                    possibilities.update({stat_val: stat.probability})

    return possibilities


def reward_stat_collection(stats, *args, **kwargs):
    val = 0
    for stat in stats:
        stat_val = stat(*args, **kwargs)
        if stat_val is not None:
            val += stat_val * stat.probability
    return val


def conditional_statement(if_condition, if_statements, elif_condition=None, elif_statements=None, else_statements=None,
                          *args, **kwargs):
    # These '== True' are necessary, don't remove them.
    if if_condition(*args, **kwargs) == True:
        return if_statements(*args, **kwargs)
    elif elif_condition is not None and elif_condition(*args, **kwargs) == True:
        return elif_statements(*args, **kwargs)
    elif else_statements is not None:
        return else_statements(*args, **kwargs)
    else:
        return None


def build_conditional_stat(ctx, filter_object, name_filter=lambda x: True):
    if filter_object == RewardFunction:
        stat_collection = reward_stat_collection
    else:
        stat_collection = default_stat_collection

    if_condition = ctx.if_condition.value
    if_stats = list(
        filter(lambda x: isinstance(x, filter_object) and name_filter(x), ctx.if_statements))

    if_statements = lambda *args, **kwargs: stat_collection(if_stats, *args, **kwargs)
    elif_condition = None
    elif_statements = None
    else_statements = None

    if ctx.elif_condition is not None:
        elif_condition = ctx.elif_condition.value
        elif_stats = list(
            filter(lambda x: isinstance(x, filter_object) and name_filter(x), ctx.elif_statements))
        # if len(elif_stats) == 0:
        #     pass
        elif_statements = lambda *args, **kwargs: stat_collection(elif_stats, *args, **kwargs)

    if len(ctx.else_statements) > 0:
        else_stats = list(
            filter(lambda x: isinstance(x, filter_object) and name_filter(x), ctx.else_statements))
        # if len(else_stats) == 0:
        #     pass
        else_statements = lambda *args, **kwargs: stat_collection(else_stats, *args, **kwargs)

    return lambda *args, **kwargs: conditional_statement(
        if_condition, if_statements, elif_condition, elif_statements, else_statements, *args, **kwargs)
