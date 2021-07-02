grammar predicate;

expr: PREDICATE EOF;

/*
LEXER RULES
*/

PREDICATE: PREDICATE_TYPE IDENTIFIER ASSIGNMENT boolean_expression EOF;

fragment PREDICATE_TYPE: 'Predicate';
fragment IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
fragment ASSIGNMENT: ':=';


boolean_expression
    : boolean_expression boolean_operator boolean_expression
    | OPEN_PAREN boolean_expression CLOSE_PAREN
    | operand operator operand
    | NOT boolean_expression
    | IDENTIFIER
    ;

boolean_operator
    : AND
    | OR
    ;

operator
    : GREATER_THAN
    | LESS_THAN
    | GREATER_THAN_EQUAL
    | LESS_THAN_EQUAL
    | EQUAL
    | NOT_EQUAL
    ;

operand
    : 
    | NUMBER
    | IDENTIFIER
    ;

/*
LEXER RULES
 */

// boolean operators
AND: 'and';
OR: 'or';
NOT: 'not';

OPEN_PAREN: '(';
CLOSE_PAREN: ')'; 

// operators 
GREATER_THAN: '>';
GREATER_THAN_EQUAL: '>=';
LESS_THAN: '<'; 
LESS_THAN_EQUAL: '<=';
EQUAL: '==';
NOT_EQUAL: '!=';

// operands
NUMBER: [0-9]+;

WHITESPACE: [ \t\f\r\n]+ -> channel(HIDDEN); // skip whitespaces
DISCARDABLE: . -> channel(HIDDEN); // keeping whitespace tokenised makes it easier for syntax highlighting
