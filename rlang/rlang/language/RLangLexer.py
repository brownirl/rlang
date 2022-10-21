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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2P")
        buf.write("\u0224\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\3\2\5\2\u00a7\n")
        buf.write("\2\3\2\3\2\7\2\u00ab\n\2\f\2\16\2\u00ae\13\2\3\2\5\2\u00b1")
        buf.write("\n\2\3\2\3\2\7\2\u00b5\n\2\f\2\16\2\u00b8\13\2\5\2\u00ba")
        buf.write("\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3")
        buf.write("!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3")
        buf.write("$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3\'\3\'\3")
        buf.write("\'\3\'\3(\3(\3(\3)\3)\3)\3)\3*\3*\3*\3*\3*\3+\3+\3+\3")
        buf.write("+\3+\3+\3,\3,\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3\60\3\60")
        buf.write("\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\64")
        buf.write("\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67")
        buf.write("\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3")
        buf.write("@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3G\7G\u01e9")
        buf.write("\nG\fG\16G\u01ec\13G\3H\3H\7H\u01f0\nH\fH\16H\u01f3\13")
        buf.write("H\3I\6I\u01f6\nI\rI\16I\u01f7\3I\3I\6I\u01fc\nI\rI\16")
        buf.write("I\u01fd\3J\6J\u0201\nJ\rJ\16J\u0202\3K\3K\3L\5L\u0208")
        buf.write("\nL\3M\3M\3M\5M\u020d\nM\3N\3N\3O\6O\u0212\nO\rO\16O\u0213")
        buf.write("\3P\3P\7P\u0218\nP\fP\16P\u021b\13P\3Q\3Q\5Q\u021f\nQ")
        buf.write("\3Q\3Q\3R\3R\2\2S\3\5\5\6\7\7\t\b\13\t\r\n\17\13\21\f")
        buf.write("\23\r\25\16\27\17\31\20\33\21\35\22\37\23!\24#\25%\26")
        buf.write("\'\27)\30+\31-\32/\33\61\34\63\35\65\36\67\379 ;!=\"?")
        buf.write("#A$C%E&G\'I(K)M*O+Q,S-U.W/Y\60[\61]\62_\63a\64c\65e\66")
        buf.write("g\67i8k9m:o;q<s=u>w?y@{A}B\177C\u0081D\u0083E\u0085F\u0087")
        buf.write("G\u0089H\u008bI\u008dJ\u008fK\u0091L\u0093M\u0095N\u0097")
        buf.write("\2\u0099\2\u009b\2\u009d\2\u009f\2\u00a1O\u00a3P\3\2\6")
        buf.write("\4\2C\\c|\3\2\62;\4\2\13\13\"\"\4\2\f\f\16\17\2\u022d")
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
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u00a1\3\2\2")
        buf.write("\2\2\u00a3\3\2\2\2\3\u00b9\3\2\2\2\5\u00bb\3\2\2\2\7\u00c2")
        buf.write("\3\2\2\2\t\u00ce\3\2\2\2\13\u00d8\3\2\2\2\r\u00e0\3\2")
        buf.write("\2\2\17\u00e7\3\2\2\2\21\u00ec\3\2\2\2\23\u00f2\3\2\2")
        buf.write("\2\25\u00f9\3\2\2\2\27\u0102\3\2\2\2\31\u0109\3\2\2\2")
        buf.write("\33\u0110\3\2\2\2\35\u0117\3\2\2\2\37\u011e\3\2\2\2!\u0126")
        buf.write("\3\2\2\2#\u012d\3\2\2\2%\u013b\3\2\2\2\'\u013f\3\2\2\2")
        buf.write(")\u0145\3\2\2\2+\u0149\3\2\2\2-\u014e\3\2\2\2/\u0152\3")
        buf.write("\2\2\2\61\u0155\3\2\2\2\63\u0157\3\2\2\2\65\u0159\3\2")
        buf.write("\2\2\67\u015b\3\2\2\29\u015d\3\2\2\2;\u0160\3\2\2\2=\u0165")
        buf.write("\3\2\2\2?\u016a\3\2\2\2A\u016d\3\2\2\2C\u0172\3\2\2\2")
        buf.write("E\u0178\3\2\2\2G\u017d\3\2\2\2I\u0182\3\2\2\2K\u0188\3")
        buf.write("\2\2\2M\u018d\3\2\2\2O\u0191\3\2\2\2Q\u0194\3\2\2\2S\u0198")
        buf.write("\3\2\2\2U\u019d\3\2\2\2W\u01a3\3\2\2\2Y\u01a7\3\2\2\2")
        buf.write("[\u01aa\3\2\2\2]\u01ad\3\2\2\2_\u01af\3\2\2\2a\u01b2\3")
        buf.write("\2\2\2c\u01b5\3\2\2\2e\u01b8\3\2\2\2g\u01bb\3\2\2\2i\u01be")
        buf.write("\3\2\2\2k\u01c1\3\2\2\2m\u01c4\3\2\2\2o\u01c7\3\2\2\2")
        buf.write("q\u01c9\3\2\2\2s\u01cb\3\2\2\2u\u01cd\3\2\2\2w\u01cf\3")
        buf.write("\2\2\2y\u01d1\3\2\2\2{\u01d3\3\2\2\2}\u01d5\3\2\2\2\177")
        buf.write("\u01d7\3\2\2\2\u0081\u01d9\3\2\2\2\u0083\u01db\3\2\2\2")
        buf.write("\u0085\u01dd\3\2\2\2\u0087\u01df\3\2\2\2\u0089\u01e1\3")
        buf.write("\2\2\2\u008b\u01e3\3\2\2\2\u008d\u01e5\3\2\2\2\u008f\u01ed")
        buf.write("\3\2\2\2\u0091\u01f5\3\2\2\2\u0093\u0200\3\2\2\2\u0095")
        buf.write("\u0204\3\2\2\2\u0097\u0207\3\2\2\2\u0099\u020c\3\2\2\2")
        buf.write("\u009b\u020e\3\2\2\2\u009d\u0211\3\2\2\2\u009f\u0215\3")
        buf.write("\2\2\2\u00a1\u021e\3\2\2\2\u00a3\u0222\3\2\2\2\u00a5\u00a7")
        buf.write("\7\17\2\2\u00a6\u00a5\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7")
        buf.write("\u00a8\3\2\2\2\u00a8\u00ac\7\f\2\2\u00a9\u00ab\7\"\2\2")
        buf.write("\u00aa\u00a9\3\2\2\2\u00ab\u00ae\3\2\2\2\u00ac\u00aa\3")
        buf.write("\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00ba\3\2\2\2\u00ae\u00ac")
        buf.write("\3\2\2\2\u00af\u00b1\7\17\2\2\u00b0\u00af\3\2\2\2\u00b0")
        buf.write("\u00b1\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b6\7\f\2\2")
        buf.write("\u00b3\u00b5\7\13\2\2\u00b4\u00b3\3\2\2\2\u00b5\u00b8")
        buf.write("\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7")
        buf.write("\u00ba\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b9\u00a6\3\2\2\2")
        buf.write("\u00b9\u00b0\3\2\2\2\u00ba\4\3\2\2\2\u00bb\u00bc\7k\2")
        buf.write("\2\u00bc\u00bd\7o\2\2\u00bd\u00be\7r\2\2\u00be\u00bf\7")
        buf.write("q\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1\7v\2\2\u00c1\6\3")
        buf.write("\2\2\2\u00c2\u00c3\7R\2\2\u00c3\u00c4\7t\2\2\u00c4\u00c5")
        buf.write("\7q\2\2\u00c5\u00c6\7r\2\2\u00c6\u00c7\7q\2\2\u00c7\u00c8")
        buf.write("\7u\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca\7v\2\2\u00ca\u00cb")
        buf.write("\7k\2\2\u00cb\u00cc\7q\2\2\u00cc\u00cd\7p\2\2\u00cd\b")
        buf.write("\3\2\2\2\u00ce\u00cf\7R\2\2\u00cf\u00d0\7t\2\2\u00d0\u00d1")
        buf.write("\7g\2\2\u00d1\u00d2\7f\2\2\u00d2\u00d3\7k\2\2\u00d3\u00d4")
        buf.write("\7e\2\2\u00d4\u00d5\7c\2\2\u00d5\u00d6\7v\2\2\u00d6\u00d7")
        buf.write("\7g\2\2\u00d7\n\3\2\2\2\u00d8\u00d9\7H\2\2\u00d9\u00da")
        buf.write("\7g\2\2\u00da\u00db\7c\2\2\u00db\u00dc\7v\2\2\u00dc\u00dd")
        buf.write("\7w\2\2\u00dd\u00de\7t\2\2\u00de\u00df\7g\2\2\u00df\f")
        buf.write("\3\2\2\2\u00e0\u00e1\7H\2\2\u00e1\u00e2\7c\2\2\u00e2\u00e3")
        buf.write("\7e\2\2\u00e3\u00e4\7v\2\2\u00e4\u00e5\7q\2\2\u00e5\u00e6")
        buf.write("\7t\2\2\u00e6\16\3\2\2\2\u00e7\u00e8\7I\2\2\u00e8\u00e9")
        buf.write("\7q\2\2\u00e9\u00ea\7c\2\2\u00ea\u00eb\7n\2\2\u00eb\20")
        buf.write("\3\2\2\2\u00ec\u00ed\7E\2\2\u00ed\u00ee\7n\2\2\u00ee\u00ef")
        buf.write("\7c\2\2\u00ef\u00f0\7u\2\2\u00f0\u00f1\7u\2\2\u00f1\22")
        buf.write("\3\2\2\2\u00f2\u00f3\7Q\2\2\u00f3\u00f4\7d\2\2\u00f4\u00f5")
        buf.write("\7l\2\2\u00f5\u00f6\7g\2\2\u00f6\u00f7\7e\2\2\u00f7\u00f8")
        buf.write("\7v\2\2\u00f8\24\3\2\2\2\u00f9\u00fa\7E\2\2\u00fa\u00fb")
        buf.write("\7q\2\2\u00fb\u00fc\7p\2\2\u00fc\u00fd\7u\2\2\u00fd\u00fe")
        buf.write("\7v\2\2\u00fe\u00ff\7c\2\2\u00ff\u0100\7p\2\2\u0100\u0101")
        buf.write("\7v\2\2\u0101\26\3\2\2\2\u0102\u0103\7C\2\2\u0103\u0104")
        buf.write("\7e\2\2\u0104\u0105\7v\2\2\u0105\u0106\7k\2\2\u0106\u0107")
        buf.write("\7q\2\2\u0107\u0108\7p\2\2\u0108\30\3\2\2\2\u0109\u010a")
        buf.write("\7G\2\2\u010a\u010b\7h\2\2\u010b\u010c\7h\2\2\u010c\u010d")
        buf.write("\7g\2\2\u010d\u010e\7e\2\2\u010e\u010f\7v\2\2\u010f\32")
        buf.write("\3\2\2\2\u0110\u0111\7T\2\2\u0111\u0112\7g\2\2\u0112\u0113")
        buf.write("\7y\2\2\u0113\u0114\7c\2\2\u0114\u0115\7t\2\2\u0115\u0116")
        buf.write("\7f\2\2\u0116\34\3\2\2\2\u0117\u0118\7R\2\2\u0118\u0119")
        buf.write("\7q\2\2\u0119\u011a\7n\2\2\u011a\u011b\7k\2\2\u011b\u011c")
        buf.write("\7e\2\2\u011c\u011d\7{\2\2\u011d\36\3\2\2\2\u011e\u011f")
        buf.write("\7G\2\2\u011f\u0120\7z\2\2\u0120\u0121\7g\2\2\u0121\u0122")
        buf.write("\7e\2\2\u0122\u0123\7w\2\2\u0123\u0124\7v\2\2\u0124\u0125")
        buf.write("\7g\2\2\u0125 \3\2\2\2\u0126\u0127\7Q\2\2\u0127\u0128")
        buf.write("\7r\2\2\u0128\u0129\7v\2\2\u0129\u012a\7k\2\2\u012a\u012b")
        buf.write("\7q\2\2\u012b\u012c\7p\2\2\u012c\"\3\2\2\2\u012d\u012e")
        buf.write("\7O\2\2\u012e\u012f\7c\2\2\u012f\u0130\7t\2\2\u0130\u0131")
        buf.write("\7m\2\2\u0131\u0132\7q\2\2\u0132\u0133\7x\2\2\u0133\u0134")
        buf.write("\7H\2\2\u0134\u0135\7g\2\2\u0135\u0136\7c\2\2\u0136\u0137")
        buf.write("\7v\2\2\u0137\u0138\7w\2\2\u0138\u0139\7t\2\2\u0139\u013a")
        buf.write("\7g\2\2\u013a$\3\2\2\2\u013b\u013c\7k\2\2\u013c\u013d")
        buf.write("\7p\2\2\u013d\u013e\7v\2\2\u013e&\3\2\2\2\u013f\u0140")
        buf.write("\7h\2\2\u0140\u0141\7n\2\2\u0141\u0142\7q\2\2\u0142\u0143")
        buf.write("\7c\2\2\u0143\u0144\7v\2\2\u0144(\3\2\2\2\u0145\u0146")
        buf.write("\7u\2\2\u0146\u0147\7v\2\2\u0147\u0148\7t\2\2\u0148*\3")
        buf.write("\2\2\2\u0149\u014a\7n\2\2\u014a\u014b\7k\2\2\u014b\u014c")
        buf.write("\7u\2\2\u014c\u014d\7v\2\2\u014d,\3\2\2\2\u014e\u014f")
        buf.write("\7u\2\2\u014f\u0150\7g\2\2\u0150\u0151\7v\2\2\u0151.\3")
        buf.write("\2\2\2\u0152\u0153\5\61\31\2\u0153\u0154\5\67\34\2\u0154")
        buf.write("\60\3\2\2\2\u0155\u0156\7U\2\2\u0156\62\3\2\2\2\u0157")
        buf.write("\u0158\7C\2\2\u0158\64\3\2\2\2\u0159\u015a\7R\2\2\u015a")
        buf.write("\66\3\2\2\2\u015b\u015c\7)\2\2\u015c8\3\2\2\2\u015d\u015e")
        buf.write("\7k\2\2\u015e\u015f\7h\2\2\u015f:\3\2\2\2\u0160\u0161")
        buf.write("\7g\2\2\u0161\u0162\7n\2\2\u0162\u0163\7u\2\2\u0163\u0164")
        buf.write("\7g\2\2\u0164<\3\2\2\2\u0165\u0166\7g\2\2\u0166\u0167")
        buf.write("\7n\2\2\u0167\u0168\7k\2\2\u0168\u0169\7h\2\2\u0169>\3")
        buf.write("\2\2\2\u016a\u016b\7k\2\2\u016b\u016c\7p\2\2\u016c@\3")
        buf.write("\2\2\2\u016d\u016e\7k\2\2\u016e\u016f\7p\2\2\u016f\u0170")
        buf.write("\7k\2\2\u0170\u0171\7v\2\2\u0171B\3\2\2\2\u0172\u0173")
        buf.write("\7w\2\2\u0173\u0174\7p\2\2\u0174\u0175\7v\2\2\u0175\u0176")
        buf.write("\7k\2\2\u0176\u0177\7n\2\2\u0177D\3\2\2\2\u0178\u0179")
        buf.write("\7y\2\2\u0179\u017a\7k\2\2\u017a\u017b\7v\2\2\u017b\u017c")
        buf.write("\7j\2\2\u017cF\3\2\2\2\u017d\u017e\7v\2\2\u017e\u017f")
        buf.write("\7j\2\2\u017f\u0180\7g\2\2\u0180\u0181\7p\2\2\u0181H\3")
        buf.write("\2\2\2\u0182\u0183\7p\2\2\u0183\u0184\7g\2\2\u0184\u0185")
        buf.write("\7x\2\2\u0185\u0186\7g\2\2\u0186\u0187\7t\2\2\u0187J\3")
        buf.write("\2\2\2\u0188\u0189\7o\2\2\u0189\u018a\7c\2\2\u018a\u018b")
        buf.write("\7k\2\2\u018b\u018c\7p\2\2\u018cL\3\2\2\2\u018d\u018e")
        buf.write("\7c\2\2\u018e\u018f\7p\2\2\u018f\u0190\7f\2\2\u0190N\3")
        buf.write("\2\2\2\u0191\u0192\7q\2\2\u0192\u0193\7t\2\2\u0193P\3")
        buf.write("\2\2\2\u0194\u0195\7p\2\2\u0195\u0196\7q\2\2\u0196\u0197")
        buf.write("\7v\2\2\u0197R\3\2\2\2\u0198\u0199\7V\2\2\u0199\u019a")
        buf.write("\7t\2\2\u019a\u019b\7w\2\2\u019b\u019c\7g\2\2\u019cT\3")
        buf.write("\2\2\2\u019d\u019e\7H\2\2\u019e\u019f\7c\2\2\u019f\u01a0")
        buf.write("\7n\2\2\u01a0\u01a1\7u\2\2\u01a1\u01a2\7g\2\2\u01a2V\3")
        buf.write("\2\2\2\u01a3\u01a4\7C\2\2\u01a4\u01a5\7p\2\2\u01a5\u01a6")
        buf.write("\7{\2\2\u01a6X\3\2\2\2\u01a7\u01a8\7<\2\2\u01a8\u01a9")
        buf.write("\7?\2\2\u01a9Z\3\2\2\2\u01aa\u01ab\7/\2\2\u01ab\u01ac")
        buf.write("\7@\2\2\u01ac\\\3\2\2\2\u01ad\u01ae\7?\2\2\u01ae^\3\2")
        buf.write("\2\2\u01af\u01b0\7,\2\2\u01b0\u01b1\7?\2\2\u01b1`\3\2")
        buf.write("\2\2\u01b2\u01b3\7\61\2\2\u01b3\u01b4\7?\2\2\u01b4b\3")
        buf.write("\2\2\2\u01b5\u01b6\7-\2\2\u01b6\u01b7\7?\2\2\u01b7d\3")
        buf.write("\2\2\2\u01b8\u01b9\7/\2\2\u01b9\u01ba\7?\2\2\u01baf\3")
        buf.write("\2\2\2\u01bb\u01bc\7?\2\2\u01bc\u01bd\7?\2\2\u01bdh\3")
        buf.write("\2\2\2\u01be\u01bf\7@\2\2\u01bf\u01c0\7?\2\2\u01c0j\3")
        buf.write("\2\2\2\u01c1\u01c2\7>\2\2\u01c2\u01c3\7?\2\2\u01c3l\3")
        buf.write("\2\2\2\u01c4\u01c5\7#\2\2\u01c5\u01c6\7?\2\2\u01c6n\3")
        buf.write("\2\2\2\u01c7\u01c8\7<\2\2\u01c8p\3\2\2\2\u01c9\u01ca\7")
        buf.write(".\2\2\u01car\3\2\2\2\u01cb\u01cc\7]\2\2\u01cct\3\2\2\2")
        buf.write("\u01cd\u01ce\7_\2\2\u01cev\3\2\2\2\u01cf\u01d0\7}\2\2")
        buf.write("\u01d0x\3\2\2\2\u01d1\u01d2\7\177\2\2\u01d2z\3\2\2\2\u01d3")
        buf.write("\u01d4\7*\2\2\u01d4|\3\2\2\2\u01d5\u01d6\7+\2\2\u01d6")
        buf.write("~\3\2\2\2\u01d7\u01d8\7>\2\2\u01d8\u0080\3\2\2\2\u01d9")
        buf.write("\u01da\7@\2\2\u01da\u0082\3\2\2\2\u01db\u01dc\7,\2\2\u01dc")
        buf.write("\u0084\3\2\2\2\u01dd\u01de\7\61\2\2\u01de\u0086\3\2\2")
        buf.write("\2\u01df\u01e0\7-\2\2\u01e0\u0088\3\2\2\2\u01e1\u01e2")
        buf.write("\7/\2\2\u01e2\u008a\3\2\2\2\u01e3\u01e4\7$\2\2\u01e4\u008c")
        buf.write("\3\2\2\2\u01e5\u01e6\5\u008fH\2\u01e6\u01ea\5\u0095K\2")
        buf.write("\u01e7\u01e9\5\u0097L\2\u01e8\u01e7\3\2\2\2\u01e9\u01ec")
        buf.write("\3\2\2\2\u01ea\u01e8\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb")
        buf.write("\u008e\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ed\u01f1\5\u0097")
        buf.write("L\2\u01ee\u01f0\5\u0099M\2\u01ef\u01ee\3\2\2\2\u01f0\u01f3")
        buf.write("\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2")
        buf.write("\u0090\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f4\u01f6\5\u009b")
        buf.write("N\2\u01f5\u01f4\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01f5")
        buf.write("\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9")
        buf.write("\u01fb\5\u0095K\2\u01fa\u01fc\5\u009bN\2\u01fb\u01fa\3")
        buf.write("\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fd\u01fe")
        buf.write("\3\2\2\2\u01fe\u0092\3\2\2\2\u01ff\u0201\5\u009bN\2\u0200")
        buf.write("\u01ff\3\2\2\2\u0201\u0202\3\2\2\2\u0202\u0200\3\2\2\2")
        buf.write("\u0202\u0203\3\2\2\2\u0203\u0094\3\2\2\2\u0204\u0205\7")
        buf.write("\60\2\2\u0205\u0096\3\2\2\2\u0206\u0208\t\2\2\2\u0207")
        buf.write("\u0206\3\2\2\2\u0208\u0098\3\2\2\2\u0209\u020d\5\u0097")
        buf.write("L\2\u020a\u020d\5\u009bN\2\u020b\u020d\7a\2\2\u020c\u0209")
        buf.write("\3\2\2\2\u020c\u020a\3\2\2\2\u020c\u020b\3\2\2\2\u020d")
        buf.write("\u009a\3\2\2\2\u020e\u020f\t\3\2\2\u020f\u009c\3\2\2\2")
        buf.write("\u0210\u0212\t\4\2\2\u0211\u0210\3\2\2\2\u0212\u0213\3")
        buf.write("\2\2\2\u0213\u0211\3\2\2\2\u0213\u0214\3\2\2\2\u0214\u009e")
        buf.write("\3\2\2\2\u0215\u0219\7%\2\2\u0216\u0218\n\5\2\2\u0217")
        buf.write("\u0216\3\2\2\2\u0218\u021b\3\2\2\2\u0219\u0217\3\2\2\2")
        buf.write("\u0219\u021a\3\2\2\2\u021a\u00a0\3\2\2\2\u021b\u0219\3")
        buf.write("\2\2\2\u021c\u021f\5\u009dO\2\u021d\u021f\5\u009fP\2\u021e")
        buf.write("\u021c\3\2\2\2\u021e\u021d\3\2\2\2\u021f\u0220\3\2\2\2")
        buf.write("\u0220\u0221\bQ\2\2\u0221\u00a2\3\2\2\2\u0222\u0223\13")
        buf.write("\2\2\2\u0223\u00a4\3\2\2\2\22\2\u00a6\u00ac\u00b0\u00b6")
        buf.write("\u00b9\u01ea\u01f1\u01f7\u01fd\u0202\u0207\u020c\u0213")
        buf.write("\u0219\u021e\3\b\2\2")
        return buf.getvalue()


class RLangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INDENT = 1
    DEDENT = 2
    NL = 3
    IMPORT = 4
    PROPOSITION = 5
    PREDICATE = 6
    FEATURE = 7
    FACTOR = 8
    GOAL = 9
    CLASS = 10
    OBJECT = 11
    CONSTANT = 12
    ACTION = 13
    EFFECT = 14
    REWARD = 15
    POLICY = 16
    EXECUTE = 17
    OPTION = 18
    MARKOVFEATURE = 19
    INT = 20
    FLOAT = 21
    STR = 22
    LIST = 23
    SET = 24
    S_PRIME = 25
    S = 26
    A = 27
    P = 28
    PRIME = 29
    IF = 30
    ELSE = 31
    ELIF = 32
    IN = 33
    INIT = 34
    UNTIL = 35
    WITH = 36
    THEN = 37
    NEVER = 38
    MAIN = 39
    AND = 40
    OR = 41
    NOT = 42
    TRUE = 43
    FALSE = 44
    ANY_CONDITION = 45
    BIND = 46
    PREDICT = 47
    ASSIGN = 48
    TIMES_EQ = 49
    DIV_EQ = 50
    PLUS_EQ = 51
    MINUS_EQ = 52
    EQ_TO = 53
    GT_EQ = 54
    LT_EQ = 55
    NOT_EQ = 56
    COL = 57
    COM = 58
    L_BRK = 59
    R_BRK = 60
    L_CBRK = 61
    R_CBRK = 62
    L_PAR = 63
    R_PAR = 64
    LT = 65
    GT = 66
    TIMES = 67
    DIVIDE = 68
    PLUS = 69
    MINUS = 70
    QUOTE = 71
    FNAME = 72
    IDENTIFIER = 73
    DECIMAL = 74
    INTEGER = 75
    DOT = 76
    SKIP_ = 77
    ANY = 78

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'import'", "'Proposition'", "'Predicate'", "'Feature'", "'Factor'", 
            "'Goal'", "'Class'", "'Object'", "'Constant'", "'Action'", "'Effect'", 
            "'Reward'", "'Policy'", "'Execute'", "'Option'", "'MarkovFeature'", 
            "'int'", "'float'", "'str'", "'list'", "'set'", "'S'", "'A'", 
            "'P'", "'''", "'if'", "'else'", "'elif'", "'in'", "'init'", 
            "'until'", "'with'", "'then'", "'never'", "'main'", "'and'", 
            "'or'", "'not'", "'True'", "'False'", "'Any'", "':='", "'->'", 
            "'='", "'*='", "'/='", "'+='", "'-='", "'=='", "'>='", "'<='", 
            "'!='", "':'", "','", "'['", "']'", "'{'", "'}'", "'('", "')'", 
            "'<'", "'>'", "'*'", "'/'", "'+'", "'-'", "'\"'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "NL", "IMPORT", "PROPOSITION", "PREDICATE", 
            "FEATURE", "FACTOR", "GOAL", "CLASS", "OBJECT", "CONSTANT", 
            "ACTION", "EFFECT", "REWARD", "POLICY", "EXECUTE", "OPTION", 
            "MARKOVFEATURE", "INT", "FLOAT", "STR", "LIST", "SET", "S_PRIME", 
            "S", "A", "P", "PRIME", "IF", "ELSE", "ELIF", "IN", "INIT", 
            "UNTIL", "WITH", "THEN", "NEVER", "MAIN", "AND", "OR", "NOT", 
            "TRUE", "FALSE", "ANY_CONDITION", "BIND", "PREDICT", "ASSIGN", 
            "TIMES_EQ", "DIV_EQ", "PLUS_EQ", "MINUS_EQ", "EQ_TO", "GT_EQ", 
            "LT_EQ", "NOT_EQ", "COL", "COM", "L_BRK", "R_BRK", "L_CBRK", 
            "R_CBRK", "L_PAR", "R_PAR", "LT", "GT", "TIMES", "DIVIDE", "PLUS", 
            "MINUS", "QUOTE", "FNAME", "IDENTIFIER", "DECIMAL", "INTEGER", 
            "DOT", "SKIP_", "ANY" ]

    ruleNames = [ "NL", "IMPORT", "PROPOSITION", "PREDICATE", "FEATURE", 
                  "FACTOR", "GOAL", "CLASS", "OBJECT", "CONSTANT", "ACTION", 
                  "EFFECT", "REWARD", "POLICY", "EXECUTE", "OPTION", "MARKOVFEATURE", 
                  "INT", "FLOAT", "STR", "LIST", "SET", "S_PRIME", "S", 
                  "A", "P", "PRIME", "IF", "ELSE", "ELIF", "IN", "INIT", 
                  "UNTIL", "WITH", "THEN", "NEVER", "MAIN", "AND", "OR", 
                  "NOT", "TRUE", "FALSE", "ANY_CONDITION", "BIND", "PREDICT", 
                  "ASSIGN", "TIMES_EQ", "DIV_EQ", "PLUS_EQ", "MINUS_EQ", 
                  "EQ_TO", "GT_EQ", "LT_EQ", "NOT_EQ", "COL", "COM", "L_BRK", 
                  "R_BRK", "L_CBRK", "R_CBRK", "L_PAR", "R_PAR", "LT", "GT", 
                  "TIMES", "DIVIDE", "PLUS", "MINUS", "QUOTE", "FNAME", 
                  "IDENTIFIER", "DECIMAL", "INTEGER", "DOT", "LETTER", "ANY_CHAR", 
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



