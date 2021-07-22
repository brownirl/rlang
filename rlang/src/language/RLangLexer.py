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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<")
        buf.write("\u01aa\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\3\2\5\2\177\n\2\3\2\3\2\7\2\u0083")
        buf.write("\n\2\f\2\16\2\u0086\13\2\3\2\5\2\u0089\n\2\3\2\3\2\7\2")
        buf.write("\u008d\n\2\f\2\16\2\u0090\13\2\5\2\u0092\n\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$")
        buf.write("\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3")
        buf.write("+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\63\3\63\3\64\3\64\3\65\3\65\3\65\7\65\u0173\n\65\f")
        buf.write("\65\16\65\u0176\13\65\3\66\3\66\7\66\u017a\n\66\f\66\16")
        buf.write("\66\u017d\13\66\3\67\6\67\u0180\n\67\r\67\16\67\u0181")
        buf.write("\3\67\3\67\6\67\u0186\n\67\r\67\16\67\u0187\38\68\u018b")
        buf.write("\n8\r8\168\u018c\39\59\u0190\n9\3:\3:\3:\5:\u0195\n:\3")
        buf.write(";\3;\3<\6<\u019a\n<\r<\16<\u019b\3=\3=\7=\u01a0\n=\f=")
        buf.write("\16=\u01a3\13=\3>\3>\5>\u01a7\n>\3>\3>\2\2?\3\5\5\6\7")
        buf.write("\7\t\b\13\t\r\n\17\13\21\f\23\r\25\16\27\17\31\20\33\21")
        buf.write("\35\22\37\23!\24#\25%\26\'\27)\30+\31-\32/\33\61\34\63")
        buf.write("\35\65\36\67\379 ;!=\"?#A$C%E&G\'I(K)M*O+Q,S-U.W/Y\60")
        buf.write("[\61]\62_\63a\64c\65e\66g\67i8k9m:o;q\2s\2u\2w\2y\2{<")
        buf.write("\3\2\6\4\2C\\c|\3\2\62;\4\2\13\13\"\"\4\2\f\f\16\17\2")
        buf.write("\u01b3\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
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
        buf.write("\2\2{\3\2\2\2\3\u0091\3\2\2\2\5\u0093\3\2\2\2\7\u009d")
        buf.write("\3\2\2\2\t\u00a5\3\2\2\2\13\u00ac\3\2\2\2\r\u00b1\3\2")
        buf.write("\2\2\17\u00ba\3\2\2\2\21\u00c1\3\2\2\2\23\u00c8\3\2\2")
        buf.write("\2\25\u00cf\3\2\2\2\27\u00d6\3\2\2\2\31\u00de\3\2\2\2")
        buf.write("\33\u00e5\3\2\2\2\35\u00f3\3\2\2\2\37\u00f9\3\2\2\2!\u0103")
        buf.write("\3\2\2\2#\u0105\3\2\2\2%\u0107\3\2\2\2\'\u010a\3\2\2\2")
        buf.write(")\u010f\3\2\2\2+\u0114\3\2\2\2-\u0117\3\2\2\2/\u011c\3")
        buf.write("\2\2\2\61\u0122\3\2\2\2\63\u0126\3\2\2\2\65\u0129\3\2")
        buf.write("\2\2\67\u012d\3\2\2\29\u0132\3\2\2\2;\u0138\3\2\2\2=\u013b")
        buf.write("\3\2\2\2?\u013d\3\2\2\2A\u0140\3\2\2\2C\u0143\3\2\2\2")
        buf.write("E\u0146\3\2\2\2G\u0149\3\2\2\2I\u014c\3\2\2\2K\u014f\3")
        buf.write("\2\2\2M\u0152\3\2\2\2O\u0155\3\2\2\2Q\u0157\3\2\2\2S\u0159")
        buf.write("\3\2\2\2U\u015b\3\2\2\2W\u015d\3\2\2\2Y\u015f\3\2\2\2")
        buf.write("[\u0161\3\2\2\2]\u0163\3\2\2\2_\u0165\3\2\2\2a\u0167\3")
        buf.write("\2\2\2c\u0169\3\2\2\2e\u016b\3\2\2\2g\u016d\3\2\2\2i\u016f")
        buf.write("\3\2\2\2k\u0177\3\2\2\2m\u017f\3\2\2\2o\u018a\3\2\2\2")
        buf.write("q\u018f\3\2\2\2s\u0194\3\2\2\2u\u0196\3\2\2\2w\u0199\3")
        buf.write("\2\2\2y\u019d\3\2\2\2{\u01a6\3\2\2\2}\177\7\17\2\2~}\3")
        buf.write("\2\2\2~\177\3\2\2\2\177\u0080\3\2\2\2\u0080\u0084\7\f")
        buf.write("\2\2\u0081\u0083\7\"\2\2\u0082\u0081\3\2\2\2\u0083\u0086")
        buf.write("\3\2\2\2\u0084\u0082\3\2\2\2\u0084\u0085\3\2\2\2\u0085")
        buf.write("\u0092\3\2\2\2\u0086\u0084\3\2\2\2\u0087\u0089\7\17\2")
        buf.write("\2\u0088\u0087\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008a")
        buf.write("\3\2\2\2\u008a\u008e\7\f\2\2\u008b\u008d\7\13\2\2\u008c")
        buf.write("\u008b\3\2\2\2\u008d\u0090\3\2\2\2\u008e\u008c\3\2\2\2")
        buf.write("\u008e\u008f\3\2\2\2\u008f\u0092\3\2\2\2\u0090\u008e\3")
        buf.write("\2\2\2\u0091~\3\2\2\2\u0091\u0088\3\2\2\2\u0092\4\3\2")
        buf.write("\2\2\u0093\u0094\7R\2\2\u0094\u0095\7t\2\2\u0095\u0096")
        buf.write("\7g\2\2\u0096\u0097\7f\2\2\u0097\u0098\7k\2\2\u0098\u0099")
        buf.write("\7e\2\2\u0099\u009a\7c\2\2\u009a\u009b\7v\2\2\u009b\u009c")
        buf.write("\7g\2\2\u009c\6\3\2\2\2\u009d\u009e\7H\2\2\u009e\u009f")
        buf.write("\7g\2\2\u009f\u00a0\7c\2\2\u00a0\u00a1\7v\2\2\u00a1\u00a2")
        buf.write("\7w\2\2\u00a2\u00a3\7t\2\2\u00a3\u00a4\7g\2\2\u00a4\b")
        buf.write("\3\2\2\2\u00a5\u00a6\7H\2\2\u00a6\u00a7\7c\2\2\u00a7\u00a8")
        buf.write("\7e\2\2\u00a8\u00a9\7v\2\2\u00a9\u00aa\7q\2\2\u00aa\u00ab")
        buf.write("\7t\2\2\u00ab\n\3\2\2\2\u00ac\u00ad\7I\2\2\u00ad\u00ae")
        buf.write("\7q\2\2\u00ae\u00af\7c\2\2\u00af\u00b0\7n\2\2\u00b0\f")
        buf.write("\3\2\2\2\u00b1\u00b2\7E\2\2\u00b2\u00b3\7q\2\2\u00b3\u00b4")
        buf.write("\7p\2\2\u00b4\u00b5\7u\2\2\u00b5\u00b6\7v\2\2\u00b6\u00b7")
        buf.write("\7c\2\2\u00b7\u00b8\7p\2\2\u00b8\u00b9\7v\2\2\u00b9\16")
        buf.write("\3\2\2\2\u00ba\u00bb\7C\2\2\u00bb\u00bc\7e\2\2\u00bc\u00bd")
        buf.write("\7v\2\2\u00bd\u00be\7k\2\2\u00be\u00bf\7q\2\2\u00bf\u00c0")
        buf.write("\7p\2\2\u00c0\20\3\2\2\2\u00c1\u00c2\7G\2\2\u00c2\u00c3")
        buf.write("\7h\2\2\u00c3\u00c4\7h\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6")
        buf.write("\7e\2\2\u00c6\u00c7\7v\2\2\u00c7\22\3\2\2\2\u00c8\u00c9")
        buf.write("\7T\2\2\u00c9\u00ca\7g\2\2\u00ca\u00cb\7y\2\2\u00cb\u00cc")
        buf.write("\7c\2\2\u00cc\u00cd\7t\2\2\u00cd\u00ce\7f\2\2\u00ce\24")
        buf.write("\3\2\2\2\u00cf\u00d0\7R\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2")
        buf.write("\7n\2\2\u00d2\u00d3\7k\2\2\u00d3\u00d4\7e\2\2\u00d4\u00d5")
        buf.write("\7{\2\2\u00d5\26\3\2\2\2\u00d6\u00d7\7G\2\2\u00d7\u00d8")
        buf.write("\7z\2\2\u00d8\u00d9\7g\2\2\u00d9\u00da\7e\2\2\u00da\u00db")
        buf.write("\7w\2\2\u00db\u00dc\7v\2\2\u00dc\u00dd\7g\2\2\u00dd\30")
        buf.write("\3\2\2\2\u00de\u00df\7Q\2\2\u00df\u00e0\7r\2\2\u00e0\u00e1")
        buf.write("\7v\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4")
        buf.write("\7p\2\2\u00e4\32\3\2\2\2\u00e5\u00e6\7O\2\2\u00e6\u00e7")
        buf.write("\7c\2\2\u00e7\u00e8\7t\2\2\u00e8\u00e9\7m\2\2\u00e9\u00ea")
        buf.write("\7q\2\2\u00ea\u00eb\7x\2\2\u00eb\u00ec\7H\2\2\u00ec\u00ed")
        buf.write("\7g\2\2\u00ed\u00ee\7c\2\2\u00ee\u00ef\7v\2\2\u00ef\u00f0")
        buf.write("\7w\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2\7g\2\2\u00f2\34")
        buf.write("\3\2\2\2\u00f3\u00f4\7x\2\2\u00f4\u00f5\7q\2\2\u00f5\u00f6")
        buf.write("\7e\2\2\u00f6\u00f7\7c\2\2\u00f7\u00f8\7d\2\2\u00f8\36")
        buf.write("\3\2\2\2\u00f9\u00fa\7i\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc")
        buf.write("\7q\2\2\u00fc\u00fd\7w\2\2\u00fd\u00fe\7p\2\2\u00fe\u00ff")
        buf.write("\7f\2\2\u00ff\u0100\7k\2\2\u0100\u0101\7p\2\2\u0101\u0102")
        buf.write("\7i\2\2\u0102 \3\2\2\2\u0103\u0104\7U\2\2\u0104\"\3\2")
        buf.write("\2\2\u0105\u0106\7C\2\2\u0106$\3\2\2\2\u0107\u0108\7k")
        buf.write("\2\2\u0108\u0109\7h\2\2\u0109&\3\2\2\2\u010a\u010b\7g")
        buf.write("\2\2\u010b\u010c\7n\2\2\u010c\u010d\7u\2\2\u010d\u010e")
        buf.write("\7g\2\2\u010e(\3\2\2\2\u010f\u0110\7g\2\2\u0110\u0111")
        buf.write("\7n\2\2\u0111\u0112\7k\2\2\u0112\u0113\7h\2\2\u0113*\3")
        buf.write("\2\2\2\u0114\u0115\7k\2\2\u0115\u0116\7p\2\2\u0116,\3")
        buf.write("\2\2\2\u0117\u0118\7k\2\2\u0118\u0119\7p\2\2\u0119\u011a")
        buf.write("\7k\2\2\u011a\u011b\7v\2\2\u011b.\3\2\2\2\u011c\u011d")
        buf.write("\7w\2\2\u011d\u011e\7p\2\2\u011e\u011f\7v\2\2\u011f\u0120")
        buf.write("\7k\2\2\u0120\u0121\7n\2\2\u0121\60\3\2\2\2\u0122\u0123")
        buf.write("\7c\2\2\u0123\u0124\7p\2\2\u0124\u0125\7f\2\2\u0125\62")
        buf.write("\3\2\2\2\u0126\u0127\7q\2\2\u0127\u0128\7t\2\2\u0128\64")
        buf.write("\3\2\2\2\u0129\u012a\7p\2\2\u012a\u012b\7q\2\2\u012b\u012c")
        buf.write("\7v\2\2\u012c\66\3\2\2\2\u012d\u012e\7V\2\2\u012e\u012f")
        buf.write("\7t\2\2\u012f\u0130\7w\2\2\u0130\u0131\7g\2\2\u01318\3")
        buf.write("\2\2\2\u0132\u0133\7H\2\2\u0133\u0134\7c\2\2\u0134\u0135")
        buf.write("\7n\2\2\u0135\u0136\7u\2\2\u0136\u0137\7g\2\2\u0137:\3")
        buf.write("\2\2\2\u0138\u0139\7<\2\2\u0139\u013a\7?\2\2\u013a<\3")
        buf.write("\2\2\2\u013b\u013c\7?\2\2\u013c>\3\2\2\2\u013d\u013e\7")
        buf.write(",\2\2\u013e\u013f\7?\2\2\u013f@\3\2\2\2\u0140\u0141\7")
        buf.write("\61\2\2\u0141\u0142\7?\2\2\u0142B\3\2\2\2\u0143\u0144")
        buf.write("\7-\2\2\u0144\u0145\7?\2\2\u0145D\3\2\2\2\u0146\u0147")
        buf.write("\7/\2\2\u0147\u0148\7?\2\2\u0148F\3\2\2\2\u0149\u014a")
        buf.write("\7?\2\2\u014a\u014b\7?\2\2\u014bH\3\2\2\2\u014c\u014d")
        buf.write("\7@\2\2\u014d\u014e\7?\2\2\u014eJ\3\2\2\2\u014f\u0150")
        buf.write("\7>\2\2\u0150\u0151\7?\2\2\u0151L\3\2\2\2\u0152\u0153")
        buf.write("\7#\2\2\u0153\u0154\7?\2\2\u0154N\3\2\2\2\u0155\u0156")
        buf.write("\7<\2\2\u0156P\3\2\2\2\u0157\u0158\7.\2\2\u0158R\3\2\2")
        buf.write("\2\u0159\u015a\7]\2\2\u015aT\3\2\2\2\u015b\u015c\7_\2")
        buf.write("\2\u015cV\3\2\2\2\u015d\u015e\7*\2\2\u015eX\3\2\2\2\u015f")
        buf.write("\u0160\7+\2\2\u0160Z\3\2\2\2\u0161\u0162\7>\2\2\u0162")
        buf.write("\\\3\2\2\2\u0163\u0164\7@\2\2\u0164^\3\2\2\2\u0165\u0166")
        buf.write("\7,\2\2\u0166`\3\2\2\2\u0167\u0168\7\61\2\2\u0168b\3\2")
        buf.write("\2\2\u0169\u016a\7-\2\2\u016ad\3\2\2\2\u016b\u016c\7/")
        buf.write("\2\2\u016cf\3\2\2\2\u016d\u016e\7)\2\2\u016eh\3\2\2\2")
        buf.write("\u016f\u0170\5k\66\2\u0170\u0174\7\60\2\2\u0171\u0173")
        buf.write("\5q9\2\u0172\u0171\3\2\2\2\u0173\u0176\3\2\2\2\u0174\u0172")
        buf.write("\3\2\2\2\u0174\u0175\3\2\2\2\u0175j\3\2\2\2\u0176\u0174")
        buf.write("\3\2\2\2\u0177\u017b\5q9\2\u0178\u017a\5s:\2\u0179\u0178")
        buf.write("\3\2\2\2\u017a\u017d\3\2\2\2\u017b\u0179\3\2\2\2\u017b")
        buf.write("\u017c\3\2\2\2\u017cl\3\2\2\2\u017d\u017b\3\2\2\2\u017e")
        buf.write("\u0180\5u;\2\u017f\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181")
        buf.write("\u017f\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0183\3\2\2\2")
        buf.write("\u0183\u0185\7\60\2\2\u0184\u0186\5u;\2\u0185\u0184\3")
        buf.write("\2\2\2\u0186\u0187\3\2\2\2\u0187\u0185\3\2\2\2\u0187\u0188")
        buf.write("\3\2\2\2\u0188n\3\2\2\2\u0189\u018b\5u;\2\u018a\u0189")
        buf.write("\3\2\2\2\u018b\u018c\3\2\2\2\u018c\u018a\3\2\2\2\u018c")
        buf.write("\u018d\3\2\2\2\u018dp\3\2\2\2\u018e\u0190\t\2\2\2\u018f")
        buf.write("\u018e\3\2\2\2\u0190r\3\2\2\2\u0191\u0195\5q9\2\u0192")
        buf.write("\u0195\5u;\2\u0193\u0195\7a\2\2\u0194\u0191\3\2\2\2\u0194")
        buf.write("\u0192\3\2\2\2\u0194\u0193\3\2\2\2\u0195t\3\2\2\2\u0196")
        buf.write("\u0197\t\3\2\2\u0197v\3\2\2\2\u0198\u019a\t\4\2\2\u0199")
        buf.write("\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u0199\3\2\2\2")
        buf.write("\u019b\u019c\3\2\2\2\u019cx\3\2\2\2\u019d\u01a1\7%\2\2")
        buf.write("\u019e\u01a0\n\5\2\2\u019f\u019e\3\2\2\2\u01a0\u01a3\3")
        buf.write("\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2z")
        buf.write("\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4\u01a7\5w<\2\u01a5\u01a7")
        buf.write("\5y=\2\u01a6\u01a4\3\2\2\2\u01a6\u01a5\3\2\2\2\u01a7\u01a8")
        buf.write("\3\2\2\2\u01a8\u01a9\b>\2\2\u01a9|\3\2\2\2\22\2~\u0084")
        buf.write("\u0088\u008e\u0091\u0174\u017b\u0181\u0187\u018c\u018f")
        buf.write("\u0194\u019b\u01a1\u01a6\3\b\2\2")
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
    GROUNDING = 17
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
    ASIGN = 32
    TIMES_EQ = 33
    DIV_EQ = 34
    PLUS_EQ = 35
    MINUS_EQ = 36
    EQUALS = 37
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
    PRIME = 53
    FNAME = 54
    IDENTIFIER = 55
    DECIMAL = 56
    INTEGER = 57
    SKIP_ = 58

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Predicate'", "'Feature'", "'Factor'", "'Goal'", "'Constant'", 
            "'Action'", "'Effect'", "'Reward'", "'Policy'", "'Execute'", 
            "'Option'", "'MarkovFeature'", "'vocab'", "'grounding'", "'S'", 
            "'A'", "'if'", "'else'", "'elif'", "'in'", "'init'", "'until'", 
            "'and'", "'or'", "'not'", "'True'", "'False'", "':='", "'='", 
            "'*='", "'/='", "'+='", "'-='", "'=='", "'>='", "'<='", "'!='", 
            "':'", "','", "'['", "']'", "'('", "')'", "'<'", "'>'", "'*'", 
            "'/'", "'+'", "'-'", "'''" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "NL", "PREDICATE", "FEATURE", "FACTOR", 
            "GOAL", "CONSTANT", "ACTION", "EFFECT", "REWARD", "POLICY", 
            "EXECUTE", "OPTION", "MARKOVFEATURE", "VOCAB", "GROUNDING", 
            "S", "A", "IF", "ELSE", "ELIF", "IN", "INIT", "UNTIL", "AND", 
            "OR", "NOT", "TRUE", "FALSE", "BIND", "ASIGN", "TIMES_EQ", "DIV_EQ", 
            "PLUS_EQ", "MINUS_EQ", "EQUALS", "GT_EQ", "LT_EQ", "NOT_EQ", 
            "COL", "COM", "L_BRK", "R_BRK", "L_PAR", "R_PAR", "LT", "GT", 
            "TIMES", "DIVIDE", "PLUS", "MINUS", "PRIME", "FNAME", "IDENTIFIER", 
            "DECIMAL", "INTEGER", "SKIP_" ]

    ruleNames = [ "NL", "PREDICATE", "FEATURE", "FACTOR", "GOAL", "CONSTANT", 
                  "ACTION", "EFFECT", "REWARD", "POLICY", "EXECUTE", "OPTION", 
                  "MARKOVFEATURE", "VOCAB", "GROUNDING", "S", "A", "IF", 
                  "ELSE", "ELIF", "IN", "INIT", "UNTIL", "AND", "OR", "NOT", 
                  "TRUE", "FALSE", "BIND", "ASIGN", "TIMES_EQ", "DIV_EQ", 
                  "PLUS_EQ", "MINUS_EQ", "EQUALS", "GT_EQ", "LT_EQ", "NOT_EQ", 
                  "COL", "COM", "L_BRK", "R_BRK", "L_PAR", "R_PAR", "LT", 
                  "GT", "TIMES", "DIVIDE", "PLUS", "MINUS", "PRIME", "FNAME", 
                  "IDENTIFIER", "DECIMAL", "INTEGER", "LETTER", "ANY_CHAR", 
                  "DIGIT", "SPACES", "COMMENT", "SKIP_" ]

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



