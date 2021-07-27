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
        # RLangListener needs to eventually construct an lmdp object.
        # Statements can be stored in a dict or list until
        # they are packaged into an lmdp object?
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

    # Exit a parse tree produced by RLangParser#program.
    def exitProgram(self, ctx: RLangParser.ProgramContext):
        # This is only for DEBUG purposes
        print(f"grounded_vars: {self.grounded_vars}")
        print(f"new_vars: {self.new_vars}")

    # Enter a parse tree produced by RLangParser#imprt.
    def enterImport_stat(self, ctx: RLangParser.Import_statContext):
        self.vocab_fnames.append(ctx.FNAME().getText())

    # Exit a parse tree produced by RLangParser#imprts.
    def exitImports(self, ctx: RLangParser.ImportsContext):
        self.vocab_fnames = list(set(self.vocab_fnames))  # Remove duplicates
        self.parseVocabFiles()

    # Exit a parse tree produced by RLangParser#factor.
    def exitFactor(self, ctx: RLangParser.FactorContext):
        new_factor = StateFactor(ctx.trailer().value, ctx.IDENTIFIER().getText())
        # TODO: support slice trailers!
        if new_factor.name in self.new_vars.keys() or new_factor.name in self.grounded_vars.keys():
            raise AlreadyBoundError(new_factor.name)
        self.new_vars.update({new_factor.name: new_factor})

    # Enter a parse tree produced by RLangParser#arith_number.
    def enterArith_number(self, ctx: RLangParser.Arith_numberContext):
        pass

    # Exit a parse tree produced by RLangParser#arith_number.
    def exitArith_number(self, ctx: RLangParser.Arith_numberContext):
        pass

    # Enter a parse tree produced by RLangParser#arith_plus_minus.
    def enterArith_plus_minus(self, ctx: RLangParser.Arith_plus_minusContext):
        pass

    # Exit a parse tree produced by RLangParser#arith_plus_minus.
    def exitArith_plus_minus(self, ctx: RLangParser.Arith_plus_minusContext):
        pass

    # Enter a parse tree produced by RLangParser#arith_var_with_trailer.
    def enterArith_var_with_trailer(self, ctx: RLangParser.Arith_var_with_trailerContext):
        pass

    # # Exit a parse tree produced by RLangParser#arith_var_with_trailer.
    # def exitArith_var_with_trailer(self, ctx: RLangParser.Arith_var_with_trailerContext):
    #     variable = None
    #     if ctx.IDENTIFIER() is not None:
    #         variable = self.retrieveVariable(ctx.IDENTIFIER().getText())
    #     elif ctx.S() is not None:
    #         print(ctx.S())
    #     elif ctx.S_PRIME() is not None:
    #         print(ctx.S_PRIME())
    #     print(variable)
    #     print(ctx.trailer())
    #     if ctx.trailer():   # if it's not empty
    #         print(ctx.trailer()[0].value)
    #     else:
    #         ctx.value = variable

    # Enter a parse tree produced by RLangParser#arith_paren.
    def enterArith_paren(self, ctx: RLangParser.Arith_parenContext):
        pass

    # Exit a parse tree produced by RLangParser#arith_paren.
    def exitArith_paren(self, ctx: RLangParser.Arith_parenContext):
        pass

    # Enter a parse tree produced by RLangParser#arith_times_divide.
    def enterArith_times_divide(self, ctx: RLangParser.Arith_times_divideContext):
        pass

    # Exit a parse tree produced by RLangParser#arith_times_divide.
    # def exitArith_times_divide(self, ctx: RLangParser.Arith_times_divideContext):
    #     if ctx.DIVIDE() is not None:
    #         ctx.lhs
    #     print(type(ctx.DIVIDE()))
    #     print(type(ctx.TIMES()))
    #     print(ctx.DIVIDE())
    #     print(ctx.lhs)
    #     print(ctx.rhs)

    def exitTrailer_array(self, ctx: RLangParser.Trailer_arrayContext):
        ctx.value = ctx.array_exp().value

    def exitTrailer_slice(self, ctx: RLangParser.Trailer_sliceContext):
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

    # Enter a parse tree produced by RLangParser#any_decimal.
    def enterAny_decimal(self, ctx: RLangParser.Any_decimalContext):
        ctx.value = float(ctx.getText())
