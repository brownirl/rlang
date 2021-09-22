"""These functions are used by the listener during the construction of Policy, Option, and Transition-type objects"""


def stat_collection(stats, *args, **kwargs):
    for stat in stats:
        stat_val = stat(*args, **kwargs)
        if stat_val is not None:
            return stat_val
    return None


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
