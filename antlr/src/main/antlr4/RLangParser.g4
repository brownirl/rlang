parser grammar RLangParser;

options {
    tokenVocab=RLangLexer;
}

program: NL* imports declarations NL*;

imports: (import_stat NL+)*;
import_stat: IMPORT FNAME;

declarations: dec*;
dec
    : constant NL+
    | factor NL+
    | feature NL+
    | predicate NL+
    | goal NL+
    | action NL+
    | markov_feature NL+
    | effect
    | option
    | policy
    ;

constant: CONSTANT IDENTIFIER BIND (arithmetic_exp | boolean_exp);

factor: FACTOR IDENTIFIER BIND S trailer?;
feature: FEATURE IDENTIFIER BIND arithmetic_exp;
predicate: PREDICATE IDENTIFIER BIND boolean_exp;
action: ACTION IDENTIFIER BIND (any_number | int_array_exp | any_array_exp);
goal: GOAL IDENTIFIER BIND boolean_exp;
markov_feature: MARKOVFEATURE IDENTIFIER BIND arithmetic_exp;
effect: EFFECT boolean_exp COL INDENT (effect_stat NL*)* DEDENT;
option: OPTION IDENTIFIER COL INDENT INIT init=boolean_exp INDENT (stats+=policy_stat NL*)+ DEDENT UNTIL until=boolean_exp NL* DEDENT;
policy: POLICY IDENTIFIER COL INDENT (stats+=policy_stat NL*)+ DEDENT;

effect_stat
    : reward
    | assignment
    | constant
    ;

reward: REWARD any_number;
assignment: ((IDENTIFIER | S_PRIME) trailer*) (ASSIGN | TIMES_EQ | DIV_EQ | PLUS_EQ | MINUS_EQ) ((IDENTIFIER | S) trailer* | boolean_exp | arithmetic_exp | int_array_exp);

policy_stat
    : execute        # policy_stat_execute
    | IF if_condition=boolean_exp COL INDENT (if_statements+=policy_stat NL*)+ DEDENT (ELIF elif_condition=boolean_exp COL INDENT (elif_statements+=policy_stat NL*)+ DEDENT)* (ELSE COL INDENT (else_statements+=policy_stat NL*)+ DEDENT)*  # policy_stat_conditional
    ;

execute: EXECUTE (IDENTIFIER | arithmetic_exp);

arithmetic_exp
    : L_PAR arithmetic_exp R_PAR                                # arith_paren
    | lhs=arithmetic_exp (TIMES | DIVIDE) rhs=arithmetic_exp    # arith_times_divide
    | lhs=arithmetic_exp (PLUS | MINUS) rhs=arithmetic_exp      # arith_plus_minus
    | any_number                                                # arith_number
    | any_array_exp                                             # arith_array
    | any_bound_var                                             # arith_bound_var
    ;

boolean_exp
    : L_PAR boolean_exp R_PAR                                   # bool_paren
    | lhs=boolean_exp AND rhs=boolean_exp                       # bool_and
    | lhs=boolean_exp OR rhs=boolean_exp                        # bool_or
    | NOT boolean_exp                                           # bool_not
    | lhs=arithmetic_exp IN rhs=arithmetic_exp                  # bool_in
    | lhs=boolean_exp (EQ_TO | NOT_EQ) rhs=boolean_exp          # bool_bool_eq
    | lhs=arithmetic_exp (EQ_TO | LT | GT | LT_EQ | GT_EQ | NOT_EQ) rhs=arithmetic_exp   # bool_arith_eq
    | any_bound_var                                             # bool_bound_var
    | (TRUE | FALSE)                                            # bool_tf
    ;

any_bound_var
    : IDENTIFIER trailer*    # bound_identifier
    | S trailer?             # bound_state
    | S_PRIME trailer?       # bound_next_state
    | A			             # bound_action
    ;

trailer
    : int_array_exp     # trailer_array
    | slice_exp         # trailer_slice
    ;

int_array_exp: L_BRK arr+=any_integer (COM arr+=any_integer?)* R_BRK;
any_array_exp: L_BRK arr+=any_number (COM arr+=any_number?)* R_BRK;
slice_exp: L_BRK start_ind=any_integer? COL stop_ind=any_integer? R_BRK;

any_number
    : any_integer   # any_num_int
    | any_decimal   # any_num_dec
    ;

any_integer: (MINUS)? INTEGER;
any_decimal: (MINUS)? DECIMAL;