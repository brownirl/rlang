"""These functions are used by the listener during the construction of Policy, Option, and Transition-type objects"""


def policy_stat_collection(policy_stats, *args, **kwargs):
    for policy_stat in policy_stats:
        if policy_stat(*args, **kwargs) is not None:
            return policy_stat(*args, **kwargs)
    return None


def conditional_policy_statement(if_condition, if_statements, elif_condition=None, elif_statements=None, else_statements=None, *args, **kwargs):
    # These '== True' are necessary, don't remove them.
    if if_condition(*args, **kwargs) == True:
        return if_statements(*args, **kwargs)
    elif elif_condition is not None and elif_condition(*args, **kwargs) == True:
        return elif_statements(*args, **kwargs)
    elif else_statements is not None:
        return else_statements(*args, **kwargs)
    else:
        return None
