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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u01cd\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\5\2\u008d\n\2\3\2\3\2\7\2\u0091\n\2")
        buf.write("\f\2\16\2\u0094\13\2\3\2\5\2\u0097\n\2\3\2\3\2\7\2\u009b")
        buf.write("\n\2\f\2\16\2\u009e\13\2\5\2\u00a0\n\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\23\3\23")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!\3!\3!\3!\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3")
        buf.write("&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3")
        buf.write(",\3,\3-\3-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62")
        buf.write("\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67")
        buf.write("\38\38\39\39\3:\3:\3;\3;\3;\7;\u0194\n;\f;\16;\u0197\13")
        buf.write(";\3<\3<\7<\u019b\n<\f<\16<\u019e\13<\3=\6=\u01a1\n=\r")
        buf.write("=\16=\u01a2\3=\3=\6=\u01a7\n=\r=\16=\u01a8\3>\6>\u01ac")
        buf.write("\n>\r>\16>\u01ad\3?\5?\u01b1\n?\3@\3@\3@\5@\u01b6\n@\3")
        buf.write("A\3A\3B\6B\u01bb\nB\rB\16B\u01bc\3C\3C\7C\u01c1\nC\fC")
        buf.write("\16C\u01c4\13C\3D\3D\5D\u01c8\nD\3D\3D\3E\3E\2\2F\3\5")
        buf.write("\5\6\7\7\t\b\13\t\r\n\17\13\21\f\23\r\25\16\27\17\31\20")
        buf.write("\33\21\35\22\37\23!\24#\25%\26\'\27)\30+\31-\32/\33\61")
        buf.write("\34\63\35\65\36\67\379 ;!=\"?#A$C%E&G\'I(K)M*O+Q,S-U.")
        buf.write("W/Y\60[\61]\62_\63a\64c\65e\66g\67i8k9m:o;q<s=u>w?y@{")
        buf.write("A}\2\177\2\u0081\2\u0083\2\u0085\2\u0087B\u0089C\3\2\6")
        buf.write("\4\2C\\c|\3\2\62;\4\2\13\13\"\"\4\2\f\f\16\17\2\u01d6")
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
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\3\u009f\3\2")
        buf.write("\2\2\5\u00a1\3\2\2\2\7\u00a8\3\2\2\2\t\u00b2\3\2\2\2\13")
        buf.write("\u00ba\3\2\2\2\r\u00c1\3\2\2\2\17\u00c6\3\2\2\2\21\u00cf")
        buf.write("\3\2\2\2\23\u00d6\3\2\2\2\25\u00dd\3\2\2\2\27\u00e4\3")
        buf.write("\2\2\2\31\u00eb\3\2\2\2\33\u00f3\3\2\2\2\35\u00fa\3\2")
        buf.write("\2\2\37\u0108\3\2\2\2!\u010e\3\2\2\2#\u0111\3\2\2\2%\u0113")
        buf.write("\3\2\2\2\'\u0115\3\2\2\2)\u0117\3\2\2\2+\u0119\3\2\2\2")
        buf.write("-\u011c\3\2\2\2/\u0121\3\2\2\2\61\u0126\3\2\2\2\63\u0129")
        buf.write("\3\2\2\2\65\u012e\3\2\2\2\67\u0134\3\2\2\29\u0139\3\2")
        buf.write("\2\2;\u013e\3\2\2\2=\u0142\3\2\2\2?\u0145\3\2\2\2A\u0149")
        buf.write("\3\2\2\2C\u014e\3\2\2\2E\u0154\3\2\2\2G\u0158\3\2\2\2")
        buf.write("I\u015b\3\2\2\2K\u015e\3\2\2\2M\u0160\3\2\2\2O\u0163\3")
        buf.write("\2\2\2Q\u0166\3\2\2\2S\u0169\3\2\2\2U\u016c\3\2\2\2W\u016f")
        buf.write("\3\2\2\2Y\u0172\3\2\2\2[\u0175\3\2\2\2]\u0178\3\2\2\2")
        buf.write("_\u017a\3\2\2\2a\u017c\3\2\2\2c\u017e\3\2\2\2e\u0180\3")
        buf.write("\2\2\2g\u0182\3\2\2\2i\u0184\3\2\2\2k\u0186\3\2\2\2m\u0188")
        buf.write("\3\2\2\2o\u018a\3\2\2\2q\u018c\3\2\2\2s\u018e\3\2\2\2")
        buf.write("u\u0190\3\2\2\2w\u0198\3\2\2\2y\u01a0\3\2\2\2{\u01ab\3")
        buf.write("\2\2\2}\u01b0\3\2\2\2\177\u01b5\3\2\2\2\u0081\u01b7\3")
        buf.write("\2\2\2\u0083\u01ba\3\2\2\2\u0085\u01be\3\2\2\2\u0087\u01c7")
        buf.write("\3\2\2\2\u0089\u01cb\3\2\2\2\u008b\u008d\7\17\2\2\u008c")
        buf.write("\u008b\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008e\3\2\2\2")
        buf.write("\u008e\u0092\7\f\2\2\u008f\u0091\7\"\2\2\u0090\u008f\3")
        buf.write("\2\2\2\u0091\u0094\3\2\2\2\u0092\u0090\3\2\2\2\u0092\u0093")
        buf.write("\3\2\2\2\u0093\u00a0\3\2\2\2\u0094\u0092\3\2\2\2\u0095")
        buf.write("\u0097\7\17\2\2\u0096\u0095\3\2\2\2\u0096\u0097\3\2\2")
        buf.write("\2\u0097\u0098\3\2\2\2\u0098\u009c\7\f\2\2\u0099\u009b")
        buf.write("\7\13\2\2\u009a\u0099\3\2\2\2\u009b\u009e\3\2\2\2\u009c")
        buf.write("\u009a\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u00a0\3\2\2\2")
        buf.write("\u009e\u009c\3\2\2\2\u009f\u008c\3\2\2\2\u009f\u0096\3")
        buf.write("\2\2\2\u00a0\4\3\2\2\2\u00a1\u00a2\7k\2\2\u00a2\u00a3")
        buf.write("\7o\2\2\u00a3\u00a4\7r\2\2\u00a4\u00a5\7q\2\2\u00a5\u00a6")
        buf.write("\7t\2\2\u00a6\u00a7\7v\2\2\u00a7\6\3\2\2\2\u00a8\u00a9")
        buf.write("\7R\2\2\u00a9\u00aa\7t\2\2\u00aa\u00ab\7g\2\2\u00ab\u00ac")
        buf.write("\7f\2\2\u00ac\u00ad\7k\2\2\u00ad\u00ae\7e\2\2\u00ae\u00af")
        buf.write("\7c\2\2\u00af\u00b0\7v\2\2\u00b0\u00b1\7g\2\2\u00b1\b")
        buf.write("\3\2\2\2\u00b2\u00b3\7H\2\2\u00b3\u00b4\7g\2\2\u00b4\u00b5")
        buf.write("\7c\2\2\u00b5\u00b6\7v\2\2\u00b6\u00b7\7w\2\2\u00b7\u00b8")
        buf.write("\7t\2\2\u00b8\u00b9\7g\2\2\u00b9\n\3\2\2\2\u00ba\u00bb")
        buf.write("\7H\2\2\u00bb\u00bc\7c\2\2\u00bc\u00bd\7e\2\2\u00bd\u00be")
        buf.write("\7v\2\2\u00be\u00bf\7q\2\2\u00bf\u00c0\7t\2\2\u00c0\f")
        buf.write("\3\2\2\2\u00c1\u00c2\7I\2\2\u00c2\u00c3\7q\2\2\u00c3\u00c4")
        buf.write("\7c\2\2\u00c4\u00c5\7n\2\2\u00c5\16\3\2\2\2\u00c6\u00c7")
        buf.write("\7E\2\2\u00c7\u00c8\7q\2\2\u00c8\u00c9\7p\2\2\u00c9\u00ca")
        buf.write("\7u\2\2\u00ca\u00cb\7v\2\2\u00cb\u00cc\7c\2\2\u00cc\u00cd")
        buf.write("\7p\2\2\u00cd\u00ce\7v\2\2\u00ce\20\3\2\2\2\u00cf\u00d0")
        buf.write("\7C\2\2\u00d0\u00d1\7e\2\2\u00d1\u00d2\7v\2\2\u00d2\u00d3")
        buf.write("\7k\2\2\u00d3\u00d4\7q\2\2\u00d4\u00d5\7p\2\2\u00d5\22")
        buf.write("\3\2\2\2\u00d6\u00d7\7G\2\2\u00d7\u00d8\7h\2\2\u00d8\u00d9")
        buf.write("\7h\2\2\u00d9\u00da\7g\2\2\u00da\u00db\7e\2\2\u00db\u00dc")
        buf.write("\7v\2\2\u00dc\24\3\2\2\2\u00dd\u00de\7T\2\2\u00de\u00df")
        buf.write("\7g\2\2\u00df\u00e0\7y\2\2\u00e0\u00e1\7c\2\2\u00e1\u00e2")
        buf.write("\7t\2\2\u00e2\u00e3\7f\2\2\u00e3\26\3\2\2\2\u00e4\u00e5")
        buf.write("\7R\2\2\u00e5\u00e6\7q\2\2\u00e6\u00e7\7n\2\2\u00e7\u00e8")
        buf.write("\7k\2\2\u00e8\u00e9\7e\2\2\u00e9\u00ea\7{\2\2\u00ea\30")
        buf.write("\3\2\2\2\u00eb\u00ec\7G\2\2\u00ec\u00ed\7z\2\2\u00ed\u00ee")
        buf.write("\7g\2\2\u00ee\u00ef\7e\2\2\u00ef\u00f0\7w\2\2\u00f0\u00f1")
        buf.write("\7v\2\2\u00f1\u00f2\7g\2\2\u00f2\32\3\2\2\2\u00f3\u00f4")
        buf.write("\7Q\2\2\u00f4\u00f5\7r\2\2\u00f5\u00f6\7v\2\2\u00f6\u00f7")
        buf.write("\7k\2\2\u00f7\u00f8\7q\2\2\u00f8\u00f9\7p\2\2\u00f9\34")
        buf.write("\3\2\2\2\u00fa\u00fb\7O\2\2\u00fb\u00fc\7c\2\2\u00fc\u00fd")
        buf.write("\7t\2\2\u00fd\u00fe\7m\2\2\u00fe\u00ff\7q\2\2\u00ff\u0100")
        buf.write("\7x\2\2\u0100\u0101\7H\2\2\u0101\u0102\7g\2\2\u0102\u0103")
        buf.write("\7c\2\2\u0103\u0104\7v\2\2\u0104\u0105\7w\2\2\u0105\u0106")
        buf.write("\7t\2\2\u0106\u0107\7g\2\2\u0107\36\3\2\2\2\u0108\u0109")
        buf.write("\7P\2\2\u0109\u010a\7g\2\2\u010a\u010b\7x\2\2\u010b\u010c")
        buf.write("\7g\2\2\u010c\u010d\7t\2\2\u010d \3\2\2\2\u010e\u010f")
        buf.write("\5#\22\2\u010f\u0110\5)\25\2\u0110\"\3\2\2\2\u0111\u0112")
        buf.write("\7U\2\2\u0112$\3\2\2\2\u0113\u0114\7C\2\2\u0114&\3\2\2")
        buf.write("\2\u0115\u0116\7R\2\2\u0116(\3\2\2\2\u0117\u0118\7)\2")
        buf.write("\2\u0118*\3\2\2\2\u0119\u011a\7k\2\2\u011a\u011b\7h\2")
        buf.write("\2\u011b,\3\2\2\2\u011c\u011d\7g\2\2\u011d\u011e\7n\2")
        buf.write("\2\u011e\u011f\7u\2\2\u011f\u0120\7g\2\2\u0120.\3\2\2")
        buf.write("\2\u0121\u0122\7g\2\2\u0122\u0123\7n\2\2\u0123\u0124\7")
        buf.write("k\2\2\u0124\u0125\7h\2\2\u0125\60\3\2\2\2\u0126\u0127")
        buf.write("\7k\2\2\u0127\u0128\7p\2\2\u0128\62\3\2\2\2\u0129\u012a")
        buf.write("\7k\2\2\u012a\u012b\7p\2\2\u012b\u012c\7k\2\2\u012c\u012d")
        buf.write("\7v\2\2\u012d\64\3\2\2\2\u012e\u012f\7w\2\2\u012f\u0130")
        buf.write("\7p\2\2\u0130\u0131\7v\2\2\u0131\u0132\7k\2\2\u0132\u0133")
        buf.write("\7n\2\2\u0133\66\3\2\2\2\u0134\u0135\7y\2\2\u0135\u0136")
        buf.write("\7k\2\2\u0136\u0137\7v\2\2\u0137\u0138\7j\2\2\u01388\3")
        buf.write("\2\2\2\u0139\u013a\7v\2\2\u013a\u013b\7j\2\2\u013b\u013c")
        buf.write("\7g\2\2\u013c\u013d\7p\2\2\u013d:\3\2\2\2\u013e\u013f")
        buf.write("\7c\2\2\u013f\u0140\7p\2\2\u0140\u0141\7f\2\2\u0141<\3")
        buf.write("\2\2\2\u0142\u0143\7q\2\2\u0143\u0144\7t\2\2\u0144>\3")
        buf.write("\2\2\2\u0145\u0146\7p\2\2\u0146\u0147\7q\2\2\u0147\u0148")
        buf.write("\7v\2\2\u0148@\3\2\2\2\u0149\u014a\7V\2\2\u014a\u014b")
        buf.write("\7t\2\2\u014b\u014c\7w\2\2\u014c\u014d\7g\2\2\u014dB\3")
        buf.write("\2\2\2\u014e\u014f\7H\2\2\u014f\u0150\7c\2\2\u0150\u0151")
        buf.write("\7n\2\2\u0151\u0152\7u\2\2\u0152\u0153\7g\2\2\u0153D\3")
        buf.write("\2\2\2\u0154\u0155\7C\2\2\u0155\u0156\7p\2\2\u0156\u0157")
        buf.write("\7{\2\2\u0157F\3\2\2\2\u0158\u0159\7<\2\2\u0159\u015a")
        buf.write("\7?\2\2\u015aH\3\2\2\2\u015b\u015c\7/\2\2\u015c\u015d")
        buf.write("\7@\2\2\u015dJ\3\2\2\2\u015e\u015f\7?\2\2\u015fL\3\2\2")
        buf.write("\2\u0160\u0161\7,\2\2\u0161\u0162\7?\2\2\u0162N\3\2\2")
        buf.write("\2\u0163\u0164\7\61\2\2\u0164\u0165\7?\2\2\u0165P\3\2")
        buf.write("\2\2\u0166\u0167\7-\2\2\u0167\u0168\7?\2\2\u0168R\3\2")
        buf.write("\2\2\u0169\u016a\7/\2\2\u016a\u016b\7?\2\2\u016bT\3\2")
        buf.write("\2\2\u016c\u016d\7?\2\2\u016d\u016e\7?\2\2\u016eV\3\2")
        buf.write("\2\2\u016f\u0170\7@\2\2\u0170\u0171\7?\2\2\u0171X\3\2")
        buf.write("\2\2\u0172\u0173\7>\2\2\u0173\u0174\7?\2\2\u0174Z\3\2")
        buf.write("\2\2\u0175\u0176\7#\2\2\u0176\u0177\7?\2\2\u0177\\\3\2")
        buf.write("\2\2\u0178\u0179\7<\2\2\u0179^\3\2\2\2\u017a\u017b\7.")
        buf.write("\2\2\u017b`\3\2\2\2\u017c\u017d\7]\2\2\u017db\3\2\2\2")
        buf.write("\u017e\u017f\7_\2\2\u017fd\3\2\2\2\u0180\u0181\7*\2\2")
        buf.write("\u0181f\3\2\2\2\u0182\u0183\7+\2\2\u0183h\3\2\2\2\u0184")
        buf.write("\u0185\7>\2\2\u0185j\3\2\2\2\u0186\u0187\7@\2\2\u0187")
        buf.write("l\3\2\2\2\u0188\u0189\7,\2\2\u0189n\3\2\2\2\u018a\u018b")
        buf.write("\7\61\2\2\u018bp\3\2\2\2\u018c\u018d\7-\2\2\u018dr\3\2")
        buf.write("\2\2\u018e\u018f\7/\2\2\u018ft\3\2\2\2\u0190\u0191\5w")
        buf.write("<\2\u0191\u0195\7\60\2\2\u0192\u0194\5}?\2\u0193\u0192")
        buf.write("\3\2\2\2\u0194\u0197\3\2\2\2\u0195\u0193\3\2\2\2\u0195")
        buf.write("\u0196\3\2\2\2\u0196v\3\2\2\2\u0197\u0195\3\2\2\2\u0198")
        buf.write("\u019c\5}?\2\u0199\u019b\5\177@\2\u019a\u0199\3\2\2\2")
        buf.write("\u019b\u019e\3\2\2\2\u019c\u019a\3\2\2\2\u019c\u019d\3")
        buf.write("\2\2\2\u019dx\3\2\2\2\u019e\u019c\3\2\2\2\u019f\u01a1")
        buf.write("\5\u0081A\2\u01a0\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2")
        buf.write("\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a4\3\2\2\2")
        buf.write("\u01a4\u01a6\7\60\2\2\u01a5\u01a7\5\u0081A\2\u01a6\u01a5")
        buf.write("\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8")
        buf.write("\u01a9\3\2\2\2\u01a9z\3\2\2\2\u01aa\u01ac\5\u0081A\2\u01ab")
        buf.write("\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01ab\3\2\2\2")
        buf.write("\u01ad\u01ae\3\2\2\2\u01ae|\3\2\2\2\u01af\u01b1\t\2\2")
        buf.write("\2\u01b0\u01af\3\2\2\2\u01b1~\3\2\2\2\u01b2\u01b6\5}?")
        buf.write("\2\u01b3\u01b6\5\u0081A\2\u01b4\u01b6\7a\2\2\u01b5\u01b2")
        buf.write("\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b5\u01b4\3\2\2\2\u01b6")
        buf.write("\u0080\3\2\2\2\u01b7\u01b8\t\3\2\2\u01b8\u0082\3\2\2\2")
        buf.write("\u01b9\u01bb\t\4\2\2\u01ba\u01b9\3\2\2\2\u01bb\u01bc\3")
        buf.write("\2\2\2\u01bc\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u0084")
        buf.write("\3\2\2\2\u01be\u01c2\7%\2\2\u01bf\u01c1\n\5\2\2\u01c0")
        buf.write("\u01bf\3\2\2\2\u01c1\u01c4\3\2\2\2\u01c2\u01c0\3\2\2\2")
        buf.write("\u01c2\u01c3\3\2\2\2\u01c3\u0086\3\2\2\2\u01c4\u01c2\3")
        buf.write("\2\2\2\u01c5\u01c8\5\u0083B\2\u01c6\u01c8\5\u0085C\2\u01c7")
        buf.write("\u01c5\3\2\2\2\u01c7\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2")
        buf.write("\u01c9\u01ca\bD\2\2\u01ca\u0088\3\2\2\2\u01cb\u01cc\13")
        buf.write("\2\2\2\u01cc\u008a\3\2\2\2\22\2\u008c\u0092\u0096\u009c")
        buf.write("\u009f\u0195\u019c\u01a2\u01a8\u01ad\u01b0\u01b5\u01bc")
        buf.write("\u01c2\u01c7\3\b\2\2")
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
    ANY_CONDITION = 36
    BIND = 37
    PREDICT = 38
    ASSIGN = 39
    TIMES_EQ = 40
    DIV_EQ = 41
    PLUS_EQ = 42
    MINUS_EQ = 43
    EQ_TO = 44
    GT_EQ = 45
    LT_EQ = 46
    NOT_EQ = 47
    COL = 48
    COM = 49
    L_BRK = 50
    R_BRK = 51
    L_PAR = 52
    R_PAR = 53
    LT = 54
    GT = 55
    TIMES = 56
    DIVIDE = 57
    PLUS = 58
    MINUS = 59
    FNAME = 60
    IDENTIFIER = 61
    DECIMAL = 62
    INTEGER = 63
    SKIP_ = 64
    ANY = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'import'", "'Predicate'", "'Feature'", "'Factor'", "'Goal'", 
            "'Constant'", "'Action'", "'Effect'", "'Reward'", "'Policy'", 
            "'Execute'", "'Option'", "'MarkovFeature'", "'Never'", "'S'", 
            "'A'", "'P'", "'''", "'if'", "'else'", "'elif'", "'in'", "'init'", 
            "'until'", "'with'", "'then'", "'and'", "'or'", "'not'", "'True'", 
            "'False'", "'Any'", "':='", "'->'", "'='", "'*='", "'/='", "'+='", 
            "'-='", "'=='", "'>='", "'<='", "'!='", "':'", "','", "'['", 
            "']'", "'('", "')'", "'<'", "'>'", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "NL", "IMPORT", "PREDICATE", "FEATURE", 
            "FACTOR", "GOAL", "CONSTANT", "ACTION", "EFFECT", "REWARD", 
            "POLICY", "EXECUTE", "OPTION", "MARKOVFEATURE", "NEVER", "S_PRIME", 
            "S", "A", "P", "PRIME", "IF", "ELSE", "ELIF", "IN", "INIT", 
            "UNTIL", "WITH", "THEN", "AND", "OR", "NOT", "TRUE", "FALSE", 
            "ANY_CONDITION", "BIND", "PREDICT", "ASSIGN", "TIMES_EQ", "DIV_EQ", 
            "PLUS_EQ", "MINUS_EQ", "EQ_TO", "GT_EQ", "LT_EQ", "NOT_EQ", 
            "COL", "COM", "L_BRK", "R_BRK", "L_PAR", "R_PAR", "LT", "GT", 
            "TIMES", "DIVIDE", "PLUS", "MINUS", "FNAME", "IDENTIFIER", "DECIMAL", 
            "INTEGER", "SKIP_", "ANY" ]

    ruleNames = [ "NL", "IMPORT", "PREDICATE", "FEATURE", "FACTOR", "GOAL", 
                  "CONSTANT", "ACTION", "EFFECT", "REWARD", "POLICY", "EXECUTE", 
                  "OPTION", "MARKOVFEATURE", "NEVER", "S_PRIME", "S", "A", 
                  "P", "PRIME", "IF", "ELSE", "ELIF", "IN", "INIT", "UNTIL", 
                  "WITH", "THEN", "AND", "OR", "NOT", "TRUE", "FALSE", "ANY_CONDITION", 
                  "BIND", "PREDICT", "ASSIGN", "TIMES_EQ", "DIV_EQ", "PLUS_EQ", 
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



