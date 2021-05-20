from vocab import *
from lmdp import *


def program():
    lmdp = LMDP()

    ### subpolicies
   
    with lmdp.when(any_state) as c:
        c.subpolicy(name='go_to_workshop_0',
                    until=at_workshop0)

    with lmdp.when(any_state) as c:
        c.subpolicy(name='go_to_workshop_1',
                    until=at_workshop1)
    
    with lmdp.when(any_state) as c:
        c.subpolicy(name='go_to_workshop_2',
                    until=at_workshop2)
    
    # with lmdp.when(any_state) as c:
    #     c.subpolicy(name='go_to_workshop_3',
    #                 until=at_workshop3)

    with lmdp.when(bool_and(wood >= 1, iron >= 1, at_workshop2)) as c:
        c.subpolicy(
                name='build_bridge',
                until= delta_bridge > 0
            )

    with lmdp.when(any_state) as c:
        c.subpolicy(
                name='get_iron',
                until= delta_iron > 0
            )
    
    with lmdp.when(any_state) as c:
        c.subpolicy(
                name='get_wood',
                until=delta_wood > 0
            )

    return lmdp


__all__ = ["program"]