from antlr4.error.ErrorStrategy import DefaultErrorStrategy
from antlr4.Parser import Parser
from antlr4.error.Errors import InputMismatchException, NoViableAltException, ParseCancellationException, RecognitionException

class RLangErrorStrategy(DefaultErrorStrategy):
    def __init__(self):
        super().__init__()
    
    def recoverInline(self, recognizer: Parser):
        self.reportError(recognizer, InputMismatchException(recognizer))
        # raise InputMismatchException(recognizer)

    def sync(self, recognizer: Parser):
        # pass
        try:
            super().sync(recognizer)
        except InputMismatchException as e:
            # self.recoverInline(recognizer)
            print("caught")
            self.reportInputMismatch(recognizer, e)