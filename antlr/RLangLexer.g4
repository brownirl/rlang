lexer grammar RLangLexer;

/*
 * lexer rules
 */

PROPOSITION: 'Proposition';

IDENTIFIER
    : LETTER ANY_CHAR*
    ;

/*
 *
 */

AND: 'and';
OR: 'or';
NOT: 'not';

ASSIGN : ':=';

OPEN_PAREN: '(';
CLOSE_PAREN: ')';

LESS_THAN : '<';
GREATER_THAN : '>';
EQUALS : '==';
GT_EQ : '>=';
LT_EQ : '<=';
NOT_EQ : '!=';

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