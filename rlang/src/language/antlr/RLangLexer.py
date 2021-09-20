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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2=")
        buf.write("\u01a8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\3\2\5\2\u0081\n\2\3\2\3")
        buf.write("\2\7\2\u0085\n\2\f\2\16\2\u0088\13\2\3\2\5\2\u008b\n\2")
        buf.write("\3\2\3\2\7\2\u008f\n\2\f\2\16\2\u0092\13\2\5\2\u0094\n")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'")
        buf.write("\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.")
        buf.write("\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3")
        buf.write("\64\3\65\3\65\3\65\7\65\u016f\n\65\f\65\16\65\u0172\13")
        buf.write("\65\3\66\3\66\7\66\u0176\n\66\f\66\16\66\u0179\13\66\3")
        buf.write("\67\6\67\u017c\n\67\r\67\16\67\u017d\3\67\3\67\6\67\u0182")
        buf.write("\n\67\r\67\16\67\u0183\38\68\u0187\n8\r8\168\u0188\39")
        buf.write("\59\u018c\n9\3:\3:\3:\5:\u0191\n:\3;\3;\3<\6<\u0196\n")
        buf.write("<\r<\16<\u0197\3=\3=\7=\u019c\n=\f=\16=\u019f\13=\3>\3")
        buf.write(">\5>\u01a3\n>\3>\3>\3?\3?\2\2@\3\5\5\6\7\7\t\b\13\t\r")
        buf.write("\n\17\13\21\f\23\r\25\16\27\17\31\20\33\21\35\22\37\23")
        buf.write("!\24#\25%\26\'\27)\30+\31-\32/\33\61\34\63\35\65\36\67")
        buf.write("\379 ;!=\"?#A$C%E&G\'I(K)M*O+Q,S-U.W/Y\60[\61]\62_\63")
        buf.write("a\64c\65e\66g\67i8k9m:o;q\2s\2u\2w\2y\2{<}=\3\2\6\4\2")
        buf.write("C\\c|\3\2\62;\4\2\13\13\"\"\4\2\f\f\16\17\2\u01b1\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2{")
        buf.write("\3\2\2\2\2}\3\2\2\2\3\u0093\3\2\2\2\5\u0095\3\2\2\2\7")
        buf.write("\u009f\3\2\2\2\t\u00a7\3\2\2\2\13\u00ae\3\2\2\2\r\u00b3")
        buf.write("\3\2\2\2\17\u00bc\3\2\2\2\21\u00c3\3\2\2\2\23\u00ca\3")
        buf.write("\2\2\2\25\u00d1\3\2\2\2\27\u00d8\3\2\2\2\31\u00e0\3\2")
        buf.write("\2\2\33\u00e7\3\2\2\2\35\u00f5\3\2\2\2\37\u00fc\3\2\2")
        buf.write("\2!\u00ff\3\2\2\2#\u0101\3\2\2\2%\u0103\3\2\2\2\'\u0105")
        buf.write("\3\2\2\2)\u0108\3\2\2\2+\u010d\3\2\2\2-\u0112\3\2\2\2")
        buf.write("/\u0115\3\2\2\2\61\u011a\3\2\2\2\63\u0120\3\2\2\2\65\u0124")
        buf.write("\3\2\2\2\67\u0127\3\2\2\29\u012b\3\2\2\2;\u0130\3\2\2")
        buf.write("\2=\u0136\3\2\2\2?\u0139\3\2\2\2A\u013b\3\2\2\2C\u013e")
        buf.write("\3\2\2\2E\u0141\3\2\2\2G\u0144\3\2\2\2I\u0147\3\2\2\2")
        buf.write("K\u014a\3\2\2\2M\u014d\3\2\2\2O\u0150\3\2\2\2Q\u0153\3")
        buf.write("\2\2\2S\u0155\3\2\2\2U\u0157\3\2\2\2W\u0159\3\2\2\2Y\u015b")
        buf.write("\3\2\2\2[\u015d\3\2\2\2]\u015f\3\2\2\2_\u0161\3\2\2\2")
        buf.write("a\u0163\3\2\2\2c\u0165\3\2\2\2e\u0167\3\2\2\2g\u0169\3")
        buf.write("\2\2\2i\u016b\3\2\2\2k\u0173\3\2\2\2m\u017b\3\2\2\2o\u0186")
        buf.write("\3\2\2\2q\u018b\3\2\2\2s\u0190\3\2\2\2u\u0192\3\2\2\2")
        buf.write("w\u0195\3\2\2\2y\u0199\3\2\2\2{\u01a2\3\2\2\2}\u01a6\3")
        buf.write("\2\2\2\177\u0081\7\17\2\2\u0080\177\3\2\2\2\u0080\u0081")
        buf.write("\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0086\7\f\2\2\u0083")
        buf.write("\u0085\7\"\2\2\u0084\u0083\3\2\2\2\u0085\u0088\3\2\2\2")
        buf.write("\u0086\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0094\3")
        buf.write("\2\2\2\u0088\u0086\3\2\2\2\u0089\u008b\7\17\2\2\u008a")
        buf.write("\u0089\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u008c\3\2\2\2")
        buf.write("\u008c\u0090\7\f\2\2\u008d\u008f\7\13\2\2\u008e\u008d")
        buf.write("\3\2\2\2\u008f\u0092\3\2\2\2\u0090\u008e\3\2\2\2\u0090")
        buf.write("\u0091\3\2\2\2\u0091\u0094\3\2\2\2\u0092\u0090\3\2\2\2")
        buf.write("\u0093\u0080\3\2\2\2\u0093\u008a\3\2\2\2\u0094\4\3\2\2")
        buf.write("\2\u0095\u0096\7R\2\2\u0096\u0097\7t\2\2\u0097\u0098\7")
        buf.write("g\2\2\u0098\u0099\7f\2\2\u0099\u009a\7k\2\2\u009a\u009b")
        buf.write("\7e\2\2\u009b\u009c\7c\2\2\u009c\u009d\7v\2\2\u009d\u009e")
        buf.write("\7g\2\2\u009e\6\3\2\2\2\u009f\u00a0\7H\2\2\u00a0\u00a1")
        buf.write("\7g\2\2\u00a1\u00a2\7c\2\2\u00a2\u00a3\7v\2\2\u00a3\u00a4")
        buf.write("\7w\2\2\u00a4\u00a5\7t\2\2\u00a5\u00a6\7g\2\2\u00a6\b")
        buf.write("\3\2\2\2\u00a7\u00a8\7H\2\2\u00a8\u00a9\7c\2\2\u00a9\u00aa")
        buf.write("\7e\2\2\u00aa\u00ab\7v\2\2\u00ab\u00ac\7q\2\2\u00ac\u00ad")
        buf.write("\7t\2\2\u00ad\n\3\2\2\2\u00ae\u00af\7I\2\2\u00af\u00b0")
        buf.write("\7q\2\2\u00b0\u00b1\7c\2\2\u00b1\u00b2\7n\2\2\u00b2\f")
        buf.write("\3\2\2\2\u00b3\u00b4\7E\2\2\u00b4\u00b5\7q\2\2\u00b5\u00b6")
        buf.write("\7p\2\2\u00b6\u00b7\7u\2\2\u00b7\u00b8\7v\2\2\u00b8\u00b9")
        buf.write("\7c\2\2\u00b9\u00ba\7p\2\2\u00ba\u00bb\7v\2\2\u00bb\16")
        buf.write("\3\2\2\2\u00bc\u00bd\7C\2\2\u00bd\u00be\7e\2\2\u00be\u00bf")
        buf.write("\7v\2\2\u00bf\u00c0\7k\2\2\u00c0\u00c1\7q\2\2\u00c1\u00c2")
        buf.write("\7p\2\2\u00c2\20\3\2\2\2\u00c3\u00c4\7G\2\2\u00c4\u00c5")
        buf.write("\7h\2\2\u00c5\u00c6\7h\2\2\u00c6\u00c7\7g\2\2\u00c7\u00c8")
        buf.write("\7e\2\2\u00c8\u00c9\7v\2\2\u00c9\22\3\2\2\2\u00ca\u00cb")
        buf.write("\7T\2\2\u00cb\u00cc\7g\2\2\u00cc\u00cd\7y\2\2\u00cd\u00ce")
        buf.write("\7c\2\2\u00ce\u00cf\7t\2\2\u00cf\u00d0\7f\2\2\u00d0\24")
        buf.write("\3\2\2\2\u00d1\u00d2\7R\2\2\u00d2\u00d3\7q\2\2\u00d3\u00d4")
        buf.write("\7n\2\2\u00d4\u00d5\7k\2\2\u00d5\u00d6\7e\2\2\u00d6\u00d7")
        buf.write("\7{\2\2\u00d7\26\3\2\2\2\u00d8\u00d9\7G\2\2\u00d9\u00da")
        buf.write("\7z\2\2\u00da\u00db\7g\2\2\u00db\u00dc\7e\2\2\u00dc\u00dd")
        buf.write("\7w\2\2\u00dd\u00de\7v\2\2\u00de\u00df\7g\2\2\u00df\30")
        buf.write("\3\2\2\2\u00e0\u00e1\7Q\2\2\u00e1\u00e2\7r\2\2\u00e2\u00e3")
        buf.write("\7v\2\2\u00e3\u00e4\7k\2\2\u00e4\u00e5\7q\2\2\u00e5\u00e6")
        buf.write("\7p\2\2\u00e6\32\3\2\2\2\u00e7\u00e8\7O\2\2\u00e8\u00e9")
        buf.write("\7c\2\2\u00e9\u00ea\7t\2\2\u00ea\u00eb\7m\2\2\u00eb\u00ec")
        buf.write("\7q\2\2\u00ec\u00ed\7x\2\2\u00ed\u00ee\7H\2\2\u00ee\u00ef")
        buf.write("\7g\2\2\u00ef\u00f0\7c\2\2\u00f0\u00f1\7v\2\2\u00f1\u00f2")
        buf.write("\7w\2\2\u00f2\u00f3\7t\2\2\u00f3\u00f4\7g\2\2\u00f4\34")
        buf.write("\3\2\2\2\u00f5\u00f6\7k\2\2\u00f6\u00f7\7o\2\2\u00f7\u00f8")
        buf.write("\7r\2\2\u00f8\u00f9\7q\2\2\u00f9\u00fa\7t\2\2\u00fa\u00fb")
        buf.write("\7v\2\2\u00fb\36\3\2\2\2\u00fc\u00fd\5!\21\2\u00fd\u00fe")
        buf.write("\5%\23\2\u00fe \3\2\2\2\u00ff\u0100\7U\2\2\u0100\"\3\2")
        buf.write("\2\2\u0101\u0102\7C\2\2\u0102$\3\2\2\2\u0103\u0104\7)")
        buf.write("\2\2\u0104&\3\2\2\2\u0105\u0106\7k\2\2\u0106\u0107\7h")
        buf.write("\2\2\u0107(\3\2\2\2\u0108\u0109\7g\2\2\u0109\u010a\7n")
        buf.write("\2\2\u010a\u010b\7u\2\2\u010b\u010c\7g\2\2\u010c*\3\2")
        buf.write("\2\2\u010d\u010e\7g\2\2\u010e\u010f\7n\2\2\u010f\u0110")
        buf.write("\7k\2\2\u0110\u0111\7h\2\2\u0111,\3\2\2\2\u0112\u0113")
        buf.write("\7k\2\2\u0113\u0114\7p\2\2\u0114.\3\2\2\2\u0115\u0116")
        buf.write("\7k\2\2\u0116\u0117\7p\2\2\u0117\u0118\7k\2\2\u0118\u0119")
        buf.write("\7v\2\2\u0119\60\3\2\2\2\u011a\u011b\7w\2\2\u011b\u011c")
        buf.write("\7p\2\2\u011c\u011d\7v\2\2\u011d\u011e\7k\2\2\u011e\u011f")
        buf.write("\7n\2\2\u011f\62\3\2\2\2\u0120\u0121\7c\2\2\u0121\u0122")
        buf.write("\7p\2\2\u0122\u0123\7f\2\2\u0123\64\3\2\2\2\u0124\u0125")
        buf.write("\7q\2\2\u0125\u0126\7t\2\2\u0126\66\3\2\2\2\u0127\u0128")
        buf.write("\7p\2\2\u0128\u0129\7q\2\2\u0129\u012a\7v\2\2\u012a8\3")
        buf.write("\2\2\2\u012b\u012c\7V\2\2\u012c\u012d\7t\2\2\u012d\u012e")
        buf.write("\7w\2\2\u012e\u012f\7g\2\2\u012f:\3\2\2\2\u0130\u0131")
        buf.write("\7H\2\2\u0131\u0132\7c\2\2\u0132\u0133\7n\2\2\u0133\u0134")
        buf.write("\7u\2\2\u0134\u0135\7g\2\2\u0135<\3\2\2\2\u0136\u0137")
        buf.write("\7<\2\2\u0137\u0138\7?\2\2\u0138>\3\2\2\2\u0139\u013a")
        buf.write("\7?\2\2\u013a@\3\2\2\2\u013b\u013c\7,\2\2\u013c\u013d")
        buf.write("\7?\2\2\u013dB\3\2\2\2\u013e\u013f\7\61\2\2\u013f\u0140")
        buf.write("\7?\2\2\u0140D\3\2\2\2\u0141\u0142\7-\2\2\u0142\u0143")
        buf.write("\7?\2\2\u0143F\3\2\2\2\u0144\u0145\7/\2\2\u0145\u0146")
        buf.write("\7?\2\2\u0146H\3\2\2\2\u0147\u0148\7?\2\2\u0148\u0149")
        buf.write("\7?\2\2\u0149J\3\2\2\2\u014a\u014b\7@\2\2\u014b\u014c")
        buf.write("\7?\2\2\u014cL\3\2\2\2\u014d\u014e\7>\2\2\u014e\u014f")
        buf.write("\7?\2\2\u014fN\3\2\2\2\u0150\u0151\7#\2\2\u0151\u0152")
        buf.write("\7?\2\2\u0152P\3\2\2\2\u0153\u0154\7<\2\2\u0154R\3\2\2")
        buf.write("\2\u0155\u0156\7.\2\2\u0156T\3\2\2\2\u0157\u0158\7]\2")
        buf.write("\2\u0158V\3\2\2\2\u0159\u015a\7_\2\2\u015aX\3\2\2\2\u015b")
        buf.write("\u015c\7*\2\2\u015cZ\3\2\2\2\u015d\u015e\7+\2\2\u015e")
        buf.write("\\\3\2\2\2\u015f\u0160\7>\2\2\u0160^\3\2\2\2\u0161\u0162")
        buf.write("\7@\2\2\u0162`\3\2\2\2\u0163\u0164\7,\2\2\u0164b\3\2\2")
        buf.write("\2\u0165\u0166\7\61\2\2\u0166d\3\2\2\2\u0167\u0168\7-")
        buf.write("\2\2\u0168f\3\2\2\2\u0169\u016a\7/\2\2\u016ah\3\2\2\2")
        buf.write("\u016b\u016c\5k\66\2\u016c\u0170\7\60\2\2\u016d\u016f")
        buf.write("\5q9\2\u016e\u016d\3\2\2\2\u016f\u0172\3\2\2\2\u0170\u016e")
        buf.write("\3\2\2\2\u0170\u0171\3\2\2\2\u0171j\3\2\2\2\u0172\u0170")
        buf.write("\3\2\2\2\u0173\u0177\5q9\2\u0174\u0176\5s:\2\u0175\u0174")
        buf.write("\3\2\2\2\u0176\u0179\3\2\2\2\u0177\u0175\3\2\2\2\u0177")
        buf.write("\u0178\3\2\2\2\u0178l\3\2\2\2\u0179\u0177\3\2\2\2\u017a")
        buf.write("\u017c\5u;\2\u017b\u017a\3\2\2\2\u017c\u017d\3\2\2\2\u017d")
        buf.write("\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017e\u017f\3\2\2\2")
        buf.write("\u017f\u0181\7\60\2\2\u0180\u0182\5u;\2\u0181\u0180\3")
        buf.write("\2\2\2\u0182\u0183\3\2\2\2\u0183\u0181\3\2\2\2\u0183\u0184")
        buf.write("\3\2\2\2\u0184n\3\2\2\2\u0185\u0187\5u;\2\u0186\u0185")
        buf.write("\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u0186\3\2\2\2\u0188")
        buf.write("\u0189\3\2\2\2\u0189p\3\2\2\2\u018a\u018c\t\2\2\2\u018b")
        buf.write("\u018a\3\2\2\2\u018cr\3\2\2\2\u018d\u0191\5q9\2\u018e")
        buf.write("\u0191\5u;\2\u018f\u0191\7a\2\2\u0190\u018d\3\2\2\2\u0190")
        buf.write("\u018e\3\2\2\2\u0190\u018f\3\2\2\2\u0191t\3\2\2\2\u0192")
        buf.write("\u0193\t\3\2\2\u0193v\3\2\2\2\u0194\u0196\t\4\2\2\u0195")
        buf.write("\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0195\3\2\2\2")
        buf.write("\u0197\u0198\3\2\2\2\u0198x\3\2\2\2\u0199\u019d\7%\2\2")
        buf.write("\u019a\u019c\n\5\2\2\u019b\u019a\3\2\2\2\u019c\u019f\3")
        buf.write("\2\2\2\u019d\u019b\3\2\2\2\u019d\u019e\3\2\2\2\u019ez")
        buf.write("\3\2\2\2\u019f\u019d\3\2\2\2\u01a0\u01a3\5w<\2\u01a1\u01a3")
        buf.write("\5y=\2\u01a2\u01a0\3\2\2\2\u01a2\u01a1\3\2\2\2\u01a3\u01a4")
        buf.write("\3\2\2\2\u01a4\u01a5\b>\2\2\u01a5|\3\2\2\2\u01a6\u01a7")
        buf.write("\13\2\2\2\u01a7~\3\2\2\2\22\2\u0080\u0086\u008a\u0090")
        buf.write("\u0093\u0170\u0177\u017d\u0183\u0188\u018b\u0190\u0197")
        buf.write("\u019d\u01a2\3\b\2\2")
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
    PRIME = 20
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
    ANY = 59

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Predicate'", "'Feature'", "'Factor'", "'Goal'", "'Constant'", 
            "'Action'", "'Effect'", "'Reward'", "'Policy'", "'Execute'", 
            "'Option'", "'MarkovFeature'", "'import'", "'S'", "'A'", "'''", 
            "'if'", "'else'", "'elif'", "'in'", "'init'", "'until'", "'and'", 
            "'or'", "'not'", "'True'", "'False'", "':='", "'='", "'*='", 
            "'/='", "'+='", "'-='", "'=='", "'>='", "'<='", "'!='", "':'", 
            "','", "'['", "']'", "'('", "')'", "'<'", "'>'", "'*'", "'/'", 
            "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "NL", "PREDICATE", "FEATURE", "FACTOR", 
            "GOAL", "CONSTANT", "ACTION", "EFFECT", "REWARD", "POLICY", 
            "EXECUTE", "OPTION", "MARKOVFEATURE", "IMPORT", "S_PRIME", "S", 
            "A", "PRIME", "IF", "ELSE", "ELIF", "IN", "INIT", "UNTIL", "AND", 
            "OR", "NOT", "TRUE", "FALSE", "BIND", "ASSIGN", "TIMES_EQ", 
            "DIV_EQ", "PLUS_EQ", "MINUS_EQ", "EQ_TO", "GT_EQ", "LT_EQ", 
            "NOT_EQ", "COL", "COM", "L_BRK", "R_BRK", "L_PAR", "R_PAR", 
            "LT", "GT", "TIMES", "DIVIDE", "PLUS", "MINUS", "FNAME", "IDENTIFIER", 
            "DECIMAL", "INTEGER", "SKIP_", "ANY" ]

    ruleNames = [ "NL", "PREDICATE", "FEATURE", "FACTOR", "GOAL", "CONSTANT", 
                  "ACTION", "EFFECT", "REWARD", "POLICY", "EXECUTE", "OPTION", 
                  "MARKOVFEATURE", "IMPORT", "S_PRIME", "S", "A", "PRIME", 
                  "IF", "ELSE", "ELIF", "IN", "INIT", "UNTIL", "AND", "OR", 
                  "NOT", "TRUE", "FALSE", "BIND", "ASSIGN", "TIMES_EQ", 
                  "DIV_EQ", "PLUS_EQ", "MINUS_EQ", "EQ_TO", "GT_EQ", "LT_EQ", 
                  "NOT_EQ", "COL", "COM", "L_BRK", "R_BRK", "L_PAR", "R_PAR", 
                  "LT", "GT", "TIMES", "DIVIDE", "PLUS", "MINUS", "FNAME", 
                  "IDENTIFIER", "DECIMAL", "INTEGER", "LETTER", "ANY_CHAR", 
                  "DIGIT", "SPACES", "COMMENT", "SKIP_", "ANY" ]

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



