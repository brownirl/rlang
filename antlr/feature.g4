grammar feature;

expr: feature EOF;

/*
PARSER RULES
*/

feature: FEATURE_TYPE IDENTIFIER ASSIGNMENT arthemetic_expr;

arthemetic_expr
    : arthemetic_expr arthmetic_operators arthemetic_expr
    | OPEN_PAREN arthemetic_expr CLOSE_PAREN
    | operand
    ;

operand
    : NUMBER
    | spliced
    | NEGATIVE_NUMBER
    | IDENTIFIER
    ;

arthmetic_operators
    : MULTIPLY
    | ADD
    | SUBTRACT
    | DIVIDE
    | POW
    ;

spliced
    : IDENTIFIER'['NUMBER']'
    | IDENTIFIER'['NUMBER':'NUMBER']'
;

/* 
LEXER RULES
 */

FEATURE_TYPE: 'Feature';
IDENTIFIER: [a-zA-Z][A-Za-z0-9_]*;
ASSIGNMENT: ':=';
NUMBER: [0-9]+;

OPEN_PAREN: '(';
CLOSE_PAREN: ')'; 

MULTIPLY: '*';
ADD: '+';
SUBTRACT: '-';
DIVIDE: '/';
POW: '^';

NEGATIVE_NUMBER: '-'NUMBER;

WHITESPACE: [ \t\f\r\n]+ -> channel(HIDDEN); // skip whitespaces
DISCARDABLE: . -> channel(HIDDEN); // keeping whitespace tokenised makes it easier for syntax highlighting

