import numpy as np
import rlang
from rlang.src.grounding import *


def test_Factor():
    metadata = rlang.metadata_from_state(np.zeros(5))
    state = State(np.array([4, 5, 6, 7, 8]))

    position_parsed = rlang.parse("Factor position := S", metadata)['position']
    position = Factor([0, 1, 2, 3, 4], "position")
    assert position(state=state) == position_parsed(state=state)

    position_parsed = rlang.parse("Factor position := S[0]", metadata)['position']
    position = Factor(0, "position")
    assert position(state=state) == position_parsed(state=state)

    position_parsed = rlang.parse("Factor position := S[0:3]", metadata)['position']
    position = Factor([0, 1, 2], "position")
    assert position(state=state) == position_parsed(state=state)

    position_parsed = rlang.parse("Factor position := S[:3]", metadata)['position']
    assert position(state=state) == position_parsed(state=state)

    position_parsed = rlang.parse("Factor position := S[0, 3, 1]", metadata)['position']
    position = Factor([0, 3, 1], "position")
    assert position(state=state) == position_parsed(state=state)


def test_Feature():
    metadata = rlang.metadata_from_state(np.zeros(5))
    state = State(np.array([4, 5, 6, 7, 8]))

    x_parsed = rlang.parse("Feature x := S[0, 1]", metadata)['x']
    x = Feature.from_Factor(Factor([0, 1]), "x")
    assert x(state=state) == x_parsed(state=state)

    x_parsed = rlang.parse("Factor position := S[0, 1]\nFeature x := position[0]", metadata)['x']
    position = Factor([0, 1], "position")
    x = Feature.from_Factor(position[0], "x")
    assert x(state=state) == x_parsed(state=state)
    #
    # x_parsed = rlang.parse("Factor position := S[0, 1]\nFeature x := position * 2", metadata)['x']
    # position = Factor([0, 1], "position")
    # x = Feature.from_Factor(position[0] * 2, "x")
    # assert x(state=state) == x_parsed(state=state)
    #
    # x_parsed = rlang.parse("Factor position := S[0, 1]\nFeature x := position[0] + 4 * 2 + position[1]", metadata)['x']
    # position = Factor([0, 1], "position")
    # x = Feature(position[0] + 4 * 2 + position[1], "x")
    # assert x(state=state) == x_parsed(state=state)


# def test_Predicate():
#     hi_parsed = listener_from_input("Factor position := S[0, 1]\nFeature x := position[0]\nPredicate hi := x == 1 and True or False").new_vars['hi']
#     position = StateFactor([0, 1], "position")
#     x = StateFeature(position[0], 1)
#     hi = Predicate(x == 1 and BOOL_TRUE.or_(BOOL_FALSE))
#     assert hi_parsed == hi
#     assert hi_parsed(np.array([0, 1, 2])) == hi(np.array([0, 1, 2]))
#

if __name__ == "__main__":
    test_Feature()
