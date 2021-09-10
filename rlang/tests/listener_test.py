import numpy as np
import rlang
from rlang.src.grounding import *


def test_Factor():
    metadata = MDPMetadata.from_state_action(np.zeros(5), np.zeros(5))
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
    metadata = MDPMetadata.from_state_action(np.zeros(5), np.zeros(5))
    state = State(np.array([4, 5, 6, 7, 8]))

    x_parsed = rlang.parse("Feature x := S[0, 1]", metadata)['x']
    x = Feature.from_Factor(Factor([0, 1]), "x")
    assert x(state=state) == x_parsed(state=state)

    x_parsed = rlang.parse("Factor position := S[0, 1]\nFeature x := position[0]", metadata)['x']
    position = Factor([0, 1], "position")
    x = Feature.from_Factor(position[0], "x")
    assert x(state=state) == x_parsed(state=state)

    x_parsed = rlang.parse("Factor position := S[0, 1]\nFeature x := position * 2", metadata)['x']
    position = Factor([0, 1], "position")
    x = Feature.from_Factor(position * 2, "x")
    assert x(state=state) == x_parsed(state=state)
    x = Feature.from_Factor(2 * position, "x")
    assert x(state=state) == x_parsed(state=state)

    x_parsed = rlang.parse("Factor position := S[0, 1]\nFeature x := position[0] + 4 * 2 + position[1]", metadata)['x']
    position = Factor([0, 1], "position")
    x = Feature(position[0] + 4 * 2 + position[1], "x")
    assert x(state=state) == x_parsed(state=state)

    x_parsed = rlang.parse("Factor position := S[0:3]\nFeature x := position[0] + 4 * 2 + 3 / position[1]", metadata)['x']
    position = Factor(list(range(5))[slice(0, 3, 1)], "position")
    x = Feature(position[0] + 4 * 2 + 3 / position[1], "x")
    assert x(state=state) == x_parsed(state=state)


def test_Predicate():
    metadata = MDPMetadata.from_state_action(np.zeros(5), np.zeros(5))
    state = State(np.array([4, 5, 6, 7, 8]))

    hi_parsed = rlang.parse("Factor position := S[0, 1]\nFeature x := position[0]\nPredicate hi := x == 1 and True or False", metadata)['hi']
    position = Factor([0, 1], "position")
    x = Feature(position[0])
    hi = Predicate(x == 1 & True | False)
    assert hi(state=state) == hi_parsed(state=state)

    # TODO: Need more tests for Predicate


def test_Action():
    metadata = MDPMetadata.from_state_action(np.zeros(5), np.zeros(5))

    up_parsed = rlang.parse("Action up := -1.3", metadata)['up']
    up = ActionReference(-1.3, "up")
    assert up() == up_parsed()

    up_parsed = rlang.parse("Action up := [0, 1.0, -4.2]", metadata)['up']
    up = ActionReference([0, 1.0, -4.2], "up")
    # assert up() == up_parsed()

    # TODO: Need more tests for Action


def test_Policy():
    metadata = MDPMetadata.from_state_action(np.zeros(5), np.zeros(5))
    s = State([4, 1, 2, 3, 4])

    knowledge = rlang.parse_file("tests_resources/listener_tests/policy.rlang", metadata)
    test1 = knowledge['test1']
    test2 = knowledge['test2']

    # print(test2(state=s))


if __name__ == "__main__":
    test_Policy()
