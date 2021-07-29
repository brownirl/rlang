import numpy as np
from antlr4 import *

from rlang.src.lmdp.grounding.states.StateGroundingClass import StateFactor, StateFeature
from rlang.src.language.RLangLexer import RLangLexer
from rlang.src.language.RLangParser import RLangParser
from rlang.src.language.RLangListener import RLangListener


# TODO: replace state_size with a more comprehensive MDP parameter object
def listener_from_input(rlang_str, state_size=None):
    rlang = InputStream(rlang_str)
    lexer = RLangLexer(rlang)
    stream = CommonTokenStream(lexer)
    parser = RLangParser(stream)
    tree = parser.program()
    listener = RLangListener()
    listener.state_size = state_size
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener


def test_Factor():
    position_parsed = listener_from_input("Factor position := S", 3).new_vars['position']
    position = StateFactor([0, 1, 2], "position")
    assert position_parsed == position
    assert position_parsed(np.array([5, 6, 7])) == position(np.array([5, 6, 7]))

    position_parsed = listener_from_input("Factor position := S[0]").new_vars['position']
    position = StateFactor([0], "position")
    assert position_parsed == position
    assert position_parsed(np.array([5, 6, 7])) == position(np.array([5, 6, 7]))

    position_parsed = listener_from_input("Factor position := S[0, 3, 2]").new_vars['position']
    position = StateFactor([0, 3, 2], "position")
    assert position_parsed == position
    assert position_parsed(np.array([5, 6, 7, 8, 9])) == position(np.array([5, 6, 7, 8, 9]))

    # TODO: Support slices
    # position_parsed = listener_from_input("Factor position := S[0:2]").new_vars['position']
    # position = StateFactor([0:2], "position")
    # assert position_parsed == position
    # assert position_parsed(np.array([5, 6, 7, 8, 9])) == position(np.array([5, 6, 7, 8, 9]))


def test_Feature():
    x_parsed = listener_from_input("Factor position := S[0, 1]\nFeature x := position[0]").new_vars['x']
    position = StateFactor([0, 1], "position")
    x = StateFeature(position[0], 1)
    assert x_parsed == x
    assert x_parsed(np.array([5, 6, 7])) == x(np.array([5, 6, 7]))

    # TODO: Support S, A, S' parsing for Feature
    # x_parsed = listener_from_input("Feature x := S", 3).new_vars['x']
    # x_parsed = listener_from_input("Feature x := A", 3).new_vars['x']
    # x_parsed = listener_from_input("Feature x := S'", 3).new_vars['x']

    x_parsed = listener_from_input("Factor position := S[0, 1]\nFeature x := position[0] + 4 * 2 + position[1]").new_vars['x']
    position = StateFactor([0, 1], "position")
    x = StateFeature(position[0] + 4 * 2 + position[1], 1)
    assert x_parsed == x
    assert x_parsed(np.array([5, 6, 7])) == x(np.array([5, 6, 7]))


def test_Predicate():
    pass


if __name__ == "__main__":
    test_Feature()
