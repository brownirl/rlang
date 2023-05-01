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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3R")
        buf.write("\u02e5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\7\2r\n\2\f\2")
        buf.write("\16\2u\13\2\3\2\3\2\3\2\7\2z\n\2\f\2\16\2}\13\2\3\3\3")
        buf.write("\3\6\3\u0081\n\3\r\3\16\3\u0082\7\3\u0085\n\3\f\3\16\3")
        buf.write("\u0088\13\3\3\4\3\4\3\4\3\5\7\5\u008e\n\5\f\5\16\5\u0091")
        buf.write("\13\5\3\6\3\6\6\6\u0095\n\6\r\6\16\6\u0096\3\6\3\6\6\6")
        buf.write("\u009b\n\6\r\6\16\6\u009c\3\6\3\6\6\6\u00a1\n\6\r\6\16")
        buf.write("\6\u00a2\3\6\3\6\6\6\u00a7\n\6\r\6\16\6\u00a8\3\6\3\6")
        buf.write("\6\6\u00ad\n\6\r\6\16\6\u00ae\3\6\3\6\6\6\u00b3\n\6\r")
        buf.write("\6\16\6\u00b4\3\6\3\6\6\6\u00b9\n\6\r\6\16\6\u00ba\3\6")
        buf.write("\3\6\6\6\u00bf\n\6\r\6\16\6\u00c0\3\6\3\6\3\6\3\6\5\6")
        buf.write("\u00c7\n\6\3\7\3\7\3\7\3\7\3\7\5\7\u00ce\n\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\5\b\u00d5\n\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\5\17\u00fb\n\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\7\20\u0104\n\20\f\20\16\20\u0107")
        buf.write("\13\20\6\20\u0109\n\20\r\20\16\20\u010a\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\7\22")
        buf.write("\u011a\n\22\f\22\16\22\u011d\13\22\3\22\3\22\3\22\3\22")
        buf.write("\7\22\u0123\n\22\f\22\16\22\u0126\13\22\3\22\3\22\3\23")
        buf.write("\3\23\5\23\u012c\n\23\3\24\3\24\3\24\3\24\3\24\3\24\7")
        buf.write("\24\u0134\n\24\f\24\16\24\u0137\13\24\3\24\3\24\3\25\3")
        buf.write("\25\3\25\5\25\u013e\n\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\7\26\u0146\n\26\f\26\16\26\u0149\13\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\7\26\u0152\n\26\f\26\16\26\u0155")
        buf.write("\13\26\3\26\3\26\7\26\u0159\n\26\f\26\16\26\u015c\13\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\7\26\u0163\n\26\f\26\16\26\u0166")
        buf.write("\13\26\3\26\3\26\5\26\u016a\n\26\3\27\3\27\3\27\7\27\u016f")
        buf.write("\n\27\f\27\16\27\u0172\13\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\7\30\u0179\n\30\f\30\16\30\u017c\13\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\6\30\u0183\n\30\r\30\16\30\u0184\5\30\u0187")
        buf.write("\n\30\3\31\3\31\3\31\5\31\u018c\n\31\3\32\3\32\3\32\3")
        buf.write("\32\3\32\7\32\u0193\n\32\f\32\16\32\u0196\13\32\5\32\u0198")
        buf.write("\n\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\7\34\u01a5\n\34\f\34\16\34\u01a8\13\34\6\34\u01aa")
        buf.write("\n\34\r\34\16\34\u01ab\3\35\3\35\3\35\3\35\3\35\5\35\u01b3")
        buf.write("\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\7\36\u01c2\n\36\f\36\16\36\u01c5\13\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u01cd\n\36\3\37\3")
        buf.write("\37\3\37\7\37\u01d2\n\37\f\37\16\37\u01d5\13\37\3 \3 ")
        buf.write("\3 \3 \3 \3 \3 \3 \3 \5 \u01e0\n \3 \3 \6 \u01e4\n \r")
        buf.write(" \16 \u01e5\5 \u01e8\n \3!\3!\3!\3\"\3\"\5\"\u01ef\n\"")
        buf.write("\3\"\3\"\5\"\u01f3\n\"\3\"\5\"\u01f6\n\"\5\"\u01f8\n\"")
        buf.write("\3\"\3\"\3\"\3\"\5\"\u01fe\n\"\3#\3#\3#\3$\3$\3$\3$\3")
        buf.write("$\5$\u0208\n$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\5%\u0214\n")
        buf.write("%\3%\3%\3%\3%\3%\3%\7%\u021c\n%\f%\16%\u021f\13%\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\5&\u023a\n&\3&\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\7&\u0245\n&\f&\16&\u0248\13&\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3(\3(\3)\3)\5)\u0254\n)\3*\3*\3*\3*\5*\u025a\n*\3*\3")
        buf.write("*\5*\u025e\n*\3*\3*\3*\3*\5*\u0264\n*\3*\3*\5*\u0268\n")
        buf.write("*\5*\u026a\n*\3+\3+\3+\3+\3+\5+\u0271\n+\3,\3,\5,\u0275")
        buf.write("\n,\3,\3,\5,\u0279\n,\3,\3,\5,\u027d\n,\3,\7,\u0280\n")
        buf.write(",\f,\16,\u0283\13,\3,\3,\5,\u0287\n,\3-\3-\3.\3.\3.\5")
        buf.write(".\u028e\n.\3/\3/\6/\u0292\n/\r/\16/\u0293\3\60\3\60\5")
        buf.write("\60\u0298\n\60\3\61\3\61\3\61\3\61\3\61\7\61\u029f\n\61")
        buf.write("\f\61\16\61\u02a2\13\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\7\61\u02aa\n\61\f\61\16\61\u02ad\13\61\3\61\3\61\5\61")
        buf.write("\u02b1\n\61\3\62\3\62\3\62\3\62\7\62\u02b7\n\62\f\62\16")
        buf.write("\62\u02ba\13\62\3\62\3\62\3\63\3\63\3\63\3\63\7\63\u02c2")
        buf.write("\n\63\f\63\16\63\u02c5\13\63\3\63\3\63\3\64\3\64\5\64")
        buf.write("\u02cb\n\64\3\64\3\64\5\64\u02cf\n\64\3\64\3\64\3\65\3")
        buf.write("\65\3\65\3\65\3\66\3\66\5\66\u02d9\n\66\3\67\5\67\u02dc")
        buf.write("\n\67\3\67\3\67\38\58\u02e1\n8\38\38\38\2\4HJ9\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668")
        buf.write(":<>@BDFHJLNPRTVXZ\\^`bdfhjln\2\t\4\2**LL\3\2GH\3\2IJ\4")
        buf.write("\29<EF\3\2./\4\299<<\3\2\60\61\2\u0320\2s\3\2\2\2\4\u0086")
        buf.write("\3\2\2\2\6\u0089\3\2\2\2\b\u008f\3\2\2\2\n\u00c6\3\2\2")
        buf.write("\2\f\u00c8\3\2\2\2\16\u00cf\3\2\2\2\20\u00d6\3\2\2\2\22")
        buf.write("\u00db\3\2\2\2\24\u00e0\3\2\2\2\26\u00e5\3\2\2\2\30\u00ea")
        buf.write("\3\2\2\2\32\u00ef\3\2\2\2\34\u00f4\3\2\2\2\36\u0108\3")
        buf.write("\2\2\2 \u010c\3\2\2\2\"\u0110\3\2\2\2$\u012b\3\2\2\2&")
        buf.write("\u012d\3\2\2\2(\u013d\3\2\2\2*\u013f\3\2\2\2,\u016b\3")
        buf.write("\2\2\2.\u0186\3\2\2\2\60\u0188\3\2\2\2\62\u018d\3\2\2")
        buf.write("\2\64\u019b\3\2\2\2\66\u01a9\3\2\2\28\u01b2\3\2\2\2:\u01b4")
        buf.write("\3\2\2\2<\u01ce\3\2\2\2>\u01e7\3\2\2\2@\u01e9\3\2\2\2")
        buf.write("B\u01f7\3\2\2\2D\u01ff\3\2\2\2F\u0202\3\2\2\2H\u0213\3")
        buf.write("\2\2\2J\u0239\3\2\2\2L\u0249\3\2\2\2N\u024f\3\2\2\2P\u0253")
        buf.write("\3\2\2\2R\u0269\3\2\2\2T\u0270\3\2\2\2V\u0286\3\2\2\2")
        buf.write("X\u0288\3\2\2\2Z\u028d\3\2\2\2\\\u0291\3\2\2\2^\u0297")
        buf.write("\3\2\2\2`\u02b0\3\2\2\2b\u02b2\3\2\2\2d\u02bd\3\2\2\2")
        buf.write("f\u02c8\3\2\2\2h\u02d2\3\2\2\2j\u02d8\3\2\2\2l\u02db\3")
        buf.write("\2\2\2n\u02e0\3\2\2\2pr\7\5\2\2qp\3\2\2\2ru\3\2\2\2sq")
        buf.write("\3\2\2\2st\3\2\2\2tv\3\2\2\2us\3\2\2\2vw\5\4\3\2w{\5\b")
        buf.write("\5\2xz\7\5\2\2yx\3\2\2\2z}\3\2\2\2{y\3\2\2\2{|\3\2\2\2")
        buf.write("|\3\3\2\2\2}{\3\2\2\2~\u0080\5\6\4\2\177\u0081\7\5\2\2")
        buf.write("\u0080\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0080\3\2")
        buf.write("\2\2\u0082\u0083\3\2\2\2\u0083\u0085\3\2\2\2\u0084~\3")
        buf.write("\2\2\2\u0085\u0088\3\2\2\2\u0086\u0084\3\2\2\2\u0086\u0087")
        buf.write("\3\2\2\2\u0087\5\3\2\2\2\u0088\u0086\3\2\2\2\u0089\u008a")
        buf.write("\7\6\2\2\u008a\u008b\7M\2\2\u008b\7\3\2\2\2\u008c\u008e")
        buf.write("\5\n\6\2\u008d\u008c\3\2\2\2\u008e\u0091\3\2\2\2\u008f")
        buf.write("\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090\t\3\2\2\2\u0091")
        buf.write("\u008f\3\2\2\2\u0092\u0094\5\f\7\2\u0093\u0095\7\5\2\2")
        buf.write("\u0094\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0094\3")
        buf.write("\2\2\2\u0096\u0097\3\2\2\2\u0097\u00c7\3\2\2\2\u0098\u009a")
        buf.write("\5\16\b\2\u0099\u009b\7\5\2\2\u009a\u0099\3\2\2\2\u009b")
        buf.write("\u009c\3\2\2\2\u009c\u009a\3\2\2\2\u009c\u009d\3\2\2\2")
        buf.write("\u009d\u00c7\3\2\2\2\u009e\u00a0\5\20\t\2\u009f\u00a1")
        buf.write("\7\5\2\2\u00a0\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2")
        buf.write("\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00c7\3\2\2\2")
        buf.write("\u00a4\u00a6\5\22\n\2\u00a5\u00a7\7\5\2\2\u00a6\u00a5")
        buf.write("\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a8")
        buf.write("\u00a9\3\2\2\2\u00a9\u00c7\3\2\2\2\u00aa\u00ac\5\24\13")
        buf.write("\2\u00ab\u00ad\7\5\2\2\u00ac\u00ab\3\2\2\2\u00ad\u00ae")
        buf.write("\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af")
        buf.write("\u00c7\3\2\2\2\u00b0\u00b2\5\26\f\2\u00b1\u00b3\7\5\2")
        buf.write("\2\u00b2\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b2")
        buf.write("\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00c7\3\2\2\2\u00b6")
        buf.write("\u00b8\5\30\r\2\u00b7\u00b9\7\5\2\2\u00b8\u00b7\3\2\2")
        buf.write("\2\u00b9\u00ba\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb")
        buf.write("\3\2\2\2\u00bb\u00c7\3\2\2\2\u00bc\u00be\5\32\16\2\u00bd")
        buf.write("\u00bf\7\5\2\2\u00be\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2")
        buf.write("\u00c0\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c7\3")
        buf.write("\2\2\2\u00c2\u00c7\5\34\17\2\u00c3\u00c7\5\"\22\2\u00c4")
        buf.write("\u00c7\5&\24\2\u00c5\u00c7\5\64\33\2\u00c6\u0092\3\2\2")
        buf.write("\2\u00c6\u0098\3\2\2\2\u00c6\u009e\3\2\2\2\u00c6\u00a4")
        buf.write("\3\2\2\2\u00c6\u00aa\3\2\2\2\u00c6\u00b0\3\2\2\2\u00c6")
        buf.write("\u00b6\3\2\2\2\u00c6\u00bc\3\2\2\2\u00c6\u00c2\3\2\2\2")
        buf.write("\u00c6\u00c3\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c5\3")
        buf.write("\2\2\2\u00c7\13\3\2\2\2\u00c8\u00c9\7\16\2\2\u00c9\u00ca")
        buf.write("\7L\2\2\u00ca\u00cd\7\62\2\2\u00cb\u00ce\5H%\2\u00cc\u00ce")
        buf.write("\5J&\2\u00cd\u00cb\3\2\2\2\u00cd\u00cc\3\2\2\2\u00ce\r")
        buf.write("\3\2\2\2\u00cf\u00d0\7\17\2\2\u00d0\u00d1\7L\2\2\u00d1")
        buf.write("\u00d4\7\62\2\2\u00d2\u00d5\5j\66\2\u00d3\u00d5\5d\63")
        buf.write("\2\u00d4\u00d2\3\2\2\2\u00d4\u00d3\3\2\2\2\u00d5\17\3")
        buf.write("\2\2\2\u00d6\u00d7\7\n\2\2\u00d7\u00d8\7L\2\2\u00d8\u00d9")
        buf.write("\7\62\2\2\u00d9\u00da\5V,\2\u00da\21\3\2\2\2\u00db\u00dc")
        buf.write("\7\7\2\2\u00dc\u00dd\7L\2\2\u00dd\u00de\7\62\2\2\u00de")
        buf.write("\u00df\5J&\2\u00df\23\3\2\2\2\u00e0\u00e1\7\13\2\2\u00e1")
        buf.write("\u00e2\7L\2\2\u00e2\u00e3\7\62\2\2\u00e3\u00e4\5J&\2\u00e4")
        buf.write("\25\3\2\2\2\u00e5\u00e6\7\t\2\2\u00e6\u00e7\7L\2\2\u00e7")
        buf.write("\u00e8\7\62\2\2\u00e8\u00e9\5H%\2\u00e9\27\3\2\2\2\u00ea")
        buf.write("\u00eb\7\25\2\2\u00eb\u00ec\7L\2\2\u00ec\u00ed\7\62\2")
        buf.write("\2\u00ed\u00ee\5H%\2\u00ee\31\3\2\2\2\u00ef\u00f0\7\r")
        buf.write("\2\2\u00f0\u00f1\7L\2\2\u00f1\u00f2\7\62\2\2\u00f2\u00f3")
        buf.write("\5\62\32\2\u00f3\33\3\2\2\2\u00f4\u00f5\7\f\2\2\u00f5")
        buf.write("\u00fa\7L\2\2\u00f6\u00f7\7C\2\2\u00f7\u00f8\5X-\2\u00f8")
        buf.write("\u00f9\7D\2\2\u00f9\u00fb\3\2\2\2\u00fa\u00f6\3\2\2\2")
        buf.write("\u00fa\u00fb\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fd\7")
        buf.write("=\2\2\u00fd\u00fe\7\3\2\2\u00fe\u00ff\5\36\20\2\u00ff")
        buf.write("\u0100\7\4\2\2\u0100\35\3\2\2\2\u0101\u0105\5 \21\2\u0102")
        buf.write("\u0104\7\5\2\2\u0103\u0102\3\2\2\2\u0104\u0107\3\2\2\2")
        buf.write("\u0105\u0103\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0109\3")
        buf.write("\2\2\2\u0107\u0105\3\2\2\2\u0108\u0101\3\2\2\2\u0109\u010a")
        buf.write("\3\2\2\2\u010a\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b")
        buf.write("\37\3\2\2\2\u010c\u010d\7L\2\2\u010d\u010e\7=\2\2\u010e")
        buf.write("\u010f\5P)\2\u010f!\3\2\2\2\u0110\u0111\7\24\2\2\u0111")
        buf.write("\u0112\7L\2\2\u0112\u0113\7=\2\2\u0113\u0114\7\3\2\2\u0114")
        buf.write("\u0115\7%\2\2\u0115\u0116\5$\23\2\u0116\u0117\7\3\2\2")
        buf.write("\u0117\u011b\5(\25\2\u0118\u011a\7\5\2\2\u0119\u0118\3")
        buf.write("\2\2\2\u011a\u011d\3\2\2\2\u011b\u0119\3\2\2\2\u011b\u011c")
        buf.write("\3\2\2\2\u011c\u011e\3\2\2\2\u011d\u011b\3\2\2\2\u011e")
        buf.write("\u011f\7\4\2\2\u011f\u0120\7&\2\2\u0120\u0124\5$\23\2")
        buf.write("\u0121\u0123\7\5\2\2\u0122\u0121\3\2\2\2\u0123\u0126\3")
        buf.write("\2\2\2\u0124\u0122\3\2\2\2\u0124\u0125\3\2\2\2\u0125\u0127")
        buf.write("\3\2\2\2\u0126\u0124\3\2\2\2\u0127\u0128\7\4\2\2\u0128")
        buf.write("#\3\2\2\2\u0129\u012c\5J&\2\u012a\u012c\7\60\2\2\u012b")
        buf.write("\u0129\3\2\2\2\u012b\u012a\3\2\2\2\u012c%\3\2\2\2\u012d")
        buf.write("\u012e\7\22\2\2\u012e\u012f\t\2\2\2\u012f\u0130\7=\2\2")
        buf.write("\u0130\u0131\7\3\2\2\u0131\u0135\5(\25\2\u0132\u0134\7")
        buf.write("\5\2\2\u0133\u0132\3\2\2\2\u0134\u0137\3\2\2\2\u0135\u0133")
        buf.write("\3\2\2\2\u0135\u0136\3\2\2\2\u0136\u0138\3\2\2\2\u0137")
        buf.write("\u0135\3\2\2\2\u0138\u0139\7\4\2\2\u0139\'\3\2\2\2\u013a")
        buf.write("\u013e\5\60\31\2\u013b\u013e\5*\26\2\u013c\u013e\5,\27")
        buf.write("\2\u013d\u013a\3\2\2\2\u013d\u013b\3\2\2\2\u013d\u013c")
        buf.write("\3\2\2\2\u013e)\3\2\2\2\u013f\u0140\7!\2\2\u0140\u0141")
        buf.write("\5J&\2\u0141\u0142\7=\2\2\u0142\u0143\7\3\2\2\u0143\u0147")
        buf.write("\5(\25\2\u0144\u0146\7\5\2\2\u0145\u0144\3\2\2\2\u0146")
        buf.write("\u0149\3\2\2\2\u0147\u0145\3\2\2\2\u0147\u0148\3\2\2\2")
        buf.write("\u0148\u014a\3\2\2\2\u0149\u0147\3\2\2\2\u014a\u015a\7")
        buf.write("\4\2\2\u014b\u014c\7#\2\2\u014c\u014d\5J&\2\u014d\u014e")
        buf.write("\7=\2\2\u014e\u014f\7\3\2\2\u014f\u0153\5(\25\2\u0150")
        buf.write("\u0152\7\5\2\2\u0151\u0150\3\2\2\2\u0152\u0155\3\2\2\2")
        buf.write("\u0153\u0151\3\2\2\2\u0153\u0154\3\2\2\2\u0154\u0156\3")
        buf.write("\2\2\2\u0155\u0153\3\2\2\2\u0156\u0157\7\4\2\2\u0157\u0159")
        buf.write("\3\2\2\2\u0158\u014b\3\2\2\2\u0159\u015c\3\2\2\2\u015a")
        buf.write("\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u0169\3\2\2\2")
        buf.write("\u015c\u015a\3\2\2\2\u015d\u015e\7\"\2\2\u015e\u015f\7")
        buf.write("=\2\2\u015f\u0160\7\3\2\2\u0160\u0164\5(\25\2\u0161\u0163")
        buf.write("\7\5\2\2\u0162\u0161\3\2\2\2\u0163\u0166\3\2\2\2\u0164")
        buf.write("\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0167\3\2\2\2")
        buf.write("\u0166\u0164\3\2\2\2\u0167\u0168\7\4\2\2\u0168\u016a\3")
        buf.write("\2\2\2\u0169\u015d\3\2\2\2\u0169\u016a\3\2\2\2\u016a+")
        buf.write("\3\2\2\2\u016b\u0170\5.\30\2\u016c\u016d\7,\2\2\u016d")
        buf.write("\u016f\5.\30\2\u016e\u016c\3\2\2\2\u016f\u0172\3\2\2\2")
        buf.write("\u0170\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171-\3\2\2")
        buf.write("\2\u0172\u0170\3\2\2\2\u0173\u0174\5F$\2\u0174\u0175\7")
        buf.write("=\2\2\u0175\u0176\7\3\2\2\u0176\u017a\5(\25\2\u0177\u0179")
        buf.write("\7\5\2\2\u0178\u0177\3\2\2\2\u0179\u017c\3\2\2\2\u017a")
        buf.write("\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017d\3\2\2\2")
        buf.write("\u017c\u017a\3\2\2\2\u017d\u017e\7\4\2\2\u017e\u0187\3")
        buf.write("\2\2\2\u017f\u0180\5\60\31\2\u0180\u0182\5F$\2\u0181\u0183")
        buf.write("\7\5\2\2\u0182\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184")
        buf.write("\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0187\3\2\2\2")
        buf.write("\u0186\u0173\3\2\2\2\u0186\u017f\3\2\2\2\u0187/\3\2\2")
        buf.write("\2\u0188\u018b\7\23\2\2\u0189\u018c\7L\2\2\u018a\u018c")
        buf.write("\5H%\2\u018b\u0189\3\2\2\2\u018b\u018a\3\2\2\2\u018c\61")
        buf.write("\3\2\2\2\u018d\u018e\7L\2\2\u018e\u0197\7C\2\2\u018f\u0194")
        buf.write("\5H%\2\u0190\u0191\7>\2\2\u0191\u0193\5H%\2\u0192\u0190")
        buf.write("\3\2\2\2\u0193\u0196\3\2\2\2\u0194\u0192\3\2\2\2\u0194")
        buf.write("\u0195\3\2\2\2\u0195\u0198\3\2\2\2\u0196\u0194\3\2\2\2")
        buf.write("\u0197\u018f\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u0199\3")
        buf.write("\2\2\2\u0199\u019a\7D\2\2\u019a\63\3\2\2\2\u019b\u019c")
        buf.write("\7\20\2\2\u019c\u019d\t\2\2\2\u019d\u019e\7=\2\2\u019e")
        buf.write("\u019f\7\3\2\2\u019f\u01a0\5\66\34\2\u01a0\u01a1\7\4\2")
        buf.write("\2\u01a1\65\3\2\2\2\u01a2\u01a6\58\35\2\u01a3\u01a5\7")
        buf.write("\5\2\2\u01a4\u01a3\3\2\2\2\u01a5\u01a8\3\2\2\2\u01a6\u01a4")
        buf.write("\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01aa\3\2\2\2\u01a8")
        buf.write("\u01a6\3\2\2\2\u01a9\u01a2\3\2\2\2\u01aa\u01ab\3\2\2\2")
        buf.write("\u01ab\u01a9\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\67\3\2")
        buf.write("\2\2\u01ad\u01b3\5@!\2\u01ae\u01b3\5B\"\2\u01af\u01b3")
        buf.write("\5D#\2\u01b0\u01b3\5:\36\2\u01b1\u01b3\5<\37\2\u01b2\u01ad")
        buf.write("\3\2\2\2\u01b2\u01ae\3\2\2\2\u01b2\u01af\3\2\2\2\u01b2")
        buf.write("\u01b0\3\2\2\2\u01b2\u01b1\3\2\2\2\u01b39\3\2\2\2\u01b4")
        buf.write("\u01b5\7!\2\2\u01b5\u01b6\5J&\2\u01b6\u01b7\7=\2\2\u01b7")
        buf.write("\u01b8\7\3\2\2\u01b8\u01b9\5\66\34\2\u01b9\u01c3\7\4\2")
        buf.write("\2\u01ba\u01bb\7#\2\2\u01bb\u01bc\5J&\2\u01bc\u01bd\7")
        buf.write("=\2\2\u01bd\u01be\7\3\2\2\u01be\u01bf\5\66\34\2\u01bf")
        buf.write("\u01c0\7\4\2\2\u01c0\u01c2\3\2\2\2\u01c1\u01ba\3\2\2\2")
        buf.write("\u01c2\u01c5\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c3\u01c4\3")
        buf.write("\2\2\2\u01c4\u01cc\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c6\u01c7")
        buf.write("\7\"\2\2\u01c7\u01c8\7=\2\2\u01c8\u01c9\7\3\2\2\u01c9")
        buf.write("\u01ca\5\66\34\2\u01ca\u01cb\7\4\2\2\u01cb\u01cd\3\2\2")
        buf.write("\2\u01cc\u01c6\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd;\3\2")
        buf.write("\2\2\u01ce\u01d3\5> \2\u01cf\u01d0\7,\2\2\u01d0\u01d2")
        buf.write("\5> \2\u01d1\u01cf\3\2\2\2\u01d2\u01d5\3\2\2\2\u01d3\u01d1")
        buf.write("\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4=\3\2\2\2\u01d5\u01d3")
        buf.write("\3\2\2\2\u01d6\u01d7\5F$\2\u01d7\u01d8\7=\2\2\u01d8\u01d9")
        buf.write("\7\3\2\2\u01d9\u01da\5\66\34\2\u01da\u01db\7\4\2\2\u01db")
        buf.write("\u01e8\3\2\2\2\u01dc\u01e0\5@!\2\u01dd\u01e0\5B\"\2\u01de")
        buf.write("\u01e0\5D#\2\u01df\u01dc\3\2\2\2\u01df\u01dd\3\2\2\2\u01df")
        buf.write("\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1\u01e3\5F$\2\u01e2")
        buf.write("\u01e4\7\5\2\2\u01e3\u01e2\3\2\2\2\u01e4\u01e5\3\2\2\2")
        buf.write("\u01e5\u01e3\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01e8\3")
        buf.write("\2\2\2\u01e7\u01d6\3\2\2\2\u01e7\u01df\3\2\2\2\u01e8?")
        buf.write("\3\2\2\2\u01e9\u01ea\7\21\2\2\u01ea\u01eb\5H%\2\u01eb")
        buf.write("A\3\2\2\2\u01ec\u01ee\7\34\2\2\u01ed\u01ef\5\\/\2\u01ee")
        buf.write("\u01ed\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef\u01f8\3\2\2\2")
        buf.write("\u01f0\u01f2\7L\2\2\u01f1\u01f3\5\\/\2\u01f2\u01f1\3\2")
        buf.write("\2\2\u01f2\u01f3\3\2\2\2\u01f3\u01f5\3\2\2\2\u01f4\u01f6")
        buf.write("\7 \2\2\u01f5\u01f4\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6")
        buf.write("\u01f8\3\2\2\2\u01f7\u01ec\3\2\2\2\u01f7\u01f0\3\2\2\2")
        buf.write("\u01f8\u01f9\3\2\2\2\u01f9\u01fd\7\63\2\2\u01fa\u01fe")
        buf.write("\5H%\2\u01fb\u01fe\5J&\2\u01fc\u01fe\5\62\32\2\u01fd\u01fa")
        buf.write("\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fd\u01fc\3\2\2\2\u01fe")
        buf.write("C\3\2\2\2\u01ff\u0200\7\63\2\2\u0200\u0201\7L\2\2\u0201")
        buf.write("E\3\2\2\2\u0202\u0203\7\'\2\2\u0203\u0204\7\37\2\2\u0204")
        buf.write("\u0207\7C\2\2\u0205\u0208\5j\66\2\u0206\u0208\5h\65\2")
        buf.write("\u0207\u0205\3\2\2\2\u0207\u0206\3\2\2\2\u0208\u0209\3")
        buf.write("\2\2\2\u0209\u020a\7D\2\2\u020aG\3\2\2\2\u020b\u020c\b")
        buf.write("%\1\2\u020c\u020d\7C\2\2\u020d\u020e\5H%\2\u020e\u020f")
        buf.write("\7D\2\2\u020f\u0214\3\2\2\2\u0210\u0214\5j\66\2\u0211")
        buf.write("\u0214\5^\60\2\u0212\u0214\5V,\2\u0213\u020b\3\2\2\2\u0213")
        buf.write("\u0210\3\2\2\2\u0213\u0211\3\2\2\2\u0213\u0212\3\2\2\2")
        buf.write("\u0214\u021d\3\2\2\2\u0215\u0216\f\7\2\2\u0216\u0217\t")
        buf.write("\3\2\2\u0217\u021c\5H%\b\u0218\u0219\f\6\2\2\u0219\u021a")
        buf.write("\t\4\2\2\u021a\u021c\5H%\7\u021b\u0215\3\2\2\2\u021b\u0218")
        buf.write("\3\2\2\2\u021c\u021f\3\2\2\2\u021d\u021b\3\2\2\2\u021d")
        buf.write("\u021e\3\2\2\2\u021eI\3\2\2\2\u021f\u021d\3\2\2\2\u0220")
        buf.write("\u0221\b&\1\2\u0221\u0222\7C\2\2\u0222\u0223\5J&\2\u0223")
        buf.write("\u0224\7D\2\2\u0224\u023a\3\2\2\2\u0225\u0226\7-\2\2\u0226")
        buf.write("\u023a\5J&\n\u0227\u0228\5H%\2\u0228\u0229\7$\2\2\u0229")
        buf.write("\u022a\5H%\2\u022a\u023a\3\2\2\2\u022b\u022c\5H%\2\u022c")
        buf.write("\u022d\t\5\2\2\u022d\u022e\5L\'\2\u022e\u023a\3\2\2\2")
        buf.write("\u022f\u0230\5L\'\2\u0230\u0231\t\5\2\2\u0231\u0232\5")
        buf.write("H%\2\u0232\u023a\3\2\2\2\u0233\u0234\5H%\2\u0234\u0235")
        buf.write("\t\5\2\2\u0235\u0236\5H%\2\u0236\u023a\3\2\2\2\u0237\u023a")
        buf.write("\5V,\2\u0238\u023a\t\6\2\2\u0239\u0220\3\2\2\2\u0239\u0225")
        buf.write("\3\2\2\2\u0239\u0227\3\2\2\2\u0239\u022b\3\2\2\2\u0239")
        buf.write("\u022f\3\2\2\2\u0239\u0233\3\2\2\2\u0239\u0237\3\2\2\2")
        buf.write("\u0239\u0238\3\2\2\2\u023a\u0246\3\2\2\2\u023b\u023c\f")
        buf.write("\f\2\2\u023c\u023d\7+\2\2\u023d\u0245\5J&\r\u023e\u023f")
        buf.write("\f\13\2\2\u023f\u0240\7,\2\2\u0240\u0245\5J&\f\u0241\u0242")
        buf.write("\f\b\2\2\u0242\u0243\t\7\2\2\u0243\u0245\5J&\t\u0244\u023b")
        buf.write("\3\2\2\2\u0244\u023e\3\2\2\2\u0244\u0241\3\2\2\2\u0245")
        buf.write("\u0248\3\2\2\2\u0246\u0244\3\2\2\2\u0246\u0247\3\2\2\2")
        buf.write("\u0247K\3\2\2\2\u0248\u0246\3\2\2\2\u0249\u024a\5N(\2")
        buf.write("\u024a\u024b\7C\2\2\u024b\u024c\5X-\2\u024c\u024d\7D\2")
        buf.write("\2\u024d\u024e\5\\/\2\u024eM\3\2\2\2\u024f\u0250\t\b\2")
        buf.write("\2\u0250O\3\2\2\2\u0251\u0254\5R*\2\u0252\u0254\5T+\2")
        buf.write("\u0253\u0251\3\2\2\2\u0253\u0252\3\2\2\2\u0254Q\3\2\2")
        buf.write("\2\u0255\u025d\7\31\2\2\u0256\u0259\7?\2\2\u0257\u025a")
        buf.write("\5T+\2\u0258\u025a\5R*\2\u0259\u0257\3\2\2\2\u0259\u0258")
        buf.write("\3\2\2\2\u025a\u025b\3\2\2\2\u025b\u025c\7@\2\2\u025c")
        buf.write("\u025e\3\2\2\2\u025d\u0256\3\2\2\2\u025d\u025e\3\2\2\2")
        buf.write("\u025e\u026a\3\2\2\2\u025f\u0267\7\32\2\2\u0260\u0263")
        buf.write("\7?\2\2\u0261\u0264\5T+\2\u0262\u0264\5R*\2\u0263\u0261")
        buf.write("\3\2\2\2\u0263\u0262\3\2\2\2\u0264\u0265\3\2\2\2\u0265")
        buf.write("\u0266\7@\2\2\u0266\u0268\3\2\2\2\u0267\u0260\3\2\2\2")
        buf.write("\u0267\u0268\3\2\2\2\u0268\u026a\3\2\2\2\u0269\u0255\3")
        buf.write("\2\2\2\u0269\u025f\3\2\2\2\u026aS\3\2\2\2\u026b\u0271")
        buf.write("\7\26\2\2\u026c\u0271\7\27\2\2\u026d\u0271\7\30\2\2\u026e")
        buf.write("\u0271\7\33\2\2\u026f\u0271\5X-\2\u0270\u026b\3\2\2\2")
        buf.write("\u0270\u026c\3\2\2\2\u0270\u026d\3\2\2\2\u0270\u026e\3")
        buf.write("\2\2\2\u0270\u026f\3\2\2\2\u0271U\3\2\2\2\u0272\u0274")
        buf.write("\7\35\2\2\u0273\u0275\5Z.\2\u0274\u0273\3\2\2\2\u0274")
        buf.write("\u0275\3\2\2\2\u0275\u0287\3\2\2\2\u0276\u0278\7\34\2")
        buf.write("\2\u0277\u0279\5Z.\2\u0278\u0277\3\2\2\2\u0278\u0279\3")
        buf.write("\2\2\2\u0279\u0287\3\2\2\2\u027a\u027c\7L\2\2\u027b\u027d")
        buf.write("\7 \2\2\u027c\u027b\3\2\2\2\u027c\u027d\3\2\2\2\u027d")
        buf.write("\u0281\3\2\2\2\u027e\u0280\5Z.\2\u027f\u027e\3\2\2\2\u0280")
        buf.write("\u0283\3\2\2\2\u0281\u027f\3\2\2\2\u0281\u0282\3\2\2\2")
        buf.write("\u0282\u0287\3\2\2\2\u0283\u0281\3\2\2\2\u0284\u0287\7")
        buf.write("\36\2\2\u0285\u0287\5\62\32\2\u0286\u0272\3\2\2\2\u0286")
        buf.write("\u0276\3\2\2\2\u0286\u027a\3\2\2\2\u0286\u0284\3\2\2\2")
        buf.write("\u0286\u0285\3\2\2\2\u0287W\3\2\2\2\u0288\u0289\7L\2\2")
        buf.write("\u0289Y\3\2\2\2\u028a\u028e\5b\62\2\u028b\u028e\5f\64")
        buf.write("\2\u028c\u028e\5\\/\2\u028d\u028a\3\2\2\2\u028d\u028b")
        buf.write("\3\2\2\2\u028d\u028c\3\2\2\2\u028e[\3\2\2\2\u028f\u0290")
        buf.write("\7P\2\2\u0290\u0292\7L\2\2\u0291\u028f\3\2\2\2\u0292\u0293")
        buf.write("\3\2\2\2\u0293\u0291\3\2\2\2\u0293\u0294\3\2\2\2\u0294")
        buf.write("]\3\2\2\2\u0295\u0298\5`\61\2\u0296\u0298\5d\63\2\u0297")
        buf.write("\u0295\3\2\2\2\u0297\u0296\3\2\2\2\u0298_\3\2\2\2\u0299")
        buf.write("\u02b1\5d\63\2\u029a\u029b\7?\2\2\u029b\u02a0\5H%\2\u029c")
        buf.write("\u029d\7>\2\2\u029d\u029f\5H%\2\u029e\u029c\3\2\2\2\u029f")
        buf.write("\u02a2\3\2\2\2\u02a0\u029e\3\2\2\2\u02a0\u02a1\3\2\2\2")
        buf.write("\u02a1\u02a3\3\2\2\2\u02a2\u02a0\3\2\2\2\u02a3\u02a4\7")
        buf.write("@\2\2\u02a4\u02b1\3\2\2\2\u02a5\u02a6\7?\2\2\u02a6\u02ab")
        buf.write("\5`\61\2\u02a7\u02a8\7>\2\2\u02a8\u02aa\5`\61\2\u02a9")
        buf.write("\u02a7\3\2\2\2\u02aa\u02ad\3\2\2\2\u02ab\u02a9\3\2\2\2")
        buf.write("\u02ab\u02ac\3\2\2\2\u02ac\u02ae\3\2\2\2\u02ad\u02ab\3")
        buf.write("\2\2\2\u02ae\u02af\7@\2\2\u02af\u02b1\3\2\2\2\u02b0\u0299")
        buf.write("\3\2\2\2\u02b0\u029a\3\2\2\2\u02b0\u02a5\3\2\2\2\u02b1")
        buf.write("a\3\2\2\2\u02b2\u02b3\7?\2\2\u02b3\u02b8\5l\67\2\u02b4")
        buf.write("\u02b5\7>\2\2\u02b5\u02b7\5l\67\2\u02b6\u02b4\3\2\2\2")
        buf.write("\u02b7\u02ba\3\2\2\2\u02b8\u02b6\3\2\2\2\u02b8\u02b9\3")
        buf.write("\2\2\2\u02b9\u02bb\3\2\2\2\u02ba\u02b8\3\2\2\2\u02bb\u02bc")
        buf.write("\7@\2\2\u02bcc\3\2\2\2\u02bd\u02be\7?\2\2\u02be\u02c3")
        buf.write("\5j\66\2\u02bf\u02c0\7>\2\2\u02c0\u02c2\5j\66\2\u02c1")
        buf.write("\u02bf\3\2\2\2\u02c2\u02c5\3\2\2\2\u02c3\u02c1\3\2\2\2")
        buf.write("\u02c3\u02c4\3\2\2\2\u02c4\u02c6\3\2\2\2\u02c5\u02c3\3")
        buf.write("\2\2\2\u02c6\u02c7\7@\2\2\u02c7e\3\2\2\2\u02c8\u02ca\7")
        buf.write("?\2\2\u02c9\u02cb\5l\67\2\u02ca\u02c9\3\2\2\2\u02ca\u02cb")
        buf.write("\3\2\2\2\u02cb\u02cc\3\2\2\2\u02cc\u02ce\7=\2\2\u02cd")
        buf.write("\u02cf\5l\67\2\u02ce\u02cd\3\2\2\2\u02ce\u02cf\3\2\2\2")
        buf.write("\u02cf\u02d0\3\2\2\2\u02d0\u02d1\7@\2\2\u02d1g\3\2\2\2")
        buf.write("\u02d2\u02d3\5l\67\2\u02d3\u02d4\7H\2\2\u02d4\u02d5\5")
        buf.write("l\67\2\u02d5i\3\2\2\2\u02d6\u02d9\5l\67\2\u02d7\u02d9")
        buf.write("\5n8\2\u02d8\u02d6\3\2\2\2\u02d8\u02d7\3\2\2\2\u02d9k")
        buf.write("\3\2\2\2\u02da\u02dc\7J\2\2\u02db\u02da\3\2\2\2\u02db")
        buf.write("\u02dc\3\2\2\2\u02dc\u02dd\3\2\2\2\u02dd\u02de\7O\2\2")
        buf.write("\u02dem\3\2\2\2\u02df\u02e1\7J\2\2\u02e0\u02df\3\2\2\2")
        buf.write("\u02e0\u02e1\3\2\2\2\u02e1\u02e2\3\2\2\2\u02e2\u02e3\7")
        buf.write("N\2\2\u02e3o\3\2\2\2Ts{\u0082\u0086\u008f\u0096\u009c")
        buf.write("\u00a2\u00a8\u00ae\u00b4\u00ba\u00c0\u00c6\u00cd\u00d4")
        buf.write("\u00fa\u0105\u010a\u011b\u0124\u012b\u0135\u013d\u0147")
        buf.write("\u0153\u015a\u0164\u0169\u0170\u017a\u0184\u0186\u018b")
        buf.write("\u0194\u0197\u01a6\u01ab\u01b2\u01c3\u01cc\u01d3\u01df")
        buf.write("\u01e5\u01e7\u01ee\u01f2\u01f5\u01f7\u01fd\u0207\u0213")
        buf.write("\u021b\u021d\u0239\u0244\u0246\u0253\u0259\u025d\u0263")
        buf.write("\u0267\u0269\u0270\u0274\u0278\u027c\u0281\u0286\u028d")
        buf.write("\u0293\u0297\u02a0\u02ab\u02b0\u02b8\u02c3\u02ca\u02ce")
        buf.write("\u02d8\u02db\u02e0")
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
                     "'Any'", "'All'", "':='", "'->'", "'='", "'*='", "'/='", 
                     "'+='", "'-='", "'=='", "'>='", "'<='", "'!='", "':'", 
                     "','", "'['", "']'", "'{'", "'}'", "'('", "')'", "'<'", 
                     "'>'", "'*'", "'/'", "'+'", "'-'", "'\"'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'.'" ]

    symbolicNames = [ "<INVALID>", "INDENT", "DEDENT", "NL", "IMPORT", "PROPOSITION", 
                      "PREDICATE", "FEATURE", "FACTOR", "GOAL", "CLASS", 
                      "OBJECT", "CONSTANT", "ACTION", "EFFECT", "REWARD", 
                      "POLICY", "EXECUTE", "OPTION", "MARKOVFEATURE", "INT", 
                      "FLOAT", "STR", "LIST", "SET", "BOOL", "S_PRIME", 
                      "S", "A", "P", "PRIME", "IF", "ELSE", "ELIF", "IN", 
                      "INIT", "UNTIL", "WITH", "THEN", "NEVER", "MAIN", 
                      "AND", "OR", "NOT", "TRUE", "FALSE", "ANY_CONDITION", 
                      "ALL_CONDITION", "BIND", "PREDICT", "ASSIGN", "TIMES_EQ", 
                      "DIV_EQ", "PLUS_EQ", "MINUS_EQ", "EQ_TO", "GT_EQ", 
                      "LT_EQ", "NOT_EQ", "COL", "COM", "L_BRK", "R_BRK", 
                      "L_CBRK", "R_CBRK", "L_PAR", "R_PAR", "LT", "GT", 
                      "TIMES", "DIVIDE", "PLUS", "MINUS", "QUOTE", "IDENTIFIER", 
                      "FNAME", "DECIMAL", "INTEGER", "DOT", "SKIP_", "ANY" ]

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
    RULE_lifted_execution = 24
    RULE_effect = 25
    RULE_effect_statement_collection = 26
    RULE_effect_statement = 27
    RULE_conditional_effect = 28
    RULE_probabilistic_effect = 29
    RULE_probabilistic_effect_statement = 30
    RULE_reward = 31
    RULE_prediction = 32
    RULE_effect_reference = 33
    RULE_probabilistic_condition = 34
    RULE_arithmetic_exp = 35
    RULE_boolean_exp = 36
    RULE_quantification_exp = 37
    RULE_quantifier = 38
    RULE_type_def = 39
    RULE_compound_type = 40
    RULE_simple_type = 41
    RULE_any_bound_var = 42
    RULE_any_bound_class = 43
    RULE_trailer = 44
    RULE_dot_exp = 45
    RULE_any_array = 46
    RULE_compound_array_exp = 47
    RULE_int_array_exp = 48
    RULE_any_num_array_exp = 49
    RULE_slice_exp = 50
    RULE_integer_fraction = 51
    RULE_any_number = 52
    RULE_any_integer = 53
    RULE_any_decimal = 54

    ruleNames =  [ "program", "imports", "import_stat", "declarations", 
                   "dec", "constant", "action", "factor", "proposition", 
                   "goal", "feature", "markov_feature", "object_def", "class_def", 
                   "attribute_definition_collection", "attribute_definition", 
                   "option", "option_condition", "policy", "policy_statement", 
                   "conditional_subpolicy", "probabilistic_subpolicy", "probabilistic_policy_statement", 
                   "execute", "lifted_execution", "effect", "effect_statement_collection", 
                   "effect_statement", "conditional_effect", "probabilistic_effect", 
                   "probabilistic_effect_statement", "reward", "prediction", 
                   "effect_reference", "probabilistic_condition", "arithmetic_exp", 
                   "boolean_exp", "quantification_exp", "quantifier", "type_def", 
                   "compound_type", "simple_type", "any_bound_var", "any_bound_class", 
                   "trailer", "dot_exp", "any_array", "compound_array_exp", 
                   "int_array_exp", "any_num_array_exp", "slice_exp", "integer_fraction", 
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
    ALL_CONDITION=47
    BIND=48
    PREDICT=49
    ASSIGN=50
    TIMES_EQ=51
    DIV_EQ=52
    PLUS_EQ=53
    MINUS_EQ=54
    EQ_TO=55
    GT_EQ=56
    LT_EQ=57
    NOT_EQ=58
    COL=59
    COM=60
    L_BRK=61
    R_BRK=62
    L_CBRK=63
    R_CBRK=64
    L_PAR=65
    R_PAR=66
    LT=67
    GT=68
    TIMES=69
    DIVIDE=70
    PLUS=71
    MINUS=72
    QUOTE=73
    IDENTIFIER=74
    FNAME=75
    DECIMAL=76
    INTEGER=77
    DOT=78
    SKIP_=79
    ANY=80

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
            self.state = 113
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 110
                    self.match(RLangParser.NL) 
                self.state = 115
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 116
            self.imports()
            self.state = 117
            self.declarations()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.NL:
                self.state = 118
                self.match(RLangParser.NL)
                self.state = 123
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
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.IMPORT:
                self.state = 124
                self.import_stat()
                self.state = 126 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 125
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 128 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                self.state = 134
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
            self.state = 135
            self.match(RLangParser.IMPORT)
            self.state = 136
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
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RLangParser.PROPOSITION) | (1 << RLangParser.FEATURE) | (1 << RLangParser.FACTOR) | (1 << RLangParser.GOAL) | (1 << RLangParser.CLASS) | (1 << RLangParser.OBJECT) | (1 << RLangParser.CONSTANT) | (1 << RLangParser.ACTION) | (1 << RLangParser.EFFECT) | (1 << RLangParser.POLICY) | (1 << RLangParser.OPTION) | (1 << RLangParser.MARKOVFEATURE))) != 0):
                self.state = 138
                self.dec()
                self.state = 143
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
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.CONSTANT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.constant()
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
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                pass
            elif token in [RLangParser.ACTION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.action()
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
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                pass
            elif token in [RLangParser.FACTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 156
                self.factor()
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
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                pass
            elif token in [RLangParser.PROPOSITION]:
                self.enterOuterAlt(localctx, 4)
                self.state = 162
                self.proposition()
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
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                pass
            elif token in [RLangParser.GOAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 168
                self.goal()
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
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                pass
            elif token in [RLangParser.FEATURE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 174
                self.feature()
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
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                pass
            elif token in [RLangParser.MARKOVFEATURE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 180
                self.markov_feature()
                self.state = 182 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 181
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 184 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                pass
            elif token in [RLangParser.OBJECT]:
                self.enterOuterAlt(localctx, 8)
                self.state = 186
                self.object_def()
                self.state = 188 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 187
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 190 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                pass
            elif token in [RLangParser.CLASS]:
                self.enterOuterAlt(localctx, 9)
                self.state = 192
                self.class_def()
                pass
            elif token in [RLangParser.OPTION]:
                self.enterOuterAlt(localctx, 10)
                self.state = 193
                self.option()
                pass
            elif token in [RLangParser.POLICY]:
                self.enterOuterAlt(localctx, 11)
                self.state = 194
                self.policy()
                pass
            elif token in [RLangParser.EFFECT]:
                self.enterOuterAlt(localctx, 12)
                self.state = 195
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
            self.state = 198
            self.match(RLangParser.CONSTANT)
            self.state = 199
            self.match(RLangParser.IDENTIFIER)
            self.state = 200
            self.match(RLangParser.BIND)
            self.state = 203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 201
                self.arithmetic_exp(0)
                pass

            elif la_ == 2:
                self.state = 202
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
            self.state = 205
            self.match(RLangParser.ACTION)
            self.state = 206
            self.match(RLangParser.IDENTIFIER)
            self.state = 207
            self.match(RLangParser.BIND)
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.MINUS, RLangParser.DECIMAL, RLangParser.INTEGER]:
                self.state = 208
                self.any_number()
                pass
            elif token in [RLangParser.L_BRK]:
                self.state = 209
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
            self.state = 212
            self.match(RLangParser.FACTOR)
            self.state = 213
            self.match(RLangParser.IDENTIFIER)
            self.state = 214
            self.match(RLangParser.BIND)
            self.state = 215
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
            self.state = 217
            self.match(RLangParser.PROPOSITION)
            self.state = 218
            self.match(RLangParser.IDENTIFIER)
            self.state = 219
            self.match(RLangParser.BIND)
            self.state = 220
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
            self.state = 222
            self.match(RLangParser.GOAL)
            self.state = 223
            self.match(RLangParser.IDENTIFIER)
            self.state = 224
            self.match(RLangParser.BIND)
            self.state = 225
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
            self.state = 227
            self.match(RLangParser.FEATURE)
            self.state = 228
            self.match(RLangParser.IDENTIFIER)
            self.state = 229
            self.match(RLangParser.BIND)
            self.state = 230
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
            self.state = 232
            self.match(RLangParser.MARKOVFEATURE)
            self.state = 233
            self.match(RLangParser.IDENTIFIER)
            self.state = 234
            self.match(RLangParser.BIND)
            self.state = 235
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

        def lifted_execution(self):
            return self.getTypedRuleContext(RLangParser.Lifted_executionContext,0)


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
            self.state = 237
            self.match(RLangParser.OBJECT)
            self.state = 238
            self.match(RLangParser.IDENTIFIER)
            self.state = 239
            self.match(RLangParser.BIND)
            self.state = 240
            self.lifted_execution()
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
            self.state = 242
            self.match(RLangParser.CLASS)
            self.state = 243
            self.match(RLangParser.IDENTIFIER)
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.L_PAR:
                self.state = 244
                self.match(RLangParser.L_PAR)
                self.state = 245
                self.any_bound_class()
                self.state = 246
                self.match(RLangParser.R_PAR)


            self.state = 250
            self.match(RLangParser.COL)
            self.state = 251
            self.match(RLangParser.INDENT)
            self.state = 252
            self.attribute_definition_collection()
            self.state = 253
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
            self.state = 262 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 255
                localctx._attribute_definition = self.attribute_definition()
                localctx.definitions.append(localctx._attribute_definition)
                self.state = 259
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.NL:
                    self.state = 256
                    self.match(RLangParser.NL)
                    self.state = 261
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 264 
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
            self.state = 266
            self.match(RLangParser.IDENTIFIER)
            self.state = 267
            self.match(RLangParser.COL)
            self.state = 268
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
            self.state = 270
            self.match(RLangParser.OPTION)
            self.state = 271
            self.match(RLangParser.IDENTIFIER)
            self.state = 272
            self.match(RLangParser.COL)
            self.state = 273
            self.match(RLangParser.INDENT)
            self.state = 274
            self.match(RLangParser.INIT)
            self.state = 275
            localctx.init = self.option_condition()
            self.state = 276
            self.match(RLangParser.INDENT)
            self.state = 277
            self.policy_statement()
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.NL:
                self.state = 278
                self.match(RLangParser.NL)
                self.state = 283
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 284
            self.match(RLangParser.DEDENT)
            self.state = 285
            self.match(RLangParser.UNTIL)
            self.state = 286
            localctx.until = self.option_condition()
            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.NL:
                self.state = 287
                self.match(RLangParser.NL)
                self.state = 292
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 293
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
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.boolean_exp(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
                self.match(RLangParser.ANY_CONDITION)
                pass


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
            self.state = 299
            self.match(RLangParser.POLICY)
            self.state = 300
            _la = self._input.LA(1)
            if not(_la==RLangParser.MAIN or _la==RLangParser.IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 301
            self.match(RLangParser.COL)
            self.state = 302
            self.match(RLangParser.INDENT)
            self.state = 303
            self.policy_statement()
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.NL:
                self.state = 304
                self.match(RLangParser.NL)
                self.state = 309
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 310
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
            self.state = 315
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Policy_statement_executeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.execute()
                pass

            elif la_ == 2:
                localctx = RLangParser.Policy_statement_conditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.conditional_subpolicy()
                pass

            elif la_ == 3:
                localctx = RLangParser.Policy_statement_probabilisticContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 314
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
            self.state = 317
            self.match(RLangParser.IF)
            self.state = 318
            localctx.if_condition = self.boolean_exp(0)
            self.state = 319
            self.match(RLangParser.COL)
            self.state = 320
            self.match(RLangParser.INDENT)
            self.state = 321
            localctx.if_subpolicy = self.policy_statement()
            self.state = 325
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.NL:
                self.state = 322
                self.match(RLangParser.NL)
                self.state = 327
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 328
            self.match(RLangParser.DEDENT)
            self.state = 344
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.ELIF:
                self.state = 329
                self.match(RLangParser.ELIF)
                self.state = 330
                localctx._boolean_exp = self.boolean_exp(0)
                localctx.elif_conditions.append(localctx._boolean_exp)
                self.state = 331
                self.match(RLangParser.COL)
                self.state = 332
                self.match(RLangParser.INDENT)
                self.state = 333
                localctx._policy_statement = self.policy_statement()
                localctx.elif_subpolicies.append(localctx._policy_statement)
                self.state = 337
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.NL:
                    self.state = 334
                    self.match(RLangParser.NL)
                    self.state = 339
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 340
                self.match(RLangParser.DEDENT)
                self.state = 346
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 359
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.ELSE:
                self.state = 347
                self.match(RLangParser.ELSE)
                self.state = 348
                self.match(RLangParser.COL)
                self.state = 349
                self.match(RLangParser.INDENT)
                self.state = 350
                localctx.else_subpolicy = self.policy_statement()
                self.state = 354
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.NL:
                    self.state = 351
                    self.match(RLangParser.NL)
                    self.state = 356
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 357
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
            self.state = 361
            localctx._probabilistic_policy_statement = self.probabilistic_policy_statement()
            localctx.subpolicies.append(localctx._probabilistic_policy_statement)
            self.state = 366
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.OR:
                self.state = 362
                self.match(RLangParser.OR)
                self.state = 363
                localctx._probabilistic_policy_statement = self.probabilistic_policy_statement()
                localctx.subpolicies.append(localctx._probabilistic_policy_statement)
                self.state = 368
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
            self.state = 388
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.WITH]:
                localctx = RLangParser.Probabilistic_policy_statement_no_sugarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.probabilistic_condition()
                self.state = 370
                self.match(RLangParser.COL)
                self.state = 371
                self.match(RLangParser.INDENT)
                self.state = 372
                self.policy_statement()
                self.state = 376
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.NL:
                    self.state = 373
                    self.match(RLangParser.NL)
                    self.state = 378
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 379
                self.match(RLangParser.DEDENT)
                pass
            elif token in [RLangParser.EXECUTE]:
                localctx = RLangParser.Probabilistic_policy_statement_sugarContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 381
                self.execute()
                self.state = 382
                self.probabilistic_condition()
                self.state = 384 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 383
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 386 
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
            self.state = 390
            self.match(RLangParser.EXECUTE)
            self.state = 393
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 391
                self.match(RLangParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 392
                self.arithmetic_exp(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lifted_executionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._arithmetic_exp = None # Arithmetic_expContext
            self.arr = list() # of Arithmetic_expContexts

        def IDENTIFIER(self):
            return self.getToken(RLangParser.IDENTIFIER, 0)

        def L_PAR(self):
            return self.getToken(RLangParser.L_PAR, 0)

        def R_PAR(self):
            return self.getToken(RLangParser.R_PAR, 0)

        def arithmetic_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Arithmetic_expContext)
            else:
                return self.getTypedRuleContext(RLangParser.Arithmetic_expContext,i)


        def COM(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.COM)
            else:
                return self.getToken(RLangParser.COM, i)

        def getRuleIndex(self):
            return RLangParser.RULE_lifted_execution

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLifted_execution" ):
                listener.enterLifted_execution(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLifted_execution" ):
                listener.exitLifted_execution(self)




    def lifted_execution(self):

        localctx = RLangParser.Lifted_executionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_lifted_execution)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.match(RLangParser.IDENTIFIER)
            self.state = 396
            self.match(RLangParser.L_PAR)
            self.state = 405
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 26)) & ~0x3f) == 0 and ((1 << (_la - 26)) & ((1 << (RLangParser.S_PRIME - 26)) | (1 << (RLangParser.S - 26)) | (1 << (RLangParser.A - 26)) | (1 << (RLangParser.L_BRK - 26)) | (1 << (RLangParser.L_PAR - 26)) | (1 << (RLangParser.MINUS - 26)) | (1 << (RLangParser.IDENTIFIER - 26)) | (1 << (RLangParser.DECIMAL - 26)) | (1 << (RLangParser.INTEGER - 26)))) != 0):
                self.state = 397
                localctx._arithmetic_exp = self.arithmetic_exp(0)
                localctx.arr.append(localctx._arithmetic_exp)
                self.state = 402
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.COM:
                    self.state = 398
                    self.match(RLangParser.COM)
                    self.state = 399
                    localctx._arithmetic_exp = self.arithmetic_exp(0)
                    localctx.arr.append(localctx._arithmetic_exp)
                    self.state = 404
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 407
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
        self.enterRule(localctx, 50, self.RULE_effect)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.match(RLangParser.EFFECT)
            self.state = 410
            _la = self._input.LA(1)
            if not(_la==RLangParser.MAIN or _la==RLangParser.IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 411
            self.match(RLangParser.COL)
            self.state = 412
            self.match(RLangParser.INDENT)
            self.state = 413
            self.effect_statement_collection()
            self.state = 414
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
        self.enterRule(localctx, 52, self.RULE_effect_statement_collection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 416
                localctx._effect_statement = self.effect_statement()
                localctx.statements.append(localctx._effect_statement)
                self.state = 420
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.NL:
                    self.state = 417
                    self.match(RLangParser.NL)
                    self.state = 422
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 425 
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
        self.enterRule(localctx, 54, self.RULE_effect_statement)
        try:
            self.state = 432
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Effect_statement_rewardContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self.reward()
                pass

            elif la_ == 2:
                localctx = RLangParser.Effect_statement_predictionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                self.prediction()
                pass

            elif la_ == 3:
                localctx = RLangParser.Effect_statement_referenceContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 429
                self.effect_reference()
                pass

            elif la_ == 4:
                localctx = RLangParser.Effect_statement_conditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 430
                self.conditional_effect()
                pass

            elif la_ == 5:
                localctx = RLangParser.Effect_statement_probabilisticContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 431
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
        self.enterRule(localctx, 56, self.RULE_conditional_effect)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.match(RLangParser.IF)
            self.state = 435
            localctx.if_condition = self.boolean_exp(0)
            self.state = 436
            self.match(RLangParser.COL)
            self.state = 437
            self.match(RLangParser.INDENT)
            self.state = 438
            localctx.if_effect = self.effect_statement_collection()
            self.state = 439
            self.match(RLangParser.DEDENT)
            self.state = 449
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.ELIF:
                self.state = 440
                self.match(RLangParser.ELIF)
                self.state = 441
                localctx._boolean_exp = self.boolean_exp(0)
                localctx.elif_conditions.append(localctx._boolean_exp)
                self.state = 442
                self.match(RLangParser.COL)
                self.state = 443
                self.match(RLangParser.INDENT)
                self.state = 444
                localctx._effect_statement_collection = self.effect_statement_collection()
                localctx.elif_effects.append(localctx._effect_statement_collection)
                self.state = 445
                self.match(RLangParser.DEDENT)
                self.state = 451
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 458
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.ELSE:
                self.state = 452
                self.match(RLangParser.ELSE)
                self.state = 453
                self.match(RLangParser.COL)
                self.state = 454
                self.match(RLangParser.INDENT)
                self.state = 455
                localctx.else_effect = self.effect_statement_collection()
                self.state = 456
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
        self.enterRule(localctx, 58, self.RULE_probabilistic_effect)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            localctx._probabilistic_effect_statement = self.probabilistic_effect_statement()
            localctx.effects.append(localctx._probabilistic_effect_statement)
            self.state = 465
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.OR:
                self.state = 461
                self.match(RLangParser.OR)
                self.state = 462
                localctx._probabilistic_effect_statement = self.probabilistic_effect_statement()
                localctx.effects.append(localctx._probabilistic_effect_statement)
                self.state = 467
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
        self.enterRule(localctx, 60, self.RULE_probabilistic_effect_statement)
        try:
            self.state = 485
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.WITH]:
                localctx = RLangParser.Probabilistic_effect_statement_no_sugarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 468
                self.probabilistic_condition()
                self.state = 469
                self.match(RLangParser.COL)
                self.state = 470
                self.match(RLangParser.INDENT)
                self.state = 471
                self.effect_statement_collection()
                self.state = 472
                self.match(RLangParser.DEDENT)
                pass
            elif token in [RLangParser.REWARD, RLangParser.S_PRIME, RLangParser.PREDICT, RLangParser.IDENTIFIER]:
                localctx = RLangParser.Probabilistic_effect_statement_sugarContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 477
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RLangParser.REWARD]:
                    self.state = 474
                    self.reward()
                    pass
                elif token in [RLangParser.S_PRIME, RLangParser.IDENTIFIER]:
                    self.state = 475
                    self.prediction()
                    pass
                elif token in [RLangParser.PREDICT]:
                    self.state = 476
                    self.effect_reference()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 479
                self.probabilistic_condition()
                self.state = 481 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 480
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 483 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

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
        self.enterRule(localctx, 62, self.RULE_reward)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self.match(RLangParser.REWARD)
            self.state = 488
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

        def S_PRIME(self):
            return self.getToken(RLangParser.S_PRIME, 0)

        def IDENTIFIER(self):
            return self.getToken(RLangParser.IDENTIFIER, 0)

        def arithmetic_exp(self):
            return self.getTypedRuleContext(RLangParser.Arithmetic_expContext,0)


        def boolean_exp(self):
            return self.getTypedRuleContext(RLangParser.Boolean_expContext,0)


        def lifted_execution(self):
            return self.getTypedRuleContext(RLangParser.Lifted_executionContext,0)


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
        self.enterRule(localctx, 64, self.RULE_prediction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.S_PRIME]:
                self.state = 490
                self.match(RLangParser.S_PRIME)
                self.state = 492
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==RLangParser.DOT:
                    self.state = 491
                    self.dot_exp()


                pass
            elif token in [RLangParser.IDENTIFIER]:
                self.state = 494
                self.match(RLangParser.IDENTIFIER)
                self.state = 496
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==RLangParser.DOT:
                    self.state = 495
                    self.dot_exp()


                self.state = 499
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==RLangParser.PRIME:
                    self.state = 498
                    self.match(RLangParser.PRIME)


                pass
            else:
                raise NoViableAltException(self)

            self.state = 503
            self.match(RLangParser.PREDICT)
            self.state = 507
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.state = 504
                self.arithmetic_exp(0)
                pass

            elif la_ == 2:
                self.state = 505
                self.boolean_exp(0)
                pass

            elif la_ == 3:
                self.state = 506
                self.lifted_execution()
                pass


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
        self.enterRule(localctx, 66, self.RULE_effect_reference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 509
            self.match(RLangParser.PREDICT)
            self.state = 510
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
        self.enterRule(localctx, 68, self.RULE_probabilistic_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512
            self.match(RLangParser.WITH)
            self.state = 513
            self.match(RLangParser.P)
            self.state = 514
            self.match(RLangParser.L_PAR)
            self.state = 517
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.state = 515
                self.any_number()
                pass

            elif la_ == 2:
                self.state = 516
                self.integer_fraction()
                pass


            self.state = 519
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
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_arithmetic_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.L_PAR]:
                localctx = RLangParser.Arith_parenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 522
                self.match(RLangParser.L_PAR)
                self.state = 523
                self.arithmetic_exp(0)
                self.state = 524
                self.match(RLangParser.R_PAR)
                pass
            elif token in [RLangParser.MINUS, RLangParser.DECIMAL, RLangParser.INTEGER]:
                localctx = RLangParser.Arith_numberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 526
                self.any_number()
                pass
            elif token in [RLangParser.L_BRK]:
                localctx = RLangParser.Arith_arrayContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 527
                self.any_array()
                pass
            elif token in [RLangParser.S_PRIME, RLangParser.S, RLangParser.A, RLangParser.IDENTIFIER]:
                localctx = RLangParser.Arith_bound_varContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 528
                self.any_bound_var()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 539
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,53,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 537
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
                    if la_ == 1:
                        localctx = RLangParser.Arith_times_divideContext(self, RLangParser.Arithmetic_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_exp)
                        self.state = 531
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 532
                        _la = self._input.LA(1)
                        if not(_la==RLangParser.TIMES or _la==RLangParser.DIVIDE):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 533
                        localctx.rhs = self.arithmetic_exp(6)
                        pass

                    elif la_ == 2:
                        localctx = RLangParser.Arith_plus_minusContext(self, RLangParser.Arithmetic_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_exp)
                        self.state = 534
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 535
                        _la = self._input.LA(1)
                        if not(_la==RLangParser.PLUS or _la==RLangParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 536
                        localctx.rhs = self.arithmetic_exp(5)
                        pass

             
                self.state = 541
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,53,self._ctx)

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


    class Bool_quant_arith_eqContext(Boolean_expContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Boolean_expContext
            super().__init__(parser)
            self.lhs = None # Quantification_expContext
            self.rhs = None # Arithmetic_expContext
            self.copyFrom(ctx)

        def quantification_exp(self):
            return self.getTypedRuleContext(RLangParser.Quantification_expContext,0)

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
        def arithmetic_exp(self):
            return self.getTypedRuleContext(RLangParser.Arithmetic_expContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_quant_arith_eq" ):
                listener.enterBool_quant_arith_eq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_quant_arith_eq" ):
                listener.exitBool_quant_arith_eq(self)


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


    class Bool_arith_quant_eqContext(Boolean_expContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Boolean_expContext
            super().__init__(parser)
            self.lhs = None # Arithmetic_expContext
            self.rhs = None # Quantification_expContext
            self.copyFrom(ctx)

        def arithmetic_exp(self):
            return self.getTypedRuleContext(RLangParser.Arithmetic_expContext,0)

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
        def quantification_exp(self):
            return self.getTypedRuleContext(RLangParser.Quantification_expContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_arith_quant_eq" ):
                listener.enterBool_arith_quant_eq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_arith_quant_eq" ):
                listener.exitBool_arith_quant_eq(self)


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
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_boolean_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 567
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Bool_parenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 543
                self.match(RLangParser.L_PAR)
                self.state = 544
                self.boolean_exp(0)
                self.state = 545
                self.match(RLangParser.R_PAR)
                pass

            elif la_ == 2:
                localctx = RLangParser.Bool_notContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 547
                self.match(RLangParser.NOT)
                self.state = 548
                self.boolean_exp(8)
                pass

            elif la_ == 3:
                localctx = RLangParser.Bool_inContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 549
                localctx.lhs = self.arithmetic_exp(0)
                self.state = 550
                self.match(RLangParser.IN)
                self.state = 551
                localctx.rhs = self.arithmetic_exp(0)
                pass

            elif la_ == 4:
                localctx = RLangParser.Bool_arith_quant_eqContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 553
                localctx.lhs = self.arithmetic_exp(0)
                self.state = 554
                _la = self._input.LA(1)
                if not(((((_la - 55)) & ~0x3f) == 0 and ((1 << (_la - 55)) & ((1 << (RLangParser.EQ_TO - 55)) | (1 << (RLangParser.GT_EQ - 55)) | (1 << (RLangParser.LT_EQ - 55)) | (1 << (RLangParser.NOT_EQ - 55)) | (1 << (RLangParser.LT - 55)) | (1 << (RLangParser.GT - 55)))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 555
                localctx.rhs = self.quantification_exp()
                pass

            elif la_ == 5:
                localctx = RLangParser.Bool_quant_arith_eqContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 557
                localctx.lhs = self.quantification_exp()
                self.state = 558
                _la = self._input.LA(1)
                if not(((((_la - 55)) & ~0x3f) == 0 and ((1 << (_la - 55)) & ((1 << (RLangParser.EQ_TO - 55)) | (1 << (RLangParser.GT_EQ - 55)) | (1 << (RLangParser.LT_EQ - 55)) | (1 << (RLangParser.NOT_EQ - 55)) | (1 << (RLangParser.LT - 55)) | (1 << (RLangParser.GT - 55)))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 559
                localctx.rhs = self.arithmetic_exp(0)
                pass

            elif la_ == 6:
                localctx = RLangParser.Bool_arith_eqContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 561
                localctx.lhs = self.arithmetic_exp(0)
                self.state = 562
                _la = self._input.LA(1)
                if not(((((_la - 55)) & ~0x3f) == 0 and ((1 << (_la - 55)) & ((1 << (RLangParser.EQ_TO - 55)) | (1 << (RLangParser.GT_EQ - 55)) | (1 << (RLangParser.LT_EQ - 55)) | (1 << (RLangParser.NOT_EQ - 55)) | (1 << (RLangParser.LT - 55)) | (1 << (RLangParser.GT - 55)))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 563
                localctx.rhs = self.arithmetic_exp(0)
                pass

            elif la_ == 7:
                localctx = RLangParser.Bool_bound_varContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 565
                self.any_bound_var()
                pass

            elif la_ == 8:
                localctx = RLangParser.Bool_tfContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 566
                _la = self._input.LA(1)
                if not(_la==RLangParser.TRUE or _la==RLangParser.FALSE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 580
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 578
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
                    if la_ == 1:
                        localctx = RLangParser.Bool_andContext(self, RLangParser.Boolean_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_exp)
                        self.state = 569
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 570
                        self.match(RLangParser.AND)
                        self.state = 571
                        localctx.rhs = self.boolean_exp(11)
                        pass

                    elif la_ == 2:
                        localctx = RLangParser.Bool_orContext(self, RLangParser.Boolean_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_exp)
                        self.state = 572
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 573
                        self.match(RLangParser.OR)
                        self.state = 574
                        localctx.rhs = self.boolean_exp(10)
                        pass

                    elif la_ == 3:
                        localctx = RLangParser.Bool_bool_eqContext(self, RLangParser.Boolean_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_exp)
                        self.state = 575
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 576
                        _la = self._input.LA(1)
                        if not(_la==RLangParser.EQ_TO or _la==RLangParser.NOT_EQ):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 577
                        localctx.rhs = self.boolean_exp(7)
                        pass

             
                self.state = 582
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Quantification_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def quantifier(self):
            return self.getTypedRuleContext(RLangParser.QuantifierContext,0)


        def L_PAR(self):
            return self.getToken(RLangParser.L_PAR, 0)

        def any_bound_class(self):
            return self.getTypedRuleContext(RLangParser.Any_bound_classContext,0)


        def R_PAR(self):
            return self.getToken(RLangParser.R_PAR, 0)

        def dot_exp(self):
            return self.getTypedRuleContext(RLangParser.Dot_expContext,0)


        def getRuleIndex(self):
            return RLangParser.RULE_quantification_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuantification_exp" ):
                listener.enterQuantification_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuantification_exp" ):
                listener.exitQuantification_exp(self)




    def quantification_exp(self):

        localctx = RLangParser.Quantification_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_quantification_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 583
            self.quantifier()
            self.state = 584
            self.match(RLangParser.L_PAR)
            self.state = 585
            self.any_bound_class()
            self.state = 586
            self.match(RLangParser.R_PAR)
            self.state = 587
            self.dot_exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuantifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ANY_CONDITION(self):
            return self.getToken(RLangParser.ANY_CONDITION, 0)

        def ALL_CONDITION(self):
            return self.getToken(RLangParser.ALL_CONDITION, 0)

        def getRuleIndex(self):
            return RLangParser.RULE_quantifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuantifier" ):
                listener.enterQuantifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuantifier" ):
                listener.exitQuantifier(self)




    def quantifier(self):

        localctx = RLangParser.QuantifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_quantifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 589
            _la = self._input.LA(1)
            if not(_la==RLangParser.ANY_CONDITION or _la==RLangParser.ALL_CONDITION):
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
            self.state = 593
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.LIST, RLangParser.SET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 591
                self.compound_type()
                pass
            elif token in [RLangParser.INT, RLangParser.FLOAT, RLangParser.STR, RLangParser.BOOL, RLangParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 592
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
            self.state = 615
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.LIST]:
                localctx = RLangParser.Type_listContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 595
                self.match(RLangParser.LIST)
                self.state = 603
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==RLangParser.L_BRK:
                    self.state = 596
                    self.match(RLangParser.L_BRK)
                    self.state = 599
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [RLangParser.INT, RLangParser.FLOAT, RLangParser.STR, RLangParser.BOOL, RLangParser.IDENTIFIER]:
                        self.state = 597
                        self.simple_type()
                        pass
                    elif token in [RLangParser.LIST, RLangParser.SET]:
                        self.state = 598
                        self.compound_type()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 601
                    self.match(RLangParser.R_BRK)


                pass
            elif token in [RLangParser.SET]:
                localctx = RLangParser.Type_setContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 605
                self.match(RLangParser.SET)
                self.state = 613
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==RLangParser.L_BRK:
                    self.state = 606
                    self.match(RLangParser.L_BRK)
                    self.state = 609
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [RLangParser.INT, RLangParser.FLOAT, RLangParser.STR, RLangParser.BOOL, RLangParser.IDENTIFIER]:
                        self.state = 607
                        self.simple_type()
                        pass
                    elif token in [RLangParser.LIST, RLangParser.SET]:
                        self.state = 608
                        self.compound_type()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 611
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
            self.state = 622
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 617
                self.match(RLangParser.INT)
                pass
            elif token in [RLangParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 618
                self.match(RLangParser.FLOAT)
                pass
            elif token in [RLangParser.STR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 619
                self.match(RLangParser.STR)
                pass
            elif token in [RLangParser.BOOL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 620
                self.match(RLangParser.BOOL)
                pass
            elif token in [RLangParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 5)
                self.state = 621
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


    class Bound_lifted_executionContext(Any_bound_varContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Any_bound_varContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def lifted_execution(self):
            return self.getTypedRuleContext(RLangParser.Lifted_executionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBound_lifted_execution" ):
                listener.enterBound_lifted_execution(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBound_lifted_execution" ):
                listener.exitBound_lifted_execution(self)


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
        self.enterRule(localctx, 84, self.RULE_any_bound_var)
        try:
            self.state = 644
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Bound_stateContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 624
                self.match(RLangParser.S)
                self.state = 626
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
                if la_ == 1:
                    self.state = 625
                    self.trailer()


                pass

            elif la_ == 2:
                localctx = RLangParser.Bound_next_stateContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 628
                self.match(RLangParser.S_PRIME)
                self.state = 630
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
                if la_ == 1:
                    self.state = 629
                    self.trailer()


                pass

            elif la_ == 3:
                localctx = RLangParser.Bound_identifierContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 632
                self.match(RLangParser.IDENTIFIER)
                self.state = 634
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
                if la_ == 1:
                    self.state = 633
                    self.match(RLangParser.PRIME)


                self.state = 639
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,67,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 636
                        self.trailer() 
                    self.state = 641
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,67,self._ctx)

                pass

            elif la_ == 4:
                localctx = RLangParser.Bound_actionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 642
                self.match(RLangParser.A)
                pass

            elif la_ == 5:
                localctx = RLangParser.Bound_lifted_executionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 643
                self.lifted_execution()
                pass


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
        self.enterRule(localctx, 86, self.RULE_any_bound_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 646
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
        self.enterRule(localctx, 88, self.RULE_trailer)
        try:
            self.state = 651
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Trailer_arrayContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 648
                self.int_array_exp()
                pass

            elif la_ == 2:
                localctx = RLangParser.Trailer_sliceContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 649
                self.slice_exp()
                pass

            elif la_ == 3:
                localctx = RLangParser.Trailer_objectContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 650
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
        self.enterRule(localctx, 90, self.RULE_dot_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 655 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 653
                    self.match(RLangParser.DOT)
                    self.state = 654
                    localctx._IDENTIFIER = self.match(RLangParser.IDENTIFIER)
                    localctx.attr.append(localctx._IDENTIFIER)

                else:
                    raise NoViableAltException(self)
                self.state = 657 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,70,self._ctx)

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
        self.enterRule(localctx, 92, self.RULE_any_array)
        try:
            self.state = 661
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Any_array_compoundContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 659
                self.compound_array_exp()
                pass

            elif la_ == 2:
                localctx = RLangParser.Any_array_any_numContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 660
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


    class Compound_array_arithContext(Compound_array_expContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Compound_array_expContext
            super().__init__(parser)
            self._arithmetic_exp = None # Arithmetic_expContext
            self.arr = list() # of Arithmetic_expContexts
            self.copyFrom(ctx)

        def L_BRK(self):
            return self.getToken(RLangParser.L_BRK, 0)
        def R_BRK(self):
            return self.getToken(RLangParser.R_BRK, 0)
        def arithmetic_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Arithmetic_expContext)
            else:
                return self.getTypedRuleContext(RLangParser.Arithmetic_expContext,i)

        def COM(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.COM)
            else:
                return self.getToken(RLangParser.COM, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompound_array_arith" ):
                listener.enterCompound_array_arith(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompound_array_arith" ):
                listener.exitCompound_array_arith(self)



    def compound_array_exp(self):

        localctx = RLangParser.Compound_array_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_compound_array_exp)
        self._la = 0 # Token type
        try:
            self.state = 686
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,74,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Compound_array_simpleContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 663
                self.any_num_array_exp()
                pass

            elif la_ == 2:
                localctx = RLangParser.Compound_array_arithContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 664
                self.match(RLangParser.L_BRK)
                self.state = 665
                localctx._arithmetic_exp = self.arithmetic_exp(0)
                localctx.arr.append(localctx._arithmetic_exp)
                self.state = 670
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.COM:
                    self.state = 666
                    self.match(RLangParser.COM)
                    self.state = 667
                    localctx._arithmetic_exp = self.arithmetic_exp(0)
                    localctx.arr.append(localctx._arithmetic_exp)
                    self.state = 672
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 673
                self.match(RLangParser.R_BRK)
                pass

            elif la_ == 3:
                localctx = RLangParser.Compound_array_compoundContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 675
                self.match(RLangParser.L_BRK)
                self.state = 676
                localctx._compound_array_exp = self.compound_array_exp()
                localctx.arr.append(localctx._compound_array_exp)
                self.state = 681
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.COM:
                    self.state = 677
                    self.match(RLangParser.COM)
                    self.state = 678
                    localctx._compound_array_exp = self.compound_array_exp()
                    localctx.arr.append(localctx._compound_array_exp)
                    self.state = 683
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 684
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
        self.enterRule(localctx, 96, self.RULE_int_array_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 688
            self.match(RLangParser.L_BRK)
            self.state = 689
            localctx._any_integer = self.any_integer()
            localctx.arr.append(localctx._any_integer)
            self.state = 694
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.COM:
                self.state = 690
                self.match(RLangParser.COM)
                self.state = 691
                localctx._any_integer = self.any_integer()
                localctx.arr.append(localctx._any_integer)
                self.state = 696
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 697
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
        self.enterRule(localctx, 98, self.RULE_any_num_array_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 699
            self.match(RLangParser.L_BRK)
            self.state = 700
            localctx._any_number = self.any_number()
            localctx.arr.append(localctx._any_number)
            self.state = 705
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.COM:
                self.state = 701
                self.match(RLangParser.COM)
                self.state = 702
                localctx._any_number = self.any_number()
                localctx.arr.append(localctx._any_number)
                self.state = 707
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 708
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
        self.enterRule(localctx, 100, self.RULE_slice_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 710
            self.match(RLangParser.L_BRK)
            self.state = 712
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.MINUS or _la==RLangParser.INTEGER:
                self.state = 711
                localctx.start_ind = self.any_integer()


            self.state = 714
            self.match(RLangParser.COL)
            self.state = 716
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.MINUS or _la==RLangParser.INTEGER:
                self.state = 715
                localctx.stop_ind = self.any_integer()


            self.state = 718
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
        self.enterRule(localctx, 102, self.RULE_integer_fraction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 720
            localctx.lhs = self.any_integer()
            self.state = 721
            self.match(RLangParser.DIVIDE)
            self.state = 722
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
        self.enterRule(localctx, 104, self.RULE_any_number)
        try:
            self.state = 726
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,79,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Any_num_intContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 724
                self.any_integer()
                pass

            elif la_ == 2:
                localctx = RLangParser.Any_num_decContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 725
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
        self.enterRule(localctx, 106, self.RULE_any_integer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 729
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.MINUS:
                self.state = 728
                self.match(RLangParser.MINUS)


            self.state = 731
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
        self.enterRule(localctx, 108, self.RULE_any_decimal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 734
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.MINUS:
                self.state = 733
                self.match(RLangParser.MINUS)


            self.state = 736
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
        self._predicates[35] = self.arithmetic_exp_sempred
        self._predicates[36] = self.boolean_exp_sempred
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
                return self.precpred(self._ctx, 10)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         




