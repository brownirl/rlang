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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u01b8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\5")
        buf.write("\2\u0087\n\2\3\2\3\2\7\2\u008b\n\2\f\2\16\2\u008e\13\2")
        buf.write("\3\2\5\2\u0091\n\2\3\2\3\2\7\2\u0095\n\2\f\2\16\2\u0098")
        buf.write("\13\2\5\2\u009a\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3")
        buf.write("%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3")
        buf.write("*\3+\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61")
        buf.write("\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67")
        buf.write("\3\67\38\38\38\78\u017f\n8\f8\168\u0182\138\39\39\79\u0186")
        buf.write("\n9\f9\169\u0189\139\3:\6:\u018c\n:\r:\16:\u018d\3:\3")
        buf.write(":\6:\u0192\n:\r:\16:\u0193\3;\6;\u0197\n;\r;\16;\u0198")
        buf.write("\3<\5<\u019c\n<\3=\3=\3=\5=\u01a1\n=\3>\3>\3?\6?\u01a6")
        buf.write("\n?\r?\16?\u01a7\3@\3@\7@\u01ac\n@\f@\16@\u01af\13@\3")
        buf.write("A\3A\5A\u01b3\nA\3A\3A\3B\3B\2\2C\3\5\5\6\7\7\t\b\13\t")
        buf.write("\r\n\17\13\21\f\23\r\25\16\27\17\31\20\33\21\35\22\37")
        buf.write("\23!\24#\25%\26\'\27)\30+\31-\32/\33\61\34\63\35\65\36")
        buf.write("\67\379 ;!=\"?#A$C%E&G\'I(K)M*O+Q,S-U.W/Y\60[\61]\62_")
        buf.write("\63a\64c\65e\66g\67i8k9m:o;q<s=u>w\2y\2{\2}\2\177\2\u0081")
        buf.write("?\u0083@\3\2\6\4\2C\\c|\3\2\62;\4\2\13\13\"\"\4\2\f\f")
        buf.write("\16\17\2\u01c1\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2")
        buf.write("\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2")
        buf.write("\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2\u0081\3\2")
        buf.write("\2\2\2\u0083\3\2\2\2\3\u0099\3\2\2\2\5\u009b\3\2\2\2\7")
        buf.write("\u00a5\3\2\2\2\t\u00ad\3\2\2\2\13\u00b4\3\2\2\2\r\u00b9")
        buf.write("\3\2\2\2\17\u00c2\3\2\2\2\21\u00c9\3\2\2\2\23\u00d0\3")
        buf.write("\2\2\2\25\u00d7\3\2\2\2\27\u00de\3\2\2\2\31\u00e6\3\2")
        buf.write("\2\2\33\u00ed\3\2\2\2\35\u00fb\3\2\2\2\37\u0102\3\2\2")
        buf.write("\2!\u0105\3\2\2\2#\u0107\3\2\2\2%\u0109\3\2\2\2\'\u010b")
        buf.write("\3\2\2\2)\u010d\3\2\2\2+\u0110\3\2\2\2-\u0115\3\2\2\2")
        buf.write("/\u011a\3\2\2\2\61\u011d\3\2\2\2\63\u0122\3\2\2\2\65\u0128")
        buf.write("\3\2\2\2\67\u012d\3\2\2\29\u0131\3\2\2\2;\u0134\3\2\2")
        buf.write("\2=\u0138\3\2\2\2?\u013d\3\2\2\2A\u0143\3\2\2\2C\u0146")
        buf.write("\3\2\2\2E\u0149\3\2\2\2G\u014b\3\2\2\2I\u014e\3\2\2\2")
        buf.write("K\u0151\3\2\2\2M\u0154\3\2\2\2O\u0157\3\2\2\2Q\u015a\3")
        buf.write("\2\2\2S\u015d\3\2\2\2U\u0160\3\2\2\2W\u0163\3\2\2\2Y\u0165")
        buf.write("\3\2\2\2[\u0167\3\2\2\2]\u0169\3\2\2\2_\u016b\3\2\2\2")
        buf.write("a\u016d\3\2\2\2c\u016f\3\2\2\2e\u0171\3\2\2\2g\u0173\3")
        buf.write("\2\2\2i\u0175\3\2\2\2k\u0177\3\2\2\2m\u0179\3\2\2\2o\u017b")
        buf.write("\3\2\2\2q\u0183\3\2\2\2s\u018b\3\2\2\2u\u0196\3\2\2\2")
        buf.write("w\u019b\3\2\2\2y\u01a0\3\2\2\2{\u01a2\3\2\2\2}\u01a5\3")
        buf.write("\2\2\2\177\u01a9\3\2\2\2\u0081\u01b2\3\2\2\2\u0083\u01b6")
        buf.write("\3\2\2\2\u0085\u0087\7\17\2\2\u0086\u0085\3\2\2\2\u0086")
        buf.write("\u0087\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u008c\7\f\2\2")
        buf.write("\u0089\u008b\7\"\2\2\u008a\u0089\3\2\2\2\u008b\u008e\3")
        buf.write("\2\2\2\u008c\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u009a")
        buf.write("\3\2\2\2\u008e\u008c\3\2\2\2\u008f\u0091\7\17\2\2\u0090")
        buf.write("\u008f\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u0092\3\2\2\2")
        buf.write("\u0092\u0096\7\f\2\2\u0093\u0095\7\13\2\2\u0094\u0093")
        buf.write("\3\2\2\2\u0095\u0098\3\2\2\2\u0096\u0094\3\2\2\2\u0096")
        buf.write("\u0097\3\2\2\2\u0097\u009a\3\2\2\2\u0098\u0096\3\2\2\2")
        buf.write("\u0099\u0086\3\2\2\2\u0099\u0090\3\2\2\2\u009a\4\3\2\2")
        buf.write("\2\u009b\u009c\7R\2\2\u009c\u009d\7t\2\2\u009d\u009e\7")
        buf.write("g\2\2\u009e\u009f\7f\2\2\u009f\u00a0\7k\2\2\u00a0\u00a1")
        buf.write("\7e\2\2\u00a1\u00a2\7c\2\2\u00a2\u00a3\7v\2\2\u00a3\u00a4")
        buf.write("\7g\2\2\u00a4\6\3\2\2\2\u00a5\u00a6\7H\2\2\u00a6\u00a7")
        buf.write("\7g\2\2\u00a7\u00a8\7c\2\2\u00a8\u00a9\7v\2\2\u00a9\u00aa")
        buf.write("\7w\2\2\u00aa\u00ab\7t\2\2\u00ab\u00ac\7g\2\2\u00ac\b")
        buf.write("\3\2\2\2\u00ad\u00ae\7H\2\2\u00ae\u00af\7c\2\2\u00af\u00b0")
        buf.write("\7e\2\2\u00b0\u00b1\7v\2\2\u00b1\u00b2\7q\2\2\u00b2\u00b3")
        buf.write("\7t\2\2\u00b3\n\3\2\2\2\u00b4\u00b5\7I\2\2\u00b5\u00b6")
        buf.write("\7q\2\2\u00b6\u00b7\7c\2\2\u00b7\u00b8\7n\2\2\u00b8\f")
        buf.write("\3\2\2\2\u00b9\u00ba\7E\2\2\u00ba\u00bb\7q\2\2\u00bb\u00bc")
        buf.write("\7p\2\2\u00bc\u00bd\7u\2\2\u00bd\u00be\7v\2\2\u00be\u00bf")
        buf.write("\7c\2\2\u00bf\u00c0\7p\2\2\u00c0\u00c1\7v\2\2\u00c1\16")
        buf.write("\3\2\2\2\u00c2\u00c3\7C\2\2\u00c3\u00c4\7e\2\2\u00c4\u00c5")
        buf.write("\7v\2\2\u00c5\u00c6\7k\2\2\u00c6\u00c7\7q\2\2\u00c7\u00c8")
        buf.write("\7p\2\2\u00c8\20\3\2\2\2\u00c9\u00ca\7G\2\2\u00ca\u00cb")
        buf.write("\7h\2\2\u00cb\u00cc\7h\2\2\u00cc\u00cd\7g\2\2\u00cd\u00ce")
        buf.write("\7e\2\2\u00ce\u00cf\7v\2\2\u00cf\22\3\2\2\2\u00d0\u00d1")
        buf.write("\7T\2\2\u00d1\u00d2\7g\2\2\u00d2\u00d3\7y\2\2\u00d3\u00d4")
        buf.write("\7c\2\2\u00d4\u00d5\7t\2\2\u00d5\u00d6\7f\2\2\u00d6\24")
        buf.write("\3\2\2\2\u00d7\u00d8\7R\2\2\u00d8\u00d9\7q\2\2\u00d9\u00da")
        buf.write("\7n\2\2\u00da\u00db\7k\2\2\u00db\u00dc\7e\2\2\u00dc\u00dd")
        buf.write("\7{\2\2\u00dd\26\3\2\2\2\u00de\u00df\7G\2\2\u00df\u00e0")
        buf.write("\7z\2\2\u00e0\u00e1\7g\2\2\u00e1\u00e2\7e\2\2\u00e2\u00e3")
        buf.write("\7w\2\2\u00e3\u00e4\7v\2\2\u00e4\u00e5\7g\2\2\u00e5\30")
        buf.write("\3\2\2\2\u00e6\u00e7\7Q\2\2\u00e7\u00e8\7r\2\2\u00e8\u00e9")
        buf.write("\7v\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb\7q\2\2\u00eb\u00ec")
        buf.write("\7p\2\2\u00ec\32\3\2\2\2\u00ed\u00ee\7O\2\2\u00ee\u00ef")
        buf.write("\7c\2\2\u00ef\u00f0\7t\2\2\u00f0\u00f1\7m\2\2\u00f1\u00f2")
        buf.write("\7q\2\2\u00f2\u00f3\7x\2\2\u00f3\u00f4\7H\2\2\u00f4\u00f5")
        buf.write("\7g\2\2\u00f5\u00f6\7c\2\2\u00f6\u00f7\7v\2\2\u00f7\u00f8")
        buf.write("\7w\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa\7g\2\2\u00fa\34")
        buf.write("\3\2\2\2\u00fb\u00fc\7k\2\2\u00fc\u00fd\7o\2\2\u00fd\u00fe")
        buf.write("\7r\2\2\u00fe\u00ff\7q\2\2\u00ff\u0100\7t\2\2\u0100\u0101")
        buf.write("\7v\2\2\u0101\36\3\2\2\2\u0102\u0103\5!\21\2\u0103\u0104")
        buf.write("\5\'\24\2\u0104 \3\2\2\2\u0105\u0106\7U\2\2\u0106\"\3")
        buf.write("\2\2\2\u0107\u0108\7C\2\2\u0108$\3\2\2\2\u0109\u010a\7")
        buf.write("R\2\2\u010a&\3\2\2\2\u010b\u010c\7)\2\2\u010c(\3\2\2\2")
        buf.write("\u010d\u010e\7k\2\2\u010e\u010f\7h\2\2\u010f*\3\2\2\2")
        buf.write("\u0110\u0111\7g\2\2\u0111\u0112\7n\2\2\u0112\u0113\7u")
        buf.write("\2\2\u0113\u0114\7g\2\2\u0114,\3\2\2\2\u0115\u0116\7g")
        buf.write("\2\2\u0116\u0117\7n\2\2\u0117\u0118\7k\2\2\u0118\u0119")
        buf.write("\7h\2\2\u0119.\3\2\2\2\u011a\u011b\7k\2\2\u011b\u011c")
        buf.write("\7p\2\2\u011c\60\3\2\2\2\u011d\u011e\7k\2\2\u011e\u011f")
        buf.write("\7p\2\2\u011f\u0120\7k\2\2\u0120\u0121\7v\2\2\u0121\62")
        buf.write("\3\2\2\2\u0122\u0123\7w\2\2\u0123\u0124\7p\2\2\u0124\u0125")
        buf.write("\7v\2\2\u0125\u0126\7k\2\2\u0126\u0127\7n\2\2\u0127\64")
        buf.write("\3\2\2\2\u0128\u0129\7y\2\2\u0129\u012a\7k\2\2\u012a\u012b")
        buf.write("\7v\2\2\u012b\u012c\7j\2\2\u012c\66\3\2\2\2\u012d\u012e")
        buf.write("\7c\2\2\u012e\u012f\7p\2\2\u012f\u0130\7f\2\2\u01308\3")
        buf.write("\2\2\2\u0131\u0132\7q\2\2\u0132\u0133\7t\2\2\u0133:\3")
        buf.write("\2\2\2\u0134\u0135\7p\2\2\u0135\u0136\7q\2\2\u0136\u0137")
        buf.write("\7v\2\2\u0137<\3\2\2\2\u0138\u0139\7V\2\2\u0139\u013a")
        buf.write("\7t\2\2\u013a\u013b\7w\2\2\u013b\u013c\7g\2\2\u013c>\3")
        buf.write("\2\2\2\u013d\u013e\7H\2\2\u013e\u013f\7c\2\2\u013f\u0140")
        buf.write("\7n\2\2\u0140\u0141\7u\2\2\u0141\u0142\7g\2\2\u0142@\3")
        buf.write("\2\2\2\u0143\u0144\7<\2\2\u0144\u0145\7?\2\2\u0145B\3")
        buf.write("\2\2\2\u0146\u0147\7/\2\2\u0147\u0148\7@\2\2\u0148D\3")
        buf.write("\2\2\2\u0149\u014a\7?\2\2\u014aF\3\2\2\2\u014b\u014c\7")
        buf.write(",\2\2\u014c\u014d\7?\2\2\u014dH\3\2\2\2\u014e\u014f\7")
        buf.write("\61\2\2\u014f\u0150\7?\2\2\u0150J\3\2\2\2\u0151\u0152")
        buf.write("\7-\2\2\u0152\u0153\7?\2\2\u0153L\3\2\2\2\u0154\u0155")
        buf.write("\7/\2\2\u0155\u0156\7?\2\2\u0156N\3\2\2\2\u0157\u0158")
        buf.write("\7?\2\2\u0158\u0159\7?\2\2\u0159P\3\2\2\2\u015a\u015b")
        buf.write("\7@\2\2\u015b\u015c\7?\2\2\u015cR\3\2\2\2\u015d\u015e")
        buf.write("\7>\2\2\u015e\u015f\7?\2\2\u015fT\3\2\2\2\u0160\u0161")
        buf.write("\7#\2\2\u0161\u0162\7?\2\2\u0162V\3\2\2\2\u0163\u0164")
        buf.write("\7<\2\2\u0164X\3\2\2\2\u0165\u0166\7.\2\2\u0166Z\3\2\2")
        buf.write("\2\u0167\u0168\7]\2\2\u0168\\\3\2\2\2\u0169\u016a\7_\2")
        buf.write("\2\u016a^\3\2\2\2\u016b\u016c\7*\2\2\u016c`\3\2\2\2\u016d")
        buf.write("\u016e\7+\2\2\u016eb\3\2\2\2\u016f\u0170\7>\2\2\u0170")
        buf.write("d\3\2\2\2\u0171\u0172\7@\2\2\u0172f\3\2\2\2\u0173\u0174")
        buf.write("\7,\2\2\u0174h\3\2\2\2\u0175\u0176\7\61\2\2\u0176j\3\2")
        buf.write("\2\2\u0177\u0178\7-\2\2\u0178l\3\2\2\2\u0179\u017a\7/")
        buf.write("\2\2\u017an\3\2\2\2\u017b\u017c\5q9\2\u017c\u0180\7\60")
        buf.write("\2\2\u017d\u017f\5w<\2\u017e\u017d\3\2\2\2\u017f\u0182")
        buf.write("\3\2\2\2\u0180\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181")
        buf.write("p\3\2\2\2\u0182\u0180\3\2\2\2\u0183\u0187\5w<\2\u0184")
        buf.write("\u0186\5y=\2\u0185\u0184\3\2\2\2\u0186\u0189\3\2\2\2\u0187")
        buf.write("\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188r\3\2\2\2\u0189")
        buf.write("\u0187\3\2\2\2\u018a\u018c\5{>\2\u018b\u018a\3\2\2\2\u018c")
        buf.write("\u018d\3\2\2\2\u018d\u018b\3\2\2\2\u018d\u018e\3\2\2\2")
        buf.write("\u018e\u018f\3\2\2\2\u018f\u0191\7\60\2\2\u0190\u0192")
        buf.write("\5{>\2\u0191\u0190\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0191")
        buf.write("\3\2\2\2\u0193\u0194\3\2\2\2\u0194t\3\2\2\2\u0195\u0197")
        buf.write("\5{>\2\u0196\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u0196")
        buf.write("\3\2\2\2\u0198\u0199\3\2\2\2\u0199v\3\2\2\2\u019a\u019c")
        buf.write("\t\2\2\2\u019b\u019a\3\2\2\2\u019cx\3\2\2\2\u019d\u01a1")
        buf.write("\5w<\2\u019e\u01a1\5{>\2\u019f\u01a1\7a\2\2\u01a0\u019d")
        buf.write("\3\2\2\2\u01a0\u019e\3\2\2\2\u01a0\u019f\3\2\2\2\u01a1")
        buf.write("z\3\2\2\2\u01a2\u01a3\t\3\2\2\u01a3|\3\2\2\2\u01a4\u01a6")
        buf.write("\t\4\2\2\u01a5\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7")
        buf.write("\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8~\3\2\2\2\u01a9")
        buf.write("\u01ad\7%\2\2\u01aa\u01ac\n\5\2\2\u01ab\u01aa\3\2\2\2")
        buf.write("\u01ac\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3")
        buf.write("\2\2\2\u01ae\u0080\3\2\2\2\u01af\u01ad\3\2\2\2\u01b0\u01b3")
        buf.write("\5}?\2\u01b1\u01b3\5\177@\2\u01b2\u01b0\3\2\2\2\u01b2")
        buf.write("\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b5\bA\2\2")
        buf.write("\u01b5\u0082\3\2\2\2\u01b6\u01b7\13\2\2\2\u01b7\u0084")
        buf.write("\3\2\2\2\22\2\u0086\u008c\u0090\u0096\u0099\u0180\u0187")
        buf.write("\u018d\u0193\u0198\u019b\u01a0\u01a7\u01ad\u01b2\3\b\2")
        buf.write("\2")
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
    AND = 29
    OR = 30
    NOT = 31
    TRUE = 32
    FALSE = 33
    BIND = 34
    PREDICT = 35
    ASSIGN = 36
    TIMES_EQ = 37
    DIV_EQ = 38
    PLUS_EQ = 39
    MINUS_EQ = 40
    EQ_TO = 41
    GT_EQ = 42
    LT_EQ = 43
    NOT_EQ = 44
    COL = 45
    COM = 46
    L_BRK = 47
    R_BRK = 48
    L_PAR = 49
    R_PAR = 50
    LT = 51
    GT = 52
    TIMES = 53
    DIVIDE = 54
    PLUS = 55
    MINUS = 56
    FNAME = 57
    IDENTIFIER = 58
    DECIMAL = 59
    INTEGER = 60
    SKIP_ = 61
    ANY = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Predicate'", "'Feature'", "'Factor'", "'Goal'", "'Constant'", 
            "'Action'", "'Effect'", "'Reward'", "'Policy'", "'Execute'", 
            "'Option'", "'MarkovFeature'", "'import'", "'S'", "'A'", "'P'", 
            "'''", "'if'", "'else'", "'elif'", "'in'", "'init'", "'until'", 
            "'with'", "'and'", "'or'", "'not'", "'True'", "'False'", "':='", 
            "'->'", "'='", "'*='", "'/='", "'+='", "'-='", "'=='", "'>='", 
            "'<='", "'!='", "':'", "','", "'['", "']'", "'('", "')'", "'<'", 
            "'>'", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "NL", "PREDICATE", "FEATURE", "FACTOR", 
            "GOAL", "CONSTANT", "ACTION", "EFFECT", "REWARD", "POLICY", 
            "EXECUTE", "OPTION", "MARKOVFEATURE", "IMPORT", "S_PRIME", "S", 
            "A", "P", "PRIME", "IF", "ELSE", "ELIF", "IN", "INIT", "UNTIL", 
            "WITH", "AND", "OR", "NOT", "TRUE", "FALSE", "BIND", "PREDICT", 
            "ASSIGN", "TIMES_EQ", "DIV_EQ", "PLUS_EQ", "MINUS_EQ", "EQ_TO", 
            "GT_EQ", "LT_EQ", "NOT_EQ", "COL", "COM", "L_BRK", "R_BRK", 
            "L_PAR", "R_PAR", "LT", "GT", "TIMES", "DIVIDE", "PLUS", "MINUS", 
            "FNAME", "IDENTIFIER", "DECIMAL", "INTEGER", "SKIP_", "ANY" ]

    ruleNames = [ "NL", "PREDICATE", "FEATURE", "FACTOR", "GOAL", "CONSTANT", 
                  "ACTION", "EFFECT", "REWARD", "POLICY", "EXECUTE", "OPTION", 
                  "MARKOVFEATURE", "IMPORT", "S_PRIME", "S", "A", "P", "PRIME", 
                  "IF", "ELSE", "ELIF", "IN", "INIT", "UNTIL", "WITH", "AND", 
                  "OR", "NOT", "TRUE", "FALSE", "BIND", "PREDICT", "ASSIGN", 
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



