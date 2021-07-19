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
    | option
    | policy
    ;

predicate: PREDICATE IDENTIFIER BIND boolean_exp;
feature: FEATURE IDENTIFIER BIND arithmetic_exp;
factor: FACTOR IDENTIFIER BIND S trailer?;
goal: GOAL IDENTIFIER BIND boolean_exp;
action: ACTION IDENTIFIER BIND INTEGER;
effect: EFFECT boolean_exp COL INDENT (effect_stat NL*)* DEDENT;
option: OPTION IDENTIFIER COL INDENT INIT boolean_exp INDENT (policy_stat NL*)* DEDENT UNTIL boolean_exp;
policy: POLICY IDENTIFIER COL INDENT (policy_stat NL*)* DEDENT;

effect_stat
    : reward
    | assignment
    | constant
    ;

policy_stat
    : execute
    | IF boolean_exp COL INDENT (policy_stat NL*)* DEDENT (ELIF boolean_exp COL INDENT (policy_stat NL*)* DEDENT)* (ELSE COL INDENT (policy_stat NL*)* DEDENT)*
    ;

reward: REWARD (DECIMAL | INTEGER);
constant: CONSTANT IDENTIFIER BIND (boolean_exp | arithmetic_exp | array_exp);
assignment
    : IDENTIFIER trailer? (ASIGN | TIMES_EQ | DIV_EQ | PLUS_EQ | MINUS_EQ) (boolean_exp | arithmetic_exp | array_exp);
execute: EXECUTE IDENTIFIER;

boolean_exp
    : L_PAR boolean_exp R_PAR
    | boolean_exp AND boolean_exp
    | boolean_exp OR boolean_exp
    | NOT boolean_exp
    | IDENTIFIER IN IDENTIFIER trailer?
    | A (EQUALS | NOT_EQ) IDENTIFIER
    | boolean_exp (EQUALS | NOT_EQ) boolean_exp
    | arithmetic_exp (EQUALS | LT | GT | LT_EQ | GT_EQ | NOT_EQ) arithmetic_exp
    | (TRUE | FALSE)
    | IDENTIFIER
    ;

arithmetic_exp
    : L_PAR arithmetic_exp R_PAR
    | arithmetic_exp (TIMES | DIVIDE) arithmetic_exp
    | arithmetic_exp (PLUS | MINUS) arithmetic_exp
    | (MINUS)? (DECIMAL | INTEGER)
    | IDENTIFIER trailer*
    ;

trailer
    : L_BRK (MINUS)? INTEGER (COM (MINUS)? INTEGER)* R_BRK
    | L_BRK ((MINUS)? INTEGER)? COL ((MINUS)? INTEGER)? R_BRK
    ;

array_exp: L_BRK (MINUS)? INTEGER (COM (MINUS)? INTEGER)* R_BRK;