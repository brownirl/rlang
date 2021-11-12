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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("\u0231\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\3\2\7\2Z\n\2\f")
        buf.write("\2\16\2]\13\2\3\2\3\2\3\2\7\2b\n\2\f\2\16\2e\13\2\3\3")
        buf.write("\3\3\6\3i\n\3\r\3\16\3j\7\3m\n\3\f\3\16\3p\13\3\3\4\3")
        buf.write("\4\3\4\3\5\7\5v\n\5\f\5\16\5y\13\5\3\6\3\6\6\6}\n\6\r")
        buf.write("\6\16\6~\3\6\3\6\6\6\u0083\n\6\r\6\16\6\u0084\3\6\3\6")
        buf.write("\6\6\u0089\n\6\r\6\16\6\u008a\3\6\3\6\6\6\u008f\n\6\r")
        buf.write("\6\16\6\u0090\3\6\3\6\6\6\u0095\n\6\r\6\16\6\u0096\3\6")
        buf.write("\3\6\6\6\u009b\n\6\r\6\16\6\u009c\3\6\3\6\6\6\u00a1\n")
        buf.write("\6\r\6\16\6\u00a2\3\6\3\6\3\6\5\6\u00a8\n\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\5\7\u00af\n\7\3\b\3\b\3\b\3\b\3\b\5\b\u00b6")
        buf.write("\n\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\7\16\u00dd\n\16\f\16\16\16\u00e0\13\16\3\16\3")
        buf.write("\16\3\17\3\17\5\17\u00e6\n\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\7\20\u00ee\n\20\f\20\16\20\u00f1\13\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\5\21\u00f8\n\21\3\22\3\22\3\22\5\22\u00fd")
        buf.write("\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\7\23\u010c\n\23\f\23\16\23\u010f\13\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u0117\n\23\3\24\3")
        buf.write("\24\3\24\7\24\u011c\n\24\f\24\16\24\u011f\13\24\3\25\3")
        buf.write("\25\3\25\3\25\3\25\6\25\u0126\n\25\r\25\16\25\u0127\3")
        buf.write("\25\3\25\3\25\3\25\3\25\6\25\u012f\n\25\r\25\16\25\u0130")
        buf.write("\5\25\u0133\n\25\3\26\3\26\5\26\u0137\n\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\27\3\27\7\27\u0140\n\27\f\27\16\27\u0143")
        buf.write("\13\27\6\27\u0145\n\27\r\27\16\27\u0146\3\30\3\30\3\30")
        buf.write("\3\30\3\30\5\30\u014e\n\30\3\31\3\31\3\31\3\32\3\32\5")
        buf.write("\32\u0155\n\32\3\32\5\32\u0158\n\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\7\34\u016d\n\34\f\34\16\34\u0170")
        buf.write("\13\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0178\n\34\3")
        buf.write("\35\3\35\3\35\7\35\u017d\n\35\f\35\16\35\u0180\13\35\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u018b")
        buf.write("\n\36\3\36\3\36\6\36\u018f\n\36\r\36\16\36\u0190\5\36")
        buf.write("\u0193\n\36\3\37\3\37\3\37\3\37\3\37\5\37\u019a\n\37\3")
        buf.write("\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \5 \u01a6\n \3 \3 \3 ")
        buf.write("\3 \3 \3 \7 \u01ae\n \f \16 \u01b1\13 \3!\3!\3!\3!\3!")
        buf.write("\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u01c4\n!\3!\3")
        buf.write("!\3!\3!\3!\3!\3!\3!\3!\7!\u01cf\n!\f!\16!\u01d2\13!\3")
        buf.write("\"\3\"\5\"\u01d6\n\"\3\"\7\"\u01d9\n\"\f\"\16\"\u01dc")
        buf.write("\13\"\3\"\3\"\5\"\u01e0\n\"\3\"\3\"\5\"\u01e4\n\"\3\"")
        buf.write("\5\"\u01e7\n\"\3#\3#\5#\u01eb\n#\3$\3$\5$\u01ef\n$\3%")
        buf.write("\3%\3%\3%\3%\7%\u01f6\n%\f%\16%\u01f9\13%\3%\3%\5%\u01fd")
        buf.write("\n%\3&\3&\3&\3&\7&\u0203\n&\f&\16&\u0206\13&\3&\3&\3\'")
        buf.write("\3\'\3\'\3\'\7\'\u020e\n\'\f\'\16\'\u0211\13\'\3\'\3\'")
        buf.write("\3(\3(\5(\u0217\n(\3(\3(\5(\u021b\n(\3(\3(\3)\3)\3)\3")
        buf.write(")\3*\3*\5*\u0225\n*\3+\5+\u0228\n+\3+\3+\3,\5,\u022d\n")
        buf.write(",\3,\3,\3,\2\4>@-\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTV\2\7\3\2;<\3\2")
        buf.write("=>\4\2/\629:\3\2%&\4\2//\62\62\2\u0258\2[\3\2\2\2\4n\3")
        buf.write("\2\2\2\6q\3\2\2\2\bw\3\2\2\2\n\u00a7\3\2\2\2\f\u00a9\3")
        buf.write("\2\2\2\16\u00b0\3\2\2\2\20\u00b7\3\2\2\2\22\u00bc\3\2")
        buf.write("\2\2\24\u00c1\3\2\2\2\26\u00c6\3\2\2\2\30\u00cb\3\2\2")
        buf.write("\2\32\u00d0\3\2\2\2\34\u00e5\3\2\2\2\36\u00e7\3\2\2\2")
        buf.write(" \u00f7\3\2\2\2\"\u00f9\3\2\2\2$\u00fe\3\2\2\2&\u0118")
        buf.write("\3\2\2\2(\u0132\3\2\2\2*\u0134\3\2\2\2,\u0144\3\2\2\2")
        buf.write(".\u014d\3\2\2\2\60\u014f\3\2\2\2\62\u0157\3\2\2\2\64\u015c")
        buf.write("\3\2\2\2\66\u015f\3\2\2\28\u0179\3\2\2\2:\u0192\3\2\2")
        buf.write("\2<\u0194\3\2\2\2>\u01a5\3\2\2\2@\u01c3\3\2\2\2B\u01e6")
        buf.write("\3\2\2\2D\u01ea\3\2\2\2F\u01ee\3\2\2\2H\u01fc\3\2\2\2")
        buf.write("J\u01fe\3\2\2\2L\u0209\3\2\2\2N\u0214\3\2\2\2P\u021e\3")
        buf.write("\2\2\2R\u0224\3\2\2\2T\u0227\3\2\2\2V\u022c\3\2\2\2XZ")
        buf.write("\7\5\2\2YX\3\2\2\2Z]\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\^\3")
        buf.write("\2\2\2][\3\2\2\2^_\5\4\3\2_c\5\b\5\2`b\7\5\2\2a`\3\2\2")
        buf.write("\2be\3\2\2\2ca\3\2\2\2cd\3\2\2\2d\3\3\2\2\2ec\3\2\2\2")
        buf.write("fh\5\6\4\2gi\7\5\2\2hg\3\2\2\2ij\3\2\2\2jh\3\2\2\2jk\3")
        buf.write("\2\2\2km\3\2\2\2lf\3\2\2\2mp\3\2\2\2nl\3\2\2\2no\3\2\2")
        buf.write("\2o\5\3\2\2\2pn\3\2\2\2qr\7\6\2\2rs\7?\2\2s\7\3\2\2\2")
        buf.write("tv\5\n\6\2ut\3\2\2\2vy\3\2\2\2wu\3\2\2\2wx\3\2\2\2x\t")
        buf.write("\3\2\2\2yw\3\2\2\2z|\5\f\7\2{}\7\5\2\2|{\3\2\2\2}~\3\2")
        buf.write("\2\2~|\3\2\2\2~\177\3\2\2\2\177\u00a8\3\2\2\2\u0080\u0082")
        buf.write("\5\16\b\2\u0081\u0083\7\5\2\2\u0082\u0081\3\2\2\2\u0083")
        buf.write("\u0084\3\2\2\2\u0084\u0082\3\2\2\2\u0084\u0085\3\2\2\2")
        buf.write("\u0085\u00a8\3\2\2\2\u0086\u0088\5\20\t\2\u0087\u0089")
        buf.write("\7\5\2\2\u0088\u0087\3\2\2\2\u0089\u008a\3\2\2\2\u008a")
        buf.write("\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u00a8\3\2\2\2")
        buf.write("\u008c\u008e\5\22\n\2\u008d\u008f\7\5\2\2\u008e\u008d")
        buf.write("\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u008e\3\2\2\2\u0090")
        buf.write("\u0091\3\2\2\2\u0091\u00a8\3\2\2\2\u0092\u0094\5\24\13")
        buf.write("\2\u0093\u0095\7\5\2\2\u0094\u0093\3\2\2\2\u0095\u0096")
        buf.write("\3\2\2\2\u0096\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097")
        buf.write("\u00a8\3\2\2\2\u0098\u009a\5\26\f\2\u0099\u009b\7\5\2")
        buf.write("\2\u009a\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009a")
        buf.write("\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u00a8\3\2\2\2\u009e")
        buf.write("\u00a0\5\30\r\2\u009f\u00a1\7\5\2\2\u00a0\u009f\3\2\2")
        buf.write("\2\u00a1\u00a2\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a3")
        buf.write("\3\2\2\2\u00a3\u00a8\3\2\2\2\u00a4\u00a8\5\32\16\2\u00a5")
        buf.write("\u00a8\5\36\20\2\u00a6\u00a8\5*\26\2\u00a7z\3\2\2\2\u00a7")
        buf.write("\u0080\3\2\2\2\u00a7\u0086\3\2\2\2\u00a7\u008c\3\2\2\2")
        buf.write("\u00a7\u0092\3\2\2\2\u00a7\u0098\3\2\2\2\u00a7\u009e\3")
        buf.write("\2\2\2\u00a7\u00a4\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7\u00a6")
        buf.write("\3\2\2\2\u00a8\13\3\2\2\2\u00a9\u00aa\7\13\2\2\u00aa\u00ab")
        buf.write("\7@\2\2\u00ab\u00ae\7(\2\2\u00ac\u00af\5> \2\u00ad\u00af")
        buf.write("\5@!\2\u00ae\u00ac\3\2\2\2\u00ae\u00ad\3\2\2\2\u00af\r")
        buf.write("\3\2\2\2\u00b0\u00b1\7\f\2\2\u00b1\u00b2\7@\2\2\u00b2")
        buf.write("\u00b5\7(\2\2\u00b3\u00b6\5R*\2\u00b4\u00b6\5L\'\2\u00b5")
        buf.write("\u00b3\3\2\2\2\u00b5\u00b4\3\2\2\2\u00b6\17\3\2\2\2\u00b7")
        buf.write("\u00b8\7\t\2\2\u00b8\u00b9\7@\2\2\u00b9\u00ba\7(\2\2\u00ba")
        buf.write("\u00bb\5B\"\2\u00bb\21\3\2\2\2\u00bc\u00bd\7\7\2\2\u00bd")
        buf.write("\u00be\7@\2\2\u00be\u00bf\7(\2\2\u00bf\u00c0\5@!\2\u00c0")
        buf.write("\23\3\2\2\2\u00c1\u00c2\7\n\2\2\u00c2\u00c3\7@\2\2\u00c3")
        buf.write("\u00c4\7(\2\2\u00c4\u00c5\5@!\2\u00c5\25\3\2\2\2\u00c6")
        buf.write("\u00c7\7\b\2\2\u00c7\u00c8\7@\2\2\u00c8\u00c9\7(\2\2\u00c9")
        buf.write("\u00ca\5> \2\u00ca\27\3\2\2\2\u00cb\u00cc\7\22\2\2\u00cc")
        buf.write("\u00cd\7@\2\2\u00cd\u00ce\7(\2\2\u00ce\u00cf\5> \2\u00cf")
        buf.write("\31\3\2\2\2\u00d0\u00d1\7\21\2\2\u00d1\u00d2\7@\2\2\u00d2")
        buf.write("\u00d3\7\63\2\2\u00d3\u00d4\7\3\2\2\u00d4\u00d5\7\35\2")
        buf.write("\2\u00d5\u00d6\5\34\17\2\u00d6\u00d7\7\3\2\2\u00d7\u00d8")
        buf.write("\5 \21\2\u00d8\u00d9\7\4\2\2\u00d9\u00da\7\36\2\2\u00da")
        buf.write("\u00de\5\34\17\2\u00db\u00dd\7\5\2\2\u00dc\u00db\3\2\2")
        buf.write("\2\u00dd\u00e0\3\2\2\2\u00de\u00dc\3\2\2\2\u00de\u00df")
        buf.write("\3\2\2\2\u00df\u00e1\3\2\2\2\u00e0\u00de\3\2\2\2\u00e1")
        buf.write("\u00e2\7\4\2\2\u00e2\33\3\2\2\2\u00e3\u00e6\5@!\2\u00e4")
        buf.write("\u00e6\7\'\2\2\u00e5\u00e3\3\2\2\2\u00e5\u00e4\3\2\2\2")
        buf.write("\u00e6\35\3\2\2\2\u00e7\u00e8\7\17\2\2\u00e8\u00e9\7@")
        buf.write("\2\2\u00e9\u00ea\7\63\2\2\u00ea\u00eb\7\3\2\2\u00eb\u00ef")
        buf.write("\5 \21\2\u00ec\u00ee\7\5\2\2\u00ed\u00ec\3\2\2\2\u00ee")
        buf.write("\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2")
        buf.write("\u00f0\u00f2\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f2\u00f3\7")
        buf.write("\4\2\2\u00f3\37\3\2\2\2\u00f4\u00f8\5\"\22\2\u00f5\u00f8")
        buf.write("\5$\23\2\u00f6\u00f8\5&\24\2\u00f7\u00f4\3\2\2\2\u00f7")
        buf.write("\u00f5\3\2\2\2\u00f7\u00f6\3\2\2\2\u00f8!\3\2\2\2\u00f9")
        buf.write("\u00fc\7\20\2\2\u00fa\u00fd\7@\2\2\u00fb\u00fd\5> \2\u00fc")
        buf.write("\u00fa\3\2\2\2\u00fc\u00fb\3\2\2\2\u00fd#\3\2\2\2\u00fe")
        buf.write("\u00ff\7\31\2\2\u00ff\u0100\5@!\2\u0100\u0101\7\63\2\2")
        buf.write("\u0101\u0102\7\3\2\2\u0102\u0103\5 \21\2\u0103\u010d\7")
        buf.write("\4\2\2\u0104\u0105\7\33\2\2\u0105\u0106\5@!\2\u0106\u0107")
        buf.write("\7\63\2\2\u0107\u0108\7\3\2\2\u0108\u0109\5 \21\2\u0109")
        buf.write("\u010a\7\4\2\2\u010a\u010c\3\2\2\2\u010b\u0104\3\2\2\2")
        buf.write("\u010c\u010f\3\2\2\2\u010d\u010b\3\2\2\2\u010d\u010e\3")
        buf.write("\2\2\2\u010e\u0116\3\2\2\2\u010f\u010d\3\2\2\2\u0110\u0111")
        buf.write("\7\32\2\2\u0111\u0112\7\63\2\2\u0112\u0113\7\3\2\2\u0113")
        buf.write("\u0114\5 \21\2\u0114\u0115\7\4\2\2\u0115\u0117\3\2\2\2")
        buf.write("\u0116\u0110\3\2\2\2\u0116\u0117\3\2\2\2\u0117%\3\2\2")
        buf.write("\2\u0118\u011d\5(\25\2\u0119\u011a\7#\2\2\u011a\u011c")
        buf.write("\5(\25\2\u011b\u0119\3\2\2\2\u011c\u011f\3\2\2\2\u011d")
        buf.write("\u011b\3\2\2\2\u011d\u011e\3\2\2\2\u011e\'\3\2\2\2\u011f")
        buf.write("\u011d\3\2\2\2\u0120\u0121\5<\37\2\u0121\u0122\7\63\2")
        buf.write("\2\u0122\u0123\7\3\2\2\u0123\u0125\5 \21\2\u0124\u0126")
        buf.write("\7\5\2\2\u0125\u0124\3\2\2\2\u0126\u0127\3\2\2\2\u0127")
        buf.write("\u0125\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u0129\3\2\2\2")
        buf.write("\u0129\u012a\7\4\2\2\u012a\u0133\3\2\2\2\u012b\u012c\5")
        buf.write("\"\22\2\u012c\u012e\5<\37\2\u012d\u012f\7\5\2\2\u012e")
        buf.write("\u012d\3\2\2\2\u012f\u0130\3\2\2\2\u0130\u012e\3\2\2\2")
        buf.write("\u0130\u0131\3\2\2\2\u0131\u0133\3\2\2\2\u0132\u0120\3")
        buf.write("\2\2\2\u0132\u012b\3\2\2\2\u0133)\3\2\2\2\u0134\u0136")
        buf.write("\7\r\2\2\u0135\u0137\7@\2\2\u0136\u0135\3\2\2\2\u0136")
        buf.write("\u0137\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u0139\7\63\2")
        buf.write("\2\u0139\u013a\7\3\2\2\u013a\u013b\5,\27\2\u013b\u013c")
        buf.write("\7\4\2\2\u013c+\3\2\2\2\u013d\u0141\5.\30\2\u013e\u0140")
        buf.write("\7\5\2\2\u013f\u013e\3\2\2\2\u0140\u0143\3\2\2\2\u0141")
        buf.write("\u013f\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0145\3\2\2\2")
        buf.write("\u0143\u0141\3\2\2\2\u0144\u013d\3\2\2\2\u0145\u0146\3")
        buf.write("\2\2\2\u0146\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147-")
        buf.write("\3\2\2\2\u0148\u014e\5\60\31\2\u0149\u014e\5\62\32\2\u014a")
        buf.write("\u014e\5\64\33\2\u014b\u014e\5\66\34\2\u014c\u014e\58")
        buf.write("\35\2\u014d\u0148\3\2\2\2\u014d\u0149\3\2\2\2\u014d\u014a")
        buf.write("\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014c\3\2\2\2\u014e")
        buf.write("/\3\2\2\2\u014f\u0150\7\16\2\2\u0150\u0151\5> \2\u0151")
        buf.write("\61\3\2\2\2\u0152\u0154\7@\2\2\u0153\u0155\7\30\2\2\u0154")
        buf.write("\u0153\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0158\3\2\2\2")
        buf.write("\u0156\u0158\7\24\2\2\u0157\u0152\3\2\2\2\u0157\u0156")
        buf.write("\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u015a\7)\2\2\u015a")
        buf.write("\u015b\5> \2\u015b\63\3\2\2\2\u015c\u015d\7)\2\2\u015d")
        buf.write("\u015e\7@\2\2\u015e\65\3\2\2\2\u015f\u0160\7\31\2\2\u0160")
        buf.write("\u0161\5@!\2\u0161\u0162\7\63\2\2\u0162\u0163\7\3\2\2")
        buf.write("\u0163\u0164\5,\27\2\u0164\u016e\7\4\2\2\u0165\u0166\7")
        buf.write("\33\2\2\u0166\u0167\5@!\2\u0167\u0168\7\63\2\2\u0168\u0169")
        buf.write("\7\3\2\2\u0169\u016a\5,\27\2\u016a\u016b\7\4\2\2\u016b")
        buf.write("\u016d\3\2\2\2\u016c\u0165\3\2\2\2\u016d\u0170\3\2\2\2")
        buf.write("\u016e\u016c\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0177\3")
        buf.write("\2\2\2\u0170\u016e\3\2\2\2\u0171\u0172\7\32\2\2\u0172")
        buf.write("\u0173\7\63\2\2\u0173\u0174\7\3\2\2\u0174\u0175\5,\27")
        buf.write("\2\u0175\u0176\7\4\2\2\u0176\u0178\3\2\2\2\u0177\u0171")
        buf.write("\3\2\2\2\u0177\u0178\3\2\2\2\u0178\67\3\2\2\2\u0179\u017e")
        buf.write("\5:\36\2\u017a\u017b\7#\2\2\u017b\u017d\5:\36\2\u017c")
        buf.write("\u017a\3\2\2\2\u017d\u0180\3\2\2\2\u017e\u017c\3\2\2\2")
        buf.write("\u017e\u017f\3\2\2\2\u017f9\3\2\2\2\u0180\u017e\3\2\2")
        buf.write("\2\u0181\u0182\5<\37\2\u0182\u0183\7\63\2\2\u0183\u0184")
        buf.write("\7\3\2\2\u0184\u0185\5,\27\2\u0185\u0186\7\4\2\2\u0186")
        buf.write("\u0193\3\2\2\2\u0187\u018b\5\60\31\2\u0188\u018b\5\62")
        buf.write("\32\2\u0189\u018b\5\64\33\2\u018a\u0187\3\2\2\2\u018a")
        buf.write("\u0188\3\2\2\2\u018a\u0189\3\2\2\2\u018b\u018c\3\2\2\2")
        buf.write("\u018c\u018e\5<\37\2\u018d\u018f\7\5\2\2\u018e\u018d\3")
        buf.write("\2\2\2\u018f\u0190\3\2\2\2\u0190\u018e\3\2\2\2\u0190\u0191")
        buf.write("\3\2\2\2\u0191\u0193\3\2\2\2\u0192\u0181\3\2\2\2\u0192")
        buf.write("\u018a\3\2\2\2\u0193;\3\2\2\2\u0194\u0195\7\37\2\2\u0195")
        buf.write("\u0196\7\27\2\2\u0196\u0199\7\67\2\2\u0197\u019a\5R*\2")
        buf.write("\u0198\u019a\5P)\2\u0199\u0197\3\2\2\2\u0199\u0198\3\2")
        buf.write("\2\2\u019a\u019b\3\2\2\2\u019b\u019c\78\2\2\u019c=\3\2")
        buf.write("\2\2\u019d\u019e\b \1\2\u019e\u019f\7\67\2\2\u019f\u01a0")
        buf.write("\5> \2\u01a0\u01a1\78\2\2\u01a1\u01a6\3\2\2\2\u01a2\u01a6")
        buf.write("\5R*\2\u01a3\u01a6\5F$\2\u01a4\u01a6\5B\"\2\u01a5\u019d")
        buf.write("\3\2\2\2\u01a5\u01a2\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5")
        buf.write("\u01a4\3\2\2\2\u01a6\u01af\3\2\2\2\u01a7\u01a8\f\7\2\2")
        buf.write("\u01a8\u01a9\t\2\2\2\u01a9\u01ae\5> \b\u01aa\u01ab\f\6")
        buf.write("\2\2\u01ab\u01ac\t\3\2\2\u01ac\u01ae\5> \7\u01ad\u01a7")
        buf.write("\3\2\2\2\u01ad\u01aa\3\2\2\2\u01ae\u01b1\3\2\2\2\u01af")
        buf.write("\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0?\3\2\2\2\u01b1")
        buf.write("\u01af\3\2\2\2\u01b2\u01b3\b!\1\2\u01b3\u01b4\7\67\2\2")
        buf.write("\u01b4\u01b5\5@!\2\u01b5\u01b6\78\2\2\u01b6\u01c4\3\2")
        buf.write("\2\2\u01b7\u01b8\7$\2\2\u01b8\u01c4\5@!\b\u01b9\u01ba")
        buf.write("\5> \2\u01ba\u01bb\7\34\2\2\u01bb\u01bc\5> \2\u01bc\u01c4")
        buf.write("\3\2\2\2\u01bd\u01be\5> \2\u01be\u01bf\t\4\2\2\u01bf\u01c0")
        buf.write("\5> \2\u01c0\u01c4\3\2\2\2\u01c1\u01c4\5B\"\2\u01c2\u01c4")
        buf.write("\t\5\2\2\u01c3\u01b2\3\2\2\2\u01c3\u01b7\3\2\2\2\u01c3")
        buf.write("\u01b9\3\2\2\2\u01c3\u01bd\3\2\2\2\u01c3\u01c1\3\2\2\2")
        buf.write("\u01c3\u01c2\3\2\2\2\u01c4\u01d0\3\2\2\2\u01c5\u01c6\f")
        buf.write("\n\2\2\u01c6\u01c7\7\"\2\2\u01c7\u01cf\5@!\13\u01c8\u01c9")
        buf.write("\f\t\2\2\u01c9\u01ca\7#\2\2\u01ca\u01cf\5@!\n\u01cb\u01cc")
        buf.write("\f\6\2\2\u01cc\u01cd\t\6\2\2\u01cd\u01cf\5@!\7\u01ce\u01c5")
        buf.write("\3\2\2\2\u01ce\u01c8\3\2\2\2\u01ce\u01cb\3\2\2\2\u01cf")
        buf.write("\u01d2\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d0\u01d1\3\2\2\2")
        buf.write("\u01d1A\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d3\u01d5\7@\2\2")
        buf.write("\u01d4\u01d6\7\30\2\2\u01d5\u01d4\3\2\2\2\u01d5\u01d6")
        buf.write("\3\2\2\2\u01d6\u01da\3\2\2\2\u01d7\u01d9\5D#\2\u01d8\u01d7")
        buf.write("\3\2\2\2\u01d9\u01dc\3\2\2\2\u01da\u01d8\3\2\2\2\u01da")
        buf.write("\u01db\3\2\2\2\u01db\u01e7\3\2\2\2\u01dc\u01da\3\2\2\2")
        buf.write("\u01dd\u01df\7\25\2\2\u01de\u01e0\5D#\2\u01df\u01de\3")
        buf.write("\2\2\2\u01df\u01e0\3\2\2\2\u01e0\u01e7\3\2\2\2\u01e1\u01e3")
        buf.write("\7\24\2\2\u01e2\u01e4\5D#\2\u01e3\u01e2\3\2\2\2\u01e3")
        buf.write("\u01e4\3\2\2\2\u01e4\u01e7\3\2\2\2\u01e5\u01e7\7\26\2")
        buf.write("\2\u01e6\u01d3\3\2\2\2\u01e6\u01dd\3\2\2\2\u01e6\u01e1")
        buf.write("\3\2\2\2\u01e6\u01e5\3\2\2\2\u01e7C\3\2\2\2\u01e8\u01eb")
        buf.write("\5J&\2\u01e9\u01eb\5N(\2\u01ea\u01e8\3\2\2\2\u01ea\u01e9")
        buf.write("\3\2\2\2\u01ebE\3\2\2\2\u01ec\u01ef\5H%\2\u01ed\u01ef")
        buf.write("\5L\'\2\u01ee\u01ec\3\2\2\2\u01ee\u01ed\3\2\2\2\u01ef")
        buf.write("G\3\2\2\2\u01f0\u01fd\5L\'\2\u01f1\u01f2\7\65\2\2\u01f2")
        buf.write("\u01f7\5H%\2\u01f3\u01f4\7\64\2\2\u01f4\u01f6\5H%\2\u01f5")
        buf.write("\u01f3\3\2\2\2\u01f6\u01f9\3\2\2\2\u01f7\u01f5\3\2\2\2")
        buf.write("\u01f7\u01f8\3\2\2\2\u01f8\u01fa\3\2\2\2\u01f9\u01f7\3")
        buf.write("\2\2\2\u01fa\u01fb\7\66\2\2\u01fb\u01fd\3\2\2\2\u01fc")
        buf.write("\u01f0\3\2\2\2\u01fc\u01f1\3\2\2\2\u01fdI\3\2\2\2\u01fe")
        buf.write("\u01ff\7\65\2\2\u01ff\u0204\5T+\2\u0200\u0201\7\64\2\2")
        buf.write("\u0201\u0203\5T+\2\u0202\u0200\3\2\2\2\u0203\u0206\3\2")
        buf.write("\2\2\u0204\u0202\3\2\2\2\u0204\u0205\3\2\2\2\u0205\u0207")
        buf.write("\3\2\2\2\u0206\u0204\3\2\2\2\u0207\u0208\7\66\2\2\u0208")
        buf.write("K\3\2\2\2\u0209\u020a\7\65\2\2\u020a\u020f\5R*\2\u020b")
        buf.write("\u020c\7\64\2\2\u020c\u020e\5R*\2\u020d\u020b\3\2\2\2")
        buf.write("\u020e\u0211\3\2\2\2\u020f\u020d\3\2\2\2\u020f\u0210\3")
        buf.write("\2\2\2\u0210\u0212\3\2\2\2\u0211\u020f\3\2\2\2\u0212\u0213")
        buf.write("\7\66\2\2\u0213M\3\2\2\2\u0214\u0216\7\65\2\2\u0215\u0217")
        buf.write("\5T+\2\u0216\u0215\3\2\2\2\u0216\u0217\3\2\2\2\u0217\u0218")
        buf.write("\3\2\2\2\u0218\u021a\7\63\2\2\u0219\u021b\5T+\2\u021a")
        buf.write("\u0219\3\2\2\2\u021a\u021b\3\2\2\2\u021b\u021c\3\2\2\2")
        buf.write("\u021c\u021d\7\66\2\2\u021dO\3\2\2\2\u021e\u021f\5T+\2")
        buf.write("\u021f\u0220\7<\2\2\u0220\u0221\5T+\2\u0221Q\3\2\2\2\u0222")
        buf.write("\u0225\5T+\2\u0223\u0225\5V,\2\u0224\u0222\3\2\2\2\u0224")
        buf.write("\u0223\3\2\2\2\u0225S\3\2\2\2\u0226\u0228\7>\2\2\u0227")
        buf.write("\u0226\3\2\2\2\u0227\u0228\3\2\2\2\u0228\u0229\3\2\2\2")
        buf.write("\u0229\u022a\7B\2\2\u022aU\3\2\2\2\u022b\u022d\7>\2\2")
        buf.write("\u022c\u022b\3\2\2\2\u022c\u022d\3\2\2\2\u022d\u022e\3")
        buf.write("\2\2\2\u022e\u022f\7A\2\2\u022fW\3\2\2\2?[cjnw~\u0084")
        buf.write("\u008a\u0090\u0096\u009c\u00a2\u00a7\u00ae\u00b5\u00de")
        buf.write("\u00e5\u00ef\u00f7\u00fc\u010d\u0116\u011d\u0127\u0130")
        buf.write("\u0132\u0136\u0141\u0146\u014d\u0154\u0157\u016e\u0177")
        buf.write("\u017e\u018a\u0190\u0192\u0199\u01a5\u01ad\u01af\u01c3")
        buf.write("\u01ce\u01d0\u01d5\u01da\u01df\u01e3\u01e6\u01ea\u01ee")
        buf.write("\u01f7\u01fc\u0204\u020f\u0216\u021a\u0224\u0227\u022c")
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
                     "'Dynamics'", "<INVALID>", "'S'", "'A'", "'P'", "'''", 
                     "'if'", "'else'", "'elif'", "'in'", "'init'", "'until'", 
                     "'with'", "'then'", "'never'", "'and'", "'or'", "'not'", 
                     "'True'", "'False'", "'Any'", "':='", "'->'", "'='", 
                     "'*='", "'/='", "'+='", "'-='", "'=='", "'>='", "'<='", 
                     "'!='", "':'", "','", "'['", "']'", "'('", "')'", "'<'", 
                     "'>'", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "INDENT", "DEDENT", "NL", "IMPORT", "PREDICATE", 
                      "FEATURE", "FACTOR", "GOAL", "CONSTANT", "ACTION", 
                      "EFFECT", "REWARD", "POLICY", "EXECUTE", "OPTION", 
                      "MARKOVFEATURE", "DYNAMICS", "S_PRIME", "S", "A", 
                      "P", "PRIME", "IF", "ELSE", "ELIF", "IN", "INIT", 
                      "UNTIL", "WITH", "THEN", "NEVER", "AND", "OR", "NOT", 
                      "TRUE", "FALSE", "ANY_CONDITION", "BIND", "PREDICT", 
                      "ASSIGN", "TIMES_EQ", "DIV_EQ", "PLUS_EQ", "MINUS_EQ", 
                      "EQ_TO", "GT_EQ", "LT_EQ", "NOT_EQ", "COL", "COM", 
                      "L_BRK", "R_BRK", "L_PAR", "R_PAR", "LT", "GT", "TIMES", 
                      "DIVIDE", "PLUS", "MINUS", "FNAME", "IDENTIFIER", 
                      "DECIMAL", "INTEGER", "SKIP_", "ANY" ]

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
    RULE_policy_statement = 15
    RULE_execute = 16
    RULE_conditional_subpolicy = 17
    RULE_probabilistic_subpolicy = 18
    RULE_probabilistic_policy_statement = 19
    RULE_effect = 20
    RULE_effect_statement_collection = 21
    RULE_effect_statement = 22
    RULE_reward = 23
    RULE_prediction = 24
    RULE_effect_reference = 25
    RULE_conditional_effect = 26
    RULE_probabilistic_effect = 27
    RULE_probabilistic_effect_statement = 28
    RULE_probabilistic_condition = 29
    RULE_arithmetic_exp = 30
    RULE_boolean_exp = 31
    RULE_any_bound_var = 32
    RULE_trailer = 33
    RULE_any_array = 34
    RULE_compound_array_exp = 35
    RULE_int_array_exp = 36
    RULE_any_num_array_exp = 37
    RULE_slice_exp = 38
    RULE_integer_fraction = 39
    RULE_any_number = 40
    RULE_any_integer = 41
    RULE_any_decimal = 42

    ruleNames =  [ "program", "imports", "import_stat", "declarations", 
                   "dec", "constant", "action", "factor", "predicate", "goal", 
                   "feature", "markov_feature", "option", "option_condition", 
                   "policy", "policy_statement", "execute", "conditional_subpolicy", 
                   "probabilistic_subpolicy", "probabilistic_policy_statement", 
                   "effect", "effect_statement_collection", "effect_statement", 
                   "reward", "prediction", "effect_reference", "conditional_effect", 
                   "probabilistic_effect", "probabilistic_effect_statement", 
                   "probabilistic_condition", "arithmetic_exp", "boolean_exp", 
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
    DYNAMICS=17
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
    NEVER=31
    AND=32
    OR=33
    NOT=34
    TRUE=35
    FALSE=36
    ANY_CONDITION=37
    BIND=38
    PREDICT=39
    ASSIGN=40
    TIMES_EQ=41
    DIV_EQ=42
    PLUS_EQ=43
    MINUS_EQ=44
    EQ_TO=45
    GT_EQ=46
    LT_EQ=47
    NOT_EQ=48
    COL=49
    COM=50
    L_BRK=51
    R_BRK=52
    L_PAR=53
    R_PAR=54
    LT=55
    GT=56
    TIMES=57
    DIVIDE=58
    PLUS=59
    MINUS=60
    FNAME=61
    IDENTIFIER=62
    DECIMAL=63
    INTEGER=64
    SKIP_=65
    ANY=66

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
            self.state = 89
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 86
                    self.match(RLangParser.NL) 
                self.state = 91
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 92
            self.imports()
            self.state = 93
            self.declarations()
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.NL:
                self.state = 94
                self.match(RLangParser.NL)
                self.state = 99
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
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.IMPORT:
                self.state = 100
                self.import_stat()
                self.state = 102 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 101
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 104 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                self.state = 110
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
            self.state = 111
            self.match(RLangParser.IMPORT)
            self.state = 112
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
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RLangParser.PREDICATE) | (1 << RLangParser.FEATURE) | (1 << RLangParser.FACTOR) | (1 << RLangParser.GOAL) | (1 << RLangParser.CONSTANT) | (1 << RLangParser.ACTION) | (1 << RLangParser.EFFECT) | (1 << RLangParser.POLICY) | (1 << RLangParser.OPTION) | (1 << RLangParser.MARKOVFEATURE))) != 0):
                self.state = 114
                self.dec()
                self.state = 119
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
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.CONSTANT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.constant()
                self.state = 122 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 121
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 124 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                pass
            elif token in [RLangParser.ACTION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.action()
                self.state = 128 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 127
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 130 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                pass
            elif token in [RLangParser.FACTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 132
                self.factor()
                self.state = 134 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 133
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 136 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                pass
            elif token in [RLangParser.PREDICATE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 138
                self.predicate()
                self.state = 140 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 139
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 142 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                pass
            elif token in [RLangParser.GOAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 144
                self.goal()
                self.state = 146 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 145
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 148 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                pass
            elif token in [RLangParser.FEATURE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 150
                self.feature()
                self.state = 152 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 151
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 154 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                pass
            elif token in [RLangParser.MARKOVFEATURE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 156
                self.markov_feature()
                self.state = 158 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 157
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 160 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                pass
            elif token in [RLangParser.OPTION]:
                self.enterOuterAlt(localctx, 8)
                self.state = 162
                self.option()
                pass
            elif token in [RLangParser.POLICY]:
                self.enterOuterAlt(localctx, 9)
                self.state = 163
                self.policy()
                pass
            elif token in [RLangParser.EFFECT]:
                self.enterOuterAlt(localctx, 10)
                self.state = 164
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
            self.state = 167
            self.match(RLangParser.CONSTANT)
            self.state = 168
            self.match(RLangParser.IDENTIFIER)
            self.state = 169
            self.match(RLangParser.BIND)
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 170
                self.arithmetic_exp(0)
                pass

            elif la_ == 2:
                self.state = 171
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
            self.state = 174
            self.match(RLangParser.ACTION)
            self.state = 175
            self.match(RLangParser.IDENTIFIER)
            self.state = 176
            self.match(RLangParser.BIND)
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.MINUS, RLangParser.DECIMAL, RLangParser.INTEGER]:
                self.state = 177
                self.any_number()
                pass
            elif token in [RLangParser.L_BRK]:
                self.state = 178
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
            self.state = 181
            self.match(RLangParser.FACTOR)
            self.state = 182
            self.match(RLangParser.IDENTIFIER)
            self.state = 183
            self.match(RLangParser.BIND)
            self.state = 184
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
            self.state = 186
            self.match(RLangParser.PREDICATE)
            self.state = 187
            self.match(RLangParser.IDENTIFIER)
            self.state = 188
            self.match(RLangParser.BIND)
            self.state = 189
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
            self.state = 191
            self.match(RLangParser.GOAL)
            self.state = 192
            self.match(RLangParser.IDENTIFIER)
            self.state = 193
            self.match(RLangParser.BIND)
            self.state = 194
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
            self.state = 196
            self.match(RLangParser.FEATURE)
            self.state = 197
            self.match(RLangParser.IDENTIFIER)
            self.state = 198
            self.match(RLangParser.BIND)
            self.state = 199
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
            self.state = 201
            self.match(RLangParser.MARKOVFEATURE)
            self.state = 202
            self.match(RLangParser.IDENTIFIER)
            self.state = 203
            self.match(RLangParser.BIND)
            self.state = 204
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

        def policy_statement(self):
            return self.getTypedRuleContext(RLangParser.Policy_statementContext,0)


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
            self.state = 206
            self.match(RLangParser.OPTION)
            self.state = 207
            self.match(RLangParser.IDENTIFIER)
            self.state = 208
            self.match(RLangParser.COL)
            self.state = 209
            self.match(RLangParser.INDENT)
            self.state = 210
            self.match(RLangParser.INIT)
            self.state = 211
            localctx.init = self.option_condition()
            self.state = 212
            self.match(RLangParser.INDENT)
            self.state = 213
            self.policy_statement()
            self.state = 214
            self.match(RLangParser.DEDENT)
            self.state = 215
            self.match(RLangParser.UNTIL)
            self.state = 216
            localctx.until = self.option_condition()
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.NL:
                self.state = 217
                self.match(RLangParser.NL)
                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 223
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
            self.state = 227
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.S_PRIME, RLangParser.S, RLangParser.A, RLangParser.NOT, RLangParser.TRUE, RLangParser.FALSE, RLangParser.L_BRK, RLangParser.L_PAR, RLangParser.MINUS, RLangParser.IDENTIFIER, RLangParser.DECIMAL, RLangParser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.boolean_exp(0)
                pass
            elif token in [RLangParser.ANY_CONDITION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
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

        def policy_statement(self):
            return self.getTypedRuleContext(RLangParser.Policy_statementContext,0)


        def DEDENT(self):
            return self.getToken(RLangParser.DEDENT, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.NL)
            else:
                return self.getToken(RLangParser.NL, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(RLangParser.POLICY)
            self.state = 230
            self.match(RLangParser.IDENTIFIER)
            self.state = 231
            self.match(RLangParser.COL)
            self.state = 232
            self.match(RLangParser.INDENT)
            self.state = 233
            self.policy_statement()
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.NL:
                self.state = 234
                self.match(RLangParser.NL)
                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 240
            self.match(RLangParser.DEDENT)
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
        self.enterRule(localctx, 30, self.RULE_policy_statement)
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Policy_statement_executeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.execute()
                pass

            elif la_ == 2:
                localctx = RLangParser.Policy_statement_conditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 243
                self.conditional_subpolicy()
                pass

            elif la_ == 3:
                localctx = RLangParser.Policy_statement_probabilisticContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 244
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
        self.enterRule(localctx, 32, self.RULE_execute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(RLangParser.EXECUTE)
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 248
                self.match(RLangParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 249
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
            self.if_subpolicy = None # Policy_statementContext
            self._boolean_exp = None # Boolean_expContext
            self.elif_conditions = list() # of Boolean_expContexts
            self._policy_statement = None # Policy_statementContext
            self.elif_subpolicies = list() # of Policy_statementContexts
            self.else_subpolicy = None # Policy_statementContext

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


        def policy_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Policy_statementContext)
            else:
                return self.getTypedRuleContext(RLangParser.Policy_statementContext,i)


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
        self.enterRule(localctx, 34, self.RULE_conditional_subpolicy)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(RLangParser.IF)
            self.state = 253
            localctx.if_condition = self.boolean_exp(0)
            self.state = 254
            self.match(RLangParser.COL)
            self.state = 255
            self.match(RLangParser.INDENT)
            self.state = 256
            localctx.if_subpolicy = self.policy_statement()
            self.state = 257
            self.match(RLangParser.DEDENT)
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.ELIF:
                self.state = 258
                self.match(RLangParser.ELIF)
                self.state = 259
                localctx._boolean_exp = self.boolean_exp(0)
                localctx.elif_conditions.append(localctx._boolean_exp)
                self.state = 260
                self.match(RLangParser.COL)
                self.state = 261
                self.match(RLangParser.INDENT)
                self.state = 262
                localctx._policy_statement = self.policy_statement()
                localctx.elif_subpolicies.append(localctx._policy_statement)
                self.state = 263
                self.match(RLangParser.DEDENT)
                self.state = 269
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.ELSE:
                self.state = 270
                self.match(RLangParser.ELSE)
                self.state = 271
                self.match(RLangParser.COL)
                self.state = 272
                self.match(RLangParser.INDENT)
                self.state = 273
                localctx.else_subpolicy = self.policy_statement()
                self.state = 274
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
        self.enterRule(localctx, 36, self.RULE_probabilistic_subpolicy)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            localctx._probabilistic_policy_statement = self.probabilistic_policy_statement()
            localctx.subpolicies.append(localctx._probabilistic_policy_statement)
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.OR:
                self.state = 279
                self.match(RLangParser.OR)
                self.state = 280
                localctx._probabilistic_policy_statement = self.probabilistic_policy_statement()
                localctx.subpolicies.append(localctx._probabilistic_policy_statement)
                self.state = 285
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
        def policy_statement(self):
            return self.getTypedRuleContext(RLangParser.Policy_statementContext,0)

        def DEDENT(self):
            return self.getToken(RLangParser.DEDENT, 0)
        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.NL)
            else:
                return self.getToken(RLangParser.NL, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProbabilistic_policy_statement_no_sugar" ):
                listener.enterProbabilistic_policy_statement_no_sugar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProbabilistic_policy_statement_no_sugar" ):
                listener.exitProbabilistic_policy_statement_no_sugar(self)



    def probabilistic_policy_statement(self):

        localctx = RLangParser.Probabilistic_policy_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_probabilistic_policy_statement)
        self._la = 0 # Token type
        try:
            self.state = 304
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.WITH]:
                localctx = RLangParser.Probabilistic_policy_statement_no_sugarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.probabilistic_condition()
                self.state = 287
                self.match(RLangParser.COL)
                self.state = 288
                self.match(RLangParser.INDENT)
                self.state = 289
                self.policy_statement()
                self.state = 291 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 290
                    self.match(RLangParser.NL)
                    self.state = 293 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RLangParser.NL):
                        break

                self.state = 295
                self.match(RLangParser.DEDENT)
                pass
            elif token in [RLangParser.EXECUTE]:
                localctx = RLangParser.Probabilistic_policy_statement_sugarContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.execute()
                self.state = 298
                self.probabilistic_condition()
                self.state = 300 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 299
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 302 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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


    class EffectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EFFECT(self):
            return self.getToken(RLangParser.EFFECT, 0)

        def COL(self):
            return self.getToken(RLangParser.COL, 0)

        def INDENT(self):
            return self.getToken(RLangParser.INDENT, 0)

        def effect_statement_collection(self):
            return self.getTypedRuleContext(RLangParser.Effect_statement_collectionContext,0)


        def DEDENT(self):
            return self.getToken(RLangParser.DEDENT, 0)

        def IDENTIFIER(self):
            return self.getToken(RLangParser.IDENTIFIER, 0)

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
        self.enterRule(localctx, 40, self.RULE_effect)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(RLangParser.EFFECT)
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.IDENTIFIER:
                self.state = 307
                self.match(RLangParser.IDENTIFIER)


            self.state = 310
            self.match(RLangParser.COL)
            self.state = 311
            self.match(RLangParser.INDENT)
            self.state = 312
            self.effect_statement_collection()
            self.state = 313
            self.match(RLangParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Effect_statement_collectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._effect_statement = None # Effect_statementContext
            self.statements = list() # of Effect_statementContexts

        def effect_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Effect_statementContext)
            else:
                return self.getTypedRuleContext(RLangParser.Effect_statementContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.NL)
            else:
                return self.getToken(RLangParser.NL, i)

        def getRuleIndex(self):
            return RLangParser.RULE_effect_statement_collection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEffect_statement_collection" ):
                listener.enterEffect_statement_collection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEffect_statement_collection" ):
                listener.exitEffect_statement_collection(self)




    def effect_statement_collection(self):

        localctx = RLangParser.Effect_statement_collectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_effect_statement_collection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 315
                localctx._effect_statement = self.effect_statement()
                localctx.statements.append(localctx._effect_statement)
                self.state = 319
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.NL:
                    self.state = 316
                    self.match(RLangParser.NL)
                    self.state = 321
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 324 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RLangParser.REWARD) | (1 << RLangParser.S_PRIME) | (1 << RLangParser.IF) | (1 << RLangParser.WITH) | (1 << RLangParser.PREDICT) | (1 << RLangParser.IDENTIFIER))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Effect_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RLangParser.RULE_effect_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Effect_statement_referenceContext(Effect_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Effect_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def effect_reference(self):
            return self.getTypedRuleContext(RLangParser.Effect_referenceContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEffect_statement_reference" ):
                listener.enterEffect_statement_reference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEffect_statement_reference" ):
                listener.exitEffect_statement_reference(self)


    class Effect_statement_predictionContext(Effect_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Effect_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def prediction(self):
            return self.getTypedRuleContext(RLangParser.PredictionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEffect_statement_prediction" ):
                listener.enterEffect_statement_prediction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEffect_statement_prediction" ):
                listener.exitEffect_statement_prediction(self)


    class Effect_statement_conditionalContext(Effect_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Effect_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def conditional_effect(self):
            return self.getTypedRuleContext(RLangParser.Conditional_effectContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEffect_statement_conditional" ):
                listener.enterEffect_statement_conditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEffect_statement_conditional" ):
                listener.exitEffect_statement_conditional(self)


    class Effect_statement_probabilisticContext(Effect_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Effect_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def probabilistic_effect(self):
            return self.getTypedRuleContext(RLangParser.Probabilistic_effectContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEffect_statement_probabilistic" ):
                listener.enterEffect_statement_probabilistic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEffect_statement_probabilistic" ):
                listener.exitEffect_statement_probabilistic(self)


    class Effect_statement_rewardContext(Effect_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Effect_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def reward(self):
            return self.getTypedRuleContext(RLangParser.RewardContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEffect_statement_reward" ):
                listener.enterEffect_statement_reward(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEffect_statement_reward" ):
                listener.exitEffect_statement_reward(self)



    def effect_statement(self):

        localctx = RLangParser.Effect_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_effect_statement)
        try:
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Effect_statement_rewardContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.reward()
                pass

            elif la_ == 2:
                localctx = RLangParser.Effect_statement_predictionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 327
                self.prediction()
                pass

            elif la_ == 3:
                localctx = RLangParser.Effect_statement_referenceContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 328
                self.effect_reference()
                pass

            elif la_ == 4:
                localctx = RLangParser.Effect_statement_conditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 329
                self.conditional_effect()
                pass

            elif la_ == 5:
                localctx = RLangParser.Effect_statement_probabilisticContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 330
                self.probabilistic_effect()
                pass


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
        self.enterRule(localctx, 46, self.RULE_reward)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(RLangParser.REWARD)
            self.state = 334
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
        self.enterRule(localctx, 48, self.RULE_prediction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.IDENTIFIER]:
                self.state = 336
                self.match(RLangParser.IDENTIFIER)
                self.state = 338
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==RLangParser.PRIME:
                    self.state = 337
                    self.match(RLangParser.PRIME)


                pass
            elif token in [RLangParser.S_PRIME]:
                self.state = 340
                self.match(RLangParser.S_PRIME)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 343
            self.match(RLangParser.PREDICT)
            self.state = 344
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
        self.enterRule(localctx, 50, self.RULE_effect_reference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(RLangParser.PREDICT)
            self.state = 347
            self.match(RLangParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conditional_effectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.if_condition = None # Boolean_expContext
            self.if_effect = None # Effect_statement_collectionContext
            self._boolean_exp = None # Boolean_expContext
            self.elif_conditions = list() # of Boolean_expContexts
            self._effect_statement_collection = None # Effect_statement_collectionContext
            self.elif_effects = list() # of Effect_statement_collectionContexts
            self.else_effect = None # Effect_statement_collectionContext

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


        def effect_statement_collection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Effect_statement_collectionContext)
            else:
                return self.getTypedRuleContext(RLangParser.Effect_statement_collectionContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.ELIF)
            else:
                return self.getToken(RLangParser.ELIF, i)

        def ELSE(self):
            return self.getToken(RLangParser.ELSE, 0)

        def getRuleIndex(self):
            return RLangParser.RULE_conditional_effect

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional_effect" ):
                listener.enterConditional_effect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional_effect" ):
                listener.exitConditional_effect(self)




    def conditional_effect(self):

        localctx = RLangParser.Conditional_effectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_conditional_effect)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(RLangParser.IF)
            self.state = 350
            localctx.if_condition = self.boolean_exp(0)
            self.state = 351
            self.match(RLangParser.COL)
            self.state = 352
            self.match(RLangParser.INDENT)
            self.state = 353
            localctx.if_effect = self.effect_statement_collection()
            self.state = 354
            self.match(RLangParser.DEDENT)
            self.state = 364
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.ELIF:
                self.state = 355
                self.match(RLangParser.ELIF)
                self.state = 356
                localctx._boolean_exp = self.boolean_exp(0)
                localctx.elif_conditions.append(localctx._boolean_exp)
                self.state = 357
                self.match(RLangParser.COL)
                self.state = 358
                self.match(RLangParser.INDENT)
                self.state = 359
                localctx._effect_statement_collection = self.effect_statement_collection()
                localctx.elif_effects.append(localctx._effect_statement_collection)
                self.state = 360
                self.match(RLangParser.DEDENT)
                self.state = 366
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 373
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.ELSE:
                self.state = 367
                self.match(RLangParser.ELSE)
                self.state = 368
                self.match(RLangParser.COL)
                self.state = 369
                self.match(RLangParser.INDENT)
                self.state = 370
                localctx.else_effect = self.effect_statement_collection()
                self.state = 371
                self.match(RLangParser.DEDENT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Probabilistic_effectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._probabilistic_effect_statement = None # Probabilistic_effect_statementContext
            self.effects = list() # of Probabilistic_effect_statementContexts

        def probabilistic_effect_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Probabilistic_effect_statementContext)
            else:
                return self.getTypedRuleContext(RLangParser.Probabilistic_effect_statementContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.OR)
            else:
                return self.getToken(RLangParser.OR, i)

        def getRuleIndex(self):
            return RLangParser.RULE_probabilistic_effect

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProbabilistic_effect" ):
                listener.enterProbabilistic_effect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProbabilistic_effect" ):
                listener.exitProbabilistic_effect(self)




    def probabilistic_effect(self):

        localctx = RLangParser.Probabilistic_effectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_probabilistic_effect)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            localctx._probabilistic_effect_statement = self.probabilistic_effect_statement()
            localctx.effects.append(localctx._probabilistic_effect_statement)
            self.state = 380
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.OR:
                self.state = 376
                self.match(RLangParser.OR)
                self.state = 377
                localctx._probabilistic_effect_statement = self.probabilistic_effect_statement()
                localctx.effects.append(localctx._probabilistic_effect_statement)
                self.state = 382
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Probabilistic_effect_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RLangParser.RULE_probabilistic_effect_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Probabilistic_effect_statement_no_sugarContext(Probabilistic_effect_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Probabilistic_effect_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def probabilistic_condition(self):
            return self.getTypedRuleContext(RLangParser.Probabilistic_conditionContext,0)

        def COL(self):
            return self.getToken(RLangParser.COL, 0)
        def INDENT(self):
            return self.getToken(RLangParser.INDENT, 0)
        def effect_statement_collection(self):
            return self.getTypedRuleContext(RLangParser.Effect_statement_collectionContext,0)

        def DEDENT(self):
            return self.getToken(RLangParser.DEDENT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProbabilistic_effect_statement_no_sugar" ):
                listener.enterProbabilistic_effect_statement_no_sugar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProbabilistic_effect_statement_no_sugar" ):
                listener.exitProbabilistic_effect_statement_no_sugar(self)


    class Probabilistic_effect_statement_sugarContext(Probabilistic_effect_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Probabilistic_effect_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def probabilistic_condition(self):
            return self.getTypedRuleContext(RLangParser.Probabilistic_conditionContext,0)

        def reward(self):
            return self.getTypedRuleContext(RLangParser.RewardContext,0)

        def prediction(self):
            return self.getTypedRuleContext(RLangParser.PredictionContext,0)

        def effect_reference(self):
            return self.getTypedRuleContext(RLangParser.Effect_referenceContext,0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.NL)
            else:
                return self.getToken(RLangParser.NL, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProbabilistic_effect_statement_sugar" ):
                listener.enterProbabilistic_effect_statement_sugar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProbabilistic_effect_statement_sugar" ):
                listener.exitProbabilistic_effect_statement_sugar(self)



    def probabilistic_effect_statement(self):

        localctx = RLangParser.Probabilistic_effect_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_probabilistic_effect_statement)
        try:
            self.state = 400
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.WITH]:
                localctx = RLangParser.Probabilistic_effect_statement_no_sugarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                self.probabilistic_condition()
                self.state = 384
                self.match(RLangParser.COL)
                self.state = 385
                self.match(RLangParser.INDENT)
                self.state = 386
                self.effect_statement_collection()
                self.state = 387
                self.match(RLangParser.DEDENT)
                pass
            elif token in [RLangParser.REWARD, RLangParser.S_PRIME, RLangParser.PREDICT, RLangParser.IDENTIFIER]:
                localctx = RLangParser.Probabilistic_effect_statement_sugarContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 392
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RLangParser.REWARD]:
                    self.state = 389
                    self.reward()
                    pass
                elif token in [RLangParser.S_PRIME, RLangParser.IDENTIFIER]:
                    self.state = 390
                    self.prediction()
                    pass
                elif token in [RLangParser.PREDICT]:
                    self.state = 391
                    self.effect_reference()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 394
                self.probabilistic_condition()
                self.state = 396 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 395
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 398 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

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
        self.enterRule(localctx, 58, self.RULE_probabilistic_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.match(RLangParser.WITH)
            self.state = 403
            self.match(RLangParser.P)
            self.state = 404
            self.match(RLangParser.L_PAR)
            self.state = 407
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 405
                self.any_number()
                pass

            elif la_ == 2:
                self.state = 406
                self.integer_fraction()
                pass


            self.state = 409
            self.match(RLangParser.R_PAR)
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
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_arithmetic_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.L_PAR]:
                localctx = RLangParser.Arith_parenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 412
                self.match(RLangParser.L_PAR)
                self.state = 413
                self.arithmetic_exp(0)
                self.state = 414
                self.match(RLangParser.R_PAR)
                pass
            elif token in [RLangParser.MINUS, RLangParser.DECIMAL, RLangParser.INTEGER]:
                localctx = RLangParser.Arith_numberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 416
                self.any_number()
                pass
            elif token in [RLangParser.L_BRK]:
                localctx = RLangParser.Arith_arrayContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 417
                self.any_array()
                pass
            elif token in [RLangParser.S_PRIME, RLangParser.S, RLangParser.A, RLangParser.IDENTIFIER]:
                localctx = RLangParser.Arith_bound_varContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 418
                self.any_bound_var()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 429
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 427
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                    if la_ == 1:
                        localctx = RLangParser.Arith_times_divideContext(self, RLangParser.Arithmetic_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_exp)
                        self.state = 421
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 422
                        _la = self._input.LA(1)
                        if not(_la==RLangParser.TIMES or _la==RLangParser.DIVIDE):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 423
                        localctx.rhs = self.arithmetic_exp(6)
                        pass

                    elif la_ == 2:
                        localctx = RLangParser.Arith_plus_minusContext(self, RLangParser.Arithmetic_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_exp)
                        self.state = 424
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 425
                        _la = self._input.LA(1)
                        if not(_la==RLangParser.PLUS or _la==RLangParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 426
                        localctx.rhs = self.arithmetic_exp(5)
                        pass

             
                self.state = 431
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

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
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_boolean_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Bool_parenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 433
                self.match(RLangParser.L_PAR)
                self.state = 434
                self.boolean_exp(0)
                self.state = 435
                self.match(RLangParser.R_PAR)
                pass

            elif la_ == 2:
                localctx = RLangParser.Bool_notContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 437
                self.match(RLangParser.NOT)
                self.state = 438
                self.boolean_exp(6)
                pass

            elif la_ == 3:
                localctx = RLangParser.Bool_inContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 439
                localctx.lhs = self.arithmetic_exp(0)
                self.state = 440
                self.match(RLangParser.IN)
                self.state = 441
                localctx.rhs = self.arithmetic_exp(0)
                pass

            elif la_ == 4:
                localctx = RLangParser.Bool_arith_eqContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 443
                localctx.lhs = self.arithmetic_exp(0)
                self.state = 444
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RLangParser.EQ_TO) | (1 << RLangParser.GT_EQ) | (1 << RLangParser.LT_EQ) | (1 << RLangParser.NOT_EQ) | (1 << RLangParser.LT) | (1 << RLangParser.GT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 445
                localctx.rhs = self.arithmetic_exp(0)
                pass

            elif la_ == 5:
                localctx = RLangParser.Bool_bound_varContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 447
                self.any_bound_var()
                pass

            elif la_ == 6:
                localctx = RLangParser.Bool_tfContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 448
                _la = self._input.LA(1)
                if not(_la==RLangParser.TRUE or _la==RLangParser.FALSE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 462
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 460
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
                    if la_ == 1:
                        localctx = RLangParser.Bool_andContext(self, RLangParser.Boolean_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_exp)
                        self.state = 451
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 452
                        self.match(RLangParser.AND)
                        self.state = 453
                        localctx.rhs = self.boolean_exp(9)
                        pass

                    elif la_ == 2:
                        localctx = RLangParser.Bool_orContext(self, RLangParser.Boolean_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_exp)
                        self.state = 454
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 455
                        self.match(RLangParser.OR)
                        self.state = 456
                        localctx.rhs = self.boolean_exp(8)
                        pass

                    elif la_ == 3:
                        localctx = RLangParser.Bool_bool_eqContext(self, RLangParser.Boolean_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_exp)
                        self.state = 457
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 458
                        _la = self._input.LA(1)
                        if not(_la==RLangParser.EQ_TO or _la==RLangParser.NOT_EQ):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 459
                        localctx.rhs = self.boolean_exp(5)
                        pass

             
                self.state = 464
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

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
        self.enterRule(localctx, 64, self.RULE_any_bound_var)
        try:
            self.state = 484
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.IDENTIFIER]:
                localctx = RLangParser.Bound_identifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 465
                self.match(RLangParser.IDENTIFIER)
                self.state = 467
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
                if la_ == 1:
                    self.state = 466
                    self.match(RLangParser.PRIME)


                self.state = 472
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 469
                        self.trailer() 
                    self.state = 474
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

                pass
            elif token in [RLangParser.S]:
                localctx = RLangParser.Bound_stateContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 475
                self.match(RLangParser.S)
                self.state = 477
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                if la_ == 1:
                    self.state = 476
                    self.trailer()


                pass
            elif token in [RLangParser.S_PRIME]:
                localctx = RLangParser.Bound_next_stateContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 479
                self.match(RLangParser.S_PRIME)
                self.state = 481
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
                if la_ == 1:
                    self.state = 480
                    self.trailer()


                pass
            elif token in [RLangParser.A]:
                localctx = RLangParser.Bound_actionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 483
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
        self.enterRule(localctx, 66, self.RULE_trailer)
        try:
            self.state = 488
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Trailer_arrayContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 486
                self.int_array_exp()
                pass

            elif la_ == 2:
                localctx = RLangParser.Trailer_sliceContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 487
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
        self.enterRule(localctx, 68, self.RULE_any_array)
        try:
            self.state = 492
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Any_array_compoundContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 490
                self.compound_array_exp()
                pass

            elif la_ == 2:
                localctx = RLangParser.Any_array_any_numContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 491
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
        self.enterRule(localctx, 70, self.RULE_compound_array_exp)
        self._la = 0 # Token type
        try:
            self.state = 506
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Compound_array_simpleContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 494
                self.any_num_array_exp()
                pass

            elif la_ == 2:
                localctx = RLangParser.Compound_array_compoundContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 495
                self.match(RLangParser.L_BRK)
                self.state = 496
                localctx._compound_array_exp = self.compound_array_exp()
                localctx.arr.append(localctx._compound_array_exp)
                self.state = 501
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.COM:
                    self.state = 497
                    self.match(RLangParser.COM)
                    self.state = 498
                    localctx._compound_array_exp = self.compound_array_exp()
                    localctx.arr.append(localctx._compound_array_exp)
                    self.state = 503
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 504
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
        self.enterRule(localctx, 72, self.RULE_int_array_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            self.match(RLangParser.L_BRK)
            self.state = 509
            localctx._any_integer = self.any_integer()
            localctx.arr.append(localctx._any_integer)
            self.state = 514
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.COM:
                self.state = 510
                self.match(RLangParser.COM)
                self.state = 511
                localctx._any_integer = self.any_integer()
                localctx.arr.append(localctx._any_integer)
                self.state = 516
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 517
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
        self.enterRule(localctx, 74, self.RULE_any_num_array_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            self.match(RLangParser.L_BRK)
            self.state = 520
            localctx._any_number = self.any_number()
            localctx.arr.append(localctx._any_number)
            self.state = 525
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.COM:
                self.state = 521
                self.match(RLangParser.COM)
                self.state = 522
                localctx._any_number = self.any_number()
                localctx.arr.append(localctx._any_number)
                self.state = 527
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 528
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
        self.enterRule(localctx, 76, self.RULE_slice_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
            self.match(RLangParser.L_BRK)
            self.state = 532
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.MINUS or _la==RLangParser.INTEGER:
                self.state = 531
                localctx.start_ind = self.any_integer()


            self.state = 534
            self.match(RLangParser.COL)
            self.state = 536
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.MINUS or _la==RLangParser.INTEGER:
                self.state = 535
                localctx.stop_ind = self.any_integer()


            self.state = 538
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
        self.enterRule(localctx, 78, self.RULE_integer_fraction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 540
            localctx.lhs = self.any_integer()
            self.state = 541
            self.match(RLangParser.DIVIDE)
            self.state = 542
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
        self.enterRule(localctx, 80, self.RULE_any_number)
        try:
            self.state = 546
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Any_num_intContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 544
                self.any_integer()
                pass

            elif la_ == 2:
                localctx = RLangParser.Any_num_decContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 545
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
        self.enterRule(localctx, 82, self.RULE_any_integer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 549
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.MINUS:
                self.state = 548
                self.match(RLangParser.MINUS)


            self.state = 551
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
        self.enterRule(localctx, 84, self.RULE_any_decimal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 554
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.MINUS:
                self.state = 553
                self.match(RLangParser.MINUS)


            self.state = 556
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
        self._predicates[30] = self.arithmetic_exp_sempred
        self._predicates[31] = self.boolean_exp_sempred
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
         




