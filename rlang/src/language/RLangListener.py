import types
from functools import reduce

import numpy as np
from antlr4 import *
import json

from lmdp.grounding.states import Predicate
from lmdp.grounding.booleans.BooleanFunClass import BOOL_TRUE, BOOL_FALSE
from lmdp.grounding.real.RealExpressionClass import RealConstant, RealExpression
from lmdp.grounding.expressions.ExpressionsClass import S, A, S_prime
from lmdp.grounding.states.StateGroundingClass import StateFactor, StateFeature
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
        self.state_size = None  # TODO: Refactor this with dataclass about the MDP

    # This function add the lmdp objects in the vocabulary files to self.grounded_vars
    # And probably keep track of object names in the vocab for later reference from the rlang file
    def parseVocabFiles(self):
        def parseVocabFile(fname):
            with open(fname, 'r') as f:
                vocab = json.load(f)
                # I'm not sure if this is best practice, maybe I should make VocabularyAssembler callable
                voc_assembler = VocabularyAssembler(vocab)
                self.grounded_vars.update(voc_assembler.lmdp_objects)
                self.state_size = voc_assembler.state_size

        for fname in self.vocab_fnames:
            parseVocabFile(fname)

    def retrieveVariable(self, variable_name):
        if variable_name in self.grounded_vars.keys():
            return self.grounded_vars[variable_name]
        elif variable_name in self.new_vars.keys():
            return self.new_vars[variable_name]
        else:
            raise UnknownVariableError(variable_name)

    def addVariable(self, variable_name, variable):
        if variable_name in self.new_vars.keys() or variable_name in self.grounded_vars.keys():
            raise AlreadyBoundError(variable_name)
        self.new_vars.update({variable_name: variable})

    def exitProgram(self, ctx: RLangParser.ProgramContext):
        # This is only for DEBUG purposes
        print(f"grounded_vars: {self.grounded_vars}")
        print(f"new_vars: {self.new_vars}")
        print(self.new_vars['position'](np.array([0, 0, 0, 0])))
        print(self.new_vars['x'](np.array([0, 0, 0, 0])))

    def enterImport_stat(self, ctx: RLangParser.Import_statContext):
        self.vocab_fnames.append(ctx.FNAME().getText())

    def exitImports(self, ctx: RLangParser.ImportsContext):
        self.vocab_fnames = list(set(self.vocab_fnames))  # Remove duplicates
        self.parseVocabFiles()

    def exitFactor(self, ctx: RLangParser.FactorContext):
        feature_positions = None
        if ctx.trailer() is not None:
            # TODO: support slice trailers! ctx.trailer() can be an index or a slice
            feature_positions = ctx.trailer().value
        if ctx.array_exp() is not None:
            feature_positions = ctx.array_exp().value
        new_factor = StateFactor(feature_positions, name=ctx.IDENTIFIER().getText())
        self.addVariable(new_factor.name, new_factor)

    def exitFeature(self, ctx: RLangParser.FeatureContext):
        arith_exp = ctx.arithmetic_exp().value
        new_feature = None
        if isinstance(arith_exp, StateFactor):
            # TODO: Fix this wrapping code, it does not work
            new_feature = StateFeature(lambda **args: arith_exp(args), arith_exp.number_of_features(),
                                       variables=arith_exp.variables(), name=ctx.IDENTIFIER().getText())
        elif isinstance(arith_exp, types.FunctionType):
            # TODO: Keep track of size of arith_exp for number_of_features. hardcoded to 1
            new_feature = StateFeature(arith_exp, 1, name=ctx.IDENTIFIER().getText())

        self.addVariable(ctx.IDENTIFIER().getText(), new_feature)

    def exitPredicate(self, ctx: RLangParser.PredicateContext):
        new_predicate = Predicate(ctx.boolean_exp().value, name=ctx.IDENTIFIER().getText())
        self.addVariable(ctx.IDENTIFIER().getText(), new_predicate)
        print(type(new_predicate))

    def exitArith_paren(self, ctx: RLangParser.Arith_parenContext):
        ctx.value = ctx.arithmetic_exp().value

    def exitArith_times_divide(self, ctx: RLangParser.Arith_times_divideContext):
        operation = None
        if ctx.TIMES() is not None:
            operation = lambda a, b: a * b
        elif ctx.DIVIDE() is not None:
            operation = lambda a, b: a / b
        ctx.value = lambda **args: operation(ctx.lhs.value(args), ctx.rhs.value(args))

    def exitArith_plus_minus(self, ctx: RLangParser.Arith_plus_minusContext):
        operation = None
        if ctx.PLUS() is not None:
            operation = lambda a, b: a + b
        elif ctx.MINUS() is not None:
            operation = lambda a, b: a - b
        ctx.value = lambda **args: operation(ctx.lhs.value(args), ctx.rhs.value(args))

    def exitArith_number(self, ctx: RLangParser.Arith_numberContext):
        ctx.value = ctx.any_number().value

    def exitArith_bound_var(self, ctx: RLangParser.Arith_bound_varContext):
        ctx.value = ctx.any_bound_var().value

    def exitBool_paren(self, ctx: RLangParser.Bool_parenContext):
        ctx.value = ctx.boolean_exp().value

    def exitBool_and(self, ctx: RLangParser.Bool_andContext):
        ctx.value = ctx.lhs.value and ctx.rhs.value

    def exitBool_or(self, ctx: RLangParser.Bool_orContext):
        ctx.value = ctx.lhs.value or ctx.rhs.value

    def exitBool_not(self, ctx: RLangParser.Bool_notContext):
        ctx.value = not ctx.boolean_exp().value

    def exitBool_in(self, ctx: RLangParser.Bool_inContext):
        # TODO: Investigate StateFactor .in_ method
        lhs = None
        rhs = None
        if ctx.lhs_arr is not None:
            lhs = ctx.lhs_arr.value
        elif ctx.lhs_arith is not None:
            lhs = ctx.lhs_arith.value
        if ctx.rhs_arr is not None:
            rhs = ctx.rhs_arr.value
        elif ctx.rhs_bound_var is not None:
            rhs = ctx.rhs_bound_var.value
        # print(lhs)
        # print(rhs)

    def exitBool_bool_eq(self, ctx: RLangParser.Bool_bool_eqContext):
        # TODO: Should ctx.value be a callable here as well? Check BooleanFunClass.py
        bool_operation = None
        if ctx.EQ_TO() is not None:
            bool_operation = lambda a, b: a == b
        elif ctx.NOT_EQ() is not None:
            bool_operation = lambda a, b: a != b
        ctx.value = lambda **args: bool_operation(ctx.lhs.value(args), ctx.rhs.value(args))

    def exitBool_arith_eq(self, ctx: RLangParser.Bool_arith_eqContext):
        # TODO: Should ctx.value be a callable lambda function? A RealExpression?
        bool_operation = None
        if ctx.EQ_TO() is not None:
            bool_operation = lambda a, b: a == b
        elif ctx.LT() is not None:
            bool_operation = lambda a, b: a < b
        elif ctx.GT() is not None:
            bool_operation = lambda a, b: a > b
        elif ctx.LT_EQ() is not None:
            bool_operation = lambda a, b: a <= b
        elif ctx.GT_EQ() is not None:
            bool_operation = lambda a, b: a >= b
        elif ctx.NOT_EQ() is not None:
            bool_operation = lambda a, b: a != b
        # TODO: What about if ctx.lhs.value is a StateFeature and needs a state variable?
        print(type(ctx.lhs.value))
        print(type(ctx.rhs.value))
        # TODO: This breaks with function and RealExpression
        ctx.value = lambda **args: bool_operation(ctx.lhs.value(args), ctx.rhs.value(args))

    def exitBool_bound_var(self, ctx: RLangParser.Bool_bound_varContext):
        ctx.value = ctx.any_bound_var().value

    def exitBool_tf(self, ctx: RLangParser.Bool_tfContext):
        if ctx.TRUE() is not None:
            ctx.value = BOOL_TRUE
        elif ctx.FALSE() is not None:
            ctx.value = BOOL_FALSE

    def exitAny_bound_var(self, ctx: RLangParser.Any_bound_varContext):
        variable = None
        if ctx.IDENTIFIER() is not None:
            variable = self.retrieveVariable(ctx.IDENTIFIER().getText())
        elif ctx.S() is not None:
            # TODO: Support this
            variable = S
            pass
        elif ctx.S_PRIME() is not None:
            # TODO: Support this
            variable = S_prime
            pass
        elif ctx.A() is not None:
            # TODO: Support this
            variable = A
        if ctx.trailer():  # if it's not empty
            trailers = list(map(lambda x: x.value, ctx.trailer()))
            trailers.insert(0, variable)
            # TODO: this needs to change based on type(variable)
            # print(variable)
            # print(trailers)
            indexed_variable = reduce(lambda a, b: a[b], trailers)
            variable = indexed_variable
        ctx.value = variable
        # print(type(variable))

    def exitTrailer_index(self, ctx: RLangParser.Trailer_indexContext):
        ctx.value = ctx.index_exp().value

    def exitTrailer_slice(self, ctx: RLangParser.Trailer_sliceContext):
        ctx.value = ctx.slice_exp().value

    def exitIndex_exp(self, ctx: RLangParser.Index_expContext):
        ctx.value = ctx.any_integer().value()

    def exitArray_exp(self, ctx: RLangParser.Array_expContext):
        ctx.value = list(map(lambda x: x.value(), ctx.arr))

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

    def exitAny_num_int(self, ctx: RLangParser.Any_num_intContext):
        ctx.value = ctx.any_integer().value

    def exitAny_num_dec(self, ctx: RLangParser.Any_num_decContext):
        ctx.value = ctx.any_decimal().value

    def enterAny_integer(self, ctx: RLangParser.Any_integerContext):
        ctx.value = RealConstant(int(ctx.getText()))

    def enterAny_decimal(self, ctx: RLangParser.Any_decimalContext):
        ctx.value = RealConstant(float(ctx.getText()))
