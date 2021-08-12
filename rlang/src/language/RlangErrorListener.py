from antlr4.error.Errors import CancellationException, ParseCancellationException, RecognitionException
from antlr4.error.ErrorListener import *

class RLangErrorListener(ErrorListener):
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        msg = "line " + str(line) + ":" + str(column) + " " + msg
        if e is None:
            e = RecognitionException(msg, recognizer, recognizer.getInputStream(), recognizer._ctx)
            e.offendingToken = offendingSymbol  
        raise RLangException(e, msg)

class RLangException(ParseCancellationException):
    def __init__(self, e, msg: str):
        super().__init__(msg)
        self.e = e