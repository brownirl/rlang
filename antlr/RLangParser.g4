parser grammar RLangParser;

options {
    tokenVocab=RLangLexer;
}

program: stat*;

stat
    : predicate
    | feature
    | goal
    ;

predicate: PREDICATE IDENTIFIER ASSIGN boolean_expression;
feature: FEATURE IDENTIFIER ASSIGN arithmetic_expression;
goal: GOAL IDENTIFIER ASSIGN boolean_expression;

boolean_expression
    : L_PAR boolean_expression R_PAR
    | boolean_expression AND boolean_expression
    | boolean_expression OR boolean_expression
    | NOT boolean_expression
    | arithmetic_expression (EQUALS | LT | GT | LT_EQ | GT_EQ | NOT_EQ) arithmetic_expression
    | (TRUE | FALSE)
    | IDENTIFIER
    ;

arithmetic_expression
    : L_PAR arithmetic_expression R_PAR
    | arithmetic_expression (TIMES | DIVIDE) arithmetic_expression
    | arithmetic_expression (PLUS | MINUS) arithmetic_expression
    | (MINUS)? (DECIMAL | INTEGER)
    | IDENTIFIER trailer*
    ;

trailer
    : L_BRK (MINUS)? INTEGER R_BRK
    | L_BRK ((MINUS)? INTEGER)? COL ((MINUS)? INTEGER)? R_BRK
    ;

