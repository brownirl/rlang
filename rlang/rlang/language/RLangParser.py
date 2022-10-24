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
        buf.write("\u02d1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\7\2t\n")
        buf.write("\2\f\2\16\2w\13\2\3\2\3\2\3\2\7\2|\n\2\f\2\16\2\177\13")
        buf.write("\2\3\3\3\3\6\3\u0083\n\3\r\3\16\3\u0084\7\3\u0087\n\3")
        buf.write("\f\3\16\3\u008a\13\3\3\4\3\4\3\4\3\5\7\5\u0090\n\5\f\5")
        buf.write("\16\5\u0093\13\5\3\6\3\6\6\6\u0097\n\6\r\6\16\6\u0098")
        buf.write("\3\6\3\6\6\6\u009d\n\6\r\6\16\6\u009e\3\6\3\6\6\6\u00a3")
        buf.write("\n\6\r\6\16\6\u00a4\3\6\3\6\6\6\u00a9\n\6\r\6\16\6\u00aa")
        buf.write("\3\6\3\6\6\6\u00af\n\6\r\6\16\6\u00b0\3\6\3\6\6\6\u00b5")
        buf.write("\n\6\r\6\16\6\u00b6\3\6\3\6\6\6\u00bb\n\6\r\6\16\6\u00bc")
        buf.write("\3\6\3\6\6\6\u00c1\n\6\r\6\16\6\u00c2\3\6\3\6\3\6\3\6")
        buf.write("\5\6\u00c9\n\6\3\7\3\7\3\7\3\7\3\7\5\7\u00d0\n\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\5\b\u00d7\n\b\3\t\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\5\17\u00fd\n\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\7\20\u0106\n\20\f\20\16\20\u0109")
        buf.write("\13\20\6\20\u010b\n\20\r\20\16\20\u010c\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\7\22")
        buf.write("\u011c\n\22\f\22\16\22\u011f\13\22\3\22\3\22\3\22\3\22")
        buf.write("\7\22\u0125\n\22\f\22\16\22\u0128\13\22\3\22\3\22\3\23")
        buf.write("\3\23\5\23\u012e\n\23\3\24\3\24\3\24\3\24\3\24\3\24\7")
        buf.write("\24\u0136\n\24\f\24\16\24\u0139\13\24\3\24\3\24\3\25\3")
        buf.write("\25\3\25\5\25\u0140\n\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\7\26\u0148\n\26\f\26\16\26\u014b\13\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\7\26\u0154\n\26\f\26\16\26\u0157")
        buf.write("\13\26\3\26\3\26\7\26\u015b\n\26\f\26\16\26\u015e\13\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\7\26\u0165\n\26\f\26\16\26\u0168")
        buf.write("\13\26\3\26\3\26\5\26\u016c\n\26\3\27\3\27\3\27\7\27\u0171")
        buf.write("\n\27\f\27\16\27\u0174\13\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\7\30\u017b\n\30\f\30\16\30\u017e\13\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\6\30\u0185\n\30\r\30\16\30\u0186\5\30\u0189")
        buf.write("\n\30\3\31\3\31\3\31\5\31\u018e\n\31\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\33\3\33\7\33\u0199\n\33\f\33\16\33")
        buf.write("\u019c\13\33\6\33\u019e\n\33\r\33\16\33\u019f\3\34\3\34")
        buf.write("\3\34\3\34\3\34\5\34\u01a7\n\34\3\35\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\7\35\u01b6")
        buf.write("\n\35\f\35\16\35\u01b9\13\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\5\35\u01c1\n\35\3\36\3\36\3\36\7\36\u01c6\n\36\f")
        buf.write("\36\16\36\u01c9\13\36\3\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\5\37\u01d4\n\37\3\37\3\37\6\37\u01d8\n\37")
        buf.write("\r\37\16\37\u01d9\5\37\u01dc\n\37\3 \3 \3 \3!\3!\5!\u01e3")
        buf.write("\n!\3!\5!\u01e6\n!\3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3")
        buf.write("#\5#\u01f3\n#\3#\3#\3$\3$\3$\3$\3$\3%\5%\u01fd\n%\3%\3")
        buf.write("%\7%\u0201\n%\f%\16%\u0204\13%\3&\3&\3&\3&\5&\u020a\n")
        buf.write("&\3\'\3\'\5\'\u020e\n\'\3(\3(\3(\3(\3(\3(\3(\3(\5(\u0218")
        buf.write("\n(\3(\3(\3(\3(\3(\3(\7(\u0220\n(\f(\16(\u0223\13(\3)")
        buf.write("\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\5)\u0236")
        buf.write("\n)\3)\3)\3)\3)\3)\3)\3)\3)\3)\7)\u0241\n)\f)\16)\u0244")
        buf.write("\13)\3*\3*\5*\u0248\n*\3+\3+\3+\3+\5+\u024e\n+\3+\3+\5")
        buf.write("+\u0252\n+\3+\3+\3+\3+\5+\u0258\n+\3+\3+\5+\u025c\n+\5")
        buf.write("+\u025e\n+\3,\3,\3,\3,\3,\5,\u0265\n,\3-\3-\5-\u0269\n")
        buf.write("-\3-\7-\u026c\n-\f-\16-\u026f\13-\3-\3-\5-\u0273\n-\3")
        buf.write("-\3-\5-\u0277\n-\3-\5-\u027a\n-\3.\3.\3/\3/\5/\u0280\n")
        buf.write("/\3\60\3\60\3\60\3\60\7\60\u0286\n\60\f\60\16\60\u0289")
        buf.write("\13\60\3\60\3\60\3\61\3\61\5\61\u028f\n\61\3\62\3\62\3")
        buf.write("\62\3\62\3\62\7\62\u0296\n\62\f\62\16\62\u0299\13\62\3")
        buf.write("\62\3\62\5\62\u029d\n\62\3\63\3\63\3\63\3\63\7\63\u02a3")
        buf.write("\n\63\f\63\16\63\u02a6\13\63\3\63\3\63\3\64\3\64\3\64")
        buf.write("\3\64\7\64\u02ae\n\64\f\64\16\64\u02b1\13\64\3\64\3\64")
        buf.write("\3\65\3\65\5\65\u02b7\n\65\3\65\3\65\5\65\u02bb\n\65\3")
        buf.write("\65\3\65\3\66\3\66\3\66\3\66\3\67\3\67\5\67\u02c5\n\67")
        buf.write("\38\58\u02c8\n8\38\38\39\59\u02cd\n9\39\39\39\2\4NP:\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnp\2\b\4\2**LL\3\2FG\3")
        buf.write("\2HI\4\28;DE\3\2./\4\288;;\2\u0305\2u\3\2\2\2\4\u0088")
        buf.write("\3\2\2\2\6\u008b\3\2\2\2\b\u0091\3\2\2\2\n\u00c8\3\2\2")
        buf.write("\2\f\u00ca\3\2\2\2\16\u00d1\3\2\2\2\20\u00d8\3\2\2\2\22")
        buf.write("\u00dd\3\2\2\2\24\u00e2\3\2\2\2\26\u00e7\3\2\2\2\30\u00ec")
        buf.write("\3\2\2\2\32\u00f1\3\2\2\2\34\u00f6\3\2\2\2\36\u010a\3")
        buf.write("\2\2\2 \u010e\3\2\2\2\"\u0112\3\2\2\2$\u012d\3\2\2\2&")
        buf.write("\u012f\3\2\2\2(\u013f\3\2\2\2*\u0141\3\2\2\2,\u016d\3")
        buf.write("\2\2\2.\u0188\3\2\2\2\60\u018a\3\2\2\2\62\u018f\3\2\2")
        buf.write("\2\64\u019d\3\2\2\2\66\u01a6\3\2\2\28\u01a8\3\2\2\2:\u01c2")
        buf.write("\3\2\2\2<\u01db\3\2\2\2>\u01dd\3\2\2\2@\u01e5\3\2\2\2")
        buf.write("B\u01ea\3\2\2\2D\u01ed\3\2\2\2F\u01f6\3\2\2\2H\u01fc\3")
        buf.write("\2\2\2J\u0209\3\2\2\2L\u020d\3\2\2\2N\u0217\3\2\2\2P\u0235")
        buf.write("\3\2\2\2R\u0247\3\2\2\2T\u025d\3\2\2\2V\u0264\3\2\2\2")
        buf.write("X\u0279\3\2\2\2Z\u027b\3\2\2\2\\\u027f\3\2\2\2^\u0281")
        buf.write("\3\2\2\2`\u028e\3\2\2\2b\u029c\3\2\2\2d\u029e\3\2\2\2")
        buf.write("f\u02a9\3\2\2\2h\u02b4\3\2\2\2j\u02be\3\2\2\2l\u02c4\3")
        buf.write("\2\2\2n\u02c7\3\2\2\2p\u02cc\3\2\2\2rt\7\5\2\2sr\3\2\2")
        buf.write("\2tw\3\2\2\2us\3\2\2\2uv\3\2\2\2vx\3\2\2\2wu\3\2\2\2x")
        buf.write("y\5\4\3\2y}\5\b\5\2z|\7\5\2\2{z\3\2\2\2|\177\3\2\2\2}")
        buf.write("{\3\2\2\2}~\3\2\2\2~\3\3\2\2\2\177}\3\2\2\2\u0080\u0082")
        buf.write("\5\6\4\2\u0081\u0083\7\5\2\2\u0082\u0081\3\2\2\2\u0083")
        buf.write("\u0084\3\2\2\2\u0084\u0082\3\2\2\2\u0084\u0085\3\2\2\2")
        buf.write("\u0085\u0087\3\2\2\2\u0086\u0080\3\2\2\2\u0087\u008a\3")
        buf.write("\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\5")
        buf.write("\3\2\2\2\u008a\u0088\3\2\2\2\u008b\u008c\7\6\2\2\u008c")
        buf.write("\u008d\7K\2\2\u008d\7\3\2\2\2\u008e\u0090\5\n\6\2\u008f")
        buf.write("\u008e\3\2\2\2\u0090\u0093\3\2\2\2\u0091\u008f\3\2\2\2")
        buf.write("\u0091\u0092\3\2\2\2\u0092\t\3\2\2\2\u0093\u0091\3\2\2")
        buf.write("\2\u0094\u0096\5\f\7\2\u0095\u0097\7\5\2\2\u0096\u0095")
        buf.write("\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0096\3\2\2\2\u0098")
        buf.write("\u0099\3\2\2\2\u0099\u00c9\3\2\2\2\u009a\u009c\5\16\b")
        buf.write("\2\u009b\u009d\7\5\2\2\u009c\u009b\3\2\2\2\u009d\u009e")
        buf.write("\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009f\3\2\2\2\u009f")
        buf.write("\u00c9\3\2\2\2\u00a0\u00a2\5\20\t\2\u00a1\u00a3\7\5\2")
        buf.write("\2\u00a2\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a2")
        buf.write("\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00c9\3\2\2\2\u00a6")
        buf.write("\u00a8\5\22\n\2\u00a7\u00a9\7\5\2\2\u00a8\u00a7\3\2\2")
        buf.write("\2\u00a9\u00aa\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa\u00ab")
        buf.write("\3\2\2\2\u00ab\u00c9\3\2\2\2\u00ac\u00ae\5\24\13\2\u00ad")
        buf.write("\u00af\7\5\2\2\u00ae\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2")
        buf.write("\u00b0\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00c9\3")
        buf.write("\2\2\2\u00b2\u00b4\5\26\f\2\u00b3\u00b5\7\5\2\2\u00b4")
        buf.write("\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b4\3\2\2\2")
        buf.write("\u00b6\u00b7\3\2\2\2\u00b7\u00c9\3\2\2\2\u00b8\u00ba\5")
        buf.write("\30\r\2\u00b9\u00bb\7\5\2\2\u00ba\u00b9\3\2\2\2\u00bb")
        buf.write("\u00bc\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2")
        buf.write("\u00bd\u00c9\3\2\2\2\u00be\u00c0\5\32\16\2\u00bf\u00c1")
        buf.write("\7\5\2\2\u00c0\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2")
        buf.write("\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c9\3\2\2\2")
        buf.write("\u00c4\u00c9\5\34\17\2\u00c5\u00c9\5\"\22\2\u00c6\u00c9")
        buf.write("\5&\24\2\u00c7\u00c9\5\62\32\2\u00c8\u0094\3\2\2\2\u00c8")
        buf.write("\u009a\3\2\2\2\u00c8\u00a0\3\2\2\2\u00c8\u00a6\3\2\2\2")
        buf.write("\u00c8\u00ac\3\2\2\2\u00c8\u00b2\3\2\2\2\u00c8\u00b8\3")
        buf.write("\2\2\2\u00c8\u00be\3\2\2\2\u00c8\u00c4\3\2\2\2\u00c8\u00c5")
        buf.write("\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c7\3\2\2\2\u00c9")
        buf.write("\13\3\2\2\2\u00ca\u00cb\7\16\2\2\u00cb\u00cc\7L\2\2\u00cc")
        buf.write("\u00cf\7\61\2\2\u00cd\u00d0\5N(\2\u00ce\u00d0\5P)\2\u00cf")
        buf.write("\u00cd\3\2\2\2\u00cf\u00ce\3\2\2\2\u00d0\r\3\2\2\2\u00d1")
        buf.write("\u00d2\7\17\2\2\u00d2\u00d3\7L\2\2\u00d3\u00d6\7\61\2")
        buf.write("\2\u00d4\u00d7\5l\67\2\u00d5\u00d7\5f\64\2\u00d6\u00d4")
        buf.write("\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7\17\3\2\2\2\u00d8\u00d9")
        buf.write("\7\n\2\2\u00d9\u00da\7L\2\2\u00da\u00db\7\61\2\2\u00db")
        buf.write("\u00dc\5X-\2\u00dc\21\3\2\2\2\u00dd\u00de\7\7\2\2\u00de")
        buf.write("\u00df\7L\2\2\u00df\u00e0\7\61\2\2\u00e0\u00e1\5P)\2\u00e1")
        buf.write("\23\3\2\2\2\u00e2\u00e3\7\13\2\2\u00e3\u00e4\7L\2\2\u00e4")
        buf.write("\u00e5\7\61\2\2\u00e5\u00e6\5P)\2\u00e6\25\3\2\2\2\u00e7")
        buf.write("\u00e8\7\t\2\2\u00e8\u00e9\7L\2\2\u00e9\u00ea\7\61\2\2")
        buf.write("\u00ea\u00eb\5N(\2\u00eb\27\3\2\2\2\u00ec\u00ed\7\25\2")
        buf.write("\2\u00ed\u00ee\7L\2\2\u00ee\u00ef\7\61\2\2\u00ef\u00f0")
        buf.write("\5N(\2\u00f0\31\3\2\2\2\u00f1\u00f2\7\r\2\2\u00f2\u00f3")
        buf.write("\7L\2\2\u00f3\u00f4\7\61\2\2\u00f4\u00f5\5F$\2\u00f5\33")
        buf.write("\3\2\2\2\u00f6\u00f7\7\f\2\2\u00f7\u00fc\7L\2\2\u00f8")
        buf.write("\u00f9\7B\2\2\u00f9\u00fa\5Z.\2\u00fa\u00fb\7C\2\2\u00fb")
        buf.write("\u00fd\3\2\2\2\u00fc\u00f8\3\2\2\2\u00fc\u00fd\3\2\2\2")
        buf.write("\u00fd\u00fe\3\2\2\2\u00fe\u00ff\7<\2\2\u00ff\u0100\7")
        buf.write("\3\2\2\u0100\u0101\5\36\20\2\u0101\u0102\7\4\2\2\u0102")
        buf.write("\35\3\2\2\2\u0103\u0107\5 \21\2\u0104\u0106\7\5\2\2\u0105")
        buf.write("\u0104\3\2\2\2\u0106\u0109\3\2\2\2\u0107\u0105\3\2\2\2")
        buf.write("\u0107\u0108\3\2\2\2\u0108\u010b\3\2\2\2\u0109\u0107\3")
        buf.write("\2\2\2\u010a\u0103\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010a")
        buf.write("\3\2\2\2\u010c\u010d\3\2\2\2\u010d\37\3\2\2\2\u010e\u010f")
        buf.write("\7L\2\2\u010f\u0110\7<\2\2\u0110\u0111\5R*\2\u0111!\3")
        buf.write("\2\2\2\u0112\u0113\7\24\2\2\u0113\u0114\7L\2\2\u0114\u0115")
        buf.write("\7<\2\2\u0115\u0116\7\3\2\2\u0116\u0117\7%\2\2\u0117\u0118")
        buf.write("\5$\23\2\u0118\u0119\7\3\2\2\u0119\u011d\5(\25\2\u011a")
        buf.write("\u011c\7\5\2\2\u011b\u011a\3\2\2\2\u011c\u011f\3\2\2\2")
        buf.write("\u011d\u011b\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u0120\3")
        buf.write("\2\2\2\u011f\u011d\3\2\2\2\u0120\u0121\7\4\2\2\u0121\u0122")
        buf.write("\7&\2\2\u0122\u0126\5$\23\2\u0123\u0125\7\5\2\2\u0124")
        buf.write("\u0123\3\2\2\2\u0125\u0128\3\2\2\2\u0126\u0124\3\2\2\2")
        buf.write("\u0126\u0127\3\2\2\2\u0127\u0129\3\2\2\2\u0128\u0126\3")
        buf.write("\2\2\2\u0129\u012a\7\4\2\2\u012a#\3\2\2\2\u012b\u012e")
        buf.write("\5P)\2\u012c\u012e\7\60\2\2\u012d\u012b\3\2\2\2\u012d")
        buf.write("\u012c\3\2\2\2\u012e%\3\2\2\2\u012f\u0130\7\22\2\2\u0130")
        buf.write("\u0131\t\2\2\2\u0131\u0132\7<\2\2\u0132\u0133\7\3\2\2")
        buf.write("\u0133\u0137\5(\25\2\u0134\u0136\7\5\2\2\u0135\u0134\3")
        buf.write("\2\2\2\u0136\u0139\3\2\2\2\u0137\u0135\3\2\2\2\u0137\u0138")
        buf.write("\3\2\2\2\u0138\u013a\3\2\2\2\u0139\u0137\3\2\2\2\u013a")
        buf.write("\u013b\7\4\2\2\u013b\'\3\2\2\2\u013c\u0140\5\60\31\2\u013d")
        buf.write("\u0140\5*\26\2\u013e\u0140\5,\27\2\u013f\u013c\3\2\2\2")
        buf.write("\u013f\u013d\3\2\2\2\u013f\u013e\3\2\2\2\u0140)\3\2\2")
        buf.write("\2\u0141\u0142\7!\2\2\u0142\u0143\5P)\2\u0143\u0144\7")
        buf.write("<\2\2\u0144\u0145\7\3\2\2\u0145\u0149\5(\25\2\u0146\u0148")
        buf.write("\7\5\2\2\u0147\u0146\3\2\2\2\u0148\u014b\3\2\2\2\u0149")
        buf.write("\u0147\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u014c\3\2\2\2")
        buf.write("\u014b\u0149\3\2\2\2\u014c\u015c\7\4\2\2\u014d\u014e\7")
        buf.write("#\2\2\u014e\u014f\5P)\2\u014f\u0150\7<\2\2\u0150\u0151")
        buf.write("\7\3\2\2\u0151\u0155\5(\25\2\u0152\u0154\7\5\2\2\u0153")
        buf.write("\u0152\3\2\2\2\u0154\u0157\3\2\2\2\u0155\u0153\3\2\2\2")
        buf.write("\u0155\u0156\3\2\2\2\u0156\u0158\3\2\2\2\u0157\u0155\3")
        buf.write("\2\2\2\u0158\u0159\7\4\2\2\u0159\u015b\3\2\2\2\u015a\u014d")
        buf.write("\3\2\2\2\u015b\u015e\3\2\2\2\u015c\u015a\3\2\2\2\u015c")
        buf.write("\u015d\3\2\2\2\u015d\u016b\3\2\2\2\u015e\u015c\3\2\2\2")
        buf.write("\u015f\u0160\7\"\2\2\u0160\u0161\7<\2\2\u0161\u0162\7")
        buf.write("\3\2\2\u0162\u0166\5(\25\2\u0163\u0165\7\5\2\2\u0164\u0163")
        buf.write("\3\2\2\2\u0165\u0168\3\2\2\2\u0166\u0164\3\2\2\2\u0166")
        buf.write("\u0167\3\2\2\2\u0167\u0169\3\2\2\2\u0168\u0166\3\2\2\2")
        buf.write("\u0169\u016a\7\4\2\2\u016a\u016c\3\2\2\2\u016b\u015f\3")
        buf.write("\2\2\2\u016b\u016c\3\2\2\2\u016c+\3\2\2\2\u016d\u0172")
        buf.write("\5.\30\2\u016e\u016f\7,\2\2\u016f\u0171\5.\30\2\u0170")
        buf.write("\u016e\3\2\2\2\u0171\u0174\3\2\2\2\u0172\u0170\3\2\2\2")
        buf.write("\u0172\u0173\3\2\2\2\u0173-\3\2\2\2\u0174\u0172\3\2\2")
        buf.write("\2\u0175\u0176\5D#\2\u0176\u0177\7<\2\2\u0177\u0178\7")
        buf.write("\3\2\2\u0178\u017c\5(\25\2\u0179\u017b\7\5\2\2\u017a\u0179")
        buf.write("\3\2\2\2\u017b\u017e\3\2\2\2\u017c\u017a\3\2\2\2\u017c")
        buf.write("\u017d\3\2\2\2\u017d\u017f\3\2\2\2\u017e\u017c\3\2\2\2")
        buf.write("\u017f\u0180\7\4\2\2\u0180\u0189\3\2\2\2\u0181\u0182\5")
        buf.write("\60\31\2\u0182\u0184\5D#\2\u0183\u0185\7\5\2\2\u0184\u0183")
        buf.write("\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0184\3\2\2\2\u0186")
        buf.write("\u0187\3\2\2\2\u0187\u0189\3\2\2\2\u0188\u0175\3\2\2\2")
        buf.write("\u0188\u0181\3\2\2\2\u0189/\3\2\2\2\u018a\u018d\7\23\2")
        buf.write("\2\u018b\u018e\7L\2\2\u018c\u018e\5N(\2\u018d\u018b\3")
        buf.write("\2\2\2\u018d\u018c\3\2\2\2\u018e\61\3\2\2\2\u018f\u0190")
        buf.write("\7\20\2\2\u0190\u0191\t\2\2\2\u0191\u0192\7<\2\2\u0192")
        buf.write("\u0193\7\3\2\2\u0193\u0194\5\64\33\2\u0194\u0195\7\4\2")
        buf.write("\2\u0195\63\3\2\2\2\u0196\u019a\5\66\34\2\u0197\u0199")
        buf.write("\7\5\2\2\u0198\u0197\3\2\2\2\u0199\u019c\3\2\2\2\u019a")
        buf.write("\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u019e\3\2\2\2")
        buf.write("\u019c\u019a\3\2\2\2\u019d\u0196\3\2\2\2\u019e\u019f\3")
        buf.write("\2\2\2\u019f\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\65")
        buf.write("\3\2\2\2\u01a1\u01a7\5> \2\u01a2\u01a7\5@!\2\u01a3\u01a7")
        buf.write("\5B\"\2\u01a4\u01a7\58\35\2\u01a5\u01a7\5:\36\2\u01a6")
        buf.write("\u01a1\3\2\2\2\u01a6\u01a2\3\2\2\2\u01a6\u01a3\3\2\2\2")
        buf.write("\u01a6\u01a4\3\2\2\2\u01a6\u01a5\3\2\2\2\u01a7\67\3\2")
        buf.write("\2\2\u01a8\u01a9\7!\2\2\u01a9\u01aa\5P)\2\u01aa\u01ab")
        buf.write("\7<\2\2\u01ab\u01ac\7\3\2\2\u01ac\u01ad\5\64\33\2\u01ad")
        buf.write("\u01b7\7\4\2\2\u01ae\u01af\7#\2\2\u01af\u01b0\5P)\2\u01b0")
        buf.write("\u01b1\7<\2\2\u01b1\u01b2\7\3\2\2\u01b2\u01b3\5\64\33")
        buf.write("\2\u01b3\u01b4\7\4\2\2\u01b4\u01b6\3\2\2\2\u01b5\u01ae")
        buf.write("\3\2\2\2\u01b6\u01b9\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b7")
        buf.write("\u01b8\3\2\2\2\u01b8\u01c0\3\2\2\2\u01b9\u01b7\3\2\2\2")
        buf.write("\u01ba\u01bb\7\"\2\2\u01bb\u01bc\7<\2\2\u01bc\u01bd\7")
        buf.write("\3\2\2\u01bd\u01be\5\64\33\2\u01be\u01bf\7\4\2\2\u01bf")
        buf.write("\u01c1\3\2\2\2\u01c0\u01ba\3\2\2\2\u01c0\u01c1\3\2\2\2")
        buf.write("\u01c19\3\2\2\2\u01c2\u01c7\5<\37\2\u01c3\u01c4\7,\2\2")
        buf.write("\u01c4\u01c6\5<\37\2\u01c5\u01c3\3\2\2\2\u01c6\u01c9\3")
        buf.write("\2\2\2\u01c7\u01c5\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8;")
        buf.write("\3\2\2\2\u01c9\u01c7\3\2\2\2\u01ca\u01cb\5D#\2\u01cb\u01cc")
        buf.write("\7<\2\2\u01cc\u01cd\7\3\2\2\u01cd\u01ce\5\64\33\2\u01ce")
        buf.write("\u01cf\7\4\2\2\u01cf\u01dc\3\2\2\2\u01d0\u01d4\5> \2\u01d1")
        buf.write("\u01d4\5@!\2\u01d2\u01d4\5B\"\2\u01d3\u01d0\3\2\2\2\u01d3")
        buf.write("\u01d1\3\2\2\2\u01d3\u01d2\3\2\2\2\u01d4\u01d5\3\2\2\2")
        buf.write("\u01d5\u01d7\5D#\2\u01d6\u01d8\7\5\2\2\u01d7\u01d6\3\2")
        buf.write("\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01d7\3\2\2\2\u01d9\u01da")
        buf.write("\3\2\2\2\u01da\u01dc\3\2\2\2\u01db\u01ca\3\2\2\2\u01db")
        buf.write("\u01d3\3\2\2\2\u01dc=\3\2\2\2\u01dd\u01de\7\21\2\2\u01de")
        buf.write("\u01df\5N(\2\u01df?\3\2\2\2\u01e0\u01e2\7L\2\2\u01e1\u01e3")
        buf.write("\7 \2\2\u01e2\u01e1\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3")
        buf.write("\u01e6\3\2\2\2\u01e4\u01e6\7\34\2\2\u01e5\u01e0\3\2\2")
        buf.write("\2\u01e5\u01e4\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e8")
        buf.write("\7\62\2\2\u01e8\u01e9\5N(\2\u01e9A\3\2\2\2\u01ea\u01eb")
        buf.write("\7\62\2\2\u01eb\u01ec\7L\2\2\u01ecC\3\2\2\2\u01ed\u01ee")
        buf.write("\7\'\2\2\u01ee\u01ef\7\37\2\2\u01ef\u01f2\7B\2\2\u01f0")
        buf.write("\u01f3\5l\67\2\u01f1\u01f3\5j\66\2\u01f2\u01f0\3\2\2\2")
        buf.write("\u01f2\u01f1\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4\u01f5\7")
        buf.write("C\2\2\u01f5E\3\2\2\2\u01f6\u01f7\5Z.\2\u01f7\u01f8\7B")
        buf.write("\2\2\u01f8\u01f9\5H%\2\u01f9\u01fa\7C\2\2\u01faG\3\2\2")
        buf.write("\2\u01fb\u01fd\5J&\2\u01fc\u01fb\3\2\2\2\u01fc\u01fd\3")
        buf.write("\2\2\2\u01fd\u0202\3\2\2\2\u01fe\u01ff\7=\2\2\u01ff\u0201")
        buf.write("\5J&\2\u0200\u01fe\3\2\2\2\u0201\u0204\3\2\2\2\u0202\u0200")
        buf.write("\3\2\2\2\u0202\u0203\3\2\2\2\u0203I\3\2\2\2\u0204\u0202")
        buf.write("\3\2\2\2\u0205\u020a\5L\'\2\u0206\u020a\5N(\2\u0207\u020a")
        buf.write("\5P)\2\u0208\u020a\5^\60\2\u0209\u0205\3\2\2\2\u0209\u0206")
        buf.write("\3\2\2\2\u0209\u0207\3\2\2\2\u0209\u0208\3\2\2\2\u020a")
        buf.write("K\3\2\2\2\u020b\u020e\5X-\2\u020c\u020e\5F$\2\u020d\u020b")
        buf.write("\3\2\2\2\u020d\u020c\3\2\2\2\u020eM\3\2\2\2\u020f\u0210")
        buf.write("\b(\1\2\u0210\u0211\7B\2\2\u0211\u0212\5N(\2\u0212\u0213")
        buf.write("\7C\2\2\u0213\u0218\3\2\2\2\u0214\u0218\5l\67\2\u0215")
        buf.write("\u0218\5`\61\2\u0216\u0218\5X-\2\u0217\u020f\3\2\2\2\u0217")
        buf.write("\u0214\3\2\2\2\u0217\u0215\3\2\2\2\u0217\u0216\3\2\2\2")
        buf.write("\u0218\u0221\3\2\2\2\u0219\u021a\f\7\2\2\u021a\u021b\t")
        buf.write("\3\2\2\u021b\u0220\5N(\b\u021c\u021d\f\6\2\2\u021d\u021e")
        buf.write("\t\4\2\2\u021e\u0220\5N(\7\u021f\u0219\3\2\2\2\u021f\u021c")
        buf.write("\3\2\2\2\u0220\u0223\3\2\2\2\u0221\u021f\3\2\2\2\u0221")
        buf.write("\u0222\3\2\2\2\u0222O\3\2\2\2\u0223\u0221\3\2\2\2\u0224")
        buf.write("\u0225\b)\1\2\u0225\u0226\7B\2\2\u0226\u0227\5P)\2\u0227")
        buf.write("\u0228\7C\2\2\u0228\u0236\3\2\2\2\u0229\u022a\7-\2\2\u022a")
        buf.write("\u0236\5P)\b\u022b\u022c\5N(\2\u022c\u022d\7$\2\2\u022d")
        buf.write("\u022e\5N(\2\u022e\u0236\3\2\2\2\u022f\u0230\5N(\2\u0230")
        buf.write("\u0231\t\5\2\2\u0231\u0232\5N(\2\u0232\u0236\3\2\2\2\u0233")
        buf.write("\u0236\5X-\2\u0234\u0236\t\6\2\2\u0235\u0224\3\2\2\2\u0235")
        buf.write("\u0229\3\2\2\2\u0235\u022b\3\2\2\2\u0235\u022f\3\2\2\2")
        buf.write("\u0235\u0233\3\2\2\2\u0235\u0234\3\2\2\2\u0236\u0242\3")
        buf.write("\2\2\2\u0237\u0238\f\n\2\2\u0238\u0239\7+\2\2\u0239\u0241")
        buf.write("\5P)\13\u023a\u023b\f\t\2\2\u023b\u023c\7,\2\2\u023c\u0241")
        buf.write("\5P)\n\u023d\u023e\f\6\2\2\u023e\u023f\t\7\2\2\u023f\u0241")
        buf.write("\5P)\7\u0240\u0237\3\2\2\2\u0240\u023a\3\2\2\2\u0240\u023d")
        buf.write("\3\2\2\2\u0241\u0244\3\2\2\2\u0242\u0240\3\2\2\2\u0242")
        buf.write("\u0243\3\2\2\2\u0243Q\3\2\2\2\u0244\u0242\3\2\2\2\u0245")
        buf.write("\u0248\5T+\2\u0246\u0248\5V,\2\u0247\u0245\3\2\2\2\u0247")
        buf.write("\u0246\3\2\2\2\u0248S\3\2\2\2\u0249\u0251\7\31\2\2\u024a")
        buf.write("\u024d\7>\2\2\u024b\u024e\5V,\2\u024c\u024e\5T+\2\u024d")
        buf.write("\u024b\3\2\2\2\u024d\u024c\3\2\2\2\u024e\u024f\3\2\2\2")
        buf.write("\u024f\u0250\7?\2\2\u0250\u0252\3\2\2\2\u0251\u024a\3")
        buf.write("\2\2\2\u0251\u0252\3\2\2\2\u0252\u025e\3\2\2\2\u0253\u025b")
        buf.write("\7\32\2\2\u0254\u0257\7>\2\2\u0255\u0258\5V,\2\u0256\u0258")
        buf.write("\5T+\2\u0257\u0255\3\2\2\2\u0257\u0256\3\2\2\2\u0258\u0259")
        buf.write("\3\2\2\2\u0259\u025a\7?\2\2\u025a\u025c\3\2\2\2\u025b")
        buf.write("\u0254\3\2\2\2\u025b\u025c\3\2\2\2\u025c\u025e\3\2\2\2")
        buf.write("\u025d\u0249\3\2\2\2\u025d\u0253\3\2\2\2\u025eU\3\2\2")
        buf.write("\2\u025f\u0265\7\26\2\2\u0260\u0265\7\27\2\2\u0261\u0265")
        buf.write("\7\30\2\2\u0262\u0265\7\33\2\2\u0263\u0265\5Z.\2\u0264")
        buf.write("\u025f\3\2\2\2\u0264\u0260\3\2\2\2\u0264\u0261\3\2\2\2")
        buf.write("\u0264\u0262\3\2\2\2\u0264\u0263\3\2\2\2\u0265W\3\2\2")
        buf.write("\2\u0266\u0268\7L\2\2\u0267\u0269\7 \2\2\u0268\u0267\3")
        buf.write("\2\2\2\u0268\u0269\3\2\2\2\u0269\u026d\3\2\2\2\u026a\u026c")
        buf.write("\5\\/\2\u026b\u026a\3\2\2\2\u026c\u026f\3\2\2\2\u026d")
        buf.write("\u026b\3\2\2\2\u026d\u026e\3\2\2\2\u026e\u027a\3\2\2\2")
        buf.write("\u026f\u026d\3\2\2\2\u0270\u0272\7\35\2\2\u0271\u0273")
        buf.write("\5\\/\2\u0272\u0271\3\2\2\2\u0272\u0273\3\2\2\2\u0273")
        buf.write("\u027a\3\2\2\2\u0274\u0276\7\34\2\2\u0275\u0277\5\\/\2")
        buf.write("\u0276\u0275\3\2\2\2\u0276\u0277\3\2\2\2\u0277\u027a\3")
        buf.write("\2\2\2\u0278\u027a\7\36\2\2\u0279\u0266\3\2\2\2\u0279")
        buf.write("\u0270\3\2\2\2\u0279\u0274\3\2\2\2\u0279\u0278\3\2\2\2")
        buf.write("\u027aY\3\2\2\2\u027b\u027c\7L\2\2\u027c[\3\2\2\2\u027d")
        buf.write("\u0280\5d\63\2\u027e\u0280\5h\65\2\u027f\u027d\3\2\2\2")
        buf.write("\u027f\u027e\3\2\2\2\u0280]\3\2\2\2\u0281\u0282\7>\2\2")
        buf.write("\u0282\u0287\5L\'\2\u0283\u0284\7=\2\2\u0284\u0286\5L")
        buf.write("\'\2\u0285\u0283\3\2\2\2\u0286\u0289\3\2\2\2\u0287\u0285")
        buf.write("\3\2\2\2\u0287\u0288\3\2\2\2\u0288\u028a\3\2\2\2\u0289")
        buf.write("\u0287\3\2\2\2\u028a\u028b\7?\2\2\u028b_\3\2\2\2\u028c")
        buf.write("\u028f\5b\62\2\u028d\u028f\5f\64\2\u028e\u028c\3\2\2\2")
        buf.write("\u028e\u028d\3\2\2\2\u028fa\3\2\2\2\u0290\u029d\5f\64")
        buf.write("\2\u0291\u0292\7>\2\2\u0292\u0297\5b\62\2\u0293\u0294")
        buf.write("\7=\2\2\u0294\u0296\5b\62\2\u0295\u0293\3\2\2\2\u0296")
        buf.write("\u0299\3\2\2\2\u0297\u0295\3\2\2\2\u0297\u0298\3\2\2\2")
        buf.write("\u0298\u029a\3\2\2\2\u0299\u0297\3\2\2\2\u029a\u029b\7")
        buf.write("?\2\2\u029b\u029d\3\2\2\2\u029c\u0290\3\2\2\2\u029c\u0291")
        buf.write("\3\2\2\2\u029dc\3\2\2\2\u029e\u029f\7>\2\2\u029f\u02a4")
        buf.write("\5n8\2\u02a0\u02a1\7=\2\2\u02a1\u02a3\5n8\2\u02a2\u02a0")
        buf.write("\3\2\2\2\u02a3\u02a6\3\2\2\2\u02a4\u02a2\3\2\2\2\u02a4")
        buf.write("\u02a5\3\2\2\2\u02a5\u02a7\3\2\2\2\u02a6\u02a4\3\2\2\2")
        buf.write("\u02a7\u02a8\7?\2\2\u02a8e\3\2\2\2\u02a9\u02aa\7>\2\2")
        buf.write("\u02aa\u02af\5l\67\2\u02ab\u02ac\7=\2\2\u02ac\u02ae\5")
        buf.write("l\67\2\u02ad\u02ab\3\2\2\2\u02ae\u02b1\3\2\2\2\u02af\u02ad")
        buf.write("\3\2\2\2\u02af\u02b0\3\2\2\2\u02b0\u02b2\3\2\2\2\u02b1")
        buf.write("\u02af\3\2\2\2\u02b2\u02b3\7?\2\2\u02b3g\3\2\2\2\u02b4")
        buf.write("\u02b6\7>\2\2\u02b5\u02b7\5n8\2\u02b6\u02b5\3\2\2\2\u02b6")
        buf.write("\u02b7\3\2\2\2\u02b7\u02b8\3\2\2\2\u02b8\u02ba\7<\2\2")
        buf.write("\u02b9\u02bb\5n8\2\u02ba\u02b9\3\2\2\2\u02ba\u02bb\3\2")
        buf.write("\2\2\u02bb\u02bc\3\2\2\2\u02bc\u02bd\7?\2\2\u02bdi\3\2")
        buf.write("\2\2\u02be\u02bf\5n8\2\u02bf\u02c0\7G\2\2\u02c0\u02c1")
        buf.write("\5n8\2\u02c1k\3\2\2\2\u02c2\u02c5\5n8\2\u02c3\u02c5\5")
        buf.write("p9\2\u02c4\u02c2\3\2\2\2\u02c4\u02c3\3\2\2\2\u02c5m\3")
        buf.write("\2\2\2\u02c6\u02c8\7I\2\2\u02c7\u02c6\3\2\2\2\u02c7\u02c8")
        buf.write("\3\2\2\2\u02c8\u02c9\3\2\2\2\u02c9\u02ca\7N\2\2\u02ca")
        buf.write("o\3\2\2\2\u02cb\u02cd\7I\2\2\u02cc\u02cb\3\2\2\2\u02cc")
        buf.write("\u02cd\3\2\2\2\u02cd\u02ce\3\2\2\2\u02ce\u02cf\7M\2\2")
        buf.write("\u02cfq\3\2\2\2Ru}\u0084\u0088\u0091\u0098\u009e\u00a4")
        buf.write("\u00aa\u00b0\u00b6\u00bc\u00c2\u00c8\u00cf\u00d6\u00fc")
        buf.write("\u0107\u010c\u011d\u0126\u012d\u0137\u013f\u0149\u0155")
        buf.write("\u015c\u0166\u016b\u0172\u017c\u0186\u0188\u018d\u019a")
        buf.write("\u019f\u01a6\u01b7\u01c0\u01c7\u01d3\u01d9\u01db\u01e2")
        buf.write("\u01e5\u01f2\u01fc\u0202\u0209\u020d\u0217\u021f\u0221")
        buf.write("\u0235\u0240\u0242\u0247\u024d\u0251\u0257\u025b\u025d")
        buf.write("\u0264\u0268\u026d\u0272\u0276\u0279\u027f\u0287\u028e")
        buf.write("\u0297\u029c\u02a4\u02af\u02b6\u02ba\u02c4\u02c7\u02cc")
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
    RULE_object_def = 12
    RULE_class_def = 13
    RULE_attribute_definition_collection = 14
    RULE_attribute_definition = 15
    RULE_option = 16
    RULE_option_condition = 17
    RULE_policy = 18
    RULE_policy_statement = 19
    RULE_conditional_subpolicy = 20
    RULE_probabilistic_subpolicy = 21
    RULE_probabilistic_policy_statement = 22
    RULE_execute = 23
    RULE_effect = 24
    RULE_effect_statement_collection = 25
    RULE_effect_statement = 26
    RULE_conditional_effect = 27
    RULE_probabilistic_effect = 28
    RULE_probabilistic_effect_statement = 29
    RULE_reward = 30
    RULE_prediction = 31
    RULE_effect_reference = 32
    RULE_probabilistic_condition = 33
    RULE_object_instantiation = 34
    RULE_object_constructor_arg_list = 35
    RULE_object_constructor_arg = 36
    RULE_an_object = 37
    RULE_arithmetic_exp = 38
    RULE_boolean_exp = 39
    RULE_type_def = 40
    RULE_compound_type = 41
    RULE_simple_type = 42
    RULE_any_bound_var = 43
    RULE_any_bound_class = 44
    RULE_trailer = 45
    RULE_object_array = 46
    RULE_any_array = 47
    RULE_compound_array_exp = 48
    RULE_int_array_exp = 49
    RULE_any_num_array_exp = 50
    RULE_slice_exp = 51
    RULE_integer_fraction = 52
    RULE_any_number = 53
    RULE_any_integer = 54
    RULE_any_decimal = 55

    ruleNames =  [ "program", "imports", "import_stat", "declarations", 
                   "dec", "constant", "action", "factor", "proposition", 
                   "goal", "feature", "markov_feature", "object_def", "class_def", 
                   "attribute_definition_collection", "attribute_definition", 
                   "option", "option_condition", "policy", "policy_statement", 
                   "conditional_subpolicy", "probabilistic_subpolicy", "probabilistic_policy_statement", 
                   "execute", "effect", "effect_statement_collection", "effect_statement", 
                   "conditional_effect", "probabilistic_effect", "probabilistic_effect_statement", 
                   "reward", "prediction", "effect_reference", "probabilistic_condition", 
                   "object_instantiation", "object_constructor_arg_list", 
                   "object_constructor_arg", "an_object", "arithmetic_exp", 
                   "boolean_exp", "type_def", "compound_type", "simple_type", 
                   "any_bound_var", "any_bound_class", "trailer", "object_array", 
                   "any_array", "compound_array_exp", "int_array_exp", "any_num_array_exp", 
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
            self.state = 115
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 112
                    self.match(RLangParser.NL) 
                self.state = 117
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 118
            self.imports()
            self.state = 119
            self.declarations()
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.NL:
                self.state = 120
                self.match(RLangParser.NL)
                self.state = 125
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
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.IMPORT:
                self.state = 126
                self.import_stat()
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
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                self.state = 136
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
            self.state = 137
            self.match(RLangParser.IMPORT)
            self.state = 138
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
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RLangParser.PROPOSITION) | (1 << RLangParser.FEATURE) | (1 << RLangParser.FACTOR) | (1 << RLangParser.GOAL) | (1 << RLangParser.CLASS) | (1 << RLangParser.OBJECT) | (1 << RLangParser.CONSTANT) | (1 << RLangParser.ACTION) | (1 << RLangParser.EFFECT) | (1 << RLangParser.POLICY) | (1 << RLangParser.OPTION) | (1 << RLangParser.MARKOVFEATURE))) != 0):
                self.state = 140
                self.dec()
                self.state = 145
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


        def goal(self):
            return self.getTypedRuleContext(RLangParser.GoalContext,0)


        def feature(self):
            return self.getTypedRuleContext(RLangParser.FeatureContext,0)


        def markov_feature(self):
            return self.getTypedRuleContext(RLangParser.Markov_featureContext,0)


        def object_def(self):
            return self.getTypedRuleContext(RLangParser.Object_defContext,0)


        def class_def(self):
            return self.getTypedRuleContext(RLangParser.Class_defContext,0)


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
            self.state = 198
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.CONSTANT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.constant()
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
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                pass
            elif token in [RLangParser.ACTION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.action()
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
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                pass
            elif token in [RLangParser.FACTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 158
                self.factor()
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
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                pass
            elif token in [RLangParser.PROPOSITION]:
                self.enterOuterAlt(localctx, 4)
                self.state = 164
                self.proposition()
                self.state = 166 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 165
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 168 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                pass
            elif token in [RLangParser.GOAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 170
                self.goal()
                self.state = 172 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 171
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 174 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                pass
            elif token in [RLangParser.FEATURE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 176
                self.feature()
                self.state = 178 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 177
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 180 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                pass
            elif token in [RLangParser.MARKOVFEATURE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 182
                self.markov_feature()
                self.state = 184 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 183
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 186 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                pass
            elif token in [RLangParser.OBJECT]:
                self.enterOuterAlt(localctx, 8)
                self.state = 188
                self.object_def()
                self.state = 190 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 189
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 192 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                pass
            elif token in [RLangParser.CLASS]:
                self.enterOuterAlt(localctx, 9)
                self.state = 194
                self.class_def()
                pass
            elif token in [RLangParser.OPTION]:
                self.enterOuterAlt(localctx, 10)
                self.state = 195
                self.option()
                pass
            elif token in [RLangParser.POLICY]:
                self.enterOuterAlt(localctx, 11)
                self.state = 196
                self.policy()
                pass
            elif token in [RLangParser.EFFECT]:
                self.enterOuterAlt(localctx, 12)
                self.state = 197
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
            self.state = 200
            self.match(RLangParser.CONSTANT)
            self.state = 201
            self.match(RLangParser.IDENTIFIER)
            self.state = 202
            self.match(RLangParser.BIND)
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 203
                self.arithmetic_exp(0)
                pass

            elif la_ == 2:
                self.state = 204
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
            self.state = 207
            self.match(RLangParser.ACTION)
            self.state = 208
            self.match(RLangParser.IDENTIFIER)
            self.state = 209
            self.match(RLangParser.BIND)
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.MINUS, RLangParser.DECIMAL, RLangParser.INTEGER]:
                self.state = 210
                self.any_number()
                pass
            elif token in [RLangParser.L_BRK]:
                self.state = 211
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
            self.state = 214
            self.match(RLangParser.FACTOR)
            self.state = 215
            self.match(RLangParser.IDENTIFIER)
            self.state = 216
            self.match(RLangParser.BIND)
            self.state = 217
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
            self.state = 219
            self.match(RLangParser.PROPOSITION)
            self.state = 220
            self.match(RLangParser.IDENTIFIER)
            self.state = 221
            self.match(RLangParser.BIND)
            self.state = 222
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
            self.state = 224
            self.match(RLangParser.GOAL)
            self.state = 225
            self.match(RLangParser.IDENTIFIER)
            self.state = 226
            self.match(RLangParser.BIND)
            self.state = 227
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
            self.state = 229
            self.match(RLangParser.FEATURE)
            self.state = 230
            self.match(RLangParser.IDENTIFIER)
            self.state = 231
            self.match(RLangParser.BIND)
            self.state = 232
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
            self.state = 234
            self.match(RLangParser.MARKOVFEATURE)
            self.state = 235
            self.match(RLangParser.IDENTIFIER)
            self.state = 236
            self.match(RLangParser.BIND)
            self.state = 237
            self.arithmetic_exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBJECT(self):
            return self.getToken(RLangParser.OBJECT, 0)

        def IDENTIFIER(self):
            return self.getToken(RLangParser.IDENTIFIER, 0)

        def BIND(self):
            return self.getToken(RLangParser.BIND, 0)

        def object_instantiation(self):
            return self.getTypedRuleContext(RLangParser.Object_instantiationContext,0)


        def getRuleIndex(self):
            return RLangParser.RULE_object_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject_def" ):
                listener.enterObject_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject_def" ):
                listener.exitObject_def(self)




    def object_def(self):

        localctx = RLangParser.Object_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_object_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(RLangParser.OBJECT)
            self.state = 240
            self.match(RLangParser.IDENTIFIER)
            self.state = 241
            self.match(RLangParser.BIND)
            self.state = 242
            self.object_instantiation()
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

        def L_PAR(self):
            return self.getToken(RLangParser.L_PAR, 0)

        def any_bound_class(self):
            return self.getTypedRuleContext(RLangParser.Any_bound_classContext,0)


        def R_PAR(self):
            return self.getToken(RLangParser.R_PAR, 0)

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
        self.enterRule(localctx, 26, self.RULE_class_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(RLangParser.CLASS)
            self.state = 245
            self.match(RLangParser.IDENTIFIER)
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.L_PAR:
                self.state = 246
                self.match(RLangParser.L_PAR)
                self.state = 247
                self.any_bound_class()
                self.state = 248
                self.match(RLangParser.R_PAR)


            self.state = 252
            self.match(RLangParser.COL)
            self.state = 253
            self.match(RLangParser.INDENT)
            self.state = 254
            self.attribute_definition_collection()
            self.state = 255
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
        self.enterRule(localctx, 28, self.RULE_attribute_definition_collection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 257
                localctx._attribute_definition = self.attribute_definition()
                localctx.definitions.append(localctx._attribute_definition)
                self.state = 261
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.NL:
                    self.state = 258
                    self.match(RLangParser.NL)
                    self.state = 263
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 266 
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
        self.enterRule(localctx, 30, self.RULE_attribute_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(RLangParser.IDENTIFIER)
            self.state = 269
            self.match(RLangParser.COL)
            self.state = 270
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
        self.enterRule(localctx, 32, self.RULE_option)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(RLangParser.OPTION)
            self.state = 273
            self.match(RLangParser.IDENTIFIER)
            self.state = 274
            self.match(RLangParser.COL)
            self.state = 275
            self.match(RLangParser.INDENT)
            self.state = 276
            self.match(RLangParser.INIT)
            self.state = 277
            localctx.init = self.option_condition()
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
            self.state = 287
            self.match(RLangParser.UNTIL)
            self.state = 288
            localctx.until = self.option_condition()
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.NL:
                self.state = 289
                self.match(RLangParser.NL)
                self.state = 294
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 295
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
        self.enterRule(localctx, 34, self.RULE_option_condition)
        try:
            self.state = 299
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.S_PRIME, RLangParser.S, RLangParser.A, RLangParser.NOT, RLangParser.TRUE, RLangParser.FALSE, RLangParser.L_BRK, RLangParser.L_PAR, RLangParser.MINUS, RLangParser.IDENTIFIER, RLangParser.DECIMAL, RLangParser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.boolean_exp(0)
                pass
            elif token in [RLangParser.ANY_CONDITION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
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
        self.enterRule(localctx, 36, self.RULE_policy)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(RLangParser.POLICY)
            self.state = 302
            _la = self._input.LA(1)
            if not(_la==RLangParser.MAIN or _la==RLangParser.IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 303
            self.match(RLangParser.COL)
            self.state = 304
            self.match(RLangParser.INDENT)
            self.state = 305
            self.policy_statement()
            self.state = 309
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.NL:
                self.state = 306
                self.match(RLangParser.NL)
                self.state = 311
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 312
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
        self.enterRule(localctx, 38, self.RULE_policy_statement)
        try:
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Policy_statement_executeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.execute()
                pass

            elif la_ == 2:
                localctx = RLangParser.Policy_statement_conditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self.conditional_subpolicy()
                pass

            elif la_ == 3:
                localctx = RLangParser.Policy_statement_probabilisticContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 316
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
        self.enterRule(localctx, 40, self.RULE_conditional_subpolicy)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(RLangParser.IF)
            self.state = 320
            localctx.if_condition = self.boolean_exp(0)
            self.state = 321
            self.match(RLangParser.COL)
            self.state = 322
            self.match(RLangParser.INDENT)
            self.state = 323
            localctx.if_subpolicy = self.policy_statement()
            self.state = 327
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.NL:
                self.state = 324
                self.match(RLangParser.NL)
                self.state = 329
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 330
            self.match(RLangParser.DEDENT)
            self.state = 346
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.ELIF:
                self.state = 331
                self.match(RLangParser.ELIF)
                self.state = 332
                localctx._boolean_exp = self.boolean_exp(0)
                localctx.elif_conditions.append(localctx._boolean_exp)
                self.state = 333
                self.match(RLangParser.COL)
                self.state = 334
                self.match(RLangParser.INDENT)
                self.state = 335
                localctx._policy_statement = self.policy_statement()
                localctx.elif_subpolicies.append(localctx._policy_statement)
                self.state = 339
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.NL:
                    self.state = 336
                    self.match(RLangParser.NL)
                    self.state = 341
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 342
                self.match(RLangParser.DEDENT)
                self.state = 348
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 361
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.ELSE:
                self.state = 349
                self.match(RLangParser.ELSE)
                self.state = 350
                self.match(RLangParser.COL)
                self.state = 351
                self.match(RLangParser.INDENT)
                self.state = 352
                localctx.else_subpolicy = self.policy_statement()
                self.state = 356
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.NL:
                    self.state = 353
                    self.match(RLangParser.NL)
                    self.state = 358
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 359
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
            self.state = 363
            localctx._probabilistic_policy_statement = self.probabilistic_policy_statement()
            localctx.subpolicies.append(localctx._probabilistic_policy_statement)
            self.state = 368
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.OR:
                self.state = 364
                self.match(RLangParser.OR)
                self.state = 365
                localctx._probabilistic_policy_statement = self.probabilistic_policy_statement()
                localctx.subpolicies.append(localctx._probabilistic_policy_statement)
                self.state = 370
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
        self.enterRule(localctx, 44, self.RULE_probabilistic_policy_statement)
        self._la = 0 # Token type
        try:
            self.state = 390
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.WITH]:
                localctx = RLangParser.Probabilistic_policy_statement_no_sugarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 371
                self.probabilistic_condition()
                self.state = 372
                self.match(RLangParser.COL)
                self.state = 373
                self.match(RLangParser.INDENT)
                self.state = 374
                self.policy_statement()
                self.state = 378
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.NL:
                    self.state = 375
                    self.match(RLangParser.NL)
                    self.state = 380
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 381
                self.match(RLangParser.DEDENT)
                pass
            elif token in [RLangParser.EXECUTE]:
                localctx = RLangParser.Probabilistic_policy_statement_sugarContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 383
                self.execute()
                self.state = 384
                self.probabilistic_condition()
                self.state = 386 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 385
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 388 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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
        self.enterRule(localctx, 46, self.RULE_execute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.match(RLangParser.EXECUTE)
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 393
                self.match(RLangParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 394
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
        self.enterRule(localctx, 48, self.RULE_effect)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(RLangParser.EFFECT)
            self.state = 398
            _la = self._input.LA(1)
            if not(_la==RLangParser.MAIN or _la==RLangParser.IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 399
            self.match(RLangParser.COL)
            self.state = 400
            self.match(RLangParser.INDENT)
            self.state = 401
            self.effect_statement_collection()
            self.state = 402
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
        self.enterRule(localctx, 50, self.RULE_effect_statement_collection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 404
                localctx._effect_statement = self.effect_statement()
                localctx.statements.append(localctx._effect_statement)
                self.state = 408
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.NL:
                    self.state = 405
                    self.match(RLangParser.NL)
                    self.state = 410
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 413 
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
        self.enterRule(localctx, 52, self.RULE_effect_statement)
        try:
            self.state = 420
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Effect_statement_rewardContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 415
                self.reward()
                pass

            elif la_ == 2:
                localctx = RLangParser.Effect_statement_predictionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 416
                self.prediction()
                pass

            elif la_ == 3:
                localctx = RLangParser.Effect_statement_referenceContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 417
                self.effect_reference()
                pass

            elif la_ == 4:
                localctx = RLangParser.Effect_statement_conditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 418
                self.conditional_effect()
                pass

            elif la_ == 5:
                localctx = RLangParser.Effect_statement_probabilisticContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 419
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
        self.enterRule(localctx, 54, self.RULE_conditional_effect)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(RLangParser.IF)
            self.state = 423
            localctx.if_condition = self.boolean_exp(0)
            self.state = 424
            self.match(RLangParser.COL)
            self.state = 425
            self.match(RLangParser.INDENT)
            self.state = 426
            localctx.if_effect = self.effect_statement_collection()
            self.state = 427
            self.match(RLangParser.DEDENT)
            self.state = 437
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.ELIF:
                self.state = 428
                self.match(RLangParser.ELIF)
                self.state = 429
                localctx._boolean_exp = self.boolean_exp(0)
                localctx.elif_conditions.append(localctx._boolean_exp)
                self.state = 430
                self.match(RLangParser.COL)
                self.state = 431
                self.match(RLangParser.INDENT)
                self.state = 432
                localctx._effect_statement_collection = self.effect_statement_collection()
                localctx.elif_effects.append(localctx._effect_statement_collection)
                self.state = 433
                self.match(RLangParser.DEDENT)
                self.state = 439
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 446
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.ELSE:
                self.state = 440
                self.match(RLangParser.ELSE)
                self.state = 441
                self.match(RLangParser.COL)
                self.state = 442
                self.match(RLangParser.INDENT)
                self.state = 443
                localctx.else_effect = self.effect_statement_collection()
                self.state = 444
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
        self.enterRule(localctx, 56, self.RULE_probabilistic_effect)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            localctx._probabilistic_effect_statement = self.probabilistic_effect_statement()
            localctx.effects.append(localctx._probabilistic_effect_statement)
            self.state = 453
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.OR:
                self.state = 449
                self.match(RLangParser.OR)
                self.state = 450
                localctx._probabilistic_effect_statement = self.probabilistic_effect_statement()
                localctx.effects.append(localctx._probabilistic_effect_statement)
                self.state = 455
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
        self.enterRule(localctx, 58, self.RULE_probabilistic_effect_statement)
        try:
            self.state = 473
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.WITH]:
                localctx = RLangParser.Probabilistic_effect_statement_no_sugarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 456
                self.probabilistic_condition()
                self.state = 457
                self.match(RLangParser.COL)
                self.state = 458
                self.match(RLangParser.INDENT)
                self.state = 459
                self.effect_statement_collection()
                self.state = 460
                self.match(RLangParser.DEDENT)
                pass
            elif token in [RLangParser.REWARD, RLangParser.S_PRIME, RLangParser.PREDICT, RLangParser.IDENTIFIER]:
                localctx = RLangParser.Probabilistic_effect_statement_sugarContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 465
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RLangParser.REWARD]:
                    self.state = 462
                    self.reward()
                    pass
                elif token in [RLangParser.S_PRIME, RLangParser.IDENTIFIER]:
                    self.state = 463
                    self.prediction()
                    pass
                elif token in [RLangParser.PREDICT]:
                    self.state = 464
                    self.effect_reference()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 467
                self.probabilistic_condition()
                self.state = 469 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 468
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 471 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

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
        self.enterRule(localctx, 60, self.RULE_reward)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.match(RLangParser.REWARD)
            self.state = 476
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
        self.enterRule(localctx, 62, self.RULE_prediction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.IDENTIFIER]:
                self.state = 478
                self.match(RLangParser.IDENTIFIER)
                self.state = 480
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==RLangParser.PRIME:
                    self.state = 479
                    self.match(RLangParser.PRIME)


                pass
            elif token in [RLangParser.S_PRIME]:
                self.state = 482
                self.match(RLangParser.S_PRIME)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 485
            self.match(RLangParser.PREDICT)
            self.state = 486
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
        self.enterRule(localctx, 64, self.RULE_effect_reference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self.match(RLangParser.PREDICT)
            self.state = 489
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
        self.enterRule(localctx, 66, self.RULE_probabilistic_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self.match(RLangParser.WITH)
            self.state = 492
            self.match(RLangParser.P)
            self.state = 493
            self.match(RLangParser.L_PAR)
            self.state = 496
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 494
                self.any_number()
                pass

            elif la_ == 2:
                self.state = 495
                self.integer_fraction()
                pass


            self.state = 498
            self.match(RLangParser.R_PAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_instantiationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def any_bound_class(self):
            return self.getTypedRuleContext(RLangParser.Any_bound_classContext,0)


        def L_PAR(self):
            return self.getToken(RLangParser.L_PAR, 0)

        def object_constructor_arg_list(self):
            return self.getTypedRuleContext(RLangParser.Object_constructor_arg_listContext,0)


        def R_PAR(self):
            return self.getToken(RLangParser.R_PAR, 0)

        def getRuleIndex(self):
            return RLangParser.RULE_object_instantiation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject_instantiation" ):
                listener.enterObject_instantiation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject_instantiation" ):
                listener.exitObject_instantiation(self)




    def object_instantiation(self):

        localctx = RLangParser.Object_instantiationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_object_instantiation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            self.any_bound_class()
            self.state = 501
            self.match(RLangParser.L_PAR)
            self.state = 502
            self.object_constructor_arg_list()
            self.state = 503
            self.match(RLangParser.R_PAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_constructor_arg_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._object_constructor_arg = None # Object_constructor_argContext
            self.arg_list = list() # of Object_constructor_argContexts

        def COM(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.COM)
            else:
                return self.getToken(RLangParser.COM, i)

        def object_constructor_arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Object_constructor_argContext)
            else:
                return self.getTypedRuleContext(RLangParser.Object_constructor_argContext,i)


        def getRuleIndex(self):
            return RLangParser.RULE_object_constructor_arg_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject_constructor_arg_list" ):
                listener.enterObject_constructor_arg_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject_constructor_arg_list" ):
                listener.exitObject_constructor_arg_list(self)




    def object_constructor_arg_list(self):

        localctx = RLangParser.Object_constructor_arg_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_object_constructor_arg_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 26)) & ~0x3f) == 0 and ((1 << (_la - 26)) & ((1 << (RLangParser.S_PRIME - 26)) | (1 << (RLangParser.S - 26)) | (1 << (RLangParser.A - 26)) | (1 << (RLangParser.NOT - 26)) | (1 << (RLangParser.TRUE - 26)) | (1 << (RLangParser.FALSE - 26)) | (1 << (RLangParser.L_BRK - 26)) | (1 << (RLangParser.L_PAR - 26)) | (1 << (RLangParser.MINUS - 26)) | (1 << (RLangParser.IDENTIFIER - 26)) | (1 << (RLangParser.DECIMAL - 26)) | (1 << (RLangParser.INTEGER - 26)))) != 0):
                self.state = 505
                localctx._object_constructor_arg = self.object_constructor_arg()
                localctx.arg_list.append(localctx._object_constructor_arg)


            self.state = 512
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.COM:
                self.state = 508
                self.match(RLangParser.COM)
                self.state = 509
                localctx._object_constructor_arg = self.object_constructor_arg()
                localctx.arg_list.append(localctx._object_constructor_arg)
                self.state = 514
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_constructor_argContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RLangParser.RULE_object_constructor_arg

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Object_construct_objectContext(Object_constructor_argContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Object_constructor_argContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def an_object(self):
            return self.getTypedRuleContext(RLangParser.An_objectContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject_construct_object" ):
                listener.enterObject_construct_object(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject_construct_object" ):
                listener.exitObject_construct_object(self)


    class Object_construct_bool_expContext(Object_constructor_argContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Object_constructor_argContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def boolean_exp(self):
            return self.getTypedRuleContext(RLangParser.Boolean_expContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject_construct_bool_exp" ):
                listener.enterObject_construct_bool_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject_construct_bool_exp" ):
                listener.exitObject_construct_bool_exp(self)


    class Object_construct_arith_expContext(Object_constructor_argContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Object_constructor_argContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arithmetic_exp(self):
            return self.getTypedRuleContext(RLangParser.Arithmetic_expContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject_construct_arith_exp" ):
                listener.enterObject_construct_arith_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject_construct_arith_exp" ):
                listener.exitObject_construct_arith_exp(self)


    class Object_construct_object_arrayContext(Object_constructor_argContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Object_constructor_argContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def object_array(self):
            return self.getTypedRuleContext(RLangParser.Object_arrayContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject_construct_object_array" ):
                listener.enterObject_construct_object_array(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject_construct_object_array" ):
                listener.exitObject_construct_object_array(self)



    def object_constructor_arg(self):

        localctx = RLangParser.Object_constructor_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_object_constructor_arg)
        try:
            self.state = 519
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Object_construct_objectContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 515
                self.an_object()
                pass

            elif la_ == 2:
                localctx = RLangParser.Object_construct_arith_expContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 516
                self.arithmetic_exp(0)
                pass

            elif la_ == 3:
                localctx = RLangParser.Object_construct_bool_expContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 517
                self.boolean_exp(0)
                pass

            elif la_ == 4:
                localctx = RLangParser.Object_construct_object_arrayContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 518
                self.object_array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_objectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def any_bound_var(self):
            return self.getTypedRuleContext(RLangParser.Any_bound_varContext,0)


        def object_instantiation(self):
            return self.getTypedRuleContext(RLangParser.Object_instantiationContext,0)


        def getRuleIndex(self):
            return RLangParser.RULE_an_object

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_object" ):
                listener.enterAn_object(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_object" ):
                listener.exitAn_object(self)




    def an_object(self):

        localctx = RLangParser.An_objectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_an_object)
        try:
            self.state = 523
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 521
                self.any_bound_var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 522
                self.object_instantiation()
                pass


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
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_arithmetic_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.L_PAR]:
                localctx = RLangParser.Arith_parenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 526
                self.match(RLangParser.L_PAR)
                self.state = 527
                self.arithmetic_exp(0)
                self.state = 528
                self.match(RLangParser.R_PAR)
                pass
            elif token in [RLangParser.MINUS, RLangParser.DECIMAL, RLangParser.INTEGER]:
                localctx = RLangParser.Arith_numberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 530
                self.any_number()
                pass
            elif token in [RLangParser.L_BRK]:
                localctx = RLangParser.Arith_arrayContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 531
                self.any_array()
                pass
            elif token in [RLangParser.S_PRIME, RLangParser.S, RLangParser.A, RLangParser.IDENTIFIER]:
                localctx = RLangParser.Arith_bound_varContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 532
                self.any_bound_var()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 543
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 541
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                    if la_ == 1:
                        localctx = RLangParser.Arith_times_divideContext(self, RLangParser.Arithmetic_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_exp)
                        self.state = 535
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 536
                        _la = self._input.LA(1)
                        if not(_la==RLangParser.TIMES or _la==RLangParser.DIVIDE):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 537
                        localctx.rhs = self.arithmetic_exp(6)
                        pass

                    elif la_ == 2:
                        localctx = RLangParser.Arith_plus_minusContext(self, RLangParser.Arithmetic_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_exp)
                        self.state = 538
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 539
                        _la = self._input.LA(1)
                        if not(_la==RLangParser.PLUS or _la==RLangParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 540
                        localctx.rhs = self.arithmetic_exp(5)
                        pass

             
                self.state = 545
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

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
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_boolean_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 563
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Bool_parenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 547
                self.match(RLangParser.L_PAR)
                self.state = 548
                self.boolean_exp(0)
                self.state = 549
                self.match(RLangParser.R_PAR)
                pass

            elif la_ == 2:
                localctx = RLangParser.Bool_notContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 551
                self.match(RLangParser.NOT)
                self.state = 552
                self.boolean_exp(6)
                pass

            elif la_ == 3:
                localctx = RLangParser.Bool_inContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 553
                localctx.lhs = self.arithmetic_exp(0)
                self.state = 554
                self.match(RLangParser.IN)
                self.state = 555
                localctx.rhs = self.arithmetic_exp(0)
                pass

            elif la_ == 4:
                localctx = RLangParser.Bool_arith_eqContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 557
                localctx.lhs = self.arithmetic_exp(0)
                self.state = 558
                _la = self._input.LA(1)
                if not(((((_la - 54)) & ~0x3f) == 0 and ((1 << (_la - 54)) & ((1 << (RLangParser.EQ_TO - 54)) | (1 << (RLangParser.GT_EQ - 54)) | (1 << (RLangParser.LT_EQ - 54)) | (1 << (RLangParser.NOT_EQ - 54)) | (1 << (RLangParser.LT - 54)) | (1 << (RLangParser.GT - 54)))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 559
                localctx.rhs = self.arithmetic_exp(0)
                pass

            elif la_ == 5:
                localctx = RLangParser.Bool_bound_varContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 561
                self.any_bound_var()
                pass

            elif la_ == 6:
                localctx = RLangParser.Bool_tfContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 562
                _la = self._input.LA(1)
                if not(_la==RLangParser.TRUE or _la==RLangParser.FALSE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 576
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,55,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 574
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
                    if la_ == 1:
                        localctx = RLangParser.Bool_andContext(self, RLangParser.Boolean_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_exp)
                        self.state = 565
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 566
                        self.match(RLangParser.AND)
                        self.state = 567
                        localctx.rhs = self.boolean_exp(9)
                        pass

                    elif la_ == 2:
                        localctx = RLangParser.Bool_orContext(self, RLangParser.Boolean_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_exp)
                        self.state = 568
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 569
                        self.match(RLangParser.OR)
                        self.state = 570
                        localctx.rhs = self.boolean_exp(8)
                        pass

                    elif la_ == 3:
                        localctx = RLangParser.Bool_bool_eqContext(self, RLangParser.Boolean_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_exp)
                        self.state = 571
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 572
                        _la = self._input.LA(1)
                        if not(_la==RLangParser.EQ_TO or _la==RLangParser.NOT_EQ):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 573
                        localctx.rhs = self.boolean_exp(5)
                        pass

             
                self.state = 578
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,55,self._ctx)

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
        self.enterRule(localctx, 80, self.RULE_type_def)
        try:
            self.state = 581
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.LIST, RLangParser.SET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 579
                self.compound_type()
                pass
            elif token in [RLangParser.INT, RLangParser.FLOAT, RLangParser.STR, RLangParser.BOOL, RLangParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 580
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
        self.enterRule(localctx, 82, self.RULE_compound_type)
        self._la = 0 # Token type
        try:
            self.state = 603
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.LIST]:
                localctx = RLangParser.Type_listContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 583
                self.match(RLangParser.LIST)
                self.state = 591
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==RLangParser.L_BRK:
                    self.state = 584
                    self.match(RLangParser.L_BRK)
                    self.state = 587
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [RLangParser.INT, RLangParser.FLOAT, RLangParser.STR, RLangParser.BOOL, RLangParser.IDENTIFIER]:
                        self.state = 585
                        self.simple_type()
                        pass
                    elif token in [RLangParser.LIST, RLangParser.SET]:
                        self.state = 586
                        self.compound_type()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 589
                    self.match(RLangParser.R_BRK)


                pass
            elif token in [RLangParser.SET]:
                localctx = RLangParser.Type_setContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 593
                self.match(RLangParser.SET)
                self.state = 601
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==RLangParser.L_BRK:
                    self.state = 594
                    self.match(RLangParser.L_BRK)
                    self.state = 597
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [RLangParser.INT, RLangParser.FLOAT, RLangParser.STR, RLangParser.BOOL, RLangParser.IDENTIFIER]:
                        self.state = 595
                        self.simple_type()
                        pass
                    elif token in [RLangParser.LIST, RLangParser.SET]:
                        self.state = 596
                        self.compound_type()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 599
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

        def any_bound_class(self):
            return self.getTypedRuleContext(RLangParser.Any_bound_classContext,0)


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
        self.enterRule(localctx, 84, self.RULE_simple_type)
        try:
            self.state = 610
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 605
                self.match(RLangParser.INT)
                pass
            elif token in [RLangParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 606
                self.match(RLangParser.FLOAT)
                pass
            elif token in [RLangParser.STR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 607
                self.match(RLangParser.STR)
                pass
            elif token in [RLangParser.BOOL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 608
                self.match(RLangParser.BOOL)
                pass
            elif token in [RLangParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 5)
                self.state = 609
                self.any_bound_class()
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
        self.enterRule(localctx, 86, self.RULE_any_bound_var)
        try:
            self.state = 631
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.IDENTIFIER]:
                localctx = RLangParser.Bound_identifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 612
                self.match(RLangParser.IDENTIFIER)
                self.state = 614
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
                if la_ == 1:
                    self.state = 613
                    self.match(RLangParser.PRIME)


                self.state = 619
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,64,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 616
                        self.trailer() 
                    self.state = 621
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,64,self._ctx)

                pass
            elif token in [RLangParser.S]:
                localctx = RLangParser.Bound_stateContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 622
                self.match(RLangParser.S)
                self.state = 624
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
                if la_ == 1:
                    self.state = 623
                    self.trailer()


                pass
            elif token in [RLangParser.S_PRIME]:
                localctx = RLangParser.Bound_next_stateContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 626
                self.match(RLangParser.S_PRIME)
                self.state = 628
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
                if la_ == 1:
                    self.state = 627
                    self.trailer()


                pass
            elif token in [RLangParser.A]:
                localctx = RLangParser.Bound_actionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 630
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


    class Any_bound_classContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(RLangParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return RLangParser.RULE_any_bound_class

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAny_bound_class" ):
                listener.enterAny_bound_class(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAny_bound_class" ):
                listener.exitAny_bound_class(self)




    def any_bound_class(self):

        localctx = RLangParser.Any_bound_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_any_bound_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 633
            self.match(RLangParser.IDENTIFIER)
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
        self.enterRule(localctx, 90, self.RULE_trailer)
        try:
            self.state = 637
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Trailer_arrayContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 635
                self.int_array_exp()
                pass

            elif la_ == 2:
                localctx = RLangParser.Trailer_sliceContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 636
                self.slice_exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._an_object = None # An_objectContext
            self.arr = list() # of An_objectContexts

        def L_BRK(self):
            return self.getToken(RLangParser.L_BRK, 0)

        def R_BRK(self):
            return self.getToken(RLangParser.R_BRK, 0)

        def an_object(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.An_objectContext)
            else:
                return self.getTypedRuleContext(RLangParser.An_objectContext,i)


        def COM(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.COM)
            else:
                return self.getToken(RLangParser.COM, i)

        def getRuleIndex(self):
            return RLangParser.RULE_object_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject_array" ):
                listener.enterObject_array(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject_array" ):
                listener.exitObject_array(self)




    def object_array(self):

        localctx = RLangParser.Object_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_object_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 639
            self.match(RLangParser.L_BRK)
            self.state = 640
            localctx._an_object = self.an_object()
            localctx.arr.append(localctx._an_object)
            self.state = 645
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.COM:
                self.state = 641
                self.match(RLangParser.COM)
                self.state = 642
                localctx._an_object = self.an_object()
                localctx.arr.append(localctx._an_object)
                self.state = 647
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 648
            self.match(RLangParser.R_BRK)
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
        self.enterRule(localctx, 94, self.RULE_any_array)
        try:
            self.state = 652
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,70,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Any_array_compoundContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 650
                self.compound_array_exp()
                pass

            elif la_ == 2:
                localctx = RLangParser.Any_array_any_numContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 651
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
        self.enterRule(localctx, 96, self.RULE_compound_array_exp)
        self._la = 0 # Token type
        try:
            self.state = 666
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,72,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Compound_array_simpleContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 654
                self.any_num_array_exp()
                pass

            elif la_ == 2:
                localctx = RLangParser.Compound_array_compoundContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 655
                self.match(RLangParser.L_BRK)
                self.state = 656
                localctx._compound_array_exp = self.compound_array_exp()
                localctx.arr.append(localctx._compound_array_exp)
                self.state = 661
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.COM:
                    self.state = 657
                    self.match(RLangParser.COM)
                    self.state = 658
                    localctx._compound_array_exp = self.compound_array_exp()
                    localctx.arr.append(localctx._compound_array_exp)
                    self.state = 663
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 664
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
        self.enterRule(localctx, 98, self.RULE_int_array_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 668
            self.match(RLangParser.L_BRK)
            self.state = 669
            localctx._any_integer = self.any_integer()
            localctx.arr.append(localctx._any_integer)
            self.state = 674
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.COM:
                self.state = 670
                self.match(RLangParser.COM)
                self.state = 671
                localctx._any_integer = self.any_integer()
                localctx.arr.append(localctx._any_integer)
                self.state = 676
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 677
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
        self.enterRule(localctx, 100, self.RULE_any_num_array_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 679
            self.match(RLangParser.L_BRK)
            self.state = 680
            localctx._any_number = self.any_number()
            localctx.arr.append(localctx._any_number)
            self.state = 685
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.COM:
                self.state = 681
                self.match(RLangParser.COM)
                self.state = 682
                localctx._any_number = self.any_number()
                localctx.arr.append(localctx._any_number)
                self.state = 687
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 688
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
        self.enterRule(localctx, 102, self.RULE_slice_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 690
            self.match(RLangParser.L_BRK)
            self.state = 692
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.MINUS or _la==RLangParser.INTEGER:
                self.state = 691
                localctx.start_ind = self.any_integer()


            self.state = 694
            self.match(RLangParser.COL)
            self.state = 696
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.MINUS or _la==RLangParser.INTEGER:
                self.state = 695
                localctx.stop_ind = self.any_integer()


            self.state = 698
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
        self.enterRule(localctx, 104, self.RULE_integer_fraction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 700
            localctx.lhs = self.any_integer()
            self.state = 701
            self.match(RLangParser.DIVIDE)
            self.state = 702
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
        self.enterRule(localctx, 106, self.RULE_any_number)
        try:
            self.state = 706
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,77,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Any_num_intContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 704
                self.any_integer()
                pass

            elif la_ == 2:
                localctx = RLangParser.Any_num_decContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 705
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
        self.enterRule(localctx, 108, self.RULE_any_integer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 709
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.MINUS:
                self.state = 708
                self.match(RLangParser.MINUS)


            self.state = 711
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
        self.enterRule(localctx, 110, self.RULE_any_decimal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 714
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.MINUS:
                self.state = 713
                self.match(RLangParser.MINUS)


            self.state = 716
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
        self._predicates[38] = self.arithmetic_exp_sempred
        self._predicates[39] = self.boolean_exp_sempred
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
         




