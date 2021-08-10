from antlr4.error.Errors import RecognitionException
from antlr4.error.ErrorListener import *

class RLangErrorListener(ErrorListener):
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        msg = "line " + str(line) + ":" + str(column) + " " + msg
        if e == None:
            e = RecognitionException(None, recognizer, recognizer.getInputStream(), recognizer._ctx)
            e.offendingToken = offendingSymbol
        raise Exception(e, msg)