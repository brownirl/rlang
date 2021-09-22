from rlang.src.grounding import *

"""These functions are used by the listener during the construction of Policy, Option, and Transition-type objects"""


def default_stat_collection(stats, *args, **kwargs):
    for stat in stats:
        stat_val = stat(*args, **kwargs)
        if stat_val is not None:
            return stat_val
    return None


def reward_stat_collection(stats, *args, **kwargs):
    val = 0
    for stat in stats:
        stat_val = stat(*args, **kwargs)
        if stat_val is not None:
            val += stat_val
    return val


def conditional_statement(if_condition, if_statements, elif_condition=None, elif_statements=None, else_statements=None, *args, **kwargs):
    # These '== True' are necessary, don't remove them.
    if if_condition(*args, **kwargs) == True:
        return if_statements(*args, **kwargs)
    elif elif_condition is not None and elif_condition(*args, **kwargs) == True:
        return elif_statements(*args, **kwargs)
    elif else_statements is not None:
        return else_statements(*args, **kwargs)
    else:
        return None


def build_conditional_stat(ctx, filter_object):
    if filter_object == RewardFunction:
        stat_collection = reward_stat_collection
    else:
        stat_collection = default_stat_collection

    if_condition = ctx.if_condition.value
    if_stats = list(
        filter(lambda x: isinstance(x, filter_object), ctx.if_statements))

    if_statements = lambda *args, **kwargs: stat_collection(if_stats, *args, **kwargs)
    elif_condition = None
    elif_statements = None
    else_statements = None

    if ctx.elif_condition is not None:
        elif_condition = ctx.elif_condition.value
        elif_stats = list(
            filter(lambda x: isinstance(x, filter_object), ctx.elif_statements))
        elif_statements = lambda *args, **kwargs: stat_collection(elif_stats, *args, **kwargs)

    if len(ctx.else_statements) > 0:
        else_stats = list(
            filter(lambda x: isinstance(x, filter_object), ctx.else_statements))
        else_statements = lambda *args, **kwargs: stat_collection(else_stats, *args, **kwargs)

    function = lambda *args, **kwargs: conditional_statement(
        if_condition, if_statements, elif_condition, elif_statements, else_statements, *args, **kwargs)
    return function
