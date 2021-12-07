from __future__ import annotations
import numpy as np
import rlang
from rlang.src.grounding import *


def txest_Effect():
    metadata = MDPMetadata.from_state_action(np.zeros(5), np.zeros(5))
    s = State([0, 1, 2, 3, 4])
    s2 = State([3, 2, 2, 3, 4])
    s3 = State(np.array([[1, 1, 2, 3, 4], [3, 2, 2, 3, 4]]))
    action = Action(1)

    knowledge = rlang.parse_file("tests_resources/valid_examples/effect.rlang", metadata)
    jo = knowledge['jo']
    print(knowledge.predictions(state=s))
    print(knowledge.factors())


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


if __name__ == "__main__":
    txest_Effect()
