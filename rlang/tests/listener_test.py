from antlr4 import *

from rlang.src.lmdp.grounding.states.StateGroundingClass import StateFactor
from rlang.src.language.RLangLexer import RLangLexer
from rlang.src.language.RLangParser import RLangParser
from rlang.src.language.RLangListener import RLangListener


def listener_from_input(rlang_str):
    rlang = InputStream(rlang_str)
    lexer = RLangLexer(rlang)
    stream = CommonTokenStream(lexer)
    parser = RLangParser(stream)
    tree = parser.program()
    listener = RLangListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener


def test_Factor():
    listener = listener_from_input("Factor position := S[0, 1]")
    position = StateFactor([0, 1], "position")
    assert listener.new_vars['position'] == position


if __name__ == "__main__":
    test_Factor()
