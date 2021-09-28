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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u01b1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\5\2\u0085")
        buf.write("\n\2\3\2\3\2\7\2\u0089\n\2\f\2\16\2\u008c\13\2\3\2\5\2")
        buf.write("\u008f\n\2\3\2\3\2\7\2\u0093\n\2\f\2\16\2\u0096\13\2\5")
        buf.write("\2\u0098\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\22\3\22")
        buf.write("\3\23\3\23\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3")
        buf.write("-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3")
        buf.write("\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\3\67\7\67")
        buf.write("\u0178\n\67\f\67\16\67\u017b\13\67\38\38\78\u017f\n8\f")
        buf.write("8\168\u0182\138\39\69\u0185\n9\r9\169\u0186\39\39\69\u018b")
        buf.write("\n9\r9\169\u018c\3:\6:\u0190\n:\r:\16:\u0191\3;\5;\u0195")
        buf.write("\n;\3<\3<\3<\5<\u019a\n<\3=\3=\3>\6>\u019f\n>\r>\16>\u01a0")
        buf.write("\3?\3?\7?\u01a5\n?\f?\16?\u01a8\13?\3@\3@\5@\u01ac\n@")
        buf.write("\3@\3@\3A\3A\2\2B\3\5\5\6\7\7\t\b\13\t\r\n\17\13\21\f")
        buf.write("\23\r\25\16\27\17\31\20\33\21\35\22\37\23!\24#\25%\26")
        buf.write("\'\27)\30+\31-\32/\33\61\34\63\35\65\36\67\379 ;!=\"?")
        buf.write("#A$C%E&G\'I(K)M*O+Q,S-U.W/Y\60[\61]\62_\63a\64c\65e\66")
        buf.write("g\67i8k9m:o;q<s=u\2w\2y\2{\2}\2\177>\u0081?\3\2\6\4\2")
        buf.write("C\\c|\3\2\62;\4\2\13\13\"\"\4\2\f\f\16\17\2\u01ba\2\3")
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
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\3\u0097")
        buf.write("\3\2\2\2\5\u0099\3\2\2\2\7\u00a3\3\2\2\2\t\u00ab\3\2\2")
        buf.write("\2\13\u00b2\3\2\2\2\r\u00b7\3\2\2\2\17\u00c0\3\2\2\2\21")
        buf.write("\u00c7\3\2\2\2\23\u00ce\3\2\2\2\25\u00d5\3\2\2\2\27\u00dc")
        buf.write("\3\2\2\2\31\u00e4\3\2\2\2\33\u00eb\3\2\2\2\35\u00f9\3")
        buf.write("\2\2\2\37\u0100\3\2\2\2!\u0103\3\2\2\2#\u0105\3\2\2\2")
        buf.write("%\u0107\3\2\2\2\'\u0109\3\2\2\2)\u010b\3\2\2\2+\u010e")
        buf.write("\3\2\2\2-\u0113\3\2\2\2/\u0118\3\2\2\2\61\u011b\3\2\2")
        buf.write("\2\63\u0120\3\2\2\2\65\u0126\3\2\2\2\67\u012a\3\2\2\2")
        buf.write("9\u012d\3\2\2\2;\u0131\3\2\2\2=\u0136\3\2\2\2?\u013c\3")
        buf.write("\2\2\2A\u013f\3\2\2\2C\u0142\3\2\2\2E\u0144\3\2\2\2G\u0147")
        buf.write("\3\2\2\2I\u014a\3\2\2\2K\u014d\3\2\2\2M\u0150\3\2\2\2")
        buf.write("O\u0153\3\2\2\2Q\u0156\3\2\2\2S\u0159\3\2\2\2U\u015c\3")
        buf.write("\2\2\2W\u015e\3\2\2\2Y\u0160\3\2\2\2[\u0162\3\2\2\2]\u0164")
        buf.write("\3\2\2\2_\u0166\3\2\2\2a\u0168\3\2\2\2c\u016a\3\2\2\2")
        buf.write("e\u016c\3\2\2\2g\u016e\3\2\2\2i\u0170\3\2\2\2k\u0172\3")
        buf.write("\2\2\2m\u0174\3\2\2\2o\u017c\3\2\2\2q\u0184\3\2\2\2s\u018f")
        buf.write("\3\2\2\2u\u0194\3\2\2\2w\u0199\3\2\2\2y\u019b\3\2\2\2")
        buf.write("{\u019e\3\2\2\2}\u01a2\3\2\2\2\177\u01ab\3\2\2\2\u0081")
        buf.write("\u01af\3\2\2\2\u0083\u0085\7\17\2\2\u0084\u0083\3\2\2")
        buf.write("\2\u0084\u0085\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u008a")
        buf.write("\7\f\2\2\u0087\u0089\7\"\2\2\u0088\u0087\3\2\2\2\u0089")
        buf.write("\u008c\3\2\2\2\u008a\u0088\3\2\2\2\u008a\u008b\3\2\2\2")
        buf.write("\u008b\u0098\3\2\2\2\u008c\u008a\3\2\2\2\u008d\u008f\7")
        buf.write("\17\2\2\u008e\u008d\3\2\2\2\u008e\u008f\3\2\2\2\u008f")
        buf.write("\u0090\3\2\2\2\u0090\u0094\7\f\2\2\u0091\u0093\7\13\2")
        buf.write("\2\u0092\u0091\3\2\2\2\u0093\u0096\3\2\2\2\u0094\u0092")
        buf.write("\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0098\3\2\2\2\u0096")
        buf.write("\u0094\3\2\2\2\u0097\u0084\3\2\2\2\u0097\u008e\3\2\2\2")
        buf.write("\u0098\4\3\2\2\2\u0099\u009a\7R\2\2\u009a\u009b\7t\2\2")
        buf.write("\u009b\u009c\7g\2\2\u009c\u009d\7f\2\2\u009d\u009e\7k")
        buf.write("\2\2\u009e\u009f\7e\2\2\u009f\u00a0\7c\2\2\u00a0\u00a1")
        buf.write("\7v\2\2\u00a1\u00a2\7g\2\2\u00a2\6\3\2\2\2\u00a3\u00a4")
        buf.write("\7H\2\2\u00a4\u00a5\7g\2\2\u00a5\u00a6\7c\2\2\u00a6\u00a7")
        buf.write("\7v\2\2\u00a7\u00a8\7w\2\2\u00a8\u00a9\7t\2\2\u00a9\u00aa")
        buf.write("\7g\2\2\u00aa\b\3\2\2\2\u00ab\u00ac\7H\2\2\u00ac\u00ad")
        buf.write("\7c\2\2\u00ad\u00ae\7e\2\2\u00ae\u00af\7v\2\2\u00af\u00b0")
        buf.write("\7q\2\2\u00b0\u00b1\7t\2\2\u00b1\n\3\2\2\2\u00b2\u00b3")
        buf.write("\7I\2\2\u00b3\u00b4\7q\2\2\u00b4\u00b5\7c\2\2\u00b5\u00b6")
        buf.write("\7n\2\2\u00b6\f\3\2\2\2\u00b7\u00b8\7E\2\2\u00b8\u00b9")
        buf.write("\7q\2\2\u00b9\u00ba\7p\2\2\u00ba\u00bb\7u\2\2\u00bb\u00bc")
        buf.write("\7v\2\2\u00bc\u00bd\7c\2\2\u00bd\u00be\7p\2\2\u00be\u00bf")
        buf.write("\7v\2\2\u00bf\16\3\2\2\2\u00c0\u00c1\7C\2\2\u00c1\u00c2")
        buf.write("\7e\2\2\u00c2\u00c3\7v\2\2\u00c3\u00c4\7k\2\2\u00c4\u00c5")
        buf.write("\7q\2\2\u00c5\u00c6\7p\2\2\u00c6\20\3\2\2\2\u00c7\u00c8")
        buf.write("\7G\2\2\u00c8\u00c9\7h\2\2\u00c9\u00ca\7h\2\2\u00ca\u00cb")
        buf.write("\7g\2\2\u00cb\u00cc\7e\2\2\u00cc\u00cd\7v\2\2\u00cd\22")
        buf.write("\3\2\2\2\u00ce\u00cf\7T\2\2\u00cf\u00d0\7g\2\2\u00d0\u00d1")
        buf.write("\7y\2\2\u00d1\u00d2\7c\2\2\u00d2\u00d3\7t\2\2\u00d3\u00d4")
        buf.write("\7f\2\2\u00d4\24\3\2\2\2\u00d5\u00d6\7R\2\2\u00d6\u00d7")
        buf.write("\7q\2\2\u00d7\u00d8\7n\2\2\u00d8\u00d9\7k\2\2\u00d9\u00da")
        buf.write("\7e\2\2\u00da\u00db\7{\2\2\u00db\26\3\2\2\2\u00dc\u00dd")
        buf.write("\7G\2\2\u00dd\u00de\7z\2\2\u00de\u00df\7g\2\2\u00df\u00e0")
        buf.write("\7e\2\2\u00e0\u00e1\7w\2\2\u00e1\u00e2\7v\2\2\u00e2\u00e3")
        buf.write("\7g\2\2\u00e3\30\3\2\2\2\u00e4\u00e5\7Q\2\2\u00e5\u00e6")
        buf.write("\7r\2\2\u00e6\u00e7\7v\2\2\u00e7\u00e8\7k\2\2\u00e8\u00e9")
        buf.write("\7q\2\2\u00e9\u00ea\7p\2\2\u00ea\32\3\2\2\2\u00eb\u00ec")
        buf.write("\7O\2\2\u00ec\u00ed\7c\2\2\u00ed\u00ee\7t\2\2\u00ee\u00ef")
        buf.write("\7m\2\2\u00ef\u00f0\7q\2\2\u00f0\u00f1\7x\2\2\u00f1\u00f2")
        buf.write("\7H\2\2\u00f2\u00f3\7g\2\2\u00f3\u00f4\7c\2\2\u00f4\u00f5")
        buf.write("\7v\2\2\u00f5\u00f6\7w\2\2\u00f6\u00f7\7t\2\2\u00f7\u00f8")
        buf.write("\7g\2\2\u00f8\34\3\2\2\2\u00f9\u00fa\7k\2\2\u00fa\u00fb")
        buf.write("\7o\2\2\u00fb\u00fc\7r\2\2\u00fc\u00fd\7q\2\2\u00fd\u00fe")
        buf.write("\7t\2\2\u00fe\u00ff\7v\2\2\u00ff\36\3\2\2\2\u0100\u0101")
        buf.write("\5!\21\2\u0101\u0102\5\'\24\2\u0102 \3\2\2\2\u0103\u0104")
        buf.write("\7U\2\2\u0104\"\3\2\2\2\u0105\u0106\7C\2\2\u0106$\3\2")
        buf.write("\2\2\u0107\u0108\7R\2\2\u0108&\3\2\2\2\u0109\u010a\7)")
        buf.write("\2\2\u010a(\3\2\2\2\u010b\u010c\7k\2\2\u010c\u010d\7h")
        buf.write("\2\2\u010d*\3\2\2\2\u010e\u010f\7g\2\2\u010f\u0110\7n")
        buf.write("\2\2\u0110\u0111\7u\2\2\u0111\u0112\7g\2\2\u0112,\3\2")
        buf.write("\2\2\u0113\u0114\7g\2\2\u0114\u0115\7n\2\2\u0115\u0116")
        buf.write("\7k\2\2\u0116\u0117\7h\2\2\u0117.\3\2\2\2\u0118\u0119")
        buf.write("\7k\2\2\u0119\u011a\7p\2\2\u011a\60\3\2\2\2\u011b\u011c")
        buf.write("\7k\2\2\u011c\u011d\7p\2\2\u011d\u011e\7k\2\2\u011e\u011f")
        buf.write("\7v\2\2\u011f\62\3\2\2\2\u0120\u0121\7w\2\2\u0121\u0122")
        buf.write("\7p\2\2\u0122\u0123\7v\2\2\u0123\u0124\7k\2\2\u0124\u0125")
        buf.write("\7n\2\2\u0125\64\3\2\2\2\u0126\u0127\7c\2\2\u0127\u0128")
        buf.write("\7p\2\2\u0128\u0129\7f\2\2\u0129\66\3\2\2\2\u012a\u012b")
        buf.write("\7q\2\2\u012b\u012c\7t\2\2\u012c8\3\2\2\2\u012d\u012e")
        buf.write("\7p\2\2\u012e\u012f\7q\2\2\u012f\u0130\7v\2\2\u0130:\3")
        buf.write("\2\2\2\u0131\u0132\7V\2\2\u0132\u0133\7t\2\2\u0133\u0134")
        buf.write("\7w\2\2\u0134\u0135\7g\2\2\u0135<\3\2\2\2\u0136\u0137")
        buf.write("\7H\2\2\u0137\u0138\7c\2\2\u0138\u0139\7n\2\2\u0139\u013a")
        buf.write("\7u\2\2\u013a\u013b\7g\2\2\u013b>\3\2\2\2\u013c\u013d")
        buf.write("\7<\2\2\u013d\u013e\7?\2\2\u013e@\3\2\2\2\u013f\u0140")
        buf.write("\7/\2\2\u0140\u0141\7@\2\2\u0141B\3\2\2\2\u0142\u0143")
        buf.write("\7?\2\2\u0143D\3\2\2\2\u0144\u0145\7,\2\2\u0145\u0146")
        buf.write("\7?\2\2\u0146F\3\2\2\2\u0147\u0148\7\61\2\2\u0148\u0149")
        buf.write("\7?\2\2\u0149H\3\2\2\2\u014a\u014b\7-\2\2\u014b\u014c")
        buf.write("\7?\2\2\u014cJ\3\2\2\2\u014d\u014e\7/\2\2\u014e\u014f")
        buf.write("\7?\2\2\u014fL\3\2\2\2\u0150\u0151\7?\2\2\u0151\u0152")
        buf.write("\7?\2\2\u0152N\3\2\2\2\u0153\u0154\7@\2\2\u0154\u0155")
        buf.write("\7?\2\2\u0155P\3\2\2\2\u0156\u0157\7>\2\2\u0157\u0158")
        buf.write("\7?\2\2\u0158R\3\2\2\2\u0159\u015a\7#\2\2\u015a\u015b")
        buf.write("\7?\2\2\u015bT\3\2\2\2\u015c\u015d\7<\2\2\u015dV\3\2\2")
        buf.write("\2\u015e\u015f\7.\2\2\u015fX\3\2\2\2\u0160\u0161\7]\2")
        buf.write("\2\u0161Z\3\2\2\2\u0162\u0163\7_\2\2\u0163\\\3\2\2\2\u0164")
        buf.write("\u0165\7*\2\2\u0165^\3\2\2\2\u0166\u0167\7+\2\2\u0167")
        buf.write("`\3\2\2\2\u0168\u0169\7>\2\2\u0169b\3\2\2\2\u016a\u016b")
        buf.write("\7@\2\2\u016bd\3\2\2\2\u016c\u016d\7,\2\2\u016df\3\2\2")
        buf.write("\2\u016e\u016f\7\61\2\2\u016fh\3\2\2\2\u0170\u0171\7-")
        buf.write("\2\2\u0171j\3\2\2\2\u0172\u0173\7/\2\2\u0173l\3\2\2\2")
        buf.write("\u0174\u0175\5o8\2\u0175\u0179\7\60\2\2\u0176\u0178\5")
        buf.write("u;\2\u0177\u0176\3\2\2\2\u0178\u017b\3\2\2\2\u0179\u0177")
        buf.write("\3\2\2\2\u0179\u017a\3\2\2\2\u017an\3\2\2\2\u017b\u0179")
        buf.write("\3\2\2\2\u017c\u0180\5u;\2\u017d\u017f\5w<\2\u017e\u017d")
        buf.write("\3\2\2\2\u017f\u0182\3\2\2\2\u0180\u017e\3\2\2\2\u0180")
        buf.write("\u0181\3\2\2\2\u0181p\3\2\2\2\u0182\u0180\3\2\2\2\u0183")
        buf.write("\u0185\5y=\2\u0184\u0183\3\2\2\2\u0185\u0186\3\2\2\2\u0186")
        buf.write("\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0188\3\2\2\2")
        buf.write("\u0188\u018a\7\60\2\2\u0189\u018b\5y=\2\u018a\u0189\3")
        buf.write("\2\2\2\u018b\u018c\3\2\2\2\u018c\u018a\3\2\2\2\u018c\u018d")
        buf.write("\3\2\2\2\u018dr\3\2\2\2\u018e\u0190\5y=\2\u018f\u018e")
        buf.write("\3\2\2\2\u0190\u0191\3\2\2\2\u0191\u018f\3\2\2\2\u0191")
        buf.write("\u0192\3\2\2\2\u0192t\3\2\2\2\u0193\u0195\t\2\2\2\u0194")
        buf.write("\u0193\3\2\2\2\u0195v\3\2\2\2\u0196\u019a\5u;\2\u0197")
        buf.write("\u019a\5y=\2\u0198\u019a\7a\2\2\u0199\u0196\3\2\2\2\u0199")
        buf.write("\u0197\3\2\2\2\u0199\u0198\3\2\2\2\u019ax\3\2\2\2\u019b")
        buf.write("\u019c\t\3\2\2\u019cz\3\2\2\2\u019d\u019f\t\4\2\2\u019e")
        buf.write("\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u019e\3\2\2\2")
        buf.write("\u01a0\u01a1\3\2\2\2\u01a1|\3\2\2\2\u01a2\u01a6\7%\2\2")
        buf.write("\u01a3\u01a5\n\5\2\2\u01a4\u01a3\3\2\2\2\u01a5\u01a8\3")
        buf.write("\2\2\2\u01a6\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7~")
        buf.write("\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a9\u01ac\5{>\2\u01aa\u01ac")
        buf.write("\5}?\2\u01ab\u01a9\3\2\2\2\u01ab\u01aa\3\2\2\2\u01ac\u01ad")
        buf.write("\3\2\2\2\u01ad\u01ae\b@\2\2\u01ae\u0080\3\2\2\2\u01af")
        buf.write("\u01b0\13\2\2\2\u01b0\u0082\3\2\2\2\22\2\u0084\u008a\u008e")
        buf.write("\u0094\u0097\u0179\u0180\u0186\u018c\u0191\u0194\u0199")
        buf.write("\u01a0\u01a6\u01ab\3\b\2\2")
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
    AND = 28
    OR = 29
    NOT = 30
    TRUE = 31
    FALSE = 32
    BIND = 33
    PREDICT = 34
    ASSIGN = 35
    TIMES_EQ = 36
    DIV_EQ = 37
    PLUS_EQ = 38
    MINUS_EQ = 39
    EQ_TO = 40
    GT_EQ = 41
    LT_EQ = 42
    NOT_EQ = 43
    COL = 44
    COM = 45
    L_BRK = 46
    R_BRK = 47
    L_PAR = 48
    R_PAR = 49
    LT = 50
    GT = 51
    TIMES = 52
    DIVIDE = 53
    PLUS = 54
    MINUS = 55
    FNAME = 56
    IDENTIFIER = 57
    DECIMAL = 58
    INTEGER = 59
    SKIP_ = 60
    ANY = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Predicate'", "'Feature'", "'Factor'", "'Goal'", "'Constant'", 
            "'Action'", "'Effect'", "'Reward'", "'Policy'", "'Execute'", 
            "'Option'", "'MarkovFeature'", "'import'", "'S'", "'A'", "'P'", 
            "'''", "'if'", "'else'", "'elif'", "'in'", "'init'", "'until'", 
            "'and'", "'or'", "'not'", "'True'", "'False'", "':='", "'->'", 
            "'='", "'*='", "'/='", "'+='", "'-='", "'=='", "'>='", "'<='", 
            "'!='", "':'", "','", "'['", "']'", "'('", "')'", "'<'", "'>'", 
            "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "NL", "PREDICATE", "FEATURE", "FACTOR", 
            "GOAL", "CONSTANT", "ACTION", "EFFECT", "REWARD", "POLICY", 
            "EXECUTE", "OPTION", "MARKOVFEATURE", "IMPORT", "S_PRIME", "S", 
            "A", "P", "PRIME", "IF", "ELSE", "ELIF", "IN", "INIT", "UNTIL", 
            "AND", "OR", "NOT", "TRUE", "FALSE", "BIND", "PREDICT", "ASSIGN", 
            "TIMES_EQ", "DIV_EQ", "PLUS_EQ", "MINUS_EQ", "EQ_TO", "GT_EQ", 
            "LT_EQ", "NOT_EQ", "COL", "COM", "L_BRK", "R_BRK", "L_PAR", 
            "R_PAR", "LT", "GT", "TIMES", "DIVIDE", "PLUS", "MINUS", "FNAME", 
            "IDENTIFIER", "DECIMAL", "INTEGER", "SKIP_", "ANY" ]

    ruleNames = [ "NL", "PREDICATE", "FEATURE", "FACTOR", "GOAL", "CONSTANT", 
                  "ACTION", "EFFECT", "REWARD", "POLICY", "EXECUTE", "OPTION", 
                  "MARKOVFEATURE", "IMPORT", "S_PRIME", "S", "A", "P", "PRIME", 
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



