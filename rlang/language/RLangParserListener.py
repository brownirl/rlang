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


    # Enter a parse tree produced by RLangParser#stat.
    def enterStat(self, ctx:RLangParser.StatContext):
        pass

    # Exit a parse tree produced by RLangParser#stat.
    def exitStat(self, ctx:RLangParser.StatContext):
        pass


    # Enter a parse tree produced by RLangParser#predicate.
    def enterPredicate(self, ctx:RLangParser.PredicateContext):
        pass

    # Exit a parse tree produced by RLangParser#predicate.
    def exitPredicate(self, ctx:RLangParser.PredicateContext):
        pass


    # Enter a parse tree produced by RLangParser#feature.
    def enterFeature(self, ctx:RLangParser.FeatureContext):
        pass

    # Exit a parse tree produced by RLangParser#feature.
    def exitFeature(self, ctx:RLangParser.FeatureContext):
        pass


    # Enter a parse tree produced by RLangParser#goal.
    def enterGoal(self, ctx:RLangParser.GoalContext):
        pass

    # Exit a parse tree produced by RLangParser#goal.
    def exitGoal(self, ctx:RLangParser.GoalContext):
        pass


    # Enter a parse tree produced by RLangParser#literal.
    def enterLiteral(self, ctx:RLangParser.LiteralContext):
        pass

    # Exit a parse tree produced by RLangParser#literal.
    def exitLiteral(self, ctx:RLangParser.LiteralContext):
        pass


    # Enter a parse tree produced by RLangParser#boolean_expression.
    def enterBoolean_expression(self, ctx:RLangParser.Boolean_expressionContext):
        pass

    # Exit a parse tree produced by RLangParser#boolean_expression.
    def exitBoolean_expression(self, ctx:RLangParser.Boolean_expressionContext):
        pass


    # Enter a parse tree produced by RLangParser#arithmetic_expression.
    def enterArithmetic_expression(self, ctx:RLangParser.Arithmetic_expressionContext):
        pass

    # Exit a parse tree produced by RLangParser#arithmetic_expression.
    def exitArithmetic_expression(self, ctx:RLangParser.Arithmetic_expressionContext):
        pass


    # Enter a parse tree produced by RLangParser#trailer.
    def enterTrailer(self, ctx:RLangParser.TrailerContext):
        pass

    # Exit a parse tree produced by RLangParser#trailer.
    def exitTrailer(self, ctx:RLangParser.TrailerContext):
        pass



del RLangParser