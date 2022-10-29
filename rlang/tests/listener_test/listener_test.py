from __future__ import annotations
import unittest
import numpy as np

from .context import rlang
from rlang import VectorState, ObjectOrientedState, Action, MDPObject


class ListenerTests(unittest.TestCase):

    def test_Factor(self):
        state = VectorState(np.array([4, 5, 6, 7, 8]))

        position_parsed = rlang.parse("Factor position := S[0]")['position']
        position = rlang.Factor(0, "position")
        assert position(state=state) == position_parsed(state=state)
        # assert position_parsed(state=state) == Primitive(4)

        position_parsed = rlang.parse("Factor position := S[0:3]\nFactor p2 := position[0]")['position']
        position = rlang.Factor([0, 1, 2], "position")
        assert position(state=state) == position_parsed(state=state)

        position_parsed = rlang.parse("Factor position := S[0:3]")['position']
        assert position(state=state) == position_parsed(state=state)

        position_parsed = rlang.parse("Factor position := S[0, 3, 1]")['position']
        position = rlang.Factor([0, 3, 1], "position")
        assert position(state=state) == position_parsed(state=state)

        state2 = VectorState(np.array([[0, 1], [2, 3]]))
        position_parsed = rlang.parse("Factor position := S[0]")['position']
        position = rlang.Factor([0], "position")
        assert (position_parsed(state=state2) == position(state=state2)).all()

        position_parsed = rlang.parse("Factor position := S[:-1]")['position']
        position = rlang.Factor(slice(0, -1), "position")
        assert (position_parsed(state=state) == position(state=state)).all()

    def test_Feature(self):
        state = VectorState(np.array([4, 5, 6, 7, 8]))

        x_parsed = rlang.parse("Feature x := S[0, 1]")['x']
        x = rlang.Feature.from_Factor(rlang.Factor([0, 1]), "x")
        assert x(state=state) == x_parsed(state=state)

        x_parsed = rlang.parse("Factor position := S[0, 1]\nFeature x := position[0]")['x']
        position = rlang.Factor([0, 1], "position")
        x = rlang.Feature.from_Factor(position[0], "x")
        assert x(state=state) == x_parsed(state=state)

        x_parsed = rlang.parse("Factor position := S[0, 1]\nFeature x := position * 2")['x']
        position = rlang.Factor([0, 1], "position")
        x = rlang.Feature.from_Factor(position * 2, "x")
        assert x(state=state) == x_parsed(state=state)
        x = rlang.Feature.from_Factor(2 * position, "x")
        assert x(state=state) == x_parsed(state=state)

        x_parsed = rlang.parse("Factor position := S[0, 1]\nFeature x := position[0] + 4 * 2 + position[1]")[
            'x']
        position = rlang.Factor([0, 1], "position")
        x = rlang.Feature(position[0] + 4 * 2 + position[1], "x")
        assert x(state=state) == x_parsed(state=state)

        x_parsed = \
            rlang.parse("Factor position := S[0:3]\nFeature x := position[0] + 4 * 2 + 3 / position[1]")['x']
        position = rlang.Factor(list(range(5))[slice(0, 3, 1)], "position")
        x = rlang.Feature(position[0] + 4 * 2 + 3 / position[1], "x")
        assert x(state=state) == x_parsed(state=state)

        x_parsed = rlang.parse("Feature x := 1 * 2 + 4 * (1 + 2)")['x']
        assert x_parsed(state=state) == 14

        x_parsed = rlang.parse("Feature x := [2, 1] * 2 * S[0, 1]")['x']
        position = rlang.Factor([0, 1], "position")

        x = rlang.Feature(2 * position * np.array([2, 1]), "x")
        y = rlang.Feature(2 * np.array([2, 1]) * position, "y")
        y_parsed = rlang.parse("Feature x := S[0, 1] * [2, 1] * 2")['x']

        assert (x(state=state) == x_parsed(state=state)).all()
        assert (x(state=state) == y(state=state)).all()
        assert (y(state=state) == y_parsed(state=state)).all()

        x_parsed = rlang.parse("Feature x := [2, 1] / S[0, 1]")['x']
        y_parsed = rlang.parse("Feature x := S[0, 1] / [2, 1]")['x']
        y = rlang.Feature(position / np.array([2, 1]), "x")
        x = rlang.Feature(np.array([2, 1]) / position, "y")

        assert (x(state=state) == x_parsed(state=state)).all()
        assert (x(state=state) != y(state=state)).all()
        assert (y(state=state) == y_parsed(state=state)).all()

        x_parsed = rlang.parse("Feature x := [2, 1] + S[0, 1]")['x']
        y_parsed = rlang.parse("Feature x := S[0, 1] + [2, 1]")['x']
        y = rlang.Feature(position + np.array([2, 1]), "x")
        x = rlang.Feature(np.array([2, 1]) + position, "y")

        assert (x(state=state) == x_parsed(state=state)).all()
        assert (x(state=state) == y(state=state)).all()
        assert (y(state=state) == y_parsed(state=state)).all()

        x_parsed = rlang.parse("Feature x := [2, 1] - S[0, 1]")['x']
        y_parsed = rlang.parse("Feature x := S[0, 1] - [2, 1]")['x']
        y = rlang.Feature(position - np.array([2, 1]), "x")
        x = rlang.Feature(np.array([2, 1]) - position, "y")

        assert (x(state=state) == x_parsed(state=state)).all()
        assert (x(state=state) != y(state=state)).all()
        assert (y(state=state) == y_parsed(state=state)).all()

        x_parsed = rlang.parse("Factor position := S[0, 1]\nFeature x := position[0] + position[1]")['x']
        assert (x_parsed(state=state)) == 9

        x_parsed = \
            rlang.parse("Factor position := S[0, 1]\nFeature x := position[0]\nFeature y := position[1]/x")[
                'y']
        assert (x_parsed(state=state)) == 5 / 4

    def test_Proposition(self):
        # TODO: Re-write these using new Primitive
        state = VectorState(np.array([4, 5, 6, 7, 8]))
        state2 = VectorState(np.array([1, 4, 6, 7, 8]))

        hi_parsed = \
            rlang.parse(
                "Factor position := S[0, 1]\nFeature x := position[0]\nProposition hi := x == 1 and True or False")[
                'hi']
        position = rlang.Factor([0, 1], "position")
        x = rlang.Feature(position[0])
        hi = rlang.Proposition(x == 1 & True | False)
        assert hi(state=state) == hi_parsed(state=state)

        hi_parsed = rlang.parse("Proposition hi := True or False and True == True and 14 == 14")['hi']
        assert hi_parsed(state=state) == True

        hi_parsed = rlang.parse("Proposition hi := True or False and False or True")['hi']
        assert hi_parsed(state=state) == True

        # Singleton in
        p_parsed = rlang.parse('Proposition p := S[0] in [0, 4, 2]')['p']
        assert p_parsed(state=state) == True
        assert p_parsed(state=state2) == False

        # Array in
        p_parsed = rlang.parse('Proposition p := S[0, 1] in [[4, 5], [6, 7]]')['p']
        assert p_parsed(state=state) == True
        assert p_parsed(state=state2) == False

        knowledge = rlang.parse(
            'Constant lava_locs := [[3, 2], [1, 4], [2, 4], [2, 5]]\nFactor position := S[0, 1]\nProposition in_lava := position in lava_locs')
        in_lava = knowledge['in_lava']

        assert in_lava(state=state) == False
        assert in_lava(state=state2) == True

        # x_parsed = rlang.parse("Proposition x := [0] in [[2], [1], [2, 3]]", metadata)['x']
        # assert x_parsed(state=state) == [[False]]
        #
        # x_parsed = rlang.parse("Proposition x := [0, 1] in [[0, 1], [1, 1], [2, 3]]", metadata)['x']
        # assert x_parsed(state=state) == [[True]]
        #
        # state2 = VectorState(np.array([[0, 1], [5, 6]]))
        # x_parsed = rlang.parse("Factor h := S[0, 1]\nProposition x := h in [[0, 1], [2, 3]]", metadata)['x']

        # # TODO: fix this
        # # QUESTION: why is this true because isn't [5, 6] not in the array
        # assert x_parsed(state=state2) == [[True]]
        #
        # state2 = VectorState(np.array([[0, 1], [5, 6]]))
        # x_parsed = rlang.parse("Proposition x := S[0] == [[0, 1]]", metadata)['x']
        # assert (x_parsed(state=state2) == [[True]])

        # test_parsed = rlang.parse("Feature f := S[0, 1] * 3\nProposition test := f == [3, 6]", metadata)["test"]
        # state3 = VectorState(np.array([[1, 2], [1, 1]]))
        # assert ((test_parsed(state=state3)) == [[True], [False]]).all()

        # QUESTION: just to confirm, we cannot compare between instances of PrimitiveGroundings
        # x_parsed = rlang.parse("Factor position := S[0, 1]\nFeature x := position[0]\nFeature y := position[0]\nPredicate test3 := x < y", metadata)['x']
        # print(x_parsed(state=state2))

        # up_parsed = rlang.parse("Action up := -1.3\nProposition x := up == A", metadata)['x']
        # up = ActionReference(-1.3, "up")
        # assert up_parsed(state=state2, action=up) == [[True]]
        # assert up_parsed(state=state2, action=Action(-1.3)) == [[True]]

    def test_Action(self):
        # metadata = MDPMetadata.from_state_action(np.zeros(5), np.zeros(5))
        metadata = None

        up_parsed = rlang.parse("Action up := -1.3", metadata)['up']
        up = rlang.ActionReference(-1.3, "up")
        assert up() == up_parsed()

        up_parsed = rlang.parse("Action up := [0, 1.0, -4.2]", metadata)['up']
        up = rlang.ActionReference([0, 1.0, -4.2], "up")
        assert up() == up_parsed()

        # TODO: test action as a batched primitive in lmdp tests
        # state2 = VectorState(np.array([[0, 1], [5, 6]]))
        # down_parsed = rlang.parse("Action down := ", metadata)['down']
        # print(down_parsed(state=state2))

    def test_Policy(self):
        s = VectorState([0, 1, 2, 3, 4])
        s2 = VectorState([1, 1, 2, 3, 4])

        knowledge = rlang.parse_file("listener_test/tests_resources/valid_examples/policy.rlang")

        simple = knowledge['simple']
        assert simple(state=s) == {Action(2): 1.0}
        assert simple(state=s) == {Action(2): 1.0}  # Ensure that policies can be executed more than once

        prob_split = knowledge['prob_split']
        assert prob_split(state=s) == {Action(5): 0.1, Action(3): 0.9}

        prob_split_less_than_1 = knowledge['prob_split_less_than_1']
        assert prob_split_less_than_1(state=s) == {Action(2): 0.1, Action(6): 0.5}

        prob_split_frac = knowledge['prob_split_frac']
        assert prob_split_frac(state=s) == {Action(1): 1.0 / 3, Action(2): 2.0 / 3}

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
        s = VectorState([0, 1, 2, 3, 4])
        s2 = VectorState([1, 2, 2, 3, 4])
        s3 = VectorState([2, 1, 2, 3, 4])
        s4 = VectorState([2, 3, 2, 3, 4])
        s5 = VectorState([0, 0, 2, 3, 4])

        knowledge = rlang.parse_file("listener_test/tests_resources/valid_examples/option.rlang")

        simple_option = knowledge['simple_option']
        assert simple_option.can_initiate(state=s)
        assert not simple_option.can_initiate(state=s2)
        assert simple_option(state=s) == {Action(2): 1.0}
        assert simple_option(state=s3) == rlang.OptionTermination()

        complex_option = knowledge['complex_option']
        assert complex_option.can_initiate(state=s)
        assert not complex_option.can_initiate(state=s2)
        assert complex_option(state=s3) == {Action(2): 0.8, Action(3): 0.2}
        assert complex_option(state=s) == {Action(2): 1.0}
        assert complex_option(state=s2) == rlang.OptionTermination()

        all_in_one = knowledge['all_in_one']
        assert all_in_one.can_initiate(state=s3)
        assert all_in_one(state=s) == {Action(3): 0.2, Action(2): 0.08000000000000002}
        assert all_in_one(state=s4) == {Action(2): 1.0}
        assert all_in_one(state=s5) == {Action(3): 1.0}
        assert all_in_one(state=s2) == rlang.OptionTermination()

    def test_Effect(self):
        s = VectorState([0, 1, 2, 3, 4])
        s2 = VectorState([3, 2, 2, 3, 4])
        s3 = VectorState([5, 2, 2, 3, 4])

        knowledge = rlang.parse_file("listener_test/tests_resources/valid_examples/effect.rlang")

        single_reward = knowledge['single_reward']
        assert single_reward.reward_function(state=s) == 10

        factor_reward = knowledge['factor_reward']
        assert factor_reward.reward_function(state=s) == 0
        assert factor_reward.reward_function(state=s2) == 6

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
        # print(probabilistic_transition.transition_function(state=s))
        assert probabilistic_transition.transition_function(state=s) == {s * 3: 0.5, s * 2: 0.5}

        conditional_transition = knowledge['conditional_transition']
        assert conditional_transition.transition_function(state=s) == {s * 3: 1.0}
        assert conditional_transition.transition_function(state=s2) == {s2 * 2: 1.0}
        assert conditional_transition.transition_function(state=s3) == {s3: 0.5, s3 * 5: 0.3}

        single_predictions = knowledge['single_predictions']
        f1_prediction = single_predictions.prediction_dict['f1'][0]
        f2_prediction = single_predictions.prediction_dict['f2'][0]
        assert f1_prediction(state=s2) == {s2[0] * 10: 1.0}
        assert f2_prediction(state=s2) == {s2 * 2 + 3: 1.0}

        compound_predictions = knowledge['compound_predictions']
        f1_prediction = compound_predictions.prediction_dict['f1'][0]
        f2_prediction = compound_predictions.prediction_dict['f2'][0]
        assert f1_prediction(state=s) == {s[0] + s[1]: 1.0}
        assert f2_prediction(state=s2) == {s2[0] * 2 * s2[1]: 1.0}

        probabilistic_prediction_a = knowledge['probabilistic_prediction_a']
        f1_prediction = probabilistic_prediction_a.prediction_dict['f1'][0]
        assert f1_prediction(state=s2) == {s2[0] * 2: 0.25, s2[0] * 3: 0.75}

        probabilistic_prediction_b = knowledge['probabilistic_prediction_b']
        f1_prediction = probabilistic_prediction_b.prediction_dict['f1'][0]
        f2_prediction = probabilistic_prediction_b.prediction_dict['f2'][0]
        assert f1_prediction(state=s2) == {s2[0] + 6: 0.7}
        assert f2_prediction(state=s2) == {s2[1] + 4: 0.3}

        conditional_prediction = knowledge['conditional_prediction']
        f1_prediction = conditional_prediction.prediction_dict['f1'][0]
        f2_prediction = conditional_prediction.prediction_dict['f2'][0]
        assert f1_prediction(state=s) == {s[0] * 3: 1.0}
        assert f1_prediction(state=s2) == {s2[0] * 2: 1.0}
        assert f2_prediction(state=s3) == {s3[1]: 0.5, s3[1] * 5: 0.3}

        simple_effect_references = knowledge['simple_effect_references']
        f1_prediction = simple_effect_references.prediction_dict['f1'][0]
        f2_prediction = simple_effect_references.prediction_dict['f2'][0]
        assert f1_prediction(state=s2) == {s2[0] * 10: 1.0}
        assert f2_prediction(state=s2) == {s2 * 2 + 3: 1.0}
        assert simple_effect_references.reward_function(state=s2) == 16
        assert simple_effect_references.transition_function(state=s) == {s * 2: 1.0}

        simple_effect_references_overlap = knowledge['simple_effect_references_overlap']
        f1_prediction = simple_effect_references_overlap.prediction_dict['f1'][0]
        f2_prediction = simple_effect_references_overlap.prediction_dict['f2'][0]
        assert f1_prediction(state=s) == {s[0] * 10: 1.0, s[0] + s[1]: 1.0}
        assert f2_prediction(state=s2) == {s2 * 2 + 3: 1.0, s2[0] * s2[1] * 2: 1.0}
        assert simple_effect_references_overlap.reward_function(state=s) == 20

        simple_probabilistic_effect_references = knowledge['simple_probabilistic_effect_references']
        assert simple_probabilistic_effect_references.transition_function(state=s) == {s * 2: 0.2, s * 3: 0.1}

        combined_probabilistic_effect_references = knowledge['combined_probabilistic_effect_references']
        assert combined_probabilistic_effect_references.transition_function(state=s) == {s * 2: 0.2, s * 3: 0.1}

        conditional_effect_references = knowledge['conditional_effect_references']
        assert conditional_effect_references.transition_function(state=s) == {s * 2: 1.0}
        assert conditional_effect_references.transition_function(state=s2) == {s2 * 3: 0.5, s2 * 2: 0.5}
        assert conditional_effect_references.transition_function(state=s3) == {s3 * 2: 0.2, s3 * 3: 0.1}

        object_effect = knowledge['object_property_conditional']
        color = MDPObject(name="color")
        color.red = 256
        color.green = 0
        color.blue = 0
        oo_state = ObjectOrientedState(objects={color})
        assert object_effect.reward_function(state=oo_state) == 10

        object_conditional_effect = knowledge['object_conditional']
        color = MDPObject(name="color")
        color.red = 256
        color.green = 0
        color.blue = 0
        oo_state = ObjectOrientedState(objects={color})
        assert object_conditional_effect.reward_function(state=oo_state) == 15


    def test_ClassDef(self):
        knowledge = rlang.parse_file("listener_test/tests_resources/valid_examples/classdef.rlang")

        assert knowledge.classes().keys() == {'Color', 'Book', 'AlphaColor', 'Zalpha', 'BlphaColor'}

        color_class = knowledge['Color']

        color_vars = color_class.__dict__.keys()
        assert 'red' in color_vars and 'green' in color_vars and 'blue' in color_vars

        assert color_class.attribute_types == {'red': int, 'green': int, 'blue': int}

        red = color_class('red', 256, 0, 0)
        assert red.name == 'red' and red.red == 256 and red.green == 0 and red.blue == 0

        green = color_class('green', green=256)
        assert green.name == 'green' and green.green == 256

        purple = color_class('purple', 128, blue=128)
        assert purple.red == 128 and purple.blue == 128

        # Test Class inheritance now

        alpha_class = knowledge['AlphaColor']
        alpha = alpha_class('alpha', 0, 0, 0, 256)

        assert alpha.name == 'alpha' and alpha.red == 0 and alpha.green == 0 and alpha.alpha == 256

        semi_transparent = alpha_class('semi', 0, green=0, alpha=5)
        assert semi_transparent.red == 0 and semi_transparent.green == 0 and semi_transparent.alpha == 5

        # This makes sure that inheriting a class doesn't brake it

        blpha_class = knowledge['BlphaColor']
        blpha = blpha_class('blpha', 0, 0, 0, 256)

        assert blpha.name == 'blpha' and blpha.red == 0 and blpha.green == 0 and blpha.blpha == 256

        semi_transparent = blpha_class('semi', 0, green=0, blpha=5)
        assert semi_transparent.red == 0 and semi_transparent.green == 0 and semi_transparent.blpha == 5

        # Test grandchild inheritance

        zalpha_class = knowledge['Zalpha']
        zalpha = zalpha_class('zalpha', 0, 1, 2, 3, 4)

        assert zalpha.red == 0 and zalpha.green == 1 and zalpha.blue == 2 and zalpha.alpha == 3 and zalpha.zalpha == 4

        zeep = zalpha_class('zeep', 2, blue=6, alpha=6, zalpha=7)
        assert zeep.name == 'zeep' and zeep.red == 2 and zeep.blue == 6 and zeep.alpha == 6 and zeep.zalpha == 7

    def test_ObjectDef(self):
        knowledge = rlang.parse_file("listener_test/tests_resources/valid_examples/objectdef.rlang")

        color_class = knowledge['Color']

        red = knowledge['red']
        assert red.red == 256 and red.green == 0 and red.blue == 0

        notebook = knowledge['notebook']
        assert notebook.pages == 15 and notebook.title == red and isinstance(notebook.colors, list)

        sutton_barto = knowledge['sutton_barto']
        assert sutton_barto.pages == 15 and sutton_barto.title == red and sutton_barto.publisher_id == 67

        color_from_state = knowledge['color_from_state']
        assert color_from_state.red(state=VectorState([0, 1, 2])) == 0
        assert color_from_state.green(state=VectorState([0, 1, 2])) == 1
        assert color_from_state.blue(state=VectorState([0, 1, 2])) == 2

        # TODO: Test objects defined in a grounding file


if __name__ == '__main__':
    unittest.main()
    # ListenerTests().test_ClassDef()
