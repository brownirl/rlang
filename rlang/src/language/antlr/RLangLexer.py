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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u01da\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\3\2\5\2\u008f\n\2\3\2\3\2\7\2\u0093")
        buf.write("\n\2\f\2\16\2\u0096\13\2\3\2\5\2\u0099\n\2\3\2\3\2\7\2")
        buf.write("\u009d\n\2\f\2\16\2\u00a0\13\2\5\2\u00a2\n\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
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
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'")
        buf.write("\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3")
        buf.write("-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63")
        buf.write("\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\3")
        buf.write("9\39\3:\3:\3;\3;\3<\3<\3<\7<\u01a1\n<\f<\16<\u01a4\13")
        buf.write("<\3=\3=\7=\u01a8\n=\f=\16=\u01ab\13=\3>\6>\u01ae\n>\r")
        buf.write(">\16>\u01af\3>\3>\6>\u01b4\n>\r>\16>\u01b5\3?\6?\u01b9")
        buf.write("\n?\r?\16?\u01ba\3@\5@\u01be\n@\3A\3A\3A\5A\u01c3\nA\3")
        buf.write("B\3B\3C\6C\u01c8\nC\rC\16C\u01c9\3D\3D\7D\u01ce\nD\fD")
        buf.write("\16D\u01d1\13D\3E\3E\5E\u01d5\nE\3E\3E\3F\3F\2\2G\3\5")
        buf.write("\5\6\7\7\t\b\13\t\r\n\17\13\21\f\23\r\25\16\27\17\31\20")
        buf.write("\33\21\35\22\37\23!\24#\25%\26\'\27)\30+\31-\32/\33\61")
        buf.write("\34\63\35\65\36\67\379 ;!=\"?#A$C%E&G\'I(K)M*O+Q,S-U.")
        buf.write("W/Y\60[\61]\62_\63a\64c\65e\66g\67i8k9m:o;q<s=u>w?y@{")
        buf.write("A}B\177\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089C\u008b")
        buf.write("D\3\2\6\4\2C\\c|\3\2\62;\4\2\13\13\"\"\4\2\f\f\16\17\2")
        buf.write("\u01e3\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
        buf.write("]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2")
        buf.write("\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2")
        buf.write("\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2")
        buf.write("\2\2\2{\3\2\2\2\2}\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2")
        buf.write("\2\2\3\u00a1\3\2\2\2\5\u00a3\3\2\2\2\7\u00aa\3\2\2\2\t")
        buf.write("\u00b6\3\2\2\2\13\u00be\3\2\2\2\r\u00c5\3\2\2\2\17\u00ca")
        buf.write("\3\2\2\2\21\u00d3\3\2\2\2\23\u00da\3\2\2\2\25\u00e1\3")
        buf.write("\2\2\2\27\u00e8\3\2\2\2\31\u00ef\3\2\2\2\33\u00f7\3\2")
        buf.write("\2\2\35\u00fe\3\2\2\2\37\u010c\3\2\2\2!\u0115\3\2\2\2")
        buf.write("#\u0118\3\2\2\2%\u011a\3\2\2\2\'\u011c\3\2\2\2)\u011e")
        buf.write("\3\2\2\2+\u0120\3\2\2\2-\u0123\3\2\2\2/\u0128\3\2\2\2")
        buf.write("\61\u012d\3\2\2\2\63\u0130\3\2\2\2\65\u0135\3\2\2\2\67")
        buf.write("\u013b\3\2\2\29\u0140\3\2\2\2;\u0145\3\2\2\2=\u014b\3")
        buf.write("\2\2\2?\u014f\3\2\2\2A\u0152\3\2\2\2C\u0156\3\2\2\2E\u015b")
        buf.write("\3\2\2\2G\u0161\3\2\2\2I\u0165\3\2\2\2K\u0168\3\2\2\2")
        buf.write("M\u016b\3\2\2\2O\u016d\3\2\2\2Q\u0170\3\2\2\2S\u0173\3")
        buf.write("\2\2\2U\u0176\3\2\2\2W\u0179\3\2\2\2Y\u017c\3\2\2\2[\u017f")
        buf.write("\3\2\2\2]\u0182\3\2\2\2_\u0185\3\2\2\2a\u0187\3\2\2\2")
        buf.write("c\u0189\3\2\2\2e\u018b\3\2\2\2g\u018d\3\2\2\2i\u018f\3")
        buf.write("\2\2\2k\u0191\3\2\2\2m\u0193\3\2\2\2o\u0195\3\2\2\2q\u0197")
        buf.write("\3\2\2\2s\u0199\3\2\2\2u\u019b\3\2\2\2w\u019d\3\2\2\2")
        buf.write("y\u01a5\3\2\2\2{\u01ad\3\2\2\2}\u01b8\3\2\2\2\177\u01bd")
        buf.write("\3\2\2\2\u0081\u01c2\3\2\2\2\u0083\u01c4\3\2\2\2\u0085")
        buf.write("\u01c7\3\2\2\2\u0087\u01cb\3\2\2\2\u0089\u01d4\3\2\2\2")
        buf.write("\u008b\u01d8\3\2\2\2\u008d\u008f\7\17\2\2\u008e\u008d")
        buf.write("\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0090\3\2\2\2\u0090")
        buf.write("\u0094\7\f\2\2\u0091\u0093\7\"\2\2\u0092\u0091\3\2\2\2")
        buf.write("\u0093\u0096\3\2\2\2\u0094\u0092\3\2\2\2\u0094\u0095\3")
        buf.write("\2\2\2\u0095\u00a2\3\2\2\2\u0096\u0094\3\2\2\2\u0097\u0099")
        buf.write("\7\17\2\2\u0098\u0097\3\2\2\2\u0098\u0099\3\2\2\2\u0099")
        buf.write("\u009a\3\2\2\2\u009a\u009e\7\f\2\2\u009b\u009d\7\13\2")
        buf.write("\2\u009c\u009b\3\2\2\2\u009d\u00a0\3\2\2\2\u009e\u009c")
        buf.write("\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a2\3\2\2\2\u00a0")
        buf.write("\u009e\3\2\2\2\u00a1\u008e\3\2\2\2\u00a1\u0098\3\2\2\2")
        buf.write("\u00a2\4\3\2\2\2\u00a3\u00a4\7k\2\2\u00a4\u00a5\7o\2\2")
        buf.write("\u00a5\u00a6\7r\2\2\u00a6\u00a7\7q\2\2\u00a7\u00a8\7t")
        buf.write("\2\2\u00a8\u00a9\7v\2\2\u00a9\6\3\2\2\2\u00aa\u00ab\7")
        buf.write("R\2\2\u00ab\u00ac\7t\2\2\u00ac\u00ad\7q\2\2\u00ad\u00ae")
        buf.write("\7r\2\2\u00ae\u00af\7q\2\2\u00af\u00b0\7u\2\2\u00b0\u00b1")
        buf.write("\7k\2\2\u00b1\u00b2\7v\2\2\u00b2\u00b3\7k\2\2\u00b3\u00b4")
        buf.write("\7q\2\2\u00b4\u00b5\7p\2\2\u00b5\b\3\2\2\2\u00b6\u00b7")
        buf.write("\7H\2\2\u00b7\u00b8\7g\2\2\u00b8\u00b9\7c\2\2\u00b9\u00ba")
        buf.write("\7v\2\2\u00ba\u00bb\7w\2\2\u00bb\u00bc\7t\2\2\u00bc\u00bd")
        buf.write("\7g\2\2\u00bd\n\3\2\2\2\u00be\u00bf\7H\2\2\u00bf\u00c0")
        buf.write("\7c\2\2\u00c0\u00c1\7e\2\2\u00c1\u00c2\7v\2\2\u00c2\u00c3")
        buf.write("\7q\2\2\u00c3\u00c4\7t\2\2\u00c4\f\3\2\2\2\u00c5\u00c6")
        buf.write("\7I\2\2\u00c6\u00c7\7q\2\2\u00c7\u00c8\7c\2\2\u00c8\u00c9")
        buf.write("\7n\2\2\u00c9\16\3\2\2\2\u00ca\u00cb\7E\2\2\u00cb\u00cc")
        buf.write("\7q\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce\7u\2\2\u00ce\u00cf")
        buf.write("\7v\2\2\u00cf\u00d0\7c\2\2\u00d0\u00d1\7p\2\2\u00d1\u00d2")
        buf.write("\7v\2\2\u00d2\20\3\2\2\2\u00d3\u00d4\7C\2\2\u00d4\u00d5")
        buf.write("\7e\2\2\u00d5\u00d6\7v\2\2\u00d6\u00d7\7k\2\2\u00d7\u00d8")
        buf.write("\7q\2\2\u00d8\u00d9\7p\2\2\u00d9\22\3\2\2\2\u00da\u00db")
        buf.write("\7G\2\2\u00db\u00dc\7h\2\2\u00dc\u00dd\7h\2\2\u00dd\u00de")
        buf.write("\7g\2\2\u00de\u00df\7e\2\2\u00df\u00e0\7v\2\2\u00e0\24")
        buf.write("\3\2\2\2\u00e1\u00e2\7T\2\2\u00e2\u00e3\7g\2\2\u00e3\u00e4")
        buf.write("\7y\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6\7t\2\2\u00e6\u00e7")
        buf.write("\7f\2\2\u00e7\26\3\2\2\2\u00e8\u00e9\7R\2\2\u00e9\u00ea")
        buf.write("\7q\2\2\u00ea\u00eb\7n\2\2\u00eb\u00ec\7k\2\2\u00ec\u00ed")
        buf.write("\7e\2\2\u00ed\u00ee\7{\2\2\u00ee\30\3\2\2\2\u00ef\u00f0")
        buf.write("\7G\2\2\u00f0\u00f1\7z\2\2\u00f1\u00f2\7g\2\2\u00f2\u00f3")
        buf.write("\7e\2\2\u00f3\u00f4\7w\2\2\u00f4\u00f5\7v\2\2\u00f5\u00f6")
        buf.write("\7g\2\2\u00f6\32\3\2\2\2\u00f7\u00f8\7Q\2\2\u00f8\u00f9")
        buf.write("\7r\2\2\u00f9\u00fa\7v\2\2\u00fa\u00fb\7k\2\2\u00fb\u00fc")
        buf.write("\7q\2\2\u00fc\u00fd\7p\2\2\u00fd\34\3\2\2\2\u00fe\u00ff")
        buf.write("\7O\2\2\u00ff\u0100\7c\2\2\u0100\u0101\7t\2\2\u0101\u0102")
        buf.write("\7m\2\2\u0102\u0103\7q\2\2\u0103\u0104\7x\2\2\u0104\u0105")
        buf.write("\7H\2\2\u0105\u0106\7g\2\2\u0106\u0107\7c\2\2\u0107\u0108")
        buf.write("\7v\2\2\u0108\u0109\7w\2\2\u0109\u010a\7t\2\2\u010a\u010b")
        buf.write("\7g\2\2\u010b\36\3\2\2\2\u010c\u010d\7F\2\2\u010d\u010e")
        buf.write("\7{\2\2\u010e\u010f\7p\2\2\u010f\u0110\7c\2\2\u0110\u0111")
        buf.write("\7o\2\2\u0111\u0112\7k\2\2\u0112\u0113\7e\2\2\u0113\u0114")
        buf.write("\7u\2\2\u0114 \3\2\2\2\u0115\u0116\5#\22\2\u0116\u0117")
        buf.write("\5)\25\2\u0117\"\3\2\2\2\u0118\u0119\7U\2\2\u0119$\3\2")
        buf.write("\2\2\u011a\u011b\7C\2\2\u011b&\3\2\2\2\u011c\u011d\7R")
        buf.write("\2\2\u011d(\3\2\2\2\u011e\u011f\7)\2\2\u011f*\3\2\2\2")
        buf.write("\u0120\u0121\7k\2\2\u0121\u0122\7h\2\2\u0122,\3\2\2\2")
        buf.write("\u0123\u0124\7g\2\2\u0124\u0125\7n\2\2\u0125\u0126\7u")
        buf.write("\2\2\u0126\u0127\7g\2\2\u0127.\3\2\2\2\u0128\u0129\7g")
        buf.write("\2\2\u0129\u012a\7n\2\2\u012a\u012b\7k\2\2\u012b\u012c")
        buf.write("\7h\2\2\u012c\60\3\2\2\2\u012d\u012e\7k\2\2\u012e\u012f")
        buf.write("\7p\2\2\u012f\62\3\2\2\2\u0130\u0131\7k\2\2\u0131\u0132")
        buf.write("\7p\2\2\u0132\u0133\7k\2\2\u0133\u0134\7v\2\2\u0134\64")
        buf.write("\3\2\2\2\u0135\u0136\7w\2\2\u0136\u0137\7p\2\2\u0137\u0138")
        buf.write("\7v\2\2\u0138\u0139\7k\2\2\u0139\u013a\7n\2\2\u013a\66")
        buf.write("\3\2\2\2\u013b\u013c\7y\2\2\u013c\u013d\7k\2\2\u013d\u013e")
        buf.write("\7v\2\2\u013e\u013f\7j\2\2\u013f8\3\2\2\2\u0140\u0141")
        buf.write("\7v\2\2\u0141\u0142\7j\2\2\u0142\u0143\7g\2\2\u0143\u0144")
        buf.write("\7p\2\2\u0144:\3\2\2\2\u0145\u0146\7p\2\2\u0146\u0147")
        buf.write("\7g\2\2\u0147\u0148\7x\2\2\u0148\u0149\7g\2\2\u0149\u014a")
        buf.write("\7t\2\2\u014a<\3\2\2\2\u014b\u014c\7c\2\2\u014c\u014d")
        buf.write("\7p\2\2\u014d\u014e\7f\2\2\u014e>\3\2\2\2\u014f\u0150")
        buf.write("\7q\2\2\u0150\u0151\7t\2\2\u0151@\3\2\2\2\u0152\u0153")
        buf.write("\7p\2\2\u0153\u0154\7q\2\2\u0154\u0155\7v\2\2\u0155B\3")
        buf.write("\2\2\2\u0156\u0157\7V\2\2\u0157\u0158\7t\2\2\u0158\u0159")
        buf.write("\7w\2\2\u0159\u015a\7g\2\2\u015aD\3\2\2\2\u015b\u015c")
        buf.write("\7H\2\2\u015c\u015d\7c\2\2\u015d\u015e\7n\2\2\u015e\u015f")
        buf.write("\7u\2\2\u015f\u0160\7g\2\2\u0160F\3\2\2\2\u0161\u0162")
        buf.write("\7C\2\2\u0162\u0163\7p\2\2\u0163\u0164\7{\2\2\u0164H\3")
        buf.write("\2\2\2\u0165\u0166\7<\2\2\u0166\u0167\7?\2\2\u0167J\3")
        buf.write("\2\2\2\u0168\u0169\7/\2\2\u0169\u016a\7@\2\2\u016aL\3")
        buf.write("\2\2\2\u016b\u016c\7?\2\2\u016cN\3\2\2\2\u016d\u016e\7")
        buf.write(",\2\2\u016e\u016f\7?\2\2\u016fP\3\2\2\2\u0170\u0171\7")
        buf.write("\61\2\2\u0171\u0172\7?\2\2\u0172R\3\2\2\2\u0173\u0174")
        buf.write("\7-\2\2\u0174\u0175\7?\2\2\u0175T\3\2\2\2\u0176\u0177")
        buf.write("\7/\2\2\u0177\u0178\7?\2\2\u0178V\3\2\2\2\u0179\u017a")
        buf.write("\7?\2\2\u017a\u017b\7?\2\2\u017bX\3\2\2\2\u017c\u017d")
        buf.write("\7@\2\2\u017d\u017e\7?\2\2\u017eZ\3\2\2\2\u017f\u0180")
        buf.write("\7>\2\2\u0180\u0181\7?\2\2\u0181\\\3\2\2\2\u0182\u0183")
        buf.write("\7#\2\2\u0183\u0184\7?\2\2\u0184^\3\2\2\2\u0185\u0186")
        buf.write("\7<\2\2\u0186`\3\2\2\2\u0187\u0188\7.\2\2\u0188b\3\2\2")
        buf.write("\2\u0189\u018a\7]\2\2\u018ad\3\2\2\2\u018b\u018c\7_\2")
        buf.write("\2\u018cf\3\2\2\2\u018d\u018e\7*\2\2\u018eh\3\2\2\2\u018f")
        buf.write("\u0190\7+\2\2\u0190j\3\2\2\2\u0191\u0192\7>\2\2\u0192")
        buf.write("l\3\2\2\2\u0193\u0194\7@\2\2\u0194n\3\2\2\2\u0195\u0196")
        buf.write("\7,\2\2\u0196p\3\2\2\2\u0197\u0198\7\61\2\2\u0198r\3\2")
        buf.write("\2\2\u0199\u019a\7-\2\2\u019at\3\2\2\2\u019b\u019c\7/")
        buf.write("\2\2\u019cv\3\2\2\2\u019d\u019e\5y=\2\u019e\u01a2\7\60")
        buf.write("\2\2\u019f\u01a1\5\177@\2\u01a0\u019f\3\2\2\2\u01a1\u01a4")
        buf.write("\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3")
        buf.write("x\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a5\u01a9\5\177@\2\u01a6")
        buf.write("\u01a8\5\u0081A\2\u01a7\u01a6\3\2\2\2\u01a8\u01ab\3\2")
        buf.write("\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aaz\3")
        buf.write("\2\2\2\u01ab\u01a9\3\2\2\2\u01ac\u01ae\5\u0083B\2\u01ad")
        buf.write("\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01ad\3\2\2\2")
        buf.write("\u01af\u01b0\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01b3\7")
        buf.write("\60\2\2\u01b2\u01b4\5\u0083B\2\u01b3\u01b2\3\2\2\2\u01b4")
        buf.write("\u01b5\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2")
        buf.write("\u01b6|\3\2\2\2\u01b7\u01b9\5\u0083B\2\u01b8\u01b7\3\2")
        buf.write("\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01b8\3\2\2\2\u01ba\u01bb")
        buf.write("\3\2\2\2\u01bb~\3\2\2\2\u01bc\u01be\t\2\2\2\u01bd\u01bc")
        buf.write("\3\2\2\2\u01be\u0080\3\2\2\2\u01bf\u01c3\5\177@\2\u01c0")
        buf.write("\u01c3\5\u0083B\2\u01c1\u01c3\7a\2\2\u01c2\u01bf\3\2\2")
        buf.write("\2\u01c2\u01c0\3\2\2\2\u01c2\u01c1\3\2\2\2\u01c3\u0082")
        buf.write("\3\2\2\2\u01c4\u01c5\t\3\2\2\u01c5\u0084\3\2\2\2\u01c6")
        buf.write("\u01c8\t\4\2\2\u01c7\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2")
        buf.write("\u01c9\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u0086\3")
        buf.write("\2\2\2\u01cb\u01cf\7%\2\2\u01cc\u01ce\n\5\2\2\u01cd\u01cc")
        buf.write("\3\2\2\2\u01ce\u01d1\3\2\2\2\u01cf\u01cd\3\2\2\2\u01cf")
        buf.write("\u01d0\3\2\2\2\u01d0\u0088\3\2\2\2\u01d1\u01cf\3\2\2\2")
        buf.write("\u01d2\u01d5\5\u0085C\2\u01d3\u01d5\5\u0087D\2\u01d4\u01d2")
        buf.write("\3\2\2\2\u01d4\u01d3\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6")
        buf.write("\u01d7\bE\2\2\u01d7\u008a\3\2\2\2\u01d8\u01d9\13\2\2\2")
        buf.write("\u01d9\u008c\3\2\2\2\22\2\u008e\u0094\u0098\u009e\u00a1")
        buf.write("\u01a2\u01a9\u01af\u01b5\u01ba\u01bd\u01c2\u01c9\u01cf")
        buf.write("\u01d4\3\b\2\2")
        return buf.getvalue()


class RLangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INDENT = 1
    DEDENT = 2
    NL = 3
    IMPORT = 4
    PROPOSITION = 5
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
    AND = 32
    OR = 33
    NOT = 34
    TRUE = 35
    FALSE = 36
    ANY_CONDITION = 37
    BIND = 38
    PREDICT = 39
    ASSIGN = 40
    TIMES_EQ = 41
    DIV_EQ = 42
    PLUS_EQ = 43
    MINUS_EQ = 44
    EQ_TO = 45
    GT_EQ = 46
    LT_EQ = 47
    NOT_EQ = 48
    COL = 49
    COM = 50
    L_BRK = 51
    R_BRK = 52
    L_PAR = 53
    R_PAR = 54
    LT = 55
    GT = 56
    TIMES = 57
    DIVIDE = 58
    PLUS = 59
    MINUS = 60
    FNAME = 61
    IDENTIFIER = 62
    DECIMAL = 63
    INTEGER = 64
    SKIP_ = 65
    ANY = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'import'", "'Proposition'", "'Feature'", "'Factor'", "'Goal'", 
            "'Constant'", "'Action'", "'Effect'", "'Reward'", "'Policy'", 
            "'Execute'", "'Option'", "'MarkovFeature'", "'Dynamics'", "'S'", 
            "'A'", "'P'", "'''", "'if'", "'else'", "'elif'", "'in'", "'init'", 
            "'until'", "'with'", "'then'", "'never'", "'and'", "'or'", "'not'", 
            "'True'", "'False'", "'Any'", "':='", "'->'", "'='", "'*='", 
            "'/='", "'+='", "'-='", "'=='", "'>='", "'<='", "'!='", "':'", 
            "','", "'['", "']'", "'('", "')'", "'<'", "'>'", "'*'", "'/'", 
            "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "NL", "IMPORT", "PROPOSITION", "FEATURE", 
            "FACTOR", "GOAL", "CONSTANT", "ACTION", "EFFECT", "REWARD", 
            "POLICY", "EXECUTE", "OPTION", "MARKOVFEATURE", "DYNAMICS", 
            "S_PRIME", "S", "A", "P", "PRIME", "IF", "ELSE", "ELIF", "IN", 
            "INIT", "UNTIL", "WITH", "THEN", "NEVER", "AND", "OR", "NOT", 
            "TRUE", "FALSE", "ANY_CONDITION", "BIND", "PREDICT", "ASSIGN", 
            "TIMES_EQ", "DIV_EQ", "PLUS_EQ", "MINUS_EQ", "EQ_TO", "GT_EQ", 
            "LT_EQ", "NOT_EQ", "COL", "COM", "L_BRK", "R_BRK", "L_PAR", 
            "R_PAR", "LT", "GT", "TIMES", "DIVIDE", "PLUS", "MINUS", "FNAME", 
            "IDENTIFIER", "DECIMAL", "INTEGER", "SKIP_", "ANY" ]

    ruleNames = [ "NL", "IMPORT", "PROPOSITION", "FEATURE", "FACTOR", "GOAL", 
                  "CONSTANT", "ACTION", "EFFECT", "REWARD", "POLICY", "EXECUTE", 
                  "OPTION", "MARKOVFEATURE", "DYNAMICS", "S_PRIME", "S", 
                  "A", "P", "PRIME", "IF", "ELSE", "ELIF", "IN", "INIT", 
                  "UNTIL", "WITH", "THEN", "NEVER", "AND", "OR", "NOT", 
                  "TRUE", "FALSE", "ANY_CONDITION", "BIND", "PREDICT", "ASSIGN", 
                  "TIMES_EQ", "DIV_EQ", "PLUS_EQ", "MINUS_EQ", "EQ_TO", 
                  "GT_EQ", "LT_EQ", "NOT_EQ", "COL", "COM", "L_BRK", "R_BRK", 
                  "L_PAR", "R_PAR", "LT", "GT", "TIMES", "DIVIDE", "PLUS", 
                  "MINUS", "FNAME", "IDENTIFIER", "DECIMAL", "INTEGER", 
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



