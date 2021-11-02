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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u01df\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\5\2\u0091\n\2\3\2\3\2\7")
        buf.write("\2\u0095\n\2\f\2\16\2\u0098\13\2\3\2\5\2\u009b\n\2\3\2")
        buf.write("\3\2\7\2\u009f\n\2\f\2\16\2\u00a2\13\2\5\2\u00a4\n\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3")
        buf.write("#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3")
        buf.write("\'\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3")
        buf.write("-\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\62")
        buf.write("\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67")
        buf.write("\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3=\7=\u01a6\n=\f")
        buf.write("=\16=\u01a9\13=\3>\3>\7>\u01ad\n>\f>\16>\u01b0\13>\3?")
        buf.write("\6?\u01b3\n?\r?\16?\u01b4\3?\3?\6?\u01b9\n?\r?\16?\u01ba")
        buf.write("\3@\6@\u01be\n@\r@\16@\u01bf\3A\5A\u01c3\nA\3B\3B\3B\5")
        buf.write("B\u01c8\nB\3C\3C\3D\6D\u01cd\nD\rD\16D\u01ce\3E\3E\7E")
        buf.write("\u01d3\nE\fE\16E\u01d6\13E\3F\3F\5F\u01da\nF\3F\3F\3G")
        buf.write("\3G\2\2H\3\5\5\6\7\7\t\b\13\t\r\n\17\13\21\f\23\r\25\16")
        buf.write("\27\17\31\20\33\21\35\22\37\23!\24#\25%\26\'\27)\30+\31")
        buf.write("-\32/\33\61\34\63\35\65\36\67\379 ;!=\"?#A$C%E&G\'I(K")
        buf.write(")M*O+Q,S-U.W/Y\60[\61]\62_\63a\64c\65e\66g\67i8k9m:o;")
        buf.write("q<s=u>w?y@{A}B\177C\u0081\2\u0083\2\u0085\2\u0087\2\u0089")
        buf.write("\2\u008bD\u008dE\3\2\6\4\2C\\c|\3\2\62;\4\2\13\13\"\"")
        buf.write("\4\2\f\f\16\17\2\u01e8\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2")
        buf.write("\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\3\u00a3\3\2\2\2\5")
        buf.write("\u00a5\3\2\2\2\7\u00ac\3\2\2\2\t\u00b6\3\2\2\2\13\u00be")
        buf.write("\3\2\2\2\r\u00c5\3\2\2\2\17\u00ca\3\2\2\2\21\u00d3\3\2")
        buf.write("\2\2\23\u00da\3\2\2\2\25\u00e1\3\2\2\2\27\u00e8\3\2\2")
        buf.write("\2\31\u00ef\3\2\2\2\33\u00f7\3\2\2\2\35\u00fe\3\2\2\2")
        buf.write("\37\u010c\3\2\2\2!\u0115\3\2\2\2#\u0118\3\2\2\2%\u011a")
        buf.write("\3\2\2\2\'\u011c\3\2\2\2)\u011e\3\2\2\2+\u0120\3\2\2\2")
        buf.write("-\u0123\3\2\2\2/\u0128\3\2\2\2\61\u012d\3\2\2\2\63\u0130")
        buf.write("\3\2\2\2\65\u0135\3\2\2\2\67\u013b\3\2\2\29\u0140\3\2")
        buf.write("\2\2;\u0145\3\2\2\2=\u014b\3\2\2\2?\u0150\3\2\2\2A\u0154")
        buf.write("\3\2\2\2C\u0157\3\2\2\2E\u015b\3\2\2\2G\u0160\3\2\2\2")
        buf.write("I\u0166\3\2\2\2K\u016a\3\2\2\2M\u016d\3\2\2\2O\u0170\3")
        buf.write("\2\2\2Q\u0172\3\2\2\2S\u0175\3\2\2\2U\u0178\3\2\2\2W\u017b")
        buf.write("\3\2\2\2Y\u017e\3\2\2\2[\u0181\3\2\2\2]\u0184\3\2\2\2")
        buf.write("_\u0187\3\2\2\2a\u018a\3\2\2\2c\u018c\3\2\2\2e\u018e\3")
        buf.write("\2\2\2g\u0190\3\2\2\2i\u0192\3\2\2\2k\u0194\3\2\2\2m\u0196")
        buf.write("\3\2\2\2o\u0198\3\2\2\2q\u019a\3\2\2\2s\u019c\3\2\2\2")
        buf.write("u\u019e\3\2\2\2w\u01a0\3\2\2\2y\u01a2\3\2\2\2{\u01aa\3")
        buf.write("\2\2\2}\u01b2\3\2\2\2\177\u01bd\3\2\2\2\u0081\u01c2\3")
        buf.write("\2\2\2\u0083\u01c7\3\2\2\2\u0085\u01c9\3\2\2\2\u0087\u01cc")
        buf.write("\3\2\2\2\u0089\u01d0\3\2\2\2\u008b\u01d9\3\2\2\2\u008d")
        buf.write("\u01dd\3\2\2\2\u008f\u0091\7\17\2\2\u0090\u008f\3\2\2")
        buf.write("\2\u0090\u0091\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0096")
        buf.write("\7\f\2\2\u0093\u0095\7\"\2\2\u0094\u0093\3\2\2\2\u0095")
        buf.write("\u0098\3\2\2\2\u0096\u0094\3\2\2\2\u0096\u0097\3\2\2\2")
        buf.write("\u0097\u00a4\3\2\2\2\u0098\u0096\3\2\2\2\u0099\u009b\7")
        buf.write("\17\2\2\u009a\u0099\3\2\2\2\u009a\u009b\3\2\2\2\u009b")
        buf.write("\u009c\3\2\2\2\u009c\u00a0\7\f\2\2\u009d\u009f\7\13\2")
        buf.write("\2\u009e\u009d\3\2\2\2\u009f\u00a2\3\2\2\2\u00a0\u009e")
        buf.write("\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a4\3\2\2\2\u00a2")
        buf.write("\u00a0\3\2\2\2\u00a3\u0090\3\2\2\2\u00a3\u009a\3\2\2\2")
        buf.write("\u00a4\4\3\2\2\2\u00a5\u00a6\7k\2\2\u00a6\u00a7\7o\2\2")
        buf.write("\u00a7\u00a8\7r\2\2\u00a8\u00a9\7q\2\2\u00a9\u00aa\7t")
        buf.write("\2\2\u00aa\u00ab\7v\2\2\u00ab\6\3\2\2\2\u00ac\u00ad\7")
        buf.write("R\2\2\u00ad\u00ae\7t\2\2\u00ae\u00af\7g\2\2\u00af\u00b0")
        buf.write("\7f\2\2\u00b0\u00b1\7k\2\2\u00b1\u00b2\7e\2\2\u00b2\u00b3")
        buf.write("\7c\2\2\u00b3\u00b4\7v\2\2\u00b4\u00b5\7g\2\2\u00b5\b")
        buf.write("\3\2\2\2\u00b6\u00b7\7H\2\2\u00b7\u00b8\7g\2\2\u00b8\u00b9")
        buf.write("\7c\2\2\u00b9\u00ba\7v\2\2\u00ba\u00bb\7w\2\2\u00bb\u00bc")
        buf.write("\7t\2\2\u00bc\u00bd\7g\2\2\u00bd\n\3\2\2\2\u00be\u00bf")
        buf.write("\7H\2\2\u00bf\u00c0\7c\2\2\u00c0\u00c1\7e\2\2\u00c1\u00c2")
        buf.write("\7v\2\2\u00c2\u00c3\7q\2\2\u00c3\u00c4\7t\2\2\u00c4\f")
        buf.write("\3\2\2\2\u00c5\u00c6\7I\2\2\u00c6\u00c7\7q\2\2\u00c7\u00c8")
        buf.write("\7c\2\2\u00c8\u00c9\7n\2\2\u00c9\16\3\2\2\2\u00ca\u00cb")
        buf.write("\7E\2\2\u00cb\u00cc\7q\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce")
        buf.write("\7u\2\2\u00ce\u00cf\7v\2\2\u00cf\u00d0\7c\2\2\u00d0\u00d1")
        buf.write("\7p\2\2\u00d1\u00d2\7v\2\2\u00d2\20\3\2\2\2\u00d3\u00d4")
        buf.write("\7C\2\2\u00d4\u00d5\7e\2\2\u00d5\u00d6\7v\2\2\u00d6\u00d7")
        buf.write("\7k\2\2\u00d7\u00d8\7q\2\2\u00d8\u00d9\7p\2\2\u00d9\22")
        buf.write("\3\2\2\2\u00da\u00db\7G\2\2\u00db\u00dc\7h\2\2\u00dc\u00dd")
        buf.write("\7h\2\2\u00dd\u00de\7g\2\2\u00de\u00df\7e\2\2\u00df\u00e0")
        buf.write("\7v\2\2\u00e0\24\3\2\2\2\u00e1\u00e2\7T\2\2\u00e2\u00e3")
        buf.write("\7g\2\2\u00e3\u00e4\7y\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6")
        buf.write("\7t\2\2\u00e6\u00e7\7f\2\2\u00e7\26\3\2\2\2\u00e8\u00e9")
        buf.write("\7R\2\2\u00e9\u00ea\7q\2\2\u00ea\u00eb\7n\2\2\u00eb\u00ec")
        buf.write("\7k\2\2\u00ec\u00ed\7e\2\2\u00ed\u00ee\7{\2\2\u00ee\30")
        buf.write("\3\2\2\2\u00ef\u00f0\7G\2\2\u00f0\u00f1\7z\2\2\u00f1\u00f2")
        buf.write("\7g\2\2\u00f2\u00f3\7e\2\2\u00f3\u00f4\7w\2\2\u00f4\u00f5")
        buf.write("\7v\2\2\u00f5\u00f6\7g\2\2\u00f6\32\3\2\2\2\u00f7\u00f8")
        buf.write("\7Q\2\2\u00f8\u00f9\7r\2\2\u00f9\u00fa\7v\2\2\u00fa\u00fb")
        buf.write("\7k\2\2\u00fb\u00fc\7q\2\2\u00fc\u00fd\7p\2\2\u00fd\34")
        buf.write("\3\2\2\2\u00fe\u00ff\7O\2\2\u00ff\u0100\7c\2\2\u0100\u0101")
        buf.write("\7t\2\2\u0101\u0102\7m\2\2\u0102\u0103\7q\2\2\u0103\u0104")
        buf.write("\7x\2\2\u0104\u0105\7H\2\2\u0105\u0106\7g\2\2\u0106\u0107")
        buf.write("\7c\2\2\u0107\u0108\7v\2\2\u0108\u0109\7w\2\2\u0109\u010a")
        buf.write("\7t\2\2\u010a\u010b\7g\2\2\u010b\36\3\2\2\2\u010c\u010d")
        buf.write("\7F\2\2\u010d\u010e\7{\2\2\u010e\u010f\7p\2\2\u010f\u0110")
        buf.write("\7c\2\2\u0110\u0111\7o\2\2\u0111\u0112\7k\2\2\u0112\u0113")
        buf.write("\7e\2\2\u0113\u0114\7u\2\2\u0114 \3\2\2\2\u0115\u0116")
        buf.write("\5#\22\2\u0116\u0117\5)\25\2\u0117\"\3\2\2\2\u0118\u0119")
        buf.write("\7U\2\2\u0119$\3\2\2\2\u011a\u011b\7C\2\2\u011b&\3\2\2")
        buf.write("\2\u011c\u011d\7R\2\2\u011d(\3\2\2\2\u011e\u011f\7)\2")
        buf.write("\2\u011f*\3\2\2\2\u0120\u0121\7k\2\2\u0121\u0122\7h\2")
        buf.write("\2\u0122,\3\2\2\2\u0123\u0124\7g\2\2\u0124\u0125\7n\2")
        buf.write("\2\u0125\u0126\7u\2\2\u0126\u0127\7g\2\2\u0127.\3\2\2")
        buf.write("\2\u0128\u0129\7g\2\2\u0129\u012a\7n\2\2\u012a\u012b\7")
        buf.write("k\2\2\u012b\u012c\7h\2\2\u012c\60\3\2\2\2\u012d\u012e")
        buf.write("\7k\2\2\u012e\u012f\7p\2\2\u012f\62\3\2\2\2\u0130\u0131")
        buf.write("\7k\2\2\u0131\u0132\7p\2\2\u0132\u0133\7k\2\2\u0133\u0134")
        buf.write("\7v\2\2\u0134\64\3\2\2\2\u0135\u0136\7w\2\2\u0136\u0137")
        buf.write("\7p\2\2\u0137\u0138\7v\2\2\u0138\u0139\7k\2\2\u0139\u013a")
        buf.write("\7n\2\2\u013a\66\3\2\2\2\u013b\u013c\7y\2\2\u013c\u013d")
        buf.write("\7k\2\2\u013d\u013e\7v\2\2\u013e\u013f\7j\2\2\u013f8\3")
        buf.write("\2\2\2\u0140\u0141\7v\2\2\u0141\u0142\7j\2\2\u0142\u0143")
        buf.write("\7g\2\2\u0143\u0144\7p\2\2\u0144:\3\2\2\2\u0145\u0146")
        buf.write("\7p\2\2\u0146\u0147\7g\2\2\u0147\u0148\7x\2\2\u0148\u0149")
        buf.write("\7g\2\2\u0149\u014a\7t\2\2\u014a<\3\2\2\2\u014b\u014c")
        buf.write("\7o\2\2\u014c\u014d\7c\2\2\u014d\u014e\7k\2\2\u014e\u014f")
        buf.write("\7p\2\2\u014f>\3\2\2\2\u0150\u0151\7c\2\2\u0151\u0152")
        buf.write("\7p\2\2\u0152\u0153\7f\2\2\u0153@\3\2\2\2\u0154\u0155")
        buf.write("\7q\2\2\u0155\u0156\7t\2\2\u0156B\3\2\2\2\u0157\u0158")
        buf.write("\7p\2\2\u0158\u0159\7q\2\2\u0159\u015a\7v\2\2\u015aD\3")
        buf.write("\2\2\2\u015b\u015c\7V\2\2\u015c\u015d\7t\2\2\u015d\u015e")
        buf.write("\7w\2\2\u015e\u015f\7g\2\2\u015fF\3\2\2\2\u0160\u0161")
        buf.write("\7H\2\2\u0161\u0162\7c\2\2\u0162\u0163\7n\2\2\u0163\u0164")
        buf.write("\7u\2\2\u0164\u0165\7g\2\2\u0165H\3\2\2\2\u0166\u0167")
        buf.write("\7C\2\2\u0167\u0168\7p\2\2\u0168\u0169\7{\2\2\u0169J\3")
        buf.write("\2\2\2\u016a\u016b\7<\2\2\u016b\u016c\7?\2\2\u016cL\3")
        buf.write("\2\2\2\u016d\u016e\7/\2\2\u016e\u016f\7@\2\2\u016fN\3")
        buf.write("\2\2\2\u0170\u0171\7?\2\2\u0171P\3\2\2\2\u0172\u0173\7")
        buf.write(",\2\2\u0173\u0174\7?\2\2\u0174R\3\2\2\2\u0175\u0176\7")
        buf.write("\61\2\2\u0176\u0177\7?\2\2\u0177T\3\2\2\2\u0178\u0179")
        buf.write("\7-\2\2\u0179\u017a\7?\2\2\u017aV\3\2\2\2\u017b\u017c")
        buf.write("\7/\2\2\u017c\u017d\7?\2\2\u017dX\3\2\2\2\u017e\u017f")
        buf.write("\7?\2\2\u017f\u0180\7?\2\2\u0180Z\3\2\2\2\u0181\u0182")
        buf.write("\7@\2\2\u0182\u0183\7?\2\2\u0183\\\3\2\2\2\u0184\u0185")
        buf.write("\7>\2\2\u0185\u0186\7?\2\2\u0186^\3\2\2\2\u0187\u0188")
        buf.write("\7#\2\2\u0188\u0189\7?\2\2\u0189`\3\2\2\2\u018a\u018b")
        buf.write("\7<\2\2\u018bb\3\2\2\2\u018c\u018d\7.\2\2\u018dd\3\2\2")
        buf.write("\2\u018e\u018f\7]\2\2\u018ff\3\2\2\2\u0190\u0191\7_\2")
        buf.write("\2\u0191h\3\2\2\2\u0192\u0193\7*\2\2\u0193j\3\2\2\2\u0194")
        buf.write("\u0195\7+\2\2\u0195l\3\2\2\2\u0196\u0197\7>\2\2\u0197")
        buf.write("n\3\2\2\2\u0198\u0199\7@\2\2\u0199p\3\2\2\2\u019a\u019b")
        buf.write("\7,\2\2\u019br\3\2\2\2\u019c\u019d\7\61\2\2\u019dt\3\2")
        buf.write("\2\2\u019e\u019f\7-\2\2\u019fv\3\2\2\2\u01a0\u01a1\7/")
        buf.write("\2\2\u01a1x\3\2\2\2\u01a2\u01a3\5{>\2\u01a3\u01a7\7\60")
        buf.write("\2\2\u01a4\u01a6\5\u0081A\2\u01a5\u01a4\3\2\2\2\u01a6")
        buf.write("\u01a9\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2")
        buf.write("\u01a8z\3\2\2\2\u01a9\u01a7\3\2\2\2\u01aa\u01ae\5\u0081")
        buf.write("A\2\u01ab\u01ad\5\u0083B\2\u01ac\u01ab\3\2\2\2\u01ad\u01b0")
        buf.write("\3\2\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2\u01af")
        buf.write("|\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b1\u01b3\5\u0085C\2\u01b2")
        buf.write("\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b2\3\2\2\2")
        buf.write("\u01b4\u01b5\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01b8\7")
        buf.write("\60\2\2\u01b7\u01b9\5\u0085C\2\u01b8\u01b7\3\2\2\2\u01b9")
        buf.write("\u01ba\3\2\2\2\u01ba\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2")
        buf.write("\u01bb~\3\2\2\2\u01bc\u01be\5\u0085C\2\u01bd\u01bc\3\2")
        buf.write("\2\2\u01be\u01bf\3\2\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01c0")
        buf.write("\3\2\2\2\u01c0\u0080\3\2\2\2\u01c1\u01c3\t\2\2\2\u01c2")
        buf.write("\u01c1\3\2\2\2\u01c3\u0082\3\2\2\2\u01c4\u01c8\5\u0081")
        buf.write("A\2\u01c5\u01c8\5\u0085C\2\u01c6\u01c8\7a\2\2\u01c7\u01c4")
        buf.write("\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c7\u01c6\3\2\2\2\u01c8")
        buf.write("\u0084\3\2\2\2\u01c9\u01ca\t\3\2\2\u01ca\u0086\3\2\2\2")
        buf.write("\u01cb\u01cd\t\4\2\2\u01cc\u01cb\3\2\2\2\u01cd\u01ce\3")
        buf.write("\2\2\2\u01ce\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u0088")
        buf.write("\3\2\2\2\u01d0\u01d4\7%\2\2\u01d1\u01d3\n\5\2\2\u01d2")
        buf.write("\u01d1\3\2\2\2\u01d3\u01d6\3\2\2\2\u01d4\u01d2\3\2\2\2")
        buf.write("\u01d4\u01d5\3\2\2\2\u01d5\u008a\3\2\2\2\u01d6\u01d4\3")
        buf.write("\2\2\2\u01d7\u01da\5\u0087D\2\u01d8\u01da\5\u0089E\2\u01d9")
        buf.write("\u01d7\3\2\2\2\u01d9\u01d8\3\2\2\2\u01da\u01db\3\2\2\2")
        buf.write("\u01db\u01dc\bF\2\2\u01dc\u008c\3\2\2\2\u01dd\u01de\13")
        buf.write("\2\2\2\u01de\u008e\3\2\2\2\22\2\u0090\u0096\u009a\u00a0")
        buf.write("\u00a3\u01a7\u01ae\u01b4\u01ba\u01bf\u01c2\u01c7\u01ce")
        buf.write("\u01d4\u01d9\3\b\2\2")
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
    DYNAMICS = 17
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
    NEVER = 31
    MAIN = 32
    AND = 33
    OR = 34
    NOT = 35
    TRUE = 36
    FALSE = 37
    ANY_CONDITION = 38
    BIND = 39
    PREDICT = 40
    ASSIGN = 41
    TIMES_EQ = 42
    DIV_EQ = 43
    PLUS_EQ = 44
    MINUS_EQ = 45
    EQ_TO = 46
    GT_EQ = 47
    LT_EQ = 48
    NOT_EQ = 49
    COL = 50
    COM = 51
    L_BRK = 52
    R_BRK = 53
    L_PAR = 54
    R_PAR = 55
    LT = 56
    GT = 57
    TIMES = 58
    DIVIDE = 59
    PLUS = 60
    MINUS = 61
    FNAME = 62
    IDENTIFIER = 63
    DECIMAL = 64
    INTEGER = 65
    SKIP_ = 66
    ANY = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'import'", "'Predicate'", "'Feature'", "'Factor'", "'Goal'", 
            "'Constant'", "'Action'", "'Effect'", "'Reward'", "'Policy'", 
            "'Execute'", "'Option'", "'MarkovFeature'", "'Dynamics'", "'S'", 
            "'A'", "'P'", "'''", "'if'", "'else'", "'elif'", "'in'", "'init'", 
            "'until'", "'with'", "'then'", "'never'", "'main'", "'and'", 
            "'or'", "'not'", "'True'", "'False'", "'Any'", "':='", "'->'", 
            "'='", "'*='", "'/='", "'+='", "'-='", "'=='", "'>='", "'<='", 
            "'!='", "':'", "','", "'['", "']'", "'('", "')'", "'<'", "'>'", 
            "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "NL", "IMPORT", "PREDICATE", "FEATURE", 
            "FACTOR", "GOAL", "CONSTANT", "ACTION", "EFFECT", "REWARD", 
            "POLICY", "EXECUTE", "OPTION", "MARKOVFEATURE", "DYNAMICS", 
            "S_PRIME", "S", "A", "P", "PRIME", "IF", "ELSE", "ELIF", "IN", 
            "INIT", "UNTIL", "WITH", "THEN", "NEVER", "MAIN", "AND", "OR", 
            "NOT", "TRUE", "FALSE", "ANY_CONDITION", "BIND", "PREDICT", 
            "ASSIGN", "TIMES_EQ", "DIV_EQ", "PLUS_EQ", "MINUS_EQ", "EQ_TO", 
            "GT_EQ", "LT_EQ", "NOT_EQ", "COL", "COM", "L_BRK", "R_BRK", 
            "L_PAR", "R_PAR", "LT", "GT", "TIMES", "DIVIDE", "PLUS", "MINUS", 
            "FNAME", "IDENTIFIER", "DECIMAL", "INTEGER", "SKIP_", "ANY" ]

    ruleNames = [ "NL", "IMPORT", "PREDICATE", "FEATURE", "FACTOR", "GOAL", 
                  "CONSTANT", "ACTION", "EFFECT", "REWARD", "POLICY", "EXECUTE", 
                  "OPTION", "MARKOVFEATURE", "DYNAMICS", "S_PRIME", "S", 
                  "A", "P", "PRIME", "IF", "ELSE", "ELIF", "IN", "INIT", 
                  "UNTIL", "WITH", "THEN", "NEVER", "MAIN", "AND", "OR", 
                  "NOT", "TRUE", "FALSE", "ANY_CONDITION", "BIND", "PREDICT", 
                  "ASSIGN", "TIMES_EQ", "DIV_EQ", "PLUS_EQ", "MINUS_EQ", 
                  "EQ_TO", "GT_EQ", "LT_EQ", "NOT_EQ", "COL", "COM", "L_BRK", 
                  "R_BRK", "L_PAR", "R_PAR", "LT", "GT", "TIMES", "DIVIDE", 
                  "PLUS", "MINUS", "FNAME", "IDENTIFIER", "DECIMAL", "INTEGER", 
                  "LETTER", "ANY_CHAR", "DIGIT", "SPACES", "COMMENT", "SKIP_", 
                  "ANY" ]

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



