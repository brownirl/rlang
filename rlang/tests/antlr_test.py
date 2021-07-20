from antlr4 import CommonTokenStream, InputStream, Token
from rlang.src.language.RLangLexer import RLangLexer
from rlang.src.language.RLangParser import RLangParser
# from mytool.parsers.error_listener import MyErrorListener


# def getTokensFromText(input_string):
#     input_stream = InputStream(input_string)
#     lexer = RLangLexer(input_stream)
#     # lexer.addErrorListener(MyErrorListener)
#     stream = CommonTokenStream(lexer)
#     stream.fill()
#     return stream.tokens
#
#
# def test_lexer_bad_input():
#     tokens = getTokensFromText("Fig :=")  # assumes MyLexer won't detect/parse "function ()"
#     assert len(tokens) == 1
#     # self.assertEqual(1, len(tokens))  # // includes EOF
#     # self.assertEqual(Token.EOF, tokens[0].type)

def test_heee():
    assert True

def test_hooo():
    assert True