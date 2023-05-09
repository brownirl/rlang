from __future__ import annotations
from functools import reduce
import json

from ..grounding.groundings import *
from ..grounding.utils.primitives import *

from .utils.language_exceptions import AlreadyBoundError, UnknownVariableError, RLangSemanticError
from .utils.semantic_schemas import conditional_policy_function, conditional_reward_function, \
    conditional_transition_function, conditional_prediction_function
from .utils.vocabulary_assembler import VocabularyAssembler
from .utils.custom_class import object_class_constructor

from .RLangParser import RLangParser
from .RLangParserListener import RLangParserListener

from typing import TYPE_CHECKING, List, Set

if TYPE_CHECKING:
    from rlang.knowledge import RLangKnowledge


class RLangListener(RLangParserListener):
    def __init__(self, prior_knowledge: RLangKnowledge):

        self.vocab_fnames = []
        self.grounded_vars = {}
        self.rlang_knowledge = prior_knowledge

    # This function adds the lmdp objects in the vocabulary files to self.grounded_vars
    # And probably keep track of object names in the vocab for later reference from the rlang file
    def parseVocabFiles(self):
        def parseVocabFile(file: str):
            with open(file, 'r') as f:
                vocab = json.load(f)
                # I'm not sure if this is best practice, maybe I should make VocabularyAssembler a util function
                voc_assembler = VocabularyAssembler(vocab)
                self.grounded_vars.update(voc_assembler.lmdp_objects)
                # TODO: Augment voc_assembler to get classes
                # self.grounded_classes.update(voc_assembler.something)

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
        if variable_name == 'main_policy' and not isinstance(variable, Policy):
            raise RLangSemanticError("'main_policy' is a reserved RLang variable name")
        if variable_name == 'main_plan' and not isinstance(variable, Plan):
            raise RLangSemanticError("'main_plan' is a reserved RLang variable name")
        if variable_name == 'main_effect' and not isinstance(variable, Effect):
            raise RLangSemanticError("'main_effect' is a reserved RLang variable name")

        if variable_name in self.rlang_knowledge.keys() or variable_name in self.grounded_vars.keys():
            raise AlreadyBoundError(variable_name)
        self.rlang_knowledge.update({variable_name: variable})

        if variable_name == 'main_policy':
            self.rlang_knowledge.policy = variable

        if variable_name == 'main_plan':
            self.rlang_knowledge.plan = variable

        if variable_name == 'main_effect':
            self.rlang_knowledge.reward_function = variable.reward_function
            self.rlang_knowledge.transition_function = variable.transition_function
            self.rlang_knowledge.proto_predictions = variable.predictions

    def enterProgram(self, ctx: RLangParser.ProgramContext):
        if ctx.getText() == "":
            raise RLangSemanticError("No program text. There might be some misplaced quotes.")

    def exitProgram(self, ctx: RLangParser.ProgramContext):
        self.rlang_knowledge.update(self.grounded_vars)

    def enterImport_stat(self, ctx: RLangParser.Import_statContext):
        self.vocab_fnames.append(ctx.FNAME().getText()[1:-1])

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
            # if isinstance(new_factor.indexer, slice):
            #     if self.mdp_metadata is not None:
            #         new_factor.indexer = list(
            #             range(*new_factor.indexer.indices(self.mdp_metadata.state_space.shape[0])))
        elif isinstance(ctx.any_bound_var().value, IdentityGrounding):
            raise RLangSemanticError("A Factor must subscript from S or another Factor")
        else:
            raise RLangSemanticError(f"Cannot construct Factor with object type {type(ctx.any_bound_var().value)}")
        self.addVariable(new_factor.name, new_factor)

    def exitProposition(self, ctx: RLangParser.PropositionContext):
        new_proposition = ctx.boolean_exp().value
        new_proposition.name = ctx.IDENTIFIER().getText()
        self.addVariable(new_proposition.name, new_proposition)

    def exitGoal(self, ctx: RLangParser.GoalContext):
        new_goal = ctx.boolean_exp().value
        new_goal.__class__ = Goal
        new_goal.name = ctx.IDENTIFIER().getText()
        self.addVariable(new_goal.name, new_goal)

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

    def exitObject_def(self, ctx: RLangParser.Object_defContext):
        obj = ctx.lifted_execution().value
        obj.name = ctx.IDENTIFIER().getText()
        obj.obj.name = ctx.IDENTIFIER().getText()
        self.addVariable(ctx.IDENTIFIER().getText(), obj)

    def exitClass_def(self, ctx: RLangParser.Class_defContext):
        bases = (MDPObject,)
        if ctx.any_bound_class() is not None:
            bases = (ctx.any_bound_class().value,)
        self.addVariable(ctx.IDENTIFIER().getText(),
                         object_class_constructor(ctx.IDENTIFIER().getText(), bases,
                                                  *ctx.attribute_definition_collection().value))

    def exitAttribute_definition_collection(self, ctx: RLangParser.Attribute_definition_collectionContext):
        attributes = {}
        attribute_order_list = list()
        i = 0
        for item in ctx.definitions:
            item = item.value
            if item[0] in attributes.keys():
                raise RLangSemanticError("Attributes must have unique names for a given Class")
            else:
                attributes.update({item[0]: item[1]})
                attribute_order_list.append(item[0])
                i += 1
        ctx.value = (attributes, attribute_order_list)

    def exitAttribute_definition(self, ctx: RLangParser.Attribute_definitionContext):
        ctx.value = (ctx.IDENTIFIER().getText(), ctx.type_def().value)

    # ============================= Option =============================

    def exitOption(self, ctx: RLangParser.OptionContext):
        subpolicy = Policy.from_action_distribution(ctx.policy_statement().value)
        new_option = Option(initiation=ctx.init.value, termination=ctx.until.value, policy=subpolicy,
                            name=ctx.IDENTIFIER().getText())
        self.addVariable(new_option.name, new_option)

    def exitOption_condition(self, ctx: RLangParser.Option_conditionContext):
        if ctx.boolean_exp():
            ctx.value = ctx.boolean_exp().value
        else:
            ctx.value = Proposition.TRUE()

    # ============================= Policy =============================

    def exitPolicy(self, ctx: RLangParser.PolicyContext):
        new_policy = Policy.from_action_distribution(ctx.policy_statement().value)
        if ctx.IDENTIFIER():
            new_policy.name = ctx.IDENTIFIER().getText()
            if new_policy.name == 'main_policy':
                raise RLangSemanticError("'main_policy' is a reserved RLang variable name")
        elif ctx.MAIN():
            new_policy.name = 'main_policy'
        self.addVariable(new_policy.name, new_policy)

    def exitPolicy_statement_execute(self, ctx: RLangParser.Policy_statement_executeContext):
        if isinstance(ctx.execute().value, Plan):
            raise RLangSemanticError("Cannot execute a Plan in a Policy")
        ctx.value = ActionDistribution.from_single(ctx.execute().value)

    def exitPolicy_statement_conditional(self, ctx: RLangParser.Policy_statement_conditionalContext):
        ctx.value = ctx.conditional_subpolicy().value

    def exitPolicy_statement_probabilistic(self, ctx: RLangParser.Policy_statement_probabilisticContext):
        ctx.value = ctx.probabilistic_subpolicy().value

    def exitConditional_subpolicy(self, ctx: RLangParser.Conditional_subpolicyContext):
        elif_conditions = [s.value for s in ctx.elif_conditions]
        elif_subpolicies = [s.value for s in ctx.elif_subpolicies]
        else_subpolicy = ctx.else_subpolicy.value if ctx.else_subpolicy else None
        ctx.value = ActionDistribution.from_single(Policy(
            function=lambda *args, **kwargs: conditional_policy_function(ctx.if_condition.value, ctx.if_subpolicy.value,
                                                                         elif_conditions,
                                                                         elif_subpolicies, else_subpolicy, *args,
                                                                         **kwargs)))

    def exitProbabilistic_subpolicy(self, ctx: RLangParser.Probabilistic_subpolicyContext):
        action_distribution = ActionDistribution()
        [action_distribution.join(sp.value) for sp in ctx.subpolicies]
        ctx.value = action_distribution

    def exitProbabilistic_policy_statement_no_sugar(self,
                                                    ctx: RLangParser.Probabilistic_policy_statement_no_sugarContext):
        ctx.value = ctx.policy_statement().value
        ctx.value.compose_probabilities(ctx.probabilistic_condition().value)

    def exitProbabilistic_policy_statement_sugar(self, ctx: RLangParser.Probabilistic_policy_statement_sugarContext):
        ctx.value = ActionDistribution({ctx.execute().value: ctx.probabilistic_condition().value})

    def exitExecute(self, ctx: RLangParser.ExecuteContext):
        if ctx.IDENTIFIER() is not None:
            variable = self.retrieveVariable(ctx.IDENTIFIER().getText())
            if not isinstance(variable, (Policy, ActionReference, Plan)):
                raise RLangSemanticError(f"Cannot execute a {type(variable)}")
            ctx.value = variable
            if isinstance(variable, Plan):
                ctx.value = PlanExecution(variable)
        elif ctx.arithmetic_exp() is not None:
            if isinstance(ctx.arithmetic_exp().value, PlanExecution):
                ctx.value = ctx.arithmetic_exp().value
            else:
                ctx.value = ActionReference(action=ctx.arithmetic_exp().value)
        else:
            raise RLangSemanticError("Execute statement must have either an identifier or an arithmetic expression")

    # ============================= Lifted Execution (Parameterized Action, Predicate, and Plan) ===============

    def exitLifted_execution(self, ctx: RLangParser.Lifted_executionContext):
        lifted_execution = self.retrieveVariable(ctx.IDENTIFIER().getText())
        if isinstance(lifted_execution, ParameterizedAction):
            args = list(map(lambda x: x.value, ctx.arr))
            ctx.value = ParameterizedActionExecution(lifted_execution, args)
        elif isinstance(lifted_execution, Predicate):
            args = list(map(lambda x: x.value, ctx.arr))
            ctx.value = PredicateEvaluation(lifted_execution, args)
        elif isinstance(lifted_execution, Plan):
            args = list(map(lambda x: x.value, ctx.arr))
            ctx.value = PlanExecution(lifted_execution, args)
        elif isinstance(lifted_execution, type):
            args = list(map(lambda x: x.value, ctx.arr))
            args = [ctx.IDENTIFIER().getText()] + args
            ctx.value = MDPObjectGrounding(obj=lifted_execution(*args))
        else:
            raise RLangSemanticError(f"Cannot pass arguments to a {type(lifted_execution)}")

    # ============================= Plans =============================

    def exitPlan(self, ctx: RLangParser.PlanContext):
        # ctx.plan_statement_collection().value is a list of ActionDistributions for now
        new_plan = ctx.plan_statement_collection().value
        if ctx.IDENTIFIER():
            new_plan.name = ctx.IDENTIFIER().getText()
            if new_plan.name == 'main_plan':
                raise RLangSemanticError("'main_plan' is a reserved RLang variable name")
        elif ctx.MAIN():
            new_plan.name = 'main_plan'
        self.addVariable(new_plan.name, new_plan)

    def exitPlan_statement_collection(self, ctx: RLangParser.Plan_statement_collectionContext):
        # I need to make the plan object in here!
        # However, not all statements will be ActionDistributions, some will be probabilistic and some will be conditional TODO
        all_statements = [statement.value for statement in ctx.statements]
        ctx.value = IteratedPlan(all_statements)

    def exitPlan_statement_execute(self, ctx: RLangParser.Plan_statement_executeContext):
        if isinstance(ctx.execute().value, Plan):
            ctx.value = PlanExecution(ctx.execute().value)
        elif isinstance(ctx.execute().value, PlanExecution):
            ctx.value = ctx.execute().value
        else:
            ctx.value = ActionDistribution.from_single(ctx.execute().value)

    def exitPlan_statement_conditional(self, ctx: RLangParser.Plan_statement_conditionalContext):
        ctx.value = ctx.conditional_plan().value

    def exitPlan_statement_probabilistic(self, ctx: RLangParser.Plan_statement_probabilisticContext):
        ctx.value = ctx.probabilistic_plan().value

    def exitConditional_plan(self, ctx: RLangParser.Conditional_planContext):
        # This returns a plan given a state
        if_condition = ctx.if_condition.value
        elif_conditions = [s.value for s in ctx.elif_conditions]
        elif_plans = [s.value for s in ctx.elif_plans]
        else_plan = ctx.else_plan.value if ctx.else_plan else None

        # Right now these are mixed types, I don't want to do this right now TODO

    def exitProbabilistic_plan(self, ctx: RLangParser.Probabilistic_planContext):
        raise NotImplementedError("Probabilistic plans are not yet implemented")
        pass

    def exitProbabilistic_plan_statement_no_sugar(self, ctx: RLangParser.Probabilistic_plan_statement_no_sugarContext):
        pass

    def exitProbabilistic_plan_statement_sugar(self, ctx: RLangParser.Probabilistic_plan_statement_sugarContext):
        pass

    # ============================= Effect =============================

    def exitEffect(self, ctx: RLangParser.EffectContext):
        new_effect = ctx.effect_statement_collection().value
        if ctx.IDENTIFIER():
            new_effect.name = ctx.IDENTIFIER().getText()
            if new_effect.name == 'main_effect':
                raise RLangSemanticError("'main_effect' is a reserved RLang variable name")
        elif ctx.MAIN():
            new_effect.name = 'main_effect'
        self.addVariable(new_effect.name, new_effect)

    def exitEffect_statement_collection(self, ctx: RLangParser.Effect_statement_collectionContext):
        all_statements = [statement.value for statement in ctx.statements]

        # Effect references
        effects = list(filter(lambda x: isinstance(x, Effect), all_statements))
        effect_transitions = list()
        effect_rewards = list()
        effect_predictions = list()

        for e in effects:
            if e.transition_function is not None:
                effect_transitions.append(e.transition_function)
            if e.predictions:
                effect_predictions.extend(e.predictions)
            if e.reward_function is not None:
                effect_rewards.append(e.reward_function)

        # print("effect predictions:", effect_predictions)

        # print("effect predictions complete?", [p.complete for p in effect_predictions])

        # TransitionFunctions
        transition_functions = list(filter(lambda x: isinstance(x, TransitionFunction), all_statements))
        transition_functions.extend(effect_transitions)
        state_distributions = list(filter(lambda x: isinstance(x, StateDistribution), all_statements))

        combined_sd = StateDistribution()
        [combined_sd.join(sd) for sd in state_distributions]
        transition_functions.append(TransitionFunction.from_state_distribution(combined_sd))

        transition_function = TransitionFunction.from_state_distribution(
            StateDistribution.from_list_eq(transition_functions))

        # Rewards
        reward_functions = list(filter(lambda x: isinstance(x, RewardFunction), all_statements))
        reward_functions.extend(effect_rewards)
        reward_distributions = list(filter(lambda x: isinstance(x, RewardDistribution), all_statements))
        reward_function = None

        if len(reward_distributions) > 0:
            combined_rd = RewardDistribution()
            [combined_rd.join(rd) for rd in reward_distributions]
            reward_functions.append(RewardFunction.from_reward_distribution(combined_rd))
        if len(reward_functions) > 0:
            rd = RewardDistribution.from_list_eq(reward_functions)
            reward_function = RewardFunction.from_reward_distribution(rd)

        # Predictions
        predictions = list(filter(lambda x: isinstance(x, Prediction), all_statements))
        predictions.extend(effect_predictions)
        grounding_distributions = list(filter(lambda x: isinstance(x, GroundingDistribution), all_statements))

        # is_complete = any([gd.complete for gd in grounding_distributions]) or any([p.complete for p in predictions])

        predicted_groundings = list(
            {*[p.grounding for p in predictions], *[gd.grounding for gd in grounding_distributions]})

        # print([gd.complete for gd in grounding_distributions], [p.complete for p in predictions])
        # # print(is_complete)
        # print(predicted_groundings)
        # print([type(pg) for pg in predicted_groundings])

        new_predictions = list()
        for grounding in predicted_groundings:
            predictions_g = list(filter(lambda x: x.grounding.equals(grounding), predictions))
            # print(predictions_g)

            combined_gd = GroundingDistribution(grounding)
            [combined_gd.join(gd) for gd in
             list(filter(lambda x: x.grounding.equals(grounding), grounding_distributions))]

            predictions_g.append(Prediction.from_grounding_distribution(grounding, combined_gd))

            prediction = Prediction.from_grounding_distribution(grounding,
                                                                GroundingDistribution.from_list_eq(predictions_g,
                                                                                                   grounding))
            # print(prediction.complete)
            new_predictions.append(prediction)


        print(new_predictions)

        # print("predictions complete?", [new_p.complete for new_p in new_predictions])

        ctx.value = Effect(reward_function=reward_function, transition_function=transition_function,
                           predictions=new_predictions)

        # print(ctx.value.predictions)

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

    def exitConditional_effect(self, ctx: RLangParser.Conditional_effectContext):
        if_condition = ctx.if_condition.value
        if_effect = ctx.if_effect.value
        elif_conditions = [s.value for s in ctx.elif_conditions]
        elif_effects = [s.value for s in ctx.elif_effects]
        else_effect = ctx.else_effect.value if ctx.else_effect else Effect()

        # Rewards
        if_reward = if_effect.reward_function
        elif_rewards = [elif_effect.reward_function for elif_effect in elif_effects]
        else_reward = else_effect.reward_function

        reward_function = None
        rstats = [x for x in [if_reward, *elif_rewards, else_reward] if x]

        if len(rstats) > 0:
            domain = reduce(lambda a, b: a + b.domain, list(filter(lambda x: x is not None,
                                                                   [if_condition.domain if not isinstance(if_condition,
                                                                                                          bool) else Domain.ANY,
                                                                    if_reward, *elif_conditions,
                                                                    *elif_rewards, else_reward])))
            if isinstance(if_condition, bool):
                if_condition = PrimitiveGrounding(codomain=Domain.BOOLEAN, value=if_condition)
            reward_func = RewardFunction(
                lambda *args, **kwargs: conditional_reward_function(if_condition, if_reward, elif_conditions,
                                                                    elif_rewards, else_reward, *args, **kwargs),
                domain=domain)
            # TODO: I'm not sure this is necessary
            reward_function = RewardFunction.from_reward_distribution(RewardDistribution.from_single(reward_func))

        # TransitionFunctions
        if_transition = if_effect.transition_function
        elif_transitions = [elif_effect.transition_function for elif_effect in elif_effects]
        else_transition = else_effect.transition_function

        transition_function = None
        tstats = [x for x in [if_transition, *elif_transitions, else_transition] if x]

        if len(tstats) > 0:
            domain2 = reduce(lambda a, b: a + b.domain,
                             list(filter(lambda x: x is not None,
                                         [if_condition.domain if not isinstance(if_condition, bool) else Domain.ANY,
                                          if_transition, *elif_conditions, *elif_transitions,
                                          else_transition])))

            transition_function = TransitionFunction(
                function=lambda *args, **kwargs: conditional_transition_function(if_condition, if_transition,
                                                                                 elif_conditions, elif_transitions,
                                                                                 else_transition, *args, **kwargs),
                domain=domain2)
            # TODO: I'm not sure this is necessary
            transition_function = TransitionFunction.from_state_distribution(
                StateDistribution.from_single(transition_function))

        # Predictions
        if_predictions = if_effect.predictions
        elif_predictions = [elif_effect.predictions for elif_effect in elif_effects]
        else_predictions = else_effect.predictions

        all_predictions = list()
        all_predictions.extend(if_predictions)
        for preds in elif_predictions:
            all_predictions.extend(preds)
        all_predictions.extend(else_predictions)

        # print("conditional complete:", [p.complete for p in all_predictions])

        domain3 = reduce(lambda a, b: a + b.domain,
                         [if_condition.domain if not isinstance(if_condition, bool) else Domain.ANY, *elif_conditions])

        predicted_groundings = list({pred.grounding for pred in all_predictions})
        new_predictions = list()

        for grounding in predicted_groundings:
            new_domain = Domain.ANY + domain3
            if_preds = list(filter(lambda x: x.grounding.equals(grounding), if_predictions))
            if len(if_preds) > 0:
                if_preds = GroundingDistribution.from_list_eq(if_preds, grounding)
                new_domain += if_preds.domain
            else:
                if_preds = None

            elif_preds = list()
            for preds in elif_predictions:
                e_preds = list(filter(lambda x: x.grounding.equals(grounding), preds))
                if len(e_preds) > 0:
                    e_preds = GroundingDistribution.from_list_eq(e_preds, grounding)
                    new_domain += e_preds.domain
                else:
                    e_preds = None
                elif_preds.append(e_preds)

            else_preds = list(filter(lambda x: x.grounding.equals(grounding), else_predictions))
            if len(else_preds) > 0:
                else_preds = GroundingDistribution.from_list_eq(else_preds, grounding)
                new_domain += else_preds.domain
            else:
                else_preds = None

            # This needs to be here for lambda scope reasons
            def construct_cond_pred_func(if_cond_f, if_pred_f, elif_conds_f, elif_preds_f, else_preds_f):
                return lambda *args, **kwargs: conditional_prediction_function(if_cond_f,
                                                                               if_pred_f,
                                                                               elif_conds_f,
                                                                               elif_preds_f,
                                                                               else_preds_f,
                                                                               *args, **kwargs)

            func = construct_cond_pred_func(if_condition,
                                            if_preds,
                                            elif_conditions,
                                            elif_preds,
                                            else_preds)


            new_prediction = Prediction(grounding, func, domain=new_domain)
            # TODO: I'm not sure this next line is necessary
            # new_prediction = Prediction.from_grounding_distribution(grounding,
            #                                                         GroundingDistribution(grounding=grounding,
            #                                                                               distribution={
            #                                                                                   new_prediction: 1.0}))
            new_predictions.append(new_prediction)

        ctx.value = Effect(reward_function=reward_function, transition_function=transition_function,
                           predictions=new_predictions)

    def exitProbabilistic_effect(self, ctx: RLangParser.Probabilistic_effectContext):
        # Rewards
        reward_statements = [statement.value.reward_function for statement in ctx.effects]
        reward_statements = list(filter(lambda x: x, reward_statements))
        if len(reward_statements) > 0:
            reward_function = RewardFunction.from_reward_distribution(
                RewardDistribution.from_list_eq(reward_statements))
        else:
            reward_function = None

        # TransitionFunctions
        transition_statements = [statement.value.transition_function for statement in ctx.effects]
        transition_statements = list(filter(lambda x: x, transition_statements))
        if len(transition_statements) > 0:
            transition_function = TransitionFunction.from_state_distribution(
                StateDistribution.from_list_eq(transition_statements))
        else:
            transition_function = None

        # Predictions
        prediction_statements = list()
        for statement in ctx.effects:
            prediction_statements.extend(statement.value.predictions)

        predicted_groundings = list({p.grounding for p in prediction_statements})
        new_predictions = list()

        for grounding in predicted_groundings:
            predictions_g = list(filter(lambda x: x.grounding.equals(grounding), prediction_statements))
            prediction = Prediction.from_grounding_distribution(grounding,
                                                                GroundingDistribution.from_list_eq(predictions_g,
                                                                                                   grounding))
            new_predictions.append(prediction)

        ctx.value = Effect(reward_function=reward_function, transition_function=transition_function,
                           predictions=new_predictions)

    def exitProbabilistic_effect_statement_no_sugar(self,
                                                    ctx: RLangParser.Probabilistic_effect_statement_no_sugarContext):
        ctx.value = ctx.effect_statement_collection().value
        ctx.value.compose_probabilities(ctx.probabilistic_condition().value)

    def exitProbabilistic_effect_statement_sugar(self, ctx: RLangParser.Probabilistic_effect_statement_sugarContext):
        if ctx.reward() is not None:
            reward_function = ctx.reward().value
            ctx.value = Effect(reward_function=reward_function)
        elif ctx.prediction() is not None:
            if isinstance(ctx.prediction().value, StateDistribution):
                ctx.value = Effect(
                    transition_function=TransitionFunction.from_state_distribution(ctx.prediction().value))
            elif isinstance(ctx.prediction().value, GroundingDistribution):
                ctx.value = Effect(predictions=[
                    Prediction.from_grounding_distribution(ctx.prediction().value.grounding, ctx.prediction().value)])
        else:
            ctx.value = ctx.effect_reference().value.shallow_copy()
        ctx.value.compose_probabilities(ctx.probabilistic_condition().value)

    def exitReward(self, ctx: RLangParser.RewardContext):
        if not ctx.arithmetic_exp().value.domain <= Domain.STATE_ACTION:
            raise RLangSemanticError(
                f"Cannot prescribe reward that is a function of {ctx.arithmetic_exp().value.domain}")
        elif ctx.arithmetic_exp().value.codomain != Domain.REAL_VALUE and ctx.arithmetic_exp().value.codomain != Domain.OBJECT_VALUE:
            raise RLangSemanticError(
                f"Cannot prescribe reward that is not numerical: {ctx.arithmetic_exp().value.codomain}")
        ctx.value = RewardDistribution.from_single(ctx.arithmetic_exp().value)

    def exitPrediction(self, ctx: RLangParser.PredictionContext):
        # Will probably need to adjust the parser to include identifiers with trailers. Then set grounding_function
        # to perhaps a new grounding function that unwraps MDPObjectGroundings, similar to StateObjectAttributeGrounding
        if ctx.IDENTIFIER() is not None:
            grounding_function = self.retrieveVariable(ctx.IDENTIFIER().getText())

            # TODO: implement semantics for when it's not just a variable but a property of a variable!

            if grounding_function.domain < Domain.STATE_ACTION_NEXT_STATE and ctx.PRIME() is None:
                raise RLangSemanticError("Use prime syntax to refer to the future state of variables")
            if ctx.arithmetic_exp() is not None:
                predicted_value = ctx.arithmetic_exp().value
            elif ctx.boolean_exp() is not None:
                predicted_value = ctx.boolean_exp().value
            else:
                predicted_value = ctx.lifted_execution().value

            if ctx.dot_exp() is not None:
                grounding_function = MDPObjectAttributeGrounding(grounding_function, ctx.dot_exp().value)

            # Okay, here is where I need to handle the predict_all operator. Perhaps I can simply insert it into the existing GroundingDistribution

            ctx.value = GroundingDistribution(grounding=grounding_function, distribution={predicted_value: 1.0},
                                              complete=False) # ctx.PREDICT_ALL() is not None) # I scrapped this idea for now
        elif ctx.S_PRIME() is not None:
            if ctx.dot_exp() is not None:
                # TODO: Should be a GroundingDistribution I think. May need to implement a new kind of distribution
                # that isn't numerical! A new subclass of ProbabilityDistrubution
                grounding_function = StateObjectAttributeGrounding(ctx.dot_exp().value, domain='next_state')
                if ctx.arithmetic_exp() is not None:
                    predicted_value = ctx.arithmetic_exp().value
                elif ctx.boolean_exp() is not None:
                    predicted_value = ctx.boolean_exp().value
                else:
                    predicted_value = ctx.lifted_execution().value
                ctx.value = GroundingDistribution(grounding=grounding_function, distribution={predicted_value: 1.0})
            else:
                if ctx.arithmetic_exp() is not None:
                    ctx.value = StateDistribution.from_single(ctx.arithmetic_exp().value)
                else:
                    raise RLangSemanticError("A state cannot be predicted to be an object")

    def exitEffect_reference(self, ctx: RLangParser.Effect_referenceContext):
        effect = self.retrieveVariable(ctx.IDENTIFIER().getText())
        if not isinstance(effect, Effect):
            raise RLangSemanticError(f"Can only use this syntax to reference Effects")
        ctx.value = effect

    def exitProbabilistic_condition(self, ctx: RLangParser.Probabilistic_conditionContext):
        if ctx.any_number():
            probability = ctx.any_number().value
        else:
            probability = ctx.integer_fraction().value
        if probability > 1.0 or probability < 0.0:
            raise RLangSemanticError("Probability must be between 0 and 1")
        ctx.value = probability

    # ============================= arithmetic expression =============================

    def exitArith_paren(self, ctx: RLangParser.Arith_parenContext):
        ctx.value = ctx.arithmetic_exp().value

    def exitArith_times_divide(self, ctx: RLangParser.Arith_times_divideContext):
        if isinstance(ctx.lhs.value, GroundingFunction) or isinstance(ctx.rhs.value, GroundingFunction):
            if ctx.TIMES() is not None:
                ctx.value = ctx.lhs.value * ctx.rhs.value
            elif ctx.DIVIDE() is not None:
                ctx.value = ctx.lhs.value / ctx.rhs.value

    def exitArith_quantification(self, ctx: RLangParser.Arith_quantificationContext):
        ctx.value = ctx.quantification_exp().value

    def exitArith_plus_minus(self, ctx: RLangParser.Arith_plus_minusContext):
        if isinstance(ctx.lhs.value, GroundingFunction) or isinstance(ctx.rhs.value, GroundingFunction):
            if ctx.PLUS() is not None:
                ctx.value = ctx.lhs.value + ctx.rhs.value
            elif ctx.MINUS() is not None:
                ctx.value = ctx.lhs.value - ctx.rhs.value

    # def exitObject_instantiation(self, ctx: RLangParser.Object_instantiationContext):
    #     args = [ctx.any_bound_class().value.__name__] + ctx.object_constructor_arg_list().value
    #     ctx.value = MDPObjectGrounding(obj=ctx.any_bound_class().value(*args))

    def exitObject_constructor_arg_list(self, ctx: RLangParser.Object_constructor_arg_listContext):
        ctx.value = list(map(lambda x: x.value, ctx.arg_list))

    def exitObject_construct_arith_exp(self, ctx: RLangParser.Object_construct_arith_expContext):
        ctx.value = ctx.arithmetic_exp().value

    def exitObject_construct_bool_exp(self, ctx: RLangParser.Object_construct_bool_expContext):
        ctx.value = ctx.boolean_exp().value

    def exitObject_construct_object(self, ctx: RLangParser.Object_construct_objectContext):
        ctx.value = ctx.an_object().value

    def exitObject_construct_object_array(self, ctx: RLangParser.Object_construct_object_arrayContext):
        ctx.value = ctx.object_array().value

    def exitAn_object(self, ctx: RLangParser.An_objectContext):
        if ctx.lifted_execution() is not None:
            ctx.value = ctx.lifted_execution().value
        elif ctx.any_bound_var() is not None and isinstance(ctx.any_bound_var().value, MDPObjectGrounding):
            ctx.value = ctx.any_bound_var().value
        else:
            raise RLangSemanticError("Must be an OOMDP object")

    # def exitPredicate_eval(self, ctx:RLangParser.Predicate_evalContext):
    #     args = list(map(lambda x: x.value, ctx.arr))
    #     predicate = self.retrieveVariable(ctx.IDENTIFIER().getText())
    #     if isinstance(predicate, Predicate):
    #         ctx.value = PredicateEvaluation(predicate, args)
    #     else:
    #         raise RLangSemanticError("Must be a predicate")

    def exitArith_number(self, ctx: RLangParser.Arith_numberContext):
        ctx.value = PrimitiveGrounding(codomain=Domain.REAL_VALUE, value=ctx.any_number().value)

    def exitArith_array(self, ctx: RLangParser.Arith_arrayContext):
        ctx.value = PrimitiveGrounding(codomain=Domain.REAL_VALUE, value=ctx.any_array().value)

    def exitArith_bound_var(self, ctx: RLangParser.Arith_bound_varContext):
        if not isinstance(ctx.any_bound_var().value,
                          (IdentityGrounding, ConstantGrounding, Factor, Feature, ActionReference,
                           StateObjectAttributeGrounding, MDPObjectGrounding, MDPObjectAttributeGrounding,
                           ParameterizedActionExecution, PredicateEvaluation, PlanExecution, MDPClassGrounding)):
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
        ctx.value = ctx.rhs.value.__contains__(ctx.lhs.value)

    def exitBool_bool_eq(self, ctx: RLangParser.Bool_bool_eqContext):
        if ctx.EQ_TO() is not None:
            ctx.value = ctx.lhs.value == ctx.rhs.value
        else:
            ctx.value = ctx.lhs.value == ctx.rhs.value

    def exitBool_arith_eq(self, ctx: RLangParser.Bool_arith_eqContext):
        if isinstance(ctx.rhs.value, QuantifierSpecification):
            lhs = ctx.rhs.value
            rhs = ctx.lhs.value
        else:
            lhs = ctx.lhs.value
            rhs = ctx.rhs.value

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

        # if lhs is a quantifier specification, construct a proposition from quantifier specification
        if isinstance(lhs, QuantifierSpecification):    # TODO: Eventually just work this logic into the Proposition class
            ctx.value = Proposition.from_QuantifierSpecification(quantifier_specification=lhs, grounding=rhs,
                                                           operation=bool_operation)
        else:
            ctx.value = bool_operation(lhs, rhs)

    def exitBool_bound_var(self, ctx: RLangParser.Bool_bound_varContext):
        if not isinstance(ctx.any_bound_var().value, (
                Proposition, PrimitiveGrounding, StateObjectAttributeGrounding, MDPObjectAttributeGrounding,
                PredicateEvaluation)):
            raise RLangSemanticError(f"This {type(ctx.any_bound_var().value)} does not have a truth value")
        if isinstance(ctx.any_bound_var().value, PrimitiveGrounding):
            ctx.value = Proposition.from_PrimitiveGrounding(primitive_grounding=ctx.any_bound_var().value)
        elif isinstance(ctx.any_bound_var().value,
                        (StateObjectAttributeGrounding, MDPObjectAttributeGrounding, PredicateEvaluation)):
            ctx.value = Proposition(function=ctx.any_bound_var().value.__call__, domain=Domain.BOOLEAN)
        else:
            ctx.value = ctx.any_bound_var().value

    def exitBool_tf(self, ctx: RLangParser.Bool_tfContext):
        if ctx.TRUE() is not None:
            ctx.value = Proposition.TRUE()
        elif ctx.FALSE() is not None:
            ctx.value = Proposition.FALSE()

    def exitQuantification_exp(self, ctx: RLangParser.Quantification_expContext):
        print(ctx.any_bound_class().value)
        ctx.value = QuantifierSpecification(cls=ctx.any_bound_class().value, quantifier=ctx.quantifier().value,
                                            dot_exp=ctx.dot_exp().value if ctx.dot_exp() else None)

    def exitQuantifier(self, ctx: RLangParser.QuantifierContext):
        if ctx.ALL_CONDITION() is not None:
            ctx.value = 'all'
        else:
            ctx.value = 'any'

    def exitType_def(self, ctx: RLangParser.Type_defContext):
        if ctx.compound_type() is not None:
            ctx.value = ctx.compound_type().value
        elif ctx.simple_type() is not None:
            ctx.value = ctx.simple_type().value

    def exitType_list(self, ctx: RLangParser.Type_listContext):
        if ctx.compound_type() is not None:
            ctx.value = List[ctx.compound_type().value]
        elif ctx.simple_type() is not None:
            ctx.value = List[ctx.simple_type().value]

    def exitType_set(self, ctx: RLangParser.Type_setContext):
        if ctx.compound_type() is not None:
            ctx.value = Set[ctx.compound_type().value]
        elif ctx.simple_type() is not None:
            ctx.value = Set[ctx.simple_type().value]

    def exitSimple_type(self, ctx: RLangParser.Simple_typeContext):
        if ctx.INT() is not None:
            ctx.value = int
        elif ctx.FLOAT() is not None:
            ctx.value = float
        elif ctx.STR() is not None:
            ctx.value = str
        elif ctx.BOOL() is not None:
            ctx.value = bool
        elif ctx.any_bound_class() is not None:
            ctx.value = ctx.any_bound_class().value

    def exitBound_identifier(self, ctx: RLangParser.Bound_identifierContext):
        variable = self.retrieveVariable(ctx.IDENTIFIER().getText())
        new_var = None

        # TODO: Trailer can now be a list of strings representing attributes!

        if not ctx.trailer():  # Check if it's not empty
            new_var = variable
            if isinstance(variable, type):
                new_var = MDPClassGrounding(cls=new_var)
        elif isinstance(variable, Factor):
            if len(ctx.trailer()) > 1:
                raise RLangSemanticError("Too much subscripting on Factor")
            # print(ctx.trailer()[0].value)
            new_var = variable[ctx.trailer()[0].value]
        elif isinstance(variable, Feature):
            if len(ctx.trailer()) > 1:
                raise RLangSemanticError("Too much subscripting on Feature")
            new_var = Feature(function=lambda *args, **kwargs: variable(*args, **kwargs)[ctx.trailer()[0].value],
                              domain=variable.domain)
        elif isinstance(variable, MDPObjectGrounding):

            # new_var = MDPObjectAttributeGrounding(variable, ctx.trailer())
            trailers = [trailer.value for trailer in ctx.trailer()]
            new_var = variable
            for trailer in trailers:
                if isinstance(trailer[0], str):
                    new_var = MDPObjectAttributeGrounding(new_var, trailer)
                elif isinstance(trailer[0], int):
                    new_var = Feature(function=lambda *args, **kwargs: new_var(*args, **kwargs)[trailer[0]],
                                      domain=new_var.domain)
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
                    f"Cannot use the ' operator on a {type(new_var)} with domain {new_var.domain.name}")
        else:
            ctx.value = new_var

    def exitBound_state(self, ctx: RLangParser.Bound_stateContext):
        if ctx.trailer() is not None:
            trailer = ctx.trailer().value
            if isinstance(trailer, slice) or isinstance(trailer, int):
                ctx.value = Factor(trailer)
            elif isinstance(trailer, list) and len(trailer) > 0:
                if isinstance(trailer[0], int):
                    ctx.value = Factor(trailer)
                else:
                    ctx.value = StateObjectAttributeGrounding(trailer)
            # The value of the attributes will technically be calculable at compiletime, since RLang object properties
            # are typed. But this means we'll also expect imported classes and their properties to be typed as well.
            # This may be too rigid.
        else:
            ctx.value = IdentityGrounding(Domain.STATE)

    def exitBound_next_state(self, ctx: RLangParser.Bound_next_stateContext):
        # TODO: Trailer can now be a list of strings representing attributes!
        #  Would prefer not to use this syntax: S'.something as opposed to S.something'

        if ctx.trailer() is not None:
            trailer = ctx.trailer().value
            if isinstance(trailer, slice) or isinstance(trailer, int):
                ctx.value = Factor(trailer, domain='next_state')
            elif isinstance(trailer, list) and len(trailer) > 0:
                if isinstance(trailer[0], int):
                    ctx.value = Factor(trailer, domain='next_state')
                else:
                    ctx.value = StateObjectAttributeGrounding(trailer, domain='next_state')
        else:
            ctx.value = IdentityGrounding(Domain.NEXT_STATE)

    def exitBound_action(self, ctx: RLangParser.Bound_actionContext):
        ctx.value = IdentityGrounding(Domain.ACTION)

    def exitBound_lifted_execution(self, ctx: RLangParser.Bound_lifted_executionContext):
        ctx.value = ctx.lifted_execution().value

    def exitAny_bound_class(self, ctx: RLangParser.Any_bound_classContext):
        ctx.value = self.retrieveVariable(ctx.IDENTIFIER().getText())

    def exitTrailer_array(self, ctx: RLangParser.Trailer_arrayContext):
        ctx.value = ctx.int_array_exp().value

    def exitTrailer_slice(self, ctx: RLangParser.Trailer_sliceContext):
        ctx.value = ctx.slice_exp().value

    def exitTrailer_object(self, ctx: RLangParser.Trailer_objectContext):
        ctx.value = ctx.dot_exp().value

    # def exitObject_array(self, ctx: RLangParser.Object_arrayContext):
    #     ctx.value = list(map(lambda x: x.value, ctx.arr))

    def exitDot_exp(self, ctx: RLangParser.Dot_expContext):
        ctx.value = list(map(lambda x: x.getText(), ctx.IDENTIFIER()))

    def exitAny_array_compound(self, ctx: RLangParser.Any_array_compoundContext):
        ctx.value = ctx.compound_array_exp().value

    def exitAny_array_any_num(self, ctx: RLangParser.Any_array_any_numContext):
        ctx.value = ctx.any_num_array_exp().value

    def exitCompound_array_simple(self, ctx: RLangParser.Compound_array_simpleContext):
        ctx.value = ctx.any_num_array_exp().value

    def exitCompound_array_arith(self, ctx: RLangParser.Compound_array_arithContext):
        gds = [x.value for x in ctx.arr]
        for i in range(len(gds)):
            if isinstance(gds[i], PrimitiveGrounding):
                gds[i] = gds[i]()

        ctx.value = gds

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
