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

    def test_Proposition(self):
        metadata = MDPMetadata.from_state_action(np.zeros(5), np.zeros(5))
        state = State(np.array([4, 5, 6, 7, 8]))

        hi_parsed = \
            rlang.parse(
                "Factor position := S[0, 1]\nFeature x := position[0]\nProposition hi := x == 1 and True or False",
                metadata)['hi']
        position = Factor([0, 1], "position")
        x = Feature(position[0])
        hi = Proposition(x == 1 & True | False)
        assert hi(state=state) == hi_parsed(state=state)

        hi_parsed = rlang.parse("Proposition hi := True or False and True == True and 14 == 14", metadata)['hi']
        assert hi_parsed(state=state) == True

        hi_parsed = rlang.parse("Proposition hi := True or False and False or True", metadata)['hi']
        assert hi_parsed(state=state) == True

        x_parsed = rlang.parse("Proposition x := [0] in [[2], [1], [2, 3]]", metadata)['x']
        assert x_parsed(state=state) == [[False]]

        x_parsed = rlang.parse("Proposition x := [0, 1] in [[0, 1], [1, 1], [2, 3]]", metadata)['x']
        assert x_parsed(state=state) == [[True]]

        state2 = State(np.array([[0, 1], [5, 6]]))
        x_parsed = rlang.parse("Factor h := S[0, 1]\nProposition x := h in [[0, 1], [2, 3]]", metadata)['x']

        # TODO: fix this
        # QUESTION: why is this true because isn't [5, 6] not in the array
        assert x_parsed(state=state2) == [[True]]

        state2 = State(np.array([[0, 1], [5, 6]]))
        x_parsed = rlang.parse("Proposition x := S[0] == [[0], [5]]", metadata)['x']
        assert ((x_parsed(state=state2)) == [[True], [True]]).all()

        test_parsed = rlang.parse("Feature f := S[0, 1] * 3\nProposition test := f == [3, 6]", metadata)["test"]
        state3 = State(np.array([[1, 2], [1, 1]]))
        assert ((test_parsed(state=state3)) == [[True], [False]]).all()

        state2 = State(np.array([[0, 1], [5, 6]]))
        x_parsed = rlang.parse("Proposition x := S[0] == [[0], [1]]", metadata)['x']
        assert ((x_parsed(state=state2)) == [[True], [False]]).all()

        # QUESTION: just to confirm, we cannot compare between instances of PrimitiveGroundings
        # x_parsed = rlang.parse("Factor position := S[0, 1]\nFeature x := position[0]\nFeature y := position[0]\nPredicate test3 := x < y", metadata)['x']
        # print(x_parsed(state=state2))

        up_parsed = rlang.parse("Action up := -1.3\nProposition x := up == A", metadata)['x']
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

    def test_Policy(self):
        metadata = MDPMetadata.from_state_action(np.zeros(5), np.zeros(5))
        s = State([0, 1, 2, 3, 4])
        s2 = State([1, 1, 2, 3, 4])

        knowledge = rlang.parse_file("tests_resources/valid_examples/policy.rlang", metadata)

        simple = knowledge['simple']
        assert simple(state=s) == {Action(2): 1.0}
        assert simple(state=s) == {Action(2): 1.0}  # Ensure that policies can be executed more than once

        prob_split = knowledge['prob_split']
        assert prob_split(state=s) == {Action(5): 0.1, Action(3): 0.9}

        prob_split_less_than_1 = knowledge['prob_split_less_than_1']
        assert prob_split_less_than_1(state=s) == {Action(2): 0.1, Action(6): 0.5}

        prob_split_frac = knowledge['prob_split_frac']
        assert prob_split_frac(state=s) == {Action(1): 1.0/3, Action(2): 2.0/3}

        prob_nest = knowledge['prob_nest']
        assert prob_nest(state=s) == {Action(3): 0.025}

        prob_rejoin = knowledge['prob_rejoin']
        assert prob_rejoin(state=s) == {Action(2): 1.0}

        one_layer_deep = knowledge['one_layer_deep']
        assert one_layer_deep(state=s) == {Action(5): 0.05, Action(3): 0.95}

        two_layers_deep = knowledge['two_layers_deep']
        assert two_layers_deep(state=s) == {Action(5): 0.05, Action(3): 0.95}

        two_layers_deep_rejoin = knowledge['two_layers_deep_rejoin']
        assert two_layers_deep_rejoin(state=s) == {Action(5): 0.05, Action(3): 0.95}

        simple_conditional = knowledge['simple_conditional']
        assert simple_conditional(state=s) == {Action(2): 1.0}

        factor_conditional = knowledge['factor_conditional']
        assert factor_conditional(state=s) == {Action(2): 1.0}
        assert factor_conditional(state=s2) == {Action(2): 0.8, Action(3): 0.2}

        missing_conditional = knowledge['missing_conditional']
        assert missing_conditional(state=s) == {}

    def test_Option(self):
        metadata = MDPMetadata.from_state_action(np.zeros(5), np.zeros(5))
        s = State([0, 1, 2, 3, 4])
        s2 = State([1, 2, 2, 3, 4])
        s3 = State([2, 1, 2, 3, 4])
        s4 = State([2, 3, 2, 3, 4])
        s5 = State([0, 0, 2, 3, 4])

        knowledge = rlang.parse_file("tests_resources/valid_examples/option.rlang", metadata)

        simple_option = knowledge['simple_option']
        assert simple_option.can_initiate(state=s)
        assert not simple_option.can_initiate(state=s2)
        assert simple_option(state=s) == {Action(2): 1.0}
        assert simple_option(state=s3) == OptionTermination()

        complex_option = knowledge['complex_option']
        assert complex_option.can_initiate(state=s)
        assert not complex_option.can_initiate(state=s2)
        assert complex_option(state=s3) == {Action(2): 0.8, Action(3): 0.2}
        assert complex_option(state=s) == {Action(2): 1.0}
        assert complex_option(state=s2) == OptionTermination()

        all_in_one = knowledge['all_in_one']
        assert all_in_one.can_initiate(state=s3)
        assert all_in_one(state=s) == {Action(3): 0.2, Action(2): 0.08000000000000002}
        assert all_in_one(state=s4) == {Action(2): 1.0}
        assert all_in_one(state=s5) == {Action(3): 1.0}
        assert all_in_one(state=s2) == OptionTermination()

    def test_Effect(self):
        metadata = MDPMetadata.from_state_action(np.zeros(5), np.zeros(5))
        s = State([0, 1, 2, 3, 4])
        s2 = State([3, 2, 2, 3, 4])
        s3 = State([5, 2, 2, 3, 4])

        knowledge = rlang.parse_file("tests_resources/valid_examples/effect.rlang", metadata)

        single_reward = knowledge['single_reward']
        assert single_reward.reward_function(state=s) == 10

        probabilistic_reward = knowledge['probabilistic_reward']
        assert probabilistic_reward.reward_function(state=s) == 2.8

        multiple_rewards = knowledge['multiple_rewards']
        assert multiple_rewards.reward_function(state=s) == 10.8

        conditional_reward = knowledge['conditional_reward']
        assert conditional_reward.reward_function(state=s) == 15
        assert conditional_reward.reward_function(state=s2) == 5
        assert conditional_reward.reward_function(state=s3) == 20

        single_transition = knowledge['single_transition']
        assert single_transition.transition_function(state=s) == {s * 2: 1.0}
        assert single_transition.transition_function(state=s2) == {s2 * 2: 1.0}

        probabilistic_transition = knowledge['probabilistic_transition']
        assert probabilistic_transition.transition_function(state=s) == {s * 3: 0.5, s * 2: 0.5}

        conditional_transition = knowledge['conditional_transition']
        assert conditional_transition.transition_function(state=s) == {s * 3: 1.0}
        assert conditional_transition.transition_function(state=s2) == {s2 * 2: 1.0}
        assert conditional_transition.transition_function(state=s3) == {s3: 0.5, s3 * 5: 0.3}

        # single_predictions = knowledge['single_predictions']
        # print(single_predictions.predictions)



if __name__ == '__main__':
    unittest.main()
