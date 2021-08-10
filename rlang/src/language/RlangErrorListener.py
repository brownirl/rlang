from antlr4.error.ErrorListener import *

class RLangErrorListener(ErrorListener):
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        msg = "line " + str(line) + ":" + str(column) + " " + msg
        raise Exception(e, msg)