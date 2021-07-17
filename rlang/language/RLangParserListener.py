# Generated from RLangParser.g4 by ANTLR 4.9.2
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .RLangParser import RLangParser
else:
    from RLangParser import RLangParser


# This class defines a complete listener for a parse tree produced by RLangParser.
class RLangParserListener(ParseTreeListener):

    # Enter a parse tree produced by RLangParser#program.
    def enterProgram(self, ctx: RLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by RLangParser#program.
    def exitProgram(self, ctx: RLangParser.ProgramContext):
        pass

    # Enter a parse tree produced by RLangParser#dec.
    def enterDec(self, ctx: RLangParser.DecContext):
        pass

    # Exit a parse tree produced by RLangParser#dec.
    def exitDec(self, ctx: RLangParser.DecContext):
        pass

    # Enter a parse tree produced by RLangParser#stat.
    def enterStat(self, ctx: RLangParser.StatContext):
        pass

    # Exit a parse tree produced by RLangParser#stat.
    def exitStat(self, ctx: RLangParser.StatContext):
        pass

    # Enter a parse tree produced by RLangParser#predicate.
    def enterPredicate(self, ctx: RLangParser.PredicateContext):
        pass

    # Exit a parse tree produced by RLangParser#predicate.
    def exitPredicate(self, ctx: RLangParser.PredicateContext):
        pass

    # Enter a parse tree produced by RLangParser#feature.
    def enterFeature(self, ctx: RLangParser.FeatureContext):
        pass

    # Exit a parse tree produced by RLangParser#feature.
    def exitFeature(self, ctx: RLangParser.FeatureContext):
        pass

    # Enter a parse tree produced by RLangParser#factor.
    def enterFactor(self, ctx: RLangParser.FactorContext):
        pass

    # Exit a parse tree produced by RLangParser#factor.
    def exitFactor(self, ctx: RLangParser.FactorContext):
        pass

    # Enter a parse tree produced by RLangParser#goal.
    def enterGoal(self, ctx: RLangParser.GoalContext):
        pass

    # Exit a parse tree produced by RLangParser#goal.
    def exitGoal(self, ctx: RLangParser.GoalContext):
        pass

    # Enter a parse tree produced by RLangParser#action.
    def enterAction(self, ctx: RLangParser.ActionContext):
        pass

    # Exit a parse tree produced by RLangParser#action.
    def exitAction(self, ctx: RLangParser.ActionContext):
        pass

    # Enter a parse tree produced by RLangParser#effect.
    def enterEffect(self, ctx: RLangParser.EffectContext):
        pass

    # Exit a parse tree produced by RLangParser#effect.
    def exitEffect(self, ctx: RLangParser.EffectContext):
        pass

    # Enter a parse tree produced by RLangParser#reward.
    def enterReward(self, ctx: RLangParser.RewardContext):
        pass

    # Exit a parse tree produced by RLangParser#reward.
    def exitReward(self, ctx: RLangParser.RewardContext):
        pass

    # Enter a parse tree produced by RLangParser#constant.
    def enterConstant(self, ctx: RLangParser.ConstantContext):
        pass

    # Exit a parse tree produced by RLangParser#constant.
    def exitConstant(self, ctx: RLangParser.ConstantContext):
        pass

    # Enter a parse tree produced by RLangParser#assignment.
    def enterAssignment(self, ctx: RLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by RLangParser#assignment.
    def exitAssignment(self, ctx: RLangParser.AssignmentContext):
        pass

    # Enter a parse tree produced by RLangParser#boolean_expression.
    def enterBoolean_expression(self, ctx: RLangParser.Boolean_expressionContext):
        pass

    # Exit a parse tree produced by RLangParser#boolean_expression.
    def exitBoolean_expression(self, ctx: RLangParser.Boolean_expressionContext):
        pass

    # Enter a parse tree produced by RLangParser#arithmetic_expression.
    def enterArithmetic_expression(self, ctx: RLangParser.Arithmetic_expressionContext):
        pass

    # Exit a parse tree produced by RLangParser#arithmetic_expression.
    def exitArithmetic_expression(self, ctx: RLangParser.Arithmetic_expressionContext):
        pass

    # Enter a parse tree produced by RLangParser#trailer.
    def enterTrailer(self, ctx: RLangParser.TrailerContext):
        pass

    # Exit a parse tree produced by RLangParser#trailer.
    def exitTrailer(self, ctx: RLangParser.TrailerContext):
        pass


del RLangParser
