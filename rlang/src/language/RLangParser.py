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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\39")
        buf.write("\u017e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\7\2\60\n")
        buf.write("\2\f\2\16\2\63\13\2\3\2\3\2\6\2\67\n\2\r\2\16\28\7\2;")
        buf.write("\n\2\f\2\16\2>\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\5\3J\n\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\5\6[\n\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\6\tm\n\t\r")
        buf.write("\t\16\tn\7\tq\n\t\f\t\16\tt\13\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\6\n\u0081\n\n\r\n\16\n\u0082\7")
        buf.write("\n\u0085\n\n\f\n\16\n\u0088\13\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\6\13\u0094\n\13\r\13\16\13\u0095")
        buf.write("\7\13\u0098\n\13\f\13\16\13\u009b\13\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\5\f\u00a4\n\f\3\r\3\r\3\r\5\r\u00a9\n")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\6\16\u00b2\n\16")
        buf.write("\r\16\16\16\u00b3\7\16\u00b6\n\16\f\16\16\16\u00b9\13")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\6\16\u00c2\n\16")
        buf.write("\r\16\16\16\u00c3\7\16\u00c6\n\16\f\16\16\16\u00c9\13")
        buf.write("\16\3\16\3\16\7\16\u00cd\n\16\f\16\16\16\u00d0\13\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\6\16\u00d7\n\16\r\16\16\16\u00d8")
        buf.write("\7\16\u00db\n\16\f\16\16\16\u00de\13\16\3\16\7\16\u00e1")
        buf.write("\n\16\f\16\16\16\u00e4\13\16\5\16\u00e6\n\16\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00f1\n\20\3")
        buf.write("\21\3\21\5\21\u00f5\n\21\3\21\3\21\3\21\3\21\5\21\u00fb")
        buf.write("\n\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\5\23\u010b\n\23\3\23\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u0117\n\23\5\23")
        buf.write("\u0119\n\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\7\23\u0124\n\23\f\23\16\23\u0127\13\23\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\24\5\24\u012f\n\24\3\24\3\24\3\24\5\24")
        buf.write("\u0134\n\24\3\24\7\24\u0137\n\24\f\24\16\24\u013a\13\24")
        buf.write("\5\24\u013c\n\24\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u0144")
        buf.write("\n\24\f\24\16\24\u0147\13\24\3\25\3\25\3\25\3\26\3\26")
        buf.write("\5\26\u014e\n\26\3\26\3\26\3\26\5\26\u0153\n\26\3\26\7")
        buf.write("\26\u0156\n\26\f\26\16\26\u0159\13\26\3\26\3\26\3\26\5")
        buf.write("\26\u015e\n\26\3\26\5\26\u0161\n\26\3\26\3\26\5\26\u0165")
        buf.write("\n\26\3\26\5\26\u0168\n\26\3\26\5\26\u016b\n\26\3\27\3")
        buf.write("\27\5\27\u016f\n\27\3\27\3\27\3\27\5\27\u0174\n\27\3\27")
        buf.write("\7\27\u0177\n\27\f\27\16\27\u017a\13\27\3\27\3\27\3\27")
        buf.write("\2\4$&\30\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&")
        buf.write("(*,\2\t\3\2\678\3\2 $\4\2%%((\4\2%(/\60\3\2\35\36\3\2")
        buf.write("\61\62\3\2\63\64\2\u01a8\2\61\3\2\2\2\4I\3\2\2\2\6K\3")
        buf.write("\2\2\2\bP\3\2\2\2\nU\3\2\2\2\f\\\3\2\2\2\16a\3\2\2\2\20")
        buf.write("f\3\2\2\2\22w\3\2\2\2\24\u008d\3\2\2\2\26\u009e\3\2\2")
        buf.write("\2\30\u00a8\3\2\2\2\32\u00e5\3\2\2\2\34\u00e7\3\2\2\2")
        buf.write("\36\u00ea\3\2\2\2 \u00f2\3\2\2\2\"\u00fc\3\2\2\2$\u0118")
        buf.write("\3\2\2\2&\u013b\3\2\2\2(\u0148\3\2\2\2*\u016a\3\2\2\2")
        buf.write(",\u016c\3\2\2\2.\60\7\5\2\2/.\3\2\2\2\60\63\3\2\2\2\61")
        buf.write("/\3\2\2\2\61\62\3\2\2\2\62<\3\2\2\2\63\61\3\2\2\2\64\66")
        buf.write("\5\4\3\2\65\67\7\5\2\2\66\65\3\2\2\2\678\3\2\2\28\66\3")
        buf.write("\2\2\289\3\2\2\29;\3\2\2\2:\64\3\2\2\2;>\3\2\2\2<:\3\2")
        buf.write("\2\2<=\3\2\2\2=\3\3\2\2\2><\3\2\2\2?J\5\6\4\2@J\5\b\5")
        buf.write("\2AJ\5\n\6\2BJ\5\f\7\2CJ\5\16\b\2DJ\5\20\t\2EJ\5\36\20")
        buf.write("\2FJ\5\22\n\2GJ\5\24\13\2HJ\5\26\f\2I?\3\2\2\2I@\3\2\2")
        buf.write("\2IA\3\2\2\2IB\3\2\2\2IC\3\2\2\2ID\3\2\2\2IE\3\2\2\2I")
        buf.write("F\3\2\2\2IG\3\2\2\2IH\3\2\2\2J\5\3\2\2\2KL\7\6\2\2LM\7")
        buf.write("\66\2\2MN\7\37\2\2NO\5$\23\2O\7\3\2\2\2PQ\7\7\2\2QR\7")
        buf.write("\66\2\2RS\7\37\2\2ST\5&\24\2T\t\3\2\2\2UV\7\b\2\2VW\7")
        buf.write("\66\2\2WX\7\37\2\2XZ\7\22\2\2Y[\5*\26\2ZY\3\2\2\2Z[\3")
        buf.write("\2\2\2[\13\3\2\2\2\\]\7\t\2\2]^\7\66\2\2^_\7\37\2\2_`")
        buf.write("\5$\23\2`\r\3\2\2\2ab\7\13\2\2bc\7\66\2\2cd\7\37\2\2d")
        buf.write("e\78\2\2e\17\3\2\2\2fg\7\f\2\2gh\5$\23\2hi\7)\2\2ir\7")
        buf.write("\3\2\2jl\5\30\r\2km\7\5\2\2lk\3\2\2\2mn\3\2\2\2nl\3\2")
        buf.write("\2\2no\3\2\2\2oq\3\2\2\2pj\3\2\2\2qt\3\2\2\2rp\3\2\2\2")
        buf.write("rs\3\2\2\2su\3\2\2\2tr\3\2\2\2uv\7\4\2\2v\21\3\2\2\2w")
        buf.write("x\7\20\2\2xy\7\66\2\2yz\7)\2\2z{\7\3\2\2{|\7\30\2\2|}")
        buf.write("\5$\23\2}\u0086\7\3\2\2~\u0080\5\32\16\2\177\u0081\7\5")
        buf.write("\2\2\u0080\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0080")
        buf.write("\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0085\3\2\2\2\u0084")
        buf.write("~\3\2\2\2\u0085\u0088\3\2\2\2\u0086\u0084\3\2\2\2\u0086")
        buf.write("\u0087\3\2\2\2\u0087\u0089\3\2\2\2\u0088\u0086\3\2\2\2")
        buf.write("\u0089\u008a\7\4\2\2\u008a\u008b\7\31\2\2\u008b\u008c")
        buf.write("\5$\23\2\u008c\23\3\2\2\2\u008d\u008e\7\16\2\2\u008e\u008f")
        buf.write("\7\66\2\2\u008f\u0090\7)\2\2\u0090\u0099\7\3\2\2\u0091")
        buf.write("\u0093\5\32\16\2\u0092\u0094\7\5\2\2\u0093\u0092\3\2\2")
        buf.write("\2\u0094\u0095\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0096")
        buf.write("\3\2\2\2\u0096\u0098\3\2\2\2\u0097\u0091\3\2\2\2\u0098")
        buf.write("\u009b\3\2\2\2\u0099\u0097\3\2\2\2\u0099\u009a\3\2\2\2")
        buf.write("\u009a\u009c\3\2\2\2\u009b\u0099\3\2\2\2\u009c\u009d\7")
        buf.write("\4\2\2\u009d\25\3\2\2\2\u009e\u009f\7\21\2\2\u009f\u00a0")
        buf.write("\7\66\2\2\u00a0\u00a3\7\37\2\2\u00a1\u00a4\5$\23\2\u00a2")
        buf.write("\u00a4\5&\24\2\u00a3\u00a1\3\2\2\2\u00a3\u00a2\3\2\2\2")
        buf.write("\u00a4\27\3\2\2\2\u00a5\u00a9\5\34\17\2\u00a6\u00a9\5")
        buf.write(" \21\2\u00a7\u00a9\5\36\20\2\u00a8\u00a5\3\2\2\2\u00a8")
        buf.write("\u00a6\3\2\2\2\u00a8\u00a7\3\2\2\2\u00a9\31\3\2\2\2\u00aa")
        buf.write("\u00e6\5\"\22\2\u00ab\u00ac\7\24\2\2\u00ac\u00ad\5$\23")
        buf.write("\2\u00ad\u00ae\7)\2\2\u00ae\u00b7\7\3\2\2\u00af\u00b1")
        buf.write("\5\32\16\2\u00b0\u00b2\7\5\2\2\u00b1\u00b0\3\2\2\2\u00b2")
        buf.write("\u00b3\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2")
        buf.write("\u00b4\u00b6\3\2\2\2\u00b5\u00af\3\2\2\2\u00b6\u00b9\3")
        buf.write("\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00ba")
        buf.write("\3\2\2\2\u00b9\u00b7\3\2\2\2\u00ba\u00ce\7\4\2\2\u00bb")
        buf.write("\u00bc\7\26\2\2\u00bc\u00bd\5$\23\2\u00bd\u00be\7)\2\2")
        buf.write("\u00be\u00c7\7\3\2\2\u00bf\u00c1\5\32\16\2\u00c0\u00c2")
        buf.write("\7\5\2\2\u00c1\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3")
        buf.write("\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c6\3\2\2\2")
        buf.write("\u00c5\u00bf\3\2\2\2\u00c6\u00c9\3\2\2\2\u00c7\u00c5\3")
        buf.write("\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00ca\3\2\2\2\u00c9\u00c7")
        buf.write("\3\2\2\2\u00ca\u00cb\7\4\2\2\u00cb\u00cd\3\2\2\2\u00cc")
        buf.write("\u00bb\3\2\2\2\u00cd\u00d0\3\2\2\2\u00ce\u00cc\3\2\2\2")
        buf.write("\u00ce\u00cf\3\2\2\2\u00cf\u00e2\3\2\2\2\u00d0\u00ce\3")
        buf.write("\2\2\2\u00d1\u00d2\7\25\2\2\u00d2\u00d3\7)\2\2\u00d3\u00dc")
        buf.write("\7\3\2\2\u00d4\u00d6\5\32\16\2\u00d5\u00d7\7\5\2\2\u00d6")
        buf.write("\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00d6\3\2\2\2")
        buf.write("\u00d8\u00d9\3\2\2\2\u00d9\u00db\3\2\2\2\u00da\u00d4\3")
        buf.write("\2\2\2\u00db\u00de\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00dd")
        buf.write("\3\2\2\2\u00dd\u00df\3\2\2\2\u00de\u00dc\3\2\2\2\u00df")
        buf.write("\u00e1\7\4\2\2\u00e0\u00d1\3\2\2\2\u00e1\u00e4\3\2\2\2")
        buf.write("\u00e2\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e6\3")
        buf.write("\2\2\2\u00e4\u00e2\3\2\2\2\u00e5\u00aa\3\2\2\2\u00e5\u00ab")
        buf.write("\3\2\2\2\u00e6\33\3\2\2\2\u00e7\u00e8\7\r\2\2\u00e8\u00e9")
        buf.write("\t\2\2\2\u00e9\35\3\2\2\2\u00ea\u00eb\7\n\2\2\u00eb\u00ec")
        buf.write("\7\66\2\2\u00ec\u00f0\7\37\2\2\u00ed\u00f1\5$\23\2\u00ee")
        buf.write("\u00f1\5&\24\2\u00ef\u00f1\5,\27\2\u00f0\u00ed\3\2\2\2")
        buf.write("\u00f0\u00ee\3\2\2\2\u00f0\u00ef\3\2\2\2\u00f1\37\3\2")
        buf.write("\2\2\u00f2\u00f4\7\66\2\2\u00f3\u00f5\5*\26\2\u00f4\u00f3")
        buf.write("\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6")
        buf.write("\u00fa\t\3\2\2\u00f7\u00fb\5$\23\2\u00f8\u00fb\5&\24\2")
        buf.write("\u00f9\u00fb\5,\27\2\u00fa\u00f7\3\2\2\2\u00fa\u00f8\3")
        buf.write("\2\2\2\u00fa\u00f9\3\2\2\2\u00fb!\3\2\2\2\u00fc\u00fd")
        buf.write("\7\17\2\2\u00fd\u00fe\7\66\2\2\u00fe#\3\2\2\2\u00ff\u0100")
        buf.write("\b\23\1\2\u0100\u0101\7-\2\2\u0101\u0102\5$\23\2\u0102")
        buf.write("\u0103\7.\2\2\u0103\u0119\3\2\2\2\u0104\u0105\7\34\2\2")
        buf.write("\u0105\u0119\5$\23\13\u0106\u0107\7\66\2\2\u0107\u0108")
        buf.write("\7\27\2\2\u0108\u010a\7\66\2\2\u0109\u010b\5*\26\2\u010a")
        buf.write("\u0109\3\2\2\2\u010a\u010b\3\2\2\2\u010b\u0119\3\2\2\2")
        buf.write("\u010c\u010d\7\23\2\2\u010d\u010e\t\4\2\2\u010e\u0119")
        buf.write("\7\66\2\2\u010f\u0110\5&\24\2\u0110\u0111\t\5\2\2\u0111")
        buf.write("\u0112\5&\24\2\u0112\u0119\3\2\2\2\u0113\u0119\t\6\2\2")
        buf.write("\u0114\u0117\7\66\2\2\u0115\u0117\5(\25\2\u0116\u0114")
        buf.write("\3\2\2\2\u0116\u0115\3\2\2\2\u0117\u0119\3\2\2\2\u0118")
        buf.write("\u00ff\3\2\2\2\u0118\u0104\3\2\2\2\u0118\u0106\3\2\2\2")
        buf.write("\u0118\u010c\3\2\2\2\u0118\u010f\3\2\2\2\u0118\u0113\3")
        buf.write("\2\2\2\u0118\u0116\3\2\2\2\u0119\u0125\3\2\2\2\u011a\u011b")
        buf.write("\f\n\2\2\u011b\u011c\7\32\2\2\u011c\u0124\5$\23\13\u011d")
        buf.write("\u011e\f\t\2\2\u011e\u011f\7\33\2\2\u011f\u0124\5$\23")
        buf.write("\n\u0120\u0121\f\6\2\2\u0121\u0122\t\4\2\2\u0122\u0124")
        buf.write("\5$\23\7\u0123\u011a\3\2\2\2\u0123\u011d\3\2\2\2\u0123")
        buf.write("\u0120\3\2\2\2\u0124\u0127\3\2\2\2\u0125\u0123\3\2\2\2")
        buf.write("\u0125\u0126\3\2\2\2\u0126%\3\2\2\2\u0127\u0125\3\2\2")
        buf.write("\2\u0128\u0129\b\24\1\2\u0129\u012a\7-\2\2\u012a\u012b")
        buf.write("\5&\24\2\u012b\u012c\7.\2\2\u012c\u013c\3\2\2\2\u012d")
        buf.write("\u012f\7\64\2\2\u012e\u012d\3\2\2\2\u012e\u012f\3\2\2")
        buf.write("\2\u012f\u0130\3\2\2\2\u0130\u013c\t\2\2\2\u0131\u0134")
        buf.write("\7\66\2\2\u0132\u0134\5(\25\2\u0133\u0131\3\2\2\2\u0133")
        buf.write("\u0132\3\2\2\2\u0134\u0138\3\2\2\2\u0135\u0137\5*\26\2")
        buf.write("\u0136\u0135\3\2\2\2\u0137\u013a\3\2\2\2\u0138\u0136\3")
        buf.write("\2\2\2\u0138\u0139\3\2\2\2\u0139\u013c\3\2\2\2\u013a\u0138")
        buf.write("\3\2\2\2\u013b\u0128\3\2\2\2\u013b\u012e\3\2\2\2\u013b")
        buf.write("\u0133\3\2\2\2\u013c\u0145\3\2\2\2\u013d\u013e\f\6\2\2")
        buf.write("\u013e\u013f\t\7\2\2\u013f\u0144\5&\24\7\u0140\u0141\f")
        buf.write("\5\2\2\u0141\u0142\t\b\2\2\u0142\u0144\5&\24\6\u0143\u013d")
        buf.write("\3\2\2\2\u0143\u0140\3\2\2\2\u0144\u0147\3\2\2\2\u0145")
        buf.write("\u0143\3\2\2\2\u0145\u0146\3\2\2\2\u0146\'\3\2\2\2\u0147")
        buf.write("\u0145\3\2\2\2\u0148\u0149\7\66\2\2\u0149\u014a\7\65\2")
        buf.write("\2\u014a)\3\2\2\2\u014b\u014d\7+\2\2\u014c\u014e\7\64")
        buf.write("\2\2\u014d\u014c\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u014f")
        buf.write("\3\2\2\2\u014f\u0157\78\2\2\u0150\u0152\7*\2\2\u0151\u0153")
        buf.write("\7\64\2\2\u0152\u0151\3\2\2\2\u0152\u0153\3\2\2\2\u0153")
        buf.write("\u0154\3\2\2\2\u0154\u0156\78\2\2\u0155\u0150\3\2\2\2")
        buf.write("\u0156\u0159\3\2\2\2\u0157\u0155\3\2\2\2\u0157\u0158\3")
        buf.write("\2\2\2\u0158\u015a\3\2\2\2\u0159\u0157\3\2\2\2\u015a\u016b")
        buf.write("\7,\2\2\u015b\u0160\7+\2\2\u015c\u015e\7\64\2\2\u015d")
        buf.write("\u015c\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u015f\3\2\2\2")
        buf.write("\u015f\u0161\78\2\2\u0160\u015d\3\2\2\2\u0160\u0161\3")
        buf.write("\2\2\2\u0161\u0162\3\2\2\2\u0162\u0167\7)\2\2\u0163\u0165")
        buf.write("\7\64\2\2\u0164\u0163\3\2\2\2\u0164\u0165\3\2\2\2\u0165")
        buf.write("\u0166\3\2\2\2\u0166\u0168\78\2\2\u0167\u0164\3\2\2\2")
        buf.write("\u0167\u0168\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016b\7")
        buf.write(",\2\2\u016a\u014b\3\2\2\2\u016a\u015b\3\2\2\2\u016b+\3")
        buf.write("\2\2\2\u016c\u016e\7+\2\2\u016d\u016f\7\64\2\2\u016e\u016d")
        buf.write("\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0170\3\2\2\2\u0170")
        buf.write("\u0178\78\2\2\u0171\u0173\7*\2\2\u0172\u0174\7\64\2\2")
        buf.write("\u0173\u0172\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0175\3")
        buf.write("\2\2\2\u0175\u0177\78\2\2\u0176\u0171\3\2\2\2\u0177\u017a")
        buf.write("\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179")
        buf.write("\u017b\3\2\2\2\u017a\u0178\3\2\2\2\u017b\u017c\7,\2\2")
        buf.write("\u017c-\3\2\2\2\61\618<IZnr\u0082\u0086\u0095\u0099\u00a3")
        buf.write("\u00a8\u00b3\u00b7\u00c3\u00c7\u00ce\u00d8\u00dc\u00e2")
        buf.write("\u00e5\u00f0\u00f4\u00fa\u010a\u0116\u0118\u0123\u0125")
        buf.write("\u012e\u0133\u0138\u013b\u0143\u0145\u014d\u0152\u0157")
        buf.write("\u015d\u0160\u0164\u0167\u016a\u016e\u0173\u0178")
        return buf.getvalue()


class RLangParser ( Parser ):

    grammarFileName = "RLangParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'Predicate'", "'Feature'", "'Factor'", "'Goal'", "'Constant'", 
                     "'Action'", "'Effect'", "'Reward'", "'Policy'", "'Execute'", 
                     "'Option'", "'MarkovFeature'", "'S'", "'A'", "'if'", 
                     "'else'", "'elif'", "'in'", "'init'", "'until'", "'and'", 
                     "'or'", "'not'", "'True'", "'False'", "':='", "'='", 
                     "'*='", "'/='", "'+='", "'-='", "'=='", "'>='", "'<='", 
                     "'!='", "':'", "','", "'['", "']'", "'('", "')'", "'<'", 
                     "'>'", "'*'", "'/'", "'+'", "'-'", "'''" ]

    symbolicNames = [ "<INVALID>", "INDENT", "DEDENT", "NL", "PREDICATE", 
                      "FEATURE", "FACTOR", "GOAL", "CONSTANT", "ACTION", 
                      "EFFECT", "REWARD", "POLICY", "EXECUTE", "OPTION", 
                      "MARKOVFEATURE", "S", "A", "IF", "ELSE", "ELIF", "IN", 
                      "INIT", "UNTIL", "AND", "OR", "NOT", "TRUE", "FALSE", 
                      "BIND", "ASIGN", "TIMES_EQ", "DIV_EQ", "PLUS_EQ", 
                      "MINUS_EQ", "EQUALS", "GT_EQ", "LT_EQ", "NOT_EQ", 
                      "COL", "COM", "L_BRK", "R_BRK", "L_PAR", "R_PAR", 
                      "LT", "GT", "TIMES", "DIVIDE", "PLUS", "MINUS", "PRIME", 
                      "IDENTIFIER", "DECIMAL", "INTEGER", "SKIP_" ]

    RULE_program = 0
    RULE_dec = 1
    RULE_predicate = 2
    RULE_feature = 3
    RULE_factor = 4
    RULE_goal = 5
    RULE_action = 6
    RULE_effect = 7
    RULE_option = 8
    RULE_policy = 9
    RULE_markov_feature = 10
    RULE_effect_stat = 11
    RULE_policy_stat = 12
    RULE_reward = 13
    RULE_constant = 14
    RULE_assignment = 15
    RULE_execute = 16
    RULE_boolean_exp = 17
    RULE_arithmetic_exp = 18
    RULE_temporal_identifier = 19
    RULE_trailer = 20
    RULE_array_exp = 21

    ruleNames =  [ "program", "dec", "predicate", "feature", "factor", "goal", 
                   "action", "effect", "option", "policy", "markov_feature", 
                   "effect_stat", "policy_stat", "reward", "constant", "assignment", 
                   "execute", "boolean_exp", "arithmetic_exp", "temporal_identifier", 
                   "trailer", "array_exp" ]

    EOF = Token.EOF
    INDENT=1
    DEDENT=2
    NL=3
    PREDICATE=4
    FEATURE=5
    FACTOR=6
    GOAL=7
    CONSTANT=8
    ACTION=9
    EFFECT=10
    REWARD=11
    POLICY=12
    EXECUTE=13
    OPTION=14
    MARKOVFEATURE=15
    S=16
    A=17
    IF=18
    ELSE=19
    ELIF=20
    IN=21
    INIT=22
    UNTIL=23
    AND=24
    OR=25
    NOT=26
    TRUE=27
    FALSE=28
    BIND=29
    ASIGN=30
    TIMES_EQ=31
    DIV_EQ=32
    PLUS_EQ=33
    MINUS_EQ=34
    EQUALS=35
    GT_EQ=36
    LT_EQ=37
    NOT_EQ=38
    COL=39
    COM=40
    L_BRK=41
    R_BRK=42
    L_PAR=43
    R_PAR=44
    LT=45
    GT=46
    TIMES=47
    DIVIDE=48
    PLUS=49
    MINUS=50
    PRIME=51
    IDENTIFIER=52
    DECIMAL=53
    INTEGER=54
    SKIP_=55

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

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.NL)
            else:
                return self.getToken(RLangParser.NL, i)

        def dec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.DecContext)
            else:
                return self.getTypedRuleContext(RLangParser.DecContext,i)


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
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.NL:
                self.state = 44
                self.match(RLangParser.NL)
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RLangParser.PREDICATE) | (1 << RLangParser.FEATURE) | (1 << RLangParser.FACTOR) | (1 << RLangParser.GOAL) | (1 << RLangParser.CONSTANT) | (1 << RLangParser.ACTION) | (1 << RLangParser.EFFECT) | (1 << RLangParser.POLICY) | (1 << RLangParser.OPTION) | (1 << RLangParser.MARKOVFEATURE))) != 0):
                self.state = 50
                self.dec()
                self.state = 52 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 51
                    self.match(RLangParser.NL)
                    self.state = 54 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RLangParser.NL):
                        break

                self.state = 60
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

        def predicate(self):
            return self.getTypedRuleContext(RLangParser.PredicateContext,0)


        def feature(self):
            return self.getTypedRuleContext(RLangParser.FeatureContext,0)


        def factor(self):
            return self.getTypedRuleContext(RLangParser.FactorContext,0)


        def goal(self):
            return self.getTypedRuleContext(RLangParser.GoalContext,0)


        def action(self):
            return self.getTypedRuleContext(RLangParser.ActionContext,0)


        def effect(self):
            return self.getTypedRuleContext(RLangParser.EffectContext,0)


        def constant(self):
            return self.getTypedRuleContext(RLangParser.ConstantContext,0)


        def option(self):
            return self.getTypedRuleContext(RLangParser.OptionContext,0)


        def policy(self):
            return self.getTypedRuleContext(RLangParser.PolicyContext,0)


        def markov_feature(self):
            return self.getTypedRuleContext(RLangParser.Markov_featureContext,0)


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
        self.enterRule(localctx, 2, self.RULE_dec)
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.PREDICATE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.predicate()
                pass
            elif token in [RLangParser.FEATURE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.feature()
                pass
            elif token in [RLangParser.FACTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 63
                self.factor()
                pass
            elif token in [RLangParser.GOAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 64
                self.goal()
                pass
            elif token in [RLangParser.ACTION]:
                self.enterOuterAlt(localctx, 5)
                self.state = 65
                self.action()
                pass
            elif token in [RLangParser.EFFECT]:
                self.enterOuterAlt(localctx, 6)
                self.state = 66
                self.effect()
                pass
            elif token in [RLangParser.CONSTANT]:
                self.enterOuterAlt(localctx, 7)
                self.state = 67
                self.constant()
                pass
            elif token in [RLangParser.OPTION]:
                self.enterOuterAlt(localctx, 8)
                self.state = 68
                self.option()
                pass
            elif token in [RLangParser.POLICY]:
                self.enterOuterAlt(localctx, 9)
                self.state = 69
                self.policy()
                pass
            elif token in [RLangParser.MARKOVFEATURE]:
                self.enterOuterAlt(localctx, 10)
                self.state = 70
                self.markov_feature()
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
        self.enterRule(localctx, 4, self.RULE_predicate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(RLangParser.PREDICATE)
            self.state = 74
            self.match(RLangParser.IDENTIFIER)
            self.state = 75
            self.match(RLangParser.BIND)
            self.state = 76
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
        self.enterRule(localctx, 6, self.RULE_feature)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(RLangParser.FEATURE)
            self.state = 79
            self.match(RLangParser.IDENTIFIER)
            self.state = 80
            self.match(RLangParser.BIND)
            self.state = 81
            self.arithmetic_exp(0)
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

        def S(self):
            return self.getToken(RLangParser.S, 0)

        def trailer(self):
            return self.getTypedRuleContext(RLangParser.TrailerContext,0)


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
        self.enterRule(localctx, 8, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(RLangParser.FACTOR)
            self.state = 84
            self.match(RLangParser.IDENTIFIER)
            self.state = 85
            self.match(RLangParser.BIND)
            self.state = 86
            self.match(RLangParser.S)
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.L_BRK:
                self.state = 87
                self.trailer()


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
        self.enterRule(localctx, 10, self.RULE_goal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(RLangParser.GOAL)
            self.state = 91
            self.match(RLangParser.IDENTIFIER)
            self.state = 92
            self.match(RLangParser.BIND)
            self.state = 93
            self.boolean_exp(0)
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

        def INTEGER(self):
            return self.getToken(RLangParser.INTEGER, 0)

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
            self.state = 95
            self.match(RLangParser.ACTION)
            self.state = 96
            self.match(RLangParser.IDENTIFIER)
            self.state = 97
            self.match(RLangParser.BIND)
            self.state = 98
            self.match(RLangParser.INTEGER)
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

        def boolean_exp(self):
            return self.getTypedRuleContext(RLangParser.Boolean_expContext,0)


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
            return RLangParser.RULE_effect

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEffect" ):
                listener.enterEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEffect" ):
                listener.exitEffect(self)




    def effect(self):

        localctx = RLangParser.EffectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_effect)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(RLangParser.EFFECT)
            self.state = 101
            self.boolean_exp(0)
            self.state = 102
            self.match(RLangParser.COL)
            self.state = 103
            self.match(RLangParser.INDENT)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RLangParser.CONSTANT) | (1 << RLangParser.REWARD) | (1 << RLangParser.IDENTIFIER))) != 0):
                self.state = 104
                self.effect_stat()
                self.state = 106 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 105
                    self.match(RLangParser.NL)
                    self.state = 108 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RLangParser.NL):
                        break

                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 115
            self.match(RLangParser.DEDENT)
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

        def boolean_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Boolean_expContext)
            else:
                return self.getTypedRuleContext(RLangParser.Boolean_expContext,i)


        def DEDENT(self):
            return self.getToken(RLangParser.DEDENT, 0)

        def UNTIL(self):
            return self.getToken(RLangParser.UNTIL, 0)

        def policy_stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Policy_statContext)
            else:
                return self.getTypedRuleContext(RLangParser.Policy_statContext,i)


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
        self.enterRule(localctx, 16, self.RULE_option)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(RLangParser.OPTION)
            self.state = 118
            self.match(RLangParser.IDENTIFIER)
            self.state = 119
            self.match(RLangParser.COL)
            self.state = 120
            self.match(RLangParser.INDENT)
            self.state = 121
            self.match(RLangParser.INIT)
            self.state = 122
            self.boolean_exp(0)
            self.state = 123
            self.match(RLangParser.INDENT)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.EXECUTE or _la==RLangParser.IF:
                self.state = 124
                self.policy_stat()
                self.state = 126 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 125
                    self.match(RLangParser.NL)
                    self.state = 128 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RLangParser.NL):
                        break

                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 135
            self.match(RLangParser.DEDENT)
            self.state = 136
            self.match(RLangParser.UNTIL)
            self.state = 137
            self.boolean_exp(0)
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

        def DEDENT(self):
            return self.getToken(RLangParser.DEDENT, 0)

        def policy_stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Policy_statContext)
            else:
                return self.getTypedRuleContext(RLangParser.Policy_statContext,i)


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
        self.enterRule(localctx, 18, self.RULE_policy)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(RLangParser.POLICY)
            self.state = 140
            self.match(RLangParser.IDENTIFIER)
            self.state = 141
            self.match(RLangParser.COL)
            self.state = 142
            self.match(RLangParser.INDENT)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.EXECUTE or _la==RLangParser.IF:
                self.state = 143
                self.policy_stat()
                self.state = 145 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 144
                    self.match(RLangParser.NL)
                    self.state = 147 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==RLangParser.NL):
                        break

                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 154
            self.match(RLangParser.DEDENT)
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

        def boolean_exp(self):
            return self.getTypedRuleContext(RLangParser.Boolean_expContext,0)


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
        self.enterRule(localctx, 20, self.RULE_markov_feature)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(RLangParser.MARKOVFEATURE)
            self.state = 157
            self.match(RLangParser.IDENTIFIER)
            self.state = 158
            self.match(RLangParser.BIND)
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 159
                self.boolean_exp(0)
                pass

            elif la_ == 2:
                self.state = 160
                self.arithmetic_exp(0)
                pass


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

        def reward(self):
            return self.getTypedRuleContext(RLangParser.RewardContext,0)


        def assignment(self):
            return self.getTypedRuleContext(RLangParser.AssignmentContext,0)


        def constant(self):
            return self.getTypedRuleContext(RLangParser.ConstantContext,0)


        def getRuleIndex(self):
            return RLangParser.RULE_effect_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEffect_stat" ):
                listener.enterEffect_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEffect_stat" ):
                listener.exitEffect_stat(self)




    def effect_stat(self):

        localctx = RLangParser.Effect_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_effect_stat)
        try:
            self.state = 166
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.REWARD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.reward()
                pass
            elif token in [RLangParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.assignment()
                pass
            elif token in [RLangParser.CONSTANT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 165
                self.constant()
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


    class Policy_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def execute(self):
            return self.getTypedRuleContext(RLangParser.ExecuteContext,0)


        def IF(self):
            return self.getToken(RLangParser.IF, 0)

        def boolean_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Boolean_expContext)
            else:
                return self.getTypedRuleContext(RLangParser.Boolean_expContext,i)


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

        def policy_stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Policy_statContext)
            else:
                return self.getTypedRuleContext(RLangParser.Policy_statContext,i)


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

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.NL)
            else:
                return self.getToken(RLangParser.NL, i)

        def getRuleIndex(self):
            return RLangParser.RULE_policy_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPolicy_stat" ):
                listener.enterPolicy_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPolicy_stat" ):
                listener.exitPolicy_stat(self)




    def policy_stat(self):

        localctx = RLangParser.Policy_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_policy_stat)
        self._la = 0 # Token type
        try:
            self.state = 227
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.EXECUTE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.execute()
                pass
            elif token in [RLangParser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.match(RLangParser.IF)
                self.state = 170
                self.boolean_exp(0)
                self.state = 171
                self.match(RLangParser.COL)
                self.state = 172
                self.match(RLangParser.INDENT)
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.EXECUTE or _la==RLangParser.IF:
                    self.state = 173
                    self.policy_stat()
                    self.state = 175 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 174
                        self.match(RLangParser.NL)
                        self.state = 177 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==RLangParser.NL):
                            break

                    self.state = 183
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 184
                self.match(RLangParser.DEDENT)
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.ELIF:
                    self.state = 185
                    self.match(RLangParser.ELIF)
                    self.state = 186
                    self.boolean_exp(0)
                    self.state = 187
                    self.match(RLangParser.COL)
                    self.state = 188
                    self.match(RLangParser.INDENT)
                    self.state = 197
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==RLangParser.EXECUTE or _la==RLangParser.IF:
                        self.state = 189
                        self.policy_stat()
                        self.state = 191 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 190
                            self.match(RLangParser.NL)
                            self.state = 193 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not (_la==RLangParser.NL):
                                break

                        self.state = 199
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 200
                    self.match(RLangParser.DEDENT)
                    self.state = 206
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.ELSE:
                    self.state = 207
                    self.match(RLangParser.ELSE)
                    self.state = 208
                    self.match(RLangParser.COL)
                    self.state = 209
                    self.match(RLangParser.INDENT)
                    self.state = 218
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==RLangParser.EXECUTE or _la==RLangParser.IF:
                        self.state = 210
                        self.policy_stat()
                        self.state = 212 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 211
                            self.match(RLangParser.NL)
                            self.state = 214 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not (_la==RLangParser.NL):
                                break

                        self.state = 220
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 221
                    self.match(RLangParser.DEDENT)
                    self.state = 226
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

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

        def DECIMAL(self):
            return self.getToken(RLangParser.DECIMAL, 0)

        def INTEGER(self):
            return self.getToken(RLangParser.INTEGER, 0)

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
        self.enterRule(localctx, 26, self.RULE_reward)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(RLangParser.REWARD)
            self.state = 230
            _la = self._input.LA(1)
            if not(_la==RLangParser.DECIMAL or _la==RLangParser.INTEGER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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

        def boolean_exp(self):
            return self.getTypedRuleContext(RLangParser.Boolean_expContext,0)


        def arithmetic_exp(self):
            return self.getTypedRuleContext(RLangParser.Arithmetic_expContext,0)


        def array_exp(self):
            return self.getTypedRuleContext(RLangParser.Array_expContext,0)


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
        self.enterRule(localctx, 28, self.RULE_constant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(RLangParser.CONSTANT)
            self.state = 233
            self.match(RLangParser.IDENTIFIER)
            self.state = 234
            self.match(RLangParser.BIND)
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 235
                self.boolean_exp(0)
                pass

            elif la_ == 2:
                self.state = 236
                self.arithmetic_exp(0)
                pass

            elif la_ == 3:
                self.state = 237
                self.array_exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(RLangParser.IDENTIFIER, 0)

        def ASIGN(self):
            return self.getToken(RLangParser.ASIGN, 0)

        def TIMES_EQ(self):
            return self.getToken(RLangParser.TIMES_EQ, 0)

        def DIV_EQ(self):
            return self.getToken(RLangParser.DIV_EQ, 0)

        def PLUS_EQ(self):
            return self.getToken(RLangParser.PLUS_EQ, 0)

        def MINUS_EQ(self):
            return self.getToken(RLangParser.MINUS_EQ, 0)

        def boolean_exp(self):
            return self.getTypedRuleContext(RLangParser.Boolean_expContext,0)


        def arithmetic_exp(self):
            return self.getTypedRuleContext(RLangParser.Arithmetic_expContext,0)


        def array_exp(self):
            return self.getTypedRuleContext(RLangParser.Array_expContext,0)


        def trailer(self):
            return self.getTypedRuleContext(RLangParser.TrailerContext,0)


        def getRuleIndex(self):
            return RLangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = RLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(RLangParser.IDENTIFIER)
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.L_BRK:
                self.state = 241
                self.trailer()


            self.state = 244
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RLangParser.ASIGN) | (1 << RLangParser.TIMES_EQ) | (1 << RLangParser.DIV_EQ) | (1 << RLangParser.PLUS_EQ) | (1 << RLangParser.MINUS_EQ))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 245
                self.boolean_exp(0)
                pass

            elif la_ == 2:
                self.state = 246
                self.arithmetic_exp(0)
                pass

            elif la_ == 3:
                self.state = 247
                self.array_exp()
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
            self.state = 250
            self.match(RLangParser.EXECUTE)
            self.state = 251
            self.match(RLangParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_PAR(self):
            return self.getToken(RLangParser.L_PAR, 0)

        def boolean_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Boolean_expContext)
            else:
                return self.getTypedRuleContext(RLangParser.Boolean_expContext,i)


        def R_PAR(self):
            return self.getToken(RLangParser.R_PAR, 0)

        def NOT(self):
            return self.getToken(RLangParser.NOT, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.IDENTIFIER)
            else:
                return self.getToken(RLangParser.IDENTIFIER, i)

        def IN(self):
            return self.getToken(RLangParser.IN, 0)

        def trailer(self):
            return self.getTypedRuleContext(RLangParser.TrailerContext,0)


        def A(self):
            return self.getToken(RLangParser.A, 0)

        def EQUALS(self):
            return self.getToken(RLangParser.EQUALS, 0)

        def NOT_EQ(self):
            return self.getToken(RLangParser.NOT_EQ, 0)

        def arithmetic_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Arithmetic_expContext)
            else:
                return self.getTypedRuleContext(RLangParser.Arithmetic_expContext,i)


        def LT(self):
            return self.getToken(RLangParser.LT, 0)

        def GT(self):
            return self.getToken(RLangParser.GT, 0)

        def LT_EQ(self):
            return self.getToken(RLangParser.LT_EQ, 0)

        def GT_EQ(self):
            return self.getToken(RLangParser.GT_EQ, 0)

        def TRUE(self):
            return self.getToken(RLangParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(RLangParser.FALSE, 0)

        def temporal_identifier(self):
            return self.getTypedRuleContext(RLangParser.Temporal_identifierContext,0)


        def AND(self):
            return self.getToken(RLangParser.AND, 0)

        def OR(self):
            return self.getToken(RLangParser.OR, 0)

        def getRuleIndex(self):
            return RLangParser.RULE_boolean_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean_exp" ):
                listener.enterBoolean_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean_exp" ):
                listener.exitBoolean_exp(self)



    def boolean_exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RLangParser.Boolean_expContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_boolean_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 254
                self.match(RLangParser.L_PAR)
                self.state = 255
                self.boolean_exp(0)
                self.state = 256
                self.match(RLangParser.R_PAR)
                pass

            elif la_ == 2:
                self.state = 258
                self.match(RLangParser.NOT)
                self.state = 259
                self.boolean_exp(9)
                pass

            elif la_ == 3:
                self.state = 260
                self.match(RLangParser.IDENTIFIER)
                self.state = 261
                self.match(RLangParser.IN)
                self.state = 262
                self.match(RLangParser.IDENTIFIER)
                self.state = 264
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 263
                    self.trailer()


                pass

            elif la_ == 4:
                self.state = 266
                self.match(RLangParser.A)
                self.state = 267
                _la = self._input.LA(1)
                if not(_la==RLangParser.EQUALS or _la==RLangParser.NOT_EQ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 268
                self.match(RLangParser.IDENTIFIER)
                pass

            elif la_ == 5:
                self.state = 269
                self.arithmetic_exp(0)
                self.state = 270
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RLangParser.EQUALS) | (1 << RLangParser.GT_EQ) | (1 << RLangParser.LT_EQ) | (1 << RLangParser.NOT_EQ) | (1 << RLangParser.LT) | (1 << RLangParser.GT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 271
                self.arithmetic_exp(0)
                pass

            elif la_ == 6:
                self.state = 273
                _la = self._input.LA(1)
                if not(_la==RLangParser.TRUE or _la==RLangParser.FALSE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 7:
                self.state = 276
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                if la_ == 1:
                    self.state = 274
                    self.match(RLangParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 275
                    self.temporal_identifier()
                    pass


                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 289
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        localctx = RLangParser.Boolean_expContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_exp)
                        self.state = 280
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 281
                        self.match(RLangParser.AND)
                        self.state = 282
                        self.boolean_exp(9)
                        pass

                    elif la_ == 2:
                        localctx = RLangParser.Boolean_expContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_exp)
                        self.state = 283
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 284
                        self.match(RLangParser.OR)
                        self.state = 285
                        self.boolean_exp(8)
                        pass

                    elif la_ == 3:
                        localctx = RLangParser.Boolean_expContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_exp)
                        self.state = 286
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 287
                        _la = self._input.LA(1)
                        if not(_la==RLangParser.EQUALS or _la==RLangParser.NOT_EQ):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 288
                        self.boolean_exp(5)
                        pass

             
                self.state = 293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Arithmetic_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_PAR(self):
            return self.getToken(RLangParser.L_PAR, 0)

        def arithmetic_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Arithmetic_expContext)
            else:
                return self.getTypedRuleContext(RLangParser.Arithmetic_expContext,i)


        def R_PAR(self):
            return self.getToken(RLangParser.R_PAR, 0)

        def DECIMAL(self):
            return self.getToken(RLangParser.DECIMAL, 0)

        def INTEGER(self):
            return self.getToken(RLangParser.INTEGER, 0)

        def MINUS(self):
            return self.getToken(RLangParser.MINUS, 0)

        def IDENTIFIER(self):
            return self.getToken(RLangParser.IDENTIFIER, 0)

        def temporal_identifier(self):
            return self.getTypedRuleContext(RLangParser.Temporal_identifierContext,0)


        def trailer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.TrailerContext)
            else:
                return self.getTypedRuleContext(RLangParser.TrailerContext,i)


        def TIMES(self):
            return self.getToken(RLangParser.TIMES, 0)

        def DIVIDE(self):
            return self.getToken(RLangParser.DIVIDE, 0)

        def PLUS(self):
            return self.getToken(RLangParser.PLUS, 0)

        def getRuleIndex(self):
            return RLangParser.RULE_arithmetic_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic_exp" ):
                listener.enterArithmetic_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic_exp" ):
                listener.exitArithmetic_exp(self)



    def arithmetic_exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RLangParser.Arithmetic_expContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_arithmetic_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.L_PAR]:
                self.state = 295
                self.match(RLangParser.L_PAR)
                self.state = 296
                self.arithmetic_exp(0)
                self.state = 297
                self.match(RLangParser.R_PAR)
                pass
            elif token in [RLangParser.MINUS, RLangParser.DECIMAL, RLangParser.INTEGER]:
                self.state = 300
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==RLangParser.MINUS:
                    self.state = 299
                    self.match(RLangParser.MINUS)


                self.state = 302
                _la = self._input.LA(1)
                if not(_la==RLangParser.DECIMAL or _la==RLangParser.INTEGER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [RLangParser.IDENTIFIER]:
                self.state = 305
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                if la_ == 1:
                    self.state = 303
                    self.match(RLangParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 304
                    self.temporal_identifier()
                    pass


                self.state = 310
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 307
                        self.trailer() 
                    self.state = 312
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 323
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 321
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        localctx = RLangParser.Arithmetic_expContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_exp)
                        self.state = 315
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 316
                        _la = self._input.LA(1)
                        if not(_la==RLangParser.TIMES or _la==RLangParser.DIVIDE):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 317
                        self.arithmetic_exp(5)
                        pass

                    elif la_ == 2:
                        localctx = RLangParser.Arithmetic_expContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_exp)
                        self.state = 318
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 319
                        _la = self._input.LA(1)
                        if not(_la==RLangParser.PLUS or _la==RLangParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 320
                        self.arithmetic_exp(4)
                        pass

             
                self.state = 325
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Temporal_identifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(RLangParser.IDENTIFIER, 0)

        def PRIME(self):
            return self.getToken(RLangParser.PRIME, 0)

        def getRuleIndex(self):
            return RLangParser.RULE_temporal_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemporal_identifier" ):
                listener.enterTemporal_identifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemporal_identifier" ):
                listener.exitTemporal_identifier(self)




    def temporal_identifier(self):

        localctx = RLangParser.Temporal_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_temporal_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(RLangParser.IDENTIFIER)
            self.state = 327
            self.match(RLangParser.PRIME)
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

        def L_BRK(self):
            return self.getToken(RLangParser.L_BRK, 0)

        def INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.INTEGER)
            else:
                return self.getToken(RLangParser.INTEGER, i)

        def R_BRK(self):
            return self.getToken(RLangParser.R_BRK, 0)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.MINUS)
            else:
                return self.getToken(RLangParser.MINUS, i)

        def COM(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.COM)
            else:
                return self.getToken(RLangParser.COM, i)

        def COL(self):
            return self.getToken(RLangParser.COL, 0)

        def getRuleIndex(self):
            return RLangParser.RULE_trailer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrailer" ):
                listener.enterTrailer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrailer" ):
                listener.exitTrailer(self)




    def trailer(self):

        localctx = RLangParser.TrailerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_trailer)
        self._la = 0 # Token type
        try:
            self.state = 360
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 329
                self.match(RLangParser.L_BRK)
                self.state = 331
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==RLangParser.MINUS:
                    self.state = 330
                    self.match(RLangParser.MINUS)


                self.state = 333
                self.match(RLangParser.INTEGER)
                self.state = 341
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.COM:
                    self.state = 334
                    self.match(RLangParser.COM)
                    self.state = 336
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==RLangParser.MINUS:
                        self.state = 335
                        self.match(RLangParser.MINUS)


                    self.state = 338
                    self.match(RLangParser.INTEGER)
                    self.state = 343
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 344
                self.match(RLangParser.R_BRK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
                self.match(RLangParser.L_BRK)
                self.state = 350
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==RLangParser.MINUS or _la==RLangParser.INTEGER:
                    self.state = 347
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==RLangParser.MINUS:
                        self.state = 346
                        self.match(RLangParser.MINUS)


                    self.state = 349
                    self.match(RLangParser.INTEGER)


                self.state = 352
                self.match(RLangParser.COL)
                self.state = 357
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==RLangParser.MINUS or _la==RLangParser.INTEGER:
                    self.state = 354
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==RLangParser.MINUS:
                        self.state = 353
                        self.match(RLangParser.MINUS)


                    self.state = 356
                    self.match(RLangParser.INTEGER)


                self.state = 359
                self.match(RLangParser.R_BRK)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRK(self):
            return self.getToken(RLangParser.L_BRK, 0)

        def INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.INTEGER)
            else:
                return self.getToken(RLangParser.INTEGER, i)

        def R_BRK(self):
            return self.getToken(RLangParser.R_BRK, 0)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.MINUS)
            else:
                return self.getToken(RLangParser.MINUS, i)

        def COM(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.COM)
            else:
                return self.getToken(RLangParser.COM, i)

        def getRuleIndex(self):
            return RLangParser.RULE_array_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_exp" ):
                listener.enterArray_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_exp" ):
                listener.exitArray_exp(self)




    def array_exp(self):

        localctx = RLangParser.Array_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_array_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.match(RLangParser.L_BRK)
            self.state = 364
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.MINUS:
                self.state = 363
                self.match(RLangParser.MINUS)


            self.state = 366
            self.match(RLangParser.INTEGER)
            self.state = 374
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.COM:
                self.state = 367
                self.match(RLangParser.COM)
                self.state = 369
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==RLangParser.MINUS:
                    self.state = 368
                    self.match(RLangParser.MINUS)


                self.state = 371
                self.match(RLangParser.INTEGER)
                self.state = 376
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 377
            self.match(RLangParser.R_BRK)
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
        self._predicates[17] = self.boolean_exp_sempred
        self._predicates[18] = self.arithmetic_exp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def boolean_exp_sempred(self, localctx:Boolean_expContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

    def arithmetic_exp_sempred(self, localctx:Arithmetic_expContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         




