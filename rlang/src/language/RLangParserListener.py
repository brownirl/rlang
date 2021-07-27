# Generated from RLangParser.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RLangParser import RLangParser
else:
    from RLangParser import RLangParser

# This class defines a complete listener for a parse tree produced by RLangParser.
class RLangParserListener(ParseTreeListener):

    # Enter a parse tree produced by RLangParser#program.
    def enterProgram(self, ctx:RLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by RLangParser#program.
    def exitProgram(self, ctx:RLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by RLangParser#imports.
    def enterImports(self, ctx:RLangParser.ImportsContext):
        pass

    # Exit a parse tree produced by RLangParser#imports.
    def exitImports(self, ctx:RLangParser.ImportsContext):
        pass


    # Enter a parse tree produced by RLangParser#import_stat.
    def enterImport_stat(self, ctx:RLangParser.Import_statContext):
        pass

    # Exit a parse tree produced by RLangParser#import_stat.
    def exitImport_stat(self, ctx:RLangParser.Import_statContext):
        pass


    # Enter a parse tree produced by RLangParser#declarations.
    def enterDeclarations(self, ctx:RLangParser.DeclarationsContext):
        pass

    # Exit a parse tree produced by RLangParser#declarations.
    def exitDeclarations(self, ctx:RLangParser.DeclarationsContext):
        pass


    # Enter a parse tree produced by RLangParser#dec.
    def enterDec(self, ctx:RLangParser.DecContext):
        pass

    # Exit a parse tree produced by RLangParser#dec.
    def exitDec(self, ctx:RLangParser.DecContext):
        pass


    # Enter a parse tree produced by RLangParser#factor.
    def enterFactor(self, ctx:RLangParser.FactorContext):
        pass

    # Exit a parse tree produced by RLangParser#factor.
    def exitFactor(self, ctx:RLangParser.FactorContext):
        pass


    # Enter a parse tree produced by RLangParser#feature.
    def enterFeature(self, ctx:RLangParser.FeatureContext):
        pass

    # Exit a parse tree produced by RLangParser#feature.
    def exitFeature(self, ctx:RLangParser.FeatureContext):
        pass


    # Enter a parse tree produced by RLangParser#predicate.
    def enterPredicate(self, ctx:RLangParser.PredicateContext):
        pass

    # Exit a parse tree produced by RLangParser#predicate.
    def exitPredicate(self, ctx:RLangParser.PredicateContext):
        pass


    # Enter a parse tree produced by RLangParser#action.
    def enterAction(self, ctx:RLangParser.ActionContext):
        pass

    # Exit a parse tree produced by RLangParser#action.
    def exitAction(self, ctx:RLangParser.ActionContext):
        pass


    # Enter a parse tree produced by RLangParser#goal.
    def enterGoal(self, ctx:RLangParser.GoalContext):
        pass

    # Exit a parse tree produced by RLangParser#goal.
    def exitGoal(self, ctx:RLangParser.GoalContext):
        pass


    # Enter a parse tree produced by RLangParser#markov_feature.
    def enterMarkov_feature(self, ctx:RLangParser.Markov_featureContext):
        pass

    # Exit a parse tree produced by RLangParser#markov_feature.
    def exitMarkov_feature(self, ctx:RLangParser.Markov_featureContext):
        pass


    # Enter a parse tree produced by RLangParser#effect.
    def enterEffect(self, ctx:RLangParser.EffectContext):
        pass

    # Exit a parse tree produced by RLangParser#effect.
    def exitEffect(self, ctx:RLangParser.EffectContext):
        pass


    # Enter a parse tree produced by RLangParser#option.
    def enterOption(self, ctx:RLangParser.OptionContext):
        pass

    # Exit a parse tree produced by RLangParser#option.
    def exitOption(self, ctx:RLangParser.OptionContext):
        pass


    # Enter a parse tree produced by RLangParser#policy.
    def enterPolicy(self, ctx:RLangParser.PolicyContext):
        pass

    # Exit a parse tree produced by RLangParser#policy.
    def exitPolicy(self, ctx:RLangParser.PolicyContext):
        pass


    # Enter a parse tree produced by RLangParser#effect_stat.
    def enterEffect_stat(self, ctx:RLangParser.Effect_statContext):
        pass

    # Exit a parse tree produced by RLangParser#effect_stat.
    def exitEffect_stat(self, ctx:RLangParser.Effect_statContext):
        pass


    # Enter a parse tree produced by RLangParser#reward.
    def enterReward(self, ctx:RLangParser.RewardContext):
        pass

    # Exit a parse tree produced by RLangParser#reward.
    def exitReward(self, ctx:RLangParser.RewardContext):
        pass


    # Enter a parse tree produced by RLangParser#assignment.
    def enterAssignment(self, ctx:RLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by RLangParser#assignment.
    def exitAssignment(self, ctx:RLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by RLangParser#constant.
    def enterConstant(self, ctx:RLangParser.ConstantContext):
        pass

    # Exit a parse tree produced by RLangParser#constant.
    def exitConstant(self, ctx:RLangParser.ConstantContext):
        pass


    # Enter a parse tree produced by RLangParser#policy_stat.
    def enterPolicy_stat(self, ctx:RLangParser.Policy_statContext):
        pass

    # Exit a parse tree produced by RLangParser#policy_stat.
    def exitPolicy_stat(self, ctx:RLangParser.Policy_statContext):
        pass


    # Enter a parse tree produced by RLangParser#execute.
    def enterExecute(self, ctx:RLangParser.ExecuteContext):
        pass

    # Exit a parse tree produced by RLangParser#execute.
    def exitExecute(self, ctx:RLangParser.ExecuteContext):
        pass


    # Enter a parse tree produced by RLangParser#arithmetic_exp.
    def enterArithmetic_exp(self, ctx:RLangParser.Arithmetic_expContext):
        pass

    # Exit a parse tree produced by RLangParser#arithmetic_exp.
    def exitArithmetic_exp(self, ctx:RLangParser.Arithmetic_expContext):
        pass


    # Enter a parse tree produced by RLangParser#boolean_exp.
    def enterBoolean_exp(self, ctx:RLangParser.Boolean_expContext):
        pass

    # Exit a parse tree produced by RLangParser#boolean_exp.
    def exitBoolean_exp(self, ctx:RLangParser.Boolean_expContext):
        pass


    # Enter a parse tree produced by RLangParser#array.
    def enterArray(self, ctx:RLangParser.ArrayContext):
        pass

    # Exit a parse tree produced by RLangParser#array.
    def exitArray(self, ctx:RLangParser.ArrayContext):
        pass


    # Enter a parse tree produced by RLangParser#slice.
    def enterSlice(self, ctx:RLangParser.SliceContext):
        pass

    # Exit a parse tree produced by RLangParser#slice.
    def exitSlice(self, ctx:RLangParser.SliceContext):
        pass


    # Enter a parse tree produced by RLangParser#array_exp.
    def enterArray_exp(self, ctx:RLangParser.Array_expContext):
        pass

    # Exit a parse tree produced by RLangParser#array_exp.
    def exitArray_exp(self, ctx:RLangParser.Array_expContext):
        pass


    # Enter a parse tree produced by RLangParser#slice_exp.
    def enterSlice_exp(self, ctx:RLangParser.Slice_expContext):
        pass

    # Exit a parse tree produced by RLangParser#slice_exp.
    def exitSlice_exp(self, ctx:RLangParser.Slice_expContext):
        pass


    # Enter a parse tree produced by RLangParser#any_integer.
    def enterAny_integer(self, ctx:RLangParser.Any_integerContext):
        pass

    # Exit a parse tree produced by RLangParser#any_integer.
    def exitAny_integer(self, ctx:RLangParser.Any_integerContext):
        pass



del RLangParser