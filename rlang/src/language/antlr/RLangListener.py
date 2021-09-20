import copy
import json

from rlang.src.grounding import *
from rlang.src.grounding.groundings import GroundingFunction, PrimitiveGrounding, ConstantGrounding, IdentityGrounding

from .RLangParser import RLangParser
from .RLangParserListener import RLangParserListener
from rlang.src.language.utils.vocabulary_assembler import VocabularyAssembler
from rlang.src.language.utils.semantic_schemas import policy_stat_collection, conditional_policy_statement
from .Exceptions import *


class RLangListener(RLangParserListener):
    def __init__(self, mdp_metadata: MDPMetadata = None):
        self.vocab_fnames = []
        self.grounded_vars = {}
        self.rlang_knowledge = RLangKnowledge()
        self.mdp_metadata = mdp_metadata

    # This function adds the lmdp objects in the vocabulary files to self.grounded_vars
    # And probably keep track of object names in the vocab for later reference from the rlang file
    def parseVocabFiles(self):
        def parseVocabFile(file: str):
            with open(file, 'r') as f:
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

    def exitConstant(self, ctx: RLangParser.ConstantContext):
        if ctx.arithmetic_exp() is not None:
            new_constant = ctx.arithmetic_exp().value
        else:
            new_constant = ctx.boolean_exp().value

        if new_constant.domain is not Domain.ANY:
            raise RLangSemanticError(
                f"The value of a constant must be known at compile time. This is a function of {new_constant.domain.name}")
        new_constant = ConstantGrounding(codomain=Domain.ANY, value=new_constant(), name=ctx.IDENTIFIER().getText())
        self.addVariable(new_constant.name, new_constant)

    def exitAction(self, ctx: RLangParser.ActionContext):
        if ctx.any_number() is not None:
            new_action = ActionReference(action=ctx.any_number().value, name=ctx.IDENTIFIER().getText())
        elif ctx.int_array_exp() is not None:
            new_action = ActionReference(action=ctx.int_array_exp().value, name=ctx.IDENTIFIER().getText())
        elif ctx.any_array_exp() is not None:
            new_action = ActionReference(action=ctx.any_array_exp().value, name=ctx.IDENTIFIER().getText())
        self.addVariable(new_action.name, new_action)

    def exitFactor(self, ctx: RLangParser.FactorContext):
        feature_positions = list(range(self.mdp_metadata.state_space.shape[0]))
        if ctx.trailer() is not None:
            if isinstance(ctx.trailer().value, slice):
                feature_positions = list(range(self.mdp_metadata.state_space.shape[0]))[ctx.trailer().value]
            else:
                feature_positions = ctx.trailer().value
        new_factor = Factor(state_indexer=feature_positions, name=ctx.IDENTIFIER().getText())
        self.addVariable(new_factor.name, new_factor)

    def exitPredicate(self, ctx: RLangParser.PredicateContext):
        new_predicate = ctx.boolean_exp().value
        new_predicate.name = ctx.IDENTIFIER().getText()
        self.addVariable(new_predicate.name, new_predicate)

    def exitFeature(self, ctx: RLangParser.FeatureContext):
        arith_exp = ctx.arithmetic_exp().value
        if isinstance(arith_exp, Factor):
            new_feature = Feature.from_Factor(arith_exp, name=ctx.IDENTIFIER().getText())
        else:
            new_feature = arith_exp
            new_feature.name = ctx.IDENTIFIER().getText()
        self.addVariable(new_feature.name, new_feature)

    def exitMarkov_feature(self, ctx: RLangParser.Markov_featureContext):
        arith_exp = ctx.arithmetic_exp().value
        if isinstance(arith_exp, Factor):
            new_markov_feature = MarkovFeature.from_Factor(arith_exp, name=ctx.IDENTIFIER().getText())
        elif isinstance(arith_exp, Feature):
            new_markov_feature = MarkovFeature(function=arith_exp, name=ctx.IDENTIFIER().getText())
        else:
            raise RLangSemanticError(f"Cannot make a MarkovFeature from a {type(arith_exp)}")
        self.addVariable(ctx.IDENTIFIER().getText(), new_markov_feature)

    def exitOption(self, ctx: RLangParser.OptionContext):
        policy_stats = lambda *args, **kwargs: policy_stat_collection(
            list(map(lambda x: x.value, ctx.stats)), *args, **kwargs)
        new_policy = Policy(function=policy_stats)

        if isinstance(ctx.init.value, Predicate):
            init_predicate = ctx.init.value
        else:
            raise RLangSemanticError(f"Cannot initialize an Option based on a {type(ctx.boolean_exp().value)}")

        if isinstance(ctx.until.value, Predicate):
            until_predicate = ctx.until.value
        else:
            raise RLangSemanticError(f"Cannot terminate an Option based on a {type(ctx.boolean_exp().value)}")

        new_option = Option(initiation=init_predicate, termination=until_predicate, policy=new_policy,
                            name=ctx.IDENTIFIER().getText())
        self.addVariable(new_option.name, new_option)

    def exitPolicy(self, ctx: RLangParser.PolicyContext):
        policy_stats = lambda *args, **kwargs: policy_stat_collection(
            list(map(lambda x: x.value, ctx.stats)), *args, **kwargs)
        new_policy = Policy(function=policy_stats, name=ctx.IDENTIFIER().getText())
        self.addVariable(new_policy.name, new_policy)

    def exitReward(self, ctx: RLangParser.RewardContext):
        if ctx.arithmetic_exp().value.domain != Domain.ANY:
            raise RLangSemanticError(f"Cannot prescribe reward that is a function of {ctx.arithmetic_exp().value.domain}")
        elif ctx.arithmetic_exp().value.codomain != Domain.REAL_VALUE:
            raise RLangSemanticError(f"Cannot prescribe reward that is not numerical: {ctx.arithmetic_exp().value.codomain}")
        ctx.value = Reward(ctx.arithmetic_exp().value)

    def exitPolicy_stat_execute(self, ctx: RLangParser.Policy_stat_executeContext):
        ctx.value = ctx.execute().value

    def exitPolicy_stat_conditional(self, ctx: RLangParser.Policy_stat_conditionalContext):
        if_condition = ctx.if_condition.value
        if_statements = lambda *args, **kwargs: policy_stat_collection(
            list(map(lambda x: x.value, ctx.if_statements)), *args, **kwargs)
        elif_condition = None
        elif_statements = None
        else_statements = None

        if ctx.elif_condition is not None:
            elif_condition = ctx.elif_condition.value
            elif_statements = lambda *args, **kwargs: policy_stat_collection(
                list(map(lambda x: x.value, ctx.elif_statements)), *args, **kwargs)

        if len(ctx.else_statements) > 0:
            else_statements = lambda *args, **kwargs: policy_stat_collection(
                list(map(lambda x: x.value, ctx.else_statements)), *args, **kwargs)

        ctx.value = lambda *args, **kwargs: conditional_policy_statement(
            if_condition, if_statements, elif_condition, elif_statements, else_statements, *args, **kwargs)

    def exitExecute(self, ctx: RLangParser.ExecuteContext):
        if ctx.IDENTIFIER() is not None:
            variable = self.retrieveVariable(ctx.IDENTIFIER().getText())
            if not isinstance(variable, (Option, Policy, ActionReference)):
                raise RLangSemanticError(f"Cannot execute a {type(variable)}")
            ctx.value = variable
        else:
            ctx.value = ActionReference(action=ctx.arithmetic_exp().value)

    def exitArith_paren(self, ctx: RLangParser.Arith_parenContext):
        ctx.value = ctx.arithmetic_exp().value

    def exitArith_times_divide(self, ctx: RLangParser.Arith_times_divideContext):
        if isinstance(ctx.lhs.value, GroundingFunction) or isinstance(ctx.rhs.value, GroundingFunction):
            if ctx.TIMES() is not None:
                ctx.value = ctx.lhs.value * ctx.rhs.value
            elif ctx.DIVIDE() is not None:
                ctx.value = ctx.lhs.value / ctx.rhs.value
            return

    def exitArith_plus_minus(self, ctx: RLangParser.Arith_plus_minusContext):
        if isinstance(ctx.lhs.value, GroundingFunction) or isinstance(ctx.rhs.value, GroundingFunction):
            if ctx.PLUS() is not None:
                ctx.value = ctx.lhs.value + ctx.rhs.value
            elif ctx.MINUS() is not None:
                ctx.value = ctx.lhs.value - ctx.rhs.value
            return

    def exitArith_number(self, ctx: RLangParser.Arith_numberContext):
        ctx.value = PrimitiveGrounding(codomain=Domain.REAL_VALUE, value=ctx.any_number().value)

    def exitArith_array(self, ctx: RLangParser.Arith_arrayContext):
        ctx.value = PrimitiveGrounding(codomain=Domain.REAL_VALUE, value=ctx.any_array_exp().value)

    def exitArith_bound_var(self, ctx: RLangParser.Arith_bound_varContext):
        if not isinstance(ctx.any_bound_var().value, (Factor, Feature, Policy)):
            raise RLangSemanticError(f"{type(ctx.any_bound_var().value)} is not numerical")
        ctx.value = ctx.any_bound_var().value

    def exitBool_paren(self, ctx: RLangParser.Bool_parenContext):
        ctx.value = ctx.boolean_exp().value

    def exitBool_and(self, ctx: RLangParser.Bool_andContext):
        ctx.value = ctx.lhs.value & ctx.rhs.value

    def exitBool_or(self, ctx: RLangParser.Bool_orContext):
        ctx.value = ctx.lhs.value | ctx.rhs.value

    def exitBool_not(self, ctx: RLangParser.Bool_notContext):
        ctx.value = ~ ctx.boolean_exp().value

    def exitBool_in(self, ctx: RLangParser.Bool_inContext):
        # TODO: This IS NOT so simple. Resolve this after migrating arithmetic expressions to PrimitiveGroundings
        ctx.value = ctx.lhs.value in ctx.rhs.value

    def exitBool_bool_eq(self, ctx: RLangParser.Bool_bool_eqContext):
        if ctx.EQ_TO() is not None:
            ctx.value = ctx.lhs.value == ctx.rhs.value
        else:
            ctx.value = ctx.lhs.value == ctx.rhs.value

    def exitBool_arith_eq(self, ctx: RLangParser.Bool_arith_eqContext):
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

        ctx.value = bool_operation(ctx.lhs.value, ctx.rhs.value)

    def exitBool_bound_var(self, ctx: RLangParser.Bool_bound_varContext):
        if not isinstance(ctx.any_bound_var().value, (Predicate, PrimitiveGrounding)):
            raise RLangSemanticError(f"This {type(ctx.any_bound_var().value)} does not have a truth value")
        if isinstance(ctx.any_bound_var().value, PrimitiveGrounding):
            ctx.value = Predicate.from_PrimitiveGrounding(primitive_grounding=ctx.any_bound_var().value)
        else:
            ctx.value = ctx.any_bound_var().value

    def exitBool_tf(self, ctx: RLangParser.Bool_tfContext):
        if ctx.TRUE() is not None:
            ctx.value = Predicate(function=lambda *args, **kwargs: True, domain=Domain.ANY)
        elif ctx.FALSE() is not None:
            ctx.value = Predicate(function=lambda *args, **kwargs: False, domain=Domain.ANY)

    def exitBound_identifier(self, ctx: RLangParser.Bound_identifierContext):
        variable = self.retrieveVariable(ctx.IDENTIFIER().getText())
        new_var = None

        if not ctx.trailer():  # Check if it's not empty
            new_var = variable
        elif isinstance(variable, Factor):
            if len(ctx.trailer()) > 1:
                raise RLangSemanticError("Too much subscripting on Factor")
            new_var = variable[ctx.trailer()[0].value]
        elif isinstance(variable, Feature):
            if len(ctx.trailer()) > 1:
                raise RLangSemanticError("Too much subscripting on Feature")
            new_var = Feature(function=lambda *args, **kwargs: variable(*args, **kwargs)[ctx.trailer()[0].value],
                              domain=variable.domain)
        else:
            raise RLangSemanticError(f"Subscripting a {type(variable)} is not yet supported")

        if ctx.PRIME() is not None:
            if new_var.domain == Domain.STATE:
                if isinstance(new_var, Factor):
                    ctx.value = Factor(new_var.indexer, domain=Domain.NEXT_STATE)
                elif isinstance(new_var, Feature):
                    ctx.value = Feature(function=lambda *args, **kwargs: new_var(state=kwargs['next_state']), domain=Domain.NEXT_STATE)
            else:
                raise RLangSemanticError(f"Cannot use the ' operator on a {type(ctx.value)} with domain {ctx.value.domain.name}")
        else:
            ctx.value = new_var

    def exitBound_state(self, ctx: RLangParser.Bound_stateContext):
        if ctx.trailer() is not None:
            ctx.value = Factor(ctx.trailer().value)
        else:
            ctx.value = IdentityGrounding(Domain.STATE)

    def exitBound_next_state(self, ctx: RLangParser.Bound_next_stateContext):
        if ctx.trailer() is not None:
            ctx.value = Factor(ctx.trailer().value, domain='next_state')
        else:
            ctx.value = IdentityGrounding(Domain.NEXT_STATE)

    def exitBound_action(self, ctx: RLangParser.Bound_actionContext):
        ctx.value = IdentityGrounding(Domain.ACTION)

    def exitTrailer_array(self, ctx: RLangParser.Trailer_arrayContext):
        ctx.value = ctx.int_array_exp().value

    def exitTrailer_slice(self, ctx: RLangParser.Trailer_sliceContext):
        ctx.value = ctx.slice_exp().value

    def exitAny_array_exp(self, ctx: RLangParser.Any_array_expContext):
        ctx.value = list(map(lambda x: x.value, ctx.arr))

    def exitInt_array_exp(self, ctx: RLangParser.Int_array_expContext):
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