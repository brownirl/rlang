from antlr4 import CommonTokenStream, InputStream, Token

from rlang.src.language.RLangLexer import RLangLexer
from rlang.src.language.RLangParser import RLangParser


def parse_from_string(input_string):
    input_stream = InputStream(input_string)
    lexer = RLangLexer(input_stream)
    # lexer.addErrorListener(MyErrorListener)
    stream = CommonTokenStream(lexer)
    parser = RLangParser(stream)
    tree = parser.program()
    return tree

# All tests must begin with 'test_'


def test_something():
    tree = parse_from_string("Predicate f := True")
    print(dir(tree))
    print(tree.toStringTree())


if __name__ == "__main__":
    test_something()