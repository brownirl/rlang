from functools import reduce

from antlr4 import *
import json

from lmdp.grounding.states.StateGroundingClass import StateFactor
from lmdp import LMDP
from .RLangLexer import RLangLexer
from .RLangParser import RLangParser
from .RLangParserListener import RLangParserListener
from .VocabularyAssembler import VocabularyAssembler
from .Exceptions import *


class RLangListener(RLangParserListener):
    def __init__(self, lmdp: LMDP = None):
        self.lmdp = lmdp
        self.vocab_fnames = []
        self.grounded_vars = {}
        self.new_vars = {}

    # This function add the lmdp objects in the vocabulary files to self.grounded_vars
    # And probably keep track of object names in the vocab for later reference from the rlang file
    def parseVocabFiles(self):
        def parseVocabFile(fname):
            with open(fname, 'r') as f:
                vocab = json.load(f)
                # I'm not sure if this is best practice, maybe I should make VocabularyAssembler callable
                return VocabularyAssembler(vocab).lmdp_objects

        for fname in self.vocab_fnames:
            self.grounded_vars.update(parseVocabFile(fname))

    def retrieveVariable(self, variable_name):
        if variable_name in self.grounded_vars.keys():
            return self.grounded_vars[variable_name]
        elif variable_name in self.new_vars.keys():
            return self.new_vars[variable_name]
        else:
            raise UnknownVariableError(variable_name)

    def exitProgram(self, ctx: RLangParser.ProgramContext):
        # This is only for DEBUG purposes
        print(f"grounded_vars: {self.grounded_vars}")
        print(f"new_vars: {self.new_vars}")

    def enterImport_stat(self, ctx: RLangParser.Import_statContext):
        self.vocab_fnames.append(ctx.FNAME().getText())

    def exitImports(self, ctx: RLangParser.ImportsContext):
        self.vocab_fnames = list(set(self.vocab_fnames))  # Remove duplicates
        self.parseVocabFiles()

    def exitFactor(self, ctx: RLangParser.FactorContext):
        factor_arg = None
        if ctx.trailer() is not None:
            # TODO: support slice trailers! ctx.trailer() can be an index or a slice
            factor_arg = ctx.trailer().value
        if ctx.array_exp() is not None:
            factor_arg = ctx.array_exp().value

        new_factor = StateFactor(factor_arg, ctx.IDENTIFIER().getText())
        if new_factor.name in self.new_vars.keys() or new_factor.name in self.grounded_vars.keys():
            raise AlreadyBoundError(new_factor.name)
        self.new_vars.update({new_factor.name: new_factor})

    def exitArith_var_with_trailer(self, ctx: RLangParser.Arith_var_with_trailerContext):
        variable = None
        if ctx.IDENTIFIER() is not None:
            variable = self.retrieveVariable(ctx.IDENTIFIER().getText())
        elif ctx.S() is not None:
            # TODO: Support this
            # print(ctx.S())
            pass
        elif ctx.S_PRIME() is not None:
            # TODO: Support this
            # print(ctx.S_PRIME())
            pass
        if ctx.trailer():  # if it's not empty
            trailers = list(map(lambda x: x.value, ctx.trailer()))
            trailers.insert(0, variable)
            indexed_variable = reduce(lambda a, b: a[b], trailers)
            variable = indexed_variable
        ctx.value = variable

    # Exit a parse tree produced by RLangParser#arith_times_divide.
    # def exitArith_times_divide(self, ctx: RLangParser.Arith_times_divideContext):
    #     if ctx.DIVIDE() is not None:
    #         ctx.lhs
    #     print(type(ctx.DIVIDE()))
    #     print(type(ctx.TIMES()))
    #     print(ctx.DIVIDE())
    #     print(ctx.lhs)
    #     print(ctx.rhs)

    def exitTrailer_index(self, ctx: RLangParser.Trailer_indexContext):
        ctx.value = ctx.index_exp().value

    def exitTrailer_slice(self, ctx: RLangParser.Trailer_sliceContext):
        ctx.value = ctx.slice_exp().value

    def exitIndex_exp(self, ctx: RLangParser.Index_expContext):
        ctx.value = ctx.any_integer().value

    def exitArray_exp(self, ctx: RLangParser.Array_expContext):
        ctx.value = list(map(lambda x: x.value, ctx.arr))

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

    def enterAny_num_int(self, ctx: RLangParser.Any_num_intContext):
        ctx.value = ctx.any_integer().value

    def enterAny_num_dec(self, ctx: RLangParser.Any_num_decContext):
        ctx.value = ctx.any_decimal().value

    def enterAny_integer(self, ctx: RLangParser.Any_integerContext):
        ctx.value = int(ctx.getText())

    def enterAny_decimal(self, ctx: RLangParser.Any_decimalContext):
        ctx.value = float(ctx.getText())
