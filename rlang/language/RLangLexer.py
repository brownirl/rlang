# Generated from RLangLexer.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from antlr_denter.DenterHelper import DenterHelper
from RLangParser import RLangParser



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\67")
        buf.write("\u0178\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\5")
        buf.write("\2u\n\2\3\2\3\2\7\2y\n\2\f\2\16\2|\13\2\3\2\5\2\177\n")
        buf.write("\2\3\2\3\2\7\2\u0083\n\2\f\2\16\2\u0086\13\2\5\2\u0088")
        buf.write("\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\20\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3")
        buf.write("\"\3#\3#\3#\3$\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3")
        buf.write("*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61")
        buf.write("\7\61\u0148\n\61\f\61\16\61\u014b\13\61\3\62\6\62\u014e")
        buf.write("\n\62\r\62\16\62\u014f\3\62\3\62\6\62\u0154\n\62\r\62")
        buf.write("\16\62\u0155\3\63\6\63\u0159\n\63\r\63\16\63\u015a\3\64")
        buf.write("\5\64\u015e\n\64\3\65\3\65\3\65\5\65\u0163\n\65\3\66\3")
        buf.write("\66\3\67\6\67\u0168\n\67\r\67\16\67\u0169\38\38\78\u016e")
        buf.write("\n8\f8\168\u0171\138\39\39\59\u0175\n9\39\39\2\2:\3\5")
        buf.write("\5\6\7\7\t\b\13\t\r\n\17\13\21\f\23\r\25\16\27\17\31\20")
        buf.write("\33\21\35\22\37\23!\24#\25%\26\'\27)\30+\31-\32/\33\61")
        buf.write("\34\63\35\65\36\67\379 ;!=\"?#A$C%E&G\'I(K)M*O+Q,S-U.")
        buf.write("W/Y\60[\61]\62_\63a\64c\65e\66g\2i\2k\2m\2o\2q\67\3\2")
        buf.write("\6\4\2C\\c|\3\2\62;\4\2\13\13\"\"\4\2\f\f\16\17\2\u0180")
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
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2q\3")
        buf.write("\2\2\2\3\u0087\3\2\2\2\5\u0089\3\2\2\2\7\u0093\3\2\2\2")
        buf.write("\t\u009b\3\2\2\2\13\u00a2\3\2\2\2\r\u00a7\3\2\2\2\17\u00b0")
        buf.write("\3\2\2\2\21\u00b7\3\2\2\2\23\u00be\3\2\2\2\25\u00c5\3")
        buf.write("\2\2\2\27\u00cc\3\2\2\2\31\u00d4\3\2\2\2\33\u00db\3\2")
        buf.write("\2\2\35\u00dd\3\2\2\2\37\u00df\3\2\2\2!\u00e2\3\2\2\2")
        buf.write("#\u00e7\3\2\2\2%\u00ec\3\2\2\2\'\u00ef\3\2\2\2)\u00f4")
        buf.write("\3\2\2\2+\u00fa\3\2\2\2-\u00fe\3\2\2\2/\u0101\3\2\2\2")
        buf.write("\61\u0105\3\2\2\2\63\u010a\3\2\2\2\65\u0110\3\2\2\2\67")
        buf.write("\u0113\3\2\2\29\u0115\3\2\2\2;\u0118\3\2\2\2=\u011b\3")
        buf.write("\2\2\2?\u011e\3\2\2\2A\u0121\3\2\2\2C\u0124\3\2\2\2E\u0127")
        buf.write("\3\2\2\2G\u012a\3\2\2\2I\u012d\3\2\2\2K\u012f\3\2\2\2")
        buf.write("M\u0131\3\2\2\2O\u0133\3\2\2\2Q\u0135\3\2\2\2S\u0137\3")
        buf.write("\2\2\2U\u0139\3\2\2\2W\u013b\3\2\2\2Y\u013d\3\2\2\2[\u013f")
        buf.write("\3\2\2\2]\u0141\3\2\2\2_\u0143\3\2\2\2a\u0145\3\2\2\2")
        buf.write("c\u014d\3\2\2\2e\u0158\3\2\2\2g\u015d\3\2\2\2i\u0162\3")
        buf.write("\2\2\2k\u0164\3\2\2\2m\u0167\3\2\2\2o\u016b\3\2\2\2q\u0174")
        buf.write("\3\2\2\2su\7\17\2\2ts\3\2\2\2tu\3\2\2\2uv\3\2\2\2vz\7")
        buf.write("\f\2\2wy\7\"\2\2xw\3\2\2\2y|\3\2\2\2zx\3\2\2\2z{\3\2\2")
        buf.write("\2{\u0088\3\2\2\2|z\3\2\2\2}\177\7\17\2\2~}\3\2\2\2~\177")
        buf.write("\3\2\2\2\177\u0080\3\2\2\2\u0080\u0084\7\f\2\2\u0081\u0083")
        buf.write("\7\13\2\2\u0082\u0081\3\2\2\2\u0083\u0086\3\2\2\2\u0084")
        buf.write("\u0082\3\2\2\2\u0084\u0085\3\2\2\2\u0085\u0088\3\2\2\2")
        buf.write("\u0086\u0084\3\2\2\2\u0087t\3\2\2\2\u0087~\3\2\2\2\u0088")
        buf.write("\4\3\2\2\2\u0089\u008a\7R\2\2\u008a\u008b\7t\2\2\u008b")
        buf.write("\u008c\7g\2\2\u008c\u008d\7f\2\2\u008d\u008e\7k\2\2\u008e")
        buf.write("\u008f\7e\2\2\u008f\u0090\7c\2\2\u0090\u0091\7v\2\2\u0091")
        buf.write("\u0092\7g\2\2\u0092\6\3\2\2\2\u0093\u0094\7H\2\2\u0094")
        buf.write("\u0095\7g\2\2\u0095\u0096\7c\2\2\u0096\u0097\7v\2\2\u0097")
        buf.write("\u0098\7w\2\2\u0098\u0099\7t\2\2\u0099\u009a\7g\2\2\u009a")
        buf.write("\b\3\2\2\2\u009b\u009c\7H\2\2\u009c\u009d\7c\2\2\u009d")
        buf.write("\u009e\7e\2\2\u009e\u009f\7v\2\2\u009f\u00a0\7q\2\2\u00a0")
        buf.write("\u00a1\7t\2\2\u00a1\n\3\2\2\2\u00a2\u00a3\7I\2\2\u00a3")
        buf.write("\u00a4\7q\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6\7n\2\2\u00a6")
        buf.write("\f\3\2\2\2\u00a7\u00a8\7E\2\2\u00a8\u00a9\7q\2\2\u00a9")
        buf.write("\u00aa\7p\2\2\u00aa\u00ab\7u\2\2\u00ab\u00ac\7v\2\2\u00ac")
        buf.write("\u00ad\7c\2\2\u00ad\u00ae\7p\2\2\u00ae\u00af\7v\2\2\u00af")
        buf.write("\16\3\2\2\2\u00b0\u00b1\7C\2\2\u00b1\u00b2\7e\2\2\u00b2")
        buf.write("\u00b3\7v\2\2\u00b3\u00b4\7k\2\2\u00b4\u00b5\7q\2\2\u00b5")
        buf.write("\u00b6\7p\2\2\u00b6\20\3\2\2\2\u00b7\u00b8\7G\2\2\u00b8")
        buf.write("\u00b9\7h\2\2\u00b9\u00ba\7h\2\2\u00ba\u00bb\7g\2\2\u00bb")
        buf.write("\u00bc\7e\2\2\u00bc\u00bd\7v\2\2\u00bd\22\3\2\2\2\u00be")
        buf.write("\u00bf\7T\2\2\u00bf\u00c0\7g\2\2\u00c0\u00c1\7y\2\2\u00c1")
        buf.write("\u00c2\7c\2\2\u00c2\u00c3\7t\2\2\u00c3\u00c4\7f\2\2\u00c4")
        buf.write("\24\3\2\2\2\u00c5\u00c6\7R\2\2\u00c6\u00c7\7q\2\2\u00c7")
        buf.write("\u00c8\7n\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca\7e\2\2\u00ca")
        buf.write("\u00cb\7{\2\2\u00cb\26\3\2\2\2\u00cc\u00cd\7G\2\2\u00cd")
        buf.write("\u00ce\7z\2\2\u00ce\u00cf\7g\2\2\u00cf\u00d0\7e\2\2\u00d0")
        buf.write("\u00d1\7w\2\2\u00d1\u00d2\7v\2\2\u00d2\u00d3\7g\2\2\u00d3")
        buf.write("\30\3\2\2\2\u00d4\u00d5\7Q\2\2\u00d5\u00d6\7r\2\2\u00d6")
        buf.write("\u00d7\7v\2\2\u00d7\u00d8\7k\2\2\u00d8\u00d9\7q\2\2\u00d9")
        buf.write("\u00da\7p\2\2\u00da\32\3\2\2\2\u00db\u00dc\7U\2\2\u00dc")
        buf.write("\34\3\2\2\2\u00dd\u00de\7C\2\2\u00de\36\3\2\2\2\u00df")
        buf.write("\u00e0\7k\2\2\u00e0\u00e1\7h\2\2\u00e1 \3\2\2\2\u00e2")
        buf.write("\u00e3\7g\2\2\u00e3\u00e4\7n\2\2\u00e4\u00e5\7u\2\2\u00e5")
        buf.write("\u00e6\7g\2\2\u00e6\"\3\2\2\2\u00e7\u00e8\7g\2\2\u00e8")
        buf.write("\u00e9\7n\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb\7h\2\2\u00eb")
        buf.write("$\3\2\2\2\u00ec\u00ed\7k\2\2\u00ed\u00ee\7p\2\2\u00ee")
        buf.write("&\3\2\2\2\u00ef\u00f0\7k\2\2\u00f0\u00f1\7p\2\2\u00f1")
        buf.write("\u00f2\7k\2\2\u00f2\u00f3\7v\2\2\u00f3(\3\2\2\2\u00f4")
        buf.write("\u00f5\7w\2\2\u00f5\u00f6\7p\2\2\u00f6\u00f7\7v\2\2\u00f7")
        buf.write("\u00f8\7k\2\2\u00f8\u00f9\7n\2\2\u00f9*\3\2\2\2\u00fa")
        buf.write("\u00fb\7c\2\2\u00fb\u00fc\7p\2\2\u00fc\u00fd\7f\2\2\u00fd")
        buf.write(",\3\2\2\2\u00fe\u00ff\7q\2\2\u00ff\u0100\7t\2\2\u0100")
        buf.write(".\3\2\2\2\u0101\u0102\7p\2\2\u0102\u0103\7q\2\2\u0103")
        buf.write("\u0104\7v\2\2\u0104\60\3\2\2\2\u0105\u0106\7V\2\2\u0106")
        buf.write("\u0107\7t\2\2\u0107\u0108\7w\2\2\u0108\u0109\7g\2\2\u0109")
        buf.write("\62\3\2\2\2\u010a\u010b\7H\2\2\u010b\u010c\7c\2\2\u010c")
        buf.write("\u010d\7n\2\2\u010d\u010e\7u\2\2\u010e\u010f\7g\2\2\u010f")
        buf.write("\64\3\2\2\2\u0110\u0111\7<\2\2\u0111\u0112\7?\2\2\u0112")
        buf.write("\66\3\2\2\2\u0113\u0114\7?\2\2\u01148\3\2\2\2\u0115\u0116")
        buf.write("\7,\2\2\u0116\u0117\7?\2\2\u0117:\3\2\2\2\u0118\u0119")
        buf.write("\7\61\2\2\u0119\u011a\7?\2\2\u011a<\3\2\2\2\u011b\u011c")
        buf.write("\7-\2\2\u011c\u011d\7?\2\2\u011d>\3\2\2\2\u011e\u011f")
        buf.write("\7/\2\2\u011f\u0120\7?\2\2\u0120@\3\2\2\2\u0121\u0122")
        buf.write("\7?\2\2\u0122\u0123\7?\2\2\u0123B\3\2\2\2\u0124\u0125")
        buf.write("\7@\2\2\u0125\u0126\7?\2\2\u0126D\3\2\2\2\u0127\u0128")
        buf.write("\7>\2\2\u0128\u0129\7?\2\2\u0129F\3\2\2\2\u012a\u012b")
        buf.write("\7#\2\2\u012b\u012c\7?\2\2\u012cH\3\2\2\2\u012d\u012e")
        buf.write("\7<\2\2\u012eJ\3\2\2\2\u012f\u0130\7.\2\2\u0130L\3\2\2")
        buf.write("\2\u0131\u0132\7]\2\2\u0132N\3\2\2\2\u0133\u0134\7_\2")
        buf.write("\2\u0134P\3\2\2\2\u0135\u0136\7*\2\2\u0136R\3\2\2\2\u0137")
        buf.write("\u0138\7+\2\2\u0138T\3\2\2\2\u0139\u013a\7>\2\2\u013a")
        buf.write("V\3\2\2\2\u013b\u013c\7@\2\2\u013cX\3\2\2\2\u013d\u013e")
        buf.write("\7,\2\2\u013eZ\3\2\2\2\u013f\u0140\7\61\2\2\u0140\\\3")
        buf.write("\2\2\2\u0141\u0142\7-\2\2\u0142^\3\2\2\2\u0143\u0144\7")
        buf.write("/\2\2\u0144`\3\2\2\2\u0145\u0149\5g\64\2\u0146\u0148\5")
        buf.write("i\65\2\u0147\u0146\3\2\2\2\u0148\u014b\3\2\2\2\u0149\u0147")
        buf.write("\3\2\2\2\u0149\u014a\3\2\2\2\u014ab\3\2\2\2\u014b\u0149")
        buf.write("\3\2\2\2\u014c\u014e\5k\66\2\u014d\u014c\3\2\2\2\u014e")
        buf.write("\u014f\3\2\2\2\u014f\u014d\3\2\2\2\u014f\u0150\3\2\2\2")
        buf.write("\u0150\u0151\3\2\2\2\u0151\u0153\7\60\2\2\u0152\u0154")
        buf.write("\5k\66\2\u0153\u0152\3\2\2\2\u0154\u0155\3\2\2\2\u0155")
        buf.write("\u0153\3\2\2\2\u0155\u0156\3\2\2\2\u0156d\3\2\2\2\u0157")
        buf.write("\u0159\5k\66\2\u0158\u0157\3\2\2\2\u0159\u015a\3\2\2\2")
        buf.write("\u015a\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015bf\3\2\2")
        buf.write("\2\u015c\u015e\t\2\2\2\u015d\u015c\3\2\2\2\u015eh\3\2")
        buf.write("\2\2\u015f\u0163\5g\64\2\u0160\u0163\5k\66\2\u0161\u0163")
        buf.write("\7a\2\2\u0162\u015f\3\2\2\2\u0162\u0160\3\2\2\2\u0162")
        buf.write("\u0161\3\2\2\2\u0163j\3\2\2\2\u0164\u0165\t\3\2\2\u0165")
        buf.write("l\3\2\2\2\u0166\u0168\t\4\2\2\u0167\u0166\3\2\2\2\u0168")
        buf.write("\u0169\3\2\2\2\u0169\u0167\3\2\2\2\u0169\u016a\3\2\2\2")
        buf.write("\u016an\3\2\2\2\u016b\u016f\7%\2\2\u016c\u016e\n\5\2\2")
        buf.write("\u016d\u016c\3\2\2\2\u016e\u0171\3\2\2\2\u016f\u016d\3")
        buf.write("\2\2\2\u016f\u0170\3\2\2\2\u0170p\3\2\2\2\u0171\u016f")
        buf.write("\3\2\2\2\u0172\u0175\5m\67\2\u0173\u0175\5o8\2\u0174\u0172")
        buf.write("\3\2\2\2\u0174\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176")
        buf.write("\u0177\b9\2\2\u0177r\3\2\2\2\21\2tz~\u0084\u0087\u0149")
        buf.write("\u014f\u0155\u015a\u015d\u0162\u0169\u016f\u0174\3\b\2")
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
    S = 15
    A = 16
    IF = 17
    ELSE = 18
    ELIF = 19
    IN = 20
    INIT = 21
    UNTIL = 22
    AND = 23
    OR = 24
    NOT = 25
    TRUE = 26
    FALSE = 27
    BIND = 28
    ASIGN = 29
    TIMES_EQ = 30
    DIV_EQ = 31
    PLUS_EQ = 32
    MINUS_EQ = 33
    EQUALS = 34
    GT_EQ = 35
    LT_EQ = 36
    NOT_EQ = 37
    COL = 38
    COM = 39
    L_BRK = 40
    R_BRK = 41
    L_PAR = 42
    R_PAR = 43
    LT = 44
    GT = 45
    TIMES = 46
    DIVIDE = 47
    PLUS = 48
    MINUS = 49
    IDENTIFIER = 50
    DECIMAL = 51
    INTEGER = 52
    SKIP_ = 53

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Predicate'", "'Feature'", "'Factor'", "'Goal'", "'Constant'", 
            "'Action'", "'Effect'", "'Reward'", "'Policy'", "'Execute'", 
            "'Option'", "'S'", "'A'", "'if'", "'else'", "'elif'", "'in'", 
            "'init'", "'until'", "'and'", "'or'", "'not'", "'True'", "'False'", 
            "':='", "'='", "'*='", "'/='", "'+='", "'-='", "'=='", "'>='", 
            "'<='", "'!='", "':'", "','", "'['", "']'", "'('", "')'", "'<'", 
            "'>'", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "NL", "PREDICATE", "FEATURE", "FACTOR", 
            "GOAL", "CONSTANT", "ACTION", "EFFECT", "REWARD", "POLICY", 
            "EXECUTE", "OPTION", "S", "A", "IF", "ELSE", "ELIF", "IN", "INIT", 
            "UNTIL", "AND", "OR", "NOT", "TRUE", "FALSE", "BIND", "ASIGN", 
            "TIMES_EQ", "DIV_EQ", "PLUS_EQ", "MINUS_EQ", "EQUALS", "GT_EQ", 
            "LT_EQ", "NOT_EQ", "COL", "COM", "L_BRK", "R_BRK", "L_PAR", 
            "R_PAR", "LT", "GT", "TIMES", "DIVIDE", "PLUS", "MINUS", "IDENTIFIER", 
            "DECIMAL", "INTEGER", "SKIP_" ]

    ruleNames = [ "NL", "PREDICATE", "FEATURE", "FACTOR", "GOAL", "CONSTANT", 
                  "ACTION", "EFFECT", "REWARD", "POLICY", "EXECUTE", "OPTION", 
                  "S", "A", "IF", "ELSE", "ELIF", "IN", "INIT", "UNTIL", 
                  "AND", "OR", "NOT", "TRUE", "FALSE", "BIND", "ASIGN", 
                  "TIMES_EQ", "DIV_EQ", "PLUS_EQ", "MINUS_EQ", "EQUALS", 
                  "GT_EQ", "LT_EQ", "NOT_EQ", "COL", "COM", "L_BRK", "R_BRK", 
                  "L_PAR", "R_PAR", "LT", "GT", "TIMES", "DIVIDE", "PLUS", 
                  "MINUS", "IDENTIFIER", "DECIMAL", "INTEGER", "LETTER", 
                  "ANY_CHAR", "DIGIT", "SPACES", "COMMENT", "SKIP_" ]

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



