lexer grammar RLangLexer;

/*
 * lexer rules
 */

PREDICATE: 'Predicate';
FEATURE: 'Feature';

AND: 'and';
OR: 'or';
NOT: 'not';

TRUE: 'True';
FALSE: 'False';

ASSIGN : ':=';

L_BRK: '[';
R_BRK: ']';

L_PAR: '(';
R_PAR: ')';

LT : '<';
GT : '>';
EQUALS : '==';
GT_EQ : '>=';
LT_EQ : '<=';
NOT_EQ : '!=';

TIMES : '*';
DIVIDE : '/';
PLUS : '+';
MINUS : '-';

/*
 *
 */

IDENTIFIER
    : LETTER ANY_CHAR*
    ;

DECIMAL
    : DIGIT+ '.' DIGIT+
    ;

INTEGER
    : DIGIT+
    ;

/*
 * fragments + skip
 */

fragment LETTER
    : [a-z] | [A-Z]
    ;

fragment ANY_CHAR
    : LETTER | DIGIT | '_'
    ;

fragment DIGIT
    : [0-9]
    ;

fragment SPACES
    : [ \t]+
    ;

fragment COMMENT
    : '#' ~[\r\n\f]*
    ;

fragment NEWLINE
    : '\r' '\n' | '\n' | '\r'
    ;

SKIP_
    : ( SPACES | COMMENT | NEWLINE) -> skip
    ;