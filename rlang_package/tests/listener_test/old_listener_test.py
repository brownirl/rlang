from __future__ import annotations
import numpy as np
import rlang
from rlang.src.grounding import *


def txest_Effect():
    metadata = MDPMetadata.from_state_action(np.zeros(5), np.zeros(5))
    s = State([0, 1, 2, 3, 4])
    s2 = State([3, 2, 2, 3, 4])
    s3 = State([5, 2, 2, 3, 4])
    # s3 = State(np.array([[1, 1, 2, 3, 4], [3, 2, 2, 3, 4]]))
    # action = Action(1)
    #
    # knowledge = rlang.parse_file("tests_resources/valid_examples/effect.rlang", metadata)
    # jo = knowledge['jo']
    # print(knowledge.predictions(state=s))
    # print(knowledge.factors())

    knowledge = rlang.parse_file("listener_test/tests_resources/valid_examples/effect.rlang", metadata)

    conditional_prediction = knowledge['conditional_prediction']
    f1_prediction = conditional_prediction.prediction_dict['f1'][0]
    f2_prediction = conditional_prediction.prediction_dict['f2'][0]
    print(f1_prediction)
    print(f2_prediction)
    print(f1_prediction(state=s))
    print(f1_prediction(state=s2))
    print(f1_prediction(state=s3))
    print(f2_prediction(state=s))
    print(f2_prediction(state=s2))
    print(f2_prediction(state=s3))
    # print(f2_prediction(state=s3))
    # print({s3[1]: 0.5, s3[1] * 5: 0.3})
    # print({s3[1]: 0.5, s3[1] * 5: 0.3} == {s3[1]: 0.5, s3[1] * 5: 0.3})
    # assert f1_prediction(state=s) == {s[0] * 3: 1.0}
    # assert f1_prediction(state=s2) == {s2[0] * 2: 1.0}

    print(conditional_prediction.predictions)
    # assert f2_prediction(state=s3) == {s3[1]: 0.5, s3[1] * 5: 0.3}


    # print(jo.transition_function(state=s))
    # print(jo.reward_function(state=s2))
    # # jo2 = knowledge['jo2']
    #
    # # print(jo.predictions)
    # print(jo.predictions[0](state=s2))
    # print(jo.predictions[1](state=s))
    # print(jo2.transition_function(state=s))
    # print(jo2.reward_function(state=s))
    # print(jo2.reward_function(state=s2))
    # r = knowledge.reward_function
    # print(r)
    # print(r(state=s, action=action))
    # t = knowledge.transition_function
    # print(t)
    # print(t(state=s, action=action))

#     predictions = knowledge.predictions
#     print(predictions)
#     print(predictions['f1'](state=s))
#     print(predictions['f2'](state=s))


def test_features():
    metadata = MDPMetadata.from_state_action(np.zeros(5), np.zeros(5))
    s = State([0, 1, 2, 3, 4])

    knowledge = rlang.parse('Factor f := S[2:4]\nFeature g := f[1] + f[0]')
    f = knowledge['f']
    g = knowledge['g']
    print(f)
    print(f(state=s))
    print(g)
    print(g(state=s))

def test_prop():
    metadata = MDPMetadata.from_state_action(np.zeros(5), np.zeros(5))
    state = State(np.array([4, 5, 6, 7, 8]))

    knowledge = rlang.parse('Proposition p := S[0] in [1, 4, 2]')
    p = knowledge['p']
    # g = knowledge['g']
    print(p(state=state))


if __name__ == "__main__":
    test_prop()
