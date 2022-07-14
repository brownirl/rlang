import context
from rlang.grounding import Feature


def _angle_target(state):
    position = state[0:2]
    velocity = state[2:4]
    angle_targ = position[0] * 0.5 + velocity[0] * 1.0  # angle should point towards center
    if angle_targ > 0.4:
        angle_targ = 0.4  # more than 0.4 radians (22 degrees) is bad
    if angle_targ < -0.4:
        angle_targ = -0.4
    return angle_targ


def _hover_target(state):
    position = state[0:2]
    hover_targ = 0.55 * abs(
        position[0]
    )
    return hover_targ


angle_target = Feature(_angle_target)
hover_target = Feature(_hover_target)
