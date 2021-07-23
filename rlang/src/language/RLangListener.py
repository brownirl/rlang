from antlr4 import *

from lmdp import LMDP
from .RLangLexer import RLangLexer
from .RLangParser import RLangParser
from .RLangParserListener import RLangParserListener


class RLangListener(RLangParserListener):
    def __init__(self, lmdp: LMDP):
        # RLangListener needs to eventually construct an lmdp object.
        # Statements can be stored in a dict or list until
        # they are packaged into an lmdp object?
        self.lmdp = lmdp
        self.statements = []

    def enterProgram(self, ctx: RLangParser.ProgramContext):
        print("Entering Program")
        self.statements.append("Entering Program 2")

    def exitProgram(self, ctx: RLangParser.ProgramContext):
        print("Exiting Program")
        self.statements.append("Exiting Program 2")

    # Enter a parse tree produced by RLangParser#vocab.
    def enterVocab(self, ctx: RLangParser.VocabContext):
        print(ctx)
        pass

    # Exit a parse tree produced by RLangParser#vocab.
    def exitVocab(self, ctx: RLangParser.VocabContext):
        print(ctx)
        pass

    def enterPredicate(self, ctx: RLangParser.PredicateContext):
        print(f"Entering Predicate with ctx: {ctx}")
        self.statements.append("Entering Predicate 2")


def main():
    pass
    # lexer = RLangLexer(StdinStream())
    # stream = CommonTokenStream(lexer)
    # parser = RLangParser(stream)
    # tree = parser.program()
    # listener = RLangListener()
    # walker = ParseTreeWalker()
    # walker.walk(listener, tree)

    # statements = listener.compileLmdp()
    #
    # print(statements)


if __name__ == '__main__':
    main()
