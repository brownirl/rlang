import copy
from functools import reduce
from typing import Callable
import json
import numpy as np

from rlang.src.grounding import *
from rlang.src.grounding.groundings import GroundingFunction, PrimitiveGrounding, ConstantGrounding, IdentityGrounding

from .RLangParser import RLangParser
from .RLangParserListener import RLangParserListener
from rlang.src.language.utils.vocabulary_assembler import VocabularyAssembler
from rlang.src.language.utils.semantic_schemas import *
from .Exceptions import *


class RLangListener(RLangParserListener):
    def __init__(self, mdp_metadata: MDPMetadata = None, prior_knowledge: RLangKnowledge = None):
        if prior_knowledge is not None:
            mdp_metadata = prior_knowledge.mdp_metadata
        else:
            prior_knowledge = RLangKnowledge()

        self.vocab_fnames = []
        self.grounded_vars = {}
        self.rlang_knowledge = prior_knowledge
        self.mdp_metadata = mdp_metadata

    # This function adds the lmdp objects in the vocabulary files to self.grounded_vars
    # And probably keep track of object names in the vocab for later reference from the rlang file
    def parseVocabFiles(self):
        def parseVocabFile(file: str):
            with open(file, 'r') as f:
                vocab = json.load(f)
                # I'm not sure if this is best practice, maybe I should make VocabularyAssembler a util function
                voc_assembler = VocabularyAssembler(vocab)
                self.grounded_vars.update(voc_assembler.lmdp_objects)

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
        elif ctx.any_num_array_exp() is not None:
            new_action = ActionReference(action=ctx.any_num_array_exp().value, name=ctx.IDENTIFIER().getText())
        self.addVariable(new_action.name, new_action)

    def exitFactor(self, ctx: RLangParser.FactorContext):
        if isinstance(ctx.any_bound_var().value, Factor):
            new_factor = ctx.any_bound_var().value
            new_factor.name = ctx.IDENTIFIER().getText()
            if isinstance(new_factor.indexer, slice):
                if self.mdp_metadata is not None:
                    new_factor.indexer = list(
                        range(*new_factor.indexer.indices(self.mdp_metadata.state_space.shape[0])))
        elif isinstance(ctx.any_bound_var().value, IdentityGrounding):
            raise RLangSemanticError("A Factor must subscript from S or another Factor")
        else:
            raise RLangSemanticError(f"Cannot construct Factor with object type {type(ctx.any_bound_var().value)}")
        self.addVariable(new_factor.name, new_factor)

    def exitPredicate(self, ctx: RLangParser.PredicateContext):
        new_predicate = ctx.boolean_exp().value
        new_predicate.name = ctx.IDENTIFIER().getText()
        self.addVariable(new_predicate.name, new_predicate)

    def exitGoal(self, ctx: RLangParser.GoalContext):
        pass

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

    # ============================= Option =============================

    def exitOption(self, ctx: RLangParser.OptionContext):
        subpolicy = ctx.policy_statement_collection().value
        new_option = Option(initiation=ctx.init.value, termination=ctx.until.value, policy=subpolicy,
                            name=ctx.IDENTIFIER().getText())
        self.addVariable(new_option.name, new_option)

    def exitOption_condition(self, ctx: RLangParser.Option_conditionContext):
        if ctx.boolean_exp():
            ctx.value = ctx.boolean_exp().value
        else:
            ctx.value = Predicate.TRUE()

    # ============================= Policy =============================

    def exitPolicy(self, ctx: RLangParser.PolicyContext):
        new_policy = ctx.policy_statement_collection().value
        new_policy.name = ctx.IDENTIFIER().getText()
        self.addVariable(new_policy.name, new_policy)

    def exitPolicy_statement_collection(self, ctx: RLangParser.Policy_statement_collectionContext):
        policy_statements = [ps.value for ps in ctx.statements]
        length = 0
        for ps in policy_statements:
            if len(ps) > 0:
                length += len(ps)
            else:
                length = None
                break
        ctx.value = Policy(function=policy_generator_function(policy_statements), length=length)

    def exitPolicy_statement_execute(self, ctx: RLangParser.Policy_statement_executeContext):
        if isinstance(ctx.execute().value, ActionReference):
            ctx.value = Policy.from_action_reference(ctx.execute().value)
        elif isinstance(ctx.execute().value, Option):
            ctx.value = Policy(function=lambda *args, **kwargs: {ctx.execute().value: 1.0},
                               length=len(ctx.execute().value))
        else:
            ctx.value = ctx.execute().value

    def exitPolicy_statement_conditional(self, ctx: RLangParser.Policy_statement_conditionalContext):
        ctx.value = ctx.conditional_subpolicy().value

    def exitPolicy_statement_probabilistic(self, ctx: RLangParser.Policy_statement_probabilisticContext):
        ctx.value = ctx.probabilistic_subpolicy().value

    def exitExecute(self, ctx: RLangParser.ExecuteContext):
        if ctx.IDENTIFIER() is not None:
            variable = self.retrieveVariable(ctx.IDENTIFIER().getText())
            if not isinstance(variable, (Option, Policy, ActionReference)):
                raise RLangSemanticError(f"Cannot execute a {type(variable)}")
            ctx.value = variable
        else:
            ctx.value = ActionReference(action=ctx.arithmetic_exp().value)

    def exitConditional_subpolicy(self, ctx: RLangParser.Conditional_subpolicyContext):
        elif_conditions = [s.value for s in ctx.elif_conditions]
        elif_subpolicies = [s.value for s in ctx.elif_subpolicies]
        else_subpolicy = ctx.else_subpolicy.value if ctx.else_subpolicy else None
        ctx.value = Policy(
            function=lambda *args, **kwargs: conditional_policy_function(ctx.if_condition.value, ctx.if_subpolicy.value,
                                                                         elif_conditions,
                                                                         elif_subpolicies, else_subpolicy, *args,
                                                                         **kwargs))

    def exitProbabilistic_subpolicy(self, ctx: RLangParser.Probabilistic_subpolicyContext):
        subpolicies = [sp.value for sp in ctx.subpolicies]
        ctx.value = Policy(function=lambda *args, **kwargs: subpolicy_dict_function(subpolicies, *args, **kwargs))

    def exitProbabilistic_policy_statement_no_sugar(self,
                                                    ctx: RLangParser.Probabilistic_policy_statement_no_sugarContext):
        subpolicy = ctx.policy_statement_collection().value
        subpolicy.compose_probability(ctx.probabilistic_condition().value)
        ctx.value = subpolicy

    def exitProbabilistic_policy_statement_sugar(self, ctx: RLangParser.Probabilistic_policy_statement_sugarContext):
        subpolicy = Policy.from_action_reference(ctx.execute().value)
        subpolicy.compose_probability(ctx.probabilistic_condition().value)
        ctx.value = subpolicy

    def exitProbabilistic_condition(self, ctx: RLangParser.Probabilistic_conditionContext):
        if ctx.any_number():
            probability = ctx.any_number().value
        else:
            probability = ctx.integer_fraction().value
        if probability > 1.0 or probability < 0.0:
            raise RLangSemanticError("Probability must be between 0 and 1")
        ctx.value = probability

    # ============================= Effect =============================

    # def exitEffect(self, ctx: RLangParser.EffectContext):
    #     stats = list(map(lambda x: x.value, ctx.stats))
    #     all_stats = list()
    #     for s in stats:  # Collect all the effect statements. Some stats will be lists of effect statements.
    #         if isinstance(s, list):
    #             all_stats.extend(s)
    #         elif isinstance(s, Effect):
    #             all_stats.extend(s.transition_functions)
    #             all_stats.extend(s.reward_functions)
    #             all_stats.extend(s.predictions)
    #         else:
    #             all_stats.append(s)
    #
    #     reward_functions = list(filter(lambda x: isinstance(x, RewardFunction), all_stats))
    #     transition_functions = list(filter(lambda x: isinstance(x, TransitionFunction), all_stats))
    #     prediction_list = list(filter(lambda x: isinstance(x, Prediction), all_stats))
    #
    #     if ctx.IDENTIFIER() is not None:
    #         # This is a named effect which should not merge into the existing transition function
    #         new_effect = Effect(reward_functions=reward_functions,
    #                             transition_functions=transition_functions,
    #                             predictions=prediction_list,
    #                             name=ctx.IDENTIFIER().getText())
    #         self.addVariable(new_effect.name, new_effect)
    #     else:
    #         reward_functions.append(self.rlang_knowledge.reward_function)
    #         reward_stats = lambda *args, **kwargs: reward_stat_collection(reward_functions, *args, **kwargs)
    #         domain = Domain.ANY
    #         for funcs in reward_functions:
    #             domain += funcs.domain
    #         self.rlang_knowledge.reward_function = RewardFunction(reward=reward_stats, domain=domain)
    #
    #         transition_functions.append(self.rlang_knowledge.transition_function)
    #         transition_stats = lambda *args, **kwargs: default_stat_collection(transition_functions, *args, **kwargs)
    #         domain = Domain.ANY
    #         for funcs in transition_functions:
    #             domain += funcs.domain
    #         self.rlang_knowledge.transition_function = TransitionFunction(function=transition_stats, domain=domain)
    #
    #         predictions = dict()
    #         for p in [*prediction_list, *self.rlang_knowledge.predictions.values()]:
    #             p_name = p.grounding_predicted.name
    #             if p_name in predictions:
    #                 predictions.update({p_name: [*predictions[p_name], p]})
    #             else:
    #                 predictions.update({p_name: [p]})
    #         new_predictions = dict()
    #         for p_name2, p_value in predictions.items():
    #             # This is absolutely insane, but please do not remove it. Google 'Python for loop variable capture'
    #             def lambda_generator(these_stats):
    #                 return lambda *args, **kwargs: default_stat_collection(these_stats, *args, **kwargs)
    #
    #             new_p = Prediction(grounding_function=self.retrieveVariable(p_name2),
    #                                value=lambda_generator(p_value))
    #             # new_p.domain
    #             new_predictions.update({p_name2: new_p})
    #
    #         self.rlang_knowledge.predictions = new_predictions

    def exitEffect(self, ctx: RLangParser.EffectContext):
        new_effect = ctx.effect_statement_collection().value
        if ctx.IDENTIFIER() is not None:
            new_effect.name = ctx.IDENTIFIER().getText()
            self.addVariable(new_effect.name, new_effect)
        else:
            pass
            # must sum together reward, transition, and predictions?

    def exitEffect_statement_collection(self, ctx: RLangParser.Effect_statement_collectionContext):
        all_statements = [statement.value for statement in ctx.statements]
        # print(all_statements)

        # Rewards
        reward_statements = list(filter(lambda x: isinstance(x, RewardFunction), all_statements))

        # Effect References
        effect_references = list(filter(lambda x: isinstance(x, Effect), all_statements))
        reward_statements.extend([effect.reward_function for effect in effect_references])

        if reward_statements:
            reward_function = reduce(lambda a, b: a + b, reward_statements)
        else:
            reward_function = None

        new_effect = Effect(reward_function=reward_function)
        ctx.value = new_effect

    def exitEffect_statement_reward(self, ctx: RLangParser.Effect_statement_rewardContext):
        ctx.value = ctx.reward().value

    def exitEffect_statement_prediction(self, ctx: RLangParser.Effect_statement_predictionContext):
        ctx.value = ctx.prediction().value

    def exitEffect_statement_reference(self, ctx: RLangParser.Effect_statement_referenceContext):
        ctx.value = ctx.effect_reference().value

    def exitEffect_statement_conditional(self, ctx: RLangParser.Effect_statement_conditionalContext):
        ctx.value = ctx.conditional_effect().value

    def exitEffect_statement_probabilistic(self, ctx: RLangParser.Effect_statement_probabilisticContext):
        ctx.value = ctx.probabilistic_effect().value

    def exitReward(self, ctx: RLangParser.RewardContext):
        if not ctx.arithmetic_exp().value.domain <= Domain.STATE_ACTION:
            raise RLangSemanticError(
                f"Cannot prescribe reward that is a function of {ctx.arithmetic_exp().value.domain}")
        elif ctx.arithmetic_exp().value.codomain != Domain.REAL_VALUE:
            raise RLangSemanticError(
                f"Cannot prescribe reward that is not numerical: {ctx.arithmetic_exp().value.codomain}")
        ctx.value = RewardFunction(reward=ctx.arithmetic_exp().value)

    def exitPrediction(self, ctx: RLangParser.PredictionContext):
        if ctx.IDENTIFIER() is not None:
            grounding_function = self.retrieveVariable(ctx.IDENTIFIER().getText())
            if grounding_function.domain < Domain.STATE_ACTION_NEXT_STATE and ctx.PRIME() is None:
                raise RLangSemanticError("Use prime syntax to refer to the future state of variables")
            # if isinstance(grounding_function, MarkovFeature) and ctx.PRIME() is not None:
            #     raise RLangSemanticError("")
            ctx.value = Prediction(grounding_function=grounding_function, value=ctx.arithmetic_exp().value)
        elif ctx.S_PRIME() is not None:
            ctx.value = TransitionFunction(function=ctx.arithmetic_exp().value)

    def exitEffect_reference(self, ctx: RLangParser.Effect_referenceContext):
        effect = self.retrieveVariable(ctx.IDENTIFIER().getText())
        if not isinstance(effect, Effect):
            raise RLangSemanticError(f"Cannot predict a {type(effect)} in an Effect statement")
        ctx.value = effect

    def exitConditional_effect(self, ctx:RLangParser.Conditional_effectContext):
        if_condition = ctx.if_condition.value
        if_effect = ctx.if_effect.value
        elif_conditions = [s.value for s in ctx.elif_conditions]
        elif_effects = [s.value for s in ctx.elif_effects]
        else_effect = ctx.else_effect.value if ctx.else_effect else Effect()

        # Rewards

        if_reward = if_effect.reward_function
        elif_rewards = [elif_effect.reward_function for elif_effect in elif_effects]
        else_reward = else_effect.reward_function

        domain = reduce(lambda a, b: a + b.domain, [if_condition.domain, if_reward, *elif_conditions, *elif_rewards, else_reward])

        reward_function = RewardFunction(
            reward=lambda *args, **kwargs: conditional_reward_function(if_condition, if_reward, elif_conditions,
                                                                       elif_rewards, else_reward, *args, **kwargs),
            domain=domain)

        # TODO: Break up into rewards, transitions, and predictions, and then construct them together into a single Effect

        new_effect = Effect(reward_function=reward_function)
        ctx.value = new_effect

    # def exitStochastic_effect(self, ctx: RLangParser.Stochastic_effectContext):
    #     probability = ctx.any_number().value
    #     if probability > 1.0 or probability < 0.0:
    #         raise RLangSemanticError("Effect probability must be between 0.0 and 1.0")
    #     stats = []
    #     for s in ctx.stats:
    #         if isinstance(s.value, list):
    #             stats.extend(s.value)
    #         else:
    #             stats.append(s.value)
    #
    #     for s in stats:
    #         s.compose_probability(probability)
    #
    #     ctx.value = stats

    # def exitConditional_effect_stat(self, ctx: RLangParser.Conditional_effect_statContext):
    #     # A conditional_effect_stat has a value which is a list of other stat types. Add these back to ctx.xx_statements
    #     ifs = list(filter(lambda x: isinstance(x, list), map(lambda x: x.value, ctx.if_statements)))
    #     if ifs:
    #         ifs = list(reduce(lambda a, b: a + b, ifs))
    #     elifs = list(filter(lambda x: isinstance(x, list), map(lambda x: x.value, ctx.elif_statements)))
    #     if elifs:
    #         elifs = list(reduce(lambda a, b: a + b, elifs))
    #     elses = list(filter(lambda x: isinstance(x, list), map(lambda x: x.value, ctx.else_statements)))
    #     if elses:
    #         elses = list(reduce(lambda a, b: a + b, elses))
    #
    #     ctx.if_statements = list(
    #         filter(lambda x: not isinstance(x, list), map(lambda y: y.value, ctx.if_statements))) + ifs
    #     ctx.elif_statements = list(
    #         filter(lambda x: not isinstance(x, list), map(lambda y: y.value, ctx.elif_statements))) + elifs
    #     ctx.else_statements = list(
    #         filter(lambda x: not isinstance(x, list), map(lambda y: y.value, ctx.else_statements))) + elses
    #
    #     transition_function = build_conditional_stat(ctx, TransitionFunction)
    #     reward_function = build_conditional_stat(ctx, RewardFunction)
    #
    #     prediction_names = list(set(list(map(lambda y: y.grounding_predicted.name,
    #                                          filter(lambda x: isinstance(x, Prediction),
    #                                                 [*ctx.if_statements, *ctx.elif_statements,
    #                                                  *ctx.else_statements])))))
    #     predictions = []
    #     for p_name in prediction_names:
    #         new_p_function = build_conditional_stat(ctx, Prediction,
    #                                                 name_filter=lambda x: x.grounding_predicted.name == p_name)
    #         new_prediction = Prediction(grounding_function=self.retrieveVariable(p_name),
    #                                     value=new_p_function)
    #         predictions.append(new_prediction)
    #     ctx.value = [TransitionFunction(function=transition_function), RewardFunction(reward=reward_function),
    #                  *predictions]

    # ============================= arithmetic expression =============================

    def exitArith_paren(self, ctx: RLangParser.Arith_parenContext):
        ctx.value = ctx.arithmetic_exp().value

    def exitArith_times_divide(self, ctx: RLangParser.Arith_times_divideContext):
        if isinstance(ctx.lhs.value, GroundingFunction) or isinstance(ctx.rhs.value, GroundingFunction):
            if ctx.TIMES() is not None:
                ctx.value = ctx.lhs.value * ctx.rhs.value
            elif ctx.DIVIDE() is not None:
                ctx.value = ctx.lhs.value / ctx.rhs.value

    def exitArith_plus_minus(self, ctx: RLangParser.Arith_plus_minusContext):
        if isinstance(ctx.lhs.value, GroundingFunction) or isinstance(ctx.rhs.value, GroundingFunction):
            if ctx.PLUS() is not None:
                ctx.value = ctx.lhs.value + ctx.rhs.value
            elif ctx.MINUS() is not None:
                ctx.value = ctx.lhs.value - ctx.rhs.value

    def exitArith_number(self, ctx: RLangParser.Arith_numberContext):
        ctx.value = PrimitiveGrounding(codomain=Domain.REAL_VALUE, value=ctx.any_number().value)

    def exitArith_array(self, ctx: RLangParser.Arith_arrayContext):
        ctx.value = PrimitiveGrounding(codomain=Domain.REAL_VALUE, value=ctx.any_array().value)

    def exitArith_bound_var(self, ctx: RLangParser.Arith_bound_varContext):
        if not isinstance(ctx.any_bound_var().value,
                          (IdentityGrounding, ConstantGrounding, Factor, Feature, Policy, ActionReference)):
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
        ctx.value = ctx.rhs.value.contains(ctx.lhs.value)

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
                    ctx.value = Feature(function=lambda *args, **kwargs: new_var(state=kwargs['next_state']),
                                        domain=Domain.NEXT_STATE)
            else:
                raise RLangSemanticError(
                    f"Cannot use the ' operator on a {type(ctx.value)} with domain {ctx.value.domain.name}")
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

    def exitAny_array_compound(self, ctx: RLangParser.Any_array_compoundContext):
        ctx.value = ctx.compound_array_exp().value

    def exitAny_array_any_num(self, ctx: RLangParser.Any_array_any_numContext):
        ctx.value = ctx.any_num_array_exp().value

    def exitCompound_array_simple(self, ctx: RLangParser.Compound_array_simpleContext):
        ctx.value = ctx.any_num_array_exp().value

    def exitCompound_array_compound(self, ctx: RLangParser.Compound_array_compoundContext):
        # This may be problematic
        # array_value = []
        # same_size = True
        # size = None
        # for item in ctx.arr:
        #     if size is None:
        #         array_value.append(item.value)
        #         size = item.size
        #     elif size != item.size:
        #         same_size = False
        ctx.value = list(map(lambda x: x.value, ctx.arr))

    def exitInt_array_exp(self, ctx: RLangParser.Int_array_expContext):
        ctx.value = list(map(lambda x: x.value, ctx.arr))
        # ctx.len = len(ctx.arr)

    def exitAny_num_array_exp(self, ctx: RLangParser.Any_num_array_expContext):
        ctx.value = list(map(lambda x: x.value, ctx.arr))
        # ctx.len = len(ctx.arr)

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

    def exitInteger_fraction(self, ctx: RLangParser.Integer_fractionContext):
        if ctx.rhs.value == 0:
            raise RLangSemanticError("Divide by 0 error")
        ctx.value = float(ctx.lhs.value) / float(ctx.rhs.value)

    def exitAny_num_int(self, ctx: RLangParser.Any_num_intContext):
        ctx.value = ctx.any_integer().value

    def exitAny_num_dec(self, ctx: RLangParser.Any_num_decContext):
        ctx.value = ctx.any_decimal().value

    def enterAny_integer(self, ctx: RLangParser.Any_integerContext):
        ctx.value = int(ctx.getText())

    def enterAny_decimal(self, ctx: RLangParser.Any_decimalContext):
        ctx.value = float(ctx.getText())
