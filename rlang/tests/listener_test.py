from antlr4 import *

from rlang.src.language.RLangLexer import RLangLexer
from rlang.src.language.RLangParser import RLangParser
from rlang.src.language.RLangListener import RLangListener


def listener_from_file(rlang_fname):
    rlang = FileStream(rlang_fname)
    lexer = RLangLexer(rlang)
    stream = CommonTokenStream(lexer)
    parser = RLangParser(stream)
    tree = parser.program()
    listener = RLangListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener


def test_Factor():
    pass