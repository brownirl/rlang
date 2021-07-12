parser grammar RLangParser;

options {
    tokenVocab=RLangLexer;
}

program: NL* (dec NL*)*;

dec
    : predicate
    | feature
    | factor
    | goal
    | action
    | effect
    | constant
    ;

stat
    : reward
    | assignment
    | constant
    ;

predicate: PREDICATE IDENTIFIER BIND boolean_expression;
feature: FEATURE IDENTIFIER BIND arithmetic_expression;
factor: FACTOR IDENTIFIER BIND S trailer;
goal: GOAL IDENTIFIER BIND boolean_expression;
action: ACTION IDENTIFIER BIND INTEGER;
effect: EFFECT boolean_expression COL INDENT (stat NL*)* DEDENT;
reward: REWARD (DECIMAL | INTEGER);
constant: CONSTANT IDENTIFIER BIND (boolean_expression | arithmetic_expression);

assignment
    : IDENTIFIER trailer? (ASIGN | TIMES_EQ | DIV_EQ | PLUS_EQ | MINUS_EQ) (boolean_expression | arithmetic_expression);

boolean_expression
    : L_PAR boolean_expression R_PAR
    | boolean_expression AND boolean_expression
    | boolean_expression OR boolean_expression
    | NOT boolean_expression
    | boolean_expression (EQUALS | NOT_EQ) boolean_expression
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

