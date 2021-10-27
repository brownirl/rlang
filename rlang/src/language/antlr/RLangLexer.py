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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u01bf\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\3\2\5\2\u0089\n\2\3\2\3\2\7\2\u008d\n\2\f\2\16\2\u0090")
        buf.write("\13\2\3\2\5\2\u0093\n\2\3\2\3\2\7\2\u0097\n\2\f\2\16\2")
        buf.write("\u009a\13\2\5\2\u009c\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3#\3#\3")
        buf.write("#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3")
        buf.write(")\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3")
        buf.write("\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\38\38\39\39\39\79\u0186\n9\f9\16")
        buf.write("9\u0189\139\3:\3:\7:\u018d\n:\f:\16:\u0190\13:\3;\6;\u0193")
        buf.write("\n;\r;\16;\u0194\3;\3;\6;\u0199\n;\r;\16;\u019a\3<\6<")
        buf.write("\u019e\n<\r<\16<\u019f\3=\5=\u01a3\n=\3>\3>\3>\5>\u01a8")
        buf.write("\n>\3?\3?\3@\6@\u01ad\n@\r@\16@\u01ae\3A\3A\7A\u01b3\n")
        buf.write("A\fA\16A\u01b6\13A\3B\3B\5B\u01ba\nB\3B\3B\3C\3C\2\2D")
        buf.write("\3\5\5\6\7\7\t\b\13\t\r\n\17\13\21\f\23\r\25\16\27\17")
        buf.write("\31\20\33\21\35\22\37\23!\24#\25%\26\'\27)\30+\31-\32")
        buf.write("/\33\61\34\63\35\65\36\67\379 ;!=\"?#A$C%E&G\'I(K)M*O")
        buf.write("+Q,S-U.W/Y\60[\61]\62_\63a\64c\65e\66g\67i8k9m:o;q<s=")
        buf.write("u>w?y\2{\2}\2\177\2\u0081\2\u0083@\u0085A\3\2\6\4\2C\\")
        buf.write("c|\3\2\62;\4\2\13\13\"\"\4\2\f\f\16\17\2\u01c8\2\3\3\2")
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
        buf.write("\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\3\u009b\3\2\2\2\5\u009d\3\2\2\2\7\u00a7\3\2\2")
        buf.write("\2\t\u00af\3\2\2\2\13\u00b6\3\2\2\2\r\u00bb\3\2\2\2\17")
        buf.write("\u00c4\3\2\2\2\21\u00cb\3\2\2\2\23\u00d2\3\2\2\2\25\u00d9")
        buf.write("\3\2\2\2\27\u00e0\3\2\2\2\31\u00e8\3\2\2\2\33\u00ef\3")
        buf.write("\2\2\2\35\u00fd\3\2\2\2\37\u0104\3\2\2\2!\u0107\3\2\2")
        buf.write("\2#\u0109\3\2\2\2%\u010b\3\2\2\2\'\u010d\3\2\2\2)\u010f")
        buf.write("\3\2\2\2+\u0112\3\2\2\2-\u0117\3\2\2\2/\u011c\3\2\2\2")
        buf.write("\61\u011f\3\2\2\2\63\u0124\3\2\2\2\65\u012a\3\2\2\2\67")
        buf.write("\u012f\3\2\2\29\u0134\3\2\2\2;\u0138\3\2\2\2=\u013b\3")
        buf.write("\2\2\2?\u013f\3\2\2\2A\u0144\3\2\2\2C\u014a\3\2\2\2E\u014d")
        buf.write("\3\2\2\2G\u0150\3\2\2\2I\u0152\3\2\2\2K\u0155\3\2\2\2")
        buf.write("M\u0158\3\2\2\2O\u015b\3\2\2\2Q\u015e\3\2\2\2S\u0161\3")
        buf.write("\2\2\2U\u0164\3\2\2\2W\u0167\3\2\2\2Y\u016a\3\2\2\2[\u016c")
        buf.write("\3\2\2\2]\u016e\3\2\2\2_\u0170\3\2\2\2a\u0172\3\2\2\2")
        buf.write("c\u0174\3\2\2\2e\u0176\3\2\2\2g\u0178\3\2\2\2i\u017a\3")
        buf.write("\2\2\2k\u017c\3\2\2\2m\u017e\3\2\2\2o\u0180\3\2\2\2q\u0182")
        buf.write("\3\2\2\2s\u018a\3\2\2\2u\u0192\3\2\2\2w\u019d\3\2\2\2")
        buf.write("y\u01a2\3\2\2\2{\u01a7\3\2\2\2}\u01a9\3\2\2\2\177\u01ac")
        buf.write("\3\2\2\2\u0081\u01b0\3\2\2\2\u0083\u01b9\3\2\2\2\u0085")
        buf.write("\u01bd\3\2\2\2\u0087\u0089\7\17\2\2\u0088\u0087\3\2\2")
        buf.write("\2\u0088\u0089\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u008e")
        buf.write("\7\f\2\2\u008b\u008d\7\"\2\2\u008c\u008b\3\2\2\2\u008d")
        buf.write("\u0090\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008f\3\2\2\2")
        buf.write("\u008f\u009c\3\2\2\2\u0090\u008e\3\2\2\2\u0091\u0093\7")
        buf.write("\17\2\2\u0092\u0091\3\2\2\2\u0092\u0093\3\2\2\2\u0093")
        buf.write("\u0094\3\2\2\2\u0094\u0098\7\f\2\2\u0095\u0097\7\13\2")
        buf.write("\2\u0096\u0095\3\2\2\2\u0097\u009a\3\2\2\2\u0098\u0096")
        buf.write("\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009c\3\2\2\2\u009a")
        buf.write("\u0098\3\2\2\2\u009b\u0088\3\2\2\2\u009b\u0092\3\2\2\2")
        buf.write("\u009c\4\3\2\2\2\u009d\u009e\7R\2\2\u009e\u009f\7t\2\2")
        buf.write("\u009f\u00a0\7g\2\2\u00a0\u00a1\7f\2\2\u00a1\u00a2\7k")
        buf.write("\2\2\u00a2\u00a3\7e\2\2\u00a3\u00a4\7c\2\2\u00a4\u00a5")
        buf.write("\7v\2\2\u00a5\u00a6\7g\2\2\u00a6\6\3\2\2\2\u00a7\u00a8")
        buf.write("\7H\2\2\u00a8\u00a9\7g\2\2\u00a9\u00aa\7c\2\2\u00aa\u00ab")
        buf.write("\7v\2\2\u00ab\u00ac\7w\2\2\u00ac\u00ad\7t\2\2\u00ad\u00ae")
        buf.write("\7g\2\2\u00ae\b\3\2\2\2\u00af\u00b0\7H\2\2\u00b0\u00b1")
        buf.write("\7c\2\2\u00b1\u00b2\7e\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4")
        buf.write("\7q\2\2\u00b4\u00b5\7t\2\2\u00b5\n\3\2\2\2\u00b6\u00b7")
        buf.write("\7I\2\2\u00b7\u00b8\7q\2\2\u00b8\u00b9\7c\2\2\u00b9\u00ba")
        buf.write("\7n\2\2\u00ba\f\3\2\2\2\u00bb\u00bc\7E\2\2\u00bc\u00bd")
        buf.write("\7q\2\2\u00bd\u00be\7p\2\2\u00be\u00bf\7u\2\2\u00bf\u00c0")
        buf.write("\7v\2\2\u00c0\u00c1\7c\2\2\u00c1\u00c2\7p\2\2\u00c2\u00c3")
        buf.write("\7v\2\2\u00c3\16\3\2\2\2\u00c4\u00c5\7C\2\2\u00c5\u00c6")
        buf.write("\7e\2\2\u00c6\u00c7\7v\2\2\u00c7\u00c8\7k\2\2\u00c8\u00c9")
        buf.write("\7q\2\2\u00c9\u00ca\7p\2\2\u00ca\20\3\2\2\2\u00cb\u00cc")
        buf.write("\7G\2\2\u00cc\u00cd\7h\2\2\u00cd\u00ce\7h\2\2\u00ce\u00cf")
        buf.write("\7g\2\2\u00cf\u00d0\7e\2\2\u00d0\u00d1\7v\2\2\u00d1\22")
        buf.write("\3\2\2\2\u00d2\u00d3\7T\2\2\u00d3\u00d4\7g\2\2\u00d4\u00d5")
        buf.write("\7y\2\2\u00d5\u00d6\7c\2\2\u00d6\u00d7\7t\2\2\u00d7\u00d8")
        buf.write("\7f\2\2\u00d8\24\3\2\2\2\u00d9\u00da\7R\2\2\u00da\u00db")
        buf.write("\7q\2\2\u00db\u00dc\7n\2\2\u00dc\u00dd\7k\2\2\u00dd\u00de")
        buf.write("\7e\2\2\u00de\u00df\7{\2\2\u00df\26\3\2\2\2\u00e0\u00e1")
        buf.write("\7G\2\2\u00e1\u00e2\7z\2\2\u00e2\u00e3\7g\2\2\u00e3\u00e4")
        buf.write("\7e\2\2\u00e4\u00e5\7w\2\2\u00e5\u00e6\7v\2\2\u00e6\u00e7")
        buf.write("\7g\2\2\u00e7\30\3\2\2\2\u00e8\u00e9\7Q\2\2\u00e9\u00ea")
        buf.write("\7r\2\2\u00ea\u00eb\7v\2\2\u00eb\u00ec\7k\2\2\u00ec\u00ed")
        buf.write("\7q\2\2\u00ed\u00ee\7p\2\2\u00ee\32\3\2\2\2\u00ef\u00f0")
        buf.write("\7O\2\2\u00f0\u00f1\7c\2\2\u00f1\u00f2\7t\2\2\u00f2\u00f3")
        buf.write("\7m\2\2\u00f3\u00f4\7q\2\2\u00f4\u00f5\7x\2\2\u00f5\u00f6")
        buf.write("\7H\2\2\u00f6\u00f7\7g\2\2\u00f7\u00f8\7c\2\2\u00f8\u00f9")
        buf.write("\7v\2\2\u00f9\u00fa\7w\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc")
        buf.write("\7g\2\2\u00fc\34\3\2\2\2\u00fd\u00fe\7k\2\2\u00fe\u00ff")
        buf.write("\7o\2\2\u00ff\u0100\7r\2\2\u0100\u0101\7q\2\2\u0101\u0102")
        buf.write("\7t\2\2\u0102\u0103\7v\2\2\u0103\36\3\2\2\2\u0104\u0105")
        buf.write("\5!\21\2\u0105\u0106\5\'\24\2\u0106 \3\2\2\2\u0107\u0108")
        buf.write("\7U\2\2\u0108\"\3\2\2\2\u0109\u010a\7C\2\2\u010a$\3\2")
        buf.write("\2\2\u010b\u010c\7R\2\2\u010c&\3\2\2\2\u010d\u010e\7)")
        buf.write("\2\2\u010e(\3\2\2\2\u010f\u0110\7k\2\2\u0110\u0111\7h")
        buf.write("\2\2\u0111*\3\2\2\2\u0112\u0113\7g\2\2\u0113\u0114\7n")
        buf.write("\2\2\u0114\u0115\7u\2\2\u0115\u0116\7g\2\2\u0116,\3\2")
        buf.write("\2\2\u0117\u0118\7g\2\2\u0118\u0119\7n\2\2\u0119\u011a")
        buf.write("\7k\2\2\u011a\u011b\7h\2\2\u011b.\3\2\2\2\u011c\u011d")
        buf.write("\7k\2\2\u011d\u011e\7p\2\2\u011e\60\3\2\2\2\u011f\u0120")
        buf.write("\7k\2\2\u0120\u0121\7p\2\2\u0121\u0122\7k\2\2\u0122\u0123")
        buf.write("\7v\2\2\u0123\62\3\2\2\2\u0124\u0125\7w\2\2\u0125\u0126")
        buf.write("\7p\2\2\u0126\u0127\7v\2\2\u0127\u0128\7k\2\2\u0128\u0129")
        buf.write("\7n\2\2\u0129\64\3\2\2\2\u012a\u012b\7y\2\2\u012b\u012c")
        buf.write("\7k\2\2\u012c\u012d\7v\2\2\u012d\u012e\7j\2\2\u012e\66")
        buf.write("\3\2\2\2\u012f\u0130\7v\2\2\u0130\u0131\7j\2\2\u0131\u0132")
        buf.write("\7g\2\2\u0132\u0133\7p\2\2\u01338\3\2\2\2\u0134\u0135")
        buf.write("\7c\2\2\u0135\u0136\7p\2\2\u0136\u0137\7f\2\2\u0137:\3")
        buf.write("\2\2\2\u0138\u0139\7q\2\2\u0139\u013a\7t\2\2\u013a<\3")
        buf.write("\2\2\2\u013b\u013c\7p\2\2\u013c\u013d\7q\2\2\u013d\u013e")
        buf.write("\7v\2\2\u013e>\3\2\2\2\u013f\u0140\7V\2\2\u0140\u0141")
        buf.write("\7t\2\2\u0141\u0142\7w\2\2\u0142\u0143\7g\2\2\u0143@\3")
        buf.write("\2\2\2\u0144\u0145\7H\2\2\u0145\u0146\7c\2\2\u0146\u0147")
        buf.write("\7n\2\2\u0147\u0148\7u\2\2\u0148\u0149\7g\2\2\u0149B\3")
        buf.write("\2\2\2\u014a\u014b\7<\2\2\u014b\u014c\7?\2\2\u014cD\3")
        buf.write("\2\2\2\u014d\u014e\7/\2\2\u014e\u014f\7@\2\2\u014fF\3")
        buf.write("\2\2\2\u0150\u0151\7?\2\2\u0151H\3\2\2\2\u0152\u0153\7")
        buf.write(",\2\2\u0153\u0154\7?\2\2\u0154J\3\2\2\2\u0155\u0156\7")
        buf.write("\61\2\2\u0156\u0157\7?\2\2\u0157L\3\2\2\2\u0158\u0159")
        buf.write("\7-\2\2\u0159\u015a\7?\2\2\u015aN\3\2\2\2\u015b\u015c")
        buf.write("\7/\2\2\u015c\u015d\7?\2\2\u015dP\3\2\2\2\u015e\u015f")
        buf.write("\7?\2\2\u015f\u0160\7?\2\2\u0160R\3\2\2\2\u0161\u0162")
        buf.write("\7@\2\2\u0162\u0163\7?\2\2\u0163T\3\2\2\2\u0164\u0165")
        buf.write("\7>\2\2\u0165\u0166\7?\2\2\u0166V\3\2\2\2\u0167\u0168")
        buf.write("\7#\2\2\u0168\u0169\7?\2\2\u0169X\3\2\2\2\u016a\u016b")
        buf.write("\7<\2\2\u016bZ\3\2\2\2\u016c\u016d\7.\2\2\u016d\\\3\2")
        buf.write("\2\2\u016e\u016f\7]\2\2\u016f^\3\2\2\2\u0170\u0171\7_")
        buf.write("\2\2\u0171`\3\2\2\2\u0172\u0173\7*\2\2\u0173b\3\2\2\2")
        buf.write("\u0174\u0175\7+\2\2\u0175d\3\2\2\2\u0176\u0177\7>\2\2")
        buf.write("\u0177f\3\2\2\2\u0178\u0179\7@\2\2\u0179h\3\2\2\2\u017a")
        buf.write("\u017b\7,\2\2\u017bj\3\2\2\2\u017c\u017d\7\61\2\2\u017d")
        buf.write("l\3\2\2\2\u017e\u017f\7-\2\2\u017fn\3\2\2\2\u0180\u0181")
        buf.write("\7/\2\2\u0181p\3\2\2\2\u0182\u0183\5s:\2\u0183\u0187\7")
        buf.write("\60\2\2\u0184\u0186\5y=\2\u0185\u0184\3\2\2\2\u0186\u0189")
        buf.write("\3\2\2\2\u0187\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188")
        buf.write("r\3\2\2\2\u0189\u0187\3\2\2\2\u018a\u018e\5y=\2\u018b")
        buf.write("\u018d\5{>\2\u018c\u018b\3\2\2\2\u018d\u0190\3\2\2\2\u018e")
        buf.write("\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018ft\3\2\2\2\u0190")
        buf.write("\u018e\3\2\2\2\u0191\u0193\5}?\2\u0192\u0191\3\2\2\2\u0193")
        buf.write("\u0194\3\2\2\2\u0194\u0192\3\2\2\2\u0194\u0195\3\2\2\2")
        buf.write("\u0195\u0196\3\2\2\2\u0196\u0198\7\60\2\2\u0197\u0199")
        buf.write("\5}?\2\u0198\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u0198")
        buf.write("\3\2\2\2\u019a\u019b\3\2\2\2\u019bv\3\2\2\2\u019c\u019e")
        buf.write("\5}?\2\u019d\u019c\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u019d")
        buf.write("\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0x\3\2\2\2\u01a1\u01a3")
        buf.write("\t\2\2\2\u01a2\u01a1\3\2\2\2\u01a3z\3\2\2\2\u01a4\u01a8")
        buf.write("\5y=\2\u01a5\u01a8\5}?\2\u01a6\u01a8\7a\2\2\u01a7\u01a4")
        buf.write("\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7\u01a6\3\2\2\2\u01a8")
        buf.write("|\3\2\2\2\u01a9\u01aa\t\3\2\2\u01aa~\3\2\2\2\u01ab\u01ad")
        buf.write("\t\4\2\2\u01ac\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae")
        buf.write("\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u0080\3\2\2\2")
        buf.write("\u01b0\u01b4\7%\2\2\u01b1\u01b3\n\5\2\2\u01b2\u01b1\3")
        buf.write("\2\2\2\u01b3\u01b6\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b4\u01b5")
        buf.write("\3\2\2\2\u01b5\u0082\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b7")
        buf.write("\u01ba\5\177@\2\u01b8\u01ba\5\u0081A\2\u01b9\u01b7\3\2")
        buf.write("\2\2\u01b9\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bc")
        buf.write("\bB\2\2\u01bc\u0084\3\2\2\2\u01bd\u01be\13\2\2\2\u01be")
        buf.write("\u0086\3\2\2\2\22\2\u0088\u008e\u0092\u0098\u009b\u0187")
        buf.write("\u018e\u0194\u019a\u019f\u01a2\u01a7\u01ae\u01b4\u01b9")
        buf.write("\3\b\2\2")
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
    P = 20
    PRIME = 21
    IF = 22
    ELSE = 23
    ELIF = 24
    IN = 25
    INIT = 26
    UNTIL = 27
    WITH = 28
    THEN = 29
    AND = 30
    OR = 31
    NOT = 32
    TRUE = 33
    FALSE = 34
    BIND = 35
    PREDICT = 36
    ASSIGN = 37
    TIMES_EQ = 38
    DIV_EQ = 39
    PLUS_EQ = 40
    MINUS_EQ = 41
    EQ_TO = 42
    GT_EQ = 43
    LT_EQ = 44
    NOT_EQ = 45
    COL = 46
    COM = 47
    L_BRK = 48
    R_BRK = 49
    L_PAR = 50
    R_PAR = 51
    LT = 52
    GT = 53
    TIMES = 54
    DIVIDE = 55
    PLUS = 56
    MINUS = 57
    FNAME = 58
    IDENTIFIER = 59
    DECIMAL = 60
    INTEGER = 61
    SKIP_ = 62
    ANY = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Predicate'", "'Feature'", "'Factor'", "'Goal'", "'Constant'", 
            "'Action'", "'Effect'", "'Reward'", "'Policy'", "'Execute'", 
            "'Option'", "'MarkovFeature'", "'import'", "'S'", "'A'", "'P'", 
            "'''", "'if'", "'else'", "'elif'", "'in'", "'init'", "'until'", 
            "'with'", "'then'", "'and'", "'or'", "'not'", "'True'", "'False'", 
            "':='", "'->'", "'='", "'*='", "'/='", "'+='", "'-='", "'=='", 
            "'>='", "'<='", "'!='", "':'", "','", "'['", "']'", "'('", "')'", 
            "'<'", "'>'", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "NL", "PREDICATE", "FEATURE", "FACTOR", 
            "GOAL", "CONSTANT", "ACTION", "EFFECT", "REWARD", "POLICY", 
            "EXECUTE", "OPTION", "MARKOVFEATURE", "IMPORT", "S_PRIME", "S", 
            "A", "P", "PRIME", "IF", "ELSE", "ELIF", "IN", "INIT", "UNTIL", 
            "WITH", "THEN", "AND", "OR", "NOT", "TRUE", "FALSE", "BIND", 
            "PREDICT", "ASSIGN", "TIMES_EQ", "DIV_EQ", "PLUS_EQ", "MINUS_EQ", 
            "EQ_TO", "GT_EQ", "LT_EQ", "NOT_EQ", "COL", "COM", "L_BRK", 
            "R_BRK", "L_PAR", "R_PAR", "LT", "GT", "TIMES", "DIVIDE", "PLUS", 
            "MINUS", "FNAME", "IDENTIFIER", "DECIMAL", "INTEGER", "SKIP_", 
            "ANY" ]

    ruleNames = [ "NL", "PREDICATE", "FEATURE", "FACTOR", "GOAL", "CONSTANT", 
                  "ACTION", "EFFECT", "REWARD", "POLICY", "EXECUTE", "OPTION", 
                  "MARKOVFEATURE", "IMPORT", "S_PRIME", "S", "A", "P", "PRIME", 
                  "IF", "ELSE", "ELIF", "IN", "INIT", "UNTIL", "WITH", "THEN", 
                  "AND", "OR", "NOT", "TRUE", "FALSE", "BIND", "PREDICT", 
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



