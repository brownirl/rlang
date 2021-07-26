from antlr4 import *
import json

from lmdp import LMDP
from .RLangLexer import RLangLexer
from .RLangParser import RLangParser
from .RLangParserListener import RLangParserListener
from .VocabularyAssembler import VocabularyAssembler


class RLangListener(RLangParserListener):
    def __init__(self, lmdp: LMDP):
        # RLangListener needs to eventually construct an lmdp object.
        # Statements can be stored in a dict or list until
        # they are packaged into an lmdp object?
        self.lmdp = lmdp
        self.vocab_fnames = []
        self.grounded_vars = {}
        self.statements = []

    # This function add the lmdp objects in the vocabulary files to self.lmdp
    # And probably keep track of object names in the vocab for later reference from the rlang file
    def parseVocabFiles(self):
        # Parses an actual file
        def parseVocabFile(fname):
            with open(fname, 'r') as f:
                vocab = json.load(f)
                # I'm not sure if this is best practice, maybe I should make VocabularyAssembler callable
                return VocabularyAssembler(vocab).lmdp_objects

        for fname in self.vocab_fnames:
            self.grounded_vars.update(parseVocabFile(fname))

    def enterProgram(self, ctx: RLangParser.ProgramContext):
        print("Entering Program")
        self.statements.append("Entering Program 2")

    def exitProgram(self, ctx: RLangParser.ProgramContext):
        print("Exiting Program")
        self.statements.append("Exiting Program 2")

    # Exit a parse tree produced by RLangParser#imprt.
    def enterImport_stat(self, ctx: RLangParser.Import_statContext):
        self.vocab_fnames.append(ctx.FNAME().getText())

    # Exit a parse tree produced by RLangParser#imprts.
    def exitImports(self, ctx: RLangParser.ImportsContext):
        self.vocab_fnames = list(set(self.vocab_fnames))    # Remove duplicates
        self.parseVocabFiles()

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
