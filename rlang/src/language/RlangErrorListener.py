
# from antlr4 import Lexer, Token
# from antlr4.BufferedTokenStream import TokenStream
# from antlr4.Parser import Parser
# from rlang.src.language.RLangLexer import RLangLexer
# from antlr4.InputStream import InputStream
# from antlr4.ParserRuleContext import ParserRuleContext
# from antlr4.Recognizer import Recognizer
# from antlr4.error.ErrorListener import *
# from antlr4.error.Errors import CancellationException, LexerNoViableAltException, NoViableAltException, ParseCancellationException, RecognitionException


# class RLangErrorListener(ErrorListener):
    
#     def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
#         msg = "line " + str(line) + ":" + str(column) + " " + msg
#         raise e
#         # if type(e) == LexerNoViableAltException:
#         #     lexer_no_alt = RLangLexerNoViableAltException(recognizer, recognizer._input,
#         #      recognizer._tokenStartCharIndex, None)
#         #     raise lexer_no_alt
#         # # elif type(e) == NoViableAltException:
#         # #     parser_no_alt = RLangParserNoViableAltException(recognizer, recognizer._input, None, 
#         # #     offendingSymbol, None, recognizer._ctx)
#         # #     raise parser_no_alt
#         # else:
#         #     parse_cancellation = RLangParseCancellationException(msg, offendingSymbol, recognizer, e)
#         #     raise parse_cancellation


# ATNConfigSet = None

# class RLangParserNoViableAltException(NoViableAltException):
#     def __init__(self, recognizer: Parser, input: TokenStream, startToken: Token, offendingToken: Token, deadEndConfigs: ATNConfigSet, ctx: ParserRuleContext):
#         super().__init__(recognizer, input=input, startToken=startToken, offendingToken=offendingToken, deadEndConfigs=deadEndConfigs, ctx=ctx)


# class RLangLexerNoViableAltException(LexerNoViableAltException):
#     def __init__(self, lexer: Lexer, input: InputStream, startIndex: int, deadEndConfigs:ATNConfigSet):
#         super().__init__(lexer, input, startIndex, deadEndConfigs)
    
#     def getOffendingToken(self):
#         symbol = ""
#         if self.startIndex >= 0 and self.startIndex < self.input.size:
#             symbol = self.input.getText(self.startIndex, self.startIndex)
#         return symbol
    

# class RLangParseCancellationException(ParseCancellationException):
#     def __init__(self, msg: str, offendingToken, recognizer:Recognizer=None):
#         super().__init__(msg)
#         self.recognizer = recognizer
#         self.offendingToken = offendingToken
#         self.offendingState = -1
#         self._ctx = recognizer._ctx
#         if recognizer is not None:
#             self.offendingState = recognizer.state

    
#     def getExpectedTokens(self):
#         if self.recognizer is not None:
#             return self.recognizer.atn.getExpectedTokens(self.offendingState, self._ctx)
#         else:
#             return None