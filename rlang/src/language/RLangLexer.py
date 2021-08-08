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
        buf.write("\u01a9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3")
        buf.write("!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3")
        buf.write(".\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64")
        buf.write("\3\64\3\65\3\65\3\65\7\65\u0170\n\65\f\65\16\65\u0173")
        buf.write("\13\65\3\65\3\65\3\66\3\66\7\66\u0179\n\66\f\66\16\66")
        buf.write("\u017c\13\66\3\67\6\67\u017f\n\67\r\67\16\67\u0180\3\67")
        buf.write("\3\67\6\67\u0185\n\67\r\67\16\67\u0186\38\68\u018a\n8")
        buf.write("\r8\168\u018b\39\59\u018f\n9\3:\3:\3:\5:\u0194\n:\3;\3")
        buf.write(";\3<\6<\u0199\n<\r<\16<\u019a\3=\3=\7=\u019f\n=\f=\16")
        buf.write("=\u01a2\13=\3>\3>\5>\u01a6\n>\3>\3>\2\2?\3\5\5\6\7\7\t")
        buf.write("\b\13\t\r\n\17\13\21\f\23\r\25\16\27\17\31\20\33\21\35")
        buf.write("\22\37\23!\24#\25%\26\'\27)\30+\31-\32/\33\61\34\63\35")
        buf.write("\65\36\67\379 ;!=\"?#A$C%E&G\'I(K)M*O+Q,S-U.W/Y\60[\61")
        buf.write("]\62_\63a\64c\65e\66g\67i8k9m:o;q\2s\2u\2w\2y\2{<\3\2")
        buf.write("\6\4\2C\\c|\3\2\62;\4\2\13\13\"\"\4\2\f\f\16\17\2\u01b2")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2{")
        buf.write("\3\2\2\2\3\u0091\3\2\2\2\5\u0093\3\2\2\2\7\u009d\3\2\2")
        buf.write("\2\t\u00a5\3\2\2\2\13\u00ac\3\2\2\2\r\u00b1\3\2\2\2\17")
        buf.write("\u00ba\3\2\2\2\21\u00c1\3\2\2\2\23\u00c8\3\2\2\2\25\u00cf")
        buf.write("\3\2\2\2\27\u00d6\3\2\2\2\31\u00de\3\2\2\2\33\u00e5\3")
        buf.write("\2\2\2\35\u00ea\3\2\2\2\37\u00f8\3\2\2\2!\u00ff\3\2\2")
        buf.write("\2#\u0102\3\2\2\2%\u0104\3\2\2\2\'\u0106\3\2\2\2)\u0109")
        buf.write("\3\2\2\2+\u010e\3\2\2\2-\u0113\3\2\2\2/\u0116\3\2\2\2")
        buf.write("\61\u011b\3\2\2\2\63\u0121\3\2\2\2\65\u0125\3\2\2\2\67")
        buf.write("\u0128\3\2\2\29\u012c\3\2\2\2;\u0131\3\2\2\2=\u0137\3")
        buf.write("\2\2\2?\u013a\3\2\2\2A\u013c\3\2\2\2C\u013f\3\2\2\2E\u0142")
        buf.write("\3\2\2\2G\u0145\3\2\2\2I\u0148\3\2\2\2K\u014b\3\2\2\2")
        buf.write("M\u014e\3\2\2\2O\u0151\3\2\2\2Q\u0154\3\2\2\2S\u0156\3")
        buf.write("\2\2\2U\u0158\3\2\2\2W\u015a\3\2\2\2Y\u015c\3\2\2\2[\u015e")
        buf.write("\3\2\2\2]\u0160\3\2\2\2_\u0162\3\2\2\2a\u0164\3\2\2\2")
        buf.write("c\u0166\3\2\2\2e\u0168\3\2\2\2g\u016a\3\2\2\2i\u016c\3")
        buf.write("\2\2\2k\u0176\3\2\2\2m\u017e\3\2\2\2o\u0189\3\2\2\2q\u018e")
        buf.write("\3\2\2\2s\u0193\3\2\2\2u\u0195\3\2\2\2w\u0198\3\2\2\2")
        buf.write("y\u019c\3\2\2\2{\u01a5\3\2\2\2}\177\7\17\2\2~}\3\2\2\2")
        buf.write("~\177\3\2\2\2\177\u0080\3\2\2\2\u0080\u0084\7\f\2\2\u0081")
        buf.write("\u0083\7\"\2\2\u0082\u0081\3\2\2\2\u0083\u0086\3\2\2\2")
        buf.write("\u0084\u0082\3\2\2\2\u0084\u0085\3\2\2\2\u0085\u0092\3")
        buf.write("\2\2\2\u0086\u0084\3\2\2\2\u0087\u0089\7\17\2\2\u0088")
        buf.write("\u0087\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008a\3\2\2\2")
        buf.write("\u008a\u008e\7\f\2\2\u008b\u008d\7\13\2\2\u008c\u008b")
        buf.write("\3\2\2\2\u008d\u0090\3\2\2\2\u008e\u008c\3\2\2\2\u008e")
        buf.write("\u008f\3\2\2\2\u008f\u0092\3\2\2\2\u0090\u008e\3\2\2\2")
        buf.write("\u0091~\3\2\2\2\u0091\u0088\3\2\2\2\u0092\4\3\2\2\2\u0093")
        buf.write("\u0094\7R\2\2\u0094\u0095\7t\2\2\u0095\u0096\7g\2\2\u0096")
        buf.write("\u0097\7f\2\2\u0097\u0098\7k\2\2\u0098\u0099\7e\2\2\u0099")
        buf.write("\u009a\7c\2\2\u009a\u009b\7v\2\2\u009b\u009c\7g\2\2\u009c")
        buf.write("\6\3\2\2\2\u009d\u009e\7H\2\2\u009e\u009f\7g\2\2\u009f")
        buf.write("\u00a0\7c\2\2\u00a0\u00a1\7v\2\2\u00a1\u00a2\7w\2\2\u00a2")
        buf.write("\u00a3\7t\2\2\u00a3\u00a4\7g\2\2\u00a4\b\3\2\2\2\u00a5")
        buf.write("\u00a6\7H\2\2\u00a6\u00a7\7c\2\2\u00a7\u00a8\7e\2\2\u00a8")
        buf.write("\u00a9\7v\2\2\u00a9\u00aa\7q\2\2\u00aa\u00ab\7t\2\2\u00ab")
        buf.write("\n\3\2\2\2\u00ac\u00ad\7I\2\2\u00ad\u00ae\7q\2\2\u00ae")
        buf.write("\u00af\7c\2\2\u00af\u00b0\7n\2\2\u00b0\f\3\2\2\2\u00b1")
        buf.write("\u00b2\7E\2\2\u00b2\u00b3\7q\2\2\u00b3\u00b4\7p\2\2\u00b4")
        buf.write("\u00b5\7u\2\2\u00b5\u00b6\7v\2\2\u00b6\u00b7\7c\2\2\u00b7")
        buf.write("\u00b8\7p\2\2\u00b8\u00b9\7v\2\2\u00b9\16\3\2\2\2\u00ba")
        buf.write("\u00bb\7C\2\2\u00bb\u00bc\7e\2\2\u00bc\u00bd\7v\2\2\u00bd")
        buf.write("\u00be\7k\2\2\u00be\u00bf\7q\2\2\u00bf\u00c0\7p\2\2\u00c0")
        buf.write("\20\3\2\2\2\u00c1\u00c2\7G\2\2\u00c2\u00c3\7h\2\2\u00c3")
        buf.write("\u00c4\7h\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6\7e\2\2\u00c6")
        buf.write("\u00c7\7v\2\2\u00c7\22\3\2\2\2\u00c8\u00c9\7T\2\2\u00c9")
        buf.write("\u00ca\7g\2\2\u00ca\u00cb\7y\2\2\u00cb\u00cc\7c\2\2\u00cc")
        buf.write("\u00cd\7t\2\2\u00cd\u00ce\7f\2\2\u00ce\24\3\2\2\2\u00cf")
        buf.write("\u00d0\7R\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2\7n\2\2\u00d2")
        buf.write("\u00d3\7k\2\2\u00d3\u00d4\7e\2\2\u00d4\u00d5\7{\2\2\u00d5")
        buf.write("\26\3\2\2\2\u00d6\u00d7\7G\2\2\u00d7\u00d8\7z\2\2\u00d8")
        buf.write("\u00d9\7g\2\2\u00d9\u00da\7e\2\2\u00da\u00db\7w\2\2\u00db")
        buf.write("\u00dc\7v\2\2\u00dc\u00dd\7g\2\2\u00dd\30\3\2\2\2\u00de")
        buf.write("\u00df\7Q\2\2\u00df\u00e0\7r\2\2\u00e0\u00e1\7v\2\2\u00e1")
        buf.write("\u00e2\7k\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4\7p\2\2\u00e4")
        buf.write("\32\3\2\2\2\u00e5\u00e6\7H\2\2\u00e6\u00e7\7k\2\2\u00e7")
        buf.write("\u00e8\7p\2\2\u00e8\u00e9\7f\2\2\u00e9\34\3\2\2\2\u00ea")
        buf.write("\u00eb\7O\2\2\u00eb\u00ec\7c\2\2\u00ec\u00ed\7t\2\2\u00ed")
        buf.write("\u00ee\7m\2\2\u00ee\u00ef\7q\2\2\u00ef\u00f0\7x\2\2\u00f0")
        buf.write("\u00f1\7H\2\2\u00f1\u00f2\7g\2\2\u00f2\u00f3\7c\2\2\u00f3")
        buf.write("\u00f4\7v\2\2\u00f4\u00f5\7w\2\2\u00f5\u00f6\7t\2\2\u00f6")
        buf.write("\u00f7\7g\2\2\u00f7\36\3\2\2\2\u00f8\u00f9\7k\2\2\u00f9")
        buf.write("\u00fa\7o\2\2\u00fa\u00fb\7r\2\2\u00fb\u00fc\7q\2\2\u00fc")
        buf.write("\u00fd\7t\2\2\u00fd\u00fe\7v\2\2\u00fe \3\2\2\2\u00ff")
        buf.write("\u0100\7U\2\2\u0100\u0101\7)\2\2\u0101\"\3\2\2\2\u0102")
        buf.write("\u0103\7U\2\2\u0103$\3\2\2\2\u0104\u0105\7C\2\2\u0105")
        buf.write("&\3\2\2\2\u0106\u0107\7k\2\2\u0107\u0108\7h\2\2\u0108")
        buf.write("(\3\2\2\2\u0109\u010a\7g\2\2\u010a\u010b\7n\2\2\u010b")
        buf.write("\u010c\7u\2\2\u010c\u010d\7g\2\2\u010d*\3\2\2\2\u010e")
        buf.write("\u010f\7g\2\2\u010f\u0110\7n\2\2\u0110\u0111\7k\2\2\u0111")
        buf.write("\u0112\7h\2\2\u0112,\3\2\2\2\u0113\u0114\7k\2\2\u0114")
        buf.write("\u0115\7p\2\2\u0115.\3\2\2\2\u0116\u0117\7k\2\2\u0117")
        buf.write("\u0118\7p\2\2\u0118\u0119\7k\2\2\u0119\u011a\7v\2\2\u011a")
        buf.write("\60\3\2\2\2\u011b\u011c\7w\2\2\u011c\u011d\7p\2\2\u011d")
        buf.write("\u011e\7v\2\2\u011e\u011f\7k\2\2\u011f\u0120\7n\2\2\u0120")
        buf.write("\62\3\2\2\2\u0121\u0122\7c\2\2\u0122\u0123\7p\2\2\u0123")
        buf.write("\u0124\7f\2\2\u0124\64\3\2\2\2\u0125\u0126\7q\2\2\u0126")
        buf.write("\u0127\7t\2\2\u0127\66\3\2\2\2\u0128\u0129\7p\2\2\u0129")
        buf.write("\u012a\7q\2\2\u012a\u012b\7v\2\2\u012b8\3\2\2\2\u012c")
        buf.write("\u012d\7V\2\2\u012d\u012e\7t\2\2\u012e\u012f\7w\2\2\u012f")
        buf.write("\u0130\7g\2\2\u0130:\3\2\2\2\u0131\u0132\7H\2\2\u0132")
        buf.write("\u0133\7c\2\2\u0133\u0134\7n\2\2\u0134\u0135\7u\2\2\u0135")
        buf.write("\u0136\7g\2\2\u0136<\3\2\2\2\u0137\u0138\7<\2\2\u0138")
        buf.write("\u0139\7?\2\2\u0139>\3\2\2\2\u013a\u013b\7?\2\2\u013b")
        buf.write("@\3\2\2\2\u013c\u013d\7,\2\2\u013d\u013e\7?\2\2\u013e")
        buf.write("B\3\2\2\2\u013f\u0140\7\61\2\2\u0140\u0141\7?\2\2\u0141")
        buf.write("D\3\2\2\2\u0142\u0143\7-\2\2\u0143\u0144\7?\2\2\u0144")
        buf.write("F\3\2\2\2\u0145\u0146\7/\2\2\u0146\u0147\7?\2\2\u0147")
        buf.write("H\3\2\2\2\u0148\u0149\7?\2\2\u0149\u014a\7?\2\2\u014a")
        buf.write("J\3\2\2\2\u014b\u014c\7@\2\2\u014c\u014d\7?\2\2\u014d")
        buf.write("L\3\2\2\2\u014e\u014f\7>\2\2\u014f\u0150\7?\2\2\u0150")
        buf.write("N\3\2\2\2\u0151\u0152\7#\2\2\u0152\u0153\7?\2\2\u0153")
        buf.write("P\3\2\2\2\u0154\u0155\7<\2\2\u0155R\3\2\2\2\u0156\u0157")
        buf.write("\7.\2\2\u0157T\3\2\2\2\u0158\u0159\7]\2\2\u0159V\3\2\2")
        buf.write("\2\u015a\u015b\7_\2\2\u015bX\3\2\2\2\u015c\u015d\7*\2")
        buf.write("\2\u015dZ\3\2\2\2\u015e\u015f\7+\2\2\u015f\\\3\2\2\2\u0160")
        buf.write("\u0161\7>\2\2\u0161^\3\2\2\2\u0162\u0163\7@\2\2\u0163")
        buf.write("`\3\2\2\2\u0164\u0165\7,\2\2\u0165b\3\2\2\2\u0166\u0167")
        buf.write("\7\61\2\2\u0167d\3\2\2\2\u0168\u0169\7-\2\2\u0169f\3\2")
        buf.write("\2\2\u016a\u016b\7/\2\2\u016bh\3\2\2\2\u016c\u016d\5k")
        buf.write("\66\2\u016d\u0171\7\60\2\2\u016e\u0170\5q9\2\u016f\u016e")
        buf.write("\3\2\2\2\u0170\u0173\3\2\2\2\u0171\u016f\3\2\2\2\u0171")
        buf.write("\u0172\3\2\2\2\u0172\u0174\3\2\2\2\u0173\u0171\3\2\2\2")
        buf.write("\u0174\u0175\5u;\2\u0175j\3\2\2\2\u0176\u017a\5q9\2\u0177")
        buf.write("\u0179\5s:\2\u0178\u0177\3\2\2\2\u0179\u017c\3\2\2\2\u017a")
        buf.write("\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017bl\3\2\2\2\u017c")
        buf.write("\u017a\3\2\2\2\u017d\u017f\5u;\2\u017e\u017d\3\2\2\2\u017f")
        buf.write("\u0180\3\2\2\2\u0180\u017e\3\2\2\2\u0180\u0181\3\2\2\2")
        buf.write("\u0181\u0182\3\2\2\2\u0182\u0184\7\60\2\2\u0183\u0185")
        buf.write("\5u;\2\u0184\u0183\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0184")
        buf.write("\3\2\2\2\u0186\u0187\3\2\2\2\u0187n\3\2\2\2\u0188\u018a")
        buf.write("\5u;\2\u0189\u0188\3\2\2\2\u018a\u018b\3\2\2\2\u018b\u0189")
        buf.write("\3\2\2\2\u018b\u018c\3\2\2\2\u018cp\3\2\2\2\u018d\u018f")
        buf.write("\t\2\2\2\u018e\u018d\3\2\2\2\u018fr\3\2\2\2\u0190\u0194")
        buf.write("\5q9\2\u0191\u0194\5u;\2\u0192\u0194\7a\2\2\u0193\u0190")
        buf.write("\3\2\2\2\u0193\u0191\3\2\2\2\u0193\u0192\3\2\2\2\u0194")
        buf.write("t\3\2\2\2\u0195\u0196\t\3\2\2\u0196v\3\2\2\2\u0197\u0199")
        buf.write("\t\4\2\2\u0198\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019a")
        buf.write("\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019bx\3\2\2\2\u019c")
        buf.write("\u01a0\7%\2\2\u019d\u019f\n\5\2\2\u019e\u019d\3\2\2\2")
        buf.write("\u019f\u01a2\3\2\2\2\u01a0\u019e\3\2\2\2\u01a0\u01a1\3")
        buf.write("\2\2\2\u01a1z\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a3\u01a6")
        buf.write("\5w<\2\u01a4\u01a6\5y=\2\u01a5\u01a3\3\2\2\2\u01a5\u01a4")
        buf.write("\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a8\b>\2\2\u01a8")
        buf.write("|\3\2\2\2\22\2~\u0084\u0088\u008e\u0091\u0171\u017a\u0180")
        buf.write("\u0186\u018b\u018e\u0193\u019a\u01a0\u01a5\3\b\2\2")
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
    FIND = 15
    MARKOVFEATURE = 16
    IMPORT = 17
    S_PRIME = 18
    S = 19
    A = 20
    IF = 21
    ELSE = 22
    ELIF = 23
    IN = 24
    INIT = 25
    UNTIL = 26
    AND = 27
    OR = 28
    NOT = 29
    TRUE = 30
    FALSE = 31
    BIND = 32
    ASSIGN = 33
    TIMES_EQ = 34
    DIV_EQ = 35
    PLUS_EQ = 36
    MINUS_EQ = 37
    EQ_TO = 38
    GT_EQ = 39
    LT_EQ = 40
    NOT_EQ = 41
    COL = 42
    COM = 43
    L_BRK = 44
    R_BRK = 45
    L_PAR = 46
    R_PAR = 47
    LT = 48
    GT = 49
    TIMES = 50
    DIVIDE = 51
    PLUS = 52
    MINUS = 53
    FNAME = 54
    IDENTIFIER = 55
    DECIMAL = 56
    INTEGER = 57
    SKIP_ = 58

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Predicate'", "'Feature'", "'Factor'", "'Goal'", "'Constant'", 
            "'Action'", "'Effect'", "'Reward'", "'Policy'", "'Execute'", 
            "'Option'", "'Find'", "'MarkovFeature'", "'import'", "'S''", 
            "'S'", "'A'", "'if'", "'else'", "'elif'", "'in'", "'init'", 
            "'until'", "'and'", "'or'", "'not'", "'True'", "'False'", "':='", 
            "'='", "'*='", "'/='", "'+='", "'-='", "'=='", "'>='", "'<='", 
            "'!='", "':'", "','", "'['", "']'", "'('", "')'", "'<'", "'>'", 
            "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "NL", "PREDICATE", "FEATURE", "FACTOR", 
            "GOAL", "CONSTANT", "ACTION", "EFFECT", "REWARD", "POLICY", 
            "EXECUTE", "OPTION", "FIND", "MARKOVFEATURE", "IMPORT", "S_PRIME", 
            "S", "A", "IF", "ELSE", "ELIF", "IN", "INIT", "UNTIL", "AND", 
            "OR", "NOT", "TRUE", "FALSE", "BIND", "ASSIGN", "TIMES_EQ", 
            "DIV_EQ", "PLUS_EQ", "MINUS_EQ", "EQ_TO", "GT_EQ", "LT_EQ", 
            "NOT_EQ", "COL", "COM", "L_BRK", "R_BRK", "L_PAR", "R_PAR", 
            "LT", "GT", "TIMES", "DIVIDE", "PLUS", "MINUS", "FNAME", "IDENTIFIER", 
            "DECIMAL", "INTEGER", "SKIP_" ]

    ruleNames = [ "NL", "PREDICATE", "FEATURE", "FACTOR", "GOAL", "CONSTANT", 
                  "ACTION", "EFFECT", "REWARD", "POLICY", "EXECUTE", "OPTION", 
                  "FIND", "MARKOVFEATURE", "IMPORT", "S_PRIME", "S", "A", 
                  "IF", "ELSE", "ELIF", "IN", "INIT", "UNTIL", "AND", "OR", 
                  "NOT", "TRUE", "FALSE", "BIND", "ASSIGN", "TIMES_EQ", 
                  "DIV_EQ", "PLUS_EQ", "MINUS_EQ", "EQ_TO", "GT_EQ", "LT_EQ", 
                  "NOT_EQ", "COL", "COM", "L_BRK", "R_BRK", "L_PAR", "R_PAR", 
                  "LT", "GT", "TIMES", "DIVIDE", "PLUS", "MINUS", "FNAME", 
                  "IDENTIFIER", "DECIMAL", "INTEGER", "LETTER", "ANY_CHAR", 
                  "DIGIT", "SPACES", "COMMENT", "SKIP_" ]

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



