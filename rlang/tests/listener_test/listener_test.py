from __future__ import annotations
import unittest
import numpy as np
import rlang
from rlang.src.grounding import *


class ListenerTests(unittest.TestCase):

    def test_Factor(self):
        metadata = MDPMetadata.from_state_action(np.zeros(5), np.zeros(5))
        state = State(np.array([4, 5, 6, 7, 8]))

        position_parsed = rlang.parse("Factor position := S[0]", metadata)['position']
        position = Factor(0, "position")
        assert position(state=state) == position_parsed(state=state)
        # assert position_parsed(state=state) == BatchedPrimitive(4)

        position_parsed = rlang.parse("Factor position := S[0:3]\nFactor p2 := position[0]", metadata)['position']
        position = Factor([0, 1, 2], "position")
        assert position(state=state) == position_parsed(state=state)

        position_parsed = rlang.parse("Factor position := S[0:3]", metadata)['position']
        assert position(state=state) == position_parsed(state=state)

        position_parsed = rlang.parse("Factor position := S[0, 3, 1]", metadata)['position']
        position = Factor([0, 3, 1], "position")
        assert position(state=state) == position_parsed(state=state)

        state2 = State(np.array([[0, 1], [2, 3]]))
        position_parsed = rlang.parse("Factor position := S[0]", metadata)['position']
        position = Factor([0], "position")
        assert (position_parsed(state=state2) == position(state=state2)).all()

        position_parsed = rlang.parse("Factor position := S[:-1]", metadata)['position']
        position = Factor(slice(0, -1), "position")
        assert (position_parsed(state=state) == position(state=state)).all()

    def test_Feature(self):
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

        x_parsed = rlang.parse("Factor position := S[0, 1]\nFeature x := position[0] + 4 * 2 + position[1]", metadata)[
            'x']
        position = Factor([0, 1], "position")
        x = Feature(position[0] + 4 * 2 + position[1], "x")
        assert x(state=state) == x_parsed(state=state)

        x_parsed = \
            rlang.parse("Factor position := S[0:3]\nFeature x := position[0] + 4 * 2 + 3 / position[1]", metadata)['x']
        position = Factor(list(range(5))[slice(0, 3, 1)], "position")
        x = Feature(position[0] + 4 * 2 + 3 / position[1], "x")
        assert x(state=state) == x_parsed(state=state)

        x_parsed = rlang.parse("Feature x := 1 * 2 + 4 * (1 + 2)", metadata)['x']
        assert x_parsed(state=state) == 14

        x_parsed = rlang.parse("Feature x := [2, 1] * 2 * S[0, 1]", metadata)['x']
        position = Factor([0, 1], "position")

        x = Feature(2 * position * np.array([2, 1]), "x")
        y = Feature(2 * np.array([2, 1]) * position, "y")
        y_parsed = rlang.parse("Feature x := S[0, 1] * [2, 1] * 2", metadata)['x']

        assert (x(state=state) == x_parsed(state=state)).all()
        assert (x(state=state) == y(state=state)).all()
        assert (y(state=state) == y_parsed(state=state)).all()

        x_parsed = rlang.parse("Feature x := [2, 1] / S[0, 1]", metadata)['x']
        y_parsed = rlang.parse("Feature x := S[0, 1] / [2, 1]", metadata)['x']
        y = Feature(position / np.array([2, 1]), "x")
        x = Feature(np.array([2, 1]) / position, "y")

        assert (x(state=state) == x_parsed(state=state)).all()
        assert (x(state=state) != y(state=state)).all()
        assert (y(state=state) == y_parsed(state=state)).all()

        x_parsed = rlang.parse("Feature x := [2, 1] + S[0, 1]", metadata)['x']
        y_parsed = rlang.parse("Feature x := S[0, 1] + [2, 1]", metadata)['x']
        y = Feature(position + np.array([2, 1]), "x")
        x = Feature(np.array([2, 1]) + position, "y")

        assert (x(state=state) == x_parsed(state=state)).all()
        assert (x(state=state) == y(state=state)).all()
        assert (y(state=state) == y_parsed(state=state)).all()

        x_parsed = rlang.parse("Feature x := [2, 1] - S[0, 1]", metadata)['x']
        y_parsed = rlang.parse("Feature x := S[0, 1] - [2, 1]", metadata)['x']
        y = Feature(position - np.array([2, 1]), "x")
        x = Feature(np.array([2, 1]) - position, "y")

        assert (x(state=state) == x_parsed(state=state)).all()
        assert (x(state=state) != y(state=state)).all()
        assert (y(state=state) == y_parsed(state=state)).all()

        x_parsed = rlang.parse("Factor position := S[0, 1]\nFeature x := position[0] + position[1]", metadata)['x']
        assert (x_parsed(state=state)) == 9

        x_parsed = \
            rlang.parse("Factor position := S[0, 1]\nFeature x := position[0]\nFeature y := position[1]/x", metadata)[
                'y']
        assert (x_parsed(state=state)) == 5 / 4

    def test_Predicate(self):
        metadata = MDPMetadata.from_state_action(np.zeros(5), np.zeros(5))
        state = State(np.array([4, 5, 6, 7, 8]))

        hi_parsed = \
            rlang.parse(
                "Factor position := S[0, 1]\nFeature x := position[0]\nPredicate hi := x == 1 and True or False",
                metadata)['hi']
        position = Factor([0, 1], "position")
        x = Feature(position[0])
        hi = Predicate(x == 1 & True | False)
        assert hi(state=state) == hi_parsed(state=state)

        hi_parsed = rlang.parse("Predicate hi := True or False and True == True and 14 == 14", metadata)['hi']
        assert hi_parsed(state=state) == True

        hi_parsed = rlang.parse("Predicate hi := True or False and False or True", metadata)['hi']
        assert hi_parsed(state=state) == True

        x_parsed = rlang.parse("Predicate x := [0] in [[2], [1], [2, 3]]", metadata)['x']
        assert x_parsed(state=state) == [[False]]

        x_parsed = rlang.parse("Predicate x := [0, 1] in [[0, 1], [1, 1], [2, 3]]", metadata)['x']
        assert x_parsed(state=state) == [[True]]

        state2 = State(np.array([[0, 1], [5, 6]]))
        x_parsed = rlang.parse("Factor h := S[0, 1]\nPredicate x := h in [[0, 1], [2, 3]]", metadata)['x']

        # TODO: fix this
        # QUESTION: why is this true because isn't [5, 6] not in the array
        assert x_parsed(state=state2) == [[True]]

        state2 = State(np.array([[0, 1], [5, 6]]))
        x_parsed = rlang.parse("Predicate x := S[0] == [[0], [5]]", metadata)['x']
        assert ((x_parsed(state=state2)) == [[True], [True]]).all()

        test_parsed = rlang.parse("Feature f := S[0, 1] * 3\nPredicate test := f == [3, 6]", metadata)["test"]
        state3 = State(np.array([[1, 2], [1, 1]]))
        assert ((test_parsed(state=state3)) == [[True], [False]]).all()

        state2 = State(np.array([[0, 1], [5, 6]]))
        x_parsed = rlang.parse("Predicate x := S[0] == [[0], [1]]", metadata)['x']
        assert ((x_parsed(state=state2)) == [[True], [False]]).all()

        # QUESTION: just to confirm, we cannot compare between instances of PrimitiveGroundings
        # x_parsed = rlang.parse("Factor position := S[0, 1]\nFeature x := position[0]\nFeature y := position[0]\nPredicate test3 := x < y", metadata)['x']
        # print(x_parsed(state=state2))

        up_parsed = rlang.parse("Action up := -1.3\nPredicate x := up == A", metadata)['x']
        up = ActionReference(-1.3, "up")
        assert up_parsed(state=state2, action=up) == [[True]]
        assert up_parsed(state=state2, action=Action(-1.3)) == [[True]]

    def test_Action(self):
        metadata = MDPMetadata.from_state_action(np.zeros(5), np.zeros(5))

        up_parsed = rlang.parse("Action up := -1.3", metadata)['up']
        up = ActionReference(-1.3, "up")
        assert up() == up_parsed()

        up_parsed = rlang.parse("Action up := [0, 1.0, -4.2]", metadata)['up']
        up = ActionReference([0, 1.0, -4.2], "up")
        assert (up() == up_parsed()).all()

        # TODO: test action as a batched primitive in lmdp tests
        # state2 = State(np.array([[0, 1], [5, 6]]))
        # down_parsed = rlang.parse("Action down := ", metadata)['down']
        # print(down_parsed(state=state2))

    def policy_unwrap(self, policy, s, expected_actions):
        action = policy(state=s)
        i = 0
        while not isinstance(action, PolicyComplete):
            for k, v in action.items():
                a = k()
                if i >= len(expected_actions):
                    return False
                if a not in expected_actions[i]:
                    return False
                elif expected_actions[i][a] != v:
                    return False
            action = policy(state=s)
            i += 1
        if len(expected_actions) != i:
            return False
        else:
            return True

    def test_Policy(self):
        metadata = MDPMetadata.from_state_action(np.zeros(5), np.zeros(5))
        s = State([0, 1, 2, 3, 4])
        s2 = State([1, 1, 2, 3, 4])

        # Simple 1-layer tests
        knowledge = rlang.parse_file("tests_resources/valid_examples/policy_1_layer.rlang", metadata)
        up_down_up = knowledge['up_down_up']
        assert (self.policy_unwrap(up_down_up, s, [{Action(2): 1.0}, {Action(-1): 1.0}, {Action(1): 1.0}]))
        # assert (self.policy_unwrap(up_down_up, s, [{Action(2): 1.0}, {Action(-1): 1.0}, {Action(1): 1.0}]))
        # TODO: Need to fix policies first

        left_once = knowledge['left_once']
        assert (self.policy_unwrap(left_once, s, [{Action(2): 1.0}]))

        left_right_split = knowledge['left_right_split']
        assert (self.policy_unwrap(left_right_split, s, [{Action(2): 0.25, Action(-2): 0.75}]))

        sequential_prob = knowledge['sequential_prob']
        assert (self.policy_unwrap(sequential_prob, s, [{Action(2): 1.0}, {Action(1): 0.3, Action(-1): 0.7}]))

        conditional = knowledge['conditional']
        # assert(self.policy_unwrap(conditional, s, [{Action(-2): 1.0}]))
        # print(conditional(state=s2))
        # assert(self.policy_unwrap(conditional, s2, [{Action(2): 1.0}]))


if __name__ == '__main__':
    unittest.main()
