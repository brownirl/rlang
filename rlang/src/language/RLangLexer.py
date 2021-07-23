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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u019f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\3\2\5\2}\n\2\3\2\3\2\7\2\u0081\n\2")
        buf.write("\f\2\16\2\u0084\13\2\3\2\5\2\u0087\n\2\3\2\3\2\7\2\u008b")
        buf.write("\n\2\f\2\16\2\u008e\13\2\5\2\u0090\n\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3")
        buf.write("#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3")
        buf.write("*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61")
        buf.write("\3\62\3\62\3\63\3\63\3\64\3\64\3\64\7\64\u0168\n\64\f")
        buf.write("\64\16\64\u016b\13\64\3\65\3\65\7\65\u016f\n\65\f\65\16")
        buf.write("\65\u0172\13\65\3\66\6\66\u0175\n\66\r\66\16\66\u0176")
        buf.write("\3\66\3\66\6\66\u017b\n\66\r\66\16\66\u017c\3\67\6\67")
        buf.write("\u0180\n\67\r\67\16\67\u0181\38\58\u0185\n8\39\39\39\5")
        buf.write("9\u018a\n9\3:\3:\3;\6;\u018f\n;\r;\16;\u0190\3<\3<\7<")
        buf.write("\u0195\n<\f<\16<\u0198\13<\3=\3=\5=\u019c\n=\3=\3=\2\2")
        buf.write(">\3\5\5\6\7\7\t\b\13\t\r\n\17\13\21\f\23\r\25\16\27\17")
        buf.write("\31\20\33\21\35\22\37\23!\24#\25%\26\'\27)\30+\31-\32")
        buf.write("/\33\61\34\63\35\65\36\67\379 ;!=\"?#A$C%E&G\'I(K)M*O")
        buf.write("+Q,S-U.W/Y\60[\61]\62_\63a\64c\65e\66g\67i8k9m:o\2q\2")
        buf.write("s\2u\2w\2y;\3\2\6\4\2C\\c|\3\2\62;\4\2\13\13\"\"\4\2\f")
        buf.write("\f\16\17\2\u01a8\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2")
        buf.write("\2\2y\3\2\2\2\3\u008f\3\2\2\2\5\u0091\3\2\2\2\7\u009b")
        buf.write("\3\2\2\2\t\u00a3\3\2\2\2\13\u00aa\3\2\2\2\r\u00af\3\2")
        buf.write("\2\2\17\u00b8\3\2\2\2\21\u00bf\3\2\2\2\23\u00c6\3\2\2")
        buf.write("\2\25\u00cd\3\2\2\2\27\u00d4\3\2\2\2\31\u00dc\3\2\2\2")
        buf.write("\33\u00e3\3\2\2\2\35\u00f1\3\2\2\2\37\u00f7\3\2\2\2!\u00fa")
        buf.write("\3\2\2\2#\u00fc\3\2\2\2%\u00fe\3\2\2\2\'\u0101\3\2\2\2")
        buf.write(")\u0106\3\2\2\2+\u010b\3\2\2\2-\u010e\3\2\2\2/\u0113\3")
        buf.write("\2\2\2\61\u0119\3\2\2\2\63\u011d\3\2\2\2\65\u0120\3\2")
        buf.write("\2\2\67\u0124\3\2\2\29\u0129\3\2\2\2;\u012f\3\2\2\2=\u0132")
        buf.write("\3\2\2\2?\u0134\3\2\2\2A\u0137\3\2\2\2C\u013a\3\2\2\2")
        buf.write("E\u013d\3\2\2\2G\u0140\3\2\2\2I\u0143\3\2\2\2K\u0146\3")
        buf.write("\2\2\2M\u0149\3\2\2\2O\u014c\3\2\2\2Q\u014e\3\2\2\2S\u0150")
        buf.write("\3\2\2\2U\u0152\3\2\2\2W\u0154\3\2\2\2Y\u0156\3\2\2\2")
        buf.write("[\u0158\3\2\2\2]\u015a\3\2\2\2_\u015c\3\2\2\2a\u015e\3")
        buf.write("\2\2\2c\u0160\3\2\2\2e\u0162\3\2\2\2g\u0164\3\2\2\2i\u016c")
        buf.write("\3\2\2\2k\u0174\3\2\2\2m\u017f\3\2\2\2o\u0184\3\2\2\2")
        buf.write("q\u0189\3\2\2\2s\u018b\3\2\2\2u\u018e\3\2\2\2w\u0192\3")
        buf.write("\2\2\2y\u019b\3\2\2\2{}\7\17\2\2|{\3\2\2\2|}\3\2\2\2}")
        buf.write("~\3\2\2\2~\u0082\7\f\2\2\177\u0081\7\"\2\2\u0080\177\3")
        buf.write("\2\2\2\u0081\u0084\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0083")
        buf.write("\3\2\2\2\u0083\u0090\3\2\2\2\u0084\u0082\3\2\2\2\u0085")
        buf.write("\u0087\7\17\2\2\u0086\u0085\3\2\2\2\u0086\u0087\3\2\2")
        buf.write("\2\u0087\u0088\3\2\2\2\u0088\u008c\7\f\2\2\u0089\u008b")
        buf.write("\7\13\2\2\u008a\u0089\3\2\2\2\u008b\u008e\3\2\2\2\u008c")
        buf.write("\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u0090\3\2\2\2")
        buf.write("\u008e\u008c\3\2\2\2\u008f|\3\2\2\2\u008f\u0086\3\2\2")
        buf.write("\2\u0090\4\3\2\2\2\u0091\u0092\7R\2\2\u0092\u0093\7t\2")
        buf.write("\2\u0093\u0094\7g\2\2\u0094\u0095\7f\2\2\u0095\u0096\7")
        buf.write("k\2\2\u0096\u0097\7e\2\2\u0097\u0098\7c\2\2\u0098\u0099")
        buf.write("\7v\2\2\u0099\u009a\7g\2\2\u009a\6\3\2\2\2\u009b\u009c")
        buf.write("\7H\2\2\u009c\u009d\7g\2\2\u009d\u009e\7c\2\2\u009e\u009f")
        buf.write("\7v\2\2\u009f\u00a0\7w\2\2\u00a0\u00a1\7t\2\2\u00a1\u00a2")
        buf.write("\7g\2\2\u00a2\b\3\2\2\2\u00a3\u00a4\7H\2\2\u00a4\u00a5")
        buf.write("\7c\2\2\u00a5\u00a6\7e\2\2\u00a6\u00a7\7v\2\2\u00a7\u00a8")
        buf.write("\7q\2\2\u00a8\u00a9\7t\2\2\u00a9\n\3\2\2\2\u00aa\u00ab")
        buf.write("\7I\2\2\u00ab\u00ac\7q\2\2\u00ac\u00ad\7c\2\2\u00ad\u00ae")
        buf.write("\7n\2\2\u00ae\f\3\2\2\2\u00af\u00b0\7E\2\2\u00b0\u00b1")
        buf.write("\7q\2\2\u00b1\u00b2\7p\2\2\u00b2\u00b3\7u\2\2\u00b3\u00b4")
        buf.write("\7v\2\2\u00b4\u00b5\7c\2\2\u00b5\u00b6\7p\2\2\u00b6\u00b7")
        buf.write("\7v\2\2\u00b7\16\3\2\2\2\u00b8\u00b9\7C\2\2\u00b9\u00ba")
        buf.write("\7e\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc\7k\2\2\u00bc\u00bd")
        buf.write("\7q\2\2\u00bd\u00be\7p\2\2\u00be\20\3\2\2\2\u00bf\u00c0")
        buf.write("\7G\2\2\u00c0\u00c1\7h\2\2\u00c1\u00c2\7h\2\2\u00c2\u00c3")
        buf.write("\7g\2\2\u00c3\u00c4\7e\2\2\u00c4\u00c5\7v\2\2\u00c5\22")
        buf.write("\3\2\2\2\u00c6\u00c7\7T\2\2\u00c7\u00c8\7g\2\2\u00c8\u00c9")
        buf.write("\7y\2\2\u00c9\u00ca\7c\2\2\u00ca\u00cb\7t\2\2\u00cb\u00cc")
        buf.write("\7f\2\2\u00cc\24\3\2\2\2\u00cd\u00ce\7R\2\2\u00ce\u00cf")
        buf.write("\7q\2\2\u00cf\u00d0\7n\2\2\u00d0\u00d1\7k\2\2\u00d1\u00d2")
        buf.write("\7e\2\2\u00d2\u00d3\7{\2\2\u00d3\26\3\2\2\2\u00d4\u00d5")
        buf.write("\7G\2\2\u00d5\u00d6\7z\2\2\u00d6\u00d7\7g\2\2\u00d7\u00d8")
        buf.write("\7e\2\2\u00d8\u00d9\7w\2\2\u00d9\u00da\7v\2\2\u00da\u00db")
        buf.write("\7g\2\2\u00db\30\3\2\2\2\u00dc\u00dd\7Q\2\2\u00dd\u00de")
        buf.write("\7r\2\2\u00de\u00df\7v\2\2\u00df\u00e0\7k\2\2\u00e0\u00e1")
        buf.write("\7q\2\2\u00e1\u00e2\7p\2\2\u00e2\32\3\2\2\2\u00e3\u00e4")
        buf.write("\7O\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6\7t\2\2\u00e6\u00e7")
        buf.write("\7m\2\2\u00e7\u00e8\7q\2\2\u00e8\u00e9\7x\2\2\u00e9\u00ea")
        buf.write("\7H\2\2\u00ea\u00eb\7g\2\2\u00eb\u00ec\7c\2\2\u00ec\u00ed")
        buf.write("\7v\2\2\u00ed\u00ee\7w\2\2\u00ee\u00ef\7t\2\2\u00ef\u00f0")
        buf.write("\7g\2\2\u00f0\34\3\2\2\2\u00f1\u00f2\7x\2\2\u00f2\u00f3")
        buf.write("\7q\2\2\u00f3\u00f4\7e\2\2\u00f4\u00f5\7c\2\2\u00f5\u00f6")
        buf.write("\7d\2\2\u00f6\36\3\2\2\2\u00f7\u00f8\7U\2\2\u00f8\u00f9")
        buf.write("\7)\2\2\u00f9 \3\2\2\2\u00fa\u00fb\7U\2\2\u00fb\"\3\2")
        buf.write("\2\2\u00fc\u00fd\7C\2\2\u00fd$\3\2\2\2\u00fe\u00ff\7k")
        buf.write("\2\2\u00ff\u0100\7h\2\2\u0100&\3\2\2\2\u0101\u0102\7g")
        buf.write("\2\2\u0102\u0103\7n\2\2\u0103\u0104\7u\2\2\u0104\u0105")
        buf.write("\7g\2\2\u0105(\3\2\2\2\u0106\u0107\7g\2\2\u0107\u0108")
        buf.write("\7n\2\2\u0108\u0109\7k\2\2\u0109\u010a\7h\2\2\u010a*\3")
        buf.write("\2\2\2\u010b\u010c\7k\2\2\u010c\u010d\7p\2\2\u010d,\3")
        buf.write("\2\2\2\u010e\u010f\7k\2\2\u010f\u0110\7p\2\2\u0110\u0111")
        buf.write("\7k\2\2\u0111\u0112\7v\2\2\u0112.\3\2\2\2\u0113\u0114")
        buf.write("\7w\2\2\u0114\u0115\7p\2\2\u0115\u0116\7v\2\2\u0116\u0117")
        buf.write("\7k\2\2\u0117\u0118\7n\2\2\u0118\60\3\2\2\2\u0119\u011a")
        buf.write("\7c\2\2\u011a\u011b\7p\2\2\u011b\u011c\7f\2\2\u011c\62")
        buf.write("\3\2\2\2\u011d\u011e\7q\2\2\u011e\u011f\7t\2\2\u011f\64")
        buf.write("\3\2\2\2\u0120\u0121\7p\2\2\u0121\u0122\7q\2\2\u0122\u0123")
        buf.write("\7v\2\2\u0123\66\3\2\2\2\u0124\u0125\7V\2\2\u0125\u0126")
        buf.write("\7t\2\2\u0126\u0127\7w\2\2\u0127\u0128\7g\2\2\u01288\3")
        buf.write("\2\2\2\u0129\u012a\7H\2\2\u012a\u012b\7c\2\2\u012b\u012c")
        buf.write("\7n\2\2\u012c\u012d\7u\2\2\u012d\u012e\7g\2\2\u012e:\3")
        buf.write("\2\2\2\u012f\u0130\7<\2\2\u0130\u0131\7?\2\2\u0131<\3")
        buf.write("\2\2\2\u0132\u0133\7?\2\2\u0133>\3\2\2\2\u0134\u0135\7")
        buf.write(",\2\2\u0135\u0136\7?\2\2\u0136@\3\2\2\2\u0137\u0138\7")
        buf.write("\61\2\2\u0138\u0139\7?\2\2\u0139B\3\2\2\2\u013a\u013b")
        buf.write("\7-\2\2\u013b\u013c\7?\2\2\u013cD\3\2\2\2\u013d\u013e")
        buf.write("\7/\2\2\u013e\u013f\7?\2\2\u013fF\3\2\2\2\u0140\u0141")
        buf.write("\7?\2\2\u0141\u0142\7?\2\2\u0142H\3\2\2\2\u0143\u0144")
        buf.write("\7@\2\2\u0144\u0145\7?\2\2\u0145J\3\2\2\2\u0146\u0147")
        buf.write("\7>\2\2\u0147\u0148\7?\2\2\u0148L\3\2\2\2\u0149\u014a")
        buf.write("\7#\2\2\u014a\u014b\7?\2\2\u014bN\3\2\2\2\u014c\u014d")
        buf.write("\7<\2\2\u014dP\3\2\2\2\u014e\u014f\7.\2\2\u014fR\3\2\2")
        buf.write("\2\u0150\u0151\7]\2\2\u0151T\3\2\2\2\u0152\u0153\7_\2")
        buf.write("\2\u0153V\3\2\2\2\u0154\u0155\7*\2\2\u0155X\3\2\2\2\u0156")
        buf.write("\u0157\7+\2\2\u0157Z\3\2\2\2\u0158\u0159\7>\2\2\u0159")
        buf.write("\\\3\2\2\2\u015a\u015b\7@\2\2\u015b^\3\2\2\2\u015c\u015d")
        buf.write("\7,\2\2\u015d`\3\2\2\2\u015e\u015f\7\61\2\2\u015fb\3\2")
        buf.write("\2\2\u0160\u0161\7-\2\2\u0161d\3\2\2\2\u0162\u0163\7/")
        buf.write("\2\2\u0163f\3\2\2\2\u0164\u0165\5i\65\2\u0165\u0169\7")
        buf.write("\60\2\2\u0166\u0168\5o8\2\u0167\u0166\3\2\2\2\u0168\u016b")
        buf.write("\3\2\2\2\u0169\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016a")
        buf.write("h\3\2\2\2\u016b\u0169\3\2\2\2\u016c\u0170\5o8\2\u016d")
        buf.write("\u016f\5q9\2\u016e\u016d\3\2\2\2\u016f\u0172\3\2\2\2\u0170")
        buf.write("\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171j\3\2\2\2\u0172")
        buf.write("\u0170\3\2\2\2\u0173\u0175\5s:\2\u0174\u0173\3\2\2\2\u0175")
        buf.write("\u0176\3\2\2\2\u0176\u0174\3\2\2\2\u0176\u0177\3\2\2\2")
        buf.write("\u0177\u0178\3\2\2\2\u0178\u017a\7\60\2\2\u0179\u017b")
        buf.write("\5s:\2\u017a\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017a")
        buf.write("\3\2\2\2\u017c\u017d\3\2\2\2\u017dl\3\2\2\2\u017e\u0180")
        buf.write("\5s:\2\u017f\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u017f")
        buf.write("\3\2\2\2\u0181\u0182\3\2\2\2\u0182n\3\2\2\2\u0183\u0185")
        buf.write("\t\2\2\2\u0184\u0183\3\2\2\2\u0185p\3\2\2\2\u0186\u018a")
        buf.write("\5o8\2\u0187\u018a\5s:\2\u0188\u018a\7a\2\2\u0189\u0186")
        buf.write("\3\2\2\2\u0189\u0187\3\2\2\2\u0189\u0188\3\2\2\2\u018a")
        buf.write("r\3\2\2\2\u018b\u018c\t\3\2\2\u018ct\3\2\2\2\u018d\u018f")
        buf.write("\t\4\2\2\u018e\u018d\3\2\2\2\u018f\u0190\3\2\2\2\u0190")
        buf.write("\u018e\3\2\2\2\u0190\u0191\3\2\2\2\u0191v\3\2\2\2\u0192")
        buf.write("\u0196\7%\2\2\u0193\u0195\n\5\2\2\u0194\u0193\3\2\2\2")
        buf.write("\u0195\u0198\3\2\2\2\u0196\u0194\3\2\2\2\u0196\u0197\3")
        buf.write("\2\2\2\u0197x\3\2\2\2\u0198\u0196\3\2\2\2\u0199\u019c")
        buf.write("\5u;\2\u019a\u019c\5w<\2\u019b\u0199\3\2\2\2\u019b\u019a")
        buf.write("\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u019e\b=\2\2\u019e")
        buf.write("z\3\2\2\2\22\2|\u0082\u0086\u008c\u008f\u0169\u0170\u0176")
        buf.write("\u017c\u0181\u0184\u0189\u0190\u0196\u019b\3\b\2\2")
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
    VOCAB = 16
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

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Predicate'", "'Feature'", "'Factor'", "'Goal'", "'Constant'", 
            "'Action'", "'Effect'", "'Reward'", "'Policy'", "'Execute'", 
            "'Option'", "'MarkovFeature'", "'vocab'", "'S''", "'S'", "'A'", 
            "'if'", "'else'", "'elif'", "'in'", "'init'", "'until'", "'and'", 
            "'or'", "'not'", "'True'", "'False'", "':='", "'='", "'*='", 
            "'/='", "'+='", "'-='", "'=='", "'>='", "'<='", "'!='", "':'", 
            "','", "'['", "']'", "'('", "')'", "'<'", "'>'", "'*'", "'/'", 
            "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "NL", "PREDICATE", "FEATURE", "FACTOR", 
            "GOAL", "CONSTANT", "ACTION", "EFFECT", "REWARD", "POLICY", 
            "EXECUTE", "OPTION", "MARKOVFEATURE", "VOCAB", "S_PRIME", "S", 
            "A", "IF", "ELSE", "ELIF", "IN", "INIT", "UNTIL", "AND", "OR", 
            "NOT", "TRUE", "FALSE", "BIND", "ASSIGN", "TIMES_EQ", "DIV_EQ", 
            "PLUS_EQ", "MINUS_EQ", "EQ_TO", "GT_EQ", "LT_EQ", "NOT_EQ", 
            "COL", "COM", "L_BRK", "R_BRK", "L_PAR", "R_PAR", "LT", "GT", 
            "TIMES", "DIVIDE", "PLUS", "MINUS", "FNAME", "IDENTIFIER", "DECIMAL", 
            "INTEGER", "SKIP_" ]

    ruleNames = [ "NL", "PREDICATE", "FEATURE", "FACTOR", "GOAL", "CONSTANT", 
                  "ACTION", "EFFECT", "REWARD", "POLICY", "EXECUTE", "OPTION", 
                  "MARKOVFEATURE", "VOCAB", "S_PRIME", "S", "A", "IF", "ELSE", 
                  "ELIF", "IN", "INIT", "UNTIL", "AND", "OR", "NOT", "TRUE", 
                  "FALSE", "BIND", "ASSIGN", "TIMES_EQ", "DIV_EQ", "PLUS_EQ", 
                  "MINUS_EQ", "EQ_TO", "GT_EQ", "LT_EQ", "NOT_EQ", "COL", 
                  "COM", "L_BRK", "R_BRK", "L_PAR", "R_PAR", "LT", "GT", 
                  "TIMES", "DIVIDE", "PLUS", "MINUS", "FNAME", "IDENTIFIER", 
                  "DECIMAL", "INTEGER", "LETTER", "ANY_CHAR", "DIGIT", "SPACES", 
                  "COMMENT", "SKIP_" ]

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



