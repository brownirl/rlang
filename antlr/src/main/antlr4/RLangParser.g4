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
    | action NL+
    | factor NL+
    | proposition NL+
    | goal NL+
    | feature NL+
    | markov_feature NL+
    | object_def NL+
    | class_def
    | option
    | policy
    | plan
    | effect
    ;


constant: CONSTANT IDENTIFIER BIND (arithmetic_exp | boolean_exp);
action: ACTION IDENTIFIER BIND (any_number | any_num_array_exp);
factor: FACTOR IDENTIFIER BIND any_bound_var;
proposition: PROPOSITION IDENTIFIER BIND boolean_exp;
goal: GOAL IDENTIFIER BIND boolean_exp;
feature: FEATURE IDENTIFIER BIND arithmetic_exp;
markov_feature: MARKOVFEATURE IDENTIFIER BIND arithmetic_exp;
object_def: OBJECT IDENTIFIER BIND lifted_execution;

class_def: CLASS IDENTIFIER (L_PAR any_bound_class R_PAR)? COL INDENT attribute_definition_collection DEDENT;

attribute_definition_collection: (definitions+=attribute_definition NL *)+;
attribute_definition: IDENTIFIER COL type_def;

option: OPTION IDENTIFIER COL INDENT INIT init=option_condition INDENT policy_statement NL* DEDENT UNTIL until=option_condition NL* DEDENT;
option_condition: boolean_exp | ANY_CONDITION;

policy: POLICY (IDENTIFIER| MAIN) COL INDENT policy_statement NL* DEDENT;
policy_statement
    : execute                    # policy_statement_execute
    | conditional_subpolicy      # policy_statement_conditional
    | probabilistic_subpolicy    # policy_statement_probabilistic
    ;
conditional_subpolicy: IF if_condition=boolean_exp COL INDENT if_subpolicy=policy_statement NL* DEDENT (ELIF elif_conditions+=boolean_exp COL INDENT elif_subpolicies+=policy_statement NL* DEDENT)* (ELSE COL INDENT else_subpolicy=policy_statement NL* DEDENT)?;
probabilistic_subpolicy: subpolicies+=probabilistic_policy_statement (OR subpolicies+=probabilistic_policy_statement)*;
probabilistic_policy_statement
    : probabilistic_condition COL INDENT policy_statement NL* DEDENT    # probabilistic_policy_statement_no_sugar
    | execute probabilistic_condition NL+                               # probabilistic_policy_statement_sugar
    ;
execute: EXECUTE (IDENTIFIER | arithmetic_exp);
lifted_execution: IDENTIFIER L_PAR (arr+=arithmetic_exp (COM arr+=arithmetic_exp)*)? R_PAR;


plan: PLAN (IDENTIFIER| MAIN) COL INDENT plan_statement_collection DEDENT;
plan_statement_collection: (statements+=plan_statement NL*)+;
plan_statement
    : execute                    # plan_statement_execute
    | conditional_plan           # plan_statement_conditional
    | probabilistic_plan         # plan_statement_probabilistic
    ;
conditional_plan: IF if_condition=boolean_exp COL INDENT if_plan=plan_statement_collection DEDENT (ELIF elif_conditions+=boolean_exp COL INDENT elif_plans+=plan_statement_collection DEDENT)* (ELSE COL INDENT else_plan=plan_statement_collection DEDENT)?;
probabilistic_plan: plans+=probabilistic_plan_statement (OR plans+=probabilistic_plan_statement)*;
probabilistic_plan_statement
    : probabilistic_condition COL INDENT plan_statement_collection DEDENT   # probabilistic_plan_statement_no_sugar
    | execute probabilistic_condition NL+                                  # probabilistic_plan_statement_sugar
    ;


effect: EFFECT (IDENTIFIER| MAIN) COL INDENT effect_statement_collection DEDENT;
effect_statement_collection: (statements+=effect_statement NL*)+;
effect_statement
    : reward                    # effect_statement_reward
    | prediction                # effect_statement_prediction
    | effect_reference          # effect_statement_reference
    | conditional_effect        # effect_statement_conditional
    | probabilistic_effect      # effect_statement_probabilistic
    ;
conditional_effect: IF if_condition=boolean_exp COL INDENT if_effect=effect_statement_collection DEDENT (ELIF elif_conditions+=boolean_exp COL INDENT elif_effects+=effect_statement_collection DEDENT)* (ELSE COL INDENT else_effect=effect_statement_collection DEDENT)?;
probabilistic_effect: effects+=probabilistic_effect_statement (OR effects+=probabilistic_effect_statement)*;
probabilistic_effect_statement
    : probabilistic_condition COL INDENT effect_statement_collection DEDENT   # probabilistic_effect_statement_no_sugar
    | (reward | prediction | effect_reference) probabilistic_condition NL+    # probabilistic_effect_statement_sugar
    ;
reward: REWARD arithmetic_exp;
prediction: (S_PRIME dot_exp? | IDENTIFIER dot_exp? PRIME?) PREDICT (arithmetic_exp | boolean_exp | lifted_execution);
effect_reference: PREDICT IDENTIFIER;

probabilistic_condition: WITH P L_PAR (any_number | integer_fraction) R_PAR;

arithmetic_exp
    : L_PAR arithmetic_exp R_PAR                                # arith_paren
    | lhs=arithmetic_exp (TIMES | DIVIDE) rhs=arithmetic_exp    # arith_times_divide
    | lhs=arithmetic_exp (PLUS | MINUS) rhs=arithmetic_exp      # arith_plus_minus
    | any_number                                                # arith_number
    | any_array                                                 # arith_array
    | any_bound_var                                             # arith_bound_var
    | quantification_exp                                        # arith_quantification
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

quantification_exp: quantifier L_PAR any_bound_class R_PAR dot_exp;

quantifier: ANY_CONDITION | ALL_CONDITION;

type_def: compound_type | simple_type;

compound_type
    : LIST (L_BRK (simple_type | compound_type) R_BRK)?   # type_list
    | SET (L_BRK (simple_type | compound_type) R_BRK)?    # type_set
    ;

simple_type: INT | FLOAT | STR | BOOL | any_bound_class;


any_bound_var
    : S trailer?                    # bound_state
    | S_PRIME trailer?              # bound_next_state
    | IDENTIFIER PRIME? trailer*    # bound_identifier
    | A			                    # bound_action
    | lifted_execution              # bound_lifted_execution
    ;

any_bound_class: IDENTIFIER;

trailer
    : int_array_exp             # trailer_array
    | slice_exp                 # trailer_slice
    | dot_exp                   # trailer_object
    ;

dot_exp: (DOT attr+=IDENTIFIER)+;


// TODO: Naming is weird, need to update.
any_array
    : compound_array_exp    # any_array_compound
    | any_num_array_exp     # any_array_any_num
    ;

compound_array_exp
    : any_num_array_exp     # compound_array_simple
    | L_BRK arr+=arithmetic_exp (COM arr+=arithmetic_exp)* R_BRK    # compound_array_arith
    | L_BRK arr+=compound_array_exp (COM arr+=compound_array_exp)* R_BRK    # compound_array_compound
    ;

int_array_exp: L_BRK arr+=any_integer (COM arr+=any_integer)* R_BRK;
any_num_array_exp: L_BRK arr+=any_number (COM arr+=any_number)* R_BRK;
slice_exp: L_BRK start_ind=any_integer? COL stop_ind=any_integer? R_BRK;

integer_fraction: lhs=any_integer DIVIDE rhs=any_integer;

any_number
    : any_integer   # any_num_int
    | any_decimal   # any_num_dec
    ;

any_integer: MINUS? INTEGER;
any_decimal: MINUS? DECIMAL;
