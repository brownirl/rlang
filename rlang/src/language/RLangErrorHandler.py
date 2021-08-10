from antlr4 import Parser
from antlr4.error.Errors import InputMismatchException, RecognitionException
from antlr4.error.ErrorStrategy import DefaultErrorStrategy

class RLangErrorHandler(DefaultErrorStrategy):
    def __init__(self) -> None:
        super().__init__()

    def recover(self, recognizer:Parser, e:RecognitionException):
        context = recognizer._ctx
        while context is not None:
            context.exception = e
            context = context.parentCtx
        raise e
#     #
    def recoverInline(self, recognizer:Parser):
        self.recover(recognizer, InputMismatchException(recognizer))

    def reportUnwantedToken(self, recognizer:Parser):
        if self.inErrorRecoveryMode(recognizer):
            return

        self.beginErrorCondition(recognizer)
        t = recognizer.getCurrentToken()
        tokenName = self.getTokenErrorDisplay(t)
        expecting = self.getExpectedTokens(recognizer)
        msg = "extraneous input " + tokenName + " expecting " \
            + expecting.toString(recognizer.literalNames, recognizer.symbolicNames)
        e = RecognitionException(msg, recognizer, t)
        e.offendingToken = t
        recognizer.notifyErrorListeners(msg, t, e)
        raise e