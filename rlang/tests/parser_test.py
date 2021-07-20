from antlr4 import CommonTokenStream, InputStream, Token

from rlang.src.language.RLangLexer import RLangLexer
from rlang.src.language.RLangParser import RLangParser

from .lexer_test import tokenize_from_string

# All tests must begin with 'test_'


def test_something():
    tokens = tokenize_from_string("Predicate f := True")
    assert len(tokens) == 6