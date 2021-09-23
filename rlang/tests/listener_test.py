from __future__ import annotations
import numpy as np
import rlang
from rlang.src.grounding import *


def test_Factor():
    metadata = MDPMetadata.from_state_action(np.zeros(5), np.zeros(5))
    state = State(np.array([4, 5, 6, 7, 8]))

    position_parsed = rlang.parse("Factor position := S[0]", metadata)['position']
    position = Factor(0, "position")
    assert position(state=state) == position_parsed(state=state)

    position_parsed = rlang.parse("Factor position := S[0:3]\nFactor p2 := position[0]", metadata)['position']
    position = Factor([0, 1, 2], "position")
    assert position(state=state) == position_parsed(state=state)

    position_parsed = rlang.parse("Factor position := S[0:3]", metadata)['position']
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

    x_parsed = rlang.parse("Feature x := 1 * 2 + 4 * (1 + 2)", metadata)['x']
    assert x_parsed(state=state) == 14

    x_parsed = rlang.parse("Feature x := [0, 1] * 2 * S[0]", metadata)['x']
    print(x_parsed(state=state))


def test_Predicate():
    metadata = MDPMetadata.from_state_action(np.zeros(5), np.zeros(5))
    state = State(np.array([4, 5, 6, 7, 8]))

    hi_parsed = rlang.parse("Factor position := S[0, 1]\nFeature x := position[0]\nPredicate hi := x == 1 and True or False", metadata)['hi']
    position = Factor([0, 1], "position")
    x = Feature(position[0])
    hi = Predicate(x == 1 & True | False)
    assert hi(state=state) == hi_parsed(state=state)

    hi_parsed = rlang.parse("Predicate hi := True or False and True == True and 14 == 14", metadata)['hi']
    print(hi_parsed(state=state))
    assert hi_parsed(state=state) == True

    hi_parsed = rlang.parse("Predicate hi := True or False and False or True", metadata)['hi']
    print(hi_parsed(state=state))

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

    print(test1(state=s))

    # TODO: Need more tests


def test_Option():
    metadata = MDPMetadata.from_state_action(np.zeros(5), np.zeros(5))
    s = State([3, 1, 2, 3, 4])

    knowledge = rlang.parse_file("tests_resources/listener_tests/option.rlang", metadata)
    build_bridge = knowledge['build_bridge']
    do = knowledge['do_something']

    print(build_bridge.can_execute(state=s))
    print(build_bridge(state=s))
    print(do(state=s))

    # TODO: Need more tests


def test_MarkovFeature():
    metadata = MDPMetadata.from_state_action(np.zeros(5), np.zeros(5))
    s = State([3, 1, 2, 3, 4])
    s2 = State([3, 2, 2, 3, 4])

    # This syntax is cool. It allows you to cast a function of state to a function of next_state
    knowledge = rlang.parse_file("tests_resources/listener_tests/markov_feature.rlang", metadata)
    f1 = knowledge['f1']
    f2 = knowledge['f2']
    f3 = knowledge['f3']
    f4 = knowledge['f4']
    f5 = knowledge['f5']

    print(f1(state=s))
    print(f2(next_state=s))
    print(f3(state=s))
    print(f4(next_state=s))
    print(f5(state=s, next_state=s2))


def test_Effect():
    metadata = MDPMetadata.from_state_action(np.zeros(5), np.zeros(5))
    s = State([3, 2, 2, 3, 4])
    s2 = State([3, 2, 2, 3, 4])

    knowledge = rlang.parse_file("tests_resources/listener_tests/effect.rlang", metadata)
    r = knowledge.reward_function
    print(r(state=s))
    t = knowledge.transition_function
    print(t(state=s))


if __name__ == "__main__":
    test_Factor()
