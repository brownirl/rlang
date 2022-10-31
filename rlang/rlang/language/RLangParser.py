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
        buf.write("\u02dd\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\3\2\7")
        buf.write("\2v\n\2\f\2\16\2y\13\2\3\2\3\2\3\2\7\2~\n\2\f\2\16\2\u0081")
        buf.write("\13\2\3\3\3\3\6\3\u0085\n\3\r\3\16\3\u0086\7\3\u0089\n")
        buf.write("\3\f\3\16\3\u008c\13\3\3\4\3\4\3\4\3\5\7\5\u0092\n\5\f")
        buf.write("\5\16\5\u0095\13\5\3\6\3\6\6\6\u0099\n\6\r\6\16\6\u009a")
        buf.write("\3\6\3\6\6\6\u009f\n\6\r\6\16\6\u00a0\3\6\3\6\6\6\u00a5")
        buf.write("\n\6\r\6\16\6\u00a6\3\6\3\6\6\6\u00ab\n\6\r\6\16\6\u00ac")
        buf.write("\3\6\3\6\6\6\u00b1\n\6\r\6\16\6\u00b2\3\6\3\6\6\6\u00b7")
        buf.write("\n\6\r\6\16\6\u00b8\3\6\3\6\6\6\u00bd\n\6\r\6\16\6\u00be")
        buf.write("\3\6\3\6\6\6\u00c3\n\6\r\6\16\6\u00c4\3\6\3\6\3\6\3\6")
        buf.write("\5\6\u00cb\n\6\3\7\3\7\3\7\3\7\3\7\5\7\u00d2\n\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\5\b\u00d9\n\b\3\t\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\5\17\u00ff\n\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\7\20\u0108\n\20\f\20\16\20\u010b")
        buf.write("\13\20\6\20\u010d\n\20\r\20\16\20\u010e\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\7\22")
        buf.write("\u011e\n\22\f\22\16\22\u0121\13\22\3\22\3\22\3\22\3\22")
        buf.write("\7\22\u0127\n\22\f\22\16\22\u012a\13\22\3\22\3\22\3\23")
        buf.write("\3\23\5\23\u0130\n\23\3\24\3\24\3\24\3\24\3\24\3\24\7")
        buf.write("\24\u0138\n\24\f\24\16\24\u013b\13\24\3\24\3\24\3\25\3")
        buf.write("\25\3\25\5\25\u0142\n\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\7\26\u014a\n\26\f\26\16\26\u014d\13\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\7\26\u0156\n\26\f\26\16\26\u0159")
        buf.write("\13\26\3\26\3\26\7\26\u015d\n\26\f\26\16\26\u0160\13\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\7\26\u0167\n\26\f\26\16\26\u016a")
        buf.write("\13\26\3\26\3\26\5\26\u016e\n\26\3\27\3\27\3\27\7\27\u0173")
        buf.write("\n\27\f\27\16\27\u0176\13\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\7\30\u017d\n\30\f\30\16\30\u0180\13\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\6\30\u0187\n\30\r\30\16\30\u0188\5\30\u018b")
        buf.write("\n\30\3\31\3\31\3\31\5\31\u0190\n\31\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\33\3\33\7\33\u019b\n\33\f\33\16\33")
        buf.write("\u019e\13\33\6\33\u01a0\n\33\r\33\16\33\u01a1\3\34\3\34")
        buf.write("\3\34\3\34\3\34\5\34\u01a9\n\34\3\35\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\7\35\u01b8")
        buf.write("\n\35\f\35\16\35\u01bb\13\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\5\35\u01c3\n\35\3\36\3\36\3\36\7\36\u01c8\n\36\f")
        buf.write("\36\16\36\u01cb\13\36\3\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\5\37\u01d6\n\37\3\37\3\37\6\37\u01da\n\37")
        buf.write("\r\37\16\37\u01db\5\37\u01de\n\37\3 \3 \3 \3!\3!\5!\u01e5")
        buf.write("\n!\3!\3!\5!\u01e9\n!\5!\u01eb\n!\3!\3!\3!\3\"\3\"\3\"")
        buf.write("\3#\3#\3#\3#\3#\5#\u01f8\n#\3#\3#\3$\3$\3$\3$\3$\3%\5")
        buf.write("%\u0202\n%\3%\3%\7%\u0206\n%\f%\16%\u0209\13%\3&\3&\3")
        buf.write("&\3&\5&\u020f\n&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u0219")
        buf.write("\n\'\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u0221\n\'\f\'\16\'\u0224")
        buf.write("\13\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(")
        buf.write("\3(\5(\u0237\n(\3(\3(\3(\3(\3(\3(\3(\3(\3(\7(\u0242\n")
        buf.write("(\f(\16(\u0245\13(\3)\3)\5)\u0249\n)\3*\3*\3*\3*\5*\u024f")
        buf.write("\n*\3*\3*\5*\u0253\n*\3*\3*\3*\3*\5*\u0259\n*\3*\3*\5")
        buf.write("*\u025d\n*\5*\u025f\n*\3+\3+\3+\3+\3+\5+\u0266\n+\3,\3")
        buf.write(",\3,\3,\7,\u026c\n,\f,\16,\u026f\13,\3,\3,\3-\3-\5-\u0275")
        buf.write("\n-\3.\3.\5.\u0279\n.\3.\3.\5.\u027d\n.\3.\3.\5.\u0281")
        buf.write("\n.\3.\7.\u0284\n.\f.\16.\u0287\13.\3.\5.\u028a\n.\3/")
        buf.write("\3/\3\60\3\60\3\60\5\60\u0291\n\60\3\61\3\61\6\61\u0295")
        buf.write("\n\61\r\61\16\61\u0296\3\62\3\62\5\62\u029b\n\62\3\63")
        buf.write("\3\63\3\63\3\63\3\63\7\63\u02a2\n\63\f\63\16\63\u02a5")
        buf.write("\13\63\3\63\3\63\5\63\u02a9\n\63\3\64\3\64\3\64\3\64\7")
        buf.write("\64\u02af\n\64\f\64\16\64\u02b2\13\64\3\64\3\64\3\65\3")
        buf.write("\65\3\65\3\65\7\65\u02ba\n\65\f\65\16\65\u02bd\13\65\3")
        buf.write("\65\3\65\3\66\3\66\5\66\u02c3\n\66\3\66\3\66\5\66\u02c7")
        buf.write("\n\66\3\66\3\66\3\67\3\67\3\67\3\67\38\38\58\u02d1\n8")
        buf.write("\39\59\u02d4\n9\39\39\3:\5:\u02d9\n:\3:\3:\3:\2\4LN;\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnpr\2\b\4\2**KK\3\2FG\3")
        buf.write("\2HI\4\28;DE\3\2./\4\288;;\2\u0313\2w\3\2\2\2\4\u008a")
        buf.write("\3\2\2\2\6\u008d\3\2\2\2\b\u0093\3\2\2\2\n\u00ca\3\2\2")
        buf.write("\2\f\u00cc\3\2\2\2\16\u00d3\3\2\2\2\20\u00da\3\2\2\2\22")
        buf.write("\u00df\3\2\2\2\24\u00e4\3\2\2\2\26\u00e9\3\2\2\2\30\u00ee")
        buf.write("\3\2\2\2\32\u00f3\3\2\2\2\34\u00f8\3\2\2\2\36\u010c\3")
        buf.write("\2\2\2 \u0110\3\2\2\2\"\u0114\3\2\2\2$\u012f\3\2\2\2&")
        buf.write("\u0131\3\2\2\2(\u0141\3\2\2\2*\u0143\3\2\2\2,\u016f\3")
        buf.write("\2\2\2.\u018a\3\2\2\2\60\u018c\3\2\2\2\62\u0191\3\2\2")
        buf.write("\2\64\u019f\3\2\2\2\66\u01a8\3\2\2\28\u01aa\3\2\2\2:\u01c4")
        buf.write("\3\2\2\2<\u01dd\3\2\2\2>\u01df\3\2\2\2@\u01ea\3\2\2\2")
        buf.write("B\u01ef\3\2\2\2D\u01f2\3\2\2\2F\u01fb\3\2\2\2H\u0201\3")
        buf.write("\2\2\2J\u020e\3\2\2\2L\u0218\3\2\2\2N\u0236\3\2\2\2P\u0248")
        buf.write("\3\2\2\2R\u025e\3\2\2\2T\u0265\3\2\2\2V\u0267\3\2\2\2")
        buf.write("X\u0274\3\2\2\2Z\u0289\3\2\2\2\\\u028b\3\2\2\2^\u0290")
        buf.write("\3\2\2\2`\u0294\3\2\2\2b\u029a\3\2\2\2d\u02a8\3\2\2\2")
        buf.write("f\u02aa\3\2\2\2h\u02b5\3\2\2\2j\u02c0\3\2\2\2l\u02ca\3")
        buf.write("\2\2\2n\u02d0\3\2\2\2p\u02d3\3\2\2\2r\u02d8\3\2\2\2tv")
        buf.write("\7\5\2\2ut\3\2\2\2vy\3\2\2\2wu\3\2\2\2wx\3\2\2\2xz\3\2")
        buf.write("\2\2yw\3\2\2\2z{\5\4\3\2{\177\5\b\5\2|~\7\5\2\2}|\3\2")
        buf.write("\2\2~\u0081\3\2\2\2\177}\3\2\2\2\177\u0080\3\2\2\2\u0080")
        buf.write("\3\3\2\2\2\u0081\177\3\2\2\2\u0082\u0084\5\6\4\2\u0083")
        buf.write("\u0085\7\5\2\2\u0084\u0083\3\2\2\2\u0085\u0086\3\2\2\2")
        buf.write("\u0086\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0089\3")
        buf.write("\2\2\2\u0088\u0082\3\2\2\2\u0089\u008c\3\2\2\2\u008a\u0088")
        buf.write("\3\2\2\2\u008a\u008b\3\2\2\2\u008b\5\3\2\2\2\u008c\u008a")
        buf.write("\3\2\2\2\u008d\u008e\7\6\2\2\u008e\u008f\7L\2\2\u008f")
        buf.write("\7\3\2\2\2\u0090\u0092\5\n\6\2\u0091\u0090\3\2\2\2\u0092")
        buf.write("\u0095\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0094\3\2\2\2")
        buf.write("\u0094\t\3\2\2\2\u0095\u0093\3\2\2\2\u0096\u0098\5\f\7")
        buf.write("\2\u0097\u0099\7\5\2\2\u0098\u0097\3\2\2\2\u0099\u009a")
        buf.write("\3\2\2\2\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b")
        buf.write("\u00cb\3\2\2\2\u009c\u009e\5\16\b\2\u009d\u009f\7\5\2")
        buf.write("\2\u009e\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u009e")
        buf.write("\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00cb\3\2\2\2\u00a2")
        buf.write("\u00a4\5\20\t\2\u00a3\u00a5\7\5\2\2\u00a4\u00a3\3\2\2")
        buf.write("\2\u00a5\u00a6\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a6\u00a7")
        buf.write("\3\2\2\2\u00a7\u00cb\3\2\2\2\u00a8\u00aa\5\22\n\2\u00a9")
        buf.write("\u00ab\7\5\2\2\u00aa\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2")
        buf.write("\u00ac\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00cb\3")
        buf.write("\2\2\2\u00ae\u00b0\5\24\13\2\u00af\u00b1\7\5\2\2\u00b0")
        buf.write("\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b0\3\2\2\2")
        buf.write("\u00b2\u00b3\3\2\2\2\u00b3\u00cb\3\2\2\2\u00b4\u00b6\5")
        buf.write("\26\f\2\u00b5\u00b7\7\5\2\2\u00b6\u00b5\3\2\2\2\u00b7")
        buf.write("\u00b8\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2")
        buf.write("\u00b9\u00cb\3\2\2\2\u00ba\u00bc\5\30\r\2\u00bb\u00bd")
        buf.write("\7\5\2\2\u00bc\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be")
        buf.write("\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00cb\3\2\2\2")
        buf.write("\u00c0\u00c2\5\32\16\2\u00c1\u00c3\7\5\2\2\u00c2\u00c1")
        buf.write("\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4")
        buf.write("\u00c5\3\2\2\2\u00c5\u00cb\3\2\2\2\u00c6\u00cb\5\34\17")
        buf.write("\2\u00c7\u00cb\5\"\22\2\u00c8\u00cb\5&\24\2\u00c9\u00cb")
        buf.write("\5\62\32\2\u00ca\u0096\3\2\2\2\u00ca\u009c\3\2\2\2\u00ca")
        buf.write("\u00a2\3\2\2\2\u00ca\u00a8\3\2\2\2\u00ca\u00ae\3\2\2\2")
        buf.write("\u00ca\u00b4\3\2\2\2\u00ca\u00ba\3\2\2\2\u00ca\u00c0\3")
        buf.write("\2\2\2\u00ca\u00c6\3\2\2\2\u00ca\u00c7\3\2\2\2\u00ca\u00c8")
        buf.write("\3\2\2\2\u00ca\u00c9\3\2\2\2\u00cb\13\3\2\2\2\u00cc\u00cd")
        buf.write("\7\16\2\2\u00cd\u00ce\7K\2\2\u00ce\u00d1\7\61\2\2\u00cf")
        buf.write("\u00d2\5L\'\2\u00d0\u00d2\5N(\2\u00d1\u00cf\3\2\2\2\u00d1")
        buf.write("\u00d0\3\2\2\2\u00d2\r\3\2\2\2\u00d3\u00d4\7\17\2\2\u00d4")
        buf.write("\u00d5\7K\2\2\u00d5\u00d8\7\61\2\2\u00d6\u00d9\5n8\2\u00d7")
        buf.write("\u00d9\5h\65\2\u00d8\u00d6\3\2\2\2\u00d8\u00d7\3\2\2\2")
        buf.write("\u00d9\17\3\2\2\2\u00da\u00db\7\n\2\2\u00db\u00dc\7K\2")
        buf.write("\2\u00dc\u00dd\7\61\2\2\u00dd\u00de\5Z.\2\u00de\21\3\2")
        buf.write("\2\2\u00df\u00e0\7\7\2\2\u00e0\u00e1\7K\2\2\u00e1\u00e2")
        buf.write("\7\61\2\2\u00e2\u00e3\5N(\2\u00e3\23\3\2\2\2\u00e4\u00e5")
        buf.write("\7\13\2\2\u00e5\u00e6\7K\2\2\u00e6\u00e7\7\61\2\2\u00e7")
        buf.write("\u00e8\5N(\2\u00e8\25\3\2\2\2\u00e9\u00ea\7\t\2\2\u00ea")
        buf.write("\u00eb\7K\2\2\u00eb\u00ec\7\61\2\2\u00ec\u00ed\5L\'\2")
        buf.write("\u00ed\27\3\2\2\2\u00ee\u00ef\7\25\2\2\u00ef\u00f0\7K")
        buf.write("\2\2\u00f0\u00f1\7\61\2\2\u00f1\u00f2\5L\'\2\u00f2\31")
        buf.write("\3\2\2\2\u00f3\u00f4\7\r\2\2\u00f4\u00f5\7K\2\2\u00f5")
        buf.write("\u00f6\7\61\2\2\u00f6\u00f7\5F$\2\u00f7\33\3\2\2\2\u00f8")
        buf.write("\u00f9\7\f\2\2\u00f9\u00fe\7K\2\2\u00fa\u00fb\7B\2\2\u00fb")
        buf.write("\u00fc\5\\/\2\u00fc\u00fd\7C\2\2\u00fd\u00ff\3\2\2\2\u00fe")
        buf.write("\u00fa\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0100\3\2\2\2")
        buf.write("\u0100\u0101\7<\2\2\u0101\u0102\7\3\2\2\u0102\u0103\5")
        buf.write("\36\20\2\u0103\u0104\7\4\2\2\u0104\35\3\2\2\2\u0105\u0109")
        buf.write("\5 \21\2\u0106\u0108\7\5\2\2\u0107\u0106\3\2\2\2\u0108")
        buf.write("\u010b\3\2\2\2\u0109\u0107\3\2\2\2\u0109\u010a\3\2\2\2")
        buf.write("\u010a\u010d\3\2\2\2\u010b\u0109\3\2\2\2\u010c\u0105\3")
        buf.write("\2\2\2\u010d\u010e\3\2\2\2\u010e\u010c\3\2\2\2\u010e\u010f")
        buf.write("\3\2\2\2\u010f\37\3\2\2\2\u0110\u0111\7K\2\2\u0111\u0112")
        buf.write("\7<\2\2\u0112\u0113\5P)\2\u0113!\3\2\2\2\u0114\u0115\7")
        buf.write("\24\2\2\u0115\u0116\7K\2\2\u0116\u0117\7<\2\2\u0117\u0118")
        buf.write("\7\3\2\2\u0118\u0119\7%\2\2\u0119\u011a\5$\23\2\u011a")
        buf.write("\u011b\7\3\2\2\u011b\u011f\5(\25\2\u011c\u011e\7\5\2\2")
        buf.write("\u011d\u011c\3\2\2\2\u011e\u0121\3\2\2\2\u011f\u011d\3")
        buf.write("\2\2\2\u011f\u0120\3\2\2\2\u0120\u0122\3\2\2\2\u0121\u011f")
        buf.write("\3\2\2\2\u0122\u0123\7\4\2\2\u0123\u0124\7&\2\2\u0124")
        buf.write("\u0128\5$\23\2\u0125\u0127\7\5\2\2\u0126\u0125\3\2\2\2")
        buf.write("\u0127\u012a\3\2\2\2\u0128\u0126\3\2\2\2\u0128\u0129\3")
        buf.write("\2\2\2\u0129\u012b\3\2\2\2\u012a\u0128\3\2\2\2\u012b\u012c")
        buf.write("\7\4\2\2\u012c#\3\2\2\2\u012d\u0130\5N(\2\u012e\u0130")
        buf.write("\7\60\2\2\u012f\u012d\3\2\2\2\u012f\u012e\3\2\2\2\u0130")
        buf.write("%\3\2\2\2\u0131\u0132\7\22\2\2\u0132\u0133\t\2\2\2\u0133")
        buf.write("\u0134\7<\2\2\u0134\u0135\7\3\2\2\u0135\u0139\5(\25\2")
        buf.write("\u0136\u0138\7\5\2\2\u0137\u0136\3\2\2\2\u0138\u013b\3")
        buf.write("\2\2\2\u0139\u0137\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u013c")
        buf.write("\3\2\2\2\u013b\u0139\3\2\2\2\u013c\u013d\7\4\2\2\u013d")
        buf.write("\'\3\2\2\2\u013e\u0142\5\60\31\2\u013f\u0142\5*\26\2\u0140")
        buf.write("\u0142\5,\27\2\u0141\u013e\3\2\2\2\u0141\u013f\3\2\2\2")
        buf.write("\u0141\u0140\3\2\2\2\u0142)\3\2\2\2\u0143\u0144\7!\2\2")
        buf.write("\u0144\u0145\5N(\2\u0145\u0146\7<\2\2\u0146\u0147\7\3")
        buf.write("\2\2\u0147\u014b\5(\25\2\u0148\u014a\7\5\2\2\u0149\u0148")
        buf.write("\3\2\2\2\u014a\u014d\3\2\2\2\u014b\u0149\3\2\2\2\u014b")
        buf.write("\u014c\3\2\2\2\u014c\u014e\3\2\2\2\u014d\u014b\3\2\2\2")
        buf.write("\u014e\u015e\7\4\2\2\u014f\u0150\7#\2\2\u0150\u0151\5")
        buf.write("N(\2\u0151\u0152\7<\2\2\u0152\u0153\7\3\2\2\u0153\u0157")
        buf.write("\5(\25\2\u0154\u0156\7\5\2\2\u0155\u0154\3\2\2\2\u0156")
        buf.write("\u0159\3\2\2\2\u0157\u0155\3\2\2\2\u0157\u0158\3\2\2\2")
        buf.write("\u0158\u015a\3\2\2\2\u0159\u0157\3\2\2\2\u015a\u015b\7")
        buf.write("\4\2\2\u015b\u015d\3\2\2\2\u015c\u014f\3\2\2\2\u015d\u0160")
        buf.write("\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015f")
        buf.write("\u016d\3\2\2\2\u0160\u015e\3\2\2\2\u0161\u0162\7\"\2\2")
        buf.write("\u0162\u0163\7<\2\2\u0163\u0164\7\3\2\2\u0164\u0168\5")
        buf.write("(\25\2\u0165\u0167\7\5\2\2\u0166\u0165\3\2\2\2\u0167\u016a")
        buf.write("\3\2\2\2\u0168\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169")
        buf.write("\u016b\3\2\2\2\u016a\u0168\3\2\2\2\u016b\u016c\7\4\2\2")
        buf.write("\u016c\u016e\3\2\2\2\u016d\u0161\3\2\2\2\u016d\u016e\3")
        buf.write("\2\2\2\u016e+\3\2\2\2\u016f\u0174\5.\30\2\u0170\u0171")
        buf.write("\7,\2\2\u0171\u0173\5.\30\2\u0172\u0170\3\2\2\2\u0173")
        buf.write("\u0176\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175\3\2\2\2")
        buf.write("\u0175-\3\2\2\2\u0176\u0174\3\2\2\2\u0177\u0178\5D#\2")
        buf.write("\u0178\u0179\7<\2\2\u0179\u017a\7\3\2\2\u017a\u017e\5")
        buf.write("(\25\2\u017b\u017d\7\5\2\2\u017c\u017b\3\2\2\2\u017d\u0180")
        buf.write("\3\2\2\2\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f")
        buf.write("\u0181\3\2\2\2\u0180\u017e\3\2\2\2\u0181\u0182\7\4\2\2")
        buf.write("\u0182\u018b\3\2\2\2\u0183\u0184\5\60\31\2\u0184\u0186")
        buf.write("\5D#\2\u0185\u0187\7\5\2\2\u0186\u0185\3\2\2\2\u0187\u0188")
        buf.write("\3\2\2\2\u0188\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189")
        buf.write("\u018b\3\2\2\2\u018a\u0177\3\2\2\2\u018a\u0183\3\2\2\2")
        buf.write("\u018b/\3\2\2\2\u018c\u018f\7\23\2\2\u018d\u0190\7K\2")
        buf.write("\2\u018e\u0190\5L\'\2\u018f\u018d\3\2\2\2\u018f\u018e")
        buf.write("\3\2\2\2\u0190\61\3\2\2\2\u0191\u0192\7\20\2\2\u0192\u0193")
        buf.write("\t\2\2\2\u0193\u0194\7<\2\2\u0194\u0195\7\3\2\2\u0195")
        buf.write("\u0196\5\64\33\2\u0196\u0197\7\4\2\2\u0197\63\3\2\2\2")
        buf.write("\u0198\u019c\5\66\34\2\u0199\u019b\7\5\2\2\u019a\u0199")
        buf.write("\3\2\2\2\u019b\u019e\3\2\2\2\u019c\u019a\3\2\2\2\u019c")
        buf.write("\u019d\3\2\2\2\u019d\u01a0\3\2\2\2\u019e\u019c\3\2\2\2")
        buf.write("\u019f\u0198\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u019f\3")
        buf.write("\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\65\3\2\2\2\u01a3\u01a9")
        buf.write("\5> \2\u01a4\u01a9\5@!\2\u01a5\u01a9\5B\"\2\u01a6\u01a9")
        buf.write("\58\35\2\u01a7\u01a9\5:\36\2\u01a8\u01a3\3\2\2\2\u01a8")
        buf.write("\u01a4\3\2\2\2\u01a8\u01a5\3\2\2\2\u01a8\u01a6\3\2\2\2")
        buf.write("\u01a8\u01a7\3\2\2\2\u01a9\67\3\2\2\2\u01aa\u01ab\7!\2")
        buf.write("\2\u01ab\u01ac\5N(\2\u01ac\u01ad\7<\2\2\u01ad\u01ae\7")
        buf.write("\3\2\2\u01ae\u01af\5\64\33\2\u01af\u01b9\7\4\2\2\u01b0")
        buf.write("\u01b1\7#\2\2\u01b1\u01b2\5N(\2\u01b2\u01b3\7<\2\2\u01b3")
        buf.write("\u01b4\7\3\2\2\u01b4\u01b5\5\64\33\2\u01b5\u01b6\7\4\2")
        buf.write("\2\u01b6\u01b8\3\2\2\2\u01b7\u01b0\3\2\2\2\u01b8\u01bb")
        buf.write("\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba")
        buf.write("\u01c2\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bc\u01bd\7\"\2\2")
        buf.write("\u01bd\u01be\7<\2\2\u01be\u01bf\7\3\2\2\u01bf\u01c0\5")
        buf.write("\64\33\2\u01c0\u01c1\7\4\2\2\u01c1\u01c3\3\2\2\2\u01c2")
        buf.write("\u01bc\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c39\3\2\2\2\u01c4")
        buf.write("\u01c9\5<\37\2\u01c5\u01c6\7,\2\2\u01c6\u01c8\5<\37\2")
        buf.write("\u01c7\u01c5\3\2\2\2\u01c8\u01cb\3\2\2\2\u01c9\u01c7\3")
        buf.write("\2\2\2\u01c9\u01ca\3\2\2\2\u01ca;\3\2\2\2\u01cb\u01c9")
        buf.write("\3\2\2\2\u01cc\u01cd\5D#\2\u01cd\u01ce\7<\2\2\u01ce\u01cf")
        buf.write("\7\3\2\2\u01cf\u01d0\5\64\33\2\u01d0\u01d1\7\4\2\2\u01d1")
        buf.write("\u01de\3\2\2\2\u01d2\u01d6\5> \2\u01d3\u01d6\5@!\2\u01d4")
        buf.write("\u01d6\5B\"\2\u01d5\u01d2\3\2\2\2\u01d5\u01d3\3\2\2\2")
        buf.write("\u01d5\u01d4\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7\u01d9\5")
        buf.write("D#\2\u01d8\u01da\7\5\2\2\u01d9\u01d8\3\2\2\2\u01da\u01db")
        buf.write("\3\2\2\2\u01db\u01d9\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc")
        buf.write("\u01de\3\2\2\2\u01dd\u01cc\3\2\2\2\u01dd\u01d5\3\2\2\2")
        buf.write("\u01de=\3\2\2\2\u01df\u01e0\7\21\2\2\u01e0\u01e1\5L\'")
        buf.write("\2\u01e1?\3\2\2\2\u01e2\u01e4\7\34\2\2\u01e3\u01e5\5`")
        buf.write("\61\2\u01e4\u01e3\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01eb")
        buf.write("\3\2\2\2\u01e6\u01e8\7K\2\2\u01e7\u01e9\7 \2\2\u01e8\u01e7")
        buf.write("\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01eb\3\2\2\2\u01ea")
        buf.write("\u01e2\3\2\2\2\u01ea\u01e6\3\2\2\2\u01eb\u01ec\3\2\2\2")
        buf.write("\u01ec\u01ed\7\62\2\2\u01ed\u01ee\5L\'\2\u01eeA\3\2\2")
        buf.write("\2\u01ef\u01f0\7\62\2\2\u01f0\u01f1\7K\2\2\u01f1C\3\2")
        buf.write("\2\2\u01f2\u01f3\7\'\2\2\u01f3\u01f4\7\37\2\2\u01f4\u01f7")
        buf.write("\7B\2\2\u01f5\u01f8\5n8\2\u01f6\u01f8\5l\67\2\u01f7\u01f5")
        buf.write("\3\2\2\2\u01f7\u01f6\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9")
        buf.write("\u01fa\7C\2\2\u01faE\3\2\2\2\u01fb\u01fc\5\\/\2\u01fc")
        buf.write("\u01fd\7B\2\2\u01fd\u01fe\5H%\2\u01fe\u01ff\7C\2\2\u01ff")
        buf.write("G\3\2\2\2\u0200\u0202\5J&\2\u0201\u0200\3\2\2\2\u0201")
        buf.write("\u0202\3\2\2\2\u0202\u0207\3\2\2\2\u0203\u0204\7=\2\2")
        buf.write("\u0204\u0206\5J&\2\u0205\u0203\3\2\2\2\u0206\u0209\3\2")
        buf.write("\2\2\u0207\u0205\3\2\2\2\u0207\u0208\3\2\2\2\u0208I\3")
        buf.write("\2\2\2\u0209\u0207\3\2\2\2\u020a\u020f\5F$\2\u020b\u020f")
        buf.write("\5L\'\2\u020c\u020f\5N(\2\u020d\u020f\5V,\2\u020e\u020a")
        buf.write("\3\2\2\2\u020e\u020b\3\2\2\2\u020e\u020c\3\2\2\2\u020e")
        buf.write("\u020d\3\2\2\2\u020fK\3\2\2\2\u0210\u0211\b\'\1\2\u0211")
        buf.write("\u0212\7B\2\2\u0212\u0213\5L\'\2\u0213\u0214\7C\2\2\u0214")
        buf.write("\u0219\3\2\2\2\u0215\u0219\5n8\2\u0216\u0219\5b\62\2\u0217")
        buf.write("\u0219\5Z.\2\u0218\u0210\3\2\2\2\u0218\u0215\3\2\2\2\u0218")
        buf.write("\u0216\3\2\2\2\u0218\u0217\3\2\2\2\u0219\u0222\3\2\2\2")
        buf.write("\u021a\u021b\f\7\2\2\u021b\u021c\t\3\2\2\u021c\u0221\5")
        buf.write("L\'\b\u021d\u021e\f\6\2\2\u021e\u021f\t\4\2\2\u021f\u0221")
        buf.write("\5L\'\7\u0220\u021a\3\2\2\2\u0220\u021d\3\2\2\2\u0221")
        buf.write("\u0224\3\2\2\2\u0222\u0220\3\2\2\2\u0222\u0223\3\2\2\2")
        buf.write("\u0223M\3\2\2\2\u0224\u0222\3\2\2\2\u0225\u0226\b(\1\2")
        buf.write("\u0226\u0227\7B\2\2\u0227\u0228\5N(\2\u0228\u0229\7C\2")
        buf.write("\2\u0229\u0237\3\2\2\2\u022a\u022b\7-\2\2\u022b\u0237")
        buf.write("\5N(\b\u022c\u022d\5L\'\2\u022d\u022e\7$\2\2\u022e\u022f")
        buf.write("\5L\'\2\u022f\u0237\3\2\2\2\u0230\u0231\5L\'\2\u0231\u0232")
        buf.write("\t\5\2\2\u0232\u0233\5L\'\2\u0233\u0237\3\2\2\2\u0234")
        buf.write("\u0237\5Z.\2\u0235\u0237\t\6\2\2\u0236\u0225\3\2\2\2\u0236")
        buf.write("\u022a\3\2\2\2\u0236\u022c\3\2\2\2\u0236\u0230\3\2\2\2")
        buf.write("\u0236\u0234\3\2\2\2\u0236\u0235\3\2\2\2\u0237\u0243\3")
        buf.write("\2\2\2\u0238\u0239\f\n\2\2\u0239\u023a\7+\2\2\u023a\u0242")
        buf.write("\5N(\13\u023b\u023c\f\t\2\2\u023c\u023d\7,\2\2\u023d\u0242")
        buf.write("\5N(\n\u023e\u023f\f\6\2\2\u023f\u0240\t\7\2\2\u0240\u0242")
        buf.write("\5N(\7\u0241\u0238\3\2\2\2\u0241\u023b\3\2\2\2\u0241\u023e")
        buf.write("\3\2\2\2\u0242\u0245\3\2\2\2\u0243\u0241\3\2\2\2\u0243")
        buf.write("\u0244\3\2\2\2\u0244O\3\2\2\2\u0245\u0243\3\2\2\2\u0246")
        buf.write("\u0249\5R*\2\u0247\u0249\5T+\2\u0248\u0246\3\2\2\2\u0248")
        buf.write("\u0247\3\2\2\2\u0249Q\3\2\2\2\u024a\u0252\7\31\2\2\u024b")
        buf.write("\u024e\7>\2\2\u024c\u024f\5T+\2\u024d\u024f\5R*\2\u024e")
        buf.write("\u024c\3\2\2\2\u024e\u024d\3\2\2\2\u024f\u0250\3\2\2\2")
        buf.write("\u0250\u0251\7?\2\2\u0251\u0253\3\2\2\2\u0252\u024b\3")
        buf.write("\2\2\2\u0252\u0253\3\2\2\2\u0253\u025f\3\2\2\2\u0254\u025c")
        buf.write("\7\32\2\2\u0255\u0258\7>\2\2\u0256\u0259\5T+\2\u0257\u0259")
        buf.write("\5R*\2\u0258\u0256\3\2\2\2\u0258\u0257\3\2\2\2\u0259\u025a")
        buf.write("\3\2\2\2\u025a\u025b\7?\2\2\u025b\u025d\3\2\2\2\u025c")
        buf.write("\u0255\3\2\2\2\u025c\u025d\3\2\2\2\u025d\u025f\3\2\2\2")
        buf.write("\u025e\u024a\3\2\2\2\u025e\u0254\3\2\2\2\u025fS\3\2\2")
        buf.write("\2\u0260\u0266\7\26\2\2\u0261\u0266\7\27\2\2\u0262\u0266")
        buf.write("\7\30\2\2\u0263\u0266\7\33\2\2\u0264\u0266\5\\/\2\u0265")
        buf.write("\u0260\3\2\2\2\u0265\u0261\3\2\2\2\u0265\u0262\3\2\2\2")
        buf.write("\u0265\u0263\3\2\2\2\u0265\u0264\3\2\2\2\u0266U\3\2\2")
        buf.write("\2\u0267\u0268\7>\2\2\u0268\u026d\5X-\2\u0269\u026a\7")
        buf.write("=\2\2\u026a\u026c\5X-\2\u026b\u0269\3\2\2\2\u026c\u026f")
        buf.write("\3\2\2\2\u026d\u026b\3\2\2\2\u026d\u026e\3\2\2\2\u026e")
        buf.write("\u0270\3\2\2\2\u026f\u026d\3\2\2\2\u0270\u0271\7?\2\2")
        buf.write("\u0271W\3\2\2\2\u0272\u0275\5Z.\2\u0273\u0275\5F$\2\u0274")
        buf.write("\u0272\3\2\2\2\u0274\u0273\3\2\2\2\u0275Y\3\2\2\2\u0276")
        buf.write("\u0278\7\35\2\2\u0277\u0279\5^\60\2\u0278\u0277\3\2\2")
        buf.write("\2\u0278\u0279\3\2\2\2\u0279\u028a\3\2\2\2\u027a\u027c")
        buf.write("\7\34\2\2\u027b\u027d\5^\60\2\u027c\u027b\3\2\2\2\u027c")
        buf.write("\u027d\3\2\2\2\u027d\u028a\3\2\2\2\u027e\u0280\7K\2\2")
        buf.write("\u027f\u0281\7 \2\2\u0280\u027f\3\2\2\2\u0280\u0281\3")
        buf.write("\2\2\2\u0281\u0285\3\2\2\2\u0282\u0284\5^\60\2\u0283\u0282")
        buf.write("\3\2\2\2\u0284\u0287\3\2\2\2\u0285\u0283\3\2\2\2\u0285")
        buf.write("\u0286\3\2\2\2\u0286\u028a\3\2\2\2\u0287\u0285\3\2\2\2")
        buf.write("\u0288\u028a\7\36\2\2\u0289\u0276\3\2\2\2\u0289\u027a")
        buf.write("\3\2\2\2\u0289\u027e\3\2\2\2\u0289\u0288\3\2\2\2\u028a")
        buf.write("[\3\2\2\2\u028b\u028c\7K\2\2\u028c]\3\2\2\2\u028d\u0291")
        buf.write("\5f\64\2\u028e\u0291\5j\66\2\u028f\u0291\5`\61\2\u0290")
        buf.write("\u028d\3\2\2\2\u0290\u028e\3\2\2\2\u0290\u028f\3\2\2\2")
        buf.write("\u0291_\3\2\2\2\u0292\u0293\7O\2\2\u0293\u0295\7K\2\2")
        buf.write("\u0294\u0292\3\2\2\2\u0295\u0296\3\2\2\2\u0296\u0294\3")
        buf.write("\2\2\2\u0296\u0297\3\2\2\2\u0297a\3\2\2\2\u0298\u029b")
        buf.write("\5d\63\2\u0299\u029b\5h\65\2\u029a\u0298\3\2\2\2\u029a")
        buf.write("\u0299\3\2\2\2\u029bc\3\2\2\2\u029c\u02a9\5h\65\2\u029d")
        buf.write("\u029e\7>\2\2\u029e\u02a3\5d\63\2\u029f\u02a0\7=\2\2\u02a0")
        buf.write("\u02a2\5d\63\2\u02a1\u029f\3\2\2\2\u02a2\u02a5\3\2\2\2")
        buf.write("\u02a3\u02a1\3\2\2\2\u02a3\u02a4\3\2\2\2\u02a4\u02a6\3")
        buf.write("\2\2\2\u02a5\u02a3\3\2\2\2\u02a6\u02a7\7?\2\2\u02a7\u02a9")
        buf.write("\3\2\2\2\u02a8\u029c\3\2\2\2\u02a8\u029d\3\2\2\2\u02a9")
        buf.write("e\3\2\2\2\u02aa\u02ab\7>\2\2\u02ab\u02b0\5p9\2\u02ac\u02ad")
        buf.write("\7=\2\2\u02ad\u02af\5p9\2\u02ae\u02ac\3\2\2\2\u02af\u02b2")
        buf.write("\3\2\2\2\u02b0\u02ae\3\2\2\2\u02b0\u02b1\3\2\2\2\u02b1")
        buf.write("\u02b3\3\2\2\2\u02b2\u02b0\3\2\2\2\u02b3\u02b4\7?\2\2")
        buf.write("\u02b4g\3\2\2\2\u02b5\u02b6\7>\2\2\u02b6\u02bb\5n8\2\u02b7")
        buf.write("\u02b8\7=\2\2\u02b8\u02ba\5n8\2\u02b9\u02b7\3\2\2\2\u02ba")
        buf.write("\u02bd\3\2\2\2\u02bb\u02b9\3\2\2\2\u02bb\u02bc\3\2\2\2")
        buf.write("\u02bc\u02be\3\2\2\2\u02bd\u02bb\3\2\2\2\u02be\u02bf\7")
        buf.write("?\2\2\u02bfi\3\2\2\2\u02c0\u02c2\7>\2\2\u02c1\u02c3\5")
        buf.write("p9\2\u02c2\u02c1\3\2\2\2\u02c2\u02c3\3\2\2\2\u02c3\u02c4")
        buf.write("\3\2\2\2\u02c4\u02c6\7<\2\2\u02c5\u02c7\5p9\2\u02c6\u02c5")
        buf.write("\3\2\2\2\u02c6\u02c7\3\2\2\2\u02c7\u02c8\3\2\2\2\u02c8")
        buf.write("\u02c9\7?\2\2\u02c9k\3\2\2\2\u02ca\u02cb\5p9\2\u02cb\u02cc")
        buf.write("\7G\2\2\u02cc\u02cd\5p9\2\u02cdm\3\2\2\2\u02ce\u02d1\5")
        buf.write("p9\2\u02cf\u02d1\5r:\2\u02d0\u02ce\3\2\2\2\u02d0\u02cf")
        buf.write("\3\2\2\2\u02d1o\3\2\2\2\u02d2\u02d4\7I\2\2\u02d3\u02d2")
        buf.write("\3\2\2\2\u02d3\u02d4\3\2\2\2\u02d4\u02d5\3\2\2\2\u02d5")
        buf.write("\u02d6\7N\2\2\u02d6q\3\2\2\2\u02d7\u02d9\7I\2\2\u02d8")
        buf.write("\u02d7\3\2\2\2\u02d8\u02d9\3\2\2\2\u02d9\u02da\3\2\2\2")
        buf.write("\u02da\u02db\7M\2\2\u02dbs\3\2\2\2Tw\177\u0086\u008a\u0093")
        buf.write("\u009a\u00a0\u00a6\u00ac\u00b2\u00b8\u00be\u00c4\u00ca")
        buf.write("\u00d1\u00d8\u00fe\u0109\u010e\u011f\u0128\u012f\u0139")
        buf.write("\u0141\u014b\u0157\u015e\u0168\u016d\u0174\u017e\u0188")
        buf.write("\u018a\u018f\u019c\u01a1\u01a8\u01b9\u01c2\u01c9\u01d5")
        buf.write("\u01db\u01dd\u01e4\u01e8\u01ea\u01f7\u0201\u0207\u020e")
        buf.write("\u0218\u0220\u0222\u0236\u0241\u0243\u0248\u024e\u0252")
        buf.write("\u0258\u025c\u025e\u0265\u026d\u0274\u0278\u027c\u0280")
        buf.write("\u0285\u0289\u0290\u0296\u029a\u02a3\u02a8\u02b0\u02bb")
        buf.write("\u02c2\u02c6\u02d0\u02d3\u02d8")
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
                      "PLUS", "MINUS", "QUOTE", "IDENTIFIER", "FNAME", "DECIMAL", 
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
    RULE_arithmetic_exp = 37
    RULE_boolean_exp = 38
    RULE_type_def = 39
    RULE_compound_type = 40
    RULE_simple_type = 41
    RULE_object_array = 42
    RULE_an_object = 43
    RULE_any_bound_var = 44
    RULE_any_bound_class = 45
    RULE_trailer = 46
    RULE_dot_exp = 47
    RULE_any_array = 48
    RULE_compound_array_exp = 49
    RULE_int_array_exp = 50
    RULE_any_num_array_exp = 51
    RULE_slice_exp = 52
    RULE_integer_fraction = 53
    RULE_any_number = 54
    RULE_any_integer = 55
    RULE_any_decimal = 56

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
                   "object_constructor_arg", "arithmetic_exp", "boolean_exp", 
                   "type_def", "compound_type", "simple_type", "object_array", 
                   "an_object", "any_bound_var", "any_bound_class", "trailer", 
                   "dot_exp", "any_array", "compound_array_exp", "int_array_exp", 
                   "any_num_array_exp", "slice_exp", "integer_fraction", 
                   "any_number", "any_integer", "any_decimal" ]

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
    IDENTIFIER=73
    FNAME=74
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
            self.state = 117
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 114
                    self.match(RLangParser.NL) 
                self.state = 119
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 120
            self.imports()
            self.state = 121
            self.declarations()
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.NL:
                self.state = 122
                self.match(RLangParser.NL)
                self.state = 127
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
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.IMPORT:
                self.state = 128
                self.import_stat()
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
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                self.state = 138
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
            self.state = 139
            self.match(RLangParser.IMPORT)
            self.state = 140
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
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RLangParser.PROPOSITION) | (1 << RLangParser.FEATURE) | (1 << RLangParser.FACTOR) | (1 << RLangParser.GOAL) | (1 << RLangParser.CLASS) | (1 << RLangParser.OBJECT) | (1 << RLangParser.CONSTANT) | (1 << RLangParser.ACTION) | (1 << RLangParser.EFFECT) | (1 << RLangParser.POLICY) | (1 << RLangParser.OPTION) | (1 << RLangParser.MARKOVFEATURE))) != 0):
                self.state = 142
                self.dec()
                self.state = 147
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
            self.state = 200
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.CONSTANT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.constant()
                self.state = 150 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 149
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 152 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                pass
            elif token in [RLangParser.ACTION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.action()
                self.state = 156 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 155
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 158 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                pass
            elif token in [RLangParser.FACTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 160
                self.factor()
                self.state = 162 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 161
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 164 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                pass
            elif token in [RLangParser.PROPOSITION]:
                self.enterOuterAlt(localctx, 4)
                self.state = 166
                self.proposition()
                self.state = 168 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 167
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 170 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                pass
            elif token in [RLangParser.GOAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 172
                self.goal()
                self.state = 174 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 173
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 176 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                pass
            elif token in [RLangParser.FEATURE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 178
                self.feature()
                self.state = 180 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 179
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 182 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                pass
            elif token in [RLangParser.MARKOVFEATURE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 184
                self.markov_feature()
                self.state = 186 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 185
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 188 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                pass
            elif token in [RLangParser.OBJECT]:
                self.enterOuterAlt(localctx, 8)
                self.state = 190
                self.object_def()
                self.state = 192 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 191
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 194 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                pass
            elif token in [RLangParser.CLASS]:
                self.enterOuterAlt(localctx, 9)
                self.state = 196
                self.class_def()
                pass
            elif token in [RLangParser.OPTION]:
                self.enterOuterAlt(localctx, 10)
                self.state = 197
                self.option()
                pass
            elif token in [RLangParser.POLICY]:
                self.enterOuterAlt(localctx, 11)
                self.state = 198
                self.policy()
                pass
            elif token in [RLangParser.EFFECT]:
                self.enterOuterAlt(localctx, 12)
                self.state = 199
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
            self.state = 202
            self.match(RLangParser.CONSTANT)
            self.state = 203
            self.match(RLangParser.IDENTIFIER)
            self.state = 204
            self.match(RLangParser.BIND)
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 205
                self.arithmetic_exp(0)
                pass

            elif la_ == 2:
                self.state = 206
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
            self.state = 209
            self.match(RLangParser.ACTION)
            self.state = 210
            self.match(RLangParser.IDENTIFIER)
            self.state = 211
            self.match(RLangParser.BIND)
            self.state = 214
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.MINUS, RLangParser.DECIMAL, RLangParser.INTEGER]:
                self.state = 212
                self.any_number()
                pass
            elif token in [RLangParser.L_BRK]:
                self.state = 213
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
            self.state = 216
            self.match(RLangParser.FACTOR)
            self.state = 217
            self.match(RLangParser.IDENTIFIER)
            self.state = 218
            self.match(RLangParser.BIND)
            self.state = 219
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
            self.state = 221
            self.match(RLangParser.PROPOSITION)
            self.state = 222
            self.match(RLangParser.IDENTIFIER)
            self.state = 223
            self.match(RLangParser.BIND)
            self.state = 224
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
            self.state = 226
            self.match(RLangParser.GOAL)
            self.state = 227
            self.match(RLangParser.IDENTIFIER)
            self.state = 228
            self.match(RLangParser.BIND)
            self.state = 229
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
            self.state = 231
            self.match(RLangParser.FEATURE)
            self.state = 232
            self.match(RLangParser.IDENTIFIER)
            self.state = 233
            self.match(RLangParser.BIND)
            self.state = 234
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
            self.state = 236
            self.match(RLangParser.MARKOVFEATURE)
            self.state = 237
            self.match(RLangParser.IDENTIFIER)
            self.state = 238
            self.match(RLangParser.BIND)
            self.state = 239
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
            self.state = 241
            self.match(RLangParser.OBJECT)
            self.state = 242
            self.match(RLangParser.IDENTIFIER)
            self.state = 243
            self.match(RLangParser.BIND)
            self.state = 244
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
            self.state = 246
            self.match(RLangParser.CLASS)
            self.state = 247
            self.match(RLangParser.IDENTIFIER)
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.L_PAR:
                self.state = 248
                self.match(RLangParser.L_PAR)
                self.state = 249
                self.any_bound_class()
                self.state = 250
                self.match(RLangParser.R_PAR)


            self.state = 254
            self.match(RLangParser.COL)
            self.state = 255
            self.match(RLangParser.INDENT)
            self.state = 256
            self.attribute_definition_collection()
            self.state = 257
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
            self.state = 266 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 259
                localctx._attribute_definition = self.attribute_definition()
                localctx.definitions.append(localctx._attribute_definition)
                self.state = 263
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.NL:
                    self.state = 260
                    self.match(RLangParser.NL)
                    self.state = 265
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 268 
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
            self.state = 270
            self.match(RLangParser.IDENTIFIER)
            self.state = 271
            self.match(RLangParser.COL)
            self.state = 272
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
            self.state = 274
            self.match(RLangParser.OPTION)
            self.state = 275
            self.match(RLangParser.IDENTIFIER)
            self.state = 276
            self.match(RLangParser.COL)
            self.state = 277
            self.match(RLangParser.INDENT)
            self.state = 278
            self.match(RLangParser.INIT)
            self.state = 279
            localctx.init = self.option_condition()
            self.state = 280
            self.match(RLangParser.INDENT)
            self.state = 281
            self.policy_statement()
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.NL:
                self.state = 282
                self.match(RLangParser.NL)
                self.state = 287
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 288
            self.match(RLangParser.DEDENT)
            self.state = 289
            self.match(RLangParser.UNTIL)
            self.state = 290
            localctx.until = self.option_condition()
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.NL:
                self.state = 291
                self.match(RLangParser.NL)
                self.state = 296
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 297
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
            self.state = 301
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.S_PRIME, RLangParser.S, RLangParser.A, RLangParser.NOT, RLangParser.TRUE, RLangParser.FALSE, RLangParser.L_BRK, RLangParser.L_PAR, RLangParser.MINUS, RLangParser.IDENTIFIER, RLangParser.DECIMAL, RLangParser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.boolean_exp(0)
                pass
            elif token in [RLangParser.ANY_CONDITION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
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
            self.state = 303
            self.match(RLangParser.POLICY)
            self.state = 304
            _la = self._input.LA(1)
            if not(_la==RLangParser.MAIN or _la==RLangParser.IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 305
            self.match(RLangParser.COL)
            self.state = 306
            self.match(RLangParser.INDENT)
            self.state = 307
            self.policy_statement()
            self.state = 311
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.NL:
                self.state = 308
                self.match(RLangParser.NL)
                self.state = 313
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 314
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
            self.state = 319
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Policy_statement_executeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.execute()
                pass

            elif la_ == 2:
                localctx = RLangParser.Policy_statement_conditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.conditional_subpolicy()
                pass

            elif la_ == 3:
                localctx = RLangParser.Policy_statement_probabilisticContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 318
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
            self.state = 321
            self.match(RLangParser.IF)
            self.state = 322
            localctx.if_condition = self.boolean_exp(0)
            self.state = 323
            self.match(RLangParser.COL)
            self.state = 324
            self.match(RLangParser.INDENT)
            self.state = 325
            localctx.if_subpolicy = self.policy_statement()
            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.NL:
                self.state = 326
                self.match(RLangParser.NL)
                self.state = 331
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 332
            self.match(RLangParser.DEDENT)
            self.state = 348
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.ELIF:
                self.state = 333
                self.match(RLangParser.ELIF)
                self.state = 334
                localctx._boolean_exp = self.boolean_exp(0)
                localctx.elif_conditions.append(localctx._boolean_exp)
                self.state = 335
                self.match(RLangParser.COL)
                self.state = 336
                self.match(RLangParser.INDENT)
                self.state = 337
                localctx._policy_statement = self.policy_statement()
                localctx.elif_subpolicies.append(localctx._policy_statement)
                self.state = 341
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.NL:
                    self.state = 338
                    self.match(RLangParser.NL)
                    self.state = 343
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 344
                self.match(RLangParser.DEDENT)
                self.state = 350
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 363
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.ELSE:
                self.state = 351
                self.match(RLangParser.ELSE)
                self.state = 352
                self.match(RLangParser.COL)
                self.state = 353
                self.match(RLangParser.INDENT)
                self.state = 354
                localctx.else_subpolicy = self.policy_statement()
                self.state = 358
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.NL:
                    self.state = 355
                    self.match(RLangParser.NL)
                    self.state = 360
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 361
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
            self.state = 365
            localctx._probabilistic_policy_statement = self.probabilistic_policy_statement()
            localctx.subpolicies.append(localctx._probabilistic_policy_statement)
            self.state = 370
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.OR:
                self.state = 366
                self.match(RLangParser.OR)
                self.state = 367
                localctx._probabilistic_policy_statement = self.probabilistic_policy_statement()
                localctx.subpolicies.append(localctx._probabilistic_policy_statement)
                self.state = 372
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
            self.state = 392
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.WITH]:
                localctx = RLangParser.Probabilistic_policy_statement_no_sugarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.probabilistic_condition()
                self.state = 374
                self.match(RLangParser.COL)
                self.state = 375
                self.match(RLangParser.INDENT)
                self.state = 376
                self.policy_statement()
                self.state = 380
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.NL:
                    self.state = 377
                    self.match(RLangParser.NL)
                    self.state = 382
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 383
                self.match(RLangParser.DEDENT)
                pass
            elif token in [RLangParser.EXECUTE]:
                localctx = RLangParser.Probabilistic_policy_statement_sugarContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 385
                self.execute()
                self.state = 386
                self.probabilistic_condition()
                self.state = 388 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 387
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 390 
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
            self.state = 394
            self.match(RLangParser.EXECUTE)
            self.state = 397
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 395
                self.match(RLangParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 396
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
            self.state = 399
            self.match(RLangParser.EFFECT)
            self.state = 400
            _la = self._input.LA(1)
            if not(_la==RLangParser.MAIN or _la==RLangParser.IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 401
            self.match(RLangParser.COL)
            self.state = 402
            self.match(RLangParser.INDENT)
            self.state = 403
            self.effect_statement_collection()
            self.state = 404
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
            self.state = 413 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 406
                localctx._effect_statement = self.effect_statement()
                localctx.statements.append(localctx._effect_statement)
                self.state = 410
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.NL:
                    self.state = 407
                    self.match(RLangParser.NL)
                    self.state = 412
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 415 
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
            self.state = 422
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Effect_statement_rewardContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 417
                self.reward()
                pass

            elif la_ == 2:
                localctx = RLangParser.Effect_statement_predictionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 418
                self.prediction()
                pass

            elif la_ == 3:
                localctx = RLangParser.Effect_statement_referenceContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 419
                self.effect_reference()
                pass

            elif la_ == 4:
                localctx = RLangParser.Effect_statement_conditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 420
                self.conditional_effect()
                pass

            elif la_ == 5:
                localctx = RLangParser.Effect_statement_probabilisticContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 421
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
            self.state = 424
            self.match(RLangParser.IF)
            self.state = 425
            localctx.if_condition = self.boolean_exp(0)
            self.state = 426
            self.match(RLangParser.COL)
            self.state = 427
            self.match(RLangParser.INDENT)
            self.state = 428
            localctx.if_effect = self.effect_statement_collection()
            self.state = 429
            self.match(RLangParser.DEDENT)
            self.state = 439
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.ELIF:
                self.state = 430
                self.match(RLangParser.ELIF)
                self.state = 431
                localctx._boolean_exp = self.boolean_exp(0)
                localctx.elif_conditions.append(localctx._boolean_exp)
                self.state = 432
                self.match(RLangParser.COL)
                self.state = 433
                self.match(RLangParser.INDENT)
                self.state = 434
                localctx._effect_statement_collection = self.effect_statement_collection()
                localctx.elif_effects.append(localctx._effect_statement_collection)
                self.state = 435
                self.match(RLangParser.DEDENT)
                self.state = 441
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 448
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.ELSE:
                self.state = 442
                self.match(RLangParser.ELSE)
                self.state = 443
                self.match(RLangParser.COL)
                self.state = 444
                self.match(RLangParser.INDENT)
                self.state = 445
                localctx.else_effect = self.effect_statement_collection()
                self.state = 446
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
            self.state = 450
            localctx._probabilistic_effect_statement = self.probabilistic_effect_statement()
            localctx.effects.append(localctx._probabilistic_effect_statement)
            self.state = 455
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.OR:
                self.state = 451
                self.match(RLangParser.OR)
                self.state = 452
                localctx._probabilistic_effect_statement = self.probabilistic_effect_statement()
                localctx.effects.append(localctx._probabilistic_effect_statement)
                self.state = 457
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
            self.state = 475
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.WITH]:
                localctx = RLangParser.Probabilistic_effect_statement_no_sugarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 458
                self.probabilistic_condition()
                self.state = 459
                self.match(RLangParser.COL)
                self.state = 460
                self.match(RLangParser.INDENT)
                self.state = 461
                self.effect_statement_collection()
                self.state = 462
                self.match(RLangParser.DEDENT)
                pass
            elif token in [RLangParser.REWARD, RLangParser.S_PRIME, RLangParser.PREDICT, RLangParser.IDENTIFIER]:
                localctx = RLangParser.Probabilistic_effect_statement_sugarContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 467
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RLangParser.REWARD]:
                    self.state = 464
                    self.reward()
                    pass
                elif token in [RLangParser.S_PRIME, RLangParser.IDENTIFIER]:
                    self.state = 465
                    self.prediction()
                    pass
                elif token in [RLangParser.PREDICT]:
                    self.state = 466
                    self.effect_reference()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 469
                self.probabilistic_condition()
                self.state = 471 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 470
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 473 
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
            self.state = 477
            self.match(RLangParser.REWARD)
            self.state = 478
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


        def S_PRIME(self):
            return self.getToken(RLangParser.S_PRIME, 0)

        def IDENTIFIER(self):
            return self.getToken(RLangParser.IDENTIFIER, 0)

        def dot_exp(self):
            return self.getTypedRuleContext(RLangParser.Dot_expContext,0)


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
            self.state = 488
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.S_PRIME]:
                self.state = 480
                self.match(RLangParser.S_PRIME)
                self.state = 482
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==RLangParser.DOT:
                    self.state = 481
                    self.dot_exp()


                pass
            elif token in [RLangParser.IDENTIFIER]:
                self.state = 484
                self.match(RLangParser.IDENTIFIER)
                self.state = 486
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==RLangParser.PRIME:
                    self.state = 485
                    self.match(RLangParser.PRIME)


                pass
            else:
                raise NoViableAltException(self)

            self.state = 490
            self.match(RLangParser.PREDICT)
            self.state = 491
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
            self.state = 493
            self.match(RLangParser.PREDICT)
            self.state = 494
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
            self.state = 496
            self.match(RLangParser.WITH)
            self.state = 497
            self.match(RLangParser.P)
            self.state = 498
            self.match(RLangParser.L_PAR)
            self.state = 501
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.state = 499
                self.any_number()
                pass

            elif la_ == 2:
                self.state = 500
                self.integer_fraction()
                pass


            self.state = 503
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
            self.state = 505
            self.any_bound_class()
            self.state = 506
            self.match(RLangParser.L_PAR)
            self.state = 507
            self.object_constructor_arg_list()
            self.state = 508
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
            self.state = 511
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 26)) & ~0x3f) == 0 and ((1 << (_la - 26)) & ((1 << (RLangParser.S_PRIME - 26)) | (1 << (RLangParser.S - 26)) | (1 << (RLangParser.A - 26)) | (1 << (RLangParser.NOT - 26)) | (1 << (RLangParser.TRUE - 26)) | (1 << (RLangParser.FALSE - 26)) | (1 << (RLangParser.L_BRK - 26)) | (1 << (RLangParser.L_PAR - 26)) | (1 << (RLangParser.MINUS - 26)) | (1 << (RLangParser.IDENTIFIER - 26)) | (1 << (RLangParser.DECIMAL - 26)) | (1 << (RLangParser.INTEGER - 26)))) != 0):
                self.state = 510
                localctx._object_constructor_arg = self.object_constructor_arg()
                localctx.arg_list.append(localctx._object_constructor_arg)


            self.state = 517
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.COM:
                self.state = 513
                self.match(RLangParser.COM)
                self.state = 514
                localctx._object_constructor_arg = self.object_constructor_arg()
                localctx.arg_list.append(localctx._object_constructor_arg)
                self.state = 519
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

        def object_instantiation(self):
            return self.getTypedRuleContext(RLangParser.Object_instantiationContext,0)


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
            self.state = 524
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Object_construct_objectContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 520
                self.object_instantiation()
                pass

            elif la_ == 2:
                localctx = RLangParser.Object_construct_arith_expContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 521
                self.arithmetic_exp(0)
                pass

            elif la_ == 3:
                localctx = RLangParser.Object_construct_bool_expContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 522
                self.boolean_exp(0)
                pass

            elif la_ == 4:
                localctx = RLangParser.Object_construct_object_arrayContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 523
                self.object_array()
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
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_arithmetic_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.L_PAR]:
                localctx = RLangParser.Arith_parenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 527
                self.match(RLangParser.L_PAR)
                self.state = 528
                self.arithmetic_exp(0)
                self.state = 529
                self.match(RLangParser.R_PAR)
                pass
            elif token in [RLangParser.MINUS, RLangParser.DECIMAL, RLangParser.INTEGER]:
                localctx = RLangParser.Arith_numberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 531
                self.any_number()
                pass
            elif token in [RLangParser.L_BRK]:
                localctx = RLangParser.Arith_arrayContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 532
                self.any_array()
                pass
            elif token in [RLangParser.S_PRIME, RLangParser.S, RLangParser.A, RLangParser.IDENTIFIER]:
                localctx = RLangParser.Arith_bound_varContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 533
                self.any_bound_var()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 544
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 542
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                    if la_ == 1:
                        localctx = RLangParser.Arith_times_divideContext(self, RLangParser.Arithmetic_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_exp)
                        self.state = 536
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 537
                        _la = self._input.LA(1)
                        if not(_la==RLangParser.TIMES or _la==RLangParser.DIVIDE):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 538
                        localctx.rhs = self.arithmetic_exp(6)
                        pass

                    elif la_ == 2:
                        localctx = RLangParser.Arith_plus_minusContext(self, RLangParser.Arithmetic_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_exp)
                        self.state = 539
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 540
                        _la = self._input.LA(1)
                        if not(_la==RLangParser.PLUS or _la==RLangParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 541
                        localctx.rhs = self.arithmetic_exp(5)
                        pass

             
                self.state = 546
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
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_boolean_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 564
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Bool_parenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 548
                self.match(RLangParser.L_PAR)
                self.state = 549
                self.boolean_exp(0)
                self.state = 550
                self.match(RLangParser.R_PAR)
                pass

            elif la_ == 2:
                localctx = RLangParser.Bool_notContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 552
                self.match(RLangParser.NOT)
                self.state = 553
                self.boolean_exp(6)
                pass

            elif la_ == 3:
                localctx = RLangParser.Bool_inContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 554
                localctx.lhs = self.arithmetic_exp(0)
                self.state = 555
                self.match(RLangParser.IN)
                self.state = 556
                localctx.rhs = self.arithmetic_exp(0)
                pass

            elif la_ == 4:
                localctx = RLangParser.Bool_arith_eqContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 558
                localctx.lhs = self.arithmetic_exp(0)
                self.state = 559
                _la = self._input.LA(1)
                if not(((((_la - 54)) & ~0x3f) == 0 and ((1 << (_la - 54)) & ((1 << (RLangParser.EQ_TO - 54)) | (1 << (RLangParser.GT_EQ - 54)) | (1 << (RLangParser.LT_EQ - 54)) | (1 << (RLangParser.NOT_EQ - 54)) | (1 << (RLangParser.LT - 54)) | (1 << (RLangParser.GT - 54)))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 560
                localctx.rhs = self.arithmetic_exp(0)
                pass

            elif la_ == 5:
                localctx = RLangParser.Bool_bound_varContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 562
                self.any_bound_var()
                pass

            elif la_ == 6:
                localctx = RLangParser.Bool_tfContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 563
                _la = self._input.LA(1)
                if not(_la==RLangParser.TRUE or _la==RLangParser.FALSE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 577
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,55,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 575
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
                    if la_ == 1:
                        localctx = RLangParser.Bool_andContext(self, RLangParser.Boolean_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_exp)
                        self.state = 566
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 567
                        self.match(RLangParser.AND)
                        self.state = 568
                        localctx.rhs = self.boolean_exp(9)
                        pass

                    elif la_ == 2:
                        localctx = RLangParser.Bool_orContext(self, RLangParser.Boolean_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_exp)
                        self.state = 569
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 570
                        self.match(RLangParser.OR)
                        self.state = 571
                        localctx.rhs = self.boolean_exp(8)
                        pass

                    elif la_ == 3:
                        localctx = RLangParser.Bool_bool_eqContext(self, RLangParser.Boolean_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_exp)
                        self.state = 572
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 573
                        _la = self._input.LA(1)
                        if not(_la==RLangParser.EQ_TO or _la==RLangParser.NOT_EQ):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 574
                        localctx.rhs = self.boolean_exp(5)
                        pass

             
                self.state = 579
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
        self.enterRule(localctx, 78, self.RULE_type_def)
        try:
            self.state = 582
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.LIST, RLangParser.SET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 580
                self.compound_type()
                pass
            elif token in [RLangParser.INT, RLangParser.FLOAT, RLangParser.STR, RLangParser.BOOL, RLangParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 581
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
        self.enterRule(localctx, 80, self.RULE_compound_type)
        self._la = 0 # Token type
        try:
            self.state = 604
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.LIST]:
                localctx = RLangParser.Type_listContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 584
                self.match(RLangParser.LIST)
                self.state = 592
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==RLangParser.L_BRK:
                    self.state = 585
                    self.match(RLangParser.L_BRK)
                    self.state = 588
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [RLangParser.INT, RLangParser.FLOAT, RLangParser.STR, RLangParser.BOOL, RLangParser.IDENTIFIER]:
                        self.state = 586
                        self.simple_type()
                        pass
                    elif token in [RLangParser.LIST, RLangParser.SET]:
                        self.state = 587
                        self.compound_type()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 590
                    self.match(RLangParser.R_BRK)


                pass
            elif token in [RLangParser.SET]:
                localctx = RLangParser.Type_setContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 594
                self.match(RLangParser.SET)
                self.state = 602
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==RLangParser.L_BRK:
                    self.state = 595
                    self.match(RLangParser.L_BRK)
                    self.state = 598
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [RLangParser.INT, RLangParser.FLOAT, RLangParser.STR, RLangParser.BOOL, RLangParser.IDENTIFIER]:
                        self.state = 596
                        self.simple_type()
                        pass
                    elif token in [RLangParser.LIST, RLangParser.SET]:
                        self.state = 597
                        self.compound_type()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 600
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
        self.enterRule(localctx, 82, self.RULE_simple_type)
        try:
            self.state = 611
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 606
                self.match(RLangParser.INT)
                pass
            elif token in [RLangParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 607
                self.match(RLangParser.FLOAT)
                pass
            elif token in [RLangParser.STR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 608
                self.match(RLangParser.STR)
                pass
            elif token in [RLangParser.BOOL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 609
                self.match(RLangParser.BOOL)
                pass
            elif token in [RLangParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 5)
                self.state = 610
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
        self.enterRule(localctx, 84, self.RULE_object_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 613
            self.match(RLangParser.L_BRK)
            self.state = 614
            localctx._an_object = self.an_object()
            localctx.arr.append(localctx._an_object)
            self.state = 619
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.COM:
                self.state = 615
                self.match(RLangParser.COM)
                self.state = 616
                localctx._an_object = self.an_object()
                localctx.arr.append(localctx._an_object)
                self.state = 621
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 622
            self.match(RLangParser.R_BRK)
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
        self.enterRule(localctx, 86, self.RULE_an_object)
        try:
            self.state = 626
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 624
                self.any_bound_var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 625
                self.object_instantiation()
                pass


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
        self.enterRule(localctx, 88, self.RULE_any_bound_var)
        try:
            self.state = 647
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.S]:
                localctx = RLangParser.Bound_stateContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 628
                self.match(RLangParser.S)
                self.state = 630
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
                if la_ == 1:
                    self.state = 629
                    self.trailer()


                pass
            elif token in [RLangParser.S_PRIME]:
                localctx = RLangParser.Bound_next_stateContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 632
                self.match(RLangParser.S_PRIME)
                self.state = 634
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
                if la_ == 1:
                    self.state = 633
                    self.trailer()


                pass
            elif token in [RLangParser.IDENTIFIER]:
                localctx = RLangParser.Bound_identifierContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 636
                self.match(RLangParser.IDENTIFIER)
                self.state = 638
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
                if la_ == 1:
                    self.state = 637
                    self.match(RLangParser.PRIME)


                self.state = 643
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,68,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 640
                        self.trailer() 
                    self.state = 645
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,68,self._ctx)

                pass
            elif token in [RLangParser.A]:
                localctx = RLangParser.Bound_actionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 646
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
        self.enterRule(localctx, 90, self.RULE_any_bound_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 649
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


    class Trailer_objectContext(TrailerContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.TrailerContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def dot_exp(self):
            return self.getTypedRuleContext(RLangParser.Dot_expContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrailer_object" ):
                listener.enterTrailer_object(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrailer_object" ):
                listener.exitTrailer_object(self)



    def trailer(self):

        localctx = RLangParser.TrailerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_trailer)
        try:
            self.state = 654
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,70,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Trailer_arrayContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 651
                self.int_array_exp()
                pass

            elif la_ == 2:
                localctx = RLangParser.Trailer_sliceContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 652
                self.slice_exp()
                pass

            elif la_ == 3:
                localctx = RLangParser.Trailer_objectContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 653
                self.dot_exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dot_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._IDENTIFIER = None # Token
            self.attr = list() # of Tokens

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.DOT)
            else:
                return self.getToken(RLangParser.DOT, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.IDENTIFIER)
            else:
                return self.getToken(RLangParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return RLangParser.RULE_dot_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDot_exp" ):
                listener.enterDot_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDot_exp" ):
                listener.exitDot_exp(self)




    def dot_exp(self):

        localctx = RLangParser.Dot_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_dot_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 658 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 656
                    self.match(RLangParser.DOT)
                    self.state = 657
                    localctx._IDENTIFIER = self.match(RLangParser.IDENTIFIER)
                    localctx.attr.append(localctx._IDENTIFIER)

                else:
                    raise NoViableAltException(self)
                self.state = 660 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,71,self._ctx)

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
        self.enterRule(localctx, 96, self.RULE_any_array)
        try:
            self.state = 664
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,72,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Any_array_compoundContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 662
                self.compound_array_exp()
                pass

            elif la_ == 2:
                localctx = RLangParser.Any_array_any_numContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 663
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
        self.enterRule(localctx, 98, self.RULE_compound_array_exp)
        self._la = 0 # Token type
        try:
            self.state = 678
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,74,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Compound_array_simpleContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 666
                self.any_num_array_exp()
                pass

            elif la_ == 2:
                localctx = RLangParser.Compound_array_compoundContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 667
                self.match(RLangParser.L_BRK)
                self.state = 668
                localctx._compound_array_exp = self.compound_array_exp()
                localctx.arr.append(localctx._compound_array_exp)
                self.state = 673
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.COM:
                    self.state = 669
                    self.match(RLangParser.COM)
                    self.state = 670
                    localctx._compound_array_exp = self.compound_array_exp()
                    localctx.arr.append(localctx._compound_array_exp)
                    self.state = 675
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 676
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
        self.enterRule(localctx, 100, self.RULE_int_array_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 680
            self.match(RLangParser.L_BRK)
            self.state = 681
            localctx._any_integer = self.any_integer()
            localctx.arr.append(localctx._any_integer)
            self.state = 686
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.COM:
                self.state = 682
                self.match(RLangParser.COM)
                self.state = 683
                localctx._any_integer = self.any_integer()
                localctx.arr.append(localctx._any_integer)
                self.state = 688
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 689
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
        self.enterRule(localctx, 102, self.RULE_any_num_array_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 691
            self.match(RLangParser.L_BRK)
            self.state = 692
            localctx._any_number = self.any_number()
            localctx.arr.append(localctx._any_number)
            self.state = 697
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.COM:
                self.state = 693
                self.match(RLangParser.COM)
                self.state = 694
                localctx._any_number = self.any_number()
                localctx.arr.append(localctx._any_number)
                self.state = 699
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 700
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
        self.enterRule(localctx, 104, self.RULE_slice_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 702
            self.match(RLangParser.L_BRK)
            self.state = 704
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.MINUS or _la==RLangParser.INTEGER:
                self.state = 703
                localctx.start_ind = self.any_integer()


            self.state = 706
            self.match(RLangParser.COL)
            self.state = 708
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.MINUS or _la==RLangParser.INTEGER:
                self.state = 707
                localctx.stop_ind = self.any_integer()


            self.state = 710
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
        self.enterRule(localctx, 106, self.RULE_integer_fraction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 712
            localctx.lhs = self.any_integer()
            self.state = 713
            self.match(RLangParser.DIVIDE)
            self.state = 714
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
        self.enterRule(localctx, 108, self.RULE_any_number)
        try:
            self.state = 718
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,79,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Any_num_intContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 716
                self.any_integer()
                pass

            elif la_ == 2:
                localctx = RLangParser.Any_num_decContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 717
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
        self.enterRule(localctx, 110, self.RULE_any_integer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 721
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.MINUS:
                self.state = 720
                self.match(RLangParser.MINUS)


            self.state = 723
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
        self.enterRule(localctx, 112, self.RULE_any_decimal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 726
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.MINUS:
                self.state = 725
                self.match(RLangParser.MINUS)


            self.state = 728
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
        self._predicates[37] = self.arithmetic_exp_sempred
        self._predicates[38] = self.boolean_exp_sempred
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
         




