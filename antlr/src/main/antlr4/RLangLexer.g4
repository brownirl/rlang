lexer grammar RLangLexer;

tokens { INDENT, DEDENT }

@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from RLangParser import RLangParser
}
@lexer::members {
class SimpleDenter(DenterHelper):
    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
        self.lexer: RLangLexer = lexer

    def pull_token(self):
        return super(RLangLexer, self.lexer).nextToken()

denter = None

def nextToken(self):
    if not self.denter:
        self.denter = self.SimpleDenter(self, self.NL, RLangParser.INDENT, RLangParser.DEDENT, False)
    return self.denter.next_token()

}

NL: ('\r'? '\n' ' '*) | ('\r'? '\n' '\t'*);

/*
 * lexer rules
 */

PREDICATE: 'Predicate';
FEATURE: 'Feature';
FACTOR: 'Factor';
GOAL: 'Goal';
CONSTANT: 'Constant';
ACTION: 'Action';
EFFECT: 'Effect';
REWARD: 'Reward';

S: 'S';

AND: 'and';
OR: 'or';
NOT: 'not';

TRUE: 'True';
FALSE: 'False';

BIND : ':=';
ASIGN: '=';
TIMES_EQ: '*=';
DIV_EQ: '/=';
PLUS_EQ: '+=';
MINUS_EQ: '-=';

EQUALS : '==';
GT_EQ : '>=';
LT_EQ : '<=';
NOT_EQ : '!=';

COL: ':';

L_BRK: '[';
R_BRK: ']';

L_PAR: '(';
R_PAR: ')';

LT : '<';
GT : '>';

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

SKIP_
    : (SPACES | COMMENT) -> skip
    ;