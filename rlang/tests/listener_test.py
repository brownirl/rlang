from __future__ import annotations
import unittest
import numpy as np
import rlang
from rlang.src.grounding import *

class listenerTests(unittest.TestCase):

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

        # QUESTION: is more complex indexing allowed? Like Factor test3 := S[5:-1], Factor test4 := S[:]
        # position_parsed = rlang.parse("Factor position := S[:-1]", metadata)['position']
        # print(position_parsed(state=state2))


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

        x_parsed = rlang.parse("Feature x := [[[2, 1]]] * 2 * S[0]", metadata)['x']
        position = Factor([0], "position")
        #QUESTION: Why does this line error?
        # x = Feature([[[2, 1]]] * 2 * position, "x")
        # print(x(state=state))
        # print(x_parsed(state=state))

        x_parsed = rlang.parse("Factor position := S[0, 1]\nFeature x := position[0] + position[1]", metadata)['x']
        assert (x_parsed(state=state)) == 9

        x_parsed = rlang.parse("Factor position := S[0, 1]\nFeature x := position[0]\nFeature y := position[1]/x", metadata)['y']
        assert (x_parsed(state=state)) == 5/4
    
    def test_Predicate(self):
        metadata = MDPMetadata.from_state_action(np.zeros(5), np.zeros(5))
        state = State(np.array([4, 5, 6, 7, 8]))

        hi_parsed = rlang.parse("Factor position := S[0, 1]\nFeature x := position[0]\nPredicate hi := x == 1 and True or False", metadata)['hi']
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
        # print(x_parsed(state=state2))
        #QUESTION: why is this true because isn't [1, 6] not in the array
        assert x_parsed(state=state2) == [[True]]

        state2 = State(np.array([[0, 1], [5, 6]]))
        x_parsed = rlang.parse("Predicate x := S[0] == [[0], [5]]", metadata)['x']
        assert ((x_parsed(state=state2)) == [[True], [True]]).all()

        state2 = State(np.array([[0, 1], [5, 6]]))
        x_parsed = rlang.parse("Predicate x := S[0] == [[0], [1]]", metadata)['x']
        assert ((x_parsed(state=state2)) == [[True], [False]]).all()

        #QUESTION: just to confirm, we cannot compare between instances of PrimitiveGroundings
        # x_parsed = rlang.parse("Factor position := S[0, 1]\nFeature x := position[0]\nFeature y := position[0]\nPredicate test3 := x < y", metadata)['x']
        # print(x_parsed(state=state2))

        #QUESTION: how to compare S and S'

        #QUESTION: can you create a predicate with action
        # up_parsed = rlang.parse("Action up := -1.3\nPredicate x := up == -1.3", metadata)['x']
        # print(up_parsed(state=state2))


    def test_Action(self):
        metadata = MDPMetadata.from_state_action(np.zeros(5), np.zeros(5))

        up_parsed = rlang.parse("Action up := -1.3", metadata)['up']
        up = ActionReference(-1.3, "up")
        assert up() == up_parsed()

        up_parsed = rlang.parse("Action up := [0, 1.0, -4.2]", metadata)['up']
        up = ActionReference([0, 1.0, -4.2], "up")
        assert (up() == up_parsed()).all()

if __name__ == '__main__':
    unittest.main()
