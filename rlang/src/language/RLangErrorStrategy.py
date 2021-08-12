from antlr4.error.ErrorStrategy import DefaultErrorStrategy
from antlr4.Parser import Parser
from antlr4.error.Errors import InputMismatchException, ParseCancellationException, RecognitionException

class RLangErrorStrategy(DefaultErrorStrategy):
    def __init__(self):
        super().__init__()
    
    def recoverInline(self, recognizer: Parser):
        self.reportError(recognizer, InputMismatchException(recognizer))
        # raise InputMismatchException(recognizer)

    def sync(self, recognizer: Parser):
        pass