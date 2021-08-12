# Generated from RLangLexer.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from antlr_denter.DenterHelper import DenterHelper
from .RLangParser import RLangParser



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<")
        buf.write("\u01a4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\3\2\5\2\177\n\2\3\2\3\2\7\2\u0083")
        buf.write("\n\2\f\2\16\2\u0086\13\2\3\2\5\2\u0089\n\2\3\2\3\2\7\2")
        buf.write("\u008d\n\2\f\2\16\2\u0090\13\2\5\2\u0092\n\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3")
        buf.write("\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'")
        buf.write("\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60")
        buf.write("\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\64\7\64")
        buf.write("\u016b\n\64\f\64\16\64\u016e\13\64\3\65\3\65\7\65\u0172")
        buf.write("\n\65\f\65\16\65\u0175\13\65\3\66\6\66\u0178\n\66\r\66")
        buf.write("\16\66\u0179\3\66\3\66\6\66\u017e\n\66\r\66\16\66\u017f")
        buf.write("\3\67\6\67\u0183\n\67\r\67\16\67\u0184\38\58\u0188\n8")
        buf.write("\39\39\39\59\u018d\n9\3:\3:\3;\6;\u0192\n;\r;\16;\u0193")
        buf.write("\3<\3<\7<\u0198\n<\f<\16<\u019b\13<\3=\3=\5=\u019f\n=")
        buf.write("\3=\3=\3>\3>\2\2?\3\5\5\6\7\7\t\b\13\t\r\n\17\13\21\f")
        buf.write("\23\r\25\16\27\17\31\20\33\21\35\22\37\23!\24#\25%\26")
        buf.write("\'\27)\30+\31-\32/\33\61\34\63\35\65\36\67\379 ;!=\"?")
        buf.write("#A$C%E&G\'I(K)M*O+Q,S-U.W/Y\60[\61]\62_\63a\64c\65e\66")
        buf.write("g\67i8k9m:o\2q\2s\2u\2w\2y;{<\3\2\6\4\2C\\c|\3\2\62;\4")
        buf.write("\2\13\13\"\"\4\2\f\f\16\17\2\u01ad\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a")
        buf.write("\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2")
        buf.write("k\3\2\2\2\2m\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\3\u0091\3\2")
        buf.write("\2\2\5\u0093\3\2\2\2\7\u009d\3\2\2\2\t\u00a5\3\2\2\2\13")
        buf.write("\u00ac\3\2\2\2\r\u00b1\3\2\2\2\17\u00ba\3\2\2\2\21\u00c1")
        buf.write("\3\2\2\2\23\u00c8\3\2\2\2\25\u00cf\3\2\2\2\27\u00d6\3")
        buf.write("\2\2\2\31\u00de\3\2\2\2\33\u00e5\3\2\2\2\35\u00f3\3\2")
        buf.write("\2\2\37\u00fa\3\2\2\2!\u00fd\3\2\2\2#\u00ff\3\2\2\2%\u0101")
        buf.write("\3\2\2\2\'\u0104\3\2\2\2)\u0109\3\2\2\2+\u010e\3\2\2\2")
        buf.write("-\u0111\3\2\2\2/\u0116\3\2\2\2\61\u011c\3\2\2\2\63\u0120")
        buf.write("\3\2\2\2\65\u0123\3\2\2\2\67\u0127\3\2\2\29\u012c\3\2")
        buf.write("\2\2;\u0132\3\2\2\2=\u0135\3\2\2\2?\u0137\3\2\2\2A\u013a")
        buf.write("\3\2\2\2C\u013d\3\2\2\2E\u0140\3\2\2\2G\u0143\3\2\2\2")
        buf.write("I\u0146\3\2\2\2K\u0149\3\2\2\2M\u014c\3\2\2\2O\u014f\3")
        buf.write("\2\2\2Q\u0151\3\2\2\2S\u0153\3\2\2\2U\u0155\3\2\2\2W\u0157")
        buf.write("\3\2\2\2Y\u0159\3\2\2\2[\u015b\3\2\2\2]\u015d\3\2\2\2")
        buf.write("_\u015f\3\2\2\2a\u0161\3\2\2\2c\u0163\3\2\2\2e\u0165\3")
        buf.write("\2\2\2g\u0167\3\2\2\2i\u016f\3\2\2\2k\u0177\3\2\2\2m\u0182")
        buf.write("\3\2\2\2o\u0187\3\2\2\2q\u018c\3\2\2\2s\u018e\3\2\2\2")
        buf.write("u\u0191\3\2\2\2w\u0195\3\2\2\2y\u019e\3\2\2\2{\u01a2\3")
        buf.write("\2\2\2}\177\7\17\2\2~}\3\2\2\2~\177\3\2\2\2\177\u0080")
        buf.write("\3\2\2\2\u0080\u0084\7\f\2\2\u0081\u0083\7\"\2\2\u0082")
        buf.write("\u0081\3\2\2\2\u0083\u0086\3\2\2\2\u0084\u0082\3\2\2\2")
        buf.write("\u0084\u0085\3\2\2\2\u0085\u0092\3\2\2\2\u0086\u0084\3")
        buf.write("\2\2\2\u0087\u0089\7\17\2\2\u0088\u0087\3\2\2\2\u0088")
        buf.write("\u0089\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u008e\7\f\2\2")
        buf.write("\u008b\u008d\7\13\2\2\u008c\u008b\3\2\2\2\u008d\u0090")
        buf.write("\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f")
        buf.write("\u0092\3\2\2\2\u0090\u008e\3\2\2\2\u0091~\3\2\2\2\u0091")
        buf.write("\u0088\3\2\2\2\u0092\4\3\2\2\2\u0093\u0094\7R\2\2\u0094")
        buf.write("\u0095\7t\2\2\u0095\u0096\7g\2\2\u0096\u0097\7f\2\2\u0097")
        buf.write("\u0098\7k\2\2\u0098\u0099\7e\2\2\u0099\u009a\7c\2\2\u009a")
        buf.write("\u009b\7v\2\2\u009b\u009c\7g\2\2\u009c\6\3\2\2\2\u009d")
        buf.write("\u009e\7H\2\2\u009e\u009f\7g\2\2\u009f\u00a0\7c\2\2\u00a0")
        buf.write("\u00a1\7v\2\2\u00a1\u00a2\7w\2\2\u00a2\u00a3\7t\2\2\u00a3")
        buf.write("\u00a4\7g\2\2\u00a4\b\3\2\2\2\u00a5\u00a6\7H\2\2\u00a6")
        buf.write("\u00a7\7c\2\2\u00a7\u00a8\7e\2\2\u00a8\u00a9\7v\2\2\u00a9")
        buf.write("\u00aa\7q\2\2\u00aa\u00ab\7t\2\2\u00ab\n\3\2\2\2\u00ac")
        buf.write("\u00ad\7I\2\2\u00ad\u00ae\7q\2\2\u00ae\u00af\7c\2\2\u00af")
        buf.write("\u00b0\7n\2\2\u00b0\f\3\2\2\2\u00b1\u00b2\7E\2\2\u00b2")
        buf.write("\u00b3\7q\2\2\u00b3\u00b4\7p\2\2\u00b4\u00b5\7u\2\2\u00b5")
        buf.write("\u00b6\7v\2\2\u00b6\u00b7\7c\2\2\u00b7\u00b8\7p\2\2\u00b8")
        buf.write("\u00b9\7v\2\2\u00b9\16\3\2\2\2\u00ba\u00bb\7C\2\2\u00bb")
        buf.write("\u00bc\7e\2\2\u00bc\u00bd\7v\2\2\u00bd\u00be\7k\2\2\u00be")
        buf.write("\u00bf\7q\2\2\u00bf\u00c0\7p\2\2\u00c0\20\3\2\2\2\u00c1")
        buf.write("\u00c2\7G\2\2\u00c2\u00c3\7h\2\2\u00c3\u00c4\7h\2\2\u00c4")
        buf.write("\u00c5\7g\2\2\u00c5\u00c6\7e\2\2\u00c6\u00c7\7v\2\2\u00c7")
        buf.write("\22\3\2\2\2\u00c8\u00c9\7T\2\2\u00c9\u00ca\7g\2\2\u00ca")
        buf.write("\u00cb\7y\2\2\u00cb\u00cc\7c\2\2\u00cc\u00cd\7t\2\2\u00cd")
        buf.write("\u00ce\7f\2\2\u00ce\24\3\2\2\2\u00cf\u00d0\7R\2\2\u00d0")
        buf.write("\u00d1\7q\2\2\u00d1\u00d2\7n\2\2\u00d2\u00d3\7k\2\2\u00d3")
        buf.write("\u00d4\7e\2\2\u00d4\u00d5\7{\2\2\u00d5\26\3\2\2\2\u00d6")
        buf.write("\u00d7\7G\2\2\u00d7\u00d8\7z\2\2\u00d8\u00d9\7g\2\2\u00d9")
        buf.write("\u00da\7e\2\2\u00da\u00db\7w\2\2\u00db\u00dc\7v\2\2\u00dc")
        buf.write("\u00dd\7g\2\2\u00dd\30\3\2\2\2\u00de\u00df\7Q\2\2\u00df")
        buf.write("\u00e0\7r\2\2\u00e0\u00e1\7v\2\2\u00e1\u00e2\7k\2\2\u00e2")
        buf.write("\u00e3\7q\2\2\u00e3\u00e4\7p\2\2\u00e4\32\3\2\2\2\u00e5")
        buf.write("\u00e6\7O\2\2\u00e6\u00e7\7c\2\2\u00e7\u00e8\7t\2\2\u00e8")
        buf.write("\u00e9\7m\2\2\u00e9\u00ea\7q\2\2\u00ea\u00eb\7x\2\2\u00eb")
        buf.write("\u00ec\7H\2\2\u00ec\u00ed\7g\2\2\u00ed\u00ee\7c\2\2\u00ee")
        buf.write("\u00ef\7v\2\2\u00ef\u00f0\7w\2\2\u00f0\u00f1\7t\2\2\u00f1")
        buf.write("\u00f2\7g\2\2\u00f2\34\3\2\2\2\u00f3\u00f4\7k\2\2\u00f4")
        buf.write("\u00f5\7o\2\2\u00f5\u00f6\7r\2\2\u00f6\u00f7\7q\2\2\u00f7")
        buf.write("\u00f8\7t\2\2\u00f8\u00f9\7v\2\2\u00f9\36\3\2\2\2\u00fa")
        buf.write("\u00fb\7U\2\2\u00fb\u00fc\7)\2\2\u00fc \3\2\2\2\u00fd")
        buf.write("\u00fe\7U\2\2\u00fe\"\3\2\2\2\u00ff\u0100\7C\2\2\u0100")
        buf.write("$\3\2\2\2\u0101\u0102\7k\2\2\u0102\u0103\7h\2\2\u0103")
        buf.write("&\3\2\2\2\u0104\u0105\7g\2\2\u0105\u0106\7n\2\2\u0106")
        buf.write("\u0107\7u\2\2\u0107\u0108\7g\2\2\u0108(\3\2\2\2\u0109")
        buf.write("\u010a\7g\2\2\u010a\u010b\7n\2\2\u010b\u010c\7k\2\2\u010c")
        buf.write("\u010d\7h\2\2\u010d*\3\2\2\2\u010e\u010f\7k\2\2\u010f")
        buf.write("\u0110\7p\2\2\u0110,\3\2\2\2\u0111\u0112\7k\2\2\u0112")
        buf.write("\u0113\7p\2\2\u0113\u0114\7k\2\2\u0114\u0115\7v\2\2\u0115")
        buf.write(".\3\2\2\2\u0116\u0117\7w\2\2\u0117\u0118\7p\2\2\u0118")
        buf.write("\u0119\7v\2\2\u0119\u011a\7k\2\2\u011a\u011b\7n\2\2\u011b")
        buf.write("\60\3\2\2\2\u011c\u011d\7c\2\2\u011d\u011e\7p\2\2\u011e")
        buf.write("\u011f\7f\2\2\u011f\62\3\2\2\2\u0120\u0121\7q\2\2\u0121")
        buf.write("\u0122\7t\2\2\u0122\64\3\2\2\2\u0123\u0124\7p\2\2\u0124")
        buf.write("\u0125\7q\2\2\u0125\u0126\7v\2\2\u0126\66\3\2\2\2\u0127")
        buf.write("\u0128\7V\2\2\u0128\u0129\7t\2\2\u0129\u012a\7w\2\2\u012a")
        buf.write("\u012b\7g\2\2\u012b8\3\2\2\2\u012c\u012d\7H\2\2\u012d")
        buf.write("\u012e\7c\2\2\u012e\u012f\7n\2\2\u012f\u0130\7u\2\2\u0130")
        buf.write("\u0131\7g\2\2\u0131:\3\2\2\2\u0132\u0133\7<\2\2\u0133")
        buf.write("\u0134\7?\2\2\u0134<\3\2\2\2\u0135\u0136\7?\2\2\u0136")
        buf.write(">\3\2\2\2\u0137\u0138\7,\2\2\u0138\u0139\7?\2\2\u0139")
        buf.write("@\3\2\2\2\u013a\u013b\7\61\2\2\u013b\u013c\7?\2\2\u013c")
        buf.write("B\3\2\2\2\u013d\u013e\7-\2\2\u013e\u013f\7?\2\2\u013f")
        buf.write("D\3\2\2\2\u0140\u0141\7/\2\2\u0141\u0142\7?\2\2\u0142")
        buf.write("F\3\2\2\2\u0143\u0144\7?\2\2\u0144\u0145\7?\2\2\u0145")
        buf.write("H\3\2\2\2\u0146\u0147\7@\2\2\u0147\u0148\7?\2\2\u0148")
        buf.write("J\3\2\2\2\u0149\u014a\7>\2\2\u014a\u014b\7?\2\2\u014b")
        buf.write("L\3\2\2\2\u014c\u014d\7#\2\2\u014d\u014e\7?\2\2\u014e")
        buf.write("N\3\2\2\2\u014f\u0150\7<\2\2\u0150P\3\2\2\2\u0151\u0152")
        buf.write("\7.\2\2\u0152R\3\2\2\2\u0153\u0154\7]\2\2\u0154T\3\2\2")
        buf.write("\2\u0155\u0156\7_\2\2\u0156V\3\2\2\2\u0157\u0158\7*\2")
        buf.write("\2\u0158X\3\2\2\2\u0159\u015a\7+\2\2\u015aZ\3\2\2\2\u015b")
        buf.write("\u015c\7>\2\2\u015c\\\3\2\2\2\u015d\u015e\7@\2\2\u015e")
        buf.write("^\3\2\2\2\u015f\u0160\7,\2\2\u0160`\3\2\2\2\u0161\u0162")
        buf.write("\7\61\2\2\u0162b\3\2\2\2\u0163\u0164\7-\2\2\u0164d\3\2")
        buf.write("\2\2\u0165\u0166\7/\2\2\u0166f\3\2\2\2\u0167\u0168\5i")
        buf.write("\65\2\u0168\u016c\7\60\2\2\u0169\u016b\5o8\2\u016a\u0169")
        buf.write("\3\2\2\2\u016b\u016e\3\2\2\2\u016c\u016a\3\2\2\2\u016c")
        buf.write("\u016d\3\2\2\2\u016dh\3\2\2\2\u016e\u016c\3\2\2\2\u016f")
        buf.write("\u0173\5o8\2\u0170\u0172\5q9\2\u0171\u0170\3\2\2\2\u0172")
        buf.write("\u0175\3\2\2\2\u0173\u0171\3\2\2\2\u0173\u0174\3\2\2\2")
        buf.write("\u0174j\3\2\2\2\u0175\u0173\3\2\2\2\u0176\u0178\5s:\2")
        buf.write("\u0177\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u0177\3")
        buf.write("\2\2\2\u0179\u017a\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017d")
        buf.write("\7\60\2\2\u017c\u017e\5s:\2\u017d\u017c\3\2\2\2\u017e")
        buf.write("\u017f\3\2\2\2\u017f\u017d\3\2\2\2\u017f\u0180\3\2\2\2")
        buf.write("\u0180l\3\2\2\2\u0181\u0183\5s:\2\u0182\u0181\3\2\2\2")
        buf.write("\u0183\u0184\3\2\2\2\u0184\u0182\3\2\2\2\u0184\u0185\3")
        buf.write("\2\2\2\u0185n\3\2\2\2\u0186\u0188\t\2\2\2\u0187\u0186")
        buf.write("\3\2\2\2\u0188p\3\2\2\2\u0189\u018d\5o8\2\u018a\u018d")
        buf.write("\5s:\2\u018b\u018d\7a\2\2\u018c\u0189\3\2\2\2\u018c\u018a")
        buf.write("\3\2\2\2\u018c\u018b\3\2\2\2\u018dr\3\2\2\2\u018e\u018f")
        buf.write("\t\3\2\2\u018ft\3\2\2\2\u0190\u0192\t\4\2\2\u0191\u0190")
        buf.write("\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0191\3\2\2\2\u0193")
        buf.write("\u0194\3\2\2\2\u0194v\3\2\2\2\u0195\u0199\7%\2\2\u0196")
        buf.write("\u0198\n\5\2\2\u0197\u0196\3\2\2\2\u0198\u019b\3\2\2\2")
        buf.write("\u0199\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019ax\3\2\2")
        buf.write("\2\u019b\u0199\3\2\2\2\u019c\u019f\5u;\2\u019d\u019f\5")
        buf.write("w<\2\u019e\u019c\3\2\2\2\u019e\u019d\3\2\2\2\u019f\u01a0")
        buf.write("\3\2\2\2\u01a0\u01a1\b=\2\2\u01a1z\3\2\2\2\u01a2\u01a3")
        buf.write("\13\2\2\2\u01a3|\3\2\2\2\22\2~\u0084\u0088\u008e\u0091")
        buf.write("\u016c\u0173\u0179\u017f\u0184\u0187\u018c\u0193\u0199")
        buf.write("\u019e\3\b\2\2")
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
    POLICY = 12
    EXECUTE = 13
    OPTION = 14
    MARKOVFEATURE = 15
    IMPORT = 16
    S_PRIME = 17
    S = 18
    A = 19
    IF = 20
    ELSE = 21
    ELIF = 22
    IN = 23
    INIT = 24
    UNTIL = 25
    AND = 26
    OR = 27
    NOT = 28
    TRUE = 29
    FALSE = 30
    BIND = 31
    ASSIGN = 32
    TIMES_EQ = 33
    DIV_EQ = 34
    PLUS_EQ = 35
    MINUS_EQ = 36
    EQ_TO = 37
    GT_EQ = 38
    LT_EQ = 39
    NOT_EQ = 40
    COL = 41
    COM = 42
    L_BRK = 43
    R_BRK = 44
    L_PAR = 45
    R_PAR = 46
    LT = 47
    GT = 48
    TIMES = 49
    DIVIDE = 50
    PLUS = 51
    MINUS = 52
    FNAME = 53
    IDENTIFIER = 54
    DECIMAL = 55
    INTEGER = 56
    SKIP_ = 57
    ANY = 58

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Predicate'", "'Feature'", "'Factor'", "'Goal'", "'Constant'", 
            "'Action'", "'Effect'", "'Reward'", "'Policy'", "'Execute'", 
            "'Option'", "'MarkovFeature'", "'import'", "'S''", "'S'", "'A'", 
            "'if'", "'else'", "'elif'", "'in'", "'init'", "'until'", "'and'", 
            "'or'", "'not'", "'True'", "'False'", "':='", "'='", "'*='", 
            "'/='", "'+='", "'-='", "'=='", "'>='", "'<='", "'!='", "':'", 
            "','", "'['", "']'", "'('", "')'", "'<'", "'>'", "'*'", "'/'", 
            "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "NL", "PREDICATE", "FEATURE", "FACTOR", 
            "GOAL", "CONSTANT", "ACTION", "EFFECT", "REWARD", "POLICY", 
            "EXECUTE", "OPTION", "MARKOVFEATURE", "IMPORT", "S_PRIME", "S", 
            "A", "IF", "ELSE", "ELIF", "IN", "INIT", "UNTIL", "AND", "OR", 
            "NOT", "TRUE", "FALSE", "BIND", "ASSIGN", "TIMES_EQ", "DIV_EQ", 
            "PLUS_EQ", "MINUS_EQ", "EQ_TO", "GT_EQ", "LT_EQ", "NOT_EQ", 
            "COL", "COM", "L_BRK", "R_BRK", "L_PAR", "R_PAR", "LT", "GT", 
            "TIMES", "DIVIDE", "PLUS", "MINUS", "FNAME", "IDENTIFIER", "DECIMAL", 
            "INTEGER", "SKIP_", "ANY" ]

    ruleNames = [ "NL", "PREDICATE", "FEATURE", "FACTOR", "GOAL", "CONSTANT", 
                  "ACTION", "EFFECT", "REWARD", "POLICY", "EXECUTE", "OPTION", 
                  "MARKOVFEATURE", "IMPORT", "S_PRIME", "S", "A", "IF", 
                  "ELSE", "ELIF", "IN", "INIT", "UNTIL", "AND", "OR", "NOT", 
                  "TRUE", "FALSE", "BIND", "ASSIGN", "TIMES_EQ", "DIV_EQ", 
                  "PLUS_EQ", "MINUS_EQ", "EQ_TO", "GT_EQ", "LT_EQ", "NOT_EQ", 
                  "COL", "COM", "L_BRK", "R_BRK", "L_PAR", "R_PAR", "LT", 
                  "GT", "TIMES", "DIVIDE", "PLUS", "MINUS", "FNAME", "IDENTIFIER", 
                  "DECIMAL", "INTEGER", "LETTER", "ANY_CHAR", "DIGIT", "SPACES", 
                  "COMMENT", "SKIP_", "ANY" ]

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



