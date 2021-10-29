# Generated from RLangParser.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u0266\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\3\2\7\2")
        buf.write("\\\n\2\f\2\16\2_\13\2\3\2\3\2\3\2\7\2d\n\2\f\2\16\2g\13")
        buf.write("\2\3\3\3\3\6\3k\n\3\r\3\16\3l\7\3o\n\3\f\3\16\3r\13\3")
        buf.write("\3\4\3\4\3\4\3\5\7\5x\n\5\f\5\16\5{\13\5\3\6\3\6\6\6\177")
        buf.write("\n\6\r\6\16\6\u0080\3\6\3\6\6\6\u0085\n\6\r\6\16\6\u0086")
        buf.write("\3\6\3\6\6\6\u008b\n\6\r\6\16\6\u008c\3\6\3\6\6\6\u0091")
        buf.write("\n\6\r\6\16\6\u0092\3\6\3\6\6\6\u0097\n\6\r\6\16\6\u0098")
        buf.write("\3\6\3\6\6\6\u009d\n\6\r\6\16\6\u009e\3\6\3\6\6\6\u00a3")
        buf.write("\n\6\r\6\16\6\u00a4\3\6\3\6\3\6\5\6\u00aa\n\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\5\7\u00b1\n\7\3\b\3\b\3\b\3\b\3\b\5\b\u00b8")
        buf.write("\n\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\7\16\u00df\n\16\f\16\16\16\u00e2\13\16\3\16\3")
        buf.write("\16\3\17\3\17\5\17\u00e8\n\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\6\21\u00f3\n\21\r\21\16\21\u00f4")
        buf.write("\7\21\u00f7\n\21\f\21\16\21\u00fa\13\21\3\21\5\21\u00fd")
        buf.write("\n\21\3\22\3\22\7\22\u0101\n\22\f\22\16\22\u0104\13\22")
        buf.write("\3\22\3\22\3\22\7\22\u0109\n\22\f\22\16\22\u010c\13\22")
        buf.write("\7\22\u010e\n\22\f\22\16\22\u0111\13\22\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\5\24\u0119\n\24\3\25\3\25\3\25\5\25\u011e")
        buf.write("\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\7\26\u012d\n\26\f\26\16\26\u0130\13\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u0138\n\26\3\27\3")
        buf.write("\27\3\27\7\27\u013d\n\27\f\27\16\27\u0140\13\27\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\6\30\u014b\n\30")
        buf.write("\r\30\16\30\u014c\5\30\u014f\n\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\5\31\u0156\n\31\3\31\3\31\3\32\3\32\5\32\u015c\n")
        buf.write("\32\3\32\3\32\3\32\3\32\7\32\u0162\n\32\f\32\16\32\u0165")
        buf.write("\13\32\6\32\u0167\n\32\r\32\16\32\u0168\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\5\33\u0172\n\33\3\34\3\34\3\34\3")
        buf.write("\35\3\35\5\35\u0179\n\35\3\35\5\35\u017c\n\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\7\37\u018d\n\37\f\37\16\37\u0190\13\37\6\37")
        buf.write("\u0192\n\37\r\37\16\37\u0193\3\37\3\37\3 \3 \3 \3 \3 ")
        buf.write("\3 \7 \u019e\n \f \16 \u01a1\13 \6 \u01a3\n \r \16 \u01a4")
        buf.write("\3 \3 \3 \3 \3 \3 \3 \7 \u01ae\n \f \16 \u01b1\13 \6 ")
        buf.write("\u01b3\n \r \16 \u01b4\3 \3 \7 \u01b9\n \f \16 \u01bc")
        buf.write("\13 \3 \3 \3 \3 \3 \7 \u01c3\n \f \16 \u01c6\13 \6 \u01c8")
        buf.write("\n \r \16 \u01c9\3 \3 \7 \u01ce\n \f \16 \u01d1\13 \3")
        buf.write("!\3!\3!\3!\3!\3!\3!\3!\5!\u01db\n!\3!\3!\3!\3!\3!\3!\7")
        buf.write("!\u01e3\n!\f!\16!\u01e6\13!\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u01f9\n")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\7\"\u0204\n\"\f")
        buf.write("\"\16\"\u0207\13\"\3#\3#\5#\u020b\n#\3#\7#\u020e\n#\f")
        buf.write("#\16#\u0211\13#\3#\3#\5#\u0215\n#\3#\3#\5#\u0219\n#\3")
        buf.write("#\5#\u021c\n#\3$\3$\5$\u0220\n$\3%\3%\5%\u0224\n%\3&\3")
        buf.write("&\3&\3&\3&\7&\u022b\n&\f&\16&\u022e\13&\3&\3&\5&\u0232")
        buf.write("\n&\3\'\3\'\3\'\3\'\7\'\u0238\n\'\f\'\16\'\u023b\13\'")
        buf.write("\3\'\3\'\3(\3(\3(\3(\7(\u0243\n(\f(\16(\u0246\13(\3(\3")
        buf.write("(\3)\3)\5)\u024c\n)\3)\3)\5)\u0250\n)\3)\3)\3*\3*\3*\3")
        buf.write("*\3+\3+\5+\u025a\n+\3,\5,\u025d\n,\3,\3,\3-\5-\u0262\n")
        buf.write("-\3-\3-\3-\2\4@B.\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX\2\7\3\2:;\3")
        buf.write("\2<=\4\2.\6189\3\2$%\4\2..\61\61\2\u0293\2]\3\2\2\2\4")
        buf.write("p\3\2\2\2\6s\3\2\2\2\by\3\2\2\2\n\u00a9\3\2\2\2\f\u00ab")
        buf.write("\3\2\2\2\16\u00b2\3\2\2\2\20\u00b9\3\2\2\2\22\u00be\3")
        buf.write("\2\2\2\24\u00c3\3\2\2\2\26\u00c8\3\2\2\2\30\u00cd\3\2")
        buf.write("\2\2\32\u00d2\3\2\2\2\34\u00e7\3\2\2\2\36\u00e9\3\2\2")
        buf.write("\2 \u00f8\3\2\2\2\"\u00fe\3\2\2\2$\u0112\3\2\2\2&\u0118")
        buf.write("\3\2\2\2(\u011a\3\2\2\2*\u011f\3\2\2\2,\u0139\3\2\2\2")
        buf.write(".\u014e\3\2\2\2\60\u0150\3\2\2\2\62\u0159\3\2\2\2\64\u0171")
        buf.write("\3\2\2\2\66\u0173\3\2\2\28\u017b\3\2\2\2:\u0180\3\2\2")
        buf.write("\2<\u0183\3\2\2\2>\u0197\3\2\2\2@\u01da\3\2\2\2B\u01f8")
        buf.write("\3\2\2\2D\u021b\3\2\2\2F\u021f\3\2\2\2H\u0223\3\2\2\2")
        buf.write("J\u0231\3\2\2\2L\u0233\3\2\2\2N\u023e\3\2\2\2P\u0249\3")
        buf.write("\2\2\2R\u0253\3\2\2\2T\u0259\3\2\2\2V\u025c\3\2\2\2X\u0261")
        buf.write("\3\2\2\2Z\\\7\5\2\2[Z\3\2\2\2\\_\3\2\2\2][\3\2\2\2]^\3")
        buf.write("\2\2\2^`\3\2\2\2_]\3\2\2\2`a\5\4\3\2ae\5\b\5\2bd\7\5\2")
        buf.write("\2cb\3\2\2\2dg\3\2\2\2ec\3\2\2\2ef\3\2\2\2f\3\3\2\2\2")
        buf.write("ge\3\2\2\2hj\5\6\4\2ik\7\5\2\2ji\3\2\2\2kl\3\2\2\2lj\3")
        buf.write("\2\2\2lm\3\2\2\2mo\3\2\2\2nh\3\2\2\2or\3\2\2\2pn\3\2\2")
        buf.write("\2pq\3\2\2\2q\5\3\2\2\2rp\3\2\2\2st\7\6\2\2tu\7>\2\2u")
        buf.write("\7\3\2\2\2vx\5\n\6\2wv\3\2\2\2x{\3\2\2\2yw\3\2\2\2yz\3")
        buf.write("\2\2\2z\t\3\2\2\2{y\3\2\2\2|~\5\f\7\2}\177\7\5\2\2~}\3")
        buf.write("\2\2\2\177\u0080\3\2\2\2\u0080~\3\2\2\2\u0080\u0081\3")
        buf.write("\2\2\2\u0081\u00aa\3\2\2\2\u0082\u0084\5\16\b\2\u0083")
        buf.write("\u0085\7\5\2\2\u0084\u0083\3\2\2\2\u0085\u0086\3\2\2\2")
        buf.write("\u0086\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u00aa\3")
        buf.write("\2\2\2\u0088\u008a\5\20\t\2\u0089\u008b\7\5\2\2\u008a")
        buf.write("\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008a\3\2\2\2")
        buf.write("\u008c\u008d\3\2\2\2\u008d\u00aa\3\2\2\2\u008e\u0090\5")
        buf.write("\22\n\2\u008f\u0091\7\5\2\2\u0090\u008f\3\2\2\2\u0091")
        buf.write("\u0092\3\2\2\2\u0092\u0090\3\2\2\2\u0092\u0093\3\2\2\2")
        buf.write("\u0093\u00aa\3\2\2\2\u0094\u0096\5\24\13\2\u0095\u0097")
        buf.write("\7\5\2\2\u0096\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098")
        buf.write("\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u00aa\3\2\2\2")
        buf.write("\u009a\u009c\5\26\f\2\u009b\u009d\7\5\2\2\u009c\u009b")
        buf.write("\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u009c\3\2\2\2\u009e")
        buf.write("\u009f\3\2\2\2\u009f\u00aa\3\2\2\2\u00a0\u00a2\5\30\r")
        buf.write("\2\u00a1\u00a3\7\5\2\2\u00a2\u00a1\3\2\2\2\u00a3\u00a4")
        buf.write("\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5")
        buf.write("\u00aa\3\2\2\2\u00a6\u00aa\5\32\16\2\u00a7\u00aa\5\36")
        buf.write("\20\2\u00a8\u00aa\5\62\32\2\u00a9|\3\2\2\2\u00a9\u0082")
        buf.write("\3\2\2\2\u00a9\u0088\3\2\2\2\u00a9\u008e\3\2\2\2\u00a9")
        buf.write("\u0094\3\2\2\2\u00a9\u009a\3\2\2\2\u00a9\u00a0\3\2\2\2")
        buf.write("\u00a9\u00a6\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00a8\3")
        buf.write("\2\2\2\u00aa\13\3\2\2\2\u00ab\u00ac\7\13\2\2\u00ac\u00ad")
        buf.write("\7?\2\2\u00ad\u00b0\7\'\2\2\u00ae\u00b1\5@!\2\u00af\u00b1")
        buf.write("\5B\"\2\u00b0\u00ae\3\2\2\2\u00b0\u00af\3\2\2\2\u00b1")
        buf.write("\r\3\2\2\2\u00b2\u00b3\7\f\2\2\u00b3\u00b4\7?\2\2\u00b4")
        buf.write("\u00b7\7\'\2\2\u00b5\u00b8\5T+\2\u00b6\u00b8\5N(\2\u00b7")
        buf.write("\u00b5\3\2\2\2\u00b7\u00b6\3\2\2\2\u00b8\17\3\2\2\2\u00b9")
        buf.write("\u00ba\7\t\2\2\u00ba\u00bb\7?\2\2\u00bb\u00bc\7\'\2\2")
        buf.write("\u00bc\u00bd\5D#\2\u00bd\21\3\2\2\2\u00be\u00bf\7\7\2")
        buf.write("\2\u00bf\u00c0\7?\2\2\u00c0\u00c1\7\'\2\2\u00c1\u00c2")
        buf.write("\5B\"\2\u00c2\23\3\2\2\2\u00c3\u00c4\7\n\2\2\u00c4\u00c5")
        buf.write("\7?\2\2\u00c5\u00c6\7\'\2\2\u00c6\u00c7\5B\"\2\u00c7\25")
        buf.write("\3\2\2\2\u00c8\u00c9\7\b\2\2\u00c9\u00ca\7?\2\2\u00ca")
        buf.write("\u00cb\7\'\2\2\u00cb\u00cc\5@!\2\u00cc\27\3\2\2\2\u00cd")
        buf.write("\u00ce\7\22\2\2\u00ce\u00cf\7?\2\2\u00cf\u00d0\7\'\2\2")
        buf.write("\u00d0\u00d1\5@!\2\u00d1\31\3\2\2\2\u00d2\u00d3\7\21\2")
        buf.write("\2\u00d3\u00d4\7?\2\2\u00d4\u00d5\7\62\2\2\u00d5\u00d6")
        buf.write("\7\3\2\2\u00d6\u00d7\7\35\2\2\u00d7\u00d8\5\34\17\2\u00d8")
        buf.write("\u00d9\7\3\2\2\u00d9\u00da\5\"\22\2\u00da\u00db\7\4\2")
        buf.write("\2\u00db\u00dc\7\36\2\2\u00dc\u00e0\5\34\17\2\u00dd\u00df")
        buf.write("\7\5\2\2\u00de\u00dd\3\2\2\2\u00df\u00e2\3\2\2\2\u00e0")
        buf.write("\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e3\3\2\2\2")
        buf.write("\u00e2\u00e0\3\2\2\2\u00e3\u00e4\7\4\2\2\u00e4\33\3\2")
        buf.write("\2\2\u00e5\u00e8\5B\"\2\u00e6\u00e8\7&\2\2\u00e7\u00e5")
        buf.write("\3\2\2\2\u00e7\u00e6\3\2\2\2\u00e8\35\3\2\2\2\u00e9\u00ea")
        buf.write("\7\17\2\2\u00ea\u00eb\7?\2\2\u00eb\u00ec\7\62\2\2\u00ec")
        buf.write("\u00ed\7\3\2\2\u00ed\u00ee\5 \21\2\u00ee\u00ef\7\4\2\2")
        buf.write("\u00ef\37\3\2\2\2\u00f0\u00f2\5$\23\2\u00f1\u00f3\7\5")
        buf.write("\2\2\u00f2\u00f1\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f2")
        buf.write("\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f7\3\2\2\2\u00f6")
        buf.write("\u00f0\3\2\2\2\u00f7\u00fa\3\2\2\2\u00f8\u00f6\3\2\2\2")
        buf.write("\u00f8\u00f9\3\2\2\2\u00f9\u00fc\3\2\2\2\u00fa\u00f8\3")
        buf.write("\2\2\2\u00fb\u00fd\5\"\22\2\u00fc\u00fb\3\2\2\2\u00fc")
        buf.write("\u00fd\3\2\2\2\u00fd!\3\2\2\2\u00fe\u0102\5&\24\2\u00ff")
        buf.write("\u0101\7\5\2\2\u0100\u00ff\3\2\2\2\u0101\u0104\3\2\2\2")
        buf.write("\u0102\u0100\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u010f\3")
        buf.write("\2\2\2\u0104\u0102\3\2\2\2\u0105\u0106\7 \2\2\u0106\u010a")
        buf.write("\5&\24\2\u0107\u0109\7\5\2\2\u0108\u0107\3\2\2\2\u0109")
        buf.write("\u010c\3\2\2\2\u010a\u0108\3\2\2\2\u010a\u010b\3\2\2\2")
        buf.write("\u010b\u010e\3\2\2\2\u010c\u010a\3\2\2\2\u010d\u0105\3")
        buf.write("\2\2\2\u010e\u0111\3\2\2\2\u010f\u010d\3\2\2\2\u010f\u0110")
        buf.write("\3\2\2\2\u0110#\3\2\2\2\u0111\u010f\3\2\2\2\u0112\u0113")
        buf.write("\7\23\2\2\u0113\u0114\5(\25\2\u0114%\3\2\2\2\u0115\u0119")
        buf.write("\5(\25\2\u0116\u0119\5*\26\2\u0117\u0119\5,\27\2\u0118")
        buf.write("\u0115\3\2\2\2\u0118\u0116\3\2\2\2\u0118\u0117\3\2\2\2")
        buf.write("\u0119\'\3\2\2\2\u011a\u011d\7\20\2\2\u011b\u011e\7?\2")
        buf.write("\2\u011c\u011e\5@!\2\u011d\u011b\3\2\2\2\u011d\u011c\3")
        buf.write("\2\2\2\u011e)\3\2\2\2\u011f\u0120\7\31\2\2\u0120\u0121")
        buf.write("\5B\"\2\u0121\u0122\7\62\2\2\u0122\u0123\7\3\2\2\u0123")
        buf.write("\u0124\5 \21\2\u0124\u012e\7\4\2\2\u0125\u0126\7\33\2")
        buf.write("\2\u0126\u0127\5B\"\2\u0127\u0128\7\62\2\2\u0128\u0129")
        buf.write("\7\3\2\2\u0129\u012a\5 \21\2\u012a\u012b\7\4\2\2\u012b")
        buf.write("\u012d\3\2\2\2\u012c\u0125\3\2\2\2\u012d\u0130\3\2\2\2")
        buf.write("\u012e\u012c\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u0137\3")
        buf.write("\2\2\2\u0130\u012e\3\2\2\2\u0131\u0132\7\32\2\2\u0132")
        buf.write("\u0133\7\62\2\2\u0133\u0134\7\3\2\2\u0134\u0135\5 \21")
        buf.write("\2\u0135\u0136\7\4\2\2\u0136\u0138\3\2\2\2\u0137\u0131")
        buf.write("\3\2\2\2\u0137\u0138\3\2\2\2\u0138+\3\2\2\2\u0139\u013e")
        buf.write("\5.\30\2\u013a\u013b\7\"\2\2\u013b\u013d\5.\30\2\u013c")
        buf.write("\u013a\3\2\2\2\u013d\u0140\3\2\2\2\u013e\u013c\3\2\2\2")
        buf.write("\u013e\u013f\3\2\2\2\u013f-\3\2\2\2\u0140\u013e\3\2\2")
        buf.write("\2\u0141\u0142\5\60\31\2\u0142\u0143\7\62\2\2\u0143\u0144")
        buf.write("\7\3\2\2\u0144\u0145\5\"\22\2\u0145\u0146\7\4\2\2\u0146")
        buf.write("\u014f\3\2\2\2\u0147\u0148\5(\25\2\u0148\u014a\5\60\31")
        buf.write("\2\u0149\u014b\7\5\2\2\u014a\u0149\3\2\2\2\u014b\u014c")
        buf.write("\3\2\2\2\u014c\u014a\3\2\2\2\u014c\u014d\3\2\2\2\u014d")
        buf.write("\u014f\3\2\2\2\u014e\u0141\3\2\2\2\u014e\u0147\3\2\2\2")
        buf.write("\u014f/\3\2\2\2\u0150\u0151\7\37\2\2\u0151\u0152\7\27")
        buf.write("\2\2\u0152\u0155\7\66\2\2\u0153\u0156\5T+\2\u0154\u0156")
        buf.write("\5R*\2\u0155\u0153\3\2\2\2\u0155\u0154\3\2\2\2\u0156\u0157")
        buf.write("\3\2\2\2\u0157\u0158\7\67\2\2\u0158\61\3\2\2\2\u0159\u015b")
        buf.write("\7\r\2\2\u015a\u015c\7?\2\2\u015b\u015a\3\2\2\2\u015b")
        buf.write("\u015c\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015e\7\62\2")
        buf.write("\2\u015e\u0166\7\3\2\2\u015f\u0163\5\64\33\2\u0160\u0162")
        buf.write("\7\5\2\2\u0161\u0160\3\2\2\2\u0162\u0165\3\2\2\2\u0163")
        buf.write("\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0167\3\2\2\2")
        buf.write("\u0165\u0163\3\2\2\2\u0166\u015f\3\2\2\2\u0167\u0168\3")
        buf.write("\2\2\2\u0168\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016a")
        buf.write("\3\2\2\2\u016a\u016b\7\4\2\2\u016b\63\3\2\2\2\u016c\u0172")
        buf.write("\5\66\34\2\u016d\u0172\58\35\2\u016e\u0172\5:\36\2\u016f")
        buf.write("\u0172\5<\37\2\u0170\u0172\5> \2\u0171\u016c\3\2\2\2\u0171")
        buf.write("\u016d\3\2\2\2\u0171\u016e\3\2\2\2\u0171\u016f\3\2\2\2")
        buf.write("\u0171\u0170\3\2\2\2\u0172\65\3\2\2\2\u0173\u0174\7\16")
        buf.write("\2\2\u0174\u0175\5@!\2\u0175\67\3\2\2\2\u0176\u0178\7")
        buf.write("?\2\2\u0177\u0179\7\30\2\2\u0178\u0177\3\2\2\2\u0178\u0179")
        buf.write("\3\2\2\2\u0179\u017c\3\2\2\2\u017a\u017c\7\24\2\2\u017b")
        buf.write("\u0176\3\2\2\2\u017b\u017a\3\2\2\2\u017c\u017d\3\2\2\2")
        buf.write("\u017d\u017e\7(\2\2\u017e\u017f\5@!\2\u017f9\3\2\2\2\u0180")
        buf.write("\u0181\7(\2\2\u0181\u0182\7?\2\2\u0182;\3\2\2\2\u0183")
        buf.write("\u0184\7\37\2\2\u0184\u0185\7\27\2\2\u0185\u0186\7\66")
        buf.write("\2\2\u0186\u0187\5T+\2\u0187\u0188\7\67\2\2\u0188\u0189")
        buf.write("\7\62\2\2\u0189\u0191\7\3\2\2\u018a\u018e\5\64\33\2\u018b")
        buf.write("\u018d\7\5\2\2\u018c\u018b\3\2\2\2\u018d\u0190\3\2\2\2")
        buf.write("\u018e\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u0192\3")
        buf.write("\2\2\2\u0190\u018e\3\2\2\2\u0191\u018a\3\2\2\2\u0192\u0193")
        buf.write("\3\2\2\2\u0193\u0191\3\2\2\2\u0193\u0194\3\2\2\2\u0194")
        buf.write("\u0195\3\2\2\2\u0195\u0196\7\4\2\2\u0196=\3\2\2\2\u0197")
        buf.write("\u0198\7\31\2\2\u0198\u0199\5B\"\2\u0199\u019a\7\62\2")
        buf.write("\2\u019a\u01a2\7\3\2\2\u019b\u019f\5\64\33\2\u019c\u019e")
        buf.write("\7\5\2\2\u019d\u019c\3\2\2\2\u019e\u01a1\3\2\2\2\u019f")
        buf.write("\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a3\3\2\2\2")
        buf.write("\u01a1\u019f\3\2\2\2\u01a2\u019b\3\2\2\2\u01a3\u01a4\3")
        buf.write("\2\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a6")
        buf.write("\3\2\2\2\u01a6\u01ba\7\4\2\2\u01a7\u01a8\7\33\2\2\u01a8")
        buf.write("\u01a9\5B\"\2\u01a9\u01aa\7\62\2\2\u01aa\u01b2\7\3\2\2")
        buf.write("\u01ab\u01af\5\64\33\2\u01ac\u01ae\7\5\2\2\u01ad\u01ac")
        buf.write("\3\2\2\2\u01ae\u01b1\3\2\2\2\u01af\u01ad\3\2\2\2\u01af")
        buf.write("\u01b0\3\2\2\2\u01b0\u01b3\3\2\2\2\u01b1\u01af\3\2\2\2")
        buf.write("\u01b2\u01ab\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b2\3")
        buf.write("\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01b7")
        buf.write("\7\4\2\2\u01b7\u01b9\3\2\2\2\u01b8\u01a7\3\2\2\2\u01b9")
        buf.write("\u01bc\3\2\2\2\u01ba\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2")
        buf.write("\u01bb\u01cf\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bd\u01be\7")
        buf.write("\32\2\2\u01be\u01bf\7\62\2\2\u01bf\u01c7\7\3\2\2\u01c0")
        buf.write("\u01c4\5\64\33\2\u01c1\u01c3\7\5\2\2\u01c2\u01c1\3\2\2")
        buf.write("\2\u01c3\u01c6\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4\u01c5")
        buf.write("\3\2\2\2\u01c5\u01c8\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c7")
        buf.write("\u01c0\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01c7\3\2\2\2")
        buf.write("\u01c9\u01ca\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01cc\7")
        buf.write("\4\2\2\u01cc\u01ce\3\2\2\2\u01cd\u01bd\3\2\2\2\u01ce\u01d1")
        buf.write("\3\2\2\2\u01cf\u01cd\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0")
        buf.write("?\3\2\2\2\u01d1\u01cf\3\2\2\2\u01d2\u01d3\b!\1\2\u01d3")
        buf.write("\u01d4\7\66\2\2\u01d4\u01d5\5@!\2\u01d5\u01d6\7\67\2\2")
        buf.write("\u01d6\u01db\3\2\2\2\u01d7\u01db\5T+\2\u01d8\u01db\5H")
        buf.write("%\2\u01d9\u01db\5D#\2\u01da\u01d2\3\2\2\2\u01da\u01d7")
        buf.write("\3\2\2\2\u01da\u01d8\3\2\2\2\u01da\u01d9\3\2\2\2\u01db")
        buf.write("\u01e4\3\2\2\2\u01dc\u01dd\f\7\2\2\u01dd\u01de\t\2\2\2")
        buf.write("\u01de\u01e3\5@!\b\u01df\u01e0\f\6\2\2\u01e0\u01e1\t\3")
        buf.write("\2\2\u01e1\u01e3\5@!\7\u01e2\u01dc\3\2\2\2\u01e2\u01df")
        buf.write("\3\2\2\2\u01e3\u01e6\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e4")
        buf.write("\u01e5\3\2\2\2\u01e5A\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e7")
        buf.write("\u01e8\b\"\1\2\u01e8\u01e9\7\66\2\2\u01e9\u01ea\5B\"\2")
        buf.write("\u01ea\u01eb\7\67\2\2\u01eb\u01f9\3\2\2\2\u01ec\u01ed")
        buf.write("\7#\2\2\u01ed\u01f9\5B\"\b\u01ee\u01ef\5@!\2\u01ef\u01f0")
        buf.write("\7\34\2\2\u01f0\u01f1\5@!\2\u01f1\u01f9\3\2\2\2\u01f2")
        buf.write("\u01f3\5@!\2\u01f3\u01f4\t\4\2\2\u01f4\u01f5\5@!\2\u01f5")
        buf.write("\u01f9\3\2\2\2\u01f6\u01f9\5D#\2\u01f7\u01f9\t\5\2\2\u01f8")
        buf.write("\u01e7\3\2\2\2\u01f8\u01ec\3\2\2\2\u01f8\u01ee\3\2\2\2")
        buf.write("\u01f8\u01f2\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f8\u01f7\3")
        buf.write("\2\2\2\u01f9\u0205\3\2\2\2\u01fa\u01fb\f\n\2\2\u01fb\u01fc")
        buf.write("\7!\2\2\u01fc\u0204\5B\"\13\u01fd\u01fe\f\t\2\2\u01fe")
        buf.write("\u01ff\7\"\2\2\u01ff\u0204\5B\"\n\u0200\u0201\f\6\2\2")
        buf.write("\u0201\u0202\t\6\2\2\u0202\u0204\5B\"\7\u0203\u01fa\3")
        buf.write("\2\2\2\u0203\u01fd\3\2\2\2\u0203\u0200\3\2\2\2\u0204\u0207")
        buf.write("\3\2\2\2\u0205\u0203\3\2\2\2\u0205\u0206\3\2\2\2\u0206")
        buf.write("C\3\2\2\2\u0207\u0205\3\2\2\2\u0208\u020a\7?\2\2\u0209")
        buf.write("\u020b\7\30\2\2\u020a\u0209\3\2\2\2\u020a\u020b\3\2\2")
        buf.write("\2\u020b\u020f\3\2\2\2\u020c\u020e\5F$\2\u020d\u020c\3")
        buf.write("\2\2\2\u020e\u0211\3\2\2\2\u020f\u020d\3\2\2\2\u020f\u0210")
        buf.write("\3\2\2\2\u0210\u021c\3\2\2\2\u0211\u020f\3\2\2\2\u0212")
        buf.write("\u0214\7\25\2\2\u0213\u0215\5F$\2\u0214\u0213\3\2\2\2")
        buf.write("\u0214\u0215\3\2\2\2\u0215\u021c\3\2\2\2\u0216\u0218\7")
        buf.write("\24\2\2\u0217\u0219\5F$\2\u0218\u0217\3\2\2\2\u0218\u0219")
        buf.write("\3\2\2\2\u0219\u021c\3\2\2\2\u021a\u021c\7\26\2\2\u021b")
        buf.write("\u0208\3\2\2\2\u021b\u0212\3\2\2\2\u021b\u0216\3\2\2\2")
        buf.write("\u021b\u021a\3\2\2\2\u021cE\3\2\2\2\u021d\u0220\5L\'\2")
        buf.write("\u021e\u0220\5P)\2\u021f\u021d\3\2\2\2\u021f\u021e\3\2")
        buf.write("\2\2\u0220G\3\2\2\2\u0221\u0224\5J&\2\u0222\u0224\5N(")
        buf.write("\2\u0223\u0221\3\2\2\2\u0223\u0222\3\2\2\2\u0224I\3\2")
        buf.write("\2\2\u0225\u0232\5N(\2\u0226\u0227\7\64\2\2\u0227\u022c")
        buf.write("\5J&\2\u0228\u0229\7\63\2\2\u0229\u022b\5J&\2\u022a\u0228")
        buf.write("\3\2\2\2\u022b\u022e\3\2\2\2\u022c\u022a\3\2\2\2\u022c")
        buf.write("\u022d\3\2\2\2\u022d\u022f\3\2\2\2\u022e\u022c\3\2\2\2")
        buf.write("\u022f\u0230\7\65\2\2\u0230\u0232\3\2\2\2\u0231\u0225")
        buf.write("\3\2\2\2\u0231\u0226\3\2\2\2\u0232K\3\2\2\2\u0233\u0234")
        buf.write("\7\64\2\2\u0234\u0239\5V,\2\u0235\u0236\7\63\2\2\u0236")
        buf.write("\u0238\5V,\2\u0237\u0235\3\2\2\2\u0238\u023b\3\2\2\2\u0239")
        buf.write("\u0237\3\2\2\2\u0239\u023a\3\2\2\2\u023a\u023c\3\2\2\2")
        buf.write("\u023b\u0239\3\2\2\2\u023c\u023d\7\65\2\2\u023dM\3\2\2")
        buf.write("\2\u023e\u023f\7\64\2\2\u023f\u0244\5T+\2\u0240\u0241")
        buf.write("\7\63\2\2\u0241\u0243\5T+\2\u0242\u0240\3\2\2\2\u0243")
        buf.write("\u0246\3\2\2\2\u0244\u0242\3\2\2\2\u0244\u0245\3\2\2\2")
        buf.write("\u0245\u0247\3\2\2\2\u0246\u0244\3\2\2\2\u0247\u0248\7")
        buf.write("\65\2\2\u0248O\3\2\2\2\u0249\u024b\7\64\2\2\u024a\u024c")
        buf.write("\5V,\2\u024b\u024a\3\2\2\2\u024b\u024c\3\2\2\2\u024c\u024d")
        buf.write("\3\2\2\2\u024d\u024f\7\62\2\2\u024e\u0250\5V,\2\u024f")
        buf.write("\u024e\3\2\2\2\u024f\u0250\3\2\2\2\u0250\u0251\3\2\2\2")
        buf.write("\u0251\u0252\7\65\2\2\u0252Q\3\2\2\2\u0253\u0254\5V,\2")
        buf.write("\u0254\u0255\7;\2\2\u0255\u0256\5V,\2\u0256S\3\2\2\2\u0257")
        buf.write("\u025a\5V,\2\u0258\u025a\5X-\2\u0259\u0257\3\2\2\2\u0259")
        buf.write("\u0258\3\2\2\2\u025aU\3\2\2\2\u025b\u025d\7=\2\2\u025c")
        buf.write("\u025b\3\2\2\2\u025c\u025d\3\2\2\2\u025d\u025e\3\2\2\2")
        buf.write("\u025e\u025f\7A\2\2\u025fW\3\2\2\2\u0260\u0262\7=\2\2")
        buf.write("\u0261\u0260\3\2\2\2\u0261\u0262\3\2\2\2\u0262\u0263\3")
        buf.write("\2\2\2\u0263\u0264\7@\2\2\u0264Y\3\2\2\2G]elpy\u0080\u0086")
        buf.write("\u008c\u0092\u0098\u009e\u00a4\u00a9\u00b0\u00b7\u00e0")
        buf.write("\u00e7\u00f4\u00f8\u00fc\u0102\u010a\u010f\u0118\u011d")
        buf.write("\u012e\u0137\u013e\u014c\u014e\u0155\u015b\u0163\u0168")
        buf.write("\u0171\u0178\u017b\u018e\u0193\u019f\u01a4\u01af\u01b4")
        buf.write("\u01ba\u01c4\u01c9\u01cf\u01da\u01e2\u01e4\u01f8\u0203")
        buf.write("\u0205\u020a\u020f\u0214\u0218\u021b\u021f\u0223\u022c")
        buf.write("\u0231\u0239\u0244\u024b\u024f\u0259\u025c\u0261")
        return buf.getvalue()


class RLangParser ( Parser ):

    grammarFileName = "RLangParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'import'", "'Predicate'", "'Feature'", "'Factor'", 
                     "'Goal'", "'Constant'", "'Action'", "'Effect'", "'Reward'", 
                     "'Policy'", "'Execute'", "'Option'", "'MarkovFeature'", 
                     "'Never'", "<INVALID>", "'S'", "'A'", "'P'", "'''", 
                     "'if'", "'else'", "'elif'", "'in'", "'init'", "'until'", 
                     "'with'", "'then'", "'and'", "'or'", "'not'", "'True'", 
                     "'False'", "'Any'", "':='", "'->'", "'='", "'*='", 
                     "'/='", "'+='", "'-='", "'=='", "'>='", "'<='", "'!='", 
                     "':'", "','", "'['", "']'", "'('", "')'", "'<'", "'>'", 
                     "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "INDENT", "DEDENT", "NL", "IMPORT", "PREDICATE", 
                      "FEATURE", "FACTOR", "GOAL", "CONSTANT", "ACTION", 
                      "EFFECT", "REWARD", "POLICY", "EXECUTE", "OPTION", 
                      "MARKOVFEATURE", "NEVER", "S_PRIME", "S", "A", "P", 
                      "PRIME", "IF", "ELSE", "ELIF", "IN", "INIT", "UNTIL", 
                      "WITH", "THEN", "AND", "OR", "NOT", "TRUE", "FALSE", 
                      "ANY_CONDITION", "BIND", "PREDICT", "ASSIGN", "TIMES_EQ", 
                      "DIV_EQ", "PLUS_EQ", "MINUS_EQ", "EQ_TO", "GT_EQ", 
                      "LT_EQ", "NOT_EQ", "COL", "COM", "L_BRK", "R_BRK", 
                      "L_PAR", "R_PAR", "LT", "GT", "TIMES", "DIVIDE", "PLUS", 
                      "MINUS", "FNAME", "IDENTIFIER", "DECIMAL", "INTEGER", 
                      "SKIP_", "ANY" ]

    RULE_program = 0
    RULE_imports = 1
    RULE_import_stat = 2
    RULE_declarations = 3
    RULE_dec = 4
    RULE_constant = 5
    RULE_action = 6
    RULE_factor = 7
    RULE_predicate = 8
    RULE_goal = 9
    RULE_feature = 10
    RULE_markov_feature = 11
    RULE_option = 12
    RULE_option_condition = 13
    RULE_policy = 14
    RULE_policy_statement_collection = 15
    RULE_non_negative_policy_statement_collection = 16
    RULE_never_policy_statement = 17
    RULE_policy_statement = 18
    RULE_execute = 19
    RULE_conditional_subpolicy = 20
    RULE_probabilistic_subpolicy = 21
    RULE_probabilistic_policy_statement = 22
    RULE_probabilistic_condition = 23
    RULE_effect = 24
    RULE_effect_stat = 25
    RULE_reward = 26
    RULE_prediction = 27
    RULE_effect_reference = 28
    RULE_stochastic_effect = 29
    RULE_conditional_effect_stat = 30
    RULE_arithmetic_exp = 31
    RULE_boolean_exp = 32
    RULE_any_bound_var = 33
    RULE_trailer = 34
    RULE_any_array = 35
    RULE_compound_array_exp = 36
    RULE_int_array_exp = 37
    RULE_any_num_array_exp = 38
    RULE_slice_exp = 39
    RULE_integer_fraction = 40
    RULE_any_number = 41
    RULE_any_integer = 42
    RULE_any_decimal = 43

    ruleNames =  [ "program", "imports", "import_stat", "declarations", 
                   "dec", "constant", "action", "factor", "predicate", "goal", 
                   "feature", "markov_feature", "option", "option_condition", 
                   "policy", "policy_statement_collection", "non_negative_policy_statement_collection", 
                   "never_policy_statement", "policy_statement", "execute", 
                   "conditional_subpolicy", "probabilistic_subpolicy", "probabilistic_policy_statement", 
                   "probabilistic_condition", "effect", "effect_stat", "reward", 
                   "prediction", "effect_reference", "stochastic_effect", 
                   "conditional_effect_stat", "arithmetic_exp", "boolean_exp", 
                   "any_bound_var", "trailer", "any_array", "compound_array_exp", 
                   "int_array_exp", "any_num_array_exp", "slice_exp", "integer_fraction", 
                   "any_number", "any_integer", "any_decimal" ]

    EOF = Token.EOF
    INDENT=1
    DEDENT=2
    NL=3
    IMPORT=4
    PREDICATE=5
    FEATURE=6
    FACTOR=7
    GOAL=8
    CONSTANT=9
    ACTION=10
    EFFECT=11
    REWARD=12
    POLICY=13
    EXECUTE=14
    OPTION=15
    MARKOVFEATURE=16
    NEVER=17
    S_PRIME=18
    S=19
    A=20
    P=21
    PRIME=22
    IF=23
    ELSE=24
    ELIF=25
    IN=26
    INIT=27
    UNTIL=28
    WITH=29
    THEN=30
    AND=31
    OR=32
    NOT=33
    TRUE=34
    FALSE=35
    ANY_CONDITION=36
    BIND=37
    PREDICT=38
    ASSIGN=39
    TIMES_EQ=40
    DIV_EQ=41
    PLUS_EQ=42
    MINUS_EQ=43
    EQ_TO=44
    GT_EQ=45
    LT_EQ=46
    NOT_EQ=47
    COL=48
    COM=49
    L_BRK=50
    R_BRK=51
    L_PAR=52
    R_PAR=53
    LT=54
    GT=55
    TIMES=56
    DIVIDE=57
    PLUS=58
    MINUS=59
    FNAME=60
    IDENTIFIER=61
    DECIMAL=62
    INTEGER=63
    SKIP_=64
    ANY=65

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def imports(self):
            return self.getTypedRuleContext(RLangParser.ImportsContext,0)


        def declarations(self):
            return self.getTypedRuleContext(RLangParser.DeclarationsContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.NL)
            else:
                return self.getToken(RLangParser.NL, i)

        def getRuleIndex(self):
            return RLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = RLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 88
                    self.match(RLangParser.NL) 
                self.state = 93
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 94
            self.imports()
            self.state = 95
            self.declarations()
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.NL:
                self.state = 96
                self.match(RLangParser.NL)
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def import_stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Import_statContext)
            else:
                return self.getTypedRuleContext(RLangParser.Import_statContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.NL)
            else:
                return self.getToken(RLangParser.NL, i)

        def getRuleIndex(self):
            return RLangParser.RULE_imports

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImports" ):
                listener.enterImports(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImports" ):
                listener.exitImports(self)




    def imports(self):

        localctx = RLangParser.ImportsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_imports)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.IMPORT:
                self.state = 102
                self.import_stat()
                self.state = 104 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 103
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 106 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(RLangParser.IMPORT, 0)

        def FNAME(self):
            return self.getToken(RLangParser.FNAME, 0)

        def getRuleIndex(self):
            return RLangParser.RULE_import_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_stat" ):
                listener.enterImport_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_stat" ):
                listener.exitImport_stat(self)




    def import_stat(self):

        localctx = RLangParser.Import_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_import_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(RLangParser.IMPORT)
            self.state = 114
            self.match(RLangParser.FNAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.DecContext)
            else:
                return self.getTypedRuleContext(RLangParser.DecContext,i)


        def getRuleIndex(self):
            return RLangParser.RULE_declarations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarations" ):
                listener.enterDeclarations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarations" ):
                listener.exitDeclarations(self)




    def declarations(self):

        localctx = RLangParser.DeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declarations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RLangParser.PREDICATE) | (1 << RLangParser.FEATURE) | (1 << RLangParser.FACTOR) | (1 << RLangParser.GOAL) | (1 << RLangParser.CONSTANT) | (1 << RLangParser.ACTION) | (1 << RLangParser.EFFECT) | (1 << RLangParser.POLICY) | (1 << RLangParser.OPTION) | (1 << RLangParser.MARKOVFEATURE))) != 0):
                self.state = 116
                self.dec()
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constant(self):
            return self.getTypedRuleContext(RLangParser.ConstantContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.NL)
            else:
                return self.getToken(RLangParser.NL, i)

        def action(self):
            return self.getTypedRuleContext(RLangParser.ActionContext,0)


        def factor(self):
            return self.getTypedRuleContext(RLangParser.FactorContext,0)


        def predicate(self):
            return self.getTypedRuleContext(RLangParser.PredicateContext,0)


        def goal(self):
            return self.getTypedRuleContext(RLangParser.GoalContext,0)


        def feature(self):
            return self.getTypedRuleContext(RLangParser.FeatureContext,0)


        def markov_feature(self):
            return self.getTypedRuleContext(RLangParser.Markov_featureContext,0)


        def option(self):
            return self.getTypedRuleContext(RLangParser.OptionContext,0)


        def policy(self):
            return self.getTypedRuleContext(RLangParser.PolicyContext,0)


        def effect(self):
            return self.getTypedRuleContext(RLangParser.EffectContext,0)


        def getRuleIndex(self):
            return RLangParser.RULE_dec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDec" ):
                listener.enterDec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDec" ):
                listener.exitDec(self)




    def dec(self):

        localctx = RLangParser.DecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_dec)
        try:
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.CONSTANT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.constant()
                self.state = 124 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 123
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 126 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                pass
            elif token in [RLangParser.ACTION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.action()
                self.state = 130 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 129
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 132 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                pass
            elif token in [RLangParser.FACTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 134
                self.factor()
                self.state = 136 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 135
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 138 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                pass
            elif token in [RLangParser.PREDICATE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 140
                self.predicate()
                self.state = 142 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 141
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 144 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                pass
            elif token in [RLangParser.GOAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 146
                self.goal()
                self.state = 148 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 147
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 150 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                pass
            elif token in [RLangParser.FEATURE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 152
                self.feature()
                self.state = 154 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 153
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 156 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                pass
            elif token in [RLangParser.MARKOVFEATURE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 158
                self.markov_feature()
                self.state = 160 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 159
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 162 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                pass
            elif token in [RLangParser.OPTION]:
                self.enterOuterAlt(localctx, 8)
                self.state = 164
                self.option()
                pass
            elif token in [RLangParser.POLICY]:
                self.enterOuterAlt(localctx, 9)
                self.state = 165
                self.policy()
                pass
            elif token in [RLangParser.EFFECT]:
                self.enterOuterAlt(localctx, 10)
                self.state = 166
                self.effect()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTANT(self):
            return self.getToken(RLangParser.CONSTANT, 0)

        def IDENTIFIER(self):
            return self.getToken(RLangParser.IDENTIFIER, 0)

        def BIND(self):
            return self.getToken(RLangParser.BIND, 0)

        def arithmetic_exp(self):
            return self.getTypedRuleContext(RLangParser.Arithmetic_expContext,0)


        def boolean_exp(self):
            return self.getTypedRuleContext(RLangParser.Boolean_expContext,0)


        def getRuleIndex(self):
            return RLangParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)




    def constant(self):

        localctx = RLangParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_constant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(RLangParser.CONSTANT)
            self.state = 170
            self.match(RLangParser.IDENTIFIER)
            self.state = 171
            self.match(RLangParser.BIND)
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 172
                self.arithmetic_exp(0)
                pass

            elif la_ == 2:
                self.state = 173
                self.boolean_exp(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACTION(self):
            return self.getToken(RLangParser.ACTION, 0)

        def IDENTIFIER(self):
            return self.getToken(RLangParser.IDENTIFIER, 0)

        def BIND(self):
            return self.getToken(RLangParser.BIND, 0)

        def any_number(self):
            return self.getTypedRuleContext(RLangParser.Any_numberContext,0)


        def any_num_array_exp(self):
            return self.getTypedRuleContext(RLangParser.Any_num_array_expContext,0)


        def getRuleIndex(self):
            return RLangParser.RULE_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction" ):
                listener.enterAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction" ):
                listener.exitAction(self)




    def action(self):

        localctx = RLangParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(RLangParser.ACTION)
            self.state = 177
            self.match(RLangParser.IDENTIFIER)
            self.state = 178
            self.match(RLangParser.BIND)
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.MINUS, RLangParser.DECIMAL, RLangParser.INTEGER]:
                self.state = 179
                self.any_number()
                pass
            elif token in [RLangParser.L_BRK]:
                self.state = 180
                self.any_num_array_exp()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FACTOR(self):
            return self.getToken(RLangParser.FACTOR, 0)

        def IDENTIFIER(self):
            return self.getToken(RLangParser.IDENTIFIER, 0)

        def BIND(self):
            return self.getToken(RLangParser.BIND, 0)

        def any_bound_var(self):
            return self.getTypedRuleContext(RLangParser.Any_bound_varContext,0)


        def getRuleIndex(self):
            return RLangParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = RLangParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_factor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(RLangParser.FACTOR)
            self.state = 184
            self.match(RLangParser.IDENTIFIER)
            self.state = 185
            self.match(RLangParser.BIND)
            self.state = 186
            self.any_bound_var()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PredicateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREDICATE(self):
            return self.getToken(RLangParser.PREDICATE, 0)

        def IDENTIFIER(self):
            return self.getToken(RLangParser.IDENTIFIER, 0)

        def BIND(self):
            return self.getToken(RLangParser.BIND, 0)

        def boolean_exp(self):
            return self.getTypedRuleContext(RLangParser.Boolean_expContext,0)


        def getRuleIndex(self):
            return RLangParser.RULE_predicate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicate" ):
                listener.enterPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicate" ):
                listener.exitPredicate(self)




    def predicate(self):

        localctx = RLangParser.PredicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_predicate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(RLangParser.PREDICATE)
            self.state = 189
            self.match(RLangParser.IDENTIFIER)
            self.state = 190
            self.match(RLangParser.BIND)
            self.state = 191
            self.boolean_exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GoalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GOAL(self):
            return self.getToken(RLangParser.GOAL, 0)

        def IDENTIFIER(self):
            return self.getToken(RLangParser.IDENTIFIER, 0)

        def BIND(self):
            return self.getToken(RLangParser.BIND, 0)

        def boolean_exp(self):
            return self.getTypedRuleContext(RLangParser.Boolean_expContext,0)


        def getRuleIndex(self):
            return RLangParser.RULE_goal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGoal" ):
                listener.enterGoal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGoal" ):
                listener.exitGoal(self)




    def goal(self):

        localctx = RLangParser.GoalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_goal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(RLangParser.GOAL)
            self.state = 194
            self.match(RLangParser.IDENTIFIER)
            self.state = 195
            self.match(RLangParser.BIND)
            self.state = 196
            self.boolean_exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FeatureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FEATURE(self):
            return self.getToken(RLangParser.FEATURE, 0)

        def IDENTIFIER(self):
            return self.getToken(RLangParser.IDENTIFIER, 0)

        def BIND(self):
            return self.getToken(RLangParser.BIND, 0)

        def arithmetic_exp(self):
            return self.getTypedRuleContext(RLangParser.Arithmetic_expContext,0)


        def getRuleIndex(self):
            return RLangParser.RULE_feature

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFeature" ):
                listener.enterFeature(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFeature" ):
                listener.exitFeature(self)




    def feature(self):

        localctx = RLangParser.FeatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_feature)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(RLangParser.FEATURE)
            self.state = 199
            self.match(RLangParser.IDENTIFIER)
            self.state = 200
            self.match(RLangParser.BIND)
            self.state = 201
            self.arithmetic_exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Markov_featureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MARKOVFEATURE(self):
            return self.getToken(RLangParser.MARKOVFEATURE, 0)

        def IDENTIFIER(self):
            return self.getToken(RLangParser.IDENTIFIER, 0)

        def BIND(self):
            return self.getToken(RLangParser.BIND, 0)

        def arithmetic_exp(self):
            return self.getTypedRuleContext(RLangParser.Arithmetic_expContext,0)


        def getRuleIndex(self):
            return RLangParser.RULE_markov_feature

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMarkov_feature" ):
                listener.enterMarkov_feature(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMarkov_feature" ):
                listener.exitMarkov_feature(self)




    def markov_feature(self):

        localctx = RLangParser.Markov_featureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_markov_feature)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(RLangParser.MARKOVFEATURE)
            self.state = 204
            self.match(RLangParser.IDENTIFIER)
            self.state = 205
            self.match(RLangParser.BIND)
            self.state = 206
            self.arithmetic_exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.init = None # Option_conditionContext
            self.until = None # Option_conditionContext

        def OPTION(self):
            return self.getToken(RLangParser.OPTION, 0)

        def IDENTIFIER(self):
            return self.getToken(RLangParser.IDENTIFIER, 0)

        def COL(self):
            return self.getToken(RLangParser.COL, 0)

        def INDENT(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.INDENT)
            else:
                return self.getToken(RLangParser.INDENT, i)

        def INIT(self):
            return self.getToken(RLangParser.INIT, 0)

        def non_negative_policy_statement_collection(self):
            return self.getTypedRuleContext(RLangParser.Non_negative_policy_statement_collectionContext,0)


        def DEDENT(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.DEDENT)
            else:
                return self.getToken(RLangParser.DEDENT, i)

        def UNTIL(self):
            return self.getToken(RLangParser.UNTIL, 0)

        def option_condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Option_conditionContext)
            else:
                return self.getTypedRuleContext(RLangParser.Option_conditionContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.NL)
            else:
                return self.getToken(RLangParser.NL, i)

        def getRuleIndex(self):
            return RLangParser.RULE_option

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOption" ):
                listener.enterOption(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOption" ):
                listener.exitOption(self)




    def option(self):

        localctx = RLangParser.OptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_option)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(RLangParser.OPTION)
            self.state = 209
            self.match(RLangParser.IDENTIFIER)
            self.state = 210
            self.match(RLangParser.COL)
            self.state = 211
            self.match(RLangParser.INDENT)
            self.state = 212
            self.match(RLangParser.INIT)
            self.state = 213
            localctx.init = self.option_condition()
            self.state = 214
            self.match(RLangParser.INDENT)
            self.state = 215
            self.non_negative_policy_statement_collection()
            self.state = 216
            self.match(RLangParser.DEDENT)
            self.state = 217
            self.match(RLangParser.UNTIL)
            self.state = 218
            localctx.until = self.option_condition()
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.NL:
                self.state = 219
                self.match(RLangParser.NL)
                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 225
            self.match(RLangParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Option_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolean_exp(self):
            return self.getTypedRuleContext(RLangParser.Boolean_expContext,0)


        def ANY_CONDITION(self):
            return self.getToken(RLangParser.ANY_CONDITION, 0)

        def getRuleIndex(self):
            return RLangParser.RULE_option_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOption_condition" ):
                listener.enterOption_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOption_condition" ):
                listener.exitOption_condition(self)




    def option_condition(self):

        localctx = RLangParser.Option_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_option_condition)
        try:
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.S_PRIME, RLangParser.S, RLangParser.A, RLangParser.NOT, RLangParser.TRUE, RLangParser.FALSE, RLangParser.L_BRK, RLangParser.L_PAR, RLangParser.MINUS, RLangParser.IDENTIFIER, RLangParser.DECIMAL, RLangParser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.boolean_exp(0)
                pass
            elif token in [RLangParser.ANY_CONDITION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self.match(RLangParser.ANY_CONDITION)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PolicyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POLICY(self):
            return self.getToken(RLangParser.POLICY, 0)

        def IDENTIFIER(self):
            return self.getToken(RLangParser.IDENTIFIER, 0)

        def COL(self):
            return self.getToken(RLangParser.COL, 0)

        def INDENT(self):
            return self.getToken(RLangParser.INDENT, 0)

        def policy_statement_collection(self):
            return self.getTypedRuleContext(RLangParser.Policy_statement_collectionContext,0)


        def DEDENT(self):
            return self.getToken(RLangParser.DEDENT, 0)

        def getRuleIndex(self):
            return RLangParser.RULE_policy

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPolicy" ):
                listener.enterPolicy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPolicy" ):
                listener.exitPolicy(self)




    def policy(self):

        localctx = RLangParser.PolicyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_policy)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(RLangParser.POLICY)
            self.state = 232
            self.match(RLangParser.IDENTIFIER)
            self.state = 233
            self.match(RLangParser.COL)
            self.state = 234
            self.match(RLangParser.INDENT)
            self.state = 235
            self.policy_statement_collection()
            self.state = 236
            self.match(RLangParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Policy_statement_collectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._never_policy_statement = None # Never_policy_statementContext
            self.never_statements = list() # of Never_policy_statementContexts

        def non_negative_policy_statement_collection(self):
            return self.getTypedRuleContext(RLangParser.Non_negative_policy_statement_collectionContext,0)


        def never_policy_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Never_policy_statementContext)
            else:
                return self.getTypedRuleContext(RLangParser.Never_policy_statementContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.NL)
            else:
                return self.getToken(RLangParser.NL, i)

        def getRuleIndex(self):
            return RLangParser.RULE_policy_statement_collection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPolicy_statement_collection" ):
                listener.enterPolicy_statement_collection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPolicy_statement_collection" ):
                listener.exitPolicy_statement_collection(self)




    def policy_statement_collection(self):

        localctx = RLangParser.Policy_statement_collectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_policy_statement_collection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.NEVER:
                self.state = 238
                localctx._never_policy_statement = self.never_policy_statement()
                localctx.never_statements.append(localctx._never_policy_statement)
                self.state = 240 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 239
                    self.match(RLangParser.NL)
                    self.state = 242 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RLangParser.NL):
                        break

                self.state = 248
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RLangParser.EXECUTE) | (1 << RLangParser.IF) | (1 << RLangParser.WITH))) != 0):
                self.state = 249
                self.non_negative_policy_statement_collection()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Non_negative_policy_statement_collectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._policy_statement = None # Policy_statementContext
            self.statements = list() # of Policy_statementContexts

        def policy_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Policy_statementContext)
            else:
                return self.getTypedRuleContext(RLangParser.Policy_statementContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.NL)
            else:
                return self.getToken(RLangParser.NL, i)

        def THEN(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.THEN)
            else:
                return self.getToken(RLangParser.THEN, i)

        def getRuleIndex(self):
            return RLangParser.RULE_non_negative_policy_statement_collection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNon_negative_policy_statement_collection" ):
                listener.enterNon_negative_policy_statement_collection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNon_negative_policy_statement_collection" ):
                listener.exitNon_negative_policy_statement_collection(self)




    def non_negative_policy_statement_collection(self):

        localctx = RLangParser.Non_negative_policy_statement_collectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_non_negative_policy_statement_collection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            localctx._policy_statement = self.policy_statement()
            localctx.statements.append(localctx._policy_statement)
            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.NL:
                self.state = 253
                self.match(RLangParser.NL)
                self.state = 258
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.THEN:
                self.state = 259
                self.match(RLangParser.THEN)
                self.state = 260
                localctx._policy_statement = self.policy_statement()
                localctx.statements.append(localctx._policy_statement)
                self.state = 264
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.NL:
                    self.state = 261
                    self.match(RLangParser.NL)
                    self.state = 266
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 271
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Never_policy_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEVER(self):
            return self.getToken(RLangParser.NEVER, 0)

        def execute(self):
            return self.getTypedRuleContext(RLangParser.ExecuteContext,0)


        def getRuleIndex(self):
            return RLangParser.RULE_never_policy_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNever_policy_statement" ):
                listener.enterNever_policy_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNever_policy_statement" ):
                listener.exitNever_policy_statement(self)




    def never_policy_statement(self):

        localctx = RLangParser.Never_policy_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_never_policy_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(RLangParser.NEVER)
            self.state = 273
            self.execute()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Policy_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RLangParser.RULE_policy_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Policy_statement_executeContext(Policy_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Policy_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def execute(self):
            return self.getTypedRuleContext(RLangParser.ExecuteContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPolicy_statement_execute" ):
                listener.enterPolicy_statement_execute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPolicy_statement_execute" ):
                listener.exitPolicy_statement_execute(self)


    class Policy_statement_probabilisticContext(Policy_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Policy_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def probabilistic_subpolicy(self):
            return self.getTypedRuleContext(RLangParser.Probabilistic_subpolicyContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPolicy_statement_probabilistic" ):
                listener.enterPolicy_statement_probabilistic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPolicy_statement_probabilistic" ):
                listener.exitPolicy_statement_probabilistic(self)


    class Policy_statement_conditionalContext(Policy_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Policy_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def conditional_subpolicy(self):
            return self.getTypedRuleContext(RLangParser.Conditional_subpolicyContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPolicy_statement_conditional" ):
                listener.enterPolicy_statement_conditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPolicy_statement_conditional" ):
                listener.exitPolicy_statement_conditional(self)



    def policy_statement(self):

        localctx = RLangParser.Policy_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_policy_statement)
        try:
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Policy_statement_executeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.execute()
                pass

            elif la_ == 2:
                localctx = RLangParser.Policy_statement_conditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.conditional_subpolicy()
                pass

            elif la_ == 3:
                localctx = RLangParser.Policy_statement_probabilisticContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 277
                self.probabilistic_subpolicy()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExecuteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXECUTE(self):
            return self.getToken(RLangParser.EXECUTE, 0)

        def IDENTIFIER(self):
            return self.getToken(RLangParser.IDENTIFIER, 0)

        def arithmetic_exp(self):
            return self.getTypedRuleContext(RLangParser.Arithmetic_expContext,0)


        def getRuleIndex(self):
            return RLangParser.RULE_execute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExecute" ):
                listener.enterExecute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExecute" ):
                listener.exitExecute(self)




    def execute(self):

        localctx = RLangParser.ExecuteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_execute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(RLangParser.EXECUTE)
            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 281
                self.match(RLangParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 282
                self.arithmetic_exp(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conditional_subpolicyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.if_condition = None # Boolean_expContext
            self.if_subpolicy = None # Policy_statement_collectionContext
            self._boolean_exp = None # Boolean_expContext
            self.elif_conditions = list() # of Boolean_expContexts
            self._policy_statement_collection = None # Policy_statement_collectionContext
            self.elif_subpolicies = list() # of Policy_statement_collectionContexts
            self.else_subpolicy = None # Policy_statement_collectionContext

        def IF(self):
            return self.getToken(RLangParser.IF, 0)

        def COL(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.COL)
            else:
                return self.getToken(RLangParser.COL, i)

        def INDENT(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.INDENT)
            else:
                return self.getToken(RLangParser.INDENT, i)

        def DEDENT(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.DEDENT)
            else:
                return self.getToken(RLangParser.DEDENT, i)

        def boolean_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Boolean_expContext)
            else:
                return self.getTypedRuleContext(RLangParser.Boolean_expContext,i)


        def policy_statement_collection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Policy_statement_collectionContext)
            else:
                return self.getTypedRuleContext(RLangParser.Policy_statement_collectionContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.ELIF)
            else:
                return self.getToken(RLangParser.ELIF, i)

        def ELSE(self):
            return self.getToken(RLangParser.ELSE, 0)

        def getRuleIndex(self):
            return RLangParser.RULE_conditional_subpolicy

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional_subpolicy" ):
                listener.enterConditional_subpolicy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional_subpolicy" ):
                listener.exitConditional_subpolicy(self)




    def conditional_subpolicy(self):

        localctx = RLangParser.Conditional_subpolicyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_conditional_subpolicy)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(RLangParser.IF)
            self.state = 286
            localctx.if_condition = self.boolean_exp(0)
            self.state = 287
            self.match(RLangParser.COL)
            self.state = 288
            self.match(RLangParser.INDENT)
            self.state = 289
            localctx.if_subpolicy = self.policy_statement_collection()
            self.state = 290
            self.match(RLangParser.DEDENT)
            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.ELIF:
                self.state = 291
                self.match(RLangParser.ELIF)
                self.state = 292
                localctx._boolean_exp = self.boolean_exp(0)
                localctx.elif_conditions.append(localctx._boolean_exp)
                self.state = 293
                self.match(RLangParser.COL)
                self.state = 294
                self.match(RLangParser.INDENT)
                self.state = 295
                localctx._policy_statement_collection = self.policy_statement_collection()
                localctx.elif_subpolicies.append(localctx._policy_statement_collection)
                self.state = 296
                self.match(RLangParser.DEDENT)
                self.state = 302
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 309
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.ELSE:
                self.state = 303
                self.match(RLangParser.ELSE)
                self.state = 304
                self.match(RLangParser.COL)
                self.state = 305
                self.match(RLangParser.INDENT)
                self.state = 306
                localctx.else_subpolicy = self.policy_statement_collection()
                self.state = 307
                self.match(RLangParser.DEDENT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Probabilistic_subpolicyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._probabilistic_policy_statement = None # Probabilistic_policy_statementContext
            self.subpolicies = list() # of Probabilistic_policy_statementContexts

        def probabilistic_policy_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Probabilistic_policy_statementContext)
            else:
                return self.getTypedRuleContext(RLangParser.Probabilistic_policy_statementContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.OR)
            else:
                return self.getToken(RLangParser.OR, i)

        def getRuleIndex(self):
            return RLangParser.RULE_probabilistic_subpolicy

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProbabilistic_subpolicy" ):
                listener.enterProbabilistic_subpolicy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProbabilistic_subpolicy" ):
                listener.exitProbabilistic_subpolicy(self)




    def probabilistic_subpolicy(self):

        localctx = RLangParser.Probabilistic_subpolicyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_probabilistic_subpolicy)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            localctx._probabilistic_policy_statement = self.probabilistic_policy_statement()
            localctx.subpolicies.append(localctx._probabilistic_policy_statement)
            self.state = 316
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.OR:
                self.state = 312
                self.match(RLangParser.OR)
                self.state = 313
                localctx._probabilistic_policy_statement = self.probabilistic_policy_statement()
                localctx.subpolicies.append(localctx._probabilistic_policy_statement)
                self.state = 318
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Probabilistic_policy_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RLangParser.RULE_probabilistic_policy_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Probabilistic_policy_statement_sugarContext(Probabilistic_policy_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Probabilistic_policy_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def execute(self):
            return self.getTypedRuleContext(RLangParser.ExecuteContext,0)

        def probabilistic_condition(self):
            return self.getTypedRuleContext(RLangParser.Probabilistic_conditionContext,0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.NL)
            else:
                return self.getToken(RLangParser.NL, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProbabilistic_policy_statement_sugar" ):
                listener.enterProbabilistic_policy_statement_sugar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProbabilistic_policy_statement_sugar" ):
                listener.exitProbabilistic_policy_statement_sugar(self)


    class Probabilistic_policy_statement_no_sugarContext(Probabilistic_policy_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Probabilistic_policy_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def probabilistic_condition(self):
            return self.getTypedRuleContext(RLangParser.Probabilistic_conditionContext,0)

        def COL(self):
            return self.getToken(RLangParser.COL, 0)
        def INDENT(self):
            return self.getToken(RLangParser.INDENT, 0)
        def non_negative_policy_statement_collection(self):
            return self.getTypedRuleContext(RLangParser.Non_negative_policy_statement_collectionContext,0)

        def DEDENT(self):
            return self.getToken(RLangParser.DEDENT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProbabilistic_policy_statement_no_sugar" ):
                listener.enterProbabilistic_policy_statement_no_sugar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProbabilistic_policy_statement_no_sugar" ):
                listener.exitProbabilistic_policy_statement_no_sugar(self)



    def probabilistic_policy_statement(self):

        localctx = RLangParser.Probabilistic_policy_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_probabilistic_policy_statement)
        try:
            self.state = 332
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.WITH]:
                localctx = RLangParser.Probabilistic_policy_statement_no_sugarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.probabilistic_condition()
                self.state = 320
                self.match(RLangParser.COL)
                self.state = 321
                self.match(RLangParser.INDENT)
                self.state = 322
                self.non_negative_policy_statement_collection()
                self.state = 323
                self.match(RLangParser.DEDENT)
                pass
            elif token in [RLangParser.EXECUTE]:
                localctx = RLangParser.Probabilistic_policy_statement_sugarContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.execute()
                self.state = 326
                self.probabilistic_condition()
                self.state = 328 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 327
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 330 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Probabilistic_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WITH(self):
            return self.getToken(RLangParser.WITH, 0)

        def P(self):
            return self.getToken(RLangParser.P, 0)

        def L_PAR(self):
            return self.getToken(RLangParser.L_PAR, 0)

        def R_PAR(self):
            return self.getToken(RLangParser.R_PAR, 0)

        def any_number(self):
            return self.getTypedRuleContext(RLangParser.Any_numberContext,0)


        def integer_fraction(self):
            return self.getTypedRuleContext(RLangParser.Integer_fractionContext,0)


        def getRuleIndex(self):
            return RLangParser.RULE_probabilistic_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProbabilistic_condition" ):
                listener.enterProbabilistic_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProbabilistic_condition" ):
                listener.exitProbabilistic_condition(self)




    def probabilistic_condition(self):

        localctx = RLangParser.Probabilistic_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_probabilistic_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(RLangParser.WITH)
            self.state = 335
            self.match(RLangParser.P)
            self.state = 336
            self.match(RLangParser.L_PAR)
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 337
                self.any_number()
                pass

            elif la_ == 2:
                self.state = 338
                self.integer_fraction()
                pass


            self.state = 341
            self.match(RLangParser.R_PAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EffectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._effect_stat = None # Effect_statContext
            self.stats = list() # of Effect_statContexts

        def EFFECT(self):
            return self.getToken(RLangParser.EFFECT, 0)

        def COL(self):
            return self.getToken(RLangParser.COL, 0)

        def INDENT(self):
            return self.getToken(RLangParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(RLangParser.DEDENT, 0)

        def IDENTIFIER(self):
            return self.getToken(RLangParser.IDENTIFIER, 0)

        def effect_stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Effect_statContext)
            else:
                return self.getTypedRuleContext(RLangParser.Effect_statContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.NL)
            else:
                return self.getToken(RLangParser.NL, i)

        def getRuleIndex(self):
            return RLangParser.RULE_effect

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEffect" ):
                listener.enterEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEffect" ):
                listener.exitEffect(self)




    def effect(self):

        localctx = RLangParser.EffectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_effect)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(RLangParser.EFFECT)
            self.state = 345
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.IDENTIFIER:
                self.state = 344
                self.match(RLangParser.IDENTIFIER)


            self.state = 347
            self.match(RLangParser.COL)
            self.state = 348
            self.match(RLangParser.INDENT)
            self.state = 356 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 349
                localctx._effect_stat = self.effect_stat()
                localctx.stats.append(localctx._effect_stat)
                self.state = 353
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.NL:
                    self.state = 350
                    self.match(RLangParser.NL)
                    self.state = 355
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 358 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RLangParser.REWARD) | (1 << RLangParser.S_PRIME) | (1 << RLangParser.IF) | (1 << RLangParser.WITH) | (1 << RLangParser.PREDICT) | (1 << RLangParser.IDENTIFIER))) != 0)):
                    break

            self.state = 360
            self.match(RLangParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Effect_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RLangParser.RULE_effect_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Effect_stat_stochastic_effectContext(Effect_statContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Effect_statContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def stochastic_effect(self):
            return self.getTypedRuleContext(RLangParser.Stochastic_effectContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEffect_stat_stochastic_effect" ):
                listener.enterEffect_stat_stochastic_effect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEffect_stat_stochastic_effect" ):
                listener.exitEffect_stat_stochastic_effect(self)


    class Effect_stat_rewardContext(Effect_statContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Effect_statContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def reward(self):
            return self.getTypedRuleContext(RLangParser.RewardContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEffect_stat_reward" ):
                listener.enterEffect_stat_reward(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEffect_stat_reward" ):
                listener.exitEffect_stat_reward(self)


    class Effect_stat_predictionContext(Effect_statContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Effect_statContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def prediction(self):
            return self.getTypedRuleContext(RLangParser.PredictionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEffect_stat_prediction" ):
                listener.enterEffect_stat_prediction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEffect_stat_prediction" ):
                listener.exitEffect_stat_prediction(self)


    class Effect_stat_conditionalContext(Effect_statContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Effect_statContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def conditional_effect_stat(self):
            return self.getTypedRuleContext(RLangParser.Conditional_effect_statContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEffect_stat_conditional" ):
                listener.enterEffect_stat_conditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEffect_stat_conditional" ):
                listener.exitEffect_stat_conditional(self)


    class Effect_stat_effect_referenceContext(Effect_statContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Effect_statContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def effect_reference(self):
            return self.getTypedRuleContext(RLangParser.Effect_referenceContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEffect_stat_effect_reference" ):
                listener.enterEffect_stat_effect_reference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEffect_stat_effect_reference" ):
                listener.exitEffect_stat_effect_reference(self)



    def effect_stat(self):

        localctx = RLangParser.Effect_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_effect_stat)
        try:
            self.state = 367
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.REWARD]:
                localctx = RLangParser.Effect_stat_rewardContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.reward()
                pass
            elif token in [RLangParser.S_PRIME, RLangParser.IDENTIFIER]:
                localctx = RLangParser.Effect_stat_predictionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 363
                self.prediction()
                pass
            elif token in [RLangParser.PREDICT]:
                localctx = RLangParser.Effect_stat_effect_referenceContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 364
                self.effect_reference()
                pass
            elif token in [RLangParser.WITH]:
                localctx = RLangParser.Effect_stat_stochastic_effectContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 365
                self.stochastic_effect()
                pass
            elif token in [RLangParser.IF]:
                localctx = RLangParser.Effect_stat_conditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 366
                self.conditional_effect_stat()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RewardContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REWARD(self):
            return self.getToken(RLangParser.REWARD, 0)

        def arithmetic_exp(self):
            return self.getTypedRuleContext(RLangParser.Arithmetic_expContext,0)


        def getRuleIndex(self):
            return RLangParser.RULE_reward

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReward" ):
                listener.enterReward(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReward" ):
                listener.exitReward(self)




    def reward(self):

        localctx = RLangParser.RewardContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_reward)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.match(RLangParser.REWARD)
            self.state = 370
            self.arithmetic_exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PredictionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREDICT(self):
            return self.getToken(RLangParser.PREDICT, 0)

        def arithmetic_exp(self):
            return self.getTypedRuleContext(RLangParser.Arithmetic_expContext,0)


        def IDENTIFIER(self):
            return self.getToken(RLangParser.IDENTIFIER, 0)

        def S_PRIME(self):
            return self.getToken(RLangParser.S_PRIME, 0)

        def PRIME(self):
            return self.getToken(RLangParser.PRIME, 0)

        def getRuleIndex(self):
            return RLangParser.RULE_prediction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrediction" ):
                listener.enterPrediction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrediction" ):
                listener.exitPrediction(self)




    def prediction(self):

        localctx = RLangParser.PredictionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_prediction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.IDENTIFIER]:
                self.state = 372
                self.match(RLangParser.IDENTIFIER)
                self.state = 374
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==RLangParser.PRIME:
                    self.state = 373
                    self.match(RLangParser.PRIME)


                pass
            elif token in [RLangParser.S_PRIME]:
                self.state = 376
                self.match(RLangParser.S_PRIME)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 379
            self.match(RLangParser.PREDICT)
            self.state = 380
            self.arithmetic_exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Effect_referenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREDICT(self):
            return self.getToken(RLangParser.PREDICT, 0)

        def IDENTIFIER(self):
            return self.getToken(RLangParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return RLangParser.RULE_effect_reference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEffect_reference" ):
                listener.enterEffect_reference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEffect_reference" ):
                listener.exitEffect_reference(self)




    def effect_reference(self):

        localctx = RLangParser.Effect_referenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_effect_reference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(RLangParser.PREDICT)
            self.state = 383
            self.match(RLangParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stochastic_effectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._effect_stat = None # Effect_statContext
            self.stats = list() # of Effect_statContexts

        def WITH(self):
            return self.getToken(RLangParser.WITH, 0)

        def P(self):
            return self.getToken(RLangParser.P, 0)

        def L_PAR(self):
            return self.getToken(RLangParser.L_PAR, 0)

        def any_number(self):
            return self.getTypedRuleContext(RLangParser.Any_numberContext,0)


        def R_PAR(self):
            return self.getToken(RLangParser.R_PAR, 0)

        def COL(self):
            return self.getToken(RLangParser.COL, 0)

        def INDENT(self):
            return self.getToken(RLangParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(RLangParser.DEDENT, 0)

        def effect_stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Effect_statContext)
            else:
                return self.getTypedRuleContext(RLangParser.Effect_statContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.NL)
            else:
                return self.getToken(RLangParser.NL, i)

        def getRuleIndex(self):
            return RLangParser.RULE_stochastic_effect

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStochastic_effect" ):
                listener.enterStochastic_effect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStochastic_effect" ):
                listener.exitStochastic_effect(self)




    def stochastic_effect(self):

        localctx = RLangParser.Stochastic_effectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_stochastic_effect)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(RLangParser.WITH)
            self.state = 386
            self.match(RLangParser.P)
            self.state = 387
            self.match(RLangParser.L_PAR)
            self.state = 388
            self.any_number()
            self.state = 389
            self.match(RLangParser.R_PAR)
            self.state = 390
            self.match(RLangParser.COL)
            self.state = 391
            self.match(RLangParser.INDENT)
            self.state = 399 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 392
                localctx._effect_stat = self.effect_stat()
                localctx.stats.append(localctx._effect_stat)
                self.state = 396
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.NL:
                    self.state = 393
                    self.match(RLangParser.NL)
                    self.state = 398
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 401 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RLangParser.REWARD) | (1 << RLangParser.S_PRIME) | (1 << RLangParser.IF) | (1 << RLangParser.WITH) | (1 << RLangParser.PREDICT) | (1 << RLangParser.IDENTIFIER))) != 0)):
                    break

            self.state = 403
            self.match(RLangParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conditional_effect_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.if_condition = None # Boolean_expContext
            self._effect_stat = None # Effect_statContext
            self.if_statements = list() # of Effect_statContexts
            self.elif_condition = None # Boolean_expContext
            self.elif_statements = list() # of Effect_statContexts
            self.else_statements = list() # of Effect_statContexts

        def IF(self):
            return self.getToken(RLangParser.IF, 0)

        def COL(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.COL)
            else:
                return self.getToken(RLangParser.COL, i)

        def INDENT(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.INDENT)
            else:
                return self.getToken(RLangParser.INDENT, i)

        def DEDENT(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.DEDENT)
            else:
                return self.getToken(RLangParser.DEDENT, i)

        def boolean_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Boolean_expContext)
            else:
                return self.getTypedRuleContext(RLangParser.Boolean_expContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.ELIF)
            else:
                return self.getToken(RLangParser.ELIF, i)

        def ELSE(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.ELSE)
            else:
                return self.getToken(RLangParser.ELSE, i)

        def effect_stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Effect_statContext)
            else:
                return self.getTypedRuleContext(RLangParser.Effect_statContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.NL)
            else:
                return self.getToken(RLangParser.NL, i)

        def getRuleIndex(self):
            return RLangParser.RULE_conditional_effect_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional_effect_stat" ):
                listener.enterConditional_effect_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional_effect_stat" ):
                listener.exitConditional_effect_stat(self)




    def conditional_effect_stat(self):

        localctx = RLangParser.Conditional_effect_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_conditional_effect_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(RLangParser.IF)
            self.state = 406
            localctx.if_condition = self.boolean_exp(0)
            self.state = 407
            self.match(RLangParser.COL)
            self.state = 408
            self.match(RLangParser.INDENT)
            self.state = 416 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 409
                localctx._effect_stat = self.effect_stat()
                localctx.if_statements.append(localctx._effect_stat)
                self.state = 413
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.NL:
                    self.state = 410
                    self.match(RLangParser.NL)
                    self.state = 415
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 418 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RLangParser.REWARD) | (1 << RLangParser.S_PRIME) | (1 << RLangParser.IF) | (1 << RLangParser.WITH) | (1 << RLangParser.PREDICT) | (1 << RLangParser.IDENTIFIER))) != 0)):
                    break

            self.state = 420
            self.match(RLangParser.DEDENT)
            self.state = 440
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.ELIF:
                self.state = 421
                self.match(RLangParser.ELIF)
                self.state = 422
                localctx.elif_condition = self.boolean_exp(0)
                self.state = 423
                self.match(RLangParser.COL)
                self.state = 424
                self.match(RLangParser.INDENT)
                self.state = 432 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 425
                    localctx._effect_stat = self.effect_stat()
                    localctx.elif_statements.append(localctx._effect_stat)
                    self.state = 429
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==RLangParser.NL:
                        self.state = 426
                        self.match(RLangParser.NL)
                        self.state = 431
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 434 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RLangParser.REWARD) | (1 << RLangParser.S_PRIME) | (1 << RLangParser.IF) | (1 << RLangParser.WITH) | (1 << RLangParser.PREDICT) | (1 << RLangParser.IDENTIFIER))) != 0)):
                        break

                self.state = 436
                self.match(RLangParser.DEDENT)
                self.state = 442
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 461
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.ELSE:
                self.state = 443
                self.match(RLangParser.ELSE)
                self.state = 444
                self.match(RLangParser.COL)
                self.state = 445
                self.match(RLangParser.INDENT)
                self.state = 453 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 446
                    localctx._effect_stat = self.effect_stat()
                    localctx.else_statements.append(localctx._effect_stat)
                    self.state = 450
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==RLangParser.NL:
                        self.state = 447
                        self.match(RLangParser.NL)
                        self.state = 452
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 455 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RLangParser.REWARD) | (1 << RLangParser.S_PRIME) | (1 << RLangParser.IF) | (1 << RLangParser.WITH) | (1 << RLangParser.PREDICT) | (1 << RLangParser.IDENTIFIER))) != 0)):
                        break

                self.state = 457
                self.match(RLangParser.DEDENT)
                self.state = 463
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arithmetic_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RLangParser.RULE_arithmetic_exp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Arith_numberContext(Arithmetic_expContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Arithmetic_expContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def any_number(self):
            return self.getTypedRuleContext(RLangParser.Any_numberContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArith_number" ):
                listener.enterArith_number(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArith_number" ):
                listener.exitArith_number(self)


    class Arith_arrayContext(Arithmetic_expContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Arithmetic_expContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def any_array(self):
            return self.getTypedRuleContext(RLangParser.Any_arrayContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArith_array" ):
                listener.enterArith_array(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArith_array" ):
                listener.exitArith_array(self)


    class Arith_plus_minusContext(Arithmetic_expContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Arithmetic_expContext
            super().__init__(parser)
            self.lhs = None # Arithmetic_expContext
            self.rhs = None # Arithmetic_expContext
            self.copyFrom(ctx)

        def arithmetic_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Arithmetic_expContext)
            else:
                return self.getTypedRuleContext(RLangParser.Arithmetic_expContext,i)

        def PLUS(self):
            return self.getToken(RLangParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(RLangParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArith_plus_minus" ):
                listener.enterArith_plus_minus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArith_plus_minus" ):
                listener.exitArith_plus_minus(self)


    class Arith_parenContext(Arithmetic_expContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Arithmetic_expContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def L_PAR(self):
            return self.getToken(RLangParser.L_PAR, 0)
        def arithmetic_exp(self):
            return self.getTypedRuleContext(RLangParser.Arithmetic_expContext,0)

        def R_PAR(self):
            return self.getToken(RLangParser.R_PAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArith_paren" ):
                listener.enterArith_paren(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArith_paren" ):
                listener.exitArith_paren(self)


    class Arith_times_divideContext(Arithmetic_expContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Arithmetic_expContext
            super().__init__(parser)
            self.lhs = None # Arithmetic_expContext
            self.rhs = None # Arithmetic_expContext
            self.copyFrom(ctx)

        def arithmetic_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Arithmetic_expContext)
            else:
                return self.getTypedRuleContext(RLangParser.Arithmetic_expContext,i)

        def TIMES(self):
            return self.getToken(RLangParser.TIMES, 0)
        def DIVIDE(self):
            return self.getToken(RLangParser.DIVIDE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArith_times_divide" ):
                listener.enterArith_times_divide(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArith_times_divide" ):
                listener.exitArith_times_divide(self)


    class Arith_bound_varContext(Arithmetic_expContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Arithmetic_expContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def any_bound_var(self):
            return self.getTypedRuleContext(RLangParser.Any_bound_varContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArith_bound_var" ):
                listener.enterArith_bound_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArith_bound_var" ):
                listener.exitArith_bound_var(self)



    def arithmetic_exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RLangParser.Arithmetic_expContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_arithmetic_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.L_PAR]:
                localctx = RLangParser.Arith_parenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 465
                self.match(RLangParser.L_PAR)
                self.state = 466
                self.arithmetic_exp(0)
                self.state = 467
                self.match(RLangParser.R_PAR)
                pass
            elif token in [RLangParser.MINUS, RLangParser.DECIMAL, RLangParser.INTEGER]:
                localctx = RLangParser.Arith_numberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 469
                self.any_number()
                pass
            elif token in [RLangParser.L_BRK]:
                localctx = RLangParser.Arith_arrayContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 470
                self.any_array()
                pass
            elif token in [RLangParser.S_PRIME, RLangParser.S, RLangParser.A, RLangParser.IDENTIFIER]:
                localctx = RLangParser.Arith_bound_varContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 471
                self.any_bound_var()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 482
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,49,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 480
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
                    if la_ == 1:
                        localctx = RLangParser.Arith_times_divideContext(self, RLangParser.Arithmetic_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_exp)
                        self.state = 474
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 475
                        _la = self._input.LA(1)
                        if not(_la==RLangParser.TIMES or _la==RLangParser.DIVIDE):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 476
                        localctx.rhs = self.arithmetic_exp(6)
                        pass

                    elif la_ == 2:
                        localctx = RLangParser.Arith_plus_minusContext(self, RLangParser.Arithmetic_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_exp)
                        self.state = 477
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 478
                        _la = self._input.LA(1)
                        if not(_la==RLangParser.PLUS or _la==RLangParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 479
                        localctx.rhs = self.arithmetic_exp(5)
                        pass

             
                self.state = 484
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,49,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Boolean_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RLangParser.RULE_boolean_exp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Bool_bool_eqContext(Boolean_expContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Boolean_expContext
            super().__init__(parser)
            self.lhs = None # Boolean_expContext
            self.rhs = None # Boolean_expContext
            self.copyFrom(ctx)

        def boolean_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Boolean_expContext)
            else:
                return self.getTypedRuleContext(RLangParser.Boolean_expContext,i)

        def EQ_TO(self):
            return self.getToken(RLangParser.EQ_TO, 0)
        def NOT_EQ(self):
            return self.getToken(RLangParser.NOT_EQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_bool_eq" ):
                listener.enterBool_bool_eq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_bool_eq" ):
                listener.exitBool_bool_eq(self)


    class Bool_notContext(Boolean_expContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Boolean_expContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(RLangParser.NOT, 0)
        def boolean_exp(self):
            return self.getTypedRuleContext(RLangParser.Boolean_expContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_not" ):
                listener.enterBool_not(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_not" ):
                listener.exitBool_not(self)


    class Bool_inContext(Boolean_expContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Boolean_expContext
            super().__init__(parser)
            self.lhs = None # Arithmetic_expContext
            self.rhs = None # Arithmetic_expContext
            self.copyFrom(ctx)

        def IN(self):
            return self.getToken(RLangParser.IN, 0)
        def arithmetic_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Arithmetic_expContext)
            else:
                return self.getTypedRuleContext(RLangParser.Arithmetic_expContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_in" ):
                listener.enterBool_in(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_in" ):
                listener.exitBool_in(self)


    class Bool_orContext(Boolean_expContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Boolean_expContext
            super().__init__(parser)
            self.lhs = None # Boolean_expContext
            self.rhs = None # Boolean_expContext
            self.copyFrom(ctx)

        def OR(self):
            return self.getToken(RLangParser.OR, 0)
        def boolean_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Boolean_expContext)
            else:
                return self.getTypedRuleContext(RLangParser.Boolean_expContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_or" ):
                listener.enterBool_or(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_or" ):
                listener.exitBool_or(self)


    class Bool_parenContext(Boolean_expContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Boolean_expContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def L_PAR(self):
            return self.getToken(RLangParser.L_PAR, 0)
        def boolean_exp(self):
            return self.getTypedRuleContext(RLangParser.Boolean_expContext,0)

        def R_PAR(self):
            return self.getToken(RLangParser.R_PAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_paren" ):
                listener.enterBool_paren(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_paren" ):
                listener.exitBool_paren(self)


    class Bool_arith_eqContext(Boolean_expContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Boolean_expContext
            super().__init__(parser)
            self.lhs = None # Arithmetic_expContext
            self.rhs = None # Arithmetic_expContext
            self.copyFrom(ctx)

        def arithmetic_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Arithmetic_expContext)
            else:
                return self.getTypedRuleContext(RLangParser.Arithmetic_expContext,i)

        def EQ_TO(self):
            return self.getToken(RLangParser.EQ_TO, 0)
        def LT(self):
            return self.getToken(RLangParser.LT, 0)
        def GT(self):
            return self.getToken(RLangParser.GT, 0)
        def LT_EQ(self):
            return self.getToken(RLangParser.LT_EQ, 0)
        def GT_EQ(self):
            return self.getToken(RLangParser.GT_EQ, 0)
        def NOT_EQ(self):
            return self.getToken(RLangParser.NOT_EQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_arith_eq" ):
                listener.enterBool_arith_eq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_arith_eq" ):
                listener.exitBool_arith_eq(self)


    class Bool_bound_varContext(Boolean_expContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Boolean_expContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def any_bound_var(self):
            return self.getTypedRuleContext(RLangParser.Any_bound_varContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_bound_var" ):
                listener.enterBool_bound_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_bound_var" ):
                listener.exitBool_bound_var(self)


    class Bool_tfContext(Boolean_expContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Boolean_expContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(RLangParser.TRUE, 0)
        def FALSE(self):
            return self.getToken(RLangParser.FALSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_tf" ):
                listener.enterBool_tf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_tf" ):
                listener.exitBool_tf(self)


    class Bool_andContext(Boolean_expContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Boolean_expContext
            super().__init__(parser)
            self.lhs = None # Boolean_expContext
            self.rhs = None # Boolean_expContext
            self.copyFrom(ctx)

        def AND(self):
            return self.getToken(RLangParser.AND, 0)
        def boolean_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Boolean_expContext)
            else:
                return self.getTypedRuleContext(RLangParser.Boolean_expContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_and" ):
                listener.enterBool_and(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_and" ):
                listener.exitBool_and(self)



    def boolean_exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RLangParser.Boolean_expContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_boolean_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Bool_parenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 486
                self.match(RLangParser.L_PAR)
                self.state = 487
                self.boolean_exp(0)
                self.state = 488
                self.match(RLangParser.R_PAR)
                pass

            elif la_ == 2:
                localctx = RLangParser.Bool_notContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 490
                self.match(RLangParser.NOT)
                self.state = 491
                self.boolean_exp(6)
                pass

            elif la_ == 3:
                localctx = RLangParser.Bool_inContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 492
                localctx.lhs = self.arithmetic_exp(0)
                self.state = 493
                self.match(RLangParser.IN)
                self.state = 494
                localctx.rhs = self.arithmetic_exp(0)
                pass

            elif la_ == 4:
                localctx = RLangParser.Bool_arith_eqContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 496
                localctx.lhs = self.arithmetic_exp(0)
                self.state = 497
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RLangParser.EQ_TO) | (1 << RLangParser.GT_EQ) | (1 << RLangParser.LT_EQ) | (1 << RLangParser.NOT_EQ) | (1 << RLangParser.LT) | (1 << RLangParser.GT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 498
                localctx.rhs = self.arithmetic_exp(0)
                pass

            elif la_ == 5:
                localctx = RLangParser.Bool_bound_varContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 500
                self.any_bound_var()
                pass

            elif la_ == 6:
                localctx = RLangParser.Bool_tfContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 501
                _la = self._input.LA(1)
                if not(_la==RLangParser.TRUE or _la==RLangParser.FALSE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 515
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 513
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                    if la_ == 1:
                        localctx = RLangParser.Bool_andContext(self, RLangParser.Boolean_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_exp)
                        self.state = 504
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 505
                        self.match(RLangParser.AND)
                        self.state = 506
                        localctx.rhs = self.boolean_exp(9)
                        pass

                    elif la_ == 2:
                        localctx = RLangParser.Bool_orContext(self, RLangParser.Boolean_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_exp)
                        self.state = 507
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 508
                        self.match(RLangParser.OR)
                        self.state = 509
                        localctx.rhs = self.boolean_exp(8)
                        pass

                    elif la_ == 3:
                        localctx = RLangParser.Bool_bool_eqContext(self, RLangParser.Boolean_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_exp)
                        self.state = 510
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 511
                        _la = self._input.LA(1)
                        if not(_la==RLangParser.EQ_TO or _la==RLangParser.NOT_EQ):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 512
                        localctx.rhs = self.boolean_exp(5)
                        pass

             
                self.state = 517
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Any_bound_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RLangParser.RULE_any_bound_var

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Bound_stateContext(Any_bound_varContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Any_bound_varContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def S(self):
            return self.getToken(RLangParser.S, 0)
        def trailer(self):
            return self.getTypedRuleContext(RLangParser.TrailerContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBound_state" ):
                listener.enterBound_state(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBound_state" ):
                listener.exitBound_state(self)


    class Bound_identifierContext(Any_bound_varContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Any_bound_varContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(RLangParser.IDENTIFIER, 0)
        def PRIME(self):
            return self.getToken(RLangParser.PRIME, 0)
        def trailer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.TrailerContext)
            else:
                return self.getTypedRuleContext(RLangParser.TrailerContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBound_identifier" ):
                listener.enterBound_identifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBound_identifier" ):
                listener.exitBound_identifier(self)


    class Bound_next_stateContext(Any_bound_varContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Any_bound_varContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def S_PRIME(self):
            return self.getToken(RLangParser.S_PRIME, 0)
        def trailer(self):
            return self.getTypedRuleContext(RLangParser.TrailerContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBound_next_state" ):
                listener.enterBound_next_state(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBound_next_state" ):
                listener.exitBound_next_state(self)


    class Bound_actionContext(Any_bound_varContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Any_bound_varContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def A(self):
            return self.getToken(RLangParser.A, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBound_action" ):
                listener.enterBound_action(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBound_action" ):
                listener.exitBound_action(self)



    def any_bound_var(self):

        localctx = RLangParser.Any_bound_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_any_bound_var)
        try:
            self.state = 537
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.IDENTIFIER]:
                localctx = RLangParser.Bound_identifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 518
                self.match(RLangParser.IDENTIFIER)
                self.state = 520
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
                if la_ == 1:
                    self.state = 519
                    self.match(RLangParser.PRIME)


                self.state = 525
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,54,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 522
                        self.trailer() 
                    self.state = 527
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,54,self._ctx)

                pass
            elif token in [RLangParser.S]:
                localctx = RLangParser.Bound_stateContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 528
                self.match(RLangParser.S)
                self.state = 530
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
                if la_ == 1:
                    self.state = 529
                    self.trailer()


                pass
            elif token in [RLangParser.S_PRIME]:
                localctx = RLangParser.Bound_next_stateContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 532
                self.match(RLangParser.S_PRIME)
                self.state = 534
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
                if la_ == 1:
                    self.state = 533
                    self.trailer()


                pass
            elif token in [RLangParser.A]:
                localctx = RLangParser.Bound_actionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 536
                self.match(RLangParser.A)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TrailerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RLangParser.RULE_trailer

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Trailer_sliceContext(TrailerContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.TrailerContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def slice_exp(self):
            return self.getTypedRuleContext(RLangParser.Slice_expContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrailer_slice" ):
                listener.enterTrailer_slice(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrailer_slice" ):
                listener.exitTrailer_slice(self)


    class Trailer_arrayContext(TrailerContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.TrailerContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def int_array_exp(self):
            return self.getTypedRuleContext(RLangParser.Int_array_expContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrailer_array" ):
                listener.enterTrailer_array(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrailer_array" ):
                listener.exitTrailer_array(self)



    def trailer(self):

        localctx = RLangParser.TrailerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_trailer)
        try:
            self.state = 541
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Trailer_arrayContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 539
                self.int_array_exp()
                pass

            elif la_ == 2:
                localctx = RLangParser.Trailer_sliceContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 540
                self.slice_exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Any_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RLangParser.RULE_any_array

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Any_array_any_numContext(Any_arrayContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Any_arrayContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def any_num_array_exp(self):
            return self.getTypedRuleContext(RLangParser.Any_num_array_expContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAny_array_any_num" ):
                listener.enterAny_array_any_num(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAny_array_any_num" ):
                listener.exitAny_array_any_num(self)


    class Any_array_compoundContext(Any_arrayContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Any_arrayContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def compound_array_exp(self):
            return self.getTypedRuleContext(RLangParser.Compound_array_expContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAny_array_compound" ):
                listener.enterAny_array_compound(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAny_array_compound" ):
                listener.exitAny_array_compound(self)



    def any_array(self):

        localctx = RLangParser.Any_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_any_array)
        try:
            self.state = 545
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Any_array_compoundContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 543
                self.compound_array_exp()
                pass

            elif la_ == 2:
                localctx = RLangParser.Any_array_any_numContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 544
                self.any_num_array_exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compound_array_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RLangParser.RULE_compound_array_exp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Compound_array_simpleContext(Compound_array_expContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Compound_array_expContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def any_num_array_exp(self):
            return self.getTypedRuleContext(RLangParser.Any_num_array_expContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompound_array_simple" ):
                listener.enterCompound_array_simple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompound_array_simple" ):
                listener.exitCompound_array_simple(self)


    class Compound_array_compoundContext(Compound_array_expContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Compound_array_expContext
            super().__init__(parser)
            self._compound_array_exp = None # Compound_array_expContext
            self.arr = list() # of Compound_array_expContexts
            self.copyFrom(ctx)

        def L_BRK(self):
            return self.getToken(RLangParser.L_BRK, 0)
        def R_BRK(self):
            return self.getToken(RLangParser.R_BRK, 0)
        def compound_array_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Compound_array_expContext)
            else:
                return self.getTypedRuleContext(RLangParser.Compound_array_expContext,i)

        def COM(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.COM)
            else:
                return self.getToken(RLangParser.COM, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompound_array_compound" ):
                listener.enterCompound_array_compound(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompound_array_compound" ):
                listener.exitCompound_array_compound(self)



    def compound_array_exp(self):

        localctx = RLangParser.Compound_array_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_compound_array_exp)
        self._la = 0 # Token type
        try:
            self.state = 559
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Compound_array_simpleContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 547
                self.any_num_array_exp()
                pass

            elif la_ == 2:
                localctx = RLangParser.Compound_array_compoundContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 548
                self.match(RLangParser.L_BRK)
                self.state = 549
                localctx._compound_array_exp = self.compound_array_exp()
                localctx.arr.append(localctx._compound_array_exp)
                self.state = 554
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.COM:
                    self.state = 550
                    self.match(RLangParser.COM)
                    self.state = 551
                    localctx._compound_array_exp = self.compound_array_exp()
                    localctx.arr.append(localctx._compound_array_exp)
                    self.state = 556
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 557
                self.match(RLangParser.R_BRK)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_array_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._any_integer = None # Any_integerContext
            self.arr = list() # of Any_integerContexts

        def L_BRK(self):
            return self.getToken(RLangParser.L_BRK, 0)

        def R_BRK(self):
            return self.getToken(RLangParser.R_BRK, 0)

        def any_integer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Any_integerContext)
            else:
                return self.getTypedRuleContext(RLangParser.Any_integerContext,i)


        def COM(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.COM)
            else:
                return self.getToken(RLangParser.COM, i)

        def getRuleIndex(self):
            return RLangParser.RULE_int_array_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt_array_exp" ):
                listener.enterInt_array_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt_array_exp" ):
                listener.exitInt_array_exp(self)




    def int_array_exp(self):

        localctx = RLangParser.Int_array_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_int_array_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 561
            self.match(RLangParser.L_BRK)
            self.state = 562
            localctx._any_integer = self.any_integer()
            localctx.arr.append(localctx._any_integer)
            self.state = 567
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.COM:
                self.state = 563
                self.match(RLangParser.COM)
                self.state = 564
                localctx._any_integer = self.any_integer()
                localctx.arr.append(localctx._any_integer)
                self.state = 569
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 570
            self.match(RLangParser.R_BRK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Any_num_array_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._any_number = None # Any_numberContext
            self.arr = list() # of Any_numberContexts

        def L_BRK(self):
            return self.getToken(RLangParser.L_BRK, 0)

        def R_BRK(self):
            return self.getToken(RLangParser.R_BRK, 0)

        def any_number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Any_numberContext)
            else:
                return self.getTypedRuleContext(RLangParser.Any_numberContext,i)


        def COM(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.COM)
            else:
                return self.getToken(RLangParser.COM, i)

        def getRuleIndex(self):
            return RLangParser.RULE_any_num_array_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAny_num_array_exp" ):
                listener.enterAny_num_array_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAny_num_array_exp" ):
                listener.exitAny_num_array_exp(self)




    def any_num_array_exp(self):

        localctx = RLangParser.Any_num_array_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_any_num_array_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 572
            self.match(RLangParser.L_BRK)
            self.state = 573
            localctx._any_number = self.any_number()
            localctx.arr.append(localctx._any_number)
            self.state = 578
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.COM:
                self.state = 574
                self.match(RLangParser.COM)
                self.state = 575
                localctx._any_number = self.any_number()
                localctx.arr.append(localctx._any_number)
                self.state = 580
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 581
            self.match(RLangParser.R_BRK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Slice_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.start_ind = None # Any_integerContext
            self.stop_ind = None # Any_integerContext

        def L_BRK(self):
            return self.getToken(RLangParser.L_BRK, 0)

        def COL(self):
            return self.getToken(RLangParser.COL, 0)

        def R_BRK(self):
            return self.getToken(RLangParser.R_BRK, 0)

        def any_integer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Any_integerContext)
            else:
                return self.getTypedRuleContext(RLangParser.Any_integerContext,i)


        def getRuleIndex(self):
            return RLangParser.RULE_slice_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSlice_exp" ):
                listener.enterSlice_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSlice_exp" ):
                listener.exitSlice_exp(self)




    def slice_exp(self):

        localctx = RLangParser.Slice_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_slice_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 583
            self.match(RLangParser.L_BRK)
            self.state = 585
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.MINUS or _la==RLangParser.INTEGER:
                self.state = 584
                localctx.start_ind = self.any_integer()


            self.state = 587
            self.match(RLangParser.COL)
            self.state = 589
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.MINUS or _la==RLangParser.INTEGER:
                self.state = 588
                localctx.stop_ind = self.any_integer()


            self.state = 591
            self.match(RLangParser.R_BRK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Integer_fractionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.lhs = None # Any_integerContext
            self.rhs = None # Any_integerContext

        def DIVIDE(self):
            return self.getToken(RLangParser.DIVIDE, 0)

        def any_integer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Any_integerContext)
            else:
                return self.getTypedRuleContext(RLangParser.Any_integerContext,i)


        def getRuleIndex(self):
            return RLangParser.RULE_integer_fraction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger_fraction" ):
                listener.enterInteger_fraction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger_fraction" ):
                listener.exitInteger_fraction(self)




    def integer_fraction(self):

        localctx = RLangParser.Integer_fractionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_integer_fraction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 593
            localctx.lhs = self.any_integer()
            self.state = 594
            self.match(RLangParser.DIVIDE)
            self.state = 595
            localctx.rhs = self.any_integer()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Any_numberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RLangParser.RULE_any_number

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Any_num_decContext(Any_numberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Any_numberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def any_decimal(self):
            return self.getTypedRuleContext(RLangParser.Any_decimalContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAny_num_dec" ):
                listener.enterAny_num_dec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAny_num_dec" ):
                listener.exitAny_num_dec(self)


    class Any_num_intContext(Any_numberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Any_numberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def any_integer(self):
            return self.getTypedRuleContext(RLangParser.Any_integerContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAny_num_int" ):
                listener.enterAny_num_int(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAny_num_int" ):
                listener.exitAny_num_int(self)



    def any_number(self):

        localctx = RLangParser.Any_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_any_number)
        try:
            self.state = 599
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Any_num_intContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 597
                self.any_integer()
                pass

            elif la_ == 2:
                localctx = RLangParser.Any_num_decContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 598
                self.any_decimal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Any_integerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(RLangParser.INTEGER, 0)

        def MINUS(self):
            return self.getToken(RLangParser.MINUS, 0)

        def getRuleIndex(self):
            return RLangParser.RULE_any_integer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAny_integer" ):
                listener.enterAny_integer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAny_integer" ):
                listener.exitAny_integer(self)




    def any_integer(self):

        localctx = RLangParser.Any_integerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_any_integer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 602
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.MINUS:
                self.state = 601
                self.match(RLangParser.MINUS)


            self.state = 604
            self.match(RLangParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Any_decimalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECIMAL(self):
            return self.getToken(RLangParser.DECIMAL, 0)

        def MINUS(self):
            return self.getToken(RLangParser.MINUS, 0)

        def getRuleIndex(self):
            return RLangParser.RULE_any_decimal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAny_decimal" ):
                listener.enterAny_decimal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAny_decimal" ):
                listener.exitAny_decimal(self)




    def any_decimal(self):

        localctx = RLangParser.Any_decimalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_any_decimal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 607
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.MINUS:
                self.state = 606
                self.match(RLangParser.MINUS)


            self.state = 609
            self.match(RLangParser.DECIMAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[31] = self.arithmetic_exp_sempred
        self._predicates[32] = self.boolean_exp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def arithmetic_exp_sempred(self, localctx:Arithmetic_expContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

    def boolean_exp_sempred(self, localctx:Boolean_expContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         




