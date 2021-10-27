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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u01c7\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\3\2\5\2\u008b\n\2\3\2\3\2\7\2\u008f\n\2\f\2\16")
        buf.write("\2\u0092\13\2\3\2\5\2\u0095\n\2\3\2\3\2\7\2\u0099\n\2")
        buf.write("\f\2\16\2\u009c\13\2\5\2\u009e\n\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\23\3\23")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!\3!\3!\3!\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3&\3&\3&\3")
        buf.write("\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3")
        buf.write(",\3-\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3")
        buf.write("\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\3")
        buf.write("8\39\39\3:\3:\3:\7:\u018e\n:\f:\16:\u0191\13:\3;\3;\7")
        buf.write(";\u0195\n;\f;\16;\u0198\13;\3<\6<\u019b\n<\r<\16<\u019c")
        buf.write("\3<\3<\6<\u01a1\n<\r<\16<\u01a2\3=\6=\u01a6\n=\r=\16=")
        buf.write("\u01a7\3>\5>\u01ab\n>\3?\3?\3?\5?\u01b0\n?\3@\3@\3A\6")
        buf.write("A\u01b5\nA\rA\16A\u01b6\3B\3B\7B\u01bb\nB\fB\16B\u01be")
        buf.write("\13B\3C\3C\5C\u01c2\nC\3C\3C\3D\3D\2\2E\3\5\5\6\7\7\t")
        buf.write("\b\13\t\r\n\17\13\21\f\23\r\25\16\27\17\31\20\33\21\35")
        buf.write("\22\37\23!\24#\25%\26\'\27)\30+\31-\32/\33\61\34\63\35")
        buf.write("\65\36\67\379 ;!=\"?#A$C%E&G\'I(K)M*O+Q,S-U.W/Y\60[\61")
        buf.write("]\62_\63a\64c\65e\66g\67i8k9m:o;q<s=u>w?y@{\2}\2\177\2")
        buf.write("\u0081\2\u0083\2\u0085A\u0087B\3\2\6\4\2C\\c|\3\2\62;")
        buf.write("\4\2\13\13\"\"\4\2\f\f\16\17\2\u01d0\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2")
        buf.write("\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3")
        buf.write("\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W")
        buf.write("\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2")
        buf.write("a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2")
        buf.write("\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2")
        buf.write("\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2\u0085\3\2\2\2\2")
        buf.write("\u0087\3\2\2\2\3\u009d\3\2\2\2\5\u009f\3\2\2\2\7\u00a6")
        buf.write("\3\2\2\2\t\u00b0\3\2\2\2\13\u00b8\3\2\2\2\r\u00bf\3\2")
        buf.write("\2\2\17\u00c4\3\2\2\2\21\u00cd\3\2\2\2\23\u00d4\3\2\2")
        buf.write("\2\25\u00db\3\2\2\2\27\u00e2\3\2\2\2\31\u00e9\3\2\2\2")
        buf.write("\33\u00f1\3\2\2\2\35\u00f8\3\2\2\2\37\u0106\3\2\2\2!\u010c")
        buf.write("\3\2\2\2#\u010f\3\2\2\2%\u0111\3\2\2\2\'\u0113\3\2\2\2")
        buf.write(")\u0115\3\2\2\2+\u0117\3\2\2\2-\u011a\3\2\2\2/\u011f\3")
        buf.write("\2\2\2\61\u0124\3\2\2\2\63\u0127\3\2\2\2\65\u012c\3\2")
        buf.write("\2\2\67\u0132\3\2\2\29\u0137\3\2\2\2;\u013c\3\2\2\2=\u0140")
        buf.write("\3\2\2\2?\u0143\3\2\2\2A\u0147\3\2\2\2C\u014c\3\2\2\2")
        buf.write("E\u0152\3\2\2\2G\u0155\3\2\2\2I\u0158\3\2\2\2K\u015a\3")
        buf.write("\2\2\2M\u015d\3\2\2\2O\u0160\3\2\2\2Q\u0163\3\2\2\2S\u0166")
        buf.write("\3\2\2\2U\u0169\3\2\2\2W\u016c\3\2\2\2Y\u016f\3\2\2\2")
        buf.write("[\u0172\3\2\2\2]\u0174\3\2\2\2_\u0176\3\2\2\2a\u0178\3")
        buf.write("\2\2\2c\u017a\3\2\2\2e\u017c\3\2\2\2g\u017e\3\2\2\2i\u0180")
        buf.write("\3\2\2\2k\u0182\3\2\2\2m\u0184\3\2\2\2o\u0186\3\2\2\2")
        buf.write("q\u0188\3\2\2\2s\u018a\3\2\2\2u\u0192\3\2\2\2w\u019a\3")
        buf.write("\2\2\2y\u01a5\3\2\2\2{\u01aa\3\2\2\2}\u01af\3\2\2\2\177")
        buf.write("\u01b1\3\2\2\2\u0081\u01b4\3\2\2\2\u0083\u01b8\3\2\2\2")
        buf.write("\u0085\u01c1\3\2\2\2\u0087\u01c5\3\2\2\2\u0089\u008b\7")
        buf.write("\17\2\2\u008a\u0089\3\2\2\2\u008a\u008b\3\2\2\2\u008b")
        buf.write("\u008c\3\2\2\2\u008c\u0090\7\f\2\2\u008d\u008f\7\"\2\2")
        buf.write("\u008e\u008d\3\2\2\2\u008f\u0092\3\2\2\2\u0090\u008e\3")
        buf.write("\2\2\2\u0090\u0091\3\2\2\2\u0091\u009e\3\2\2\2\u0092\u0090")
        buf.write("\3\2\2\2\u0093\u0095\7\17\2\2\u0094\u0093\3\2\2\2\u0094")
        buf.write("\u0095\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u009a\7\f\2\2")
        buf.write("\u0097\u0099\7\13\2\2\u0098\u0097\3\2\2\2\u0099\u009c")
        buf.write("\3\2\2\2\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b")
        buf.write("\u009e\3\2\2\2\u009c\u009a\3\2\2\2\u009d\u008a\3\2\2\2")
        buf.write("\u009d\u0094\3\2\2\2\u009e\4\3\2\2\2\u009f\u00a0\7k\2")
        buf.write("\2\u00a0\u00a1\7o\2\2\u00a1\u00a2\7r\2\2\u00a2\u00a3\7")
        buf.write("q\2\2\u00a3\u00a4\7t\2\2\u00a4\u00a5\7v\2\2\u00a5\6\3")
        buf.write("\2\2\2\u00a6\u00a7\7R\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9")
        buf.write("\7g\2\2\u00a9\u00aa\7f\2\2\u00aa\u00ab\7k\2\2\u00ab\u00ac")
        buf.write("\7e\2\2\u00ac\u00ad\7c\2\2\u00ad\u00ae\7v\2\2\u00ae\u00af")
        buf.write("\7g\2\2\u00af\b\3\2\2\2\u00b0\u00b1\7H\2\2\u00b1\u00b2")
        buf.write("\7g\2\2\u00b2\u00b3\7c\2\2\u00b3\u00b4\7v\2\2\u00b4\u00b5")
        buf.write("\7w\2\2\u00b5\u00b6\7t\2\2\u00b6\u00b7\7g\2\2\u00b7\n")
        buf.write("\3\2\2\2\u00b8\u00b9\7H\2\2\u00b9\u00ba\7c\2\2\u00ba\u00bb")
        buf.write("\7e\2\2\u00bb\u00bc\7v\2\2\u00bc\u00bd\7q\2\2\u00bd\u00be")
        buf.write("\7t\2\2\u00be\f\3\2\2\2\u00bf\u00c0\7I\2\2\u00c0\u00c1")
        buf.write("\7q\2\2\u00c1\u00c2\7c\2\2\u00c2\u00c3\7n\2\2\u00c3\16")
        buf.write("\3\2\2\2\u00c4\u00c5\7E\2\2\u00c5\u00c6\7q\2\2\u00c6\u00c7")
        buf.write("\7p\2\2\u00c7\u00c8\7u\2\2\u00c8\u00c9\7v\2\2\u00c9\u00ca")
        buf.write("\7c\2\2\u00ca\u00cb\7p\2\2\u00cb\u00cc\7v\2\2\u00cc\20")
        buf.write("\3\2\2\2\u00cd\u00ce\7C\2\2\u00ce\u00cf\7e\2\2\u00cf\u00d0")
        buf.write("\7v\2\2\u00d0\u00d1\7k\2\2\u00d1\u00d2\7q\2\2\u00d2\u00d3")
        buf.write("\7p\2\2\u00d3\22\3\2\2\2\u00d4\u00d5\7G\2\2\u00d5\u00d6")
        buf.write("\7h\2\2\u00d6\u00d7\7h\2\2\u00d7\u00d8\7g\2\2\u00d8\u00d9")
        buf.write("\7e\2\2\u00d9\u00da\7v\2\2\u00da\24\3\2\2\2\u00db\u00dc")
        buf.write("\7T\2\2\u00dc\u00dd\7g\2\2\u00dd\u00de\7y\2\2\u00de\u00df")
        buf.write("\7c\2\2\u00df\u00e0\7t\2\2\u00e0\u00e1\7f\2\2\u00e1\26")
        buf.write("\3\2\2\2\u00e2\u00e3\7R\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5")
        buf.write("\7n\2\2\u00e5\u00e6\7k\2\2\u00e6\u00e7\7e\2\2\u00e7\u00e8")
        buf.write("\7{\2\2\u00e8\30\3\2\2\2\u00e9\u00ea\7G\2\2\u00ea\u00eb")
        buf.write("\7z\2\2\u00eb\u00ec\7g\2\2\u00ec\u00ed\7e\2\2\u00ed\u00ee")
        buf.write("\7w\2\2\u00ee\u00ef\7v\2\2\u00ef\u00f0\7g\2\2\u00f0\32")
        buf.write("\3\2\2\2\u00f1\u00f2\7Q\2\2\u00f2\u00f3\7r\2\2\u00f3\u00f4")
        buf.write("\7v\2\2\u00f4\u00f5\7k\2\2\u00f5\u00f6\7q\2\2\u00f6\u00f7")
        buf.write("\7p\2\2\u00f7\34\3\2\2\2\u00f8\u00f9\7O\2\2\u00f9\u00fa")
        buf.write("\7c\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc\7m\2\2\u00fc\u00fd")
        buf.write("\7q\2\2\u00fd\u00fe\7x\2\2\u00fe\u00ff\7H\2\2\u00ff\u0100")
        buf.write("\7g\2\2\u0100\u0101\7c\2\2\u0101\u0102\7v\2\2\u0102\u0103")
        buf.write("\7w\2\2\u0103\u0104\7t\2\2\u0104\u0105\7g\2\2\u0105\36")
        buf.write("\3\2\2\2\u0106\u0107\7P\2\2\u0107\u0108\7g\2\2\u0108\u0109")
        buf.write("\7x\2\2\u0109\u010a\7g\2\2\u010a\u010b\7t\2\2\u010b \3")
        buf.write("\2\2\2\u010c\u010d\5#\22\2\u010d\u010e\5)\25\2\u010e\"")
        buf.write("\3\2\2\2\u010f\u0110\7U\2\2\u0110$\3\2\2\2\u0111\u0112")
        buf.write("\7C\2\2\u0112&\3\2\2\2\u0113\u0114\7R\2\2\u0114(\3\2\2")
        buf.write("\2\u0115\u0116\7)\2\2\u0116*\3\2\2\2\u0117\u0118\7k\2")
        buf.write("\2\u0118\u0119\7h\2\2\u0119,\3\2\2\2\u011a\u011b\7g\2")
        buf.write("\2\u011b\u011c\7n\2\2\u011c\u011d\7u\2\2\u011d\u011e\7")
        buf.write("g\2\2\u011e.\3\2\2\2\u011f\u0120\7g\2\2\u0120\u0121\7")
        buf.write("n\2\2\u0121\u0122\7k\2\2\u0122\u0123\7h\2\2\u0123\60\3")
        buf.write("\2\2\2\u0124\u0125\7k\2\2\u0125\u0126\7p\2\2\u0126\62")
        buf.write("\3\2\2\2\u0127\u0128\7k\2\2\u0128\u0129\7p\2\2\u0129\u012a")
        buf.write("\7k\2\2\u012a\u012b\7v\2\2\u012b\64\3\2\2\2\u012c\u012d")
        buf.write("\7w\2\2\u012d\u012e\7p\2\2\u012e\u012f\7v\2\2\u012f\u0130")
        buf.write("\7k\2\2\u0130\u0131\7n\2\2\u0131\66\3\2\2\2\u0132\u0133")
        buf.write("\7y\2\2\u0133\u0134\7k\2\2\u0134\u0135\7v\2\2\u0135\u0136")
        buf.write("\7j\2\2\u01368\3\2\2\2\u0137\u0138\7v\2\2\u0138\u0139")
        buf.write("\7j\2\2\u0139\u013a\7g\2\2\u013a\u013b\7p\2\2\u013b:\3")
        buf.write("\2\2\2\u013c\u013d\7c\2\2\u013d\u013e\7p\2\2\u013e\u013f")
        buf.write("\7f\2\2\u013f<\3\2\2\2\u0140\u0141\7q\2\2\u0141\u0142")
        buf.write("\7t\2\2\u0142>\3\2\2\2\u0143\u0144\7p\2\2\u0144\u0145")
        buf.write("\7q\2\2\u0145\u0146\7v\2\2\u0146@\3\2\2\2\u0147\u0148")
        buf.write("\7V\2\2\u0148\u0149\7t\2\2\u0149\u014a\7w\2\2\u014a\u014b")
        buf.write("\7g\2\2\u014bB\3\2\2\2\u014c\u014d\7H\2\2\u014d\u014e")
        buf.write("\7c\2\2\u014e\u014f\7n\2\2\u014f\u0150\7u\2\2\u0150\u0151")
        buf.write("\7g\2\2\u0151D\3\2\2\2\u0152\u0153\7<\2\2\u0153\u0154")
        buf.write("\7?\2\2\u0154F\3\2\2\2\u0155\u0156\7/\2\2\u0156\u0157")
        buf.write("\7@\2\2\u0157H\3\2\2\2\u0158\u0159\7?\2\2\u0159J\3\2\2")
        buf.write("\2\u015a\u015b\7,\2\2\u015b\u015c\7?\2\2\u015cL\3\2\2")
        buf.write("\2\u015d\u015e\7\61\2\2\u015e\u015f\7?\2\2\u015fN\3\2")
        buf.write("\2\2\u0160\u0161\7-\2\2\u0161\u0162\7?\2\2\u0162P\3\2")
        buf.write("\2\2\u0163\u0164\7/\2\2\u0164\u0165\7?\2\2\u0165R\3\2")
        buf.write("\2\2\u0166\u0167\7?\2\2\u0167\u0168\7?\2\2\u0168T\3\2")
        buf.write("\2\2\u0169\u016a\7@\2\2\u016a\u016b\7?\2\2\u016bV\3\2")
        buf.write("\2\2\u016c\u016d\7>\2\2\u016d\u016e\7?\2\2\u016eX\3\2")
        buf.write("\2\2\u016f\u0170\7#\2\2\u0170\u0171\7?\2\2\u0171Z\3\2")
        buf.write("\2\2\u0172\u0173\7<\2\2\u0173\\\3\2\2\2\u0174\u0175\7")
        buf.write(".\2\2\u0175^\3\2\2\2\u0176\u0177\7]\2\2\u0177`\3\2\2\2")
        buf.write("\u0178\u0179\7_\2\2\u0179b\3\2\2\2\u017a\u017b\7*\2\2")
        buf.write("\u017bd\3\2\2\2\u017c\u017d\7+\2\2\u017df\3\2\2\2\u017e")
        buf.write("\u017f\7>\2\2\u017fh\3\2\2\2\u0180\u0181\7@\2\2\u0181")
        buf.write("j\3\2\2\2\u0182\u0183\7,\2\2\u0183l\3\2\2\2\u0184\u0185")
        buf.write("\7\61\2\2\u0185n\3\2\2\2\u0186\u0187\7-\2\2\u0187p\3\2")
        buf.write("\2\2\u0188\u0189\7/\2\2\u0189r\3\2\2\2\u018a\u018b\5u")
        buf.write(";\2\u018b\u018f\7\60\2\2\u018c\u018e\5{>\2\u018d\u018c")
        buf.write("\3\2\2\2\u018e\u0191\3\2\2\2\u018f\u018d\3\2\2\2\u018f")
        buf.write("\u0190\3\2\2\2\u0190t\3\2\2\2\u0191\u018f\3\2\2\2\u0192")
        buf.write("\u0196\5{>\2\u0193\u0195\5}?\2\u0194\u0193\3\2\2\2\u0195")
        buf.write("\u0198\3\2\2\2\u0196\u0194\3\2\2\2\u0196\u0197\3\2\2\2")
        buf.write("\u0197v\3\2\2\2\u0198\u0196\3\2\2\2\u0199\u019b\5\177")
        buf.write("@\2\u019a\u0199\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u019a")
        buf.write("\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u019e\3\2\2\2\u019e")
        buf.write("\u01a0\7\60\2\2\u019f\u01a1\5\177@\2\u01a0\u019f\3\2\2")
        buf.write("\2\u01a1\u01a2\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3")
        buf.write("\3\2\2\2\u01a3x\3\2\2\2\u01a4\u01a6\5\177@\2\u01a5\u01a4")
        buf.write("\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7")
        buf.write("\u01a8\3\2\2\2\u01a8z\3\2\2\2\u01a9\u01ab\t\2\2\2\u01aa")
        buf.write("\u01a9\3\2\2\2\u01ab|\3\2\2\2\u01ac\u01b0\5{>\2\u01ad")
        buf.write("\u01b0\5\177@\2\u01ae\u01b0\7a\2\2\u01af\u01ac\3\2\2\2")
        buf.write("\u01af\u01ad\3\2\2\2\u01af\u01ae\3\2\2\2\u01b0~\3\2\2")
        buf.write("\2\u01b1\u01b2\t\3\2\2\u01b2\u0080\3\2\2\2\u01b3\u01b5")
        buf.write("\t\4\2\2\u01b4\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6")
        buf.write("\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u0082\3\2\2\2")
        buf.write("\u01b8\u01bc\7%\2\2\u01b9\u01bb\n\5\2\2\u01ba\u01b9\3")
        buf.write("\2\2\2\u01bb\u01be\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc\u01bd")
        buf.write("\3\2\2\2\u01bd\u0084\3\2\2\2\u01be\u01bc\3\2\2\2\u01bf")
        buf.write("\u01c2\5\u0081A\2\u01c0\u01c2\5\u0083B\2\u01c1\u01bf\3")
        buf.write("\2\2\2\u01c1\u01c0\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3\u01c4")
        buf.write("\bC\2\2\u01c4\u0086\3\2\2\2\u01c5\u01c6\13\2\2\2\u01c6")
        buf.write("\u0088\3\2\2\2\22\2\u008a\u0090\u0094\u009a\u009d\u018f")
        buf.write("\u0196\u019c\u01a2\u01a7\u01aa\u01af\u01b6\u01bc\u01c1")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class RLangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INDENT = 1
    DEDENT = 2
    NL = 3
    IMPORT = 4
    PREDICATE = 5
    FEATURE = 6
    FACTOR = 7
    GOAL = 8
    CONSTANT = 9
    ACTION = 10
    EFFECT = 11
    REWARD = 12
    POLICY = 13
    EXECUTE = 14
    OPTION = 15
    MARKOVFEATURE = 16
    NEVER = 17
    S_PRIME = 18
    S = 19
    A = 20
    P = 21
    PRIME = 22
    IF = 23
    ELSE = 24
    ELIF = 25
    IN = 26
    INIT = 27
    UNTIL = 28
    WITH = 29
    THEN = 30
    AND = 31
    OR = 32
    NOT = 33
    TRUE = 34
    FALSE = 35
    BIND = 36
    PREDICT = 37
    ASSIGN = 38
    TIMES_EQ = 39
    DIV_EQ = 40
    PLUS_EQ = 41
    MINUS_EQ = 42
    EQ_TO = 43
    GT_EQ = 44
    LT_EQ = 45
    NOT_EQ = 46
    COL = 47
    COM = 48
    L_BRK = 49
    R_BRK = 50
    L_PAR = 51
    R_PAR = 52
    LT = 53
    GT = 54
    TIMES = 55
    DIVIDE = 56
    PLUS = 57
    MINUS = 58
    FNAME = 59
    IDENTIFIER = 60
    DECIMAL = 61
    INTEGER = 62
    SKIP_ = 63
    ANY = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'import'", "'Predicate'", "'Feature'", "'Factor'", "'Goal'", 
            "'Constant'", "'Action'", "'Effect'", "'Reward'", "'Policy'", 
            "'Execute'", "'Option'", "'MarkovFeature'", "'Never'", "'S'", 
            "'A'", "'P'", "'''", "'if'", "'else'", "'elif'", "'in'", "'init'", 
            "'until'", "'with'", "'then'", "'and'", "'or'", "'not'", "'True'", 
            "'False'", "':='", "'->'", "'='", "'*='", "'/='", "'+='", "'-='", 
            "'=='", "'>='", "'<='", "'!='", "':'", "','", "'['", "']'", 
            "'('", "')'", "'<'", "'>'", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "NL", "IMPORT", "PREDICATE", "FEATURE", 
            "FACTOR", "GOAL", "CONSTANT", "ACTION", "EFFECT", "REWARD", 
            "POLICY", "EXECUTE", "OPTION", "MARKOVFEATURE", "NEVER", "S_PRIME", 
            "S", "A", "P", "PRIME", "IF", "ELSE", "ELIF", "IN", "INIT", 
            "UNTIL", "WITH", "THEN", "AND", "OR", "NOT", "TRUE", "FALSE", 
            "BIND", "PREDICT", "ASSIGN", "TIMES_EQ", "DIV_EQ", "PLUS_EQ", 
            "MINUS_EQ", "EQ_TO", "GT_EQ", "LT_EQ", "NOT_EQ", "COL", "COM", 
            "L_BRK", "R_BRK", "L_PAR", "R_PAR", "LT", "GT", "TIMES", "DIVIDE", 
            "PLUS", "MINUS", "FNAME", "IDENTIFIER", "DECIMAL", "INTEGER", 
            "SKIP_", "ANY" ]

    ruleNames = [ "NL", "IMPORT", "PREDICATE", "FEATURE", "FACTOR", "GOAL", 
                  "CONSTANT", "ACTION", "EFFECT", "REWARD", "POLICY", "EXECUTE", 
                  "OPTION", "MARKOVFEATURE", "NEVER", "S_PRIME", "S", "A", 
                  "P", "PRIME", "IF", "ELSE", "ELIF", "IN", "INIT", "UNTIL", 
                  "WITH", "THEN", "AND", "OR", "NOT", "TRUE", "FALSE", "BIND", 
                  "PREDICT", "ASSIGN", "TIMES_EQ", "DIV_EQ", "PLUS_EQ", 
                  "MINUS_EQ", "EQ_TO", "GT_EQ", "LT_EQ", "NOT_EQ", "COL", 
                  "COM", "L_BRK", "R_BRK", "L_PAR", "R_PAR", "LT", "GT", 
                  "TIMES", "DIVIDE", "PLUS", "MINUS", "FNAME", "IDENTIFIER", 
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



