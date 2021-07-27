from antlr4 import *
import json

from lmdp.grounding.states.StateGroundingClass import StateFactor
from lmdp import LMDP
from .RLangLexer import RLangLexer
from .RLangParser import RLangParser
from .RLangParserListener import RLangParserListener
from .VocabularyAssembler import VocabularyAssembler


class RLangListener(RLangParserListener):
    def __init__(self, lmdp: LMDP = None):
        # RLangListener needs to eventually construct an lmdp object.
        # Statements can be stored in a dict or list until
        # they are packaged into an lmdp object?
        self.lmdp = lmdp
        self.vocab_fnames = []
        self.grounded_vars = {}
        self.new_vars = {}

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

    # Exit a parse tree produced by RLangParser#imprt.
    def enterImport_stat(self, ctx: RLangParser.Import_statContext):
        self.vocab_fnames.append(ctx.FNAME().getText())

    # Exit a parse tree produced by RLangParser#imprts.
    def exitImports(self, ctx: RLangParser.ImportsContext):
        self.vocab_fnames = list(set(self.vocab_fnames))  # Remove duplicates
        self.parseVocabFiles()

    # Enter a parse tree produced by RLangParser#factor.
    def exitFactor(self, ctx: RLangParser.FactorContext):
        new_factor = StateFactor(ctx.trailer().value, ctx.IDENTIFIER().getText())
        # TODO: should be some check that we are not over-writing an existing variable
        # TODO: support slice trailers!
        self.new_vars.update({new_factor.name: new_factor})

    # Exit a parse tree produced by RLangParser#array.
    def exitArray(self, ctx: RLangParser.ArrayContext):
        ctx.value = ctx.array_exp().value

    # Exit a parse tree produced by RLangParser#slice.
    def exitSlice(self, ctx: RLangParser.SliceContext):
        ctx.value = ctx.slice_exp().value

    # Exit a parse tree produced by RLangParser#array_exp.
    def exitArray_exp(self, ctx: RLangParser.Array_expContext):
        ctx.value = list(map(lambda x: x.value, ctx.arr))

    # Exit a parse tree produced by RLangParser#slice_exp.
    def exitSlice_exp(self, ctx: RLangParser.Slice_expContext):
        start_ind = None
        stop_ind = None
        step_size = 1
        if isinstance(ctx.start_ind, RLangParser.Any_integerContext):
            start_ind = ctx.start_ind.value

        if isinstance(ctx.stop_ind, RLangParser.Any_integerContext):
            stop_ind = ctx.stop_ind.value
        slc = slice(start_ind, stop_ind, step_size)
        ctx.value = slc

    # Enter a parse tree produced by RLangParser#any_integer.
    def enterAny_integer(self, ctx: RLangParser.Any_integerContext):
        ctx.value = int(ctx.getText())


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
