from antlr4.error.Errors import RecognitionException
from antlr4.error.ErrorListener import *
from .Exceptions import RLangParseCancellationException


class RLangErrorListener(ErrorListener):
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        msg = "line " + str(line) + ":" + str(column) + " " + msg
        if e is None:
            e = RecognitionException(msg, recognizer, recognizer.getInputStream(), recognizer._ctx)
            e.offendingToken = offendingSymbol  
        raise RLangParseCancellationException(e, msg)
