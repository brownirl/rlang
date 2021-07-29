from antlr4 import *

import sys, os
sys.path.append(os.path.abspath("../"))
from rlang.src.language.RLangLexer import RLangLexer
from rlang.src.language.RLangParser import RLangParser
from antlr4.tree.ParseTreePatternMatcher import ParseTreePatternMatcher
from rlang.src.language.RlangErrorListener import RLangErrorListener
from antlr4.error.Errors import CancellationException
from rlang.src.language.RLangParserListener import RLangParserListener
import io

# from .lexer_test import tokenize_from_string

# All tests must begin with 'test_'

def parser_from_input(input_string):
    input_stream = InputStream(input_string)
    lexer = RLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = RLangParser(stream)
    # parseTree = parser.program()

    # output = io.StringIO()
    # error = io.StringIO()

    parser.removeErrorListeners()
    errorListener = RLangErrorListener()
    parser.addErrorListener(errorListener) 

    return parser, errorListener


def test_Factor(): 
    try:
        parser, errorListener = parser_from_input("Factor position = S[0, 1]")
        tree = parser.factor()
    except CancellationException:
        print("error")
        print(errorListener.symbol)
        # print(parser.getErrorHeader().symbol)



    # assert RLangErrorListener.symbol ==  0

    # print(parseTree.decs().dec(0).factor().getRuleIndex())
    # try:
    #     parseTree = parse_tree_from_input("Factor position = S[0, 1]")
    # except RecognitionException:
    #     print("error")
    # print(parseTree.exception)
    # # print(parseTree.getRuleIndex("Factor"))
    # print(parseTree.toStringTree())
    # print(parseTree)

    # print(type(parseTree))
    # matcher.matchRuleIndex(parseTree, "factor", 5)
    # print(parser.getCurrentToken())
    # print(parser.getExpectedTokensWithinCurrentRule())
    # position = StateFactor([0, 1], "position")

test_Factor()
