from antlr4 import CommonTokenStream, InputStream, Token

from rlang.src.language.RLangLexer import RLangLexer


def tokenize_from_string(input_string):
    input_stream = InputStream(input_string)
    lexer = RLangLexer(input_stream)
    # lexer.addErrorListener(MyErrorListener)
    stream = CommonTokenStream(lexer)
    stream.fill()
    return stream.tokens


# All tests must begin with 'test_'


def test_something():
    tokens = tokenize_from_string("Predicate f := True")
    assert len(tokens) == 6
