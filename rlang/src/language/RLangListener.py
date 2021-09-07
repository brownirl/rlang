import types
from functools import reduce
import numpy as np
from antlr4 import *
import json
from typing import Callable

from rlang.src.grounding.utils.state_space import MDPMetadata
from rlang.src.grounding.groundings.state.state_grounding_function import StateGroundingFunction
from rlang.src.grounding import *

from .RLangLexer import RLangLexer
from .RLangParser import RLangParser
from .RLangParserListener import RLangParserListener
from .VocabularyAssembler import VocabularyAssembler
from .Exceptions import *


class RLangListener(RLangParserListener):
    def __init__(self, mdp_metadata: MDPMetadata = None):
        self.vocab_fnames = []
        self.grounded_vars = {}
        self.rlang_knowledge = RLangKnowledge()
        self.mdp_metadata = mdp_metadata

    # This function add the lmdp objects in the vocabulary files to self.grounded_vars
    # And probably keep track of object names in the vocab for later reference from the rlang file
    def parseVocabFiles(self):
        def parseVocabFile(fname):
            with open(fname, 'r') as f:
                vocab = json.load(f)
                # I'm not sure if this is best practice, maybe I should make VocabularyAssembler callable
                voc_assembler = VocabularyAssembler(vocab)
                self.grounded_vars.update(voc_assembler.lmdp_objects)
                # self.state_size = voc_assembler.state_size

        for fname in self.vocab_fnames:
            parseVocabFile(fname)

    def retrieveVariable(self, variable_name):
        if variable_name in self.grounded_vars.keys():
            return self.grounded_vars[variable_name]
        elif variable_name in self.rlang_knowledge.keys():
            return self.rlang_knowledge[variable_name]
        else:
            raise UnknownVariableError(variable_name)

    def addVariable(self, variable_name, variable):
        if variable_name in self.rlang_knowledge.keys() or variable_name in self.grounded_vars.keys():
            raise AlreadyBoundError(variable_name)
        self.rlang_knowledge.update({variable_name: variable})

    def enterImport_stat(self, ctx: RLangParser.Import_statContext):
        self.vocab_fnames.append(ctx.FNAME().getText())

    def exitImports(self, ctx: RLangParser.ImportsContext):
        self.vocab_fnames = list(set(self.vocab_fnames))  # Remove duplicates
        self.parseVocabFiles()

    def exitFactor(self, ctx: RLangParser.FactorContext):
        feature_positions = list(range(self.mdp_metadata.state_space.shape[0]))
        if ctx.trailer() is not None:
            if isinstance(ctx.trailer().value, slice):
                feature_positions = list(range(self.mdp_metadata.state_space.shape[0]))[ctx.trailer().value]
            else:
                feature_positions = ctx.trailer().value
        new_factor = Factor(feature_positions, name=ctx.IDENTIFIER().getText())
        self.addVariable(new_factor.name, new_factor)

    def exitFeature(self, ctx: RLangParser.FeatureContext):
        arith_exp = ctx.arithmetic_exp().value
        new_feature = None
        # print(type(arith_exp))
        if isinstance(arith_exp, Factor):
            new_feature = Feature.from_Factor(arith_exp, name=ctx.IDENTIFIER().getText())
        elif isinstance(arith_exp, Callable):
            # TODO: Keep track of size of arith_exp for number_of_features argument. hardcoded to 1
            new_feature = Feature(function=arith_exp, name=ctx.IDENTIFIER().getText())
        else:
            print(f"Something else: {type(arith_exp)}")
        self.addVariable(ctx.IDENTIFIER().getText(), new_feature)

    def exitPredicate(self, ctx: RLangParser.PredicateContext):
        # print(type(ctx.boolean_exp().value))
        new_predicate = Predicate(ctx.boolean_exp().value, name=ctx.IDENTIFIER().getText())
        self.addVariable(ctx.IDENTIFIER().getText(), new_predicate)
        # print(new_predicate(np.array([0, 0, 0, 0])))

    def exitAction(self, ctx: RLangParser.ActionContext):
        pass

    def exitArith_paren(self, ctx: RLangParser.Arith_parenContext):
        ctx.value = ctx.arithmetic_exp().value

    def exitArith_times_divide(self, ctx: RLangParser.Arith_times_divideContext):
        if isinstance(ctx.lhs.value, StateGroundingFunction):
            if ctx.TIMES() is not None:
                ctx.value = ctx.lhs.value * ctx.rhs.value
            elif ctx.DIVIDE() is not None:
                ctx.value = ctx.lhs.value / ctx.rhs.value
            return

        if isinstance(ctx.rhs.value, StateGroundingFunction):
            if ctx.TIMES() is not None:
                ctx.value = ctx.rhs.value * ctx.lhs.value
            elif ctx.DIVIDE() is not None:
                ctx.value = ctx.lhs.value / ctx.rhs.value
            return

        # TODO: Support other StateGroundings

        if isinstance(ctx.lhs.value, (int, float)) and isinstance(ctx.rhs.value, (int, float)):
            operation = None
            if ctx.TIMES() is not None:
                operation = lambda a, b: a * b
            elif ctx.DIVIDE() is not None:
                operation = lambda a, b: a / b
            ctx.value = lambda *args, **kwargs: operation(ctx.lhs.value, ctx.rhs.value)
            return

        raise RLangSemanticError(f"Using '*' or '/' on {type(ctx.lhs.value)} and {type(ctx.rhs.value)} not yet implemented")

    def exitArith_plus_minus(self, ctx: RLangParser.Arith_plus_minusContext):
        if isinstance(ctx.lhs.value, StateGroundingFunction):
            if ctx.PLUS() is not None:
                ctx.value = ctx.lhs.value + ctx.rhs.value
            elif ctx.MINUS() is not None:
                ctx.value = ctx.lhs.value - ctx.rhs.value
            return

        if isinstance(ctx.rhs.value, StateGroundingFunction):
            if ctx.PLUS() is not None:
                ctx.value = ctx.rhs.value + ctx.lhs.value
            elif ctx.MINUS() is not None:
                ctx.value = ctx.lhs.value - ctx.rhs.value
            return

        # TODO: Support other StateGroundings

        if isinstance(ctx.lhs.value, (int, float)) and isinstance(ctx.rhs.value, (int, float)):
            operation = None
            if ctx.PLUS() is not None:
                operation = lambda a, b: a + b
            elif ctx.DIVIDE() is not None:
                operation = lambda a, b: a - b
            ctx.value = lambda *args, **kwargs: operation(ctx.lhs.value, ctx.rhs.value)
            return

        raise RLangSemanticError(f"Using '+' or '-' on {type(ctx.lhs.value)} and {type(ctx.rhs.value)} not yet implemented")

    def exitArith_number(self, ctx: RLangParser.Arith_numberContext):
        ctx.value = ctx.any_number().value

    def exitArith_bound_var(self, ctx: RLangParser.Arith_bound_varContext):
        ctx.value = ctx.any_bound_var().value

    def exitBool_paren(self, ctx: RLangParser.Bool_parenContext):
        ctx.value = ctx.boolean_exp().value

    def exitBool_and(self, ctx: RLangParser.Bool_andContext):
        # TODO: Refactor this. operands may or may not be a GroundingFunction
        ctx.value = ctx.lhs.value.and_(ctx.rhs.value)

    def exitBool_or(self, ctx: RLangParser.Bool_orContext):
        # TODO: Refactor this. operands may or may not be a GroundingFunction
        ctx.value = ctx.lhs.value.or_(ctx.rhs.value)

    def exitBool_not(self, ctx: RLangParser.Bool_notContext):
        # TODO: Refactor this. expression may or may not be a GroundingFunction
        ctx.value = ctx.boolean_exp().value.not_()

    def exitBool_in(self, ctx: RLangParser.Bool_inContext):
        # TODO: What kinds of operands do we want to allow here?
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
        # TODO: Refactor this. BooleanExpressions no longer exist, operands may or may not be GroundingFunctions
        bool_operation = None
        if ctx.EQ_TO() is not None:
            bool_operation = lambda a, b: a == b
        elif ctx.NOT_EQ() is not None:
            bool_operation = lambda a, b: a != b
        ctx.value = lambda *args, **kwargs: bool_operation(ctx.lhs.value(*args, **kwargs),
                                                           ctx.rhs.value(*args, **kwargs))

    def exitBool_arith_eq(self, ctx: RLangParser.Bool_arith_eqContext):
        # TODO: Refactor this. BooleanExpressions no longer exist, operands may or may not be GroundingFunctions
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
        # print(type(ctx.lhs.value))
        # print(ctx.lhs.value(np.array([0, 1, 2])))
        # print(type(ctx.rhs.value))
        # print(ctx.rhs.value(state=np.array([0, 1, 2])))
        # TODO: This breaks with function and RealExpression
        fun = lambda *args, **kwargs: bool_operation(ctx.lhs.value(*args, **kwargs), ctx.rhs.value(*args, **kwargs))
        ctx.value = BooleanExpression(fun, ["state"])

    def exitBool_bound_var(self, ctx: RLangParser.Bool_bound_varContext):
        ctx.value = ctx.any_bound_var().value

    def exitBool_tf(self, ctx: RLangParser.Bool_tfContext):
        if ctx.TRUE() is not None:
            ctx.value = True
        elif ctx.FALSE() is not None:
            ctx.value = False

    # def exitAny_bound_var(self, ctx: RLangParser.Any_bound_varContext):
    #     variable = None
    #     if ctx.IDENTIFIER() is not None:
    #         variable = self.retrieveVariable(ctx.IDENTIFIER().getText())
    #     elif ctx.S() is not None:
    #         # TODO: Support this
    #         variable = Feature.from_Factor(Factor(ctx.trailer()[0].value))
    #         pass
    #     elif ctx.S_PRIME() is not None:
    #         # TODO: Support this
    #         variable = S_prime
    #         pass
    #     elif ctx.A() is not None:
    #         # TODO: Support this
    #         variable = A
    #     if ctx.trailer():  # if it's not empty
    #         trailers = list(map(lambda x: x.value, ctx.trailer()))
    #         trailers.insert(0, variable)
    #         # TODO: this needs to change based on type(variable)
    #         # print(variable)
    #         # print(trailers)
    #         indexed_variable = reduce(lambda a, b: a[b], trailers)
    #         variable = indexed_variable
    #     ctx.value = variable
    #     # print(type(variable))

    def exitBound_identifier(self, ctx: RLangParser.Bound_identifierContext):
        variable = self.retrieveVariable(ctx.IDENTIFIER().getText())
        if not ctx.trailer():   # Check if it's not empty
            ctx.value = variable
            return

        # TODO: Properly implement this
        if isinstance(variable, Factor):
            if len(ctx.trailer()) > 1:
                raise RLangSemanticError("Too much subscripting on Factor")
            ctx.value = variable[ctx.trailer()[0].value]
        elif isinstance(variable, Feature):
            if len(ctx.trailer()) > 1:
                raise RLangSemanticError("Too much subscripting on Feature")
            ctx.value = Feature(function=lambda *args, **kwargs: variable(*args, **kwargs)[ctx.trailer()[0].value])


    def exitBound_state(self, ctx: RLangParser.Bound_stateContext):
        feature_positions = list(range(self.mdp_metadata.state_space.shape[0]))
        if ctx.trailer() is not None:
            feature_positions = ctx.trailer().value
        ctx.value = Factor(feature_positions)

    def exitBound_next_state(self, ctx: RLangParser.Bound_next_stateContext):
        # TODO
        pass

    def exitBound_action(self, ctx: RLangParser.Bound_actionContext):
        # TODO
        pass

    def exitTrailer_array(self, ctx: RLangParser.Trailer_arrayContext):
        ctx.value = ctx.array_exp().value

    def exitTrailer_slice(self, ctx: RLangParser.Trailer_sliceContext):
        ctx.value = ctx.slice_exp().value

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

    def exitAny_num_int(self, ctx: RLangParser.Any_num_intContext):
        ctx.value = ctx.any_integer().value

    def exitAny_num_dec(self, ctx: RLangParser.Any_num_decContext):
        ctx.value = ctx.any_decimal().value

    def enterAny_integer(self, ctx: RLangParser.Any_integerContext):
        ctx.value = int(ctx.getText())

    def enterAny_decimal(self, ctx: RLangParser.Any_decimalContext):
        ctx.value = float(ctx.getText())
