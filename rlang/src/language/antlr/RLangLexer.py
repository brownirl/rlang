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
        buf.write("\u01d8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3#\3#\3")
        buf.write("#\3#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3")
        buf.write("(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3")
        buf.write(".\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63")
        buf.write("\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3")
        buf.write(":\3:\3;\3;\3<\3<\3<\7<\u019f\n<\f<\16<\u01a2\13<\3=\3")
        buf.write("=\7=\u01a6\n=\f=\16=\u01a9\13=\3>\6>\u01ac\n>\r>\16>\u01ad")
        buf.write("\3>\3>\6>\u01b2\n>\r>\16>\u01b3\3?\6?\u01b7\n?\r?\16?")
        buf.write("\u01b8\3@\5@\u01bc\n@\3A\3A\3A\5A\u01c1\nA\3B\3B\3C\6")
        buf.write("C\u01c6\nC\rC\16C\u01c7\3D\3D\7D\u01cc\nD\fD\16D\u01cf")
        buf.write("\13D\3E\3E\5E\u01d3\nE\3E\3E\3F\3F\2\2G\3\5\5\6\7\7\t")
        buf.write("\b\13\t\r\n\17\13\21\f\23\r\25\16\27\17\31\20\33\21\35")
        buf.write("\22\37\23!\24#\25%\26\'\27)\30+\31-\32/\33\61\34\63\35")
        buf.write("\65\36\67\379 ;!=\"?#A$C%E&G\'I(K)M*O+Q,S-U.W/Y\60[\61")
        buf.write("]\62_\63a\64c\65e\66g\67i8k9m:o;q<s=u>w?y@{A}B\177\2\u0081")
        buf.write("\2\u0083\2\u0085\2\u0087\2\u0089C\u008bD\3\2\6\4\2C\\")
        buf.write("c|\3\2\62;\4\2\13\13\"\"\4\2\f\f\16\17\2\u01e1\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2")
        buf.write("\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2")
        buf.write("\2\2}\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\3\u00a1")
        buf.write("\3\2\2\2\5\u00a3\3\2\2\2\7\u00aa\3\2\2\2\t\u00b4\3\2\2")
        buf.write("\2\13\u00bc\3\2\2\2\r\u00c3\3\2\2\2\17\u00c8\3\2\2\2\21")
        buf.write("\u00d1\3\2\2\2\23\u00d8\3\2\2\2\25\u00df\3\2\2\2\27\u00e6")
        buf.write("\3\2\2\2\31\u00ed\3\2\2\2\33\u00f5\3\2\2\2\35\u00fc\3")
        buf.write("\2\2\2\37\u010a\3\2\2\2!\u0113\3\2\2\2#\u0116\3\2\2\2")
        buf.write("%\u0118\3\2\2\2\'\u011a\3\2\2\2)\u011c\3\2\2\2+\u011e")
        buf.write("\3\2\2\2-\u0121\3\2\2\2/\u0126\3\2\2\2\61\u012b\3\2\2")
        buf.write("\2\63\u012e\3\2\2\2\65\u0133\3\2\2\2\67\u0139\3\2\2\2")
        buf.write("9\u013e\3\2\2\2;\u0143\3\2\2\2=\u0149\3\2\2\2?\u014d\3")
        buf.write("\2\2\2A\u0150\3\2\2\2C\u0154\3\2\2\2E\u0159\3\2\2\2G\u015f")
        buf.write("\3\2\2\2I\u0163\3\2\2\2K\u0166\3\2\2\2M\u0169\3\2\2\2")
        buf.write("O\u016b\3\2\2\2Q\u016e\3\2\2\2S\u0171\3\2\2\2U\u0174\3")
        buf.write("\2\2\2W\u0177\3\2\2\2Y\u017a\3\2\2\2[\u017d\3\2\2\2]\u0180")
        buf.write("\3\2\2\2_\u0183\3\2\2\2a\u0185\3\2\2\2c\u0187\3\2\2\2")
        buf.write("e\u0189\3\2\2\2g\u018b\3\2\2\2i\u018d\3\2\2\2k\u018f\3")
        buf.write("\2\2\2m\u0191\3\2\2\2o\u0193\3\2\2\2q\u0195\3\2\2\2s\u0197")
        buf.write("\3\2\2\2u\u0199\3\2\2\2w\u019b\3\2\2\2y\u01a3\3\2\2\2")
        buf.write("{\u01ab\3\2\2\2}\u01b6\3\2\2\2\177\u01bb\3\2\2\2\u0081")
        buf.write("\u01c0\3\2\2\2\u0083\u01c2\3\2\2\2\u0085\u01c5\3\2\2\2")
        buf.write("\u0087\u01c9\3\2\2\2\u0089\u01d2\3\2\2\2\u008b\u01d6\3")
        buf.write("\2\2\2\u008d\u008f\7\17\2\2\u008e\u008d\3\2\2\2\u008e")
        buf.write("\u008f\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u0094\7\f\2\2")
        buf.write("\u0091\u0093\7\"\2\2\u0092\u0091\3\2\2\2\u0093\u0096\3")
        buf.write("\2\2\2\u0094\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u00a2")
        buf.write("\3\2\2\2\u0096\u0094\3\2\2\2\u0097\u0099\7\17\2\2\u0098")
        buf.write("\u0097\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009a\3\2\2\2")
        buf.write("\u009a\u009e\7\f\2\2\u009b\u009d\7\13\2\2\u009c\u009b")
        buf.write("\3\2\2\2\u009d\u00a0\3\2\2\2\u009e\u009c\3\2\2\2\u009e")
        buf.write("\u009f\3\2\2\2\u009f\u00a2\3\2\2\2\u00a0\u009e\3\2\2\2")
        buf.write("\u00a1\u008e\3\2\2\2\u00a1\u0098\3\2\2\2\u00a2\4\3\2\2")
        buf.write("\2\u00a3\u00a4\7k\2\2\u00a4\u00a5\7o\2\2\u00a5\u00a6\7")
        buf.write("r\2\2\u00a6\u00a7\7q\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9")
        buf.write("\7v\2\2\u00a9\6\3\2\2\2\u00aa\u00ab\7R\2\2\u00ab\u00ac")
        buf.write("\7t\2\2\u00ac\u00ad\7g\2\2\u00ad\u00ae\7f\2\2\u00ae\u00af")
        buf.write("\7k\2\2\u00af\u00b0\7e\2\2\u00b0\u00b1\7c\2\2\u00b1\u00b2")
        buf.write("\7v\2\2\u00b2\u00b3\7g\2\2\u00b3\b\3\2\2\2\u00b4\u00b5")
        buf.write("\7H\2\2\u00b5\u00b6\7g\2\2\u00b6\u00b7\7c\2\2\u00b7\u00b8")
        buf.write("\7v\2\2\u00b8\u00b9\7w\2\2\u00b9\u00ba\7t\2\2\u00ba\u00bb")
        buf.write("\7g\2\2\u00bb\n\3\2\2\2\u00bc\u00bd\7H\2\2\u00bd\u00be")
        buf.write("\7c\2\2\u00be\u00bf\7e\2\2\u00bf\u00c0\7v\2\2\u00c0\u00c1")
        buf.write("\7q\2\2\u00c1\u00c2\7t\2\2\u00c2\f\3\2\2\2\u00c3\u00c4")
        buf.write("\7I\2\2\u00c4\u00c5\7q\2\2\u00c5\u00c6\7c\2\2\u00c6\u00c7")
        buf.write("\7n\2\2\u00c7\16\3\2\2\2\u00c8\u00c9\7E\2\2\u00c9\u00ca")
        buf.write("\7q\2\2\u00ca\u00cb\7p\2\2\u00cb\u00cc\7u\2\2\u00cc\u00cd")
        buf.write("\7v\2\2\u00cd\u00ce\7c\2\2\u00ce\u00cf\7p\2\2\u00cf\u00d0")
        buf.write("\7v\2\2\u00d0\20\3\2\2\2\u00d1\u00d2\7C\2\2\u00d2\u00d3")
        buf.write("\7e\2\2\u00d3\u00d4\7v\2\2\u00d4\u00d5\7k\2\2\u00d5\u00d6")
        buf.write("\7q\2\2\u00d6\u00d7\7p\2\2\u00d7\22\3\2\2\2\u00d8\u00d9")
        buf.write("\7G\2\2\u00d9\u00da\7h\2\2\u00da\u00db\7h\2\2\u00db\u00dc")
        buf.write("\7g\2\2\u00dc\u00dd\7e\2\2\u00dd\u00de\7v\2\2\u00de\24")
        buf.write("\3\2\2\2\u00df\u00e0\7T\2\2\u00e0\u00e1\7g\2\2\u00e1\u00e2")
        buf.write("\7y\2\2\u00e2\u00e3\7c\2\2\u00e3\u00e4\7t\2\2\u00e4\u00e5")
        buf.write("\7f\2\2\u00e5\26\3\2\2\2\u00e6\u00e7\7R\2\2\u00e7\u00e8")
        buf.write("\7q\2\2\u00e8\u00e9\7n\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb")
        buf.write("\7e\2\2\u00eb\u00ec\7{\2\2\u00ec\30\3\2\2\2\u00ed\u00ee")
        buf.write("\7G\2\2\u00ee\u00ef\7z\2\2\u00ef\u00f0\7g\2\2\u00f0\u00f1")
        buf.write("\7e\2\2\u00f1\u00f2\7w\2\2\u00f2\u00f3\7v\2\2\u00f3\u00f4")
        buf.write("\7g\2\2\u00f4\32\3\2\2\2\u00f5\u00f6\7Q\2\2\u00f6\u00f7")
        buf.write("\7r\2\2\u00f7\u00f8\7v\2\2\u00f8\u00f9\7k\2\2\u00f9\u00fa")
        buf.write("\7q\2\2\u00fa\u00fb\7p\2\2\u00fb\34\3\2\2\2\u00fc\u00fd")
        buf.write("\7O\2\2\u00fd\u00fe\7c\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100")
        buf.write("\7m\2\2\u0100\u0101\7q\2\2\u0101\u0102\7x\2\2\u0102\u0103")
        buf.write("\7H\2\2\u0103\u0104\7g\2\2\u0104\u0105\7c\2\2\u0105\u0106")
        buf.write("\7v\2\2\u0106\u0107\7w\2\2\u0107\u0108\7t\2\2\u0108\u0109")
        buf.write("\7g\2\2\u0109\36\3\2\2\2\u010a\u010b\7F\2\2\u010b\u010c")
        buf.write("\7{\2\2\u010c\u010d\7p\2\2\u010d\u010e\7c\2\2\u010e\u010f")
        buf.write("\7o\2\2\u010f\u0110\7k\2\2\u0110\u0111\7e\2\2\u0111\u0112")
        buf.write("\7u\2\2\u0112 \3\2\2\2\u0113\u0114\5#\22\2\u0114\u0115")
        buf.write("\5)\25\2\u0115\"\3\2\2\2\u0116\u0117\7U\2\2\u0117$\3\2")
        buf.write("\2\2\u0118\u0119\7C\2\2\u0119&\3\2\2\2\u011a\u011b\7R")
        buf.write("\2\2\u011b(\3\2\2\2\u011c\u011d\7)\2\2\u011d*\3\2\2\2")
        buf.write("\u011e\u011f\7k\2\2\u011f\u0120\7h\2\2\u0120,\3\2\2\2")
        buf.write("\u0121\u0122\7g\2\2\u0122\u0123\7n\2\2\u0123\u0124\7u")
        buf.write("\2\2\u0124\u0125\7g\2\2\u0125.\3\2\2\2\u0126\u0127\7g")
        buf.write("\2\2\u0127\u0128\7n\2\2\u0128\u0129\7k\2\2\u0129\u012a")
        buf.write("\7h\2\2\u012a\60\3\2\2\2\u012b\u012c\7k\2\2\u012c\u012d")
        buf.write("\7p\2\2\u012d\62\3\2\2\2\u012e\u012f\7k\2\2\u012f\u0130")
        buf.write("\7p\2\2\u0130\u0131\7k\2\2\u0131\u0132\7v\2\2\u0132\64")
        buf.write("\3\2\2\2\u0133\u0134\7w\2\2\u0134\u0135\7p\2\2\u0135\u0136")
        buf.write("\7v\2\2\u0136\u0137\7k\2\2\u0137\u0138\7n\2\2\u0138\66")
        buf.write("\3\2\2\2\u0139\u013a\7y\2\2\u013a\u013b\7k\2\2\u013b\u013c")
        buf.write("\7v\2\2\u013c\u013d\7j\2\2\u013d8\3\2\2\2\u013e\u013f")
        buf.write("\7v\2\2\u013f\u0140\7j\2\2\u0140\u0141\7g\2\2\u0141\u0142")
        buf.write("\7p\2\2\u0142:\3\2\2\2\u0143\u0144\7p\2\2\u0144\u0145")
        buf.write("\7g\2\2\u0145\u0146\7x\2\2\u0146\u0147\7g\2\2\u0147\u0148")
        buf.write("\7t\2\2\u0148<\3\2\2\2\u0149\u014a\7c\2\2\u014a\u014b")
        buf.write("\7p\2\2\u014b\u014c\7f\2\2\u014c>\3\2\2\2\u014d\u014e")
        buf.write("\7q\2\2\u014e\u014f\7t\2\2\u014f@\3\2\2\2\u0150\u0151")
        buf.write("\7p\2\2\u0151\u0152\7q\2\2\u0152\u0153\7v\2\2\u0153B\3")
        buf.write("\2\2\2\u0154\u0155\7V\2\2\u0155\u0156\7t\2\2\u0156\u0157")
        buf.write("\7w\2\2\u0157\u0158\7g\2\2\u0158D\3\2\2\2\u0159\u015a")
        buf.write("\7H\2\2\u015a\u015b\7c\2\2\u015b\u015c\7n\2\2\u015c\u015d")
        buf.write("\7u\2\2\u015d\u015e\7g\2\2\u015eF\3\2\2\2\u015f\u0160")
        buf.write("\7C\2\2\u0160\u0161\7p\2\2\u0161\u0162\7{\2\2\u0162H\3")
        buf.write("\2\2\2\u0163\u0164\7<\2\2\u0164\u0165\7?\2\2\u0165J\3")
        buf.write("\2\2\2\u0166\u0167\7/\2\2\u0167\u0168\7@\2\2\u0168L\3")
        buf.write("\2\2\2\u0169\u016a\7?\2\2\u016aN\3\2\2\2\u016b\u016c\7")
        buf.write(",\2\2\u016c\u016d\7?\2\2\u016dP\3\2\2\2\u016e\u016f\7")
        buf.write("\61\2\2\u016f\u0170\7?\2\2\u0170R\3\2\2\2\u0171\u0172")
        buf.write("\7-\2\2\u0172\u0173\7?\2\2\u0173T\3\2\2\2\u0174\u0175")
        buf.write("\7/\2\2\u0175\u0176\7?\2\2\u0176V\3\2\2\2\u0177\u0178")
        buf.write("\7?\2\2\u0178\u0179\7?\2\2\u0179X\3\2\2\2\u017a\u017b")
        buf.write("\7@\2\2\u017b\u017c\7?\2\2\u017cZ\3\2\2\2\u017d\u017e")
        buf.write("\7>\2\2\u017e\u017f\7?\2\2\u017f\\\3\2\2\2\u0180\u0181")
        buf.write("\7#\2\2\u0181\u0182\7?\2\2\u0182^\3\2\2\2\u0183\u0184")
        buf.write("\7<\2\2\u0184`\3\2\2\2\u0185\u0186\7.\2\2\u0186b\3\2\2")
        buf.write("\2\u0187\u0188\7]\2\2\u0188d\3\2\2\2\u0189\u018a\7_\2")
        buf.write("\2\u018af\3\2\2\2\u018b\u018c\7*\2\2\u018ch\3\2\2\2\u018d")
        buf.write("\u018e\7+\2\2\u018ej\3\2\2\2\u018f\u0190\7>\2\2\u0190")
        buf.write("l\3\2\2\2\u0191\u0192\7@\2\2\u0192n\3\2\2\2\u0193\u0194")
        buf.write("\7,\2\2\u0194p\3\2\2\2\u0195\u0196\7\61\2\2\u0196r\3\2")
        buf.write("\2\2\u0197\u0198\7-\2\2\u0198t\3\2\2\2\u0199\u019a\7/")
        buf.write("\2\2\u019av\3\2\2\2\u019b\u019c\5y=\2\u019c\u01a0\7\60")
        buf.write("\2\2\u019d\u019f\5\177@\2\u019e\u019d\3\2\2\2\u019f\u01a2")
        buf.write("\3\2\2\2\u01a0\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1")
        buf.write("x\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a3\u01a7\5\177@\2\u01a4")
        buf.write("\u01a6\5\u0081A\2\u01a5\u01a4\3\2\2\2\u01a6\u01a9\3\2")
        buf.write("\2\2\u01a7\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8z\3")
        buf.write("\2\2\2\u01a9\u01a7\3\2\2\2\u01aa\u01ac\5\u0083B\2\u01ab")
        buf.write("\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01ab\3\2\2\2")
        buf.write("\u01ad\u01ae\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b1\7")
        buf.write("\60\2\2\u01b0\u01b2\5\u0083B\2\u01b1\u01b0\3\2\2\2\u01b2")
        buf.write("\u01b3\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2")
        buf.write("\u01b4|\3\2\2\2\u01b5\u01b7\5\u0083B\2\u01b6\u01b5\3\2")
        buf.write("\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8\u01b9")
        buf.write("\3\2\2\2\u01b9~\3\2\2\2\u01ba\u01bc\t\2\2\2\u01bb\u01ba")
        buf.write("\3\2\2\2\u01bc\u0080\3\2\2\2\u01bd\u01c1\5\177@\2\u01be")
        buf.write("\u01c1\5\u0083B\2\u01bf\u01c1\7a\2\2\u01c0\u01bd\3\2\2")
        buf.write("\2\u01c0\u01be\3\2\2\2\u01c0\u01bf\3\2\2\2\u01c1\u0082")
        buf.write("\3\2\2\2\u01c2\u01c3\t\3\2\2\u01c3\u0084\3\2\2\2\u01c4")
        buf.write("\u01c6\t\4\2\2\u01c5\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2")
        buf.write("\u01c7\u01c5\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u0086\3")
        buf.write("\2\2\2\u01c9\u01cd\7%\2\2\u01ca\u01cc\n\5\2\2\u01cb\u01ca")
        buf.write("\3\2\2\2\u01cc\u01cf\3\2\2\2\u01cd\u01cb\3\2\2\2\u01cd")
        buf.write("\u01ce\3\2\2\2\u01ce\u0088\3\2\2\2\u01cf\u01cd\3\2\2\2")
        buf.write("\u01d0\u01d3\5\u0085C\2\u01d1\u01d3\5\u0087D\2\u01d2\u01d0")
        buf.write("\3\2\2\2\u01d2\u01d1\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4")
        buf.write("\u01d5\bE\2\2\u01d5\u008a\3\2\2\2\u01d6\u01d7\13\2\2\2")
        buf.write("\u01d7\u008c\3\2\2\2\22\2\u008e\u0094\u0098\u009e\u00a1")
        buf.write("\u01a0\u01a7\u01ad\u01b3\u01b8\u01bb\u01c0\u01c7\u01cd")
        buf.write("\u01d2\3\b\2\2")
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
            "'import'", "'Predicate'", "'Feature'", "'Factor'", "'Goal'", 
            "'Constant'", "'Action'", "'Effect'", "'Reward'", "'Policy'", 
            "'Execute'", "'Option'", "'MarkovFeature'", "'Dynamics'", "'S'", 
            "'A'", "'P'", "'''", "'if'", "'else'", "'elif'", "'in'", "'init'", 
            "'until'", "'with'", "'then'", "'never'", "'and'", "'or'", "'not'", 
            "'True'", "'False'", "'Any'", "':='", "'->'", "'='", "'*='", 
            "'/='", "'+='", "'-='", "'=='", "'>='", "'<='", "'!='", "':'", 
            "','", "'['", "']'", "'('", "')'", "'<'", "'>'", "'*'", "'/'", 
            "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "NL", "IMPORT", "PREDICATE", "FEATURE", 
            "FACTOR", "GOAL", "CONSTANT", "ACTION", "EFFECT", "REWARD", 
            "POLICY", "EXECUTE", "OPTION", "MARKOVFEATURE", "DYNAMICS", 
            "S_PRIME", "S", "A", "P", "PRIME", "IF", "ELSE", "ELIF", "IN", 
            "INIT", "UNTIL", "WITH", "THEN", "NEVER", "AND", "OR", "NOT", 
            "TRUE", "FALSE", "ANY_CONDITION", "BIND", "PREDICT", "ASSIGN", 
            "TIMES_EQ", "DIV_EQ", "PLUS_EQ", "MINUS_EQ", "EQ_TO", "GT_EQ", 
            "LT_EQ", "NOT_EQ", "COL", "COM", "L_BRK", "R_BRK", "L_PAR", 
            "R_PAR", "LT", "GT", "TIMES", "DIVIDE", "PLUS", "MINUS", "FNAME", 
            "IDENTIFIER", "DECIMAL", "INTEGER", "SKIP_", "ANY" ]

    ruleNames = [ "NL", "IMPORT", "PREDICATE", "FEATURE", "FACTOR", "GOAL", 
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



