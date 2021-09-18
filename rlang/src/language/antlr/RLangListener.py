from typing import Callable
import json

from rlang.src.grounding import *
from rlang.src.grounding.state_groundings import StateGroundingFunction

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

    # This function add the lmdp objects in the vocabulary files to self.grounded_vars
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

    def exitFactor(self, ctx: RLangParser.FactorContext):
        # TODO: Consider modifying grammar to include S' for factor definition
        feature_positions = list(range(self.mdp_metadata.state_space.shape[0]))
        if ctx.trailer() is not None:
            if isinstance(ctx.trailer().value, slice):
                feature_positions = list(range(self.mdp_metadata.state_space.shape[0]))[ctx.trailer().value]
            else:
                feature_positions = ctx.trailer().value
        new_factor = Factor(state_indexer=feature_positions, name=ctx.IDENTIFIER().getText())
        self.addVariable(new_factor.name, new_factor)

    def exitFeature(self, ctx: RLangParser.FeatureContext):
        arith_exp = ctx.arithmetic_exp().value
        if isinstance(arith_exp, Factor):
            new_feature = Feature.from_Factor(arith_exp, name=ctx.IDENTIFIER().getText())
        # TODO: This will hopefully not exist after migrating to PrimitiveGrounding. Need to check domain.
        elif isinstance(arith_exp, Callable):
            new_feature = Feature(function=arith_exp, name=ctx.IDENTIFIER().getText())
        else:
            raise RLangSemanticError(f"Cannot make a Feature from a {type(arith_exp)}")
        self.addVariable(ctx.IDENTIFIER().getText(), new_feature)

    def exitPredicate(self, ctx: RLangParser.PredicateContext):
        if isinstance(ctx.boolean_exp().value, Predicate):
            new_predicate = ctx.boolean_exp().value
        # TODO: This will hopefully not exist after migrating to PrimitiveGrounding
        elif isinstance(ctx.boolean_exp().value, Callable):
            new_predicate = Predicate(ctx.boolean_exp().value, name=ctx.IDENTIFIER().getText())
        # TODO: This MIGHT not exist after migrating to PrimitiveGrounding
        elif isinstance(ctx.boolean_exp().value, bool):
            new_predicate = Predicate(lambda *args, **kwargs: ctx.boolean_exp().value, name=ctx.IDENTIFIER().getText())
        else:
            raise RLangSemanticError(f"Cannot make a Predicate from a {type(ctx.boolean_exp().value)}")
        self.addVariable(ctx.IDENTIFIER().getText(), new_predicate)

    def exitAction(self, ctx: RLangParser.ActionContext):
        if ctx.any_number() is not None:
            new_action = ActionReference(action=ctx.any_number().value, name=ctx.IDENTIFIER().getText())
        elif ctx.int_array_exp() is not None:
            new_action = ActionReference(action=ctx.int_array_exp().value, name=ctx.IDENTIFIER().getText())
        elif ctx.any_array_exp() is not None:
            new_action = ActionReference(action=ctx.any_array_exp().value, name=ctx.IDENTIFIER().getText())
        else:
            raise RLangSemanticError(f"FATAL ERROR - You've done the impossible")
        self.addVariable(ctx.IDENTIFIER().getText(), new_action)

    def exitMarkov_feature(self, ctx: RLangParser.Markov_featureContext):
        arith_exp = ctx.arithmetic_exp().value
        if isinstance(arith_exp, Factor):
            new_markov_feature = MarkovFeature.from_Factor(arith_exp, name=ctx.IDENTIFIER().getText())
        elif isinstance(arith_exp, Callable):
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
        elif isinstance(ctx.init.value, Callable):
            init_predicate = Predicate(ctx.init.value)
        elif isinstance(ctx.init.value, bool):
            init_predicate = Predicate(lambda *args, **kwargs: ctx.init.value)
        else:
            raise RLangSemanticError(f"Cannot initialize an Option based on a {type(ctx.boolean_exp().value)}")

        if isinstance(ctx.until.value, Predicate):
            until_predicate = ctx.until.value
        elif isinstance(ctx.until.value, Callable):
            until_predicate = Predicate(ctx.until.value)
        elif isinstance(ctx.until.value, bool):
            until_predicate = Predicate(lambda *args, **kwargs: ctx.until.value)
        else:
            raise RLangSemanticError(f"Cannot terminate an Option based on a {type(ctx.boolean_exp().value)}")

        new_option = Option(initiation=init_predicate, termination=until_predicate, policy=new_policy,
                            name=ctx.IDENTIFIER().getText())
        self.addVariable(ctx.IDENTIFIER().getText(), new_option)

    def exitPolicy(self, ctx: RLangParser.PolicyContext):
        policy_stats = lambda *args, **kwargs: policy_stat_collection(
            list(map(lambda x: x.value, ctx.stats)), *args, **kwargs)
        new_policy = Policy(function=policy_stats, name=ctx.IDENTIFIER().getText())
        self.addVariable(ctx.IDENTIFIER().getText(), new_policy)

    def exitPolicy_stat_execute(self, ctx: RLangParser.Policy_stat_executeContext):
        ctx.value = ctx.execute().value

    def exitPolicy_stat_conditional(self, ctx: RLangParser.Policy_stat_conditionalContext):
        if not isinstance(ctx.if_condition.value, (bool, Predicate, Callable)):
            # TODO: May need to accommodate more object types here
            raise RLangSemanticError(
                f"A {type(ctx.if_condition.value)} cannot be used in a conditional within a Policy")

        if isinstance(ctx.if_condition.value, bool):
            if_condition = lambda *args, **kwargs: ctx.if_condition.value
        else:
            if_condition = ctx.if_condition.value

        if_statements = lambda *args, **kwargs: policy_stat_collection(
            list(map(lambda x: x.value, ctx.if_statements)), *args, **kwargs)
        elif_condition = None
        elif_statements = None
        else_statements = None

        if ctx.elif_condition is not None:
            if not isinstance(ctx.elif_condition.value, (bool, Predicate, Callable)):
                # TODO: May need to accommodate more object types here
                raise RLangSemanticError(
                    f"A {type(ctx.elif_condition.value)} cannot be used in a conditional within a Policy")
            if isinstance(ctx.elif_condition.value, bool):
                elif_condition = lambda *args, **kwargs: ctx.elif_condition.value
            else:
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
            return
        elif ctx.any_number() is not None:
            new_action = ActionReference(action=ctx.any_number().value)
        elif ctx.int_array_exp() is not None:
            new_action = ActionReference(action=ctx.int_array_exp().value)
        elif ctx.any_array_exp() is not None:
            new_action = ActionReference(action=ctx.any_array_exp().value)
        else:
            raise RLangSemanticError(f"FATAL ERROR - You've done the impossible")
        ctx.value = new_action

    def exitArith_paren(self, ctx: RLangParser.Arith_parenContext):
        ctx.value = ctx.arithmetic_exp().value

    def exitArith_times_divide(self, ctx: RLangParser.Arith_times_divideContext):
        if isinstance(ctx.lhs.value, StateGroundingFunction) or isinstance(ctx.rhs.value, StateGroundingFunction):
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

        # TODO: Replace this with PrimitiveGrounding operation
        if isinstance(ctx.lhs.value, Callable) and isinstance(ctx.rhs.value, Callable):
            if ctx.TIMES() is not None:
                ctx.value = lambda *args, **kwargs: ctx.lhs.value(*args, **kwargs) * ctx.rhs.value(*args, **kwargs)
            elif ctx.DIVIDE() is not None:
                ctx.value = lambda *args, **kwargs: ctx.lhs.value(*args, **kwargs) / ctx.rhs.value(*args, **kwargs)
            return

        # TODO: Support other GroundingFunctions

        # TODO: MAYBE replace this with PrimitiveGrounding operation
        if isinstance(ctx.lhs.value, (int, float)) and isinstance(ctx.rhs.value, (int, float)):
            operation = None
            if ctx.TIMES() is not None:
                operation = lambda a, b: a * b
            elif ctx.DIVIDE() is not None:
                operation = lambda a, b: a / b
            ctx.value = lambda *args, **kwargs: operation(ctx.lhs.value, ctx.rhs.value)
            return

        raise RLangSemanticError(
            f"Using '*' or '/' on {type(ctx.lhs.value)} and {type(ctx.rhs.value)} not yet implemented")

    def exitArith_plus_minus(self, ctx: RLangParser.Arith_plus_minusContext):
        if isinstance(ctx.lhs.value, StateGroundingFunction) or isinstance(ctx.rhs.value, StateGroundingFunction):
            if ctx.PLUS() is not None:
                ctx.value = ctx.lhs.value + ctx.rhs.value
            elif ctx.MINUS() is not None:
                ctx.value = ctx.lhs.value - ctx.rhs.value
            return

        # TODO: Replace this with PrimitiveGrounding operation
        if isinstance(ctx.lhs.value, Callable) and isinstance(ctx.rhs.value, Callable):
            if ctx.PLUS() is not None:
                ctx.value = lambda *args, **kwargs: ctx.lhs.value(*args, **kwargs) + ctx.rhs.value(*args, **kwargs)
            elif ctx.MINUS() is not None:
                ctx.value = lambda *args, **kwargs: ctx.lhs.value(*args, **kwargs) - ctx.rhs.value(*args, **kwargs)
            return

        # TODO: Support other GroundingFunctions which an any_bound_var could be

        # TODO: MAYBE replace this with PrimitiveGrounding operation
        if isinstance(ctx.lhs.value, (int, float)) and isinstance(ctx.rhs.value, (int, float)):
            operation = None
            if ctx.PLUS() is not None:
                operation = lambda a, b: a + b
            elif ctx.MINUS() is not None:
                operation = lambda a, b: a - b
            ctx.value = lambda *args, **kwargs: operation(ctx.lhs.value, ctx.rhs.value)
            return

        raise RLangSemanticError(
            f"Using '+' or '-' on {type(ctx.lhs.value)} and {type(ctx.rhs.value)} not yet implemented")

    def exitArith_number(self, ctx: RLangParser.Arith_numberContext):
        # TODO: This should not be a Callable. Maybe make this a PrimitiveGrounding
        ctx.value = lambda *args, **kwargs: ctx.any_number().value

    def exitArith_array(self, ctx: RLangParser.Arith_arrayContext):
        # TODO: Maybe replace this with a PrimitiveGrounding
        ctx.value = ctx.any_array_exp().value

    def exitArith_bound_var(self, ctx: RLangParser.Arith_bound_varContext):
        if not isinstance(ctx.any_bound_var().value, (Factor, Feature, Policy, Callable)):
            raise RLangSemanticError(f"{type(ctx.any_bound_var().value)} is not numerical")
        ctx.value = ctx.any_bound_var().value

    def exitBool_paren(self, ctx: RLangParser.Bool_parenContext):
        ctx.value = ctx.boolean_exp().value

    def exitBool_and(self, ctx: RLangParser.Bool_andContext):
        # TODO: lhs or rhs may be functions. Is there a better way to handle this?
        # TODO: UPDATE: This will change if bool_tf code migrates to PrimitiveGrounding
        if isinstance(ctx.lhs.value, Predicate) or isinstance(ctx.rhs.value, Predicate):
            ctx.value = ctx.lhs.value & ctx.rhs.value
            return
        if isinstance(ctx.lhs.value, Callable) and isinstance(ctx.rhs.value, Callable):
            ctx.value = lambda *args, **kwargs: ctx.lhs.value(*args, **kwargs) & ctx.rhs.value(*args, **kwargs)
            return
        # Do we ever get here?
        ctx.value = ctx.lhs.value & ctx.rhs.value

    def exitBool_or(self, ctx: RLangParser.Bool_orContext):
        # TODO: This will change if bool_tf code migrates to PrimitiveGrounding
        if isinstance(ctx.lhs.value, Predicate) or isinstance(ctx.rhs.value, Predicate):
            ctx.value = ctx.lhs.value | ctx.rhs.value
            return
        if isinstance(ctx.lhs.value, Callable) and isinstance(ctx.rhs.value, Callable):
            ctx.value = lambda *args, **kwargs: ctx.lhs.value(*args, **kwargs) | ctx.rhs.value(*args, **kwargs)
            return
        ctx.value = ctx.lhs.value | ctx.rhs.value

    def exitBool_not(self, ctx: RLangParser.Bool_notContext):
        # TODO: This will change if bool_tf code migrates to PrimitiveGrounding
        if isinstance(ctx.boolean_exp().value, bool):
            ctx.value = not ctx.boolean_exp().value
            return
        if isinstance(ctx.boolean_exp().value, Callable):
            ctx.value = lambda *args, **kwargs: not ctx.boolean_exp().value(*args, **kwargs)
            return
        ctx.value = ~ ctx.boolean_exp().value

    def exitBool_in(self, ctx: RLangParser.Bool_inContext):
        # TODO: This IS NOT so simple. Resolve this after migrating arithmetic expressions to PrimitiveGroundings
        ctx.value = ctx.lhs.value in ctx.rhs.value

    def exitBool_bool_eq(self, ctx: RLangParser.Bool_bool_eqContext):
        # TODO: This will change if bool_tf code migrates to PrimitiveGrounding
        bool_operation = None
        if ctx.EQ_TO() is not None:
            bool_operation = lambda a, b: a == b
        elif ctx.NOT_EQ() is not None:
            bool_operation = lambda a, b: a != b

        if isinstance(ctx.lhs.value, StateGroundingFunction) or isinstance(ctx.rhs.value, StateGroundingFunction):
            ctx.value = bool_operation(ctx.lhs.value, ctx.rhs.value)
        else:
            ctx.value = lambda *args, **kwargs: bool_operation(ctx.lhs.value, ctx.rhs.value)

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

        # TODO: Do these need to be StateGroundingFunctions? Might they just need to be GroundingFunctions?
        if isinstance(ctx.lhs.value, StateGroundingFunction) or isinstance(ctx.rhs.value, StateGroundingFunction):
            ctx.value = bool_operation(ctx.lhs.value, ctx.rhs.value)
            return

        raise RLangSemanticError(
            f"Operation not permitted (or implemented) between {type(ctx.lhs.value)} and {type(ctx.rhs.value)}")

    def exitBool_bound_var(self, ctx: RLangParser.Bool_bound_varContext):
        if not isinstance(ctx.any_bound_var().value, Predicate):
            raise RLangSemanticError(f"{type(ctx.any_bound_var().value)} does not have a truth value")
        ctx.value = ctx.any_bound_var().value

    def exitBool_tf(self, ctx: RLangParser.Bool_tfContext):
        # TODO: This should probably be changed to at least ctx.value = True/False. Maybe migrate to PrimitiveGrounding
        if ctx.TRUE() is not None:
            ctx.value = lambda *args, **kwargs: True
        elif ctx.FALSE() is not None:
            ctx.value = lambda *args, **kwargs: False

    def exitBound_identifier(self, ctx: RLangParser.Bound_identifierContext):
        variable = self.retrieveVariable(ctx.IDENTIFIER().getText())
        if not ctx.trailer():  # Check if it's not empty
            ctx.value = variable
            return

        if isinstance(variable, Factor):
            if len(ctx.trailer()) > 1:
                raise RLangSemanticError("Too much subscripting on Factor")
            ctx.value = variable[ctx.trailer()[0].value]
            return
        elif isinstance(variable, Feature):
            if len(ctx.trailer()) > 1:
                raise RLangSemanticError("Too much subscripting on Feature")
            ctx.value = Feature(function=lambda *args, **kwargs: variable(*args, **kwargs)[ctx.trailer()[0].value])
            return

        # TODO: Implement subscripting for other StateGroundings
        raise RLangSemanticError(f"Subscripting a {type(variable)} is not yet supported")

    def exitBound_state(self, ctx: RLangParser.Bound_stateContext):
        feature_positions = list(range(self.mdp_metadata.state_space.shape[0]))
        if ctx.trailer() is not None:
            feature_positions = ctx.trailer().value
        ctx.value = Factor(feature_positions)

    def exitBound_next_state(self, ctx: RLangParser.Bound_next_stateContext):
        feature_positions = list(range(self.mdp_metadata.state_space.shape[0]))
        if ctx.trailer() is not None:
            feature_positions = ctx.trailer().value
        # TODO: Replace this with something more sophisticated. You can smuggle in S' into a Feature... bad.
        ctx.value = Factor(feature_positions, state_arg='next_state')

    def exitBound_action(self, ctx: RLangParser.Bound_actionContext):
        ctx.value = lambda *args, **kwargs: kwargs['action']

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
