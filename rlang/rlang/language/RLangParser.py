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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3S")
        buf.write("\u0334\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\3\2\7\2~\n\2\f\2\16\2\u0081\13\2\3")
        buf.write("\2\3\2\3\2\7\2\u0086\n\2\f\2\16\2\u0089\13\2\3\3\3\3\6")
        buf.write("\3\u008d\n\3\r\3\16\3\u008e\7\3\u0091\n\3\f\3\16\3\u0094")
        buf.write("\13\3\3\4\3\4\3\4\3\5\7\5\u009a\n\5\f\5\16\5\u009d\13")
        buf.write("\5\3\6\3\6\6\6\u00a1\n\6\r\6\16\6\u00a2\3\6\3\6\6\6\u00a7")
        buf.write("\n\6\r\6\16\6\u00a8\3\6\3\6\6\6\u00ad\n\6\r\6\16\6\u00ae")
        buf.write("\3\6\3\6\6\6\u00b3\n\6\r\6\16\6\u00b4\3\6\3\6\6\6\u00b9")
        buf.write("\n\6\r\6\16\6\u00ba\3\6\3\6\6\6\u00bf\n\6\r\6\16\6\u00c0")
        buf.write("\3\6\3\6\6\6\u00c5\n\6\r\6\16\6\u00c6\3\6\3\6\6\6\u00cb")
        buf.write("\n\6\r\6\16\6\u00cc\3\6\3\6\3\6\3\6\3\6\5\6\u00d4\n\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\5\7\u00db\n\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\5\b\u00e2\n\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\5\17\u0108\n\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\7\20\u0111\n\20\f\20\16\20\u0114\13\20\6\20")
        buf.write("\u0116\n\20\r\20\16\20\u0117\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\7\22\u0127\n")
        buf.write("\22\f\22\16\22\u012a\13\22\3\22\3\22\3\22\3\22\7\22\u0130")
        buf.write("\n\22\f\22\16\22\u0133\13\22\3\22\3\22\3\23\3\23\5\23")
        buf.write("\u0139\n\23\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u0141\n")
        buf.write("\24\f\24\16\24\u0144\13\24\3\24\3\24\3\25\3\25\3\25\5")
        buf.write("\25\u014b\n\25\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u0153")
        buf.write("\n\26\f\26\16\26\u0156\13\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\7\26\u015f\n\26\f\26\16\26\u0162\13\26\3\26")
        buf.write("\3\26\7\26\u0166\n\26\f\26\16\26\u0169\13\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\7\26\u0170\n\26\f\26\16\26\u0173\13\26")
        buf.write("\3\26\3\26\5\26\u0177\n\26\3\27\3\27\3\27\7\27\u017c\n")
        buf.write("\27\f\27\16\27\u017f\13\27\3\30\3\30\3\30\3\30\3\30\7")
        buf.write("\30\u0186\n\30\f\30\16\30\u0189\13\30\3\30\3\30\3\30\3")
        buf.write("\30\3\30\6\30\u0190\n\30\r\30\16\30\u0191\5\30\u0194\n")
        buf.write("\30\3\31\3\31\3\31\5\31\u0199\n\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\7\32\u01a0\n\32\f\32\16\32\u01a3\13\32\5\32\u01a5")
        buf.write("\n\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\7\34\u01b2\n\34\f\34\16\34\u01b5\13\34\6\34\u01b7")
        buf.write("\n\34\r\34\16\34\u01b8\3\35\3\35\3\35\5\35\u01be\n\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\7\36\u01cd\n\36\f\36\16\36\u01d0\13\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\5\36\u01d8\n\36\3\37\3\37\3")
        buf.write("\37\7\37\u01dd\n\37\f\37\16\37\u01e0\13\37\3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \6 \u01eb\n \r \16 \u01ec\5 \u01ef\n ")
        buf.write("\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\7\"\u01fa\n\"\f\"\16\"\u01fd")
        buf.write("\13\"\6\"\u01ff\n\"\r\"\16\"\u0200\3#\3#\3#\3#\3#\5#\u0208")
        buf.write("\n#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\7$\u0217\n")
        buf.write("$\f$\16$\u021a\13$\3$\3$\3$\3$\3$\3$\5$\u0222\n$\3%\3")
        buf.write("%\3%\7%\u0227\n%\f%\16%\u022a\13%\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\5&\u0235\n&\3&\3&\6&\u0239\n&\r&\16&\u023a\5&")
        buf.write("\u023d\n&\3\'\3\'\3\'\3(\3(\5(\u0244\n(\3(\3(\5(\u0248")
        buf.write("\n(\3(\5(\u024b\n(\5(\u024d\n(\3(\3(\3(\3(\5(\u0253\n")
        buf.write("(\3)\3)\3)\3*\3*\3*\3*\3*\5*\u025d\n*\3*\3*\3+\3+\3+\3")
        buf.write("+\3+\3+\3+\3+\3+\5+\u026a\n+\3+\3+\3+\3+\3+\3+\7+\u0272")
        buf.write("\n+\f+\16+\u0275\13+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,")
        buf.write("\3,\3,\3,\3,\3,\3,\5,\u0288\n,\3,\3,\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\7,\u0293\n,\f,\16,\u0296\13,\3-\3-\3-\3-\3-\5-\u029d")
        buf.write("\n-\3.\3.\3/\3/\5/\u02a3\n/\3\60\3\60\3\60\3\60\5\60\u02a9")
        buf.write("\n\60\3\60\3\60\5\60\u02ad\n\60\3\60\3\60\3\60\3\60\5")
        buf.write("\60\u02b3\n\60\3\60\3\60\5\60\u02b7\n\60\5\60\u02b9\n")
        buf.write("\60\3\61\3\61\3\61\3\61\3\61\5\61\u02c0\n\61\3\62\3\62")
        buf.write("\5\62\u02c4\n\62\3\62\3\62\5\62\u02c8\n\62\3\62\3\62\5")
        buf.write("\62\u02cc\n\62\3\62\7\62\u02cf\n\62\f\62\16\62\u02d2\13")
        buf.write("\62\3\62\3\62\5\62\u02d6\n\62\3\63\3\63\3\64\3\64\3\64")
        buf.write("\5\64\u02dd\n\64\3\65\3\65\6\65\u02e1\n\65\r\65\16\65")
        buf.write("\u02e2\3\66\3\66\5\66\u02e7\n\66\3\67\3\67\3\67\3\67\3")
        buf.write("\67\7\67\u02ee\n\67\f\67\16\67\u02f1\13\67\3\67\3\67\3")
        buf.write("\67\3\67\3\67\3\67\7\67\u02f9\n\67\f\67\16\67\u02fc\13")
        buf.write("\67\3\67\3\67\5\67\u0300\n\67\38\38\38\38\78\u0306\n8")
        buf.write("\f8\168\u0309\138\38\38\39\39\39\39\79\u0311\n9\f9\16")
        buf.write("9\u0314\139\39\39\3:\3:\5:\u031a\n:\3:\3:\5:\u031e\n:")
        buf.write("\3:\3:\3;\3;\3;\3;\3<\3<\5<\u0328\n<\3=\5=\u032b\n=\3")
        buf.write("=\3=\3>\5>\u0330\n>\3>\3>\3>\2\4TV?\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL")
        buf.write("NPRTVXZ\\^`bdfhjlnprtvxz\2\t\4\2++MM\3\2HI\3\2JK\4\2:")
        buf.write("=FG\3\2/\60\4\2::==\3\2\61\62\2\u0373\2\177\3\2\2\2\4")
        buf.write("\u0092\3\2\2\2\6\u0095\3\2\2\2\b\u009b\3\2\2\2\n\u00d3")
        buf.write("\3\2\2\2\f\u00d5\3\2\2\2\16\u00dc\3\2\2\2\20\u00e3\3\2")
        buf.write("\2\2\22\u00e8\3\2\2\2\24\u00ed\3\2\2\2\26\u00f2\3\2\2")
        buf.write("\2\30\u00f7\3\2\2\2\32\u00fc\3\2\2\2\34\u0101\3\2\2\2")
        buf.write("\36\u0115\3\2\2\2 \u0119\3\2\2\2\"\u011d\3\2\2\2$\u0138")
        buf.write("\3\2\2\2&\u013a\3\2\2\2(\u014a\3\2\2\2*\u014c\3\2\2\2")
        buf.write(",\u0178\3\2\2\2.\u0193\3\2\2\2\60\u0195\3\2\2\2\62\u019a")
        buf.write("\3\2\2\2\64\u01a8\3\2\2\2\66\u01b6\3\2\2\28\u01bd\3\2")
        buf.write("\2\2:\u01bf\3\2\2\2<\u01d9\3\2\2\2>\u01ee\3\2\2\2@\u01f0")
        buf.write("\3\2\2\2B\u01fe\3\2\2\2D\u0207\3\2\2\2F\u0209\3\2\2\2")
        buf.write("H\u0223\3\2\2\2J\u023c\3\2\2\2L\u023e\3\2\2\2N\u024c\3")
        buf.write("\2\2\2P\u0254\3\2\2\2R\u0257\3\2\2\2T\u0269\3\2\2\2V\u0287")
        buf.write("\3\2\2\2X\u0297\3\2\2\2Z\u029e\3\2\2\2\\\u02a2\3\2\2\2")
        buf.write("^\u02b8\3\2\2\2`\u02bf\3\2\2\2b\u02d5\3\2\2\2d\u02d7\3")
        buf.write("\2\2\2f\u02dc\3\2\2\2h\u02e0\3\2\2\2j\u02e6\3\2\2\2l\u02ff")
        buf.write("\3\2\2\2n\u0301\3\2\2\2p\u030c\3\2\2\2r\u0317\3\2\2\2")
        buf.write("t\u0321\3\2\2\2v\u0327\3\2\2\2x\u032a\3\2\2\2z\u032f\3")
        buf.write("\2\2\2|~\7\5\2\2}|\3\2\2\2~\u0081\3\2\2\2\177}\3\2\2\2")
        buf.write("\177\u0080\3\2\2\2\u0080\u0082\3\2\2\2\u0081\177\3\2\2")
        buf.write("\2\u0082\u0083\5\4\3\2\u0083\u0087\5\b\5\2\u0084\u0086")
        buf.write("\7\5\2\2\u0085\u0084\3\2\2\2\u0086\u0089\3\2\2\2\u0087")
        buf.write("\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088\3\3\2\2\2\u0089")
        buf.write("\u0087\3\2\2\2\u008a\u008c\5\6\4\2\u008b\u008d\7\5\2\2")
        buf.write("\u008c\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u008c\3")
        buf.write("\2\2\2\u008e\u008f\3\2\2\2\u008f\u0091\3\2\2\2\u0090\u008a")
        buf.write("\3\2\2\2\u0091\u0094\3\2\2\2\u0092\u0090\3\2\2\2\u0092")
        buf.write("\u0093\3\2\2\2\u0093\5\3\2\2\2\u0094\u0092\3\2\2\2\u0095")
        buf.write("\u0096\7\6\2\2\u0096\u0097\7N\2\2\u0097\7\3\2\2\2\u0098")
        buf.write("\u009a\5\n\6\2\u0099\u0098\3\2\2\2\u009a\u009d\3\2\2\2")
        buf.write("\u009b\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\t\3\2\2")
        buf.write("\2\u009d\u009b\3\2\2\2\u009e\u00a0\5\f\7\2\u009f\u00a1")
        buf.write("\7\5\2\2\u00a0\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2")
        buf.write("\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00d4\3\2\2\2")
        buf.write("\u00a4\u00a6\5\16\b\2\u00a5\u00a7\7\5\2\2\u00a6\u00a5")
        buf.write("\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a8")
        buf.write("\u00a9\3\2\2\2\u00a9\u00d4\3\2\2\2\u00aa\u00ac\5\20\t")
        buf.write("\2\u00ab\u00ad\7\5\2\2\u00ac\u00ab\3\2\2\2\u00ad\u00ae")
        buf.write("\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af")
        buf.write("\u00d4\3\2\2\2\u00b0\u00b2\5\22\n\2\u00b1\u00b3\7\5\2")
        buf.write("\2\u00b2\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b2")
        buf.write("\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00d4\3\2\2\2\u00b6")
        buf.write("\u00b8\5\24\13\2\u00b7\u00b9\7\5\2\2\u00b8\u00b7\3\2\2")
        buf.write("\2\u00b9\u00ba\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb")
        buf.write("\3\2\2\2\u00bb\u00d4\3\2\2\2\u00bc\u00be\5\26\f\2\u00bd")
        buf.write("\u00bf\7\5\2\2\u00be\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2")
        buf.write("\u00c0\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00d4\3")
        buf.write("\2\2\2\u00c2\u00c4\5\30\r\2\u00c3\u00c5\7\5\2\2\u00c4")
        buf.write("\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c4\3\2\2\2")
        buf.write("\u00c6\u00c7\3\2\2\2\u00c7\u00d4\3\2\2\2\u00c8\u00ca\5")
        buf.write("\32\16\2\u00c9\u00cb\7\5\2\2\u00ca\u00c9\3\2\2\2\u00cb")
        buf.write("\u00cc\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2")
        buf.write("\u00cd\u00d4\3\2\2\2\u00ce\u00d4\5\34\17\2\u00cf\u00d4")
        buf.write("\5\"\22\2\u00d0\u00d4\5&\24\2\u00d1\u00d4\5\64\33\2\u00d2")
        buf.write("\u00d4\5@!\2\u00d3\u009e\3\2\2\2\u00d3\u00a4\3\2\2\2\u00d3")
        buf.write("\u00aa\3\2\2\2\u00d3\u00b0\3\2\2\2\u00d3\u00b6\3\2\2\2")
        buf.write("\u00d3\u00bc\3\2\2\2\u00d3\u00c2\3\2\2\2\u00d3\u00c8\3")
        buf.write("\2\2\2\u00d3\u00ce\3\2\2\2\u00d3\u00cf\3\2\2\2\u00d3\u00d0")
        buf.write("\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d2\3\2\2\2\u00d4")
        buf.write("\13\3\2\2\2\u00d5\u00d6\7\16\2\2\u00d6\u00d7\7M\2\2\u00d7")
        buf.write("\u00da\7\63\2\2\u00d8\u00db\5T+\2\u00d9\u00db\5V,\2\u00da")
        buf.write("\u00d8\3\2\2\2\u00da\u00d9\3\2\2\2\u00db\r\3\2\2\2\u00dc")
        buf.write("\u00dd\7\17\2\2\u00dd\u00de\7M\2\2\u00de\u00e1\7\63\2")
        buf.write("\2\u00df\u00e2\5v<\2\u00e0\u00e2\5p9\2\u00e1\u00df\3\2")
        buf.write("\2\2\u00e1\u00e0\3\2\2\2\u00e2\17\3\2\2\2\u00e3\u00e4")
        buf.write("\7\n\2\2\u00e4\u00e5\7M\2\2\u00e5\u00e6\7\63\2\2\u00e6")
        buf.write("\u00e7\5b\62\2\u00e7\21\3\2\2\2\u00e8\u00e9\7\7\2\2\u00e9")
        buf.write("\u00ea\7M\2\2\u00ea\u00eb\7\63\2\2\u00eb\u00ec\5V,\2\u00ec")
        buf.write("\23\3\2\2\2\u00ed\u00ee\7\13\2\2\u00ee\u00ef\7M\2\2\u00ef")
        buf.write("\u00f0\7\63\2\2\u00f0\u00f1\5V,\2\u00f1\25\3\2\2\2\u00f2")
        buf.write("\u00f3\7\t\2\2\u00f3\u00f4\7M\2\2\u00f4\u00f5\7\63\2\2")
        buf.write("\u00f5\u00f6\5T+\2\u00f6\27\3\2\2\2\u00f7\u00f8\7\26\2")
        buf.write("\2\u00f8\u00f9\7M\2\2\u00f9\u00fa\7\63\2\2\u00fa\u00fb")
        buf.write("\5T+\2\u00fb\31\3\2\2\2\u00fc\u00fd\7\r\2\2\u00fd\u00fe")
        buf.write("\7M\2\2\u00fe\u00ff\7\63\2\2\u00ff\u0100\5\62\32\2\u0100")
        buf.write("\33\3\2\2\2\u0101\u0102\7\f\2\2\u0102\u0107\7M\2\2\u0103")
        buf.write("\u0104\7D\2\2\u0104\u0105\5d\63\2\u0105\u0106\7E\2\2\u0106")
        buf.write("\u0108\3\2\2\2\u0107\u0103\3\2\2\2\u0107\u0108\3\2\2\2")
        buf.write("\u0108\u0109\3\2\2\2\u0109\u010a\7>\2\2\u010a\u010b\7")
        buf.write("\3\2\2\u010b\u010c\5\36\20\2\u010c\u010d\7\4\2\2\u010d")
        buf.write("\35\3\2\2\2\u010e\u0112\5 \21\2\u010f\u0111\7\5\2\2\u0110")
        buf.write("\u010f\3\2\2\2\u0111\u0114\3\2\2\2\u0112\u0110\3\2\2\2")
        buf.write("\u0112\u0113\3\2\2\2\u0113\u0116\3\2\2\2\u0114\u0112\3")
        buf.write("\2\2\2\u0115\u010e\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0115")
        buf.write("\3\2\2\2\u0117\u0118\3\2\2\2\u0118\37\3\2\2\2\u0119\u011a")
        buf.write("\7M\2\2\u011a\u011b\7>\2\2\u011b\u011c\5\\/\2\u011c!\3")
        buf.write("\2\2\2\u011d\u011e\7\25\2\2\u011e\u011f\7M\2\2\u011f\u0120")
        buf.write("\7>\2\2\u0120\u0121\7\3\2\2\u0121\u0122\7&\2\2\u0122\u0123")
        buf.write("\5$\23\2\u0123\u0124\7\3\2\2\u0124\u0128\5(\25\2\u0125")
        buf.write("\u0127\7\5\2\2\u0126\u0125\3\2\2\2\u0127\u012a\3\2\2\2")
        buf.write("\u0128\u0126\3\2\2\2\u0128\u0129\3\2\2\2\u0129\u012b\3")
        buf.write("\2\2\2\u012a\u0128\3\2\2\2\u012b\u012c\7\4\2\2\u012c\u012d")
        buf.write("\7\'\2\2\u012d\u0131\5$\23\2\u012e\u0130\7\5\2\2\u012f")
        buf.write("\u012e\3\2\2\2\u0130\u0133\3\2\2\2\u0131\u012f\3\2\2\2")
        buf.write("\u0131\u0132\3\2\2\2\u0132\u0134\3\2\2\2\u0133\u0131\3")
        buf.write("\2\2\2\u0134\u0135\7\4\2\2\u0135#\3\2\2\2\u0136\u0139")
        buf.write("\5V,\2\u0137\u0139\7\61\2\2\u0138\u0136\3\2\2\2\u0138")
        buf.write("\u0137\3\2\2\2\u0139%\3\2\2\2\u013a\u013b\7\22\2\2\u013b")
        buf.write("\u013c\t\2\2\2\u013c\u013d\7>\2\2\u013d\u013e\7\3\2\2")
        buf.write("\u013e\u0142\5(\25\2\u013f\u0141\7\5\2\2\u0140\u013f\3")
        buf.write("\2\2\2\u0141\u0144\3\2\2\2\u0142\u0140\3\2\2\2\u0142\u0143")
        buf.write("\3\2\2\2\u0143\u0145\3\2\2\2\u0144\u0142\3\2\2\2\u0145")
        buf.write("\u0146\7\4\2\2\u0146\'\3\2\2\2\u0147\u014b\5\60\31\2\u0148")
        buf.write("\u014b\5*\26\2\u0149\u014b\5,\27\2\u014a\u0147\3\2\2\2")
        buf.write("\u014a\u0148\3\2\2\2\u014a\u0149\3\2\2\2\u014b)\3\2\2")
        buf.write("\2\u014c\u014d\7\"\2\2\u014d\u014e\5V,\2\u014e\u014f\7")
        buf.write(">\2\2\u014f\u0150\7\3\2\2\u0150\u0154\5(\25\2\u0151\u0153")
        buf.write("\7\5\2\2\u0152\u0151\3\2\2\2\u0153\u0156\3\2\2\2\u0154")
        buf.write("\u0152\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0157\3\2\2\2")
        buf.write("\u0156\u0154\3\2\2\2\u0157\u0167\7\4\2\2\u0158\u0159\7")
        buf.write("$\2\2\u0159\u015a\5V,\2\u015a\u015b\7>\2\2\u015b\u015c")
        buf.write("\7\3\2\2\u015c\u0160\5(\25\2\u015d\u015f\7\5\2\2\u015e")
        buf.write("\u015d\3\2\2\2\u015f\u0162\3\2\2\2\u0160\u015e\3\2\2\2")
        buf.write("\u0160\u0161\3\2\2\2\u0161\u0163\3\2\2\2\u0162\u0160\3")
        buf.write("\2\2\2\u0163\u0164\7\4\2\2\u0164\u0166\3\2\2\2\u0165\u0158")
        buf.write("\3\2\2\2\u0166\u0169\3\2\2\2\u0167\u0165\3\2\2\2\u0167")
        buf.write("\u0168\3\2\2\2\u0168\u0176\3\2\2\2\u0169\u0167\3\2\2\2")
        buf.write("\u016a\u016b\7#\2\2\u016b\u016c\7>\2\2\u016c\u016d\7\3")
        buf.write("\2\2\u016d\u0171\5(\25\2\u016e\u0170\7\5\2\2\u016f\u016e")
        buf.write("\3\2\2\2\u0170\u0173\3\2\2\2\u0171\u016f\3\2\2\2\u0171")
        buf.write("\u0172\3\2\2\2\u0172\u0174\3\2\2\2\u0173\u0171\3\2\2\2")
        buf.write("\u0174\u0175\7\4\2\2\u0175\u0177\3\2\2\2\u0176\u016a\3")
        buf.write("\2\2\2\u0176\u0177\3\2\2\2\u0177+\3\2\2\2\u0178\u017d")
        buf.write("\5.\30\2\u0179\u017a\7-\2\2\u017a\u017c\5.\30\2\u017b")
        buf.write("\u0179\3\2\2\2\u017c\u017f\3\2\2\2\u017d\u017b\3\2\2\2")
        buf.write("\u017d\u017e\3\2\2\2\u017e-\3\2\2\2\u017f\u017d\3\2\2")
        buf.write("\2\u0180\u0181\5R*\2\u0181\u0182\7>\2\2\u0182\u0183\7")
        buf.write("\3\2\2\u0183\u0187\5(\25\2\u0184\u0186\7\5\2\2\u0185\u0184")
        buf.write("\3\2\2\2\u0186\u0189\3\2\2\2\u0187\u0185\3\2\2\2\u0187")
        buf.write("\u0188\3\2\2\2\u0188\u018a\3\2\2\2\u0189\u0187\3\2\2\2")
        buf.write("\u018a\u018b\7\4\2\2\u018b\u0194\3\2\2\2\u018c\u018d\5")
        buf.write("\60\31\2\u018d\u018f\5R*\2\u018e\u0190\7\5\2\2\u018f\u018e")
        buf.write("\3\2\2\2\u0190\u0191\3\2\2\2\u0191\u018f\3\2\2\2\u0191")
        buf.write("\u0192\3\2\2\2\u0192\u0194\3\2\2\2\u0193\u0180\3\2\2\2")
        buf.write("\u0193\u018c\3\2\2\2\u0194/\3\2\2\2\u0195\u0198\7\24\2")
        buf.write("\2\u0196\u0199\7M\2\2\u0197\u0199\5T+\2\u0198\u0196\3")
        buf.write("\2\2\2\u0198\u0197\3\2\2\2\u0199\61\3\2\2\2\u019a\u019b")
        buf.write("\7M\2\2\u019b\u01a4\7D\2\2\u019c\u01a1\5T+\2\u019d\u019e")
        buf.write("\7?\2\2\u019e\u01a0\5T+\2\u019f\u019d\3\2\2\2\u01a0\u01a3")
        buf.write("\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2")
        buf.write("\u01a5\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4\u019c\3\2\2\2")
        buf.write("\u01a4\u01a5\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a7\7")
        buf.write("E\2\2\u01a7\63\3\2\2\2\u01a8\u01a9\7\23\2\2\u01a9\u01aa")
        buf.write("\t\2\2\2\u01aa\u01ab\7>\2\2\u01ab\u01ac\7\3\2\2\u01ac")
        buf.write("\u01ad\5\66\34\2\u01ad\u01ae\7\4\2\2\u01ae\65\3\2\2\2")
        buf.write("\u01af\u01b3\58\35\2\u01b0\u01b2\7\5\2\2\u01b1\u01b0\3")
        buf.write("\2\2\2\u01b2\u01b5\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b4")
        buf.write("\3\2\2\2\u01b4\u01b7\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b6")
        buf.write("\u01af\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01b6\3\2\2\2")
        buf.write("\u01b8\u01b9\3\2\2\2\u01b9\67\3\2\2\2\u01ba\u01be\5\60")
        buf.write("\31\2\u01bb\u01be\5:\36\2\u01bc\u01be\5<\37\2\u01bd\u01ba")
        buf.write("\3\2\2\2\u01bd\u01bb\3\2\2\2\u01bd\u01bc\3\2\2\2\u01be")
        buf.write("9\3\2\2\2\u01bf\u01c0\7\"\2\2\u01c0\u01c1\5V,\2\u01c1")
        buf.write("\u01c2\7>\2\2\u01c2\u01c3\7\3\2\2\u01c3\u01c4\5\66\34")
        buf.write("\2\u01c4\u01ce\7\4\2\2\u01c5\u01c6\7$\2\2\u01c6\u01c7")
        buf.write("\5V,\2\u01c7\u01c8\7>\2\2\u01c8\u01c9\7\3\2\2\u01c9\u01ca")
        buf.write("\5\66\34\2\u01ca\u01cb\7\4\2\2\u01cb\u01cd\3\2\2\2\u01cc")
        buf.write("\u01c5\3\2\2\2\u01cd\u01d0\3\2\2\2\u01ce\u01cc\3\2\2\2")
        buf.write("\u01ce\u01cf\3\2\2\2\u01cf\u01d7\3\2\2\2\u01d0\u01ce\3")
        buf.write("\2\2\2\u01d1\u01d2\7#\2\2\u01d2\u01d3\7>\2\2\u01d3\u01d4")
        buf.write("\7\3\2\2\u01d4\u01d5\5\66\34\2\u01d5\u01d6\7\4\2\2\u01d6")
        buf.write("\u01d8\3\2\2\2\u01d7\u01d1\3\2\2\2\u01d7\u01d8\3\2\2\2")
        buf.write("\u01d8;\3\2\2\2\u01d9\u01de\5> \2\u01da\u01db\7-\2\2\u01db")
        buf.write("\u01dd\5> \2\u01dc\u01da\3\2\2\2\u01dd\u01e0\3\2\2\2\u01de")
        buf.write("\u01dc\3\2\2\2\u01de\u01df\3\2\2\2\u01df=\3\2\2\2\u01e0")
        buf.write("\u01de\3\2\2\2\u01e1\u01e2\5R*\2\u01e2\u01e3\7>\2\2\u01e3")
        buf.write("\u01e4\7\3\2\2\u01e4\u01e5\5\66\34\2\u01e5\u01e6\7\4\2")
        buf.write("\2\u01e6\u01ef\3\2\2\2\u01e7\u01e8\5\60\31\2\u01e8\u01ea")
        buf.write("\5R*\2\u01e9\u01eb\7\5\2\2\u01ea\u01e9\3\2\2\2\u01eb\u01ec")
        buf.write("\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ec\u01ed\3\2\2\2\u01ed")
        buf.write("\u01ef\3\2\2\2\u01ee\u01e1\3\2\2\2\u01ee\u01e7\3\2\2\2")
        buf.write("\u01ef?\3\2\2\2\u01f0\u01f1\7\20\2\2\u01f1\u01f2\t\2\2")
        buf.write("\2\u01f2\u01f3\7>\2\2\u01f3\u01f4\7\3\2\2\u01f4\u01f5")
        buf.write("\5B\"\2\u01f5\u01f6\7\4\2\2\u01f6A\3\2\2\2\u01f7\u01fb")
        buf.write("\5D#\2\u01f8\u01fa\7\5\2\2\u01f9\u01f8\3\2\2\2\u01fa\u01fd")
        buf.write("\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc")
        buf.write("\u01ff\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fe\u01f7\3\2\2\2")
        buf.write("\u01ff\u0200\3\2\2\2\u0200\u01fe\3\2\2\2\u0200\u0201\3")
        buf.write("\2\2\2\u0201C\3\2\2\2\u0202\u0208\5L\'\2\u0203\u0208\5")
        buf.write("N(\2\u0204\u0208\5P)\2\u0205\u0208\5F$\2\u0206\u0208\5")
        buf.write("H%\2\u0207\u0202\3\2\2\2\u0207\u0203\3\2\2\2\u0207\u0204")
        buf.write("\3\2\2\2\u0207\u0205\3\2\2\2\u0207\u0206\3\2\2\2\u0208")
        buf.write("E\3\2\2\2\u0209\u020a\7\"\2\2\u020a\u020b\5V,\2\u020b")
        buf.write("\u020c\7>\2\2\u020c\u020d\7\3\2\2\u020d\u020e\5B\"\2\u020e")
        buf.write("\u0218\7\4\2\2\u020f\u0210\7$\2\2\u0210\u0211\5V,\2\u0211")
        buf.write("\u0212\7>\2\2\u0212\u0213\7\3\2\2\u0213\u0214\5B\"\2\u0214")
        buf.write("\u0215\7\4\2\2\u0215\u0217\3\2\2\2\u0216\u020f\3\2\2\2")
        buf.write("\u0217\u021a\3\2\2\2\u0218\u0216\3\2\2\2\u0218\u0219\3")
        buf.write("\2\2\2\u0219\u0221\3\2\2\2\u021a\u0218\3\2\2\2\u021b\u021c")
        buf.write("\7#\2\2\u021c\u021d\7>\2\2\u021d\u021e\7\3\2\2\u021e\u021f")
        buf.write("\5B\"\2\u021f\u0220\7\4\2\2\u0220\u0222\3\2\2\2\u0221")
        buf.write("\u021b\3\2\2\2\u0221\u0222\3\2\2\2\u0222G\3\2\2\2\u0223")
        buf.write("\u0228\5J&\2\u0224\u0225\7-\2\2\u0225\u0227\5J&\2\u0226")
        buf.write("\u0224\3\2\2\2\u0227\u022a\3\2\2\2\u0228\u0226\3\2\2\2")
        buf.write("\u0228\u0229\3\2\2\2\u0229I\3\2\2\2\u022a\u0228\3\2\2")
        buf.write("\2\u022b\u022c\5R*\2\u022c\u022d\7>\2\2\u022d\u022e\7")
        buf.write("\3\2\2\u022e\u022f\5B\"\2\u022f\u0230\7\4\2\2\u0230\u023d")
        buf.write("\3\2\2\2\u0231\u0235\5L\'\2\u0232\u0235\5N(\2\u0233\u0235")
        buf.write("\5P)\2\u0234\u0231\3\2\2\2\u0234\u0232\3\2\2\2\u0234\u0233")
        buf.write("\3\2\2\2\u0235\u0236\3\2\2\2\u0236\u0238\5R*\2\u0237\u0239")
        buf.write("\7\5\2\2\u0238\u0237\3\2\2\2\u0239\u023a\3\2\2\2\u023a")
        buf.write("\u0238\3\2\2\2\u023a\u023b\3\2\2\2\u023b\u023d\3\2\2\2")
        buf.write("\u023c\u022b\3\2\2\2\u023c\u0234\3\2\2\2\u023dK\3\2\2")
        buf.write("\2\u023e\u023f\7\21\2\2\u023f\u0240\5T+\2\u0240M\3\2\2")
        buf.write("\2\u0241\u0243\7\35\2\2\u0242\u0244\5h\65\2\u0243\u0242")
        buf.write("\3\2\2\2\u0243\u0244\3\2\2\2\u0244\u024d\3\2\2\2\u0245")
        buf.write("\u0247\7M\2\2\u0246\u0248\5h\65\2\u0247\u0246\3\2\2\2")
        buf.write("\u0247\u0248\3\2\2\2\u0248\u024a\3\2\2\2\u0249\u024b\7")
        buf.write("!\2\2\u024a\u0249\3\2\2\2\u024a\u024b\3\2\2\2\u024b\u024d")
        buf.write("\3\2\2\2\u024c\u0241\3\2\2\2\u024c\u0245\3\2\2\2\u024d")
        buf.write("\u024e\3\2\2\2\u024e\u0252\7\64\2\2\u024f\u0253\5T+\2")
        buf.write("\u0250\u0253\5V,\2\u0251\u0253\5\62\32\2\u0252\u024f\3")
        buf.write("\2\2\2\u0252\u0250\3\2\2\2\u0252\u0251\3\2\2\2\u0253O")
        buf.write("\3\2\2\2\u0254\u0255\7\64\2\2\u0255\u0256\7M\2\2\u0256")
        buf.write("Q\3\2\2\2\u0257\u0258\7(\2\2\u0258\u0259\7 \2\2\u0259")
        buf.write("\u025c\7D\2\2\u025a\u025d\5v<\2\u025b\u025d\5t;\2\u025c")
        buf.write("\u025a\3\2\2\2\u025c\u025b\3\2\2\2\u025d\u025e\3\2\2\2")
        buf.write("\u025e\u025f\7E\2\2\u025fS\3\2\2\2\u0260\u0261\b+\1\2")
        buf.write("\u0261\u0262\7D\2\2\u0262\u0263\5T+\2\u0263\u0264\7E\2")
        buf.write("\2\u0264\u026a\3\2\2\2\u0265\u026a\5v<\2\u0266\u026a\5")
        buf.write("j\66\2\u0267\u026a\5b\62\2\u0268\u026a\5X-\2\u0269\u0260")
        buf.write("\3\2\2\2\u0269\u0265\3\2\2\2\u0269\u0266\3\2\2\2\u0269")
        buf.write("\u0267\3\2\2\2\u0269\u0268\3\2\2\2\u026a\u0273\3\2\2\2")
        buf.write("\u026b\u026c\f\b\2\2\u026c\u026d\t\3\2\2\u026d\u0272\5")
        buf.write("T+\t\u026e\u026f\f\7\2\2\u026f\u0270\t\4\2\2\u0270\u0272")
        buf.write("\5T+\b\u0271\u026b\3\2\2\2\u0271\u026e\3\2\2\2\u0272\u0275")
        buf.write("\3\2\2\2\u0273\u0271\3\2\2\2\u0273\u0274\3\2\2\2\u0274")
        buf.write("U\3\2\2\2\u0275\u0273\3\2\2\2\u0276\u0277\b,\1\2\u0277")
        buf.write("\u0278\7D\2\2\u0278\u0279\5V,\2\u0279\u027a\7E\2\2\u027a")
        buf.write("\u0288\3\2\2\2\u027b\u027c\7.\2\2\u027c\u0288\5V,\b\u027d")
        buf.write("\u027e\5T+\2\u027e\u027f\7%\2\2\u027f\u0280\5T+\2\u0280")
        buf.write("\u0288\3\2\2\2\u0281\u0282\5T+\2\u0282\u0283\t\5\2\2\u0283")
        buf.write("\u0284\5T+\2\u0284\u0288\3\2\2\2\u0285\u0288\5b\62\2\u0286")
        buf.write("\u0288\t\6\2\2\u0287\u0276\3\2\2\2\u0287\u027b\3\2\2\2")
        buf.write("\u0287\u027d\3\2\2\2\u0287\u0281\3\2\2\2\u0287\u0285\3")
        buf.write("\2\2\2\u0287\u0286\3\2\2\2\u0288\u0294\3\2\2\2\u0289\u028a")
        buf.write("\f\n\2\2\u028a\u028b\7,\2\2\u028b\u0293\5V,\13\u028c\u028d")
        buf.write("\f\t\2\2\u028d\u028e\7-\2\2\u028e\u0293\5V,\n\u028f\u0290")
        buf.write("\f\6\2\2\u0290\u0291\t\7\2\2\u0291\u0293\5V,\7\u0292\u0289")
        buf.write("\3\2\2\2\u0292\u028c\3\2\2\2\u0292\u028f\3\2\2\2\u0293")
        buf.write("\u0296\3\2\2\2\u0294\u0292\3\2\2\2\u0294\u0295\3\2\2\2")
        buf.write("\u0295W\3\2\2\2\u0296\u0294\3\2\2\2\u0297\u0298\5Z.\2")
        buf.write("\u0298\u0299\7D\2\2\u0299\u029a\5d\63\2\u029a\u029c\7")
        buf.write("E\2\2\u029b\u029d\5h\65\2\u029c\u029b\3\2\2\2\u029c\u029d")
        buf.write("\3\2\2\2\u029dY\3\2\2\2\u029e\u029f\t\b\2\2\u029f[\3\2")
        buf.write("\2\2\u02a0\u02a3\5^\60\2\u02a1\u02a3\5`\61\2\u02a2\u02a0")
        buf.write("\3\2\2\2\u02a2\u02a1\3\2\2\2\u02a3]\3\2\2\2\u02a4\u02ac")
        buf.write("\7\32\2\2\u02a5\u02a8\7@\2\2\u02a6\u02a9\5`\61\2\u02a7")
        buf.write("\u02a9\5^\60\2\u02a8\u02a6\3\2\2\2\u02a8\u02a7\3\2\2\2")
        buf.write("\u02a9\u02aa\3\2\2\2\u02aa\u02ab\7A\2\2\u02ab\u02ad\3")
        buf.write("\2\2\2\u02ac\u02a5\3\2\2\2\u02ac\u02ad\3\2\2\2\u02ad\u02b9")
        buf.write("\3\2\2\2\u02ae\u02b6\7\33\2\2\u02af\u02b2\7@\2\2\u02b0")
        buf.write("\u02b3\5`\61\2\u02b1\u02b3\5^\60\2\u02b2\u02b0\3\2\2\2")
        buf.write("\u02b2\u02b1\3\2\2\2\u02b3\u02b4\3\2\2\2\u02b4\u02b5\7")
        buf.write("A\2\2\u02b5\u02b7\3\2\2\2\u02b6\u02af\3\2\2\2\u02b6\u02b7")
        buf.write("\3\2\2\2\u02b7\u02b9\3\2\2\2\u02b8\u02a4\3\2\2\2\u02b8")
        buf.write("\u02ae\3\2\2\2\u02b9_\3\2\2\2\u02ba\u02c0\7\27\2\2\u02bb")
        buf.write("\u02c0\7\30\2\2\u02bc\u02c0\7\31\2\2\u02bd\u02c0\7\34")
        buf.write("\2\2\u02be\u02c0\5d\63\2\u02bf\u02ba\3\2\2\2\u02bf\u02bb")
        buf.write("\3\2\2\2\u02bf\u02bc\3\2\2\2\u02bf\u02bd\3\2\2\2\u02bf")
        buf.write("\u02be\3\2\2\2\u02c0a\3\2\2\2\u02c1\u02c3\7\36\2\2\u02c2")
        buf.write("\u02c4\5f\64\2\u02c3\u02c2\3\2\2\2\u02c3\u02c4\3\2\2\2")
        buf.write("\u02c4\u02d6\3\2\2\2\u02c5\u02c7\7\35\2\2\u02c6\u02c8")
        buf.write("\5f\64\2\u02c7\u02c6\3\2\2\2\u02c7\u02c8\3\2\2\2\u02c8")
        buf.write("\u02d6\3\2\2\2\u02c9\u02cb\7M\2\2\u02ca\u02cc\7!\2\2\u02cb")
        buf.write("\u02ca\3\2\2\2\u02cb\u02cc\3\2\2\2\u02cc\u02d0\3\2\2\2")
        buf.write("\u02cd\u02cf\5f\64\2\u02ce\u02cd\3\2\2\2\u02cf\u02d2\3")
        buf.write("\2\2\2\u02d0\u02ce\3\2\2\2\u02d0\u02d1\3\2\2\2\u02d1\u02d6")
        buf.write("\3\2\2\2\u02d2\u02d0\3\2\2\2\u02d3\u02d6\7\37\2\2\u02d4")
        buf.write("\u02d6\5\62\32\2\u02d5\u02c1\3\2\2\2\u02d5\u02c5\3\2\2")
        buf.write("\2\u02d5\u02c9\3\2\2\2\u02d5\u02d3\3\2\2\2\u02d5\u02d4")
        buf.write("\3\2\2\2\u02d6c\3\2\2\2\u02d7\u02d8\7M\2\2\u02d8e\3\2")
        buf.write("\2\2\u02d9\u02dd\5n8\2\u02da\u02dd\5r:\2\u02db\u02dd\5")
        buf.write("h\65\2\u02dc\u02d9\3\2\2\2\u02dc\u02da\3\2\2\2\u02dc\u02db")
        buf.write("\3\2\2\2\u02ddg\3\2\2\2\u02de\u02df\7Q\2\2\u02df\u02e1")
        buf.write("\7M\2\2\u02e0\u02de\3\2\2\2\u02e1\u02e2\3\2\2\2\u02e2")
        buf.write("\u02e0\3\2\2\2\u02e2\u02e3\3\2\2\2\u02e3i\3\2\2\2\u02e4")
        buf.write("\u02e7\5l\67\2\u02e5\u02e7\5p9\2\u02e6\u02e4\3\2\2\2\u02e6")
        buf.write("\u02e5\3\2\2\2\u02e7k\3\2\2\2\u02e8\u0300\5p9\2\u02e9")
        buf.write("\u02ea\7@\2\2\u02ea\u02ef\5T+\2\u02eb\u02ec\7?\2\2\u02ec")
        buf.write("\u02ee\5T+\2\u02ed\u02eb\3\2\2\2\u02ee\u02f1\3\2\2\2\u02ef")
        buf.write("\u02ed\3\2\2\2\u02ef\u02f0\3\2\2\2\u02f0\u02f2\3\2\2\2")
        buf.write("\u02f1\u02ef\3\2\2\2\u02f2\u02f3\7A\2\2\u02f3\u0300\3")
        buf.write("\2\2\2\u02f4\u02f5\7@\2\2\u02f5\u02fa\5l\67\2\u02f6\u02f7")
        buf.write("\7?\2\2\u02f7\u02f9\5l\67\2\u02f8\u02f6\3\2\2\2\u02f9")
        buf.write("\u02fc\3\2\2\2\u02fa\u02f8\3\2\2\2\u02fa\u02fb\3\2\2\2")
        buf.write("\u02fb\u02fd\3\2\2\2\u02fc\u02fa\3\2\2\2\u02fd\u02fe\7")
        buf.write("A\2\2\u02fe\u0300\3\2\2\2\u02ff\u02e8\3\2\2\2\u02ff\u02e9")
        buf.write("\3\2\2\2\u02ff\u02f4\3\2\2\2\u0300m\3\2\2\2\u0301\u0302")
        buf.write("\7@\2\2\u0302\u0307\5x=\2\u0303\u0304\7?\2\2\u0304\u0306")
        buf.write("\5x=\2\u0305\u0303\3\2\2\2\u0306\u0309\3\2\2\2\u0307\u0305")
        buf.write("\3\2\2\2\u0307\u0308\3\2\2\2\u0308\u030a\3\2\2\2\u0309")
        buf.write("\u0307\3\2\2\2\u030a\u030b\7A\2\2\u030bo\3\2\2\2\u030c")
        buf.write("\u030d\7@\2\2\u030d\u0312\5v<\2\u030e\u030f\7?\2\2\u030f")
        buf.write("\u0311\5v<\2\u0310\u030e\3\2\2\2\u0311\u0314\3\2\2\2\u0312")
        buf.write("\u0310\3\2\2\2\u0312\u0313\3\2\2\2\u0313\u0315\3\2\2\2")
        buf.write("\u0314\u0312\3\2\2\2\u0315\u0316\7A\2\2\u0316q\3\2\2\2")
        buf.write("\u0317\u0319\7@\2\2\u0318\u031a\5x=\2\u0319\u0318\3\2")
        buf.write("\2\2\u0319\u031a\3\2\2\2\u031a\u031b\3\2\2\2\u031b\u031d")
        buf.write("\7>\2\2\u031c\u031e\5x=\2\u031d\u031c\3\2\2\2\u031d\u031e")
        buf.write("\3\2\2\2\u031e\u031f\3\2\2\2\u031f\u0320\7A\2\2\u0320")
        buf.write("s\3\2\2\2\u0321\u0322\5x=\2\u0322\u0323\7I\2\2\u0323\u0324")
        buf.write("\5x=\2\u0324u\3\2\2\2\u0325\u0328\5x=\2\u0326\u0328\5")
        buf.write("z>\2\u0327\u0325\3\2\2\2\u0327\u0326\3\2\2\2\u0328w\3")
        buf.write("\2\2\2\u0329\u032b\7K\2\2\u032a\u0329\3\2\2\2\u032a\u032b")
        buf.write("\3\2\2\2\u032b\u032c\3\2\2\2\u032c\u032d\7P\2\2\u032d")
        buf.write("y\3\2\2\2\u032e\u0330\7K\2\2\u032f\u032e\3\2\2\2\u032f")
        buf.write("\u0330\3\2\2\2\u0330\u0331\3\2\2\2\u0331\u0332\7O\2\2")
        buf.write("\u0332{\3\2\2\2]\177\u0087\u008e\u0092\u009b\u00a2\u00a8")
        buf.write("\u00ae\u00b4\u00ba\u00c0\u00c6\u00cc\u00d3\u00da\u00e1")
        buf.write("\u0107\u0112\u0117\u0128\u0131\u0138\u0142\u014a\u0154")
        buf.write("\u0160\u0167\u0171\u0176\u017d\u0187\u0191\u0193\u0198")
        buf.write("\u01a1\u01a4\u01b3\u01b8\u01bd\u01ce\u01d7\u01de\u01ec")
        buf.write("\u01ee\u01fb\u0200\u0207\u0218\u0221\u0228\u0234\u023a")
        buf.write("\u023c\u0243\u0247\u024a\u024c\u0252\u025c\u0269\u0271")
        buf.write("\u0273\u0287\u0292\u0294\u029c\u02a2\u02a8\u02ac\u02b2")
        buf.write("\u02b6\u02b8\u02bf\u02c3\u02c7\u02cb\u02d0\u02d5\u02dc")
        buf.write("\u02e2\u02e6\u02ef\u02fa\u02ff\u0307\u0312\u0319\u031d")
        buf.write("\u0327\u032a\u032f")
        return buf.getvalue()


class RLangParser ( Parser ):

    grammarFileName = "RLangParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'import'", "'Proposition'", "'Predicate'", "'Feature'", 
                     "'Factor'", "'Goal'", "'Class'", "'Object'", "'Constant'", 
                     "'Action'", "'Effect'", "'Reward'", "'Policy'", "'Plan'", 
                     "'Execute'", "'Option'", "'MarkovFeature'", "'int'", 
                     "'float'", "'str'", "'list'", "'set'", "'boolean'", 
                     "<INVALID>", "'S'", "'A'", "'P'", "'''", "'if'", "'else'", 
                     "'elif'", "'in'", "'init'", "'until'", "'with'", "'then'", 
                     "'never'", "'main'", "'and'", "'or'", "'not'", "'True'", 
                     "'False'", "'Any'", "'All'", "':='", "'->'", "'='", 
                     "'*='", "'/='", "'+='", "'-='", "'=='", "'>='", "'<='", 
                     "'!='", "':'", "','", "'['", "']'", "'{'", "'}'", "'('", 
                     "')'", "'<'", "'>'", "'*'", "'/'", "'+'", "'-'", "'\"'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'.'" ]

    symbolicNames = [ "<INVALID>", "INDENT", "DEDENT", "NL", "IMPORT", "PROPOSITION", 
                      "PREDICATE", "FEATURE", "FACTOR", "GOAL", "CLASS", 
                      "OBJECT", "CONSTANT", "ACTION", "EFFECT", "REWARD", 
                      "POLICY", "PLAN", "EXECUTE", "OPTION", "MARKOVFEATURE", 
                      "INT", "FLOAT", "STR", "LIST", "SET", "BOOL", "S_PRIME", 
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
    RULE_plan = 25
    RULE_plan_statement_collection = 26
    RULE_plan_statement = 27
    RULE_conditional_plan = 28
    RULE_probabilistic_plan = 29
    RULE_probabilistic_plan_statement = 30
    RULE_effect = 31
    RULE_effect_statement_collection = 32
    RULE_effect_statement = 33
    RULE_conditional_effect = 34
    RULE_probabilistic_effect = 35
    RULE_probabilistic_effect_statement = 36
    RULE_reward = 37
    RULE_prediction = 38
    RULE_effect_reference = 39
    RULE_probabilistic_condition = 40
    RULE_arithmetic_exp = 41
    RULE_boolean_exp = 42
    RULE_quantification_exp = 43
    RULE_quantifier = 44
    RULE_type_def = 45
    RULE_compound_type = 46
    RULE_simple_type = 47
    RULE_any_bound_var = 48
    RULE_any_bound_class = 49
    RULE_trailer = 50
    RULE_dot_exp = 51
    RULE_any_array = 52
    RULE_compound_array_exp = 53
    RULE_int_array_exp = 54
    RULE_any_num_array_exp = 55
    RULE_slice_exp = 56
    RULE_integer_fraction = 57
    RULE_any_number = 58
    RULE_any_integer = 59
    RULE_any_decimal = 60

    ruleNames =  [ "program", "imports", "import_stat", "declarations", 
                   "dec", "constant", "action", "factor", "proposition", 
                   "goal", "feature", "markov_feature", "object_def", "class_def", 
                   "attribute_definition_collection", "attribute_definition", 
                   "option", "option_condition", "policy", "policy_statement", 
                   "conditional_subpolicy", "probabilistic_subpolicy", "probabilistic_policy_statement", 
                   "execute", "lifted_execution", "plan", "plan_statement_collection", 
                   "plan_statement", "conditional_plan", "probabilistic_plan", 
                   "probabilistic_plan_statement", "effect", "effect_statement_collection", 
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
    PLAN=17
    EXECUTE=18
    OPTION=19
    MARKOVFEATURE=20
    INT=21
    FLOAT=22
    STR=23
    LIST=24
    SET=25
    BOOL=26
    S_PRIME=27
    S=28
    A=29
    P=30
    PRIME=31
    IF=32
    ELSE=33
    ELIF=34
    IN=35
    INIT=36
    UNTIL=37
    WITH=38
    THEN=39
    NEVER=40
    MAIN=41
    AND=42
    OR=43
    NOT=44
    TRUE=45
    FALSE=46
    ANY_CONDITION=47
    ALL_CONDITION=48
    BIND=49
    PREDICT=50
    ASSIGN=51
    TIMES_EQ=52
    DIV_EQ=53
    PLUS_EQ=54
    MINUS_EQ=55
    EQ_TO=56
    GT_EQ=57
    LT_EQ=58
    NOT_EQ=59
    COL=60
    COM=61
    L_BRK=62
    R_BRK=63
    L_CBRK=64
    R_CBRK=65
    L_PAR=66
    R_PAR=67
    LT=68
    GT=69
    TIMES=70
    DIVIDE=71
    PLUS=72
    MINUS=73
    QUOTE=74
    IDENTIFIER=75
    FNAME=76
    DECIMAL=77
    INTEGER=78
    DOT=79
    SKIP_=80
    ANY=81

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
            self.state = 125
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 122
                    self.match(RLangParser.NL) 
                self.state = 127
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 128
            self.imports()
            self.state = 129
            self.declarations()
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.NL:
                self.state = 130
                self.match(RLangParser.NL)
                self.state = 135
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
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.IMPORT:
                self.state = 136
                self.import_stat()
                self.state = 138 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 137
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 140 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                self.state = 146
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
            self.state = 147
            self.match(RLangParser.IMPORT)
            self.state = 148
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
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RLangParser.PROPOSITION) | (1 << RLangParser.FEATURE) | (1 << RLangParser.FACTOR) | (1 << RLangParser.GOAL) | (1 << RLangParser.CLASS) | (1 << RLangParser.OBJECT) | (1 << RLangParser.CONSTANT) | (1 << RLangParser.ACTION) | (1 << RLangParser.EFFECT) | (1 << RLangParser.POLICY) | (1 << RLangParser.PLAN) | (1 << RLangParser.OPTION) | (1 << RLangParser.MARKOVFEATURE))) != 0):
                self.state = 150
                self.dec()
                self.state = 155
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


        def plan(self):
            return self.getTypedRuleContext(RLangParser.PlanContext,0)


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
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.CONSTANT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.constant()
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
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                pass
            elif token in [RLangParser.ACTION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.action()
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
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                pass
            elif token in [RLangParser.FACTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 168
                self.factor()
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
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                pass
            elif token in [RLangParser.PROPOSITION]:
                self.enterOuterAlt(localctx, 4)
                self.state = 174
                self.proposition()
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
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                pass
            elif token in [RLangParser.GOAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 180
                self.goal()
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
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                pass
            elif token in [RLangParser.FEATURE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 186
                self.feature()
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
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                pass
            elif token in [RLangParser.MARKOVFEATURE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 192
                self.markov_feature()
                self.state = 194 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 193
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 196 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                pass
            elif token in [RLangParser.OBJECT]:
                self.enterOuterAlt(localctx, 8)
                self.state = 198
                self.object_def()
                self.state = 200 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 199
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 202 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                pass
            elif token in [RLangParser.CLASS]:
                self.enterOuterAlt(localctx, 9)
                self.state = 204
                self.class_def()
                pass
            elif token in [RLangParser.OPTION]:
                self.enterOuterAlt(localctx, 10)
                self.state = 205
                self.option()
                pass
            elif token in [RLangParser.POLICY]:
                self.enterOuterAlt(localctx, 11)
                self.state = 206
                self.policy()
                pass
            elif token in [RLangParser.PLAN]:
                self.enterOuterAlt(localctx, 12)
                self.state = 207
                self.plan()
                pass
            elif token in [RLangParser.EFFECT]:
                self.enterOuterAlt(localctx, 13)
                self.state = 208
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
            self.state = 211
            self.match(RLangParser.CONSTANT)
            self.state = 212
            self.match(RLangParser.IDENTIFIER)
            self.state = 213
            self.match(RLangParser.BIND)
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 214
                self.arithmetic_exp(0)
                pass

            elif la_ == 2:
                self.state = 215
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
            self.state = 218
            self.match(RLangParser.ACTION)
            self.state = 219
            self.match(RLangParser.IDENTIFIER)
            self.state = 220
            self.match(RLangParser.BIND)
            self.state = 223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.MINUS, RLangParser.DECIMAL, RLangParser.INTEGER]:
                self.state = 221
                self.any_number()
                pass
            elif token in [RLangParser.L_BRK]:
                self.state = 222
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
            self.state = 225
            self.match(RLangParser.FACTOR)
            self.state = 226
            self.match(RLangParser.IDENTIFIER)
            self.state = 227
            self.match(RLangParser.BIND)
            self.state = 228
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
            self.state = 230
            self.match(RLangParser.PROPOSITION)
            self.state = 231
            self.match(RLangParser.IDENTIFIER)
            self.state = 232
            self.match(RLangParser.BIND)
            self.state = 233
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
            self.state = 235
            self.match(RLangParser.GOAL)
            self.state = 236
            self.match(RLangParser.IDENTIFIER)
            self.state = 237
            self.match(RLangParser.BIND)
            self.state = 238
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
            self.state = 240
            self.match(RLangParser.FEATURE)
            self.state = 241
            self.match(RLangParser.IDENTIFIER)
            self.state = 242
            self.match(RLangParser.BIND)
            self.state = 243
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
            self.state = 245
            self.match(RLangParser.MARKOVFEATURE)
            self.state = 246
            self.match(RLangParser.IDENTIFIER)
            self.state = 247
            self.match(RLangParser.BIND)
            self.state = 248
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
            self.state = 250
            self.match(RLangParser.OBJECT)
            self.state = 251
            self.match(RLangParser.IDENTIFIER)
            self.state = 252
            self.match(RLangParser.BIND)
            self.state = 253
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
            self.state = 255
            self.match(RLangParser.CLASS)
            self.state = 256
            self.match(RLangParser.IDENTIFIER)
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.L_PAR:
                self.state = 257
                self.match(RLangParser.L_PAR)
                self.state = 258
                self.any_bound_class()
                self.state = 259
                self.match(RLangParser.R_PAR)


            self.state = 263
            self.match(RLangParser.COL)
            self.state = 264
            self.match(RLangParser.INDENT)
            self.state = 265
            self.attribute_definition_collection()
            self.state = 266
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
            self.state = 275 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 268
                localctx._attribute_definition = self.attribute_definition()
                localctx.definitions.append(localctx._attribute_definition)
                self.state = 272
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.NL:
                    self.state = 269
                    self.match(RLangParser.NL)
                    self.state = 274
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 277 
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
            self.state = 279
            self.match(RLangParser.IDENTIFIER)
            self.state = 280
            self.match(RLangParser.COL)
            self.state = 281
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
            self.state = 283
            self.match(RLangParser.OPTION)
            self.state = 284
            self.match(RLangParser.IDENTIFIER)
            self.state = 285
            self.match(RLangParser.COL)
            self.state = 286
            self.match(RLangParser.INDENT)
            self.state = 287
            self.match(RLangParser.INIT)
            self.state = 288
            localctx.init = self.option_condition()
            self.state = 289
            self.match(RLangParser.INDENT)
            self.state = 290
            self.policy_statement()
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
            self.state = 298
            self.match(RLangParser.UNTIL)
            self.state = 299
            localctx.until = self.option_condition()
            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.NL:
                self.state = 300
                self.match(RLangParser.NL)
                self.state = 305
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 306
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
            self.state = 310
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 308
                self.boolean_exp(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
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
            self.state = 312
            self.match(RLangParser.POLICY)
            self.state = 313
            _la = self._input.LA(1)
            if not(_la==RLangParser.MAIN or _la==RLangParser.IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 314
            self.match(RLangParser.COL)
            self.state = 315
            self.match(RLangParser.INDENT)
            self.state = 316
            self.policy_statement()
            self.state = 320
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.NL:
                self.state = 317
                self.match(RLangParser.NL)
                self.state = 322
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 323
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
            self.state = 328
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Policy_statement_executeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.execute()
                pass

            elif la_ == 2:
                localctx = RLangParser.Policy_statement_conditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 326
                self.conditional_subpolicy()
                pass

            elif la_ == 3:
                localctx = RLangParser.Policy_statement_probabilisticContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 327
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
            self.state = 330
            self.match(RLangParser.IF)
            self.state = 331
            localctx.if_condition = self.boolean_exp(0)
            self.state = 332
            self.match(RLangParser.COL)
            self.state = 333
            self.match(RLangParser.INDENT)
            self.state = 334
            localctx.if_subpolicy = self.policy_statement()
            self.state = 338
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.NL:
                self.state = 335
                self.match(RLangParser.NL)
                self.state = 340
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 341
            self.match(RLangParser.DEDENT)
            self.state = 357
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.ELIF:
                self.state = 342
                self.match(RLangParser.ELIF)
                self.state = 343
                localctx._boolean_exp = self.boolean_exp(0)
                localctx.elif_conditions.append(localctx._boolean_exp)
                self.state = 344
                self.match(RLangParser.COL)
                self.state = 345
                self.match(RLangParser.INDENT)
                self.state = 346
                localctx._policy_statement = self.policy_statement()
                localctx.elif_subpolicies.append(localctx._policy_statement)
                self.state = 350
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.NL:
                    self.state = 347
                    self.match(RLangParser.NL)
                    self.state = 352
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 353
                self.match(RLangParser.DEDENT)
                self.state = 359
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 372
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.ELSE:
                self.state = 360
                self.match(RLangParser.ELSE)
                self.state = 361
                self.match(RLangParser.COL)
                self.state = 362
                self.match(RLangParser.INDENT)
                self.state = 363
                localctx.else_subpolicy = self.policy_statement()
                self.state = 367
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.NL:
                    self.state = 364
                    self.match(RLangParser.NL)
                    self.state = 369
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 370
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
            self.state = 374
            localctx._probabilistic_policy_statement = self.probabilistic_policy_statement()
            localctx.subpolicies.append(localctx._probabilistic_policy_statement)
            self.state = 379
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.OR:
                self.state = 375
                self.match(RLangParser.OR)
                self.state = 376
                localctx._probabilistic_policy_statement = self.probabilistic_policy_statement()
                localctx.subpolicies.append(localctx._probabilistic_policy_statement)
                self.state = 381
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
            self.state = 401
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.WITH]:
                localctx = RLangParser.Probabilistic_policy_statement_no_sugarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.probabilistic_condition()
                self.state = 383
                self.match(RLangParser.COL)
                self.state = 384
                self.match(RLangParser.INDENT)
                self.state = 385
                self.policy_statement()
                self.state = 389
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.NL:
                    self.state = 386
                    self.match(RLangParser.NL)
                    self.state = 391
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 392
                self.match(RLangParser.DEDENT)
                pass
            elif token in [RLangParser.EXECUTE]:
                localctx = RLangParser.Probabilistic_policy_statement_sugarContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                self.execute()
                self.state = 395
                self.probabilistic_condition()
                self.state = 397 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 396
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 399 
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
            self.state = 403
            self.match(RLangParser.EXECUTE)
            self.state = 406
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 404
                self.match(RLangParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 405
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
            self.state = 408
            self.match(RLangParser.IDENTIFIER)
            self.state = 409
            self.match(RLangParser.L_PAR)
            self.state = 418
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 27)) & ~0x3f) == 0 and ((1 << (_la - 27)) & ((1 << (RLangParser.S_PRIME - 27)) | (1 << (RLangParser.S - 27)) | (1 << (RLangParser.A - 27)) | (1 << (RLangParser.ANY_CONDITION - 27)) | (1 << (RLangParser.ALL_CONDITION - 27)) | (1 << (RLangParser.L_BRK - 27)) | (1 << (RLangParser.L_PAR - 27)) | (1 << (RLangParser.MINUS - 27)) | (1 << (RLangParser.IDENTIFIER - 27)) | (1 << (RLangParser.DECIMAL - 27)) | (1 << (RLangParser.INTEGER - 27)))) != 0):
                self.state = 410
                localctx._arithmetic_exp = self.arithmetic_exp(0)
                localctx.arr.append(localctx._arithmetic_exp)
                self.state = 415
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.COM:
                    self.state = 411
                    self.match(RLangParser.COM)
                    self.state = 412
                    localctx._arithmetic_exp = self.arithmetic_exp(0)
                    localctx.arr.append(localctx._arithmetic_exp)
                    self.state = 417
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 420
            self.match(RLangParser.R_PAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PlanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLAN(self):
            return self.getToken(RLangParser.PLAN, 0)

        def COL(self):
            return self.getToken(RLangParser.COL, 0)

        def INDENT(self):
            return self.getToken(RLangParser.INDENT, 0)

        def plan_statement_collection(self):
            return self.getTypedRuleContext(RLangParser.Plan_statement_collectionContext,0)


        def DEDENT(self):
            return self.getToken(RLangParser.DEDENT, 0)

        def IDENTIFIER(self):
            return self.getToken(RLangParser.IDENTIFIER, 0)

        def MAIN(self):
            return self.getToken(RLangParser.MAIN, 0)

        def getRuleIndex(self):
            return RLangParser.RULE_plan

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlan" ):
                listener.enterPlan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlan" ):
                listener.exitPlan(self)




    def plan(self):

        localctx = RLangParser.PlanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_plan)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(RLangParser.PLAN)
            self.state = 423
            _la = self._input.LA(1)
            if not(_la==RLangParser.MAIN or _la==RLangParser.IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 424
            self.match(RLangParser.COL)
            self.state = 425
            self.match(RLangParser.INDENT)
            self.state = 426
            self.plan_statement_collection()
            self.state = 427
            self.match(RLangParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Plan_statement_collectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._plan_statement = None # Plan_statementContext
            self.statements = list() # of Plan_statementContexts

        def plan_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Plan_statementContext)
            else:
                return self.getTypedRuleContext(RLangParser.Plan_statementContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.NL)
            else:
                return self.getToken(RLangParser.NL, i)

        def getRuleIndex(self):
            return RLangParser.RULE_plan_statement_collection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlan_statement_collection" ):
                listener.enterPlan_statement_collection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlan_statement_collection" ):
                listener.exitPlan_statement_collection(self)




    def plan_statement_collection(self):

        localctx = RLangParser.Plan_statement_collectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_plan_statement_collection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 429
                localctx._plan_statement = self.plan_statement()
                localctx.statements.append(localctx._plan_statement)
                self.state = 433
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.NL:
                    self.state = 430
                    self.match(RLangParser.NL)
                    self.state = 435
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 438 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RLangParser.EXECUTE) | (1 << RLangParser.IF) | (1 << RLangParser.WITH))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Plan_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RLangParser.RULE_plan_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Plan_statement_executeContext(Plan_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Plan_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def execute(self):
            return self.getTypedRuleContext(RLangParser.ExecuteContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlan_statement_execute" ):
                listener.enterPlan_statement_execute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlan_statement_execute" ):
                listener.exitPlan_statement_execute(self)


    class Plan_statement_probabilisticContext(Plan_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Plan_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def probabilistic_plan(self):
            return self.getTypedRuleContext(RLangParser.Probabilistic_planContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlan_statement_probabilistic" ):
                listener.enterPlan_statement_probabilistic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlan_statement_probabilistic" ):
                listener.exitPlan_statement_probabilistic(self)


    class Plan_statement_conditionalContext(Plan_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Plan_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def conditional_plan(self):
            return self.getTypedRuleContext(RLangParser.Conditional_planContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlan_statement_conditional" ):
                listener.enterPlan_statement_conditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlan_statement_conditional" ):
                listener.exitPlan_statement_conditional(self)



    def plan_statement(self):

        localctx = RLangParser.Plan_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_plan_statement)
        try:
            self.state = 443
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Plan_statement_executeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 440
                self.execute()
                pass

            elif la_ == 2:
                localctx = RLangParser.Plan_statement_conditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 441
                self.conditional_plan()
                pass

            elif la_ == 3:
                localctx = RLangParser.Plan_statement_probabilisticContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 442
                self.probabilistic_plan()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conditional_planContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.if_condition = None # Boolean_expContext
            self.if_plan = None # Plan_statement_collectionContext
            self._boolean_exp = None # Boolean_expContext
            self.elif_conditions = list() # of Boolean_expContexts
            self._plan_statement_collection = None # Plan_statement_collectionContext
            self.elif_plans = list() # of Plan_statement_collectionContexts
            self.else_plan = None # Plan_statement_collectionContext

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


        def plan_statement_collection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Plan_statement_collectionContext)
            else:
                return self.getTypedRuleContext(RLangParser.Plan_statement_collectionContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.ELIF)
            else:
                return self.getToken(RLangParser.ELIF, i)

        def ELSE(self):
            return self.getToken(RLangParser.ELSE, 0)

        def getRuleIndex(self):
            return RLangParser.RULE_conditional_plan

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional_plan" ):
                listener.enterConditional_plan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional_plan" ):
                listener.exitConditional_plan(self)




    def conditional_plan(self):

        localctx = RLangParser.Conditional_planContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_conditional_plan)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.match(RLangParser.IF)
            self.state = 446
            localctx.if_condition = self.boolean_exp(0)
            self.state = 447
            self.match(RLangParser.COL)
            self.state = 448
            self.match(RLangParser.INDENT)
            self.state = 449
            localctx.if_plan = self.plan_statement_collection()
            self.state = 450
            self.match(RLangParser.DEDENT)
            self.state = 460
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.ELIF:
                self.state = 451
                self.match(RLangParser.ELIF)
                self.state = 452
                localctx._boolean_exp = self.boolean_exp(0)
                localctx.elif_conditions.append(localctx._boolean_exp)
                self.state = 453
                self.match(RLangParser.COL)
                self.state = 454
                self.match(RLangParser.INDENT)
                self.state = 455
                localctx._plan_statement_collection = self.plan_statement_collection()
                localctx.elif_plans.append(localctx._plan_statement_collection)
                self.state = 456
                self.match(RLangParser.DEDENT)
                self.state = 462
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 469
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.ELSE:
                self.state = 463
                self.match(RLangParser.ELSE)
                self.state = 464
                self.match(RLangParser.COL)
                self.state = 465
                self.match(RLangParser.INDENT)
                self.state = 466
                localctx.else_plan = self.plan_statement_collection()
                self.state = 467
                self.match(RLangParser.DEDENT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Probabilistic_planContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._probabilistic_plan_statement = None # Probabilistic_plan_statementContext
            self.plans = list() # of Probabilistic_plan_statementContexts

        def probabilistic_plan_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RLangParser.Probabilistic_plan_statementContext)
            else:
                return self.getTypedRuleContext(RLangParser.Probabilistic_plan_statementContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(RLangParser.OR)
            else:
                return self.getToken(RLangParser.OR, i)

        def getRuleIndex(self):
            return RLangParser.RULE_probabilistic_plan

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProbabilistic_plan" ):
                listener.enterProbabilistic_plan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProbabilistic_plan" ):
                listener.exitProbabilistic_plan(self)




    def probabilistic_plan(self):

        localctx = RLangParser.Probabilistic_planContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_probabilistic_plan)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            localctx._probabilistic_plan_statement = self.probabilistic_plan_statement()
            localctx.plans.append(localctx._probabilistic_plan_statement)
            self.state = 476
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.OR:
                self.state = 472
                self.match(RLangParser.OR)
                self.state = 473
                localctx._probabilistic_plan_statement = self.probabilistic_plan_statement()
                localctx.plans.append(localctx._probabilistic_plan_statement)
                self.state = 478
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Probabilistic_plan_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RLangParser.RULE_probabilistic_plan_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Probabilistic_plan_statement_sugarContext(Probabilistic_plan_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Probabilistic_plan_statementContext
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
            if hasattr( listener, "enterProbabilistic_plan_statement_sugar" ):
                listener.enterProbabilistic_plan_statement_sugar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProbabilistic_plan_statement_sugar" ):
                listener.exitProbabilistic_plan_statement_sugar(self)


    class Probabilistic_plan_statement_no_sugarContext(Probabilistic_plan_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Probabilistic_plan_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def probabilistic_condition(self):
            return self.getTypedRuleContext(RLangParser.Probabilistic_conditionContext,0)

        def COL(self):
            return self.getToken(RLangParser.COL, 0)
        def INDENT(self):
            return self.getToken(RLangParser.INDENT, 0)
        def plan_statement_collection(self):
            return self.getTypedRuleContext(RLangParser.Plan_statement_collectionContext,0)

        def DEDENT(self):
            return self.getToken(RLangParser.DEDENT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProbabilistic_plan_statement_no_sugar" ):
                listener.enterProbabilistic_plan_statement_no_sugar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProbabilistic_plan_statement_no_sugar" ):
                listener.exitProbabilistic_plan_statement_no_sugar(self)



    def probabilistic_plan_statement(self):

        localctx = RLangParser.Probabilistic_plan_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_probabilistic_plan_statement)
        try:
            self.state = 492
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.WITH]:
                localctx = RLangParser.Probabilistic_plan_statement_no_sugarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 479
                self.probabilistic_condition()
                self.state = 480
                self.match(RLangParser.COL)
                self.state = 481
                self.match(RLangParser.INDENT)
                self.state = 482
                self.plan_statement_collection()
                self.state = 483
                self.match(RLangParser.DEDENT)
                pass
            elif token in [RLangParser.EXECUTE]:
                localctx = RLangParser.Probabilistic_plan_statement_sugarContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 485
                self.execute()
                self.state = 486
                self.probabilistic_condition()
                self.state = 488 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 487
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 490 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

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
        self.enterRule(localctx, 62, self.RULE_effect)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self.match(RLangParser.EFFECT)
            self.state = 495
            _la = self._input.LA(1)
            if not(_la==RLangParser.MAIN or _la==RLangParser.IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 496
            self.match(RLangParser.COL)
            self.state = 497
            self.match(RLangParser.INDENT)
            self.state = 498
            self.effect_statement_collection()
            self.state = 499
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
        self.enterRule(localctx, 64, self.RULE_effect_statement_collection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 501
                localctx._effect_statement = self.effect_statement()
                localctx.statements.append(localctx._effect_statement)
                self.state = 505
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.NL:
                    self.state = 502
                    self.match(RLangParser.NL)
                    self.state = 507
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 510 
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
        self.enterRule(localctx, 66, self.RULE_effect_statement)
        try:
            self.state = 517
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Effect_statement_rewardContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 512
                self.reward()
                pass

            elif la_ == 2:
                localctx = RLangParser.Effect_statement_predictionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 513
                self.prediction()
                pass

            elif la_ == 3:
                localctx = RLangParser.Effect_statement_referenceContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 514
                self.effect_reference()
                pass

            elif la_ == 4:
                localctx = RLangParser.Effect_statement_conditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 515
                self.conditional_effect()
                pass

            elif la_ == 5:
                localctx = RLangParser.Effect_statement_probabilisticContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 516
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
        self.enterRule(localctx, 68, self.RULE_conditional_effect)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            self.match(RLangParser.IF)
            self.state = 520
            localctx.if_condition = self.boolean_exp(0)
            self.state = 521
            self.match(RLangParser.COL)
            self.state = 522
            self.match(RLangParser.INDENT)
            self.state = 523
            localctx.if_effect = self.effect_statement_collection()
            self.state = 524
            self.match(RLangParser.DEDENT)
            self.state = 534
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.ELIF:
                self.state = 525
                self.match(RLangParser.ELIF)
                self.state = 526
                localctx._boolean_exp = self.boolean_exp(0)
                localctx.elif_conditions.append(localctx._boolean_exp)
                self.state = 527
                self.match(RLangParser.COL)
                self.state = 528
                self.match(RLangParser.INDENT)
                self.state = 529
                localctx._effect_statement_collection = self.effect_statement_collection()
                localctx.elif_effects.append(localctx._effect_statement_collection)
                self.state = 530
                self.match(RLangParser.DEDENT)
                self.state = 536
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 543
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.ELSE:
                self.state = 537
                self.match(RLangParser.ELSE)
                self.state = 538
                self.match(RLangParser.COL)
                self.state = 539
                self.match(RLangParser.INDENT)
                self.state = 540
                localctx.else_effect = self.effect_statement_collection()
                self.state = 541
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
        self.enterRule(localctx, 70, self.RULE_probabilistic_effect)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
            localctx._probabilistic_effect_statement = self.probabilistic_effect_statement()
            localctx.effects.append(localctx._probabilistic_effect_statement)
            self.state = 550
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.OR:
                self.state = 546
                self.match(RLangParser.OR)
                self.state = 547
                localctx._probabilistic_effect_statement = self.probabilistic_effect_statement()
                localctx.effects.append(localctx._probabilistic_effect_statement)
                self.state = 552
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
        self.enterRule(localctx, 72, self.RULE_probabilistic_effect_statement)
        try:
            self.state = 570
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.WITH]:
                localctx = RLangParser.Probabilistic_effect_statement_no_sugarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 553
                self.probabilistic_condition()
                self.state = 554
                self.match(RLangParser.COL)
                self.state = 555
                self.match(RLangParser.INDENT)
                self.state = 556
                self.effect_statement_collection()
                self.state = 557
                self.match(RLangParser.DEDENT)
                pass
            elif token in [RLangParser.REWARD, RLangParser.S_PRIME, RLangParser.PREDICT, RLangParser.IDENTIFIER]:
                localctx = RLangParser.Probabilistic_effect_statement_sugarContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 562
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RLangParser.REWARD]:
                    self.state = 559
                    self.reward()
                    pass
                elif token in [RLangParser.S_PRIME, RLangParser.IDENTIFIER]:
                    self.state = 560
                    self.prediction()
                    pass
                elif token in [RLangParser.PREDICT]:
                    self.state = 561
                    self.effect_reference()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 564
                self.probabilistic_condition()
                self.state = 566 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 565
                        self.match(RLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 568 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

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
        self.enterRule(localctx, 74, self.RULE_reward)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 572
            self.match(RLangParser.REWARD)
            self.state = 573
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
        self.enterRule(localctx, 76, self.RULE_prediction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 586
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.S_PRIME]:
                self.state = 575
                self.match(RLangParser.S_PRIME)
                self.state = 577
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==RLangParser.DOT:
                    self.state = 576
                    self.dot_exp()


                pass
            elif token in [RLangParser.IDENTIFIER]:
                self.state = 579
                self.match(RLangParser.IDENTIFIER)
                self.state = 581
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==RLangParser.DOT:
                    self.state = 580
                    self.dot_exp()


                self.state = 584
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==RLangParser.PRIME:
                    self.state = 583
                    self.match(RLangParser.PRIME)


                pass
            else:
                raise NoViableAltException(self)

            self.state = 588
            self.match(RLangParser.PREDICT)
            self.state = 592
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.state = 589
                self.arithmetic_exp(0)
                pass

            elif la_ == 2:
                self.state = 590
                self.boolean_exp(0)
                pass

            elif la_ == 3:
                self.state = 591
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
        self.enterRule(localctx, 78, self.RULE_effect_reference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 594
            self.match(RLangParser.PREDICT)
            self.state = 595
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
        self.enterRule(localctx, 80, self.RULE_probabilistic_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 597
            self.match(RLangParser.WITH)
            self.state = 598
            self.match(RLangParser.P)
            self.state = 599
            self.match(RLangParser.L_PAR)
            self.state = 602
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                self.state = 600
                self.any_number()
                pass

            elif la_ == 2:
                self.state = 601
                self.integer_fraction()
                pass


            self.state = 604
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


    class Arith_quantificationContext(Arithmetic_expContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RLangParser.Arithmetic_expContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def quantification_exp(self):
            return self.getTypedRuleContext(RLangParser.Quantification_expContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArith_quantification" ):
                listener.enterArith_quantification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArith_quantification" ):
                listener.exitArith_quantification(self)


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
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_arithmetic_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 615
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.L_PAR]:
                localctx = RLangParser.Arith_parenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 607
                self.match(RLangParser.L_PAR)
                self.state = 608
                self.arithmetic_exp(0)
                self.state = 609
                self.match(RLangParser.R_PAR)
                pass
            elif token in [RLangParser.MINUS, RLangParser.DECIMAL, RLangParser.INTEGER]:
                localctx = RLangParser.Arith_numberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 611
                self.any_number()
                pass
            elif token in [RLangParser.L_BRK]:
                localctx = RLangParser.Arith_arrayContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 612
                self.any_array()
                pass
            elif token in [RLangParser.S_PRIME, RLangParser.S, RLangParser.A, RLangParser.IDENTIFIER]:
                localctx = RLangParser.Arith_bound_varContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 613
                self.any_bound_var()
                pass
            elif token in [RLangParser.ANY_CONDITION, RLangParser.ALL_CONDITION]:
                localctx = RLangParser.Arith_quantificationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 614
                self.quantification_exp()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 625
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,61,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 623
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
                    if la_ == 1:
                        localctx = RLangParser.Arith_times_divideContext(self, RLangParser.Arithmetic_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_exp)
                        self.state = 617
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 618
                        _la = self._input.LA(1)
                        if not(_la==RLangParser.TIMES or _la==RLangParser.DIVIDE):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 619
                        localctx.rhs = self.arithmetic_exp(7)
                        pass

                    elif la_ == 2:
                        localctx = RLangParser.Arith_plus_minusContext(self, RLangParser.Arithmetic_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_exp)
                        self.state = 620
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 621
                        _la = self._input.LA(1)
                        if not(_la==RLangParser.PLUS or _la==RLangParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 622
                        localctx.rhs = self.arithmetic_exp(6)
                        pass

             
                self.state = 627
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,61,self._ctx)

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
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_boolean_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 645
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Bool_parenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 629
                self.match(RLangParser.L_PAR)
                self.state = 630
                self.boolean_exp(0)
                self.state = 631
                self.match(RLangParser.R_PAR)
                pass

            elif la_ == 2:
                localctx = RLangParser.Bool_notContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 633
                self.match(RLangParser.NOT)
                self.state = 634
                self.boolean_exp(6)
                pass

            elif la_ == 3:
                localctx = RLangParser.Bool_inContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 635
                localctx.lhs = self.arithmetic_exp(0)
                self.state = 636
                self.match(RLangParser.IN)
                self.state = 637
                localctx.rhs = self.arithmetic_exp(0)
                pass

            elif la_ == 4:
                localctx = RLangParser.Bool_arith_eqContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 639
                localctx.lhs = self.arithmetic_exp(0)
                self.state = 640
                _la = self._input.LA(1)
                if not(((((_la - 56)) & ~0x3f) == 0 and ((1 << (_la - 56)) & ((1 << (RLangParser.EQ_TO - 56)) | (1 << (RLangParser.GT_EQ - 56)) | (1 << (RLangParser.LT_EQ - 56)) | (1 << (RLangParser.NOT_EQ - 56)) | (1 << (RLangParser.LT - 56)) | (1 << (RLangParser.GT - 56)))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 641
                localctx.rhs = self.arithmetic_exp(0)
                pass

            elif la_ == 5:
                localctx = RLangParser.Bool_bound_varContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 643
                self.any_bound_var()
                pass

            elif la_ == 6:
                localctx = RLangParser.Bool_tfContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 644
                _la = self._input.LA(1)
                if not(_la==RLangParser.TRUE or _la==RLangParser.FALSE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 658
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,64,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 656
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
                    if la_ == 1:
                        localctx = RLangParser.Bool_andContext(self, RLangParser.Boolean_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_exp)
                        self.state = 647
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 648
                        self.match(RLangParser.AND)
                        self.state = 649
                        localctx.rhs = self.boolean_exp(9)
                        pass

                    elif la_ == 2:
                        localctx = RLangParser.Bool_orContext(self, RLangParser.Boolean_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_exp)
                        self.state = 650
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 651
                        self.match(RLangParser.OR)
                        self.state = 652
                        localctx.rhs = self.boolean_exp(8)
                        pass

                    elif la_ == 3:
                        localctx = RLangParser.Bool_bool_eqContext(self, RLangParser.Boolean_expContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_exp)
                        self.state = 653
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 654
                        _la = self._input.LA(1)
                        if not(_la==RLangParser.EQ_TO or _la==RLangParser.NOT_EQ):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 655
                        localctx.rhs = self.boolean_exp(5)
                        pass

             
                self.state = 660
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,64,self._ctx)

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
        self.enterRule(localctx, 86, self.RULE_quantification_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 661
            self.quantifier()
            self.state = 662
            self.match(RLangParser.L_PAR)
            self.state = 663
            self.any_bound_class()
            self.state = 664
            self.match(RLangParser.R_PAR)
            self.state = 666
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                self.state = 665
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
        self.enterRule(localctx, 88, self.RULE_quantifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 668
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
        self.enterRule(localctx, 90, self.RULE_type_def)
        try:
            self.state = 672
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.LIST, RLangParser.SET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 670
                self.compound_type()
                pass
            elif token in [RLangParser.INT, RLangParser.FLOAT, RLangParser.STR, RLangParser.BOOL, RLangParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 671
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
        self.enterRule(localctx, 92, self.RULE_compound_type)
        self._la = 0 # Token type
        try:
            self.state = 694
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.LIST]:
                localctx = RLangParser.Type_listContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 674
                self.match(RLangParser.LIST)
                self.state = 682
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==RLangParser.L_BRK:
                    self.state = 675
                    self.match(RLangParser.L_BRK)
                    self.state = 678
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [RLangParser.INT, RLangParser.FLOAT, RLangParser.STR, RLangParser.BOOL, RLangParser.IDENTIFIER]:
                        self.state = 676
                        self.simple_type()
                        pass
                    elif token in [RLangParser.LIST, RLangParser.SET]:
                        self.state = 677
                        self.compound_type()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 680
                    self.match(RLangParser.R_BRK)


                pass
            elif token in [RLangParser.SET]:
                localctx = RLangParser.Type_setContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 684
                self.match(RLangParser.SET)
                self.state = 692
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==RLangParser.L_BRK:
                    self.state = 685
                    self.match(RLangParser.L_BRK)
                    self.state = 688
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [RLangParser.INT, RLangParser.FLOAT, RLangParser.STR, RLangParser.BOOL, RLangParser.IDENTIFIER]:
                        self.state = 686
                        self.simple_type()
                        pass
                    elif token in [RLangParser.LIST, RLangParser.SET]:
                        self.state = 687
                        self.compound_type()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 690
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
        self.enterRule(localctx, 94, self.RULE_simple_type)
        try:
            self.state = 701
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RLangParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 696
                self.match(RLangParser.INT)
                pass
            elif token in [RLangParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 697
                self.match(RLangParser.FLOAT)
                pass
            elif token in [RLangParser.STR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 698
                self.match(RLangParser.STR)
                pass
            elif token in [RLangParser.BOOL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 699
                self.match(RLangParser.BOOL)
                pass
            elif token in [RLangParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 5)
                self.state = 700
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
        self.enterRule(localctx, 96, self.RULE_any_bound_var)
        try:
            self.state = 723
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,77,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Bound_stateContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 703
                self.match(RLangParser.S)
                self.state = 705
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,73,self._ctx)
                if la_ == 1:
                    self.state = 704
                    self.trailer()


                pass

            elif la_ == 2:
                localctx = RLangParser.Bound_next_stateContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 707
                self.match(RLangParser.S_PRIME)
                self.state = 709
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,74,self._ctx)
                if la_ == 1:
                    self.state = 708
                    self.trailer()


                pass

            elif la_ == 3:
                localctx = RLangParser.Bound_identifierContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 711
                self.match(RLangParser.IDENTIFIER)
                self.state = 713
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
                if la_ == 1:
                    self.state = 712
                    self.match(RLangParser.PRIME)


                self.state = 718
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,76,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 715
                        self.trailer() 
                    self.state = 720
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,76,self._ctx)

                pass

            elif la_ == 4:
                localctx = RLangParser.Bound_actionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 721
                self.match(RLangParser.A)
                pass

            elif la_ == 5:
                localctx = RLangParser.Bound_lifted_executionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 722
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
        self.enterRule(localctx, 98, self.RULE_any_bound_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 725
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
        self.enterRule(localctx, 100, self.RULE_trailer)
        try:
            self.state = 730
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,78,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Trailer_arrayContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 727
                self.int_array_exp()
                pass

            elif la_ == 2:
                localctx = RLangParser.Trailer_sliceContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 728
                self.slice_exp()
                pass

            elif la_ == 3:
                localctx = RLangParser.Trailer_objectContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 729
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
        self.enterRule(localctx, 102, self.RULE_dot_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 734 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 732
                    self.match(RLangParser.DOT)
                    self.state = 733
                    localctx._IDENTIFIER = self.match(RLangParser.IDENTIFIER)
                    localctx.attr.append(localctx._IDENTIFIER)

                else:
                    raise NoViableAltException(self)
                self.state = 736 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,79,self._ctx)

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
        self.enterRule(localctx, 104, self.RULE_any_array)
        try:
            self.state = 740
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Any_array_compoundContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 738
                self.compound_array_exp()
                pass

            elif la_ == 2:
                localctx = RLangParser.Any_array_any_numContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 739
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
        self.enterRule(localctx, 106, self.RULE_compound_array_exp)
        self._la = 0 # Token type
        try:
            self.state = 765
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,83,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Compound_array_simpleContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 742
                self.any_num_array_exp()
                pass

            elif la_ == 2:
                localctx = RLangParser.Compound_array_arithContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 743
                self.match(RLangParser.L_BRK)
                self.state = 744
                localctx._arithmetic_exp = self.arithmetic_exp(0)
                localctx.arr.append(localctx._arithmetic_exp)
                self.state = 749
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.COM:
                    self.state = 745
                    self.match(RLangParser.COM)
                    self.state = 746
                    localctx._arithmetic_exp = self.arithmetic_exp(0)
                    localctx.arr.append(localctx._arithmetic_exp)
                    self.state = 751
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 752
                self.match(RLangParser.R_BRK)
                pass

            elif la_ == 3:
                localctx = RLangParser.Compound_array_compoundContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 754
                self.match(RLangParser.L_BRK)
                self.state = 755
                localctx._compound_array_exp = self.compound_array_exp()
                localctx.arr.append(localctx._compound_array_exp)
                self.state = 760
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==RLangParser.COM:
                    self.state = 756
                    self.match(RLangParser.COM)
                    self.state = 757
                    localctx._compound_array_exp = self.compound_array_exp()
                    localctx.arr.append(localctx._compound_array_exp)
                    self.state = 762
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 763
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
        self.enterRule(localctx, 108, self.RULE_int_array_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 767
            self.match(RLangParser.L_BRK)
            self.state = 768
            localctx._any_integer = self.any_integer()
            localctx.arr.append(localctx._any_integer)
            self.state = 773
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.COM:
                self.state = 769
                self.match(RLangParser.COM)
                self.state = 770
                localctx._any_integer = self.any_integer()
                localctx.arr.append(localctx._any_integer)
                self.state = 775
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 776
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
        self.enterRule(localctx, 110, self.RULE_any_num_array_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 778
            self.match(RLangParser.L_BRK)
            self.state = 779
            localctx._any_number = self.any_number()
            localctx.arr.append(localctx._any_number)
            self.state = 784
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RLangParser.COM:
                self.state = 780
                self.match(RLangParser.COM)
                self.state = 781
                localctx._any_number = self.any_number()
                localctx.arr.append(localctx._any_number)
                self.state = 786
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 787
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
        self.enterRule(localctx, 112, self.RULE_slice_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 789
            self.match(RLangParser.L_BRK)
            self.state = 791
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.MINUS or _la==RLangParser.INTEGER:
                self.state = 790
                localctx.start_ind = self.any_integer()


            self.state = 793
            self.match(RLangParser.COL)
            self.state = 795
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.MINUS or _la==RLangParser.INTEGER:
                self.state = 794
                localctx.stop_ind = self.any_integer()


            self.state = 797
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
        self.enterRule(localctx, 114, self.RULE_integer_fraction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 799
            localctx.lhs = self.any_integer()
            self.state = 800
            self.match(RLangParser.DIVIDE)
            self.state = 801
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
        self.enterRule(localctx, 116, self.RULE_any_number)
        try:
            self.state = 805
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,88,self._ctx)
            if la_ == 1:
                localctx = RLangParser.Any_num_intContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 803
                self.any_integer()
                pass

            elif la_ == 2:
                localctx = RLangParser.Any_num_decContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 804
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
        self.enterRule(localctx, 118, self.RULE_any_integer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 808
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.MINUS:
                self.state = 807
                self.match(RLangParser.MINUS)


            self.state = 810
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
        self.enterRule(localctx, 120, self.RULE_any_decimal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 813
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RLangParser.MINUS:
                self.state = 812
                self.match(RLangParser.MINUS)


            self.state = 815
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
        self._predicates[41] = self.arithmetic_exp_sempred
        self._predicates[42] = self.boolean_exp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def arithmetic_exp_sempred(self, localctx:Arithmetic_expContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

    def boolean_exp_sempred(self, localctx:Boolean_expContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         




