from antlr4 import Parser
from antlr4.Recognizer import Recognizer
from antlr4.Token import Token
from antlr4.error.Errors import InputMismatchException, NoViableAltException, ParseCancellationException, RecognitionException
from antlr4.error.ErrorStrategy import DefaultErrorStrategy

class RLangErrorHandler(DefaultErrorStrategy):
    def __init__(self) -> None:
        super().__init__()

    def recover(self, recognizer:Parser, e:RecognitionException):
        raise e

    def reportNoViableAlternative(self, recognizer:Parser, e:NoViableAltException):
        tokens = recognizer.getTokenStream()
        if tokens is not None:
            if e.startToken.type==Token.EOF:
                input = "<EOF>"
            else:
                input = tokens.getText(e.startToken, e.offendingToken)
        else:
            input = "<unknown input>"
        msg = "no viable alternative at input " + self.escapeWSAndQuote(input)
        print(e.recognizer._ctx)
        recognizer.notifyErrorListeners(msg, e.offendingToken, e)
        raise e

    def reportUnwantedToken(self, recognizer:Parser):
        if self.inErrorRecoveryMode(recognizer):
            return

        self.beginErrorCondition(recognizer)
        t = recognizer.getCurrentToken()
        tokenName = self.getTokenErrorDisplay(t)
        expecting = self.getExpectedTokens(recognizer)
        msg = "extraneous input " + tokenName + " expecting " \
            + expecting.toString(recognizer.literalNames, recognizer.symbolicNames)
        recognizer.notifyErrorListeners(msg, t, None)
        raise UnwantedTokenException(msg, recognizer, t)
    
    def reportInputMismatch(self, recognizer:Parser, e:InputMismatchException):
        msg = "mismatched input " + self.getTokenErrorDisplay(e.offendingToken) \
              + " expecting " + e.getExpectedTokens().toString(recognizer.literalNames, recognizer.symbolicNames)
        recognizer.notifyErrorListeners(msg, e.offendingToken, e)
        raise e

    def reportFailedPredicate(self, recognizer, e):
        ruleName = recognizer.ruleNames[recognizer._ctx.getRuleIndex()]
        msg = "rule " + ruleName + " " + e.message
        recognizer.notifyErrorListeners(msg, e.offendingToken, e)
        raise e

    def reportMissingToken(self, recognizer):
        if self.inErrorRecoveryMode(recognizer):
            return
        self.beginErrorCondition(recognizer)
        t = recognizer.getCurrentToken()
        expecting = self.getExpectedTokens(recognizer)
        msg = "missing " + expecting.toString(recognizer.literalNames, recognizer.symbolicNames) \
              + " at " + self.getTokenErrorDisplay(t)
        recognizer.notifyErrorListeners(msg, t, None)
        raise MissingTokenException(msg, recognizer, t)


class UnwantedTokenException(RecognitionException):
    def __init__(self, message: str, recognizer: Recognizer, offendingToken: None):
        super().__init__(message=message, recognizer=recognizer, input=recognizer.getInputStream(), ctx=recognizer._ctx)
        self.offendingToken = offendingToken

class MissingTokenException(RecognitionException):
    def __init__(self, message: str, recognizer: Recognizer, offendingToken: None):
        super().__init__(message=message, recognizer=recognizer, input=recognizer.getInputStream(), ctx=recognizer._ctx)
        self.offendingToken = offendingToken