from vocab import *
from lmdp import *


def program():
    lmdp = LMDP()

    ### subpolicies
   
    # with lmdp.when(any_state) as c:
    #     c.subpolicy(name='go_to_workshop_0',
    #                 until=at_workshop0)

    # with lmdp.when(any_state) as c:
    #     c.subpolicy(name='go_to_workshop_1',
    #                 until=at_workshop1)
    
    with lmdp.when(any_state) as c:
        c.subpolicy(name='go_to_workshop_2',
                    until=at_workshop2)
    
    with lmdp.when(bool_and(wood >= 1, iron >= 1, at_workshop2)) as c:
        c.subpolicy(
                name='build_bridge',
                policy=use,
                until= delta_bridge > 0
            )

    with lmdp.when(there_is_iron) as c:
        c.subpolicy(
                name='get_iron',
                until= delta_iron > 0
            )
    
    with lmdp.when(there_is_wood) as c:
        c.subpolicy(
                name='get_wood',
                until=delta_wood > 0
            )
    with lmdp.when(bridge >= 1) as c:
        c.subpolicy(
                name='get_gold',
                until=delta_gold > 0
            )

    
    return lmdp

def program_ladder():
    lmdp = LMDP()
    with lmdp.when(any_state) as c:
        c.subpolicy(name='go_to_workshop_0',
                    until=at_workshop0)

    with lmdp.when(any_state) as c:
        c.subpolicy(name='go_to_workshop_1',
                    until=at_workshop1)
    
    with lmdp.when(any_state) as c:
        c.subpolicy(name='go_to_workshop_2',
                    until=at_workshop2)
    
    with lmdp.when(there_is_wood) as c:
        c.subpolicy(
                name='get_wood',
                until=delta_wood > 0
            )

    with lmdp.when(bool_and(wood >= 1, iron == 0, at_workshop1)) as c:
        c.subpolicy(
                name='build_stick',
                policy=use,
                until= delta_stick > 0
            )

    with lmdp.when(bool_and(wood >= 1, at_workshop0)) as c:
        c.subpolicy(
                name='build_plank',
                policy=use,
                until= delta_plank > 0
            )
    
    with lmdp.when(bool_and(stick >= 1, plank >=1 , at_workshop2)) as c:
        c.subpolicy(
                name='build_ladder',
                policy=use,
                until= delta_ladder > 0
            )
    return lmdp

__all__ = ["program"]