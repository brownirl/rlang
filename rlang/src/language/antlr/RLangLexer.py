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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2>")
        buf.write("\u01ad\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\5\2\u0083\n\2")
        buf.write("\3\2\3\2\7\2\u0087\n\2\f\2\16\2\u008a\13\2\3\2\5\2\u008d")
        buf.write("\n\2\3\2\3\2\7\2\u0091\n\2\f\2\16\2\u0094\13\2\5\2\u0096")
        buf.write("\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3+\3+\3,\3,\3-\3")
        buf.write("-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63")
        buf.write("\3\64\3\64\3\65\3\65\3\66\3\66\3\66\7\66\u0174\n\66\f")
        buf.write("\66\16\66\u0177\13\66\3\67\3\67\7\67\u017b\n\67\f\67\16")
        buf.write("\67\u017e\13\67\38\68\u0181\n8\r8\168\u0182\38\38\68\u0187")
        buf.write("\n8\r8\168\u0188\39\69\u018c\n9\r9\169\u018d\3:\5:\u0191")
        buf.write("\n:\3;\3;\3;\5;\u0196\n;\3<\3<\3=\6=\u019b\n=\r=\16=\u019c")
        buf.write("\3>\3>\7>\u01a1\n>\f>\16>\u01a4\13>\3?\3?\5?\u01a8\n?")
        buf.write("\3?\3?\3@\3@\2\2A\3\5\5\6\7\7\t\b\13\t\r\n\17\13\21\f")
        buf.write("\23\r\25\16\27\17\31\20\33\21\35\22\37\23!\24#\25%\26")
        buf.write("\'\27)\30+\31-\32/\33\61\34\63\35\65\36\67\379 ;!=\"?")
        buf.write("#A$C%E&G\'I(K)M*O+Q,S-U.W/Y\60[\61]\62_\63a\64c\65e\66")
        buf.write("g\67i8k9m:o;q<s\2u\2w\2y\2{\2}=\177>\3\2\6\4\2C\\c|\3")
        buf.write("\2\62;\4\2\13\13\"\"\4\2\f\f\16\17\2\u01b6\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2}")
        buf.write("\3\2\2\2\2\177\3\2\2\2\3\u0095\3\2\2\2\5\u0097\3\2\2\2")
        buf.write("\7\u00a1\3\2\2\2\t\u00a9\3\2\2\2\13\u00b0\3\2\2\2\r\u00b5")
        buf.write("\3\2\2\2\17\u00be\3\2\2\2\21\u00c5\3\2\2\2\23\u00cc\3")
        buf.write("\2\2\2\25\u00d3\3\2\2\2\27\u00da\3\2\2\2\31\u00e2\3\2")
        buf.write("\2\2\33\u00e9\3\2\2\2\35\u00f7\3\2\2\2\37\u00fe\3\2\2")
        buf.write("\2!\u0101\3\2\2\2#\u0103\3\2\2\2%\u0105\3\2\2\2\'\u0107")
        buf.write("\3\2\2\2)\u010a\3\2\2\2+\u010f\3\2\2\2-\u0114\3\2\2\2")
        buf.write("/\u0117\3\2\2\2\61\u011c\3\2\2\2\63\u0122\3\2\2\2\65\u0126")
        buf.write("\3\2\2\2\67\u0129\3\2\2\29\u012d\3\2\2\2;\u0132\3\2\2")
        buf.write("\2=\u0138\3\2\2\2?\u013b\3\2\2\2A\u013e\3\2\2\2C\u0140")
        buf.write("\3\2\2\2E\u0143\3\2\2\2G\u0146\3\2\2\2I\u0149\3\2\2\2")
        buf.write("K\u014c\3\2\2\2M\u014f\3\2\2\2O\u0152\3\2\2\2Q\u0155\3")
        buf.write("\2\2\2S\u0158\3\2\2\2U\u015a\3\2\2\2W\u015c\3\2\2\2Y\u015e")
        buf.write("\3\2\2\2[\u0160\3\2\2\2]\u0162\3\2\2\2_\u0164\3\2\2\2")
        buf.write("a\u0166\3\2\2\2c\u0168\3\2\2\2e\u016a\3\2\2\2g\u016c\3")
        buf.write("\2\2\2i\u016e\3\2\2\2k\u0170\3\2\2\2m\u0178\3\2\2\2o\u0180")
        buf.write("\3\2\2\2q\u018b\3\2\2\2s\u0190\3\2\2\2u\u0195\3\2\2\2")
        buf.write("w\u0197\3\2\2\2y\u019a\3\2\2\2{\u019e\3\2\2\2}\u01a7\3")
        buf.write("\2\2\2\177\u01ab\3\2\2\2\u0081\u0083\7\17\2\2\u0082\u0081")
        buf.write("\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0084\3\2\2\2\u0084")
        buf.write("\u0088\7\f\2\2\u0085\u0087\7\"\2\2\u0086\u0085\3\2\2\2")
        buf.write("\u0087\u008a\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089\3")
        buf.write("\2\2\2\u0089\u0096\3\2\2\2\u008a\u0088\3\2\2\2\u008b\u008d")
        buf.write("\7\17\2\2\u008c\u008b\3\2\2\2\u008c\u008d\3\2\2\2\u008d")
        buf.write("\u008e\3\2\2\2\u008e\u0092\7\f\2\2\u008f\u0091\7\13\2")
        buf.write("\2\u0090\u008f\3\2\2\2\u0091\u0094\3\2\2\2\u0092\u0090")
        buf.write("\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0096\3\2\2\2\u0094")
        buf.write("\u0092\3\2\2\2\u0095\u0082\3\2\2\2\u0095\u008c\3\2\2\2")
        buf.write("\u0096\4\3\2\2\2\u0097\u0098\7R\2\2\u0098\u0099\7t\2\2")
        buf.write("\u0099\u009a\7g\2\2\u009a\u009b\7f\2\2\u009b\u009c\7k")
        buf.write("\2\2\u009c\u009d\7e\2\2\u009d\u009e\7c\2\2\u009e\u009f")
        buf.write("\7v\2\2\u009f\u00a0\7g\2\2\u00a0\6\3\2\2\2\u00a1\u00a2")
        buf.write("\7H\2\2\u00a2\u00a3\7g\2\2\u00a3\u00a4\7c\2\2\u00a4\u00a5")
        buf.write("\7v\2\2\u00a5\u00a6\7w\2\2\u00a6\u00a7\7t\2\2\u00a7\u00a8")
        buf.write("\7g\2\2\u00a8\b\3\2\2\2\u00a9\u00aa\7H\2\2\u00aa\u00ab")
        buf.write("\7c\2\2\u00ab\u00ac\7e\2\2\u00ac\u00ad\7v\2\2\u00ad\u00ae")
        buf.write("\7q\2\2\u00ae\u00af\7t\2\2\u00af\n\3\2\2\2\u00b0\u00b1")
        buf.write("\7I\2\2\u00b1\u00b2\7q\2\2\u00b2\u00b3\7c\2\2\u00b3\u00b4")
        buf.write("\7n\2\2\u00b4\f\3\2\2\2\u00b5\u00b6\7E\2\2\u00b6\u00b7")
        buf.write("\7q\2\2\u00b7\u00b8\7p\2\2\u00b8\u00b9\7u\2\2\u00b9\u00ba")
        buf.write("\7v\2\2\u00ba\u00bb\7c\2\2\u00bb\u00bc\7p\2\2\u00bc\u00bd")
        buf.write("\7v\2\2\u00bd\16\3\2\2\2\u00be\u00bf\7C\2\2\u00bf\u00c0")
        buf.write("\7e\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2\7k\2\2\u00c2\u00c3")
        buf.write("\7q\2\2\u00c3\u00c4\7p\2\2\u00c4\20\3\2\2\2\u00c5\u00c6")
        buf.write("\7G\2\2\u00c6\u00c7\7h\2\2\u00c7\u00c8\7h\2\2\u00c8\u00c9")
        buf.write("\7g\2\2\u00c9\u00ca\7e\2\2\u00ca\u00cb\7v\2\2\u00cb\22")
        buf.write("\3\2\2\2\u00cc\u00cd\7T\2\2\u00cd\u00ce\7g\2\2\u00ce\u00cf")
        buf.write("\7y\2\2\u00cf\u00d0\7c\2\2\u00d0\u00d1\7t\2\2\u00d1\u00d2")
        buf.write("\7f\2\2\u00d2\24\3\2\2\2\u00d3\u00d4\7R\2\2\u00d4\u00d5")
        buf.write("\7q\2\2\u00d5\u00d6\7n\2\2\u00d6\u00d7\7k\2\2\u00d7\u00d8")
        buf.write("\7e\2\2\u00d8\u00d9\7{\2\2\u00d9\26\3\2\2\2\u00da\u00db")
        buf.write("\7G\2\2\u00db\u00dc\7z\2\2\u00dc\u00dd\7g\2\2\u00dd\u00de")
        buf.write("\7e\2\2\u00de\u00df\7w\2\2\u00df\u00e0\7v\2\2\u00e0\u00e1")
        buf.write("\7g\2\2\u00e1\30\3\2\2\2\u00e2\u00e3\7Q\2\2\u00e3\u00e4")
        buf.write("\7r\2\2\u00e4\u00e5\7v\2\2\u00e5\u00e6\7k\2\2\u00e6\u00e7")
        buf.write("\7q\2\2\u00e7\u00e8\7p\2\2\u00e8\32\3\2\2\2\u00e9\u00ea")
        buf.write("\7O\2\2\u00ea\u00eb\7c\2\2\u00eb\u00ec\7t\2\2\u00ec\u00ed")
        buf.write("\7m\2\2\u00ed\u00ee\7q\2\2\u00ee\u00ef\7x\2\2\u00ef\u00f0")
        buf.write("\7H\2\2\u00f0\u00f1\7g\2\2\u00f1\u00f2\7c\2\2\u00f2\u00f3")
        buf.write("\7v\2\2\u00f3\u00f4\7w\2\2\u00f4\u00f5\7t\2\2\u00f5\u00f6")
        buf.write("\7g\2\2\u00f6\34\3\2\2\2\u00f7\u00f8\7k\2\2\u00f8\u00f9")
        buf.write("\7o\2\2\u00f9\u00fa\7r\2\2\u00fa\u00fb\7q\2\2\u00fb\u00fc")
        buf.write("\7t\2\2\u00fc\u00fd\7v\2\2\u00fd\36\3\2\2\2\u00fe\u00ff")
        buf.write("\5!\21\2\u00ff\u0100\5%\23\2\u0100 \3\2\2\2\u0101\u0102")
        buf.write("\7U\2\2\u0102\"\3\2\2\2\u0103\u0104\7C\2\2\u0104$\3\2")
        buf.write("\2\2\u0105\u0106\7)\2\2\u0106&\3\2\2\2\u0107\u0108\7k")
        buf.write("\2\2\u0108\u0109\7h\2\2\u0109(\3\2\2\2\u010a\u010b\7g")
        buf.write("\2\2\u010b\u010c\7n\2\2\u010c\u010d\7u\2\2\u010d\u010e")
        buf.write("\7g\2\2\u010e*\3\2\2\2\u010f\u0110\7g\2\2\u0110\u0111")
        buf.write("\7n\2\2\u0111\u0112\7k\2\2\u0112\u0113\7h\2\2\u0113,\3")
        buf.write("\2\2\2\u0114\u0115\7k\2\2\u0115\u0116\7p\2\2\u0116.\3")
        buf.write("\2\2\2\u0117\u0118\7k\2\2\u0118\u0119\7p\2\2\u0119\u011a")
        buf.write("\7k\2\2\u011a\u011b\7v\2\2\u011b\60\3\2\2\2\u011c\u011d")
        buf.write("\7w\2\2\u011d\u011e\7p\2\2\u011e\u011f\7v\2\2\u011f\u0120")
        buf.write("\7k\2\2\u0120\u0121\7n\2\2\u0121\62\3\2\2\2\u0122\u0123")
        buf.write("\7c\2\2\u0123\u0124\7p\2\2\u0124\u0125\7f\2\2\u0125\64")
        buf.write("\3\2\2\2\u0126\u0127\7q\2\2\u0127\u0128\7t\2\2\u0128\66")
        buf.write("\3\2\2\2\u0129\u012a\7p\2\2\u012a\u012b\7q\2\2\u012b\u012c")
        buf.write("\7v\2\2\u012c8\3\2\2\2\u012d\u012e\7V\2\2\u012e\u012f")
        buf.write("\7t\2\2\u012f\u0130\7w\2\2\u0130\u0131\7g\2\2\u0131:\3")
        buf.write("\2\2\2\u0132\u0133\7H\2\2\u0133\u0134\7c\2\2\u0134\u0135")
        buf.write("\7n\2\2\u0135\u0136\7u\2\2\u0136\u0137\7g\2\2\u0137<\3")
        buf.write("\2\2\2\u0138\u0139\7<\2\2\u0139\u013a\7?\2\2\u013a>\3")
        buf.write("\2\2\2\u013b\u013c\7/\2\2\u013c\u013d\7@\2\2\u013d@\3")
        buf.write("\2\2\2\u013e\u013f\7?\2\2\u013fB\3\2\2\2\u0140\u0141\7")
        buf.write(",\2\2\u0141\u0142\7?\2\2\u0142D\3\2\2\2\u0143\u0144\7")
        buf.write("\61\2\2\u0144\u0145\7?\2\2\u0145F\3\2\2\2\u0146\u0147")
        buf.write("\7-\2\2\u0147\u0148\7?\2\2\u0148H\3\2\2\2\u0149\u014a")
        buf.write("\7/\2\2\u014a\u014b\7?\2\2\u014bJ\3\2\2\2\u014c\u014d")
        buf.write("\7?\2\2\u014d\u014e\7?\2\2\u014eL\3\2\2\2\u014f\u0150")
        buf.write("\7@\2\2\u0150\u0151\7?\2\2\u0151N\3\2\2\2\u0152\u0153")
        buf.write("\7>\2\2\u0153\u0154\7?\2\2\u0154P\3\2\2\2\u0155\u0156")
        buf.write("\7#\2\2\u0156\u0157\7?\2\2\u0157R\3\2\2\2\u0158\u0159")
        buf.write("\7<\2\2\u0159T\3\2\2\2\u015a\u015b\7.\2\2\u015bV\3\2\2")
        buf.write("\2\u015c\u015d\7]\2\2\u015dX\3\2\2\2\u015e\u015f\7_\2")
        buf.write("\2\u015fZ\3\2\2\2\u0160\u0161\7*\2\2\u0161\\\3\2\2\2\u0162")
        buf.write("\u0163\7+\2\2\u0163^\3\2\2\2\u0164\u0165\7>\2\2\u0165")
        buf.write("`\3\2\2\2\u0166\u0167\7@\2\2\u0167b\3\2\2\2\u0168\u0169")
        buf.write("\7,\2\2\u0169d\3\2\2\2\u016a\u016b\7\61\2\2\u016bf\3\2")
        buf.write("\2\2\u016c\u016d\7-\2\2\u016dh\3\2\2\2\u016e\u016f\7/")
        buf.write("\2\2\u016fj\3\2\2\2\u0170\u0171\5m\67\2\u0171\u0175\7")
        buf.write("\60\2\2\u0172\u0174\5s:\2\u0173\u0172\3\2\2\2\u0174\u0177")
        buf.write("\3\2\2\2\u0175\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176")
        buf.write("l\3\2\2\2\u0177\u0175\3\2\2\2\u0178\u017c\5s:\2\u0179")
        buf.write("\u017b\5u;\2\u017a\u0179\3\2\2\2\u017b\u017e\3\2\2\2\u017c")
        buf.write("\u017a\3\2\2\2\u017c\u017d\3\2\2\2\u017dn\3\2\2\2\u017e")
        buf.write("\u017c\3\2\2\2\u017f\u0181\5w<\2\u0180\u017f\3\2\2\2\u0181")
        buf.write("\u0182\3\2\2\2\u0182\u0180\3\2\2\2\u0182\u0183\3\2\2\2")
        buf.write("\u0183\u0184\3\2\2\2\u0184\u0186\7\60\2\2\u0185\u0187")
        buf.write("\5w<\2\u0186\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u0186")
        buf.write("\3\2\2\2\u0188\u0189\3\2\2\2\u0189p\3\2\2\2\u018a\u018c")
        buf.write("\5w<\2\u018b\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018b")
        buf.write("\3\2\2\2\u018d\u018e\3\2\2\2\u018er\3\2\2\2\u018f\u0191")
        buf.write("\t\2\2\2\u0190\u018f\3\2\2\2\u0191t\3\2\2\2\u0192\u0196")
        buf.write("\5s:\2\u0193\u0196\5w<\2\u0194\u0196\7a\2\2\u0195\u0192")
        buf.write("\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0194\3\2\2\2\u0196")
        buf.write("v\3\2\2\2\u0197\u0198\t\3\2\2\u0198x\3\2\2\2\u0199\u019b")
        buf.write("\t\4\2\2\u019a\u0199\3\2\2\2\u019b\u019c\3\2\2\2\u019c")
        buf.write("\u019a\3\2\2\2\u019c\u019d\3\2\2\2\u019dz\3\2\2\2\u019e")
        buf.write("\u01a2\7%\2\2\u019f\u01a1\n\5\2\2\u01a0\u019f\3\2\2\2")
        buf.write("\u01a1\u01a4\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3")
        buf.write("\2\2\2\u01a3|\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a5\u01a8")
        buf.write("\5y=\2\u01a6\u01a8\5{>\2\u01a7\u01a5\3\2\2\2\u01a7\u01a6")
        buf.write("\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01aa\b?\2\2\u01aa")
        buf.write("~\3\2\2\2\u01ab\u01ac\13\2\2\2\u01ac\u0080\3\2\2\2\22")
        buf.write("\2\u0082\u0088\u008c\u0092\u0095\u0175\u017c\u0182\u0188")
        buf.write("\u018d\u0190\u0195\u019c\u01a2\u01a7\3\b\2\2")
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
    PREDICT = 33
    ASSIGN = 34
    TIMES_EQ = 35
    DIV_EQ = 36
    PLUS_EQ = 37
    MINUS_EQ = 38
    EQ_TO = 39
    GT_EQ = 40
    LT_EQ = 41
    NOT_EQ = 42
    COL = 43
    COM = 44
    L_BRK = 45
    R_BRK = 46
    L_PAR = 47
    R_PAR = 48
    LT = 49
    GT = 50
    TIMES = 51
    DIVIDE = 52
    PLUS = 53
    MINUS = 54
    FNAME = 55
    IDENTIFIER = 56
    DECIMAL = 57
    INTEGER = 58
    SKIP_ = 59
    ANY = 60

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Predicate'", "'Feature'", "'Factor'", "'Goal'", "'Constant'", 
            "'Action'", "'Effect'", "'Reward'", "'Policy'", "'Execute'", 
            "'Option'", "'MarkovFeature'", "'import'", "'S'", "'A'", "'''", 
            "'if'", "'else'", "'elif'", "'in'", "'init'", "'until'", "'and'", 
            "'or'", "'not'", "'True'", "'False'", "':='", "'->'", "'='", 
            "'*='", "'/='", "'+='", "'-='", "'=='", "'>='", "'<='", "'!='", 
            "':'", "','", "'['", "']'", "'('", "')'", "'<'", "'>'", "'*'", 
            "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "NL", "PREDICATE", "FEATURE", "FACTOR", 
            "GOAL", "CONSTANT", "ACTION", "EFFECT", "REWARD", "POLICY", 
            "EXECUTE", "OPTION", "MARKOVFEATURE", "IMPORT", "S_PRIME", "S", 
            "A", "PRIME", "IF", "ELSE", "ELIF", "IN", "INIT", "UNTIL", "AND", 
            "OR", "NOT", "TRUE", "FALSE", "BIND", "PREDICT", "ASSIGN", "TIMES_EQ", 
            "DIV_EQ", "PLUS_EQ", "MINUS_EQ", "EQ_TO", "GT_EQ", "LT_EQ", 
            "NOT_EQ", "COL", "COM", "L_BRK", "R_BRK", "L_PAR", "R_PAR", 
            "LT", "GT", "TIMES", "DIVIDE", "PLUS", "MINUS", "FNAME", "IDENTIFIER", 
            "DECIMAL", "INTEGER", "SKIP_", "ANY" ]

    ruleNames = [ "NL", "PREDICATE", "FEATURE", "FACTOR", "GOAL", "CONSTANT", 
                  "ACTION", "EFFECT", "REWARD", "POLICY", "EXECUTE", "OPTION", 
                  "MARKOVFEATURE", "IMPORT", "S_PRIME", "S", "A", "PRIME", 
                  "IF", "ELSE", "ELIF", "IN", "INIT", "UNTIL", "AND", "OR", 
                  "NOT", "TRUE", "FALSE", "BIND", "PREDICT", "ASSIGN", "TIMES_EQ", 
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



