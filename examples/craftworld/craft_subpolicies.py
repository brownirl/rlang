from examples.craftworld.vocab import *
from lmdp import *


def program():
    lmdp = LMDP()

    ### subpolicies
    with lmdp.when(any_state) as c:
        c.subpolicy(name='go_to_workshop_1',
                    until=at_workshop_1)
    
    with lmdp.when(any_state) as c:
        c.subpolicy(name='go_to_workshop_2',
                    until=at_workshop_2)
    
    with lmdp.when(any_state) as c:
        c.subpolicy(name='go_to_workshop_3',
                    until=at_workshop_3)

    with lmdp.when(bool_and(wood >= 1, iron >= 1, at_workshop_2)) as c:
        c.subpolicy(name='build_bridge',
                    until=bool_and(bridge(S_prime)-bridge(S) >  0)
                )

    with lmdp.when(any_state) as c:
        c.subpolicy(name='get_iron',
                    until=bool_and(iron(S_prime)-iron(S) >  0)
                )
    
    with lmdp.when(any_state) as c:
        c.subpolicy(name='get_wood',
                    until=bool_and(wood(S_prime)-wood(S) >  0)
                )

    return lmdp


__all__ = ["program"]