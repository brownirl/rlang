from antlr4 import *
from antlr4.error.ErrorStrategy import DefaultErrorStrategy
from antlr4.error.Errors import *

class RLangErrorStrategy(DefaultErrorStrategy):

    def recover(self, recognizer: Parser, e: RecognitionException):
        raise e

    def reportInputMismatch(self, recognizer: Parser, e: InputMismatchException):
        msg = "mismatched input " + recognizer.getTokenErrorDisplay(e.offendingToken)
        msg += " expecting " + e.getExpectedTokens().toString(recognizer.literalNames, recognizer.symbolicNames)
        exception = RecognitionException(msg, recognizer, recognizer.getInputStream(), recognizer._ctx)
        exception.offendingToken = e.offendingToken
        raise exception


class MyErrorStrategy(BailErrorStrategy):
    def recover(self, recognizer:Parser, e:RecognitionException):
        recognizer._errHandler.reportError(recognizer,e)
        super().recover(recognizer,e)