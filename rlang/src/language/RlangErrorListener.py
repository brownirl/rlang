from antlr4 import *
from antlr4.error.ErrorListener import *
from antlr4.error.Errors import CancellationException

class RLangErrorListener(ErrorListener):
    def __init__(self):
    #     # self.output = output        
        self._symbol = ''
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):        
        # self.output.write(msg)
        self._symbol = offendingSymbol.text
        raise CancellationException(msg)
    
    @property        
    def symbol(self):
        return self._symbol