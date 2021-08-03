from antlr4 import *
from antlr4.error.ErrorListener import *
from antlr4.error.Errors import CancellationException

class RLangErrorListener(ErrorListener):
    # def __init__(self):       
    #     self._symbol = ''
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        msg = "line " + str(line) + ":" + str(column) + " " + msg
        re = RecognitionException(msg, recognizer, recognizer.getInputStream(), recognizer._ctx)
        re.offendingToken = offendingSymbol
        raise re
    # @property        
    # def symbol(self):
    #     return self._symbol