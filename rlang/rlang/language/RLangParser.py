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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3Q")
        buf.write("\u028c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\7\2f\n\2\f\2\16")
        buf.write("\2i\13\2\3\2\3\2\3\2\7\2n\n\2\f\2\16\2q\13\2\3\3\3\3\6")
        buf.write("\3u\n\3\r\3\16\3v\7\3y\n\3\f\3\16\3|\13\3\3\4\3\4\3\4")
        buf.write("\3\5\7\5\u0082\n\5\f\5\16\5\u0085\13\5\3\6\3\6\6\6\u0089")
        buf.write("\n\6\r\6\16\6\u008a\3\6\3\6\6\6\u008f\n\6\r\6\16\6\u0090")
        buf.write("\3\6\3\6\6\6\u0095\n\6\r\6\16\6\u0096\3\6\3\6\6\6\u009b")
        buf.write("\n\6\r\6\16\6\u009c\3\6\3\6\6\6\u00a1\n\6\r\6\16\6\u00a2")
        buf.write("\3\6\3\6\6\6\u00a7\n\6\r\6\16\6\u00a8\3\6\3\6\6\6\u00ad")
        buf.write("\n\6\r\6\16\6\u00ae\3\6\3\6\6\6\u00b3\n\6\r\6\16\6\u00b4")
        buf.write("\3\6\3\6\3\6\5\6\u00ba\n\6\3\7\3\7\3\7\3\7\3\7\5\7\u00c1")
        buf.write("\n\7\3\b\3\b\3\b\3\b\3\b\5\b\u00c8\n\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\7\17\u00ec\n\17\f\17\16\17")
        buf.write("\u00ef\13\17\6\17\u00f1\n\17\r\17\16\17\u00f2\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\7\21\u0102\n\21\f\21\16\21\u0105\13\21\3\21\3\21\3\21")
        buf.write("\3\21\7\21\u010b\n\21\f\21\16\21\u010e\13\21\3\21\3\21")
        buf.write("\3\22\3\22\5\22\u0114\n\22\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\7\23\u011c\n\23\f\23\16\23\u011f\13\23\3\23\3\23\3")
        buf.write("\24\3\24\3\24\5\24\u0126\n\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\7\25\u012e\n\25\f\25\16\25\u0131\13\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\7\25\u013a\n\25\f\25\16\25\u013d")
        buf.write("\13\25\3\25\3\25\7\25\u0141\n\25\f\25\16\25\u0144\13\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\7\25\u014b\n\25\f\25\16\25\u014e")
        buf.write("\13\25\3\25\3\25\5\25\u0152\n\25\3\26\3\26\3\26\7\26\u0157")
        buf.write("\n\26\f\26\16\26\u015a\13\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\7\27\u0161\n\27\f\27\16\27\u0164\13\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\6\27\u016b\n\27\r\27\16\27\u016c\5\27\u016f")
        buf.write("\n\27\3\30\3\30\3\30\5\30\u0174\n\30\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\32\3\32\7\32\u017f\n\32\f\32\16\32")
        buf.write("\u0182\13\32\6\32\u0184\n\32\r\32\16\32\u0185\3\33\3\33")
        buf.write("\3\33\3\33\3\33\5\33\u018d\n\33\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u019c")
        buf.write("\n\34\f\34\16\34\u019f\13\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\5\34\u01a7\n\34\3\35\3\35\3\35\7\35\u01ac\n\35\f")
        buf.write("\35\16\35\u01af\13\35\3\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\36\5\36\u01ba\n\36\3\36\3\36\6\36\u01be\n\36")
        buf.write("\r\36\16\36\u01bf\5\36\u01c2\n\36\3\37\3\37\3\37\3 \3")
        buf.write(" \5 \u01c9\n \3 \5 \u01cc\n \3 \3 \3 \3!\3!\3!\3\"\3\"")
        buf.write("\3\"\3\"\3\"\5\"\u01d9\n\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\5#\u01e5\n#\3#\3#\3#\3#\3#\3#\7#\u01ed\n#\f#\16#")
        buf.write("\u01f0\13#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\5$\u0203\n$\3$\3$\3$\3$\3$\3$\3$\3$\3$\7$\u020e")
        buf.write("\n$\f$\16$\u0211\13$\3%\3%\5%\u0215\n%\3&\3&\3&\3&\5&")
        buf.write("\u021b\n&\3&\3&\5&\u021f\n&\3&\3&\3&\3&\5&\u0225\n&\3")
        buf.write("&\3&\5&\u0229\n&\5&\u022b\n&\3\'\3\'\3(\3(\5(\u0231\n")
        buf.write("(\3(\7(\u0234\n(\f(\16(\u0237\13(\3(\3(\5(\u023b\n(\3")
        buf.write("(\3(\5(\u023f\n(\3(\5(\u0242\n(\3)\3)\5)\u0246\n)\3*\3")
        buf.write("*\5*\u024a\n*\3+\3+\3+\3+\3+\7+\u0251\n+\f+\16+\u0254")
        buf.write("\13+\3+\3+\5+\u0258\n+\3,\3,\3,\3,\7,\u025e\n,\f,\16,")
        buf.write("\u0261\13,\3,\3,\3-\3-\3-\3-\7-\u0269\n-\f-\16-\u026c")
        buf.write("\13-\3-\3-\3.\3.\5.\u0272\n.\3.\3.\5.\u0276\n.\3.\3.\3")
        buf.write("/\3/\3/\3/\3\60\3\60\5\60\u0280\n\60\3\61\5\61\u0283\n")
        buf.write("\61\3\61\3\61\3\62\5\62\u0288\n\62\3\62\3\62\3\62\2\4")
        buf.write("DF\63\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.")
        buf.write("\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`b\2\t\4\2**LL\3\2FG")
        buf.write("\3\2HI\4\28;DE\3\2./\4\288;;\4\2\26\30\33\33\2\u02ba\2")
        buf.write("g\3\2\2\2\4z\3\2\2\2\6}\3\2\2\2\b\u0083\3\2\2\2\n\u00b9")
        buf.write("\3\2\2\2\f\u00bb\3\2\2\2\16\u00c2\3\2\2\2\20\u00c9\3\2")
        buf.write("\2\2\22\u00ce\3\2\2\2\24\u00d3\3\2\2\2\26\u00d8\3\2\2")
        buf.write("\2\30\u00dd\3\2\2\2\32\u00e2\3\2\2\2\34\u00f0\3\2\2\2")
        buf.write("\36\u00f4\3\2\2\2 \u00f8\3\2\2\2\"\u0113\3\2\2\2$\u0115")
        buf.write("\3\2\2\2&\u0125\3\2\2\2(\u0127\3\2\2\2*\u0153\3\2\2\2")
        buf.write(",\u016e\3\2\2\2.\u0170\3\2\2\2\60\u0175\3\2\2\2\62\u0183")
        buf.write("\3\2\2\2\64\u018c\3\2\2\2\66\u018e\3\2\2\28\u01a8\3\2")
        buf.write("\2\2:\u01c1\3\2\2\2<\u01c3\3\2\2\2>\u01cb\3\2\2\2@\u01d0")
        buf.write("\3\2\2\2B\u01d3\3\2\2\2D\u01e4\3\2\2\2F\u0202\3\2\2\2")
        buf.write("H\u0214\3\2\2\2J\u022a\3\2\2\2L\u022c\3\2\2\2N\u0241\3")
        buf.write("\2\2\2P\u0245\3\2\2\2R\u0249\3\2\2\2T\u0257\3\2\2\2V\u0259")
        buf.write("\3\2\2\2X\u0264\3\2\2\2Z\u026f\3\2\2\2\\\u0279\3\2\2\2")
        buf.write("^\u027f\3\2\2\2`\u0282\3\2\2\2b\u0287\3\2\2\2df\7\5\2")
        buf.write("\2ed\3\2\2\2fi\3\2\2\2ge\3\2\2\2gh\3\2\2\2hj\3\2\2\2i")
        buf.write("g\3\2\2\2jk\5\4\3\2ko\5\b\5\2ln\7\5\2\2ml\3\2\2\2nq\3")
        buf.write("\2\2\2om\3\2\2\2op\3\2\2\2p\3\3\2\2\2qo\3\2\2\2rt\5\6")
        buf.write("\4\2su\7\5\2\2ts\3\2\2\2uv\3\2\2\2vt\3\2\2\2vw\3\2\2\2")
        buf.write("wy\3\2\2\2xr\3\2\2\2y|\3\2\2\2zx\3\2\2\2z{\3\2\2\2{\5")
        buf.write("\3\2\2\2|z\3\2\2\2}~\7\6\2\2~\177\7K\2\2\177\7\3\2\2\2")
        buf.write("\u0080\u0082\5\n\6\2\u0081\u0080\3\2\2\2\u0082\u0085\3")
        buf.write("\2\2\2\u0083\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084\t")
        buf.write("\3\2\2\2\u0085\u0083\3\2\2\2\u0086\u0088\5\f\7\2\u0087")
        buf.write("\u0089\7\5\2\2\u0088\u0087\3\2\2\2\u0089\u008a\3\2\2\2")
        buf.write("\u008a\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u00ba\3")
        buf.write("\2\2\2\u008c\u008e\5\16\b\2\u008d\u008f\7\5\2\2\u008e")
        buf.write("\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u008e\3\2\2\2")
        buf.write("\u0090\u0091\3\2\2\2\u0091\u00ba\3\2\2\2\u0092\u0094\5")
        buf.write("\20\t\2\u0093\u0095\7\5\2\2\u0094\u0093\3\2\2\2\u0095")
        buf.write("\u0096\3\2\2\2\u0096\u0094\3\2\2\2\u0096\u0097\3\2\2\2")
        buf.write("\u0097\u00ba\3\2\2\2\u0098\u009a\5\22\n\2\u0099\u009b")
        buf.write("\7\5\2\2\u009a\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c")
        buf.write("\u009a\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u00ba\3\2\2\2")
        buf.write("\u009e\u00a0\5\32\16\2\u009f\u00a1\7\5\2\2\u00a0\u009f")
        buf.write("\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2")
        buf.write("\u00a3\3\2\2\2\u00a3\u00ba\3\2\2\2\u00a4\u00a6\5\24\13")
        buf.write("\2\u00a5\u00a7\7\5\2\2\u00a6\u00a5\3\2\2\2\u00a7\u00a8")
        buf.write("\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9")
        buf.write("\u00ba\3\2\2\2\u00aa\u00ac\5\26\f\2\u00ab\u00ad\7\5\2")
        buf.write("\2\u00ac\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00ac")
        buf.write("\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00ba\3\2\2\2\u00b0")
        buf.write("\u00b2\5\30\r\2\u00b1\u00b3\7\5\2\2\u00b2\u00b1\3\2\2")
        buf.write("\2\u00b3\u00b4\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5")
        buf.write("\3\2\2\2\u00b5\u00ba\3\2\2\2\u00b6\u00ba\5 \21\2\u00b7")
        buf.write("\u00ba\5$\23\2\u00b8\u00ba\5\60\31\2\u00b9\u0086\3\2\2")
        buf.write("\2\u00b9\u008c\3\2\2\2\u00b9\u0092\3\2\2\2\u00b9\u0098")
        buf.write("\3\2\2\2\u00b9\u009e\3\2\2\2\u00b9\u00a4\3\2\2\2\u00b9")
        buf.write("\u00aa\3\2\2\2\u00b9\u00b0\3\2\2\2\u00b9\u00b6\3\2\2\2")
        buf.write("\u00b9\u00b7\3\2\2\2\u00b9\u00b8\3\2\2\2\u00ba\13\3\2")
        buf.write("\2\2\u00bb\u00bc\7\16\2\2\u00bc\u00bd\7L\2\2\u00bd\u00c0")
        buf.write("\7\61\2\2\u00be\u00c1\5D#\2\u00bf\u00c1\5F$\2\u00c0\u00be")
        buf.write("\3\2\2\2\u00c0\u00bf\3\2\2\2\u00c1\r\3\2\2\2\u00c2\u00c3")
        buf.write("\7\17\2\2\u00c3\u00c4\7L\2\2\u00c4\u00c7\7\61\2\2\u00c5")
        buf.write("\u00c8\5^\60\2\u00c6\u00c8\5X-\2\u00c7\u00c5\3\2\2\2\u00c7")
        buf.write("\u00c6\3\2\2\2\u00c8\17\3\2\2\2\u00c9\u00ca\7\n\2\2\u00ca")
        buf.write("\u00cb\7L\2\2\u00cb\u00cc\7\61\2\2\u00cc\u00cd\5N(\2\u00cd")
        buf.write("\21\3\2\2\2\u00ce\u00cf\7\7\2\2\u00cf\u00d0\7L\2\2\u00d0")
        buf.write("\u00d1\7\61\2\2\u00d1\u00d2\5F$\2\u00d2\23\3\2\2\2\u00d3")
        buf.write("\u00d4\7\13\2\2\u00d4\u00d5\7L\2\2\u00d5\u00d6\7\61\2")
        buf.write("\2\u00d6\u00d7\5F$\2\u00d7\25\3\2\2\2\u00d8\u00d9\7\t")
        buf.write("\2\2\u00d9\u00da\7L\2\2\u00da\u00db\7\61\2\2\u00db\u00dc")
        buf.write("\5D#\2\u00dc\27\3\2\2\2\u00dd\u00de\7\25\2\2\u00de\u00df")
        buf.write("\7L\2\2\u00df\u00e0\7\61\2\2\u00e0\u00e1\5D#\2\u00e1\31")
        buf.write("\3\2\2\2\u00e2\u00e3\7\f\2\2\u00e3\u00e4\7L\2\2\u00e4")
        buf.write("\u00e5\7<\2\2\u00e5\u00e6\7\3\2\2\u00e6\u00e7\5\34\17")
        buf.write("\2\u00e7\u00e8\7\4\2\2\u00e8\33\3\2\2\2\u00e9\u00ed\5")
        buf.write("\36\20\2\u00ea\u00ec\7\5\2\2\u00eb\u00ea\3\2\2\2\u00ec")
        buf.write("\u00ef\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2")
        buf.write("\u00ee\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2\u00f0\u00e9\3")
        buf.write("\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f3")
        buf.write("\3\2\2\2\u00f3\35\3\2\2\2\u00f4\u00f5\7L\2\2\u00f5\u00f6")
        buf.write("\7<\2\2\u00f6\u00f7\5H%\2\u00f7\37\3\2\2\2\u00f8\u00f9")
        buf.write("\7\24\2\2\u00f9\u00fa\7L\2\2\u00fa\u00fb\7<\2\2\u00fb")
        buf.write("\u00fc\7\3\2\2\u00fc\u00fd\7%\2\2\u00fd\u00fe\5\"\22\2")
        buf.write("\u00fe\u00ff\7\3\2\2\u00ff\u0103\5&\24\2\u0100\u0102\7")
        buf.write("\5\2\2\u0101\u0100\3\2\2\2\u0102\u0105\3\2\2\2\u0103\u0101")
        buf.write("\3\2\2\2\u0103\u0104\3\2\2\2\u0104\u0106\3\2\2\2\u0105")
        buf.write("\u0103\3\2\2\2\u0106\u0107\7\4\2\2\u0107\u0108\7&\2\2")
        buf.write("\u0108\u010c\5\"\22\2\u0109\u010b\7\5\2\2\u010a\u0109")
        buf.write("\3\2\2\2\u010b\u010e\3\2\2\2\u010c\u010a\3\2\2\2\u010c")
        buf.write("\u010d\3\2\2\2\u010d\u010f\3\2\2\2\u010e\u010c\3\2\2\2")
        buf.write("\u010f\u0110\7\4\2\2\u0110!\3\2\2\2\u0111\u0114\5F$\2")
        buf.write("\u0112\u0114\7\60\2\2\u0113\u0111\3\2\2\2\u0113\u0112")
        buf.write("\3\2\2\2\u0114#\3\2\2\2\u0115\u0116\7\22\2\2\u0116\u0117")
        buf.write("\t\2\2\2\u0117\u0118\7<\2\2\u0118\u0119\7\3\2\2\u0119")
        buf.write("\u011d\5&\24\2\u011a\u011c\7\5\2\2\u011b\u011a\3\2\2\2")
        buf.write("\u011c\u011f\3\2\2\2\u011d\u011b\3\2\2\2\u011d\u011e\3")
        buf.write("\2\2\2\u011e\u0120\3\2\2\2\u011f\u011d\3\2\2\2\u0120\u0121")
        buf.write("\7\4\2\2\u0121%\3\2\2\2\u0122\u0126\5.\30\2\u0123\u0126")
        buf.write("\5(\25\2\u0124\u0126\5*\26\2\u0125\u0122\3\2\2\2\u0125")
        buf.write("\u0123\3\2\2\2\u0125\u0124\3\2\2\2\u0126\'\3\2\2\2\u0127")
        buf.write("\u0128\7!\2\2\u0128\u0129\5F$\2\u0129\u012a\7<\2\2\u012a")
        buf.write("\u012b\7\3\2\2\u012b\u012f\5&\24\2\u012c\u012e\7\5\2\2")
        buf.write("\u012d\u012c\3\2\2\2\u012e\u0131\3\2\2\2\u012f\u012d\3")
        buf.write("\2\2\2\u012f\u0130\3\2\2\2\u0130\u0132\3\2\2\2\u0131\u012f")
        buf.write("\3\2\2\2\u0132\u0142\7\4\2\2\u0133\u0134\7#\2\2\u0134")
        buf.write("\u0135\5F$\2\u0135\u0136\7<\2\2\u0136\u0137\7\3\2\2\u0137")
        buf.write("\u013b\5&\24\2\u0138\u013a\7\5\2\2\u0139\u0138\3\2\2\2")
        buf.write("\u013a\u013d\3\2\2\2\u013b\u0139\3\2\2\2\u013b\u013c\3")
        buf.write("\2\2\2\u013c\u013e\3\2\2\2\u013d\u013b\3\2\2\2\u013e\u013f")
        buf.write("\7\4\2\2\u013f\u0141\3\2\2\2\u0140\u0133\3\2\2\2\u0141")
        buf.write("\u0144\3\2\2\2\u0142\u0140\3\2\2\2\u0142\u0143\3\2\2\2")
        buf.write("\u0143\u0151\3\2\2\2\u0144\u0142\3\2\2\2\u0145\u0146\7")
        buf.write("\"\2\2\u0146\u0147\7<\2\2\u0147\u0148\7\3\2\2\u0148\u014c")
        buf.write("\5&\24\2\u0149\u014b\7\5\2\2\u014a\u0149\3\2\2\2\u014b")
        buf.write("\u014e\3\2\2\2\u014c\u014a\3\2\2\2\u014c\u014d\3\2\2\2")
        buf.write("\u014d\u014f\3\2\2\2\u014e\u014c\3\2\2\2\u014f\u0150\7")
        buf.write("\4\2\2\u0150\u0152\3\2\2\2\u0151\u0145\3\2\2\2\u0151\u0152")
        buf.write("\3\2\2\2\u0152)\3\2\2\2\u0153\u0158\5,\27\2\u0154\u0155")
        buf.write("\7,\2\2\u0155\u0157\5,\27\2\u0156\u0154\3\2\2\2\u0157")
        buf.write("\u015a\3\2\2\2\u0158\u0156\3\2\2\2\u0158\u0159\3\2\2\2")
        buf.write("\u0159+\3\2\2\2\u015a\u0158\3\2\2\2\u015b\u015c\5B\"\2")
        buf.write("\u015c\u015d\7<\2\2\u015d\u015e\7\3\2\2\u015e\u0162\5")
        buf.write("&\24\2\u015f\u0161\7\5\2\2\u0160\u015f\3\2\2\2\u0161\u0164")
        buf.write("\3\2\2\2\u0162\u0160\3\2\2\2\u0162\u0163\3\2\2\2\u0163")
        buf.write("\u0165\3\2\2\2\u0164\u0162\3\2\2\2\u0165\u0166\7\4\2\2")
        buf.write("\u0166\u016f\3\2\2\2\u0167\u0168\5.\30\2\u0168\u016a\5")
        buf.write("B\"\2\u0169\u016b\7\5\2\2\u016a\u0169\3\2\2\2\u016b\u016c")
        buf.write("\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016d")
        buf.write("\u016f\3\2\2\2\u016e\u015b\3\2\2\2\u016e\u0167\3\2\2\2")
        buf.write("\u016f-\3\2\2\2\u0170\u0173\7\23\2\2\u0171\u0174\7L\2")
        buf.write("\2\u0172\u0174\5D#\2\u0173\u0171\3\2\2\2\u0173\u0172\3")
        buf.write("\2\2\2\u0174/\3\2\2\2\u0175\u0176\7\20\2\2\u0176\u0177")
        buf.write("\t\2\2\2\u0177\u0178\7<\2\2\u0178\u0179\7\3\2\2\u0179")
        buf.write("\u017a\5\62\32\2\u017a\u017b\7\4\2\2\u017b\61\3\2\2\2")
        buf.write("\u017c\u0180\5\64\33\2\u017d\u017f\7\5\2\2\u017e\u017d")
        buf.write("\3\2\2\2\u017f\u0182\3\2\2\2\u0180\u017e\3\2\2\2\u0180")
        buf.write("\u0181\3\2\2\2\u0181\u0184\3\2\2\2\u0182\u0180\3\2\2\2")
        buf.write("\u0183\u017c\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0183\3")
        buf.write("\2\2\2\u0185\u0186\3\2\2\2\u0186\63\3\2\2\2\u0187\u018d")
        buf.write("\5<\37\2\u0188\u018d\5> \2\u0189\u018d\5@!\2\u018a\u018d")
        buf.write("\5\66\34\2\u018b\u018d\58\35\2\u018c\u0187\3\2\2\2\u018c")
        buf.write("\u0188\3\2\2\2\u018c\u0189\3\2\2\2\u018c\u018a\3\2\2\2")
        buf.write("\u018c\u018b\3\2\2\2\u018d\65\3\2\2\2\u018e\u018f\7!\2")
        buf.write("\2\u018f\u0190\5F$\2\u0190\u0191\7<\2\2\u0191\u0192\7")
        buf.write("\3\2\2\u0192\u0193\5\62\32\2\u0193\u019d\7\4\2\2\u0194")
        buf.write("\u0195\7#\2\2\u0195\u0196\5F$\2\u0196\u0197\7<\2\2\u0197")
        buf.write("\u0198\7\3\2\2\u0198\u0199\5\62\32\2\u0199\u019a\7\4\2")
        buf.write("\2\u019a\u019c\3\2\2\2\u019b\u0194\3\2\2\2\u019c\u019f")
        buf.write("\3\2\2\2\u019d\u019b\3\2\2\2\u019d\u019e\3\2\2\2\u019e")
        buf.write("\u01a6\3\2\2\2\u019f\u019d\3\2\2\2\u01a0\u01a1\7\"\2\2")
        buf.write("\u01a1\u01a2\7<\2\2\u01a2\u01a3\7\3\2\2\u01a3\u01a4\5")
        buf.write("\62\32\2\u01a4\u01a5\7\4\2\2\u01a5\u01a7\3\2\2\2\u01a6")
        buf.write("\u01a0\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\67\3\2\2\2\u01a8")
        buf.write("\u01ad\5:\36\2\u01a9\u01aa\7,\2\2\u01aa\u01ac\5:\36\2")
        buf.write("\u01ab\u01a9\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad\u01ab\3")
        buf.write("\2\2\2\u01ad\u01ae\3\2\2\2\u01ae9\3\2\2\2\u01af\u01ad")
        buf.write("\3\2\2\2\u01b0\u01b1\5B\"\2\u01b1\u01b2\7<\2\2\u01b2\u01b3")
        buf.write("\7\3\2\2\u01b3\u01b4\5\62\32\2\u01b4\u01b5\7\4\2\2\u01b5")
        buf.write("\u01c2\3\2\2\2\u01b6\u01ba\5<\37\2\u01b7\u01ba\5> \2\u01b8")
        buf.write("\u01ba\5@!\2\u01b9\u01b6\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9")
        buf.write("\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bd\5B\"\2")
        buf.write("\u01bc\u01be\7\5\2\2\u01bd\u01bc\3\2\2\2\u01be\u01bf\3")
        buf.write("\2\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c2")
        buf.write("\3\2\2\2\u01c1\u01b0\3\2\2\2\u01c1\u01b9\3\2\2\2\u01c2")
        buf.write(";\3\2\2\2\u01c3\u01c4\7\21\2\2\u01c4\u01c5\5D#\2\u01c5")
        buf.write("=\3\2\2\2\u01c6\u01c8\7L\2\2\u01c7\u01c9\7 \2\2\u01c8")
        buf.write("\u01c7\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01cc\3\2\2\2")
        buf.write("\u01ca\u01cc\7\34\2\2\u01cb\u01c6\3\2\2\2\u01cb\u01ca")
        buf.write("\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01ce\7\62\2\2\u01ce")
        buf.write("\u01cf\5D#\2\u01cf?\3\2\2\2\u01d0\u01d1\7\62\2\2\u01d1")
        buf.write("\u01d2\7L\2\2\u01d2A\3\2\2\2\u01d3\u01d4\7\'\2\2\u01d4")
        buf.write("\u01d5\7\37\2\2\u01d5\u01d8\7B\2\2\u01d6\u01d9\5^\60\2")
        buf.write("\u01d7\u01d9\5\\/\2\u01d8\u01d6\3\2\2\2\u01d8\u01d7\3")
        buf.write("\2\2\2\u01d9\u01da\3\2\2\2\u01da\u01db\7C\2\2\u01dbC\3")
        buf.write("\2\2\2\u01dc\u01dd\b#\1\2\u01dd\u01de\7B\2\2\u01de\u01df")
        buf.write("\5D#\2\u01df\u01e0\7C\2\2\u01e0\u01e5\3\2\2\2\u01e1\u01e5")
        buf.write("\5^\60\2\u01e2\u01e5\5R*\2\u01e3\u01e5\5N(\2\u01e4\u01dc")
        buf.write("\3\2\2\2\u01e4\u01e1\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e4")
        buf.write("\u01e3\3\2\2\2\u01e5\u01ee\3\2\2\2\u01e6\u01e7\f\7\2\2")
        buf.write("\u01e7\u01e8\t\3\2\2\u01e8\u01ed\5D#\b\u01e9\u01ea\f\6")
        buf.write("\2\2\u01ea\u01eb\t\4\2\2\u01eb\u01ed\5D#\7\u01ec\u01e6")
        buf.write("\3\2\2\2\u01ec\u01e9\3\2\2\2\u01ed\u01f0\3\2\2\2\u01ee")
        buf.write("\u01ec\3\2\2\2\u01ee\u01ef\3\2\2\2\u01efE\3\2\2\2\u01f0")
        buf.write("\u01ee\3\2\2\2\u01f1\u01f2\b$\1\2\u01f2\u01f3\7B\2\2\u01f3")
        buf.write("\u01f4\5F$\2\u01f4\u01f5\7C\2\2\u01f5\u0203\3\2\2\2\u01f6")
        buf.write("\u01f7\7-\2\2\u01f7\u0203\5F$\b\u01f8\u01f9\5D#\2\u01f9")
        buf.write("\u01fa\7$\2\2\u01fa\u01fb\5D#\2\u01fb\u0203\3\2\2\2\u01fc")
        buf.write("\u01fd\5D#\2\u01fd\u01fe\t\5\2\2\u01fe\u01ff\5D#\2\u01ff")
        buf.write("\u0203\3\2\2\2\u0200\u0203\5N(\2\u0201\u0203\t\6\2\2\u0202")
        buf.write("\u01f1\3\2\2\2\u0202\u01f6\3\2\2\2\u0202\u01f8\3\2\2\2")
        buf.write("\u0202\u01fc\3\2\2\2\u0202\u0200\3\2\2\2\u0202\u0201\3")
        buf.write("\2\2\2\u0203\u020f\3\2\2\2\u0204\u0205\f\n\2\2\u0205\u0206")
        buf.write("\7+\2\2\u0206\u020e\5F$\13\u0207\u0208\f\t\2\2\u0208\u0209")
        buf.write("\7,\2\2\u0209\u020e\5F$\n\u020a\u020b\f\6\2\2\u020b\u020c")
        buf.write("\t\7\2\2\u020c\u020e\5F$\7\u020d\u0204\3\2\2\2\u020d\u0207")
        buf.write("\3\2\2\2\u020d\u020a\3\2\2\2\u020e\u0211\3\2\2\2\u020f")
        buf.write("\u020d\3\2\2\2\u020f\u0210\3\2\2\2\u0210G\3\2\2\2\u0211")
        buf.write("\u020f\3\2\2\2\u0212\u0215\5J&\2\u0213\u0215\5L\'\2\u0214")
        buf.write("\u0212\3\2\2\2\u0214\u0213\3\2\2\2\u0215I\3\2\2\2\u0216")
        buf.write("\u021e\7\31\2\2\u0217\u021a\7>\2\2\u0218\u021b\5L\'\2")
        buf.write("\u0219\u021b\5J&\2\u021a\u0218\3\2\2\2\u021a\u0219\3\2")
        buf.write("\2\2\u021b\u021c\3\2\2\2\u021c\u021d\7?\2\2\u021d\u021f")
        buf.write("\3\2\2\2\u021e\u0217\3\2\2\2\u021e\u021f\3\2\2\2\u021f")
        buf.write("\u022b\3\2\2\2\u0220\u0228\7\32\2\2\u0221\u0224\7>\2\2")
        buf.write("\u0222\u0225\5L\'\2\u0223\u0225\5J&\2\u0224\u0222\3\2")
        buf.write("\2\2\u0224\u0223\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0227")
        buf.write("\7?\2\2\u0227\u0229\3\2\2\2\u0228\u0221\3\2\2\2\u0228")
        buf.write("\u0229\3\2\2\2\u0229\u022b\3\2\2\2\u022a\u0216\3\2\2\2")
        buf.write("\u022a\u0220\3\2\2\2\u022bK\3\2\2\2\u022c\u022d\t\b\2")
        buf.write("\2\u022dM\3\2\2\2\u022e\u0230\7L\2\2\u022f\u0231\7 \2")
        buf.write("\2\u0230\u022f\3\2\2\2\u0230\u0231\3\2\2\2\u0231\u0235")
        buf.write("\3\2\2\2\u0232\u0234\5P)\2\u0233\u0232\3\2\2\2\u0234\u0237")
        buf.write("\3\2\2\2\u0235\u0233\3\2\2\2\u0235\u0236\3\2\2\2\u0236")
        buf.write("\u0242\3\2\2\2\u0237\u0235\3\2\2\2\u0238\u023a\7\35\2")
        buf.write("\2\u0239\u023b\5P)\2\u023a\u0239\3\2\2\2\u023a\u023b\3")
        buf.write("\2\2\2\u023b\u0242\3\2\2\2\u023c\u023e\7\34\2\2\u023d")
        buf.write("\u023f\5P)\2\u023e\u023d\3\2\2\2\u023e\u023f\3\2\2\2\u023f")
        buf.write("\u0242\3\2\2\2\u0240\u0242\7\36\2\2\u0241\u022e\3\2\2")
        buf.write("\2\u0241\u0238\3\2\2\2\u0241\u023c\3\2\2\2\u0241\u0240")
        buf.write("\3\2\2\2\u0242O\3\2\2\2\u0243\u0246\5V,\2\u0244\u0246")
        buf.write("\5Z.\2\u0245\u0243\3\2\2\2\u0245\u0244\3\2\2\2\u0246Q")
        buf.write("\3\2\2\2\u0247\u024a\5T+\2\u0248\u024a\5X-\2\u0249\u0247")
        buf.write("\3\2\2\2\u0249\u0248\3\2\2\2\u024aS\3\2\2\2\u024b\u0258")
        buf.write("\5X-\2\u024c\u024d\7>\2\2\u024d\u0252\5T+\2\u024e\u024f")
        buf.write("\7=\2\2\u024f\u0251\5T+\2\u0250\u024e\3\2\2\2\u0251\u0254")
        buf.write("\3\2\2\2\u0252\u0250\3\2\2\2\u0252\u0253\3\2\2\2\u0253")
        buf.write("\u0255\3\2\2\2\u0254\u0252\3\2\2\2\u0255\u0256\7?\2\2")
        buf.write("\u0256\u0258\3\2\2\2\u0257\u024b\3\2\2\2\u0257\u024c\3")
        buf.write("\2\2\2\u0258U\3\2\2\2\u0259\u025a\7>\2\2\u025a\u025f\5")
        buf.write("`\61\2\u025b\u025c\7=\2\2\u025c\u025e\5`\61\2\u025d\u025b")
        buf.write("\3\2\2\2\u025e\u0261\3\2\2\2\u025f\u025d\3\2\2\2\u025f")
        buf.write("\u0260\3\2\2\2\u0260\u0262\3\2\2\2\u0261\u025f\3\2\2\2")
        buf.write("\u0262\u0263\7?\2\2\u0263W\3\2\2\2\u0264\u0265\7>\2\2")
        buf.write("\u0265\u026a\5^\60\2\u0266\u0267\7=\2\2\u0267\u0269\5")
        buf.write("^\60\2\u0268\u0266\3\2\2\2\u0269\u026c\3\2\2\2\u026a\u0268")
        buf.write("\3\2\2\2\u026a\u026b\3\2\2\2\u026b\u026d\3\2\2\2\u026c")
        buf.write("\u026a\3\2\2\2\u026d\u026e\7?\2\2\u026eY\3\2\2\2\u026f")
        buf.write("\u0271\7>\2\2\u0270\u0272\5`\61\2\u0271\u0270\3\2\2\2")
        buf.write("\u0271\u0272\3\2\2\2\u0272\u0273\3\2\2\2\u0273\u0275\7")
        buf.write("<\2\2\u0274\u0276\5`\61\2\u0275\u0274\3\2\2\2\u0275\u0276")
        buf.write("\3\2\2\2\u0276\u0277\3\2\2\2\u0277\u0278\7?\2\2\u0278")
        buf.write("[\3\2\2\2\u0279\u027a\5`\61\2\u027a\u027b\7G\2\2\u027b")
        buf.write("\u027c\5`\61\2\u027c]\3\2\2\2\u027d\u0280\5`\61\2\u027e")
        buf.write("\u0280\5b\62\2\u027f\u027d\3\2\2\2\u027f\u027e\3\2\2\2")
        buf.write("\u0280_\3\2\2\2\u0281\u0283\7I\2\2\u0282\u0281\3\2\2\2")
        buf.write("\u0282\u0283\3\2\2\2\u0283\u0284\3\2\2\2\u0284\u0285\7")
        buf.write("N\2\2\u0285a\3\2\2\2\u0286\u0288\7I\2\2\u0287\u0286\3")
        buf.write("\2\2\2\u0287\u0288\3\2\2\2\u0288\u0289\3\2\2\2\u0289\u028a")
        buf.write("\7M\2\2\u028ac\3\2\2\2Kgovz\u0083\u008a\u0090\u0096\u009c")
        buf.write("\u00a2\u00a8\u00ae\u00b4\u00b9\u00c0\u00c7\u00ed\u00f2")
        buf.write("\u0103\u010c\u0113\u011d\u0125\u012f\u013b\u0142\u014c")
        buf.write("\u0151\u0158\u0162\u016c\u016e\u0173\u0180\u0185\u018c")
        buf.write("\u019d\u01a6\u01ad\u01b9\u01bf\u01c1\u01c8\u01cb\u01d8")
        buf.write("\u01e4\u01ec\u01ee\u0202\u020d\u020f\u0214\u021a\u021e")
        buf.write("\u0224\u0228\u022a\u0230\u0235\u023a\u023e\u0241\u0245")
        buf.write("\u0249\u0252\u0257\u025f\u026a\u0271\u0275\u027f\u0282")
        buf.write("\u0287")
        return buf.getvalue()


class RLangParser ( Parser ):

    grammarFileName = "RLangParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'import'", "'Proposition'", "'Predicate'", "'Feature'", 
                     "'Factor'", "'Goal'", "'Class'", "'Object'", "'Constant'", 
                     "'Action'", "'Effect'", "'Reward'", "'Policy'", "'Execute'", 
                     "'Option'", "'MarkovFeature'", "'int'", "'float'", 
                     "'str'", "'list'", "'set'", "'boolean'", "<INVALID>", 
                     "'S'", "'A'", "'P'", "'''", "'if'", "'else'", "'elif'", 
                     "'in'", "'init'", "'until'", "'with'", "'then'", "'never'", 
                     "'main'", "'and'", "'or'", "'not'", "'True'", "'False'", 
                     "'Any'", "':='", "'->'", "'='", "'*='", "'/='", "'+='", 
                     "'-='", "'=='", "'>='", "'<='", "'!='", "':'", "','", 
                     "'['", "']'", "'{'", "'}'", "'('", "')'", "'<'", "'>'", 
                     "'*'", "'/'", "'+'", "'-'", "'\"'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'.'" ]

    symbolicNames = [ "<INVALID>", "INDENT", "DEDENT", "NL", "IMPORT", "PROPOSITION", 
                      "PREDICATE", "FEATURE", "FACTOR", "GOAL", "CLASS", 
                      "OBJECT", "CONSTANT", "ACTION", "EFFECT", "REWARD", 
                      "POLICY", "EXECUTE", "OPTION", "MARKOVFEATURE", "INT", 
                      "FLOAT", "STR", "LIST", "SET", "BOOL", "S_PRIME", 
                      "S", "A", "P", "PRIME", "IF", "ELSE", "ELIF", "IN", 
                      "INIT", "UNTIL", "WITH", "THEN", "NEVER", "MAIN", 
                      "AND", "OR", "NOT", "TRUE", "FALSE", "ANY_CONDITION", 
                      "BIND", "PREDICT", "ASSIGN", "TIMES_EQ", "DIV_EQ", 
                      "PLUS_EQ", "MINUS_EQ", "EQ_TO", "GT_EQ", "LT_EQ", 
                      "NOT_EQ", "COL", "COM", "L_BRK", "R_BRK", "L_CBRK", 
                      "R_CBRK", "L_PAR", "R_PAR", "LT", "GT", "TIMES", "DIVIDE", 
                      "PLUS", "MINUS", "QUOTE", "FNAME", "IDENTIFIER", "DECIMAL", 
                      "INTEGER", "DOT", "SKIP_", "ANY" ]

    RULE_program = 0
    RULE_imports = 1
    RULE_import_stat = 2
    RULE_declarations = 3
    RULE_dec = 4
    RULE_constant = 5
    RULE_action = 6
    RULE_factor = 7
    RULE_proposition = 8
    RULE_goal = 9
    RULE_feature = 10
    RULE_markov_feature = 11
    RULE_class_def = 12
    RULE_attribute_definition_collection = 13
    RULE_attribute_definition = 14
    RULE_option = 15
    RULE_option_condition = 16
    RULE_policy = 17
    RULE_policy_statement = 18
    RULE_conditional_subpolicy = 19
    RULE_probabilistic_subpolicy = 20
    RULE_probabilistic_policy_statement = 21
    RULE_execute = 22
    RULE_effect = 23
    RULE_effect_statement_collection = 24
    RULE_effect_statement = 25
    RULE_conditional_effect = 26
    RULE_probabilistic_effect = 27
    RULE_probabilistic_effect_statement = 28
    RULE_reward = 29
    RULE_prediction = 30
    RULE_effect_reference = 31
    RULE_probabilistic_condition = 32
    RULE_arithmetic_exp = 33
    RULE_boolean_exp = 34
    RULE_type_def = 35
    RULE_compound_type = 36
    RULE_simple_type = 37
    RULE_any_bound_var = 38
    RULE_trailer = 39
    RULE_any_array = 40
    RULE_compound_array_exp = 41
    RULE_int_array_exp = 42
    RULE_any_num_array_exp = 43
    RULE_slice_exp = 44
    RULE_integer_fraction = 45
    RULE_any_number = 46
    RULE_any_integer = 47
    RULE_any_decimal = 48

    ruleNames =  [ "program", "imports", "import_stat", "declarations", 
                   "dec", "constant", "action", "factor", "proposition", 
                   "goal", "feature", "markov_feature", "class_def", "attribute_definition_collection", 
                   "attribute_definition", "option", "option_condition", 
                   "policy", "policy_statement", "conditional_subpolicy", 
                   "probabilistic_subpolicy", "probabilistic_policy_statement", 
                   "execute", "effect", "effect_statement_collection", "effect_statement", 
                   "conditional_effect", "probabilistic_effect", "probabilistic_effect_statement", 
                   "reward", "prediction", "effect_reference", "probabilistic_condition", 
                   "arithmetic_exp", "boolean_exp", "type_def", "compound_type", 
                   "simple_type", "any_bound_var", "trailer", "any_array", 
                   "compound_array_exp", "int_array_exp", "any_num_array_exp", 
                   "slice_exp", "integer_fraction", "any_number", "any_integer", 
                   "any_decimal" ]

    EOF = Token.EOF
    INDENT=1
    DEDENT=2
    NL=3
    IMPORT=4
    PROPOSITION=5
    PREDICATE=6
    FEATURE=7
    FACTOR=8
    GOAL=9
    CLASS=10
    OBJECT=11
    CONSTANT=12
    ACTION=13
    EFFECT=14
    REWARD=15
    POLICY=16
    EXECUTE=17
    OPTION=18
    MARKOVFEATURE=19
    INT=20
    FLOAT=21
    STR=22
    LIST=23
    SET=24
    BOOL=25
    S_PRIME=26
    S=27
    A=28
    P=29
    PRIME=30
    IF=31
    ELSE=32
    ELIF=33
    IN=34
    INIT=35
    UNTIL=36
    WITH=37
    THEN=38
    NEVER=39
    MAIN=40
    AND=41
    OR=42
    NOT=43
    TRUE=44
    FALSE=45
    ANY_CONDITION=46
    BIND=47
    PREDICT=48
    ASSIGN=49
    TIMES_EQ=50
    DIV_EQ=51
    PLUS_EQ=52
    MINUS_EQ=53
    EQ_TO=54
    GT_EQ=55
    LT_EQ=56
    NOT_EQ=57
    COL=58
    COM=59
    L_BRK=60
    R_BRK=61
    L_CBRK=62
    R_CBRK=63
    L_PAR=64
    R_PAR=65
    LT=66
    GT=67
    TIMES=68
    DIVIDE=69
    PLUS=70
    MINUS=71
    QUOTE=72
    FNAME=73
    IDENTIFIER=74
    DECIMAL=75
    INTEGER=76
    DOT=77
    SKIP_=78
    ANY=79

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
            self.state = 101
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 98
                    self.match(RLangParser.NL) 
                self.state = 103
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 104
            self.imports()
            self.state = 105
            self.declarations()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.NL:
                self.state = 106
                self.match(RLangParser.NL)
                self.state = 111
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
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.IMPORT:
                self.state = 112
                self.import_stat()
                self.state = 114 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 113
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 116 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                self.state = 122
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
            self.state = 123
            self.match(RLangParser.IMPORT)
            self.state = 124
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
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RLangParser.PROPOSITION) | (1 << RLangParser.FEATURE) | (1 << RLangParser.FACTOR) | (1 << RLangParser.GOAL) | (1 << RLangParser.CLASS) | (1 << RLangParser.CONSTANT) | (1 << RLangParser.ACTION) | (1 << RLangParser.EFFECT) | (1 << RLangParser.POLICY) | (1 << RLangParser.OPTION) | (1 << RLangParser.MARKOVFEATURE))) != 0):
                self.state = 126
                self.dec()
                self.state = 131
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


        def proposition(self):
            return self.getTypedRuleContext(RLangParser.PropositionContext,0)


        def class_def(self):
            return self.getTypedRuleContext(RLangParser.Class_defContext,0)


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
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.CONSTANT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.constant()
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
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                pass
            elif token in [RLangParser.ACTION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.action()
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
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                pass
            elif token in [RLangParser.FACTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 144
                self.factor()
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
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                pass
            elif token in [RLangParser.PROPOSITION]:
                self.enterOuterAlt(localctx, 4)
                self.state = 150
                self.proposition()
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
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                pass
            elif token in [RLangParser.CLASS]:
                self.enterOuterAlt(localctx, 5)
                self.state = 156
                self.class_def()
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
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                pass
            elif token in [RLangParser.GOAL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 162
                self.goal()
                self.state = 164 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 163
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 166 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                pass
            elif token in [RLangParser.FEATURE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 168
                self.feature()
                self.state = 170 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 169
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 172 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                pass
            elif token in [RLangParser.MARKOVFEATURE]:
                self.enterOuterAlt(localctx, 8)
                self.state = 174
                self.markov_feature()
                self.state = 176 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 175
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 178 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                pass
            elif token in [RLangParser.OPTION]:
                self.enterOuterAlt(localctx, 9)
                self.state = 180
                self.option()
                pass
            elif token in [RLangParser.POLICY]:
                self.enterOuterAlt(localctx, 10)
                self.state = 181
                self.policy()
                pass
            elif token in [RLangParser.EFFECT]:
                self.enterOuterAlt(localctx, 11)
                self.state = 182
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
            self.state = 185
            self.match(RLangParser.CONSTANT)
            self.state = 186
            self.match(RLangParser.IDENTIFIER)
            self.state = 187
            self.match(RLangParser.BIND)
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 188
                self.arithmetic_exp(0)
                pass

            elif la_ == 2:
                self.state = 189
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
            self.state = 192
            self.match(RLangParser.ACTION)
            self.state = 193
            self.match(RLangParser.IDENTIFIER)
            self.state = 194
            self.match(RLangParser.BIND)
            self.state = 197
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.MINUS, RLangParser.DECIMAL, RLangParser.INTEGER]:
                self.state = 195
                self.any_number()
                pass
            elif token in [RLangParser.L_BRK]:
                self.state = 196
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
            self.state = 199
            self.match(RLangParser.FACTOR)
            self.state = 200
            self.match(RLangParser.IDENTIFIER)
            self.state = 201
            self.match(RLangParser.BIND)
            self.state = 202
            self.any_bound_var()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropositionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROPOSITION(self):
            return self.getToken(RLangParser.PROPOSITION, 0)

        def IDENTIFIER(self):
            return self.getToken(RLangParser.IDENTIFIER, 0)

        def BIND(self):
            return self.getToken(RLangParser.BIND, 0)

        def boolean_exp(self):
            return self.getTypedRuleContext(RLangParser.Boolean_expContext,0)


        def getRuleIndex(self):
            return RLangParser.RULE_proposition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProposition" ):
                listener.enterProposition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProposition" ):
                listener.exitProposition(self)




    def proposition(self):

        localctx = RLangParser.PropositionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_proposition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(RLangParser.PROPOSITION)
            self.state = 205
            self.match(RLangParser.IDENTIFIER)
            self.state = 206
            self.match(RLangParser.BIND)
            self.state = 207
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
            self.state = 209
            self.match(RLangParser.GOAL)
            self.state = 210
            self.match(RLangParser.IDENTIFIER)
            self.state = 211
            self.match(RLangParser.BIND)
            self.state = 212
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
            self.state = 214
            self.match(RLangParser.FEATURE)
            self.state = 215
            self.match(RLangParser.IDENTIFIER)
            self.state = 216
            self.match(RLangParser.BIND)
            self.state = 217
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
            self.state = 219
            self.match(RLangParser.MARKOVFEATURE)
            self.state = 220
            self.match(RLangParser.IDENTIFIER)
            self.state = 221
            self.match(RLangParser.BIND)
            self.state = 222
            self.arithmetic_exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(RLangParser.CLASS, 0)

        def IDENTIFIER(self):
            return self.getToken(RLangParser.IDENTIFIER, 0)

        def COL(self):
            return self.getToken(RLangParser.COL, 0)

        def INDENT(self):
            return self.getToken(RLangParser.INDENT, 0)

        def attribute_definition_collection(self):
            return self.getTypedRuleContext(RLangParser.Attribute_definition_collectionContext,0)


        def DEDENT(self):
            return self.getToken(RLangParser.DEDENT, 0)

        def getRuleIndex(self):
            return RLangParser.RULE_class_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_def" ):
                listener.enterClass_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_def" ):
                listener.exitClass_def(self)




    def class_def(self):

        localctx = RLangParser.Class_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_class_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(RLangParser.CLASS)
            self.state = 225
            self.match(RLangParser.IDENTIFIER)
            self.state = 226
            self.match(RLangParser.COL)
            self.state = 227
            self.match(RLangParser.INDENT)
            self.state = 228
            self.attribute_definition_collection()
            self.state = 229
            self.match(RLangParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_definition_collectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._attribute_definition = None # Attribute_definitionContext
            self.definitions = list() # of Attribute_definitionContexts

        def attribute_definition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Attribute_definitionContext)
            else:
                return self.getTypedRuleContext(RLangParser.Attribute_definitionContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.NL)
            else:
                return self.getToken(RLangParser.NL, i)

        def getRuleIndex(self):
            return RLangParser.RULE_attribute_definition_collection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute_definition_collection" ):
                listener.enterAttribute_definition_collection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute_definition_collection" ):
                listener.exitAttribute_definition_collection(self)




    def attribute_definition_collection(self):

        localctx = RLangParser.Attribute_definition_collectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_attribute_definition_collection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 231
                localctx._attribute_definition = self.attribute_definition()
                localctx.definitions.append(localctx._attribute_definition)
                self.state = 235
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.NL:
                    self.state = 232
                    self.match(RLangParser.NL)
                    self.state = 237
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 240 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==RLangParser.IDENTIFIER):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(RLangParser.IDENTIFIER, 0)

        def COL(self):
            return self.getToken(RLangParser.COL, 0)

        def type_def(self):
            return self.getTypedRuleContext(RLangParser.Type_defContext,0)


        def getRuleIndex(self):
            return RLangParser.RULE_attribute_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute_definition" ):
                listener.enterAttribute_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute_definition" ):
                listener.exitAttribute_definition(self)




    def attribute_definition(self):

        localctx = RLangParser.Attribute_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_attribute_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(RLangParser.IDENTIFIER)
            self.state = 243
            self.match(RLangParser.COL)
            self.state = 244
            self.type_def()
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
        self.enterRule(localctx, 30, self.RULE_option)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(RLangParser.OPTION)
            self.state = 247
            self.match(RLangParser.IDENTIFIER)
            self.state = 248
            self.match(RLangParser.COL)
            self.state = 249
            self.match(RLangParser.INDENT)
            self.state = 250
            self.match(RLangParser.INIT)
            self.state = 251
            localctx.init = self.option_condition()
            self.state = 252
            self.match(RLangParser.INDENT)
            self.state = 253
            self.policy_statement()
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.NL:
                self.state = 254
                self.match(RLangParser.NL)
                self.state = 259
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 260
            self.match(RLangParser.DEDENT)
            self.state = 261
            self.match(RLangParser.UNTIL)
            self.state = 262
            localctx.until = self.option_condition()
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.NL:
                self.state = 263
                self.match(RLangParser.NL)
                self.state = 268
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 269
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
        self.enterRule(localctx, 32, self.RULE_option_condition)
        try:
            self.state = 273
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.S_PRIME, RLangParser.S, RLangParser.A, RLangParser.NOT, RLangParser.TRUE, RLangParser.FALSE, RLangParser.L_BRK, RLangParser.L_PAR, RLangParser.MINUS, RLangParser.IDENTIFIER, RLangParser.DECIMAL, RLangParser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.boolean_exp(0)
                pass
            elif token in [RLangParser.ANY_CONDITION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 272
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

        def COL(self):
            return self.getToken(RLangParser.COL, 0)

        def INDENT(self):
            return self.getToken(RLangParser.INDENT, 0)

        def policy_statement(self):
            return self.getTypedRuleContext(RLangParser.Policy_statementContext,0)


        def DEDENT(self):
            return self.getToken(RLangParser.DEDENT, 0)

        def IDENTIFIER(self):
            return self.getToken(RLangParser.IDENTIFIER, 0)

        def MAIN(self):
            return self.getToken(RLangParser.MAIN, 0)

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
        self.enterRule(localctx, 34, self.RULE_policy)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(RLangParser.POLICY)
            self.state = 276
            _la = self._input.LA(1)
            if not(_la==RLangParser.MAIN or _la==RLangParser.IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 277
            self.match(RLangParser.COL)
            self.state = 278
            self.match(RLangParser.INDENT)
            self.state = 279
            self.policy_statement()
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.NL:
                self.state = 280
                self.match(RLangParser.NL)
                self.state = 285
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 286
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
        self.enterRule(localctx, 36, self.RULE_policy_statement)
        try:
            self.state = 291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Policy_statement_executeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.execute()
                pass

            elif la_ == 2:
                localctx = RLangParser.Policy_statement_conditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 289
                self.conditional_subpolicy()
                pass

            elif la_ == 3:
                localctx = RLangParser.Policy_statement_probabilisticContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 290
                self.probabilistic_subpolicy()
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


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.NL)
            else:
                return self.getToken(RLangParser.NL, i)

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
        self.enterRule(localctx, 38, self.RULE_conditional_subpolicy)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(RLangParser.IF)
            self.state = 294
            localctx.if_condition = self.boolean_exp(0)
            self.state = 295
            self.match(RLangParser.COL)
            self.state = 296
            self.match(RLangParser.INDENT)
            self.state = 297
            localctx.if_subpolicy = self.policy_statement()
            self.state = 301
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.NL:
                self.state = 298
                self.match(RLangParser.NL)
                self.state = 303
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 304
            self.match(RLangParser.DEDENT)
            self.state = 320
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.ELIF:
                self.state = 305
                self.match(RLangParser.ELIF)
                self.state = 306
                localctx._boolean_exp = self.boolean_exp(0)
                localctx.elif_conditions.append(localctx._boolean_exp)
                self.state = 307
                self.match(RLangParser.COL)
                self.state = 308
                self.match(RLangParser.INDENT)
                self.state = 309
                localctx._policy_statement = self.policy_statement()
                localctx.elif_subpolicies.append(localctx._policy_statement)
                self.state = 313
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.NL:
                    self.state = 310
                    self.match(RLangParser.NL)
                    self.state = 315
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 316
                self.match(RLangParser.DEDENT)
                self.state = 322
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 335
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.ELSE:
                self.state = 323
                self.match(RLangParser.ELSE)
                self.state = 324
                self.match(RLangParser.COL)
                self.state = 325
                self.match(RLangParser.INDENT)
                self.state = 326
                localctx.else_subpolicy = self.policy_statement()
                self.state = 330
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.NL:
                    self.state = 327
                    self.match(RLangParser.NL)
                    self.state = 332
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 333
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
        self.enterRule(localctx, 40, self.RULE_probabilistic_subpolicy)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            localctx._probabilistic_policy_statement = self.probabilistic_policy_statement()
            localctx.subpolicies.append(localctx._probabilistic_policy_statement)
            self.state = 342
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.OR:
                self.state = 338
                self.match(RLangParser.OR)
                self.state = 339
                localctx._probabilistic_policy_statement = self.probabilistic_policy_statement()
                localctx.subpolicies.append(localctx._probabilistic_policy_statement)
                self.state = 344
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
        self.enterRule(localctx, 42, self.RULE_probabilistic_policy_statement)
        self._la = 0 # Token type
        try:
            self.state = 364
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.WITH]:
                localctx = RLangParser.Probabilistic_policy_statement_no_sugarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.probabilistic_condition()
                self.state = 346
                self.match(RLangParser.COL)
                self.state = 347
                self.match(RLangParser.INDENT)
                self.state = 348
                self.policy_statement()
                self.state = 352
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.NL:
                    self.state = 349
                    self.match(RLangParser.NL)
                    self.state = 354
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 355
                self.match(RLangParser.DEDENT)
                pass
            elif token in [RLangParser.EXECUTE]:
                localctx = RLangParser.Probabilistic_policy_statement_sugarContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                self.execute()
                self.state = 358
                self.probabilistic_condition()
                self.state = 360 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 359
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 362 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
        self.enterRule(localctx, 44, self.RULE_execute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.match(RLangParser.EXECUTE)
            self.state = 369
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 367
                self.match(RLangParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 368
                self.arithmetic_exp(0)
                pass


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

        def MAIN(self):
            return self.getToken(RLangParser.MAIN, 0)

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
        self.enterRule(localctx, 46, self.RULE_effect)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.match(RLangParser.EFFECT)
            self.state = 372
            _la = self._input.LA(1)
            if not(_la==RLangParser.MAIN or _la==RLangParser.IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 373
            self.match(RLangParser.COL)
            self.state = 374
            self.match(RLangParser.INDENT)
            self.state = 375
            self.effect_statement_collection()
            self.state = 376
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
        self.enterRule(localctx, 48, self.RULE_effect_statement_collection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 378
                localctx._effect_statement = self.effect_statement()
                localctx.statements.append(localctx._effect_statement)
                self.state = 382
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.NL:
                    self.state = 379
                    self.match(RLangParser.NL)
                    self.state = 384
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 387 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 15)) & ~0x3f) == 0 and ((1 << (_la - 15)) & ((1 << (RLangParser.REWARD - 15)) | (1 << (RLangParser.S_PRIME - 15)) | (1 << (RLangParser.IF - 15)) | (1 << (RLangParser.WITH - 15)) | (1 << (RLangParser.PREDICT - 15)) | (1 << (RLangParser.IDENTIFIER - 15)))) != 0)):
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
        self.enterRule(localctx, 50, self.RULE_effect_statement)
        try:
            self.state = 394
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Effect_statement_rewardContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                self.reward()
                pass

            elif la_ == 2:
                localctx = RLangParser.Effect_statement_predictionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 390
                self.prediction()
                pass

            elif la_ == 3:
                localctx = RLangParser.Effect_statement_referenceContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 391
                self.effect_reference()
                pass

            elif la_ == 4:
                localctx = RLangParser.Effect_statement_conditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 392
                self.conditional_effect()
                pass

            elif la_ == 5:
                localctx = RLangParser.Effect_statement_probabilisticContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 393
                self.probabilistic_effect()
                pass


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
            self.state = 396
            self.match(RLangParser.IF)
            self.state = 397
            localctx.if_condition = self.boolean_exp(0)
            self.state = 398
            self.match(RLangParser.COL)
            self.state = 399
            self.match(RLangParser.INDENT)
            self.state = 400
            localctx.if_effect = self.effect_statement_collection()
            self.state = 401
            self.match(RLangParser.DEDENT)
            self.state = 411
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.ELIF:
                self.state = 402
                self.match(RLangParser.ELIF)
                self.state = 403
                localctx._boolean_exp = self.boolean_exp(0)
                localctx.elif_conditions.append(localctx._boolean_exp)
                self.state = 404
                self.match(RLangParser.COL)
                self.state = 405
                self.match(RLangParser.INDENT)
                self.state = 406
                localctx._effect_statement_collection = self.effect_statement_collection()
                localctx.elif_effects.append(localctx._effect_statement_collection)
                self.state = 407
                self.match(RLangParser.DEDENT)
                self.state = 413
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 420
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.ELSE:
                self.state = 414
                self.match(RLangParser.ELSE)
                self.state = 415
                self.match(RLangParser.COL)
                self.state = 416
                self.match(RLangParser.INDENT)
                self.state = 417
                localctx.else_effect = self.effect_statement_collection()
                self.state = 418
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
            self.state = 422
            localctx._probabilistic_effect_statement = self.probabilistic_effect_statement()
            localctx.effects.append(localctx._probabilistic_effect_statement)
            self.state = 427
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.OR:
                self.state = 423
                self.match(RLangParser.OR)
                self.state = 424
                localctx._probabilistic_effect_statement = self.probabilistic_effect_statement()
                localctx.effects.append(localctx._probabilistic_effect_statement)
                self.state = 429
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
            self.state = 447
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.WITH]:
                localctx = RLangParser.Probabilistic_effect_statement_no_sugarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                self.probabilistic_condition()
                self.state = 431
                self.match(RLangParser.COL)
                self.state = 432
                self.match(RLangParser.INDENT)
                self.state = 433
                self.effect_statement_collection()
                self.state = 434
                self.match(RLangParser.DEDENT)
                pass
            elif token in [RLangParser.REWARD, RLangParser.S_PRIME, RLangParser.PREDICT, RLangParser.IDENTIFIER]:
                localctx = RLangParser.Probabilistic_effect_statement_sugarContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 439
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RLangParser.REWARD]:
                    self.state = 436
                    self.reward()
                    pass
                elif token in [RLangParser.S_PRIME, RLangParser.IDENTIFIER]:
                    self.state = 437
                    self.prediction()
                    pass
                elif token in [RLangParser.PREDICT]:
                    self.state = 438
                    self.effect_reference()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 441
                self.probabilistic_condition()
                self.state = 443 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 442
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 445 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

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
        self.enterRule(localctx, 58, self.RULE_reward)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.match(RLangParser.REWARD)
            self.state = 450
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
        self.enterRule(localctx, 60, self.RULE_prediction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.IDENTIFIER]:
                self.state = 452
                self.match(RLangParser.IDENTIFIER)
                self.state = 454
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==RLangParser.PRIME:
                    self.state = 453
                    self.match(RLangParser.PRIME)


                pass
            elif token in [RLangParser.S_PRIME]:
                self.state = 456
                self.match(RLangParser.S_PRIME)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 459
            self.match(RLangParser.PREDICT)
            self.state = 460
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
        self.enterRule(localctx, 62, self.RULE_effect_reference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.match(RLangParser.PREDICT)
            self.state = 463
            self.match(RLangParser.IDENTIFIER)
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
        self.enterRule(localctx, 64, self.RULE_probabilistic_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self.match(RLangParser.WITH)
            self.state = 466
            self.match(RLangParser.P)
            self.state = 467
            self.match(RLangParser.L_PAR)
            self.state = 470
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.state = 468
                self.any_number()
                pass

            elif la_ == 2:
                self.state = 469
                self.integer_fraction()
                pass


            self.state = 472
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
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_arithmetic_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.L_PAR]:
                localctx = RLangParser.Arith_parenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 475
                self.match(RLangParser.L_PAR)
                self.state = 476
                self.arithmetic_exp(0)
                self.state = 477
                self.match(RLangParser.R_PAR)
                pass
            elif token in [RLangParser.MINUS, RLangParser.DECIMAL, RLangParser.INTEGER]:
                localctx = RLangParser.Arith_numberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 479
                self.any_number()
                pass
            elif token in [RLangParser.L_BRK]:
                localctx = RLangParser.Arith_arrayContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 480
                self.any_array()
                pass
            elif token in [RLangParser.S_PRIME, RLangParser.S, RLangParser.A, RLangParser.IDENTIFIER]:
                localctx = RLangParser.Arith_bound_varContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 481
                self.any_bound_var()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 492
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 490
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                    if la_ == 1:
                        localctx = RLangParser.Arith_times_divideContext(self, RLangParser.Arithmetic_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_exp)
                        self.state = 484
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 485
                        _la = self._input.LA(1)
                        if not(_la==RLangParser.TIMES or _la==RLangParser.DIVIDE):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 486
                        localctx.rhs = self.arithmetic_exp(6)
                        pass

                    elif la_ == 2:
                        localctx = RLangParser.Arith_plus_minusContext(self, RLangParser.Arithmetic_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_exp)
                        self.state = 487
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 488
                        _la = self._input.LA(1)
                        if not(_la==RLangParser.PLUS or _la==RLangParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 489
                        localctx.rhs = self.arithmetic_exp(5)
                        pass

             
                self.state = 494
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

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
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_boolean_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Bool_parenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 496
                self.match(RLangParser.L_PAR)
                self.state = 497
                self.boolean_exp(0)
                self.state = 498
                self.match(RLangParser.R_PAR)
                pass

            elif la_ == 2:
                localctx = RLangParser.Bool_notContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 500
                self.match(RLangParser.NOT)
                self.state = 501
                self.boolean_exp(6)
                pass

            elif la_ == 3:
                localctx = RLangParser.Bool_inContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 502
                localctx.lhs = self.arithmetic_exp(0)
                self.state = 503
                self.match(RLangParser.IN)
                self.state = 504
                localctx.rhs = self.arithmetic_exp(0)
                pass

            elif la_ == 4:
                localctx = RLangParser.Bool_arith_eqContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 506
                localctx.lhs = self.arithmetic_exp(0)
                self.state = 507
                _la = self._input.LA(1)
                if not(((((_la - 54)) & ~0x3f) == 0 and ((1 << (_la - 54)) & ((1 << (RLangParser.EQ_TO - 54)) | (1 << (RLangParser.GT_EQ - 54)) | (1 << (RLangParser.LT_EQ - 54)) | (1 << (RLangParser.NOT_EQ - 54)) | (1 << (RLangParser.LT - 54)) | (1 << (RLangParser.GT - 54)))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 508
                localctx.rhs = self.arithmetic_exp(0)
                pass

            elif la_ == 5:
                localctx = RLangParser.Bool_bound_varContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 510
                self.any_bound_var()
                pass

            elif la_ == 6:
                localctx = RLangParser.Bool_tfContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 511
                _la = self._input.LA(1)
                if not(_la==RLangParser.TRUE or _la==RLangParser.FALSE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 525
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 523
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                    if la_ == 1:
                        localctx = RLangParser.Bool_andContext(self, RLangParser.Boolean_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_exp)
                        self.state = 514
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 515
                        self.match(RLangParser.AND)
                        self.state = 516
                        localctx.rhs = self.boolean_exp(9)
                        pass

                    elif la_ == 2:
                        localctx = RLangParser.Bool_orContext(self, RLangParser.Boolean_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_exp)
                        self.state = 517
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 518
                        self.match(RLangParser.OR)
                        self.state = 519
                        localctx.rhs = self.boolean_exp(8)
                        pass

                    elif la_ == 3:
                        localctx = RLangParser.Bool_bool_eqContext(self, RLangParser.Boolean_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_exp)
                        self.state = 520
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 521
                        _la = self._input.LA(1)
                        if not(_la==RLangParser.EQ_TO or _la==RLangParser.NOT_EQ):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 522
                        localctx.rhs = self.boolean_exp(5)
                        pass

             
                self.state = 527
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Type_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def compound_type(self):
            return self.getTypedRuleContext(RLangParser.Compound_typeContext,0)


        def simple_type(self):
            return self.getTypedRuleContext(RLangParser.Simple_typeContext,0)


        def getRuleIndex(self):
            return RLangParser.RULE_type_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_def" ):
                listener.enterType_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_def" ):
                listener.exitType_def(self)




    def type_def(self):

        localctx = RLangParser.Type_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_type_def)
        try:
            self.state = 530
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.LIST, RLangParser.SET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 528
                self.compound_type()
                pass
            elif token in [RLangParser.INT, RLangParser.FLOAT, RLangParser.STR, RLangParser.BOOL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 529
                self.simple_type()
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


    class Compound_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RLangParser.RULE_compound_type

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Type_listContext(Compound_typeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Compound_typeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LIST(self):
            return self.getToken(RLangParser.LIST, 0)
        def L_BRK(self):
            return self.getToken(RLangParser.L_BRK, 0)
        def R_BRK(self):
            return self.getToken(RLangParser.R_BRK, 0)
        def simple_type(self):
            return self.getTypedRuleContext(RLangParser.Simple_typeContext,0)

        def compound_type(self):
            return self.getTypedRuleContext(RLangParser.Compound_typeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_list" ):
                listener.enterType_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_list" ):
                listener.exitType_list(self)


    class Type_setContext(Compound_typeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Compound_typeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SET(self):
            return self.getToken(RLangParser.SET, 0)
        def L_BRK(self):
            return self.getToken(RLangParser.L_BRK, 0)
        def R_BRK(self):
            return self.getToken(RLangParser.R_BRK, 0)
        def simple_type(self):
            return self.getTypedRuleContext(RLangParser.Simple_typeContext,0)

        def compound_type(self):
            return self.getTypedRuleContext(RLangParser.Compound_typeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_set" ):
                listener.enterType_set(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_set" ):
                listener.exitType_set(self)



    def compound_type(self):

        localctx = RLangParser.Compound_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_compound_type)
        self._la = 0 # Token type
        try:
            self.state = 552
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.LIST]:
                localctx = RLangParser.Type_listContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 532
                self.match(RLangParser.LIST)
                self.state = 540
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==RLangParser.L_BRK:
                    self.state = 533
                    self.match(RLangParser.L_BRK)
                    self.state = 536
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [RLangParser.INT, RLangParser.FLOAT, RLangParser.STR, RLangParser.BOOL]:
                        self.state = 534
                        self.simple_type()
                        pass
                    elif token in [RLangParser.LIST, RLangParser.SET]:
                        self.state = 535
                        self.compound_type()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 538
                    self.match(RLangParser.R_BRK)


                pass
            elif token in [RLangParser.SET]:
                localctx = RLangParser.Type_setContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 542
                self.match(RLangParser.SET)
                self.state = 550
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==RLangParser.L_BRK:
                    self.state = 543
                    self.match(RLangParser.L_BRK)
                    self.state = 546
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [RLangParser.INT, RLangParser.FLOAT, RLangParser.STR, RLangParser.BOOL]:
                        self.state = 544
                        self.simple_type()
                        pass
                    elif token in [RLangParser.LIST, RLangParser.SET]:
                        self.state = 545
                        self.compound_type()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 548
                    self.match(RLangParser.R_BRK)


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


    class Simple_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(RLangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(RLangParser.FLOAT, 0)

        def STR(self):
            return self.getToken(RLangParser.STR, 0)

        def BOOL(self):
            return self.getToken(RLangParser.BOOL, 0)

        def getRuleIndex(self):
            return RLangParser.RULE_simple_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_type" ):
                listener.enterSimple_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_type" ):
                listener.exitSimple_type(self)




    def simple_type(self):

        localctx = RLangParser.Simple_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_simple_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 554
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RLangParser.INT) | (1 << RLangParser.FLOAT) | (1 << RLangParser.STR) | (1 << RLangParser.BOOL))) != 0)):
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
        self.enterRule(localctx, 76, self.RULE_any_bound_var)
        try:
            self.state = 575
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.IDENTIFIER]:
                localctx = RLangParser.Bound_identifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 556
                self.match(RLangParser.IDENTIFIER)
                self.state = 558
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
                if la_ == 1:
                    self.state = 557
                    self.match(RLangParser.PRIME)


                self.state = 563
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,58,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 560
                        self.trailer() 
                    self.state = 565
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,58,self._ctx)

                pass
            elif token in [RLangParser.S]:
                localctx = RLangParser.Bound_stateContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 566
                self.match(RLangParser.S)
                self.state = 568
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
                if la_ == 1:
                    self.state = 567
                    self.trailer()


                pass
            elif token in [RLangParser.S_PRIME]:
                localctx = RLangParser.Bound_next_stateContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 570
                self.match(RLangParser.S_PRIME)
                self.state = 572
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
                if la_ == 1:
                    self.state = 571
                    self.trailer()


                pass
            elif token in [RLangParser.A]:
                localctx = RLangParser.Bound_actionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 574
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
        self.enterRule(localctx, 78, self.RULE_trailer)
        try:
            self.state = 579
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Trailer_arrayContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 577
                self.int_array_exp()
                pass

            elif la_ == 2:
                localctx = RLangParser.Trailer_sliceContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 578
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
        self.enterRule(localctx, 80, self.RULE_any_array)
        try:
            self.state = 583
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Any_array_compoundContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 581
                self.compound_array_exp()
                pass

            elif la_ == 2:
                localctx = RLangParser.Any_array_any_numContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 582
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
        self.enterRule(localctx, 82, self.RULE_compound_array_exp)
        self._la = 0 # Token type
        try:
            self.state = 597
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Compound_array_simpleContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 585
                self.any_num_array_exp()
                pass

            elif la_ == 2:
                localctx = RLangParser.Compound_array_compoundContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 586
                self.match(RLangParser.L_BRK)
                self.state = 587
                localctx._compound_array_exp = self.compound_array_exp()
                localctx.arr.append(localctx._compound_array_exp)
                self.state = 592
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.COM:
                    self.state = 588
                    self.match(RLangParser.COM)
                    self.state = 589
                    localctx._compound_array_exp = self.compound_array_exp()
                    localctx.arr.append(localctx._compound_array_exp)
                    self.state = 594
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 595
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
        self.enterRule(localctx, 84, self.RULE_int_array_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 599
            self.match(RLangParser.L_BRK)
            self.state = 600
            localctx._any_integer = self.any_integer()
            localctx.arr.append(localctx._any_integer)
            self.state = 605
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.COM:
                self.state = 601
                self.match(RLangParser.COM)
                self.state = 602
                localctx._any_integer = self.any_integer()
                localctx.arr.append(localctx._any_integer)
                self.state = 607
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 608
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
        self.enterRule(localctx, 86, self.RULE_any_num_array_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 610
            self.match(RLangParser.L_BRK)
            self.state = 611
            localctx._any_number = self.any_number()
            localctx.arr.append(localctx._any_number)
            self.state = 616
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.COM:
                self.state = 612
                self.match(RLangParser.COM)
                self.state = 613
                localctx._any_number = self.any_number()
                localctx.arr.append(localctx._any_number)
                self.state = 618
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 619
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
        self.enterRule(localctx, 88, self.RULE_slice_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 621
            self.match(RLangParser.L_BRK)
            self.state = 623
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.MINUS or _la==RLangParser.INTEGER:
                self.state = 622
                localctx.start_ind = self.any_integer()


            self.state = 625
            self.match(RLangParser.COL)
            self.state = 627
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.MINUS or _la==RLangParser.INTEGER:
                self.state = 626
                localctx.stop_ind = self.any_integer()


            self.state = 629
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
        self.enterRule(localctx, 90, self.RULE_integer_fraction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 631
            localctx.lhs = self.any_integer()
            self.state = 632
            self.match(RLangParser.DIVIDE)
            self.state = 633
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
        self.enterRule(localctx, 92, self.RULE_any_number)
        try:
            self.state = 637
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,70,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Any_num_intContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 635
                self.any_integer()
                pass

            elif la_ == 2:
                localctx = RLangParser.Any_num_decContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 636
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
        self.enterRule(localctx, 94, self.RULE_any_integer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 640
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.MINUS:
                self.state = 639
                self.match(RLangParser.MINUS)


            self.state = 642
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
        self.enterRule(localctx, 96, self.RULE_any_decimal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 645
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.MINUS:
                self.state = 644
                self.match(RLangParser.MINUS)


            self.state = 647
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
        self._predicates[33] = self.arithmetic_exp_sempred
        self._predicates[34] = self.boolean_exp_sempred
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
         




