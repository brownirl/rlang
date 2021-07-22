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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\29")
        buf.write("\u018c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\3\2\5\2y\n\2\3\2\3\2\7\2}\n\2\f\2\16\2\u0080\13")
        buf.write("\2\3\2\5\2\u0083\n\2\3\2\3\2\7\2\u0087\n\2\f\2\16\2\u008a")
        buf.write("\13\2\5\2\u008c\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3")
        buf.write("!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3\'")
        buf.write("\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\7\63\u015c\n\63")
        buf.write("\f\63\16\63\u015f\13\63\3\64\6\64\u0162\n\64\r\64\16\64")
        buf.write("\u0163\3\64\3\64\6\64\u0168\n\64\r\64\16\64\u0169\3\65")
        buf.write("\6\65\u016d\n\65\r\65\16\65\u016e\3\66\5\66\u0172\n\66")
        buf.write("\3\67\3\67\3\67\5\67\u0177\n\67\38\38\39\69\u017c\n9\r")
        buf.write("9\169\u017d\3:\3:\7:\u0182\n:\f:\16:\u0185\13:\3;\3;\5")
        buf.write(";\u0189\n;\3;\3;\2\2<\3\5\5\6\7\7\t\b\13\t\r\n\17\13\21")
        buf.write("\f\23\r\25\16\27\17\31\20\33\21\35\22\37\23!\24#\25%\26")
        buf.write("\'\27)\30+\31-\32/\33\61\34\63\35\65\36\67\379 ;!=\"?")
        buf.write("#A$C%E&G\'I(K)M*O+Q,S-U.W/Y\60[\61]\62_\63a\64c\65e\66")
        buf.write("g\67i8k\2m\2o\2q\2s\2u9\3\2\6\4\2C\\c|\3\2\62;\4\2\13")
        buf.write("\13\"\"\4\2\f\f\16\17\2\u0194\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2")
        buf.write("\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2u\3\2")
        buf.write("\2\2\3\u008b\3\2\2\2\5\u008d\3\2\2\2\7\u0097\3\2\2\2\t")
        buf.write("\u009f\3\2\2\2\13\u00a6\3\2\2\2\r\u00ab\3\2\2\2\17\u00b4")
        buf.write("\3\2\2\2\21\u00bb\3\2\2\2\23\u00c2\3\2\2\2\25\u00c9\3")
        buf.write("\2\2\2\27\u00d0\3\2\2\2\31\u00d8\3\2\2\2\33\u00df\3\2")
        buf.write("\2\2\35\u00ed\3\2\2\2\37\u00ef\3\2\2\2!\u00f1\3\2\2\2")
        buf.write("#\u00f4\3\2\2\2%\u00f9\3\2\2\2\'\u00fe\3\2\2\2)\u0101")
        buf.write("\3\2\2\2+\u0106\3\2\2\2-\u010c\3\2\2\2/\u0110\3\2\2\2")
        buf.write("\61\u0113\3\2\2\2\63\u0117\3\2\2\2\65\u011c\3\2\2\2\67")
        buf.write("\u0122\3\2\2\29\u0125\3\2\2\2;\u0127\3\2\2\2=\u012a\3")
        buf.write("\2\2\2?\u012d\3\2\2\2A\u0130\3\2\2\2C\u0133\3\2\2\2E\u0136")
        buf.write("\3\2\2\2G\u0139\3\2\2\2I\u013c\3\2\2\2K\u013f\3\2\2\2")
        buf.write("M\u0141\3\2\2\2O\u0143\3\2\2\2Q\u0145\3\2\2\2S\u0147\3")
        buf.write("\2\2\2U\u0149\3\2\2\2W\u014b\3\2\2\2Y\u014d\3\2\2\2[\u014f")
        buf.write("\3\2\2\2]\u0151\3\2\2\2_\u0153\3\2\2\2a\u0155\3\2\2\2")
        buf.write("c\u0157\3\2\2\2e\u0159\3\2\2\2g\u0161\3\2\2\2i\u016c\3")
        buf.write("\2\2\2k\u0171\3\2\2\2m\u0176\3\2\2\2o\u0178\3\2\2\2q\u017b")
        buf.write("\3\2\2\2s\u017f\3\2\2\2u\u0188\3\2\2\2wy\7\17\2\2xw\3")
        buf.write("\2\2\2xy\3\2\2\2yz\3\2\2\2z~\7\f\2\2{}\7\"\2\2|{\3\2\2")
        buf.write("\2}\u0080\3\2\2\2~|\3\2\2\2~\177\3\2\2\2\177\u008c\3\2")
        buf.write("\2\2\u0080~\3\2\2\2\u0081\u0083\7\17\2\2\u0082\u0081\3")
        buf.write("\2\2\2\u0082\u0083\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0088")
        buf.write("\7\f\2\2\u0085\u0087\7\13\2\2\u0086\u0085\3\2\2\2\u0087")
        buf.write("\u008a\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2")
        buf.write("\u0089\u008c\3\2\2\2\u008a\u0088\3\2\2\2\u008bx\3\2\2")
        buf.write("\2\u008b\u0082\3\2\2\2\u008c\4\3\2\2\2\u008d\u008e\7R")
        buf.write("\2\2\u008e\u008f\7t\2\2\u008f\u0090\7g\2\2\u0090\u0091")
        buf.write("\7f\2\2\u0091\u0092\7k\2\2\u0092\u0093\7e\2\2\u0093\u0094")
        buf.write("\7c\2\2\u0094\u0095\7v\2\2\u0095\u0096\7g\2\2\u0096\6")
        buf.write("\3\2\2\2\u0097\u0098\7H\2\2\u0098\u0099\7g\2\2\u0099\u009a")
        buf.write("\7c\2\2\u009a\u009b\7v\2\2\u009b\u009c\7w\2\2\u009c\u009d")
        buf.write("\7t\2\2\u009d\u009e\7g\2\2\u009e\b\3\2\2\2\u009f\u00a0")
        buf.write("\7H\2\2\u00a0\u00a1\7c\2\2\u00a1\u00a2\7e\2\2\u00a2\u00a3")
        buf.write("\7v\2\2\u00a3\u00a4\7q\2\2\u00a4\u00a5\7t\2\2\u00a5\n")
        buf.write("\3\2\2\2\u00a6\u00a7\7I\2\2\u00a7\u00a8\7q\2\2\u00a8\u00a9")
        buf.write("\7c\2\2\u00a9\u00aa\7n\2\2\u00aa\f\3\2\2\2\u00ab\u00ac")
        buf.write("\7E\2\2\u00ac\u00ad\7q\2\2\u00ad\u00ae\7p\2\2\u00ae\u00af")
        buf.write("\7u\2\2\u00af\u00b0\7v\2\2\u00b0\u00b1\7c\2\2\u00b1\u00b2")
        buf.write("\7p\2\2\u00b2\u00b3\7v\2\2\u00b3\16\3\2\2\2\u00b4\u00b5")
        buf.write("\7C\2\2\u00b5\u00b6\7e\2\2\u00b6\u00b7\7v\2\2\u00b7\u00b8")
        buf.write("\7k\2\2\u00b8\u00b9\7q\2\2\u00b9\u00ba\7p\2\2\u00ba\20")
        buf.write("\3\2\2\2\u00bb\u00bc\7G\2\2\u00bc\u00bd\7h\2\2\u00bd\u00be")
        buf.write("\7h\2\2\u00be\u00bf\7g\2\2\u00bf\u00c0\7e\2\2\u00c0\u00c1")
        buf.write("\7v\2\2\u00c1\22\3\2\2\2\u00c2\u00c3\7T\2\2\u00c3\u00c4")
        buf.write("\7g\2\2\u00c4\u00c5\7y\2\2\u00c5\u00c6\7c\2\2\u00c6\u00c7")
        buf.write("\7t\2\2\u00c7\u00c8\7f\2\2\u00c8\24\3\2\2\2\u00c9\u00ca")
        buf.write("\7R\2\2\u00ca\u00cb\7q\2\2\u00cb\u00cc\7n\2\2\u00cc\u00cd")
        buf.write("\7k\2\2\u00cd\u00ce\7e\2\2\u00ce\u00cf\7{\2\2\u00cf\26")
        buf.write("\3\2\2\2\u00d0\u00d1\7G\2\2\u00d1\u00d2\7z\2\2\u00d2\u00d3")
        buf.write("\7g\2\2\u00d3\u00d4\7e\2\2\u00d4\u00d5\7w\2\2\u00d5\u00d6")
        buf.write("\7v\2\2\u00d6\u00d7\7g\2\2\u00d7\30\3\2\2\2\u00d8\u00d9")
        buf.write("\7Q\2\2\u00d9\u00da\7r\2\2\u00da\u00db\7v\2\2\u00db\u00dc")
        buf.write("\7k\2\2\u00dc\u00dd\7q\2\2\u00dd\u00de\7p\2\2\u00de\32")
        buf.write("\3\2\2\2\u00df\u00e0\7O\2\2\u00e0\u00e1\7c\2\2\u00e1\u00e2")
        buf.write("\7t\2\2\u00e2\u00e3\7m\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5")
        buf.write("\7x\2\2\u00e5\u00e6\7H\2\2\u00e6\u00e7\7g\2\2\u00e7\u00e8")
        buf.write("\7c\2\2\u00e8\u00e9\7v\2\2\u00e9\u00ea\7w\2\2\u00ea\u00eb")
        buf.write("\7t\2\2\u00eb\u00ec\7g\2\2\u00ec\34\3\2\2\2\u00ed\u00ee")
        buf.write("\7U\2\2\u00ee\36\3\2\2\2\u00ef\u00f0\7C\2\2\u00f0 \3\2")
        buf.write("\2\2\u00f1\u00f2\7k\2\2\u00f2\u00f3\7h\2\2\u00f3\"\3\2")
        buf.write("\2\2\u00f4\u00f5\7g\2\2\u00f5\u00f6\7n\2\2\u00f6\u00f7")
        buf.write("\7u\2\2\u00f7\u00f8\7g\2\2\u00f8$\3\2\2\2\u00f9\u00fa")
        buf.write("\7g\2\2\u00fa\u00fb\7n\2\2\u00fb\u00fc\7k\2\2\u00fc\u00fd")
        buf.write("\7h\2\2\u00fd&\3\2\2\2\u00fe\u00ff\7k\2\2\u00ff\u0100")
        buf.write("\7p\2\2\u0100(\3\2\2\2\u0101\u0102\7k\2\2\u0102\u0103")
        buf.write("\7p\2\2\u0103\u0104\7k\2\2\u0104\u0105\7v\2\2\u0105*\3")
        buf.write("\2\2\2\u0106\u0107\7w\2\2\u0107\u0108\7p\2\2\u0108\u0109")
        buf.write("\7v\2\2\u0109\u010a\7k\2\2\u010a\u010b\7n\2\2\u010b,\3")
        buf.write("\2\2\2\u010c\u010d\7c\2\2\u010d\u010e\7p\2\2\u010e\u010f")
        buf.write("\7f\2\2\u010f.\3\2\2\2\u0110\u0111\7q\2\2\u0111\u0112")
        buf.write("\7t\2\2\u0112\60\3\2\2\2\u0113\u0114\7p\2\2\u0114\u0115")
        buf.write("\7q\2\2\u0115\u0116\7v\2\2\u0116\62\3\2\2\2\u0117\u0118")
        buf.write("\7V\2\2\u0118\u0119\7t\2\2\u0119\u011a\7w\2\2\u011a\u011b")
        buf.write("\7g\2\2\u011b\64\3\2\2\2\u011c\u011d\7H\2\2\u011d\u011e")
        buf.write("\7c\2\2\u011e\u011f\7n\2\2\u011f\u0120\7u\2\2\u0120\u0121")
        buf.write("\7g\2\2\u0121\66\3\2\2\2\u0122\u0123\7<\2\2\u0123\u0124")
        buf.write("\7?\2\2\u01248\3\2\2\2\u0125\u0126\7?\2\2\u0126:\3\2\2")
        buf.write("\2\u0127\u0128\7,\2\2\u0128\u0129\7?\2\2\u0129<\3\2\2")
        buf.write("\2\u012a\u012b\7\61\2\2\u012b\u012c\7?\2\2\u012c>\3\2")
        buf.write("\2\2\u012d\u012e\7-\2\2\u012e\u012f\7?\2\2\u012f@\3\2")
        buf.write("\2\2\u0130\u0131\7/\2\2\u0131\u0132\7?\2\2\u0132B\3\2")
        buf.write("\2\2\u0133\u0134\7?\2\2\u0134\u0135\7?\2\2\u0135D\3\2")
        buf.write("\2\2\u0136\u0137\7@\2\2\u0137\u0138\7?\2\2\u0138F\3\2")
        buf.write("\2\2\u0139\u013a\7>\2\2\u013a\u013b\7?\2\2\u013bH\3\2")
        buf.write("\2\2\u013c\u013d\7#\2\2\u013d\u013e\7?\2\2\u013eJ\3\2")
        buf.write("\2\2\u013f\u0140\7<\2\2\u0140L\3\2\2\2\u0141\u0142\7.")
        buf.write("\2\2\u0142N\3\2\2\2\u0143\u0144\7]\2\2\u0144P\3\2\2\2")
        buf.write("\u0145\u0146\7_\2\2\u0146R\3\2\2\2\u0147\u0148\7*\2\2")
        buf.write("\u0148T\3\2\2\2\u0149\u014a\7+\2\2\u014aV\3\2\2\2\u014b")
        buf.write("\u014c\7>\2\2\u014cX\3\2\2\2\u014d\u014e\7@\2\2\u014e")
        buf.write("Z\3\2\2\2\u014f\u0150\7,\2\2\u0150\\\3\2\2\2\u0151\u0152")
        buf.write("\7\61\2\2\u0152^\3\2\2\2\u0153\u0154\7-\2\2\u0154`\3\2")
        buf.write("\2\2\u0155\u0156\7/\2\2\u0156b\3\2\2\2\u0157\u0158\7)")
        buf.write("\2\2\u0158d\3\2\2\2\u0159\u015d\5k\66\2\u015a\u015c\5")
        buf.write("m\67\2\u015b\u015a\3\2\2\2\u015c\u015f\3\2\2\2\u015d\u015b")
        buf.write("\3\2\2\2\u015d\u015e\3\2\2\2\u015ef\3\2\2\2\u015f\u015d")
        buf.write("\3\2\2\2\u0160\u0162\5o8\2\u0161\u0160\3\2\2\2\u0162\u0163")
        buf.write("\3\2\2\2\u0163\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164")
        buf.write("\u0165\3\2\2\2\u0165\u0167\7\60\2\2\u0166\u0168\5o8\2")
        buf.write("\u0167\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u0167\3")
        buf.write("\2\2\2\u0169\u016a\3\2\2\2\u016ah\3\2\2\2\u016b\u016d")
        buf.write("\5o8\2\u016c\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u016c")
        buf.write("\3\2\2\2\u016e\u016f\3\2\2\2\u016fj\3\2\2\2\u0170\u0172")
        buf.write("\t\2\2\2\u0171\u0170\3\2\2\2\u0172l\3\2\2\2\u0173\u0177")
        buf.write("\5k\66\2\u0174\u0177\5o8\2\u0175\u0177\7a\2\2\u0176\u0173")
        buf.write("\3\2\2\2\u0176\u0174\3\2\2\2\u0176\u0175\3\2\2\2\u0177")
        buf.write("n\3\2\2\2\u0178\u0179\t\3\2\2\u0179p\3\2\2\2\u017a\u017c")
        buf.write("\t\4\2\2\u017b\u017a\3\2\2\2\u017c\u017d\3\2\2\2\u017d")
        buf.write("\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017er\3\2\2\2\u017f")
        buf.write("\u0183\7%\2\2\u0180\u0182\n\5\2\2\u0181\u0180\3\2\2\2")
        buf.write("\u0182\u0185\3\2\2\2\u0183\u0181\3\2\2\2\u0183\u0184\3")
        buf.write("\2\2\2\u0184t\3\2\2\2\u0185\u0183\3\2\2\2\u0186\u0189")
        buf.write("\5q9\2\u0187\u0189\5s:\2\u0188\u0186\3\2\2\2\u0188\u0187")
        buf.write("\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018b\b;\2\2\u018b")
        buf.write("v\3\2\2\2\21\2x~\u0082\u0088\u008b\u015d\u0163\u0169\u016e")
        buf.write("\u0171\u0176\u017d\u0183\u0188\3\b\2\2")
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
    S = 16
    A = 17
    IF = 18
    ELSE = 19
    ELIF = 20
    IN = 21
    INIT = 22
    UNTIL = 23
    AND = 24
    OR = 25
    NOT = 26
    TRUE = 27
    FALSE = 28
    BIND = 29
    ASIGN = 30
    TIMES_EQ = 31
    DIV_EQ = 32
    PLUS_EQ = 33
    MINUS_EQ = 34
    EQUALS = 35
    GT_EQ = 36
    LT_EQ = 37
    NOT_EQ = 38
    COL = 39
    COM = 40
    L_BRK = 41
    R_BRK = 42
    L_PAR = 43
    R_PAR = 44
    LT = 45
    GT = 46
    TIMES = 47
    DIVIDE = 48
    PLUS = 49
    MINUS = 50
    PRIME = 51
    IDENTIFIER = 52
    DECIMAL = 53
    INTEGER = 54
    SKIP_ = 55

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Predicate'", "'Feature'", "'Factor'", "'Goal'", "'Constant'", 
            "'Action'", "'Effect'", "'Reward'", "'Policy'", "'Execute'", 
            "'Option'", "'MarkovFeature'", "'S'", "'A'", "'if'", "'else'", 
            "'elif'", "'in'", "'init'", "'until'", "'and'", "'or'", "'not'", 
            "'True'", "'False'", "':='", "'='", "'*='", "'/='", "'+='", 
            "'-='", "'=='", "'>='", "'<='", "'!='", "':'", "','", "'['", 
            "']'", "'('", "')'", "'<'", "'>'", "'*'", "'/'", "'+'", "'-'", 
            "'''" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "NL", "PREDICATE", "FEATURE", "FACTOR", 
            "GOAL", "CONSTANT", "ACTION", "EFFECT", "REWARD", "POLICY", 
            "EXECUTE", "OPTION", "MARKOVFEATURE", "S", "A", "IF", "ELSE", 
            "ELIF", "IN", "INIT", "UNTIL", "AND", "OR", "NOT", "TRUE", "FALSE", 
            "BIND", "ASIGN", "TIMES_EQ", "DIV_EQ", "PLUS_EQ", "MINUS_EQ", 
            "EQUALS", "GT_EQ", "LT_EQ", "NOT_EQ", "COL", "COM", "L_BRK", 
            "R_BRK", "L_PAR", "R_PAR", "LT", "GT", "TIMES", "DIVIDE", "PLUS", 
            "MINUS", "PRIME", "IDENTIFIER", "DECIMAL", "INTEGER", "SKIP_" ]

    ruleNames = [ "NL", "PREDICATE", "FEATURE", "FACTOR", "GOAL", "CONSTANT", 
                  "ACTION", "EFFECT", "REWARD", "POLICY", "EXECUTE", "OPTION", 
                  "MARKOVFEATURE", "S", "A", "IF", "ELSE", "ELIF", "IN", 
                  "INIT", "UNTIL", "AND", "OR", "NOT", "TRUE", "FALSE", 
                  "BIND", "ASIGN", "TIMES_EQ", "DIV_EQ", "PLUS_EQ", "MINUS_EQ", 
                  "EQUALS", "GT_EQ", "LT_EQ", "NOT_EQ", "COL", "COM", "L_BRK", 
                  "R_BRK", "L_PAR", "R_PAR", "LT", "GT", "TIMES", "DIVIDE", 
                  "PLUS", "MINUS", "PRIME", "IDENTIFIER", "DECIMAL", "INTEGER", 
                  "LETTER", "ANY_CHAR", "DIGIT", "SPACES", "COMMENT", "SKIP_" ]

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



