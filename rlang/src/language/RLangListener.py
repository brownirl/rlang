from antlr4 import *
from .RLangLexer import RLangLexer
from .RLangParser import RLangParser
from .RLangParserListener import RLangParserListener


class RLangListener(RLangParserListener):
    def __init__(self):
        # RLangListener needs to eventually construct an lmdp object.
        # Statements can be stored in a dict or list until
        # they are packaged into an lmdp object?
        self.statements = []
        pass

    def compileLmdp(self):
        return self.statements
        # Hand out lmdp object here

    def enterProgram(self, ctx: RLangParser.ProgramContext):
        print("Entering Program")
        self.statements.append("Entering Program 2")

    def exitProgram(self, ctx: RLangParser.ProgramContext):
        print("Exiting Program")
        self.statements.append("Exiting Program 2")

    def enterPredicate(self, ctx: RLangParser.PredicateContext):
        print(f"Entering Predicate with ctx: {ctx}")
        self.statements.append("Entering Predicate 2")


def main():
    lexer = RLangLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = RLangParser(stream)
    tree = parser.program()
    listener = RLangListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    statements = listener.compileLmdp()

    print(statements)


if __name__ == '__main__':
    main()
