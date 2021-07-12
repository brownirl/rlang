# Generated from RLangLexer.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from antlr_denter.DenterHelper import DenterHelper
from RLangParser import RLangParser



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2,")
        buf.write("\u012d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\3\2\5\2_\n\2\3\2\3\2\7\2c\n\2\f\2\16\2f\13\2\3\2\5")
        buf.write("\2i\n\2\3\2\3\2\7\2m\n\2\f\2\16\2p\13\2\5\2r\n\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37")
        buf.write("\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\7&\u00fd")
        buf.write("\n&\f&\16&\u0100\13&\3\'\6\'\u0103\n\'\r\'\16\'\u0104")
        buf.write("\3\'\3\'\6\'\u0109\n\'\r\'\16\'\u010a\3(\6(\u010e\n(\r")
        buf.write("(\16(\u010f\3)\5)\u0113\n)\3*\3*\3*\5*\u0118\n*\3+\3+")
        buf.write("\3,\6,\u011d\n,\r,\16,\u011e\3-\3-\7-\u0123\n-\f-\16-")
        buf.write("\u0126\13-\3.\3.\5.\u012a\n.\3.\3.\2\2/\3\5\5\6\7\7\t")
        buf.write("\b\13\t\r\n\17\13\21\f\23\r\25\16\27\17\31\20\33\21\35")
        buf.write("\22\37\23!\24#\25%\26\'\27)\30+\31-\32/\33\61\34\63\35")
        buf.write("\65\36\67\379 ;!=\"?#A$C%E&G\'I(K)M*O+Q\2S\2U\2W\2Y\2")
        buf.write("[,\3\2\6\4\2C\\c|\3\2\62;\4\2\13\13\"\"\4\2\f\f\16\17")
        buf.write("\2\u0135\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write("\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2[\3\2\2")
        buf.write("\2\3q\3\2\2\2\5s\3\2\2\2\7}\3\2\2\2\t\u0085\3\2\2\2\13")
        buf.write("\u008c\3\2\2\2\r\u0091\3\2\2\2\17\u009a\3\2\2\2\21\u00a1")
        buf.write("\3\2\2\2\23\u00a8\3\2\2\2\25\u00af\3\2\2\2\27\u00b1\3")
        buf.write("\2\2\2\31\u00b5\3\2\2\2\33\u00b8\3\2\2\2\35\u00bc\3\2")
        buf.write("\2\2\37\u00c1\3\2\2\2!\u00c7\3\2\2\2#\u00ca\3\2\2\2%\u00cc")
        buf.write("\3\2\2\2\'\u00cf\3\2\2\2)\u00d2\3\2\2\2+\u00d5\3\2\2\2")
        buf.write("-\u00d8\3\2\2\2/\u00db\3\2\2\2\61\u00de\3\2\2\2\63\u00e1")
        buf.write("\3\2\2\2\65\u00e4\3\2\2\2\67\u00e6\3\2\2\29\u00e8\3\2")
        buf.write("\2\2;\u00ea\3\2\2\2=\u00ec\3\2\2\2?\u00ee\3\2\2\2A\u00f0")
        buf.write("\3\2\2\2C\u00f2\3\2\2\2E\u00f4\3\2\2\2G\u00f6\3\2\2\2")
        buf.write("I\u00f8\3\2\2\2K\u00fa\3\2\2\2M\u0102\3\2\2\2O\u010d\3")
        buf.write("\2\2\2Q\u0112\3\2\2\2S\u0117\3\2\2\2U\u0119\3\2\2\2W\u011c")
        buf.write("\3\2\2\2Y\u0120\3\2\2\2[\u0129\3\2\2\2]_\7\17\2\2^]\3")
        buf.write("\2\2\2^_\3\2\2\2_`\3\2\2\2`d\7\f\2\2ac\7\"\2\2ba\3\2\2")
        buf.write("\2cf\3\2\2\2db\3\2\2\2de\3\2\2\2er\3\2\2\2fd\3\2\2\2g")
        buf.write("i\7\17\2\2hg\3\2\2\2hi\3\2\2\2ij\3\2\2\2jn\7\f\2\2km\7")
        buf.write("\13\2\2lk\3\2\2\2mp\3\2\2\2nl\3\2\2\2no\3\2\2\2or\3\2")
        buf.write("\2\2pn\3\2\2\2q^\3\2\2\2qh\3\2\2\2r\4\3\2\2\2st\7R\2\2")
        buf.write("tu\7t\2\2uv\7g\2\2vw\7f\2\2wx\7k\2\2xy\7e\2\2yz\7c\2\2")
        buf.write("z{\7v\2\2{|\7g\2\2|\6\3\2\2\2}~\7H\2\2~\177\7g\2\2\177")
        buf.write("\u0080\7c\2\2\u0080\u0081\7v\2\2\u0081\u0082\7w\2\2\u0082")
        buf.write("\u0083\7t\2\2\u0083\u0084\7g\2\2\u0084\b\3\2\2\2\u0085")
        buf.write("\u0086\7H\2\2\u0086\u0087\7c\2\2\u0087\u0088\7e\2\2\u0088")
        buf.write("\u0089\7v\2\2\u0089\u008a\7q\2\2\u008a\u008b\7t\2\2\u008b")
        buf.write("\n\3\2\2\2\u008c\u008d\7I\2\2\u008d\u008e\7q\2\2\u008e")
        buf.write("\u008f\7c\2\2\u008f\u0090\7n\2\2\u0090\f\3\2\2\2\u0091")
        buf.write("\u0092\7E\2\2\u0092\u0093\7q\2\2\u0093\u0094\7p\2\2\u0094")
        buf.write("\u0095\7u\2\2\u0095\u0096\7v\2\2\u0096\u0097\7c\2\2\u0097")
        buf.write("\u0098\7p\2\2\u0098\u0099\7v\2\2\u0099\16\3\2\2\2\u009a")
        buf.write("\u009b\7C\2\2\u009b\u009c\7e\2\2\u009c\u009d\7v\2\2\u009d")
        buf.write("\u009e\7k\2\2\u009e\u009f\7q\2\2\u009f\u00a0\7p\2\2\u00a0")
        buf.write("\20\3\2\2\2\u00a1\u00a2\7G\2\2\u00a2\u00a3\7h\2\2\u00a3")
        buf.write("\u00a4\7h\2\2\u00a4\u00a5\7g\2\2\u00a5\u00a6\7e\2\2\u00a6")
        buf.write("\u00a7\7v\2\2\u00a7\22\3\2\2\2\u00a8\u00a9\7T\2\2\u00a9")
        buf.write("\u00aa\7g\2\2\u00aa\u00ab\7y\2\2\u00ab\u00ac\7c\2\2\u00ac")
        buf.write("\u00ad\7t\2\2\u00ad\u00ae\7f\2\2\u00ae\24\3\2\2\2\u00af")
        buf.write("\u00b0\7U\2\2\u00b0\26\3\2\2\2\u00b1\u00b2\7c\2\2\u00b2")
        buf.write("\u00b3\7p\2\2\u00b3\u00b4\7f\2\2\u00b4\30\3\2\2\2\u00b5")
        buf.write("\u00b6\7q\2\2\u00b6\u00b7\7t\2\2\u00b7\32\3\2\2\2\u00b8")
        buf.write("\u00b9\7p\2\2\u00b9\u00ba\7q\2\2\u00ba\u00bb\7v\2\2\u00bb")
        buf.write("\34\3\2\2\2\u00bc\u00bd\7V\2\2\u00bd\u00be\7t\2\2\u00be")
        buf.write("\u00bf\7w\2\2\u00bf\u00c0\7g\2\2\u00c0\36\3\2\2\2\u00c1")
        buf.write("\u00c2\7H\2\2\u00c2\u00c3\7c\2\2\u00c3\u00c4\7n\2\2\u00c4")
        buf.write("\u00c5\7u\2\2\u00c5\u00c6\7g\2\2\u00c6 \3\2\2\2\u00c7")
        buf.write("\u00c8\7<\2\2\u00c8\u00c9\7?\2\2\u00c9\"\3\2\2\2\u00ca")
        buf.write("\u00cb\7?\2\2\u00cb$\3\2\2\2\u00cc\u00cd\7,\2\2\u00cd")
        buf.write("\u00ce\7?\2\2\u00ce&\3\2\2\2\u00cf\u00d0\7\61\2\2\u00d0")
        buf.write("\u00d1\7?\2\2\u00d1(\3\2\2\2\u00d2\u00d3\7-\2\2\u00d3")
        buf.write("\u00d4\7?\2\2\u00d4*\3\2\2\2\u00d5\u00d6\7/\2\2\u00d6")
        buf.write("\u00d7\7?\2\2\u00d7,\3\2\2\2\u00d8\u00d9\7?\2\2\u00d9")
        buf.write("\u00da\7?\2\2\u00da.\3\2\2\2\u00db\u00dc\7@\2\2\u00dc")
        buf.write("\u00dd\7?\2\2\u00dd\60\3\2\2\2\u00de\u00df\7>\2\2\u00df")
        buf.write("\u00e0\7?\2\2\u00e0\62\3\2\2\2\u00e1\u00e2\7#\2\2\u00e2")
        buf.write("\u00e3\7?\2\2\u00e3\64\3\2\2\2\u00e4\u00e5\7<\2\2\u00e5")
        buf.write("\66\3\2\2\2\u00e6\u00e7\7]\2\2\u00e78\3\2\2\2\u00e8\u00e9")
        buf.write("\7_\2\2\u00e9:\3\2\2\2\u00ea\u00eb\7*\2\2\u00eb<\3\2\2")
        buf.write("\2\u00ec\u00ed\7+\2\2\u00ed>\3\2\2\2\u00ee\u00ef\7>\2")
        buf.write("\2\u00ef@\3\2\2\2\u00f0\u00f1\7@\2\2\u00f1B\3\2\2\2\u00f2")
        buf.write("\u00f3\7,\2\2\u00f3D\3\2\2\2\u00f4\u00f5\7\61\2\2\u00f5")
        buf.write("F\3\2\2\2\u00f6\u00f7\7-\2\2\u00f7H\3\2\2\2\u00f8\u00f9")
        buf.write("\7/\2\2\u00f9J\3\2\2\2\u00fa\u00fe\5Q)\2\u00fb\u00fd\5")
        buf.write("S*\2\u00fc\u00fb\3\2\2\2\u00fd\u0100\3\2\2\2\u00fe\u00fc")
        buf.write("\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ffL\3\2\2\2\u0100\u00fe")
        buf.write("\3\2\2\2\u0101\u0103\5U+\2\u0102\u0101\3\2\2\2\u0103\u0104")
        buf.write("\3\2\2\2\u0104\u0102\3\2\2\2\u0104\u0105\3\2\2\2\u0105")
        buf.write("\u0106\3\2\2\2\u0106\u0108\7\60\2\2\u0107\u0109\5U+\2")
        buf.write("\u0108\u0107\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u0108\3")
        buf.write("\2\2\2\u010a\u010b\3\2\2\2\u010bN\3\2\2\2\u010c\u010e")
        buf.write("\5U+\2\u010d\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u010d")
        buf.write("\3\2\2\2\u010f\u0110\3\2\2\2\u0110P\3\2\2\2\u0111\u0113")
        buf.write("\t\2\2\2\u0112\u0111\3\2\2\2\u0113R\3\2\2\2\u0114\u0118")
        buf.write("\5Q)\2\u0115\u0118\5U+\2\u0116\u0118\7a\2\2\u0117\u0114")
        buf.write("\3\2\2\2\u0117\u0115\3\2\2\2\u0117\u0116\3\2\2\2\u0118")
        buf.write("T\3\2\2\2\u0119\u011a\t\3\2\2\u011aV\3\2\2\2\u011b\u011d")
        buf.write("\t\4\2\2\u011c\u011b\3\2\2\2\u011d\u011e\3\2\2\2\u011e")
        buf.write("\u011c\3\2\2\2\u011e\u011f\3\2\2\2\u011fX\3\2\2\2\u0120")
        buf.write("\u0124\7%\2\2\u0121\u0123\n\5\2\2\u0122\u0121\3\2\2\2")
        buf.write("\u0123\u0126\3\2\2\2\u0124\u0122\3\2\2\2\u0124\u0125\3")
        buf.write("\2\2\2\u0125Z\3\2\2\2\u0126\u0124\3\2\2\2\u0127\u012a")
        buf.write("\5W,\2\u0128\u012a\5Y-\2\u0129\u0127\3\2\2\2\u0129\u0128")
        buf.write("\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012c\b.\2\2\u012c")
        buf.write("\\\3\2\2\2\21\2^dhnq\u00fe\u0104\u010a\u010f\u0112\u0117")
        buf.write("\u011e\u0124\u0129\3\b\2\2")
        return buf.getvalue()


class RLangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INDENT = 1
    DEDENT = 2
    NL = 3
    PREDICATE = 4
    FEATURE = 5
    FACTOR = 6
    GOAL = 7
    CONSTANT = 8
    ACTION = 9
    EFFECT = 10
    REWARD = 11
    S = 12
    AND = 13
    OR = 14
    NOT = 15
    TRUE = 16
    FALSE = 17
    BIND = 18
    ASIGN = 19
    TIMES_EQ = 20
    DIV_EQ = 21
    PLUS_EQ = 22
    MINUS_EQ = 23
    EQUALS = 24
    GT_EQ = 25
    LT_EQ = 26
    NOT_EQ = 27
    COL = 28
    L_BRK = 29
    R_BRK = 30
    L_PAR = 31
    R_PAR = 32
    LT = 33
    GT = 34
    TIMES = 35
    DIVIDE = 36
    PLUS = 37
    MINUS = 38
    IDENTIFIER = 39
    DECIMAL = 40
    INTEGER = 41
    SKIP_ = 42

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Predicate'", "'Feature'", "'Factor'", "'Goal'", "'Constant'", 
            "'Action'", "'Effect'", "'Reward'", "'S'", "'and'", "'or'", 
            "'not'", "'True'", "'False'", "':='", "'='", "'*='", "'/='", 
            "'+='", "'-='", "'=='", "'>='", "'<='", "'!='", "':'", "'['", 
            "']'", "'('", "')'", "'<'", "'>'", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "NL", "PREDICATE", "FEATURE", "FACTOR", 
            "GOAL", "CONSTANT", "ACTION", "EFFECT", "REWARD", "S", "AND", 
            "OR", "NOT", "TRUE", "FALSE", "BIND", "ASIGN", "TIMES_EQ", "DIV_EQ", 
            "PLUS_EQ", "MINUS_EQ", "EQUALS", "GT_EQ", "LT_EQ", "NOT_EQ", 
            "COL", "L_BRK", "R_BRK", "L_PAR", "R_PAR", "LT", "GT", "TIMES", 
            "DIVIDE", "PLUS", "MINUS", "IDENTIFIER", "DECIMAL", "INTEGER", 
            "SKIP_" ]

    ruleNames = [ "NL", "PREDICATE", "FEATURE", "FACTOR", "GOAL", "CONSTANT", 
                  "ACTION", "EFFECT", "REWARD", "S", "AND", "OR", "NOT", 
                  "TRUE", "FALSE", "BIND", "ASIGN", "TIMES_EQ", "DIV_EQ", 
                  "PLUS_EQ", "MINUS_EQ", "EQUALS", "GT_EQ", "LT_EQ", "NOT_EQ", 
                  "COL", "L_BRK", "R_BRK", "L_PAR", "R_PAR", "LT", "GT", 
                  "TIMES", "DIVIDE", "PLUS", "MINUS", "IDENTIFIER", "DECIMAL", 
                  "INTEGER", "LETTER", "ANY_CHAR", "DIGIT", "SPACES", "COMMENT", 
                  "SKIP_" ]

    grammarFileName = "RLangLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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



