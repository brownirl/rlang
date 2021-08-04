from antlr4 import *
from antlr4.error.ErrorListener import *
from antlr4.error.Errors import CancellationException

class RLangErrorListener(ErrorListener):
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        msg = "line " + str(line) + ":" + str(column) + " " + msg
        re = RecognitionException(msg, recognizer, recognizer.getInputStream(), recognizer._ctx)
        re.offendingToken = offendingSymbol
        raise re