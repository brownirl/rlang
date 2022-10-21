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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2Q")
        buf.write("\u022e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\3\2\5\2\u00a9")
        buf.write("\n\2\3\2\3\2\7\2\u00ad\n\2\f\2\16\2\u00b0\13\2\3\2\5\2")
        buf.write("\u00b3\n\2\3\2\3\2\7\2\u00b7\n\2\f\2\16\2\u00ba\13\2\5")
        buf.write("\2\u00bc\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3&\3")
        buf.write("&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3)\3)\3")
        buf.write(")\3*\3*\3*\3*\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3-\3-\3")
        buf.write("-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3\61\3\62\3")
        buf.write("\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\67\3\67\3\67\38\38\38\39\39\3:\3:\3")
        buf.write(";\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3")
        buf.write("D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3H\7H\u01f3\nH\fH\16H\u01f6")
        buf.write("\13H\3I\3I\7I\u01fa\nI\fI\16I\u01fd\13I\3J\6J\u0200\n")
        buf.write("J\rJ\16J\u0201\3J\3J\6J\u0206\nJ\rJ\16J\u0207\3K\6K\u020b")
        buf.write("\nK\rK\16K\u020c\3L\3L\3M\5M\u0212\nM\3N\3N\3N\5N\u0217")
        buf.write("\nN\3O\3O\3P\6P\u021c\nP\rP\16P\u021d\3Q\3Q\7Q\u0222\n")
        buf.write("Q\fQ\16Q\u0225\13Q\3R\3R\5R\u0229\nR\3R\3R\3S\3S\2\2T")
        buf.write("\3\5\5\6\7\7\t\b\13\t\r\n\17\13\21\f\23\r\25\16\27\17")
        buf.write("\31\20\33\21\35\22\37\23!\24#\25%\26\'\27)\30+\31-\32")
        buf.write("/\33\61\34\63\35\65\36\67\379 ;!=\"?#A$C%E&G\'I(K)M*O")
        buf.write("+Q,S-U.W/Y\60[\61]\62_\63a\64c\65e\66g\67i8k9m:o;q<s=")
        buf.write("u>w?y@{A}B\177C\u0081D\u0083E\u0085F\u0087G\u0089H\u008b")
        buf.write("I\u008dJ\u008fK\u0091L\u0093M\u0095N\u0097O\u0099\2\u009b")
        buf.write("\2\u009d\2\u009f\2\u00a1\2\u00a3P\u00a5Q\3\2\6\4\2C\\")
        buf.write("c|\3\2\62;\4\2\13\13\"\"\4\2\f\f\16\17\2\u0237\2\3\3\2")
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
        buf.write("\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3")
        buf.write("\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2")
        buf.write("\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\3\u00bb\3\2\2\2\5\u00bd")
        buf.write("\3\2\2\2\7\u00c4\3\2\2\2\t\u00d0\3\2\2\2\13\u00da\3\2")
        buf.write("\2\2\r\u00e2\3\2\2\2\17\u00e9\3\2\2\2\21\u00ee\3\2\2\2")
        buf.write("\23\u00f4\3\2\2\2\25\u00fb\3\2\2\2\27\u0104\3\2\2\2\31")
        buf.write("\u010b\3\2\2\2\33\u0112\3\2\2\2\35\u0119\3\2\2\2\37\u0120")
        buf.write("\3\2\2\2!\u0128\3\2\2\2#\u012f\3\2\2\2%\u013d\3\2\2\2")
        buf.write("\'\u0141\3\2\2\2)\u0147\3\2\2\2+\u014b\3\2\2\2-\u0150")
        buf.write("\3\2\2\2/\u0154\3\2\2\2\61\u015c\3\2\2\2\63\u015f\3\2")
        buf.write("\2\2\65\u0161\3\2\2\2\67\u0163\3\2\2\29\u0165\3\2\2\2")
        buf.write(";\u0167\3\2\2\2=\u016a\3\2\2\2?\u016f\3\2\2\2A\u0174\3")
        buf.write("\2\2\2C\u0177\3\2\2\2E\u017c\3\2\2\2G\u0182\3\2\2\2I\u0187")
        buf.write("\3\2\2\2K\u018c\3\2\2\2M\u0192\3\2\2\2O\u0197\3\2\2\2")
        buf.write("Q\u019b\3\2\2\2S\u019e\3\2\2\2U\u01a2\3\2\2\2W\u01a7\3")
        buf.write("\2\2\2Y\u01ad\3\2\2\2[\u01b1\3\2\2\2]\u01b4\3\2\2\2_\u01b7")
        buf.write("\3\2\2\2a\u01b9\3\2\2\2c\u01bc\3\2\2\2e\u01bf\3\2\2\2")
        buf.write("g\u01c2\3\2\2\2i\u01c5\3\2\2\2k\u01c8\3\2\2\2m\u01cb\3")
        buf.write("\2\2\2o\u01ce\3\2\2\2q\u01d1\3\2\2\2s\u01d3\3\2\2\2u\u01d5")
        buf.write("\3\2\2\2w\u01d7\3\2\2\2y\u01d9\3\2\2\2{\u01db\3\2\2\2")
        buf.write("}\u01dd\3\2\2\2\177\u01df\3\2\2\2\u0081\u01e1\3\2\2\2")
        buf.write("\u0083\u01e3\3\2\2\2\u0085\u01e5\3\2\2\2\u0087\u01e7\3")
        buf.write("\2\2\2\u0089\u01e9\3\2\2\2\u008b\u01eb\3\2\2\2\u008d\u01ed")
        buf.write("\3\2\2\2\u008f\u01ef\3\2\2\2\u0091\u01f7\3\2\2\2\u0093")
        buf.write("\u01ff\3\2\2\2\u0095\u020a\3\2\2\2\u0097\u020e\3\2\2\2")
        buf.write("\u0099\u0211\3\2\2\2\u009b\u0216\3\2\2\2\u009d\u0218\3")
        buf.write("\2\2\2\u009f\u021b\3\2\2\2\u00a1\u021f\3\2\2\2\u00a3\u0228")
        buf.write("\3\2\2\2\u00a5\u022c\3\2\2\2\u00a7\u00a9\7\17\2\2\u00a8")
        buf.write("\u00a7\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00aa\3\2\2\2")
        buf.write("\u00aa\u00ae\7\f\2\2\u00ab\u00ad\7\"\2\2\u00ac\u00ab\3")
        buf.write("\2\2\2\u00ad\u00b0\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00af")
        buf.write("\3\2\2\2\u00af\u00bc\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b1")
        buf.write("\u00b3\7\17\2\2\u00b2\u00b1\3\2\2\2\u00b2\u00b3\3\2\2")
        buf.write("\2\u00b3\u00b4\3\2\2\2\u00b4\u00b8\7\f\2\2\u00b5\u00b7")
        buf.write("\7\13\2\2\u00b6\u00b5\3\2\2\2\u00b7\u00ba\3\2\2\2\u00b8")
        buf.write("\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00bc\3\2\2\2")
        buf.write("\u00ba\u00b8\3\2\2\2\u00bb\u00a8\3\2\2\2\u00bb\u00b2\3")
        buf.write("\2\2\2\u00bc\4\3\2\2\2\u00bd\u00be\7k\2\2\u00be\u00bf")
        buf.write("\7o\2\2\u00bf\u00c0\7r\2\2\u00c0\u00c1\7q\2\2\u00c1\u00c2")
        buf.write("\7t\2\2\u00c2\u00c3\7v\2\2\u00c3\6\3\2\2\2\u00c4\u00c5")
        buf.write("\7R\2\2\u00c5\u00c6\7t\2\2\u00c6\u00c7\7q\2\2\u00c7\u00c8")
        buf.write("\7r\2\2\u00c8\u00c9\7q\2\2\u00c9\u00ca\7u\2\2\u00ca\u00cb")
        buf.write("\7k\2\2\u00cb\u00cc\7v\2\2\u00cc\u00cd\7k\2\2\u00cd\u00ce")
        buf.write("\7q\2\2\u00ce\u00cf\7p\2\2\u00cf\b\3\2\2\2\u00d0\u00d1")
        buf.write("\7R\2\2\u00d1\u00d2\7t\2\2\u00d2\u00d3\7g\2\2\u00d3\u00d4")
        buf.write("\7f\2\2\u00d4\u00d5\7k\2\2\u00d5\u00d6\7e\2\2\u00d6\u00d7")
        buf.write("\7c\2\2\u00d7\u00d8\7v\2\2\u00d8\u00d9\7g\2\2\u00d9\n")
        buf.write("\3\2\2\2\u00da\u00db\7H\2\2\u00db\u00dc\7g\2\2\u00dc\u00dd")
        buf.write("\7c\2\2\u00dd\u00de\7v\2\2\u00de\u00df\7w\2\2\u00df\u00e0")
        buf.write("\7t\2\2\u00e0\u00e1\7g\2\2\u00e1\f\3\2\2\2\u00e2\u00e3")
        buf.write("\7H\2\2\u00e3\u00e4\7c\2\2\u00e4\u00e5\7e\2\2\u00e5\u00e6")
        buf.write("\7v\2\2\u00e6\u00e7\7q\2\2\u00e7\u00e8\7t\2\2\u00e8\16")
        buf.write("\3\2\2\2\u00e9\u00ea\7I\2\2\u00ea\u00eb\7q\2\2\u00eb\u00ec")
        buf.write("\7c\2\2\u00ec\u00ed\7n\2\2\u00ed\20\3\2\2\2\u00ee\u00ef")
        buf.write("\7E\2\2\u00ef\u00f0\7n\2\2\u00f0\u00f1\7c\2\2\u00f1\u00f2")
        buf.write("\7u\2\2\u00f2\u00f3\7u\2\2\u00f3\22\3\2\2\2\u00f4\u00f5")
        buf.write("\7Q\2\2\u00f5\u00f6\7d\2\2\u00f6\u00f7\7l\2\2\u00f7\u00f8")
        buf.write("\7g\2\2\u00f8\u00f9\7e\2\2\u00f9\u00fa\7v\2\2\u00fa\24")
        buf.write("\3\2\2\2\u00fb\u00fc\7E\2\2\u00fc\u00fd\7q\2\2\u00fd\u00fe")
        buf.write("\7p\2\2\u00fe\u00ff\7u\2\2\u00ff\u0100\7v\2\2\u0100\u0101")
        buf.write("\7c\2\2\u0101\u0102\7p\2\2\u0102\u0103\7v\2\2\u0103\26")
        buf.write("\3\2\2\2\u0104\u0105\7C\2\2\u0105\u0106\7e\2\2\u0106\u0107")
        buf.write("\7v\2\2\u0107\u0108\7k\2\2\u0108\u0109\7q\2\2\u0109\u010a")
        buf.write("\7p\2\2\u010a\30\3\2\2\2\u010b\u010c\7G\2\2\u010c\u010d")
        buf.write("\7h\2\2\u010d\u010e\7h\2\2\u010e\u010f\7g\2\2\u010f\u0110")
        buf.write("\7e\2\2\u0110\u0111\7v\2\2\u0111\32\3\2\2\2\u0112\u0113")
        buf.write("\7T\2\2\u0113\u0114\7g\2\2\u0114\u0115\7y\2\2\u0115\u0116")
        buf.write("\7c\2\2\u0116\u0117\7t\2\2\u0117\u0118\7f\2\2\u0118\34")
        buf.write("\3\2\2\2\u0119\u011a\7R\2\2\u011a\u011b\7q\2\2\u011b\u011c")
        buf.write("\7n\2\2\u011c\u011d\7k\2\2\u011d\u011e\7e\2\2\u011e\u011f")
        buf.write("\7{\2\2\u011f\36\3\2\2\2\u0120\u0121\7G\2\2\u0121\u0122")
        buf.write("\7z\2\2\u0122\u0123\7g\2\2\u0123\u0124\7e\2\2\u0124\u0125")
        buf.write("\7w\2\2\u0125\u0126\7v\2\2\u0126\u0127\7g\2\2\u0127 \3")
        buf.write("\2\2\2\u0128\u0129\7Q\2\2\u0129\u012a\7r\2\2\u012a\u012b")
        buf.write("\7v\2\2\u012b\u012c\7k\2\2\u012c\u012d\7q\2\2\u012d\u012e")
        buf.write("\7p\2\2\u012e\"\3\2\2\2\u012f\u0130\7O\2\2\u0130\u0131")
        buf.write("\7c\2\2\u0131\u0132\7t\2\2\u0132\u0133\7m\2\2\u0133\u0134")
        buf.write("\7q\2\2\u0134\u0135\7x\2\2\u0135\u0136\7H\2\2\u0136\u0137")
        buf.write("\7g\2\2\u0137\u0138\7c\2\2\u0138\u0139\7v\2\2\u0139\u013a")
        buf.write("\7w\2\2\u013a\u013b\7t\2\2\u013b\u013c\7g\2\2\u013c$\3")
        buf.write("\2\2\2\u013d\u013e\7k\2\2\u013e\u013f\7p\2\2\u013f\u0140")
        buf.write("\7v\2\2\u0140&\3\2\2\2\u0141\u0142\7h\2\2\u0142\u0143")
        buf.write("\7n\2\2\u0143\u0144\7q\2\2\u0144\u0145\7c\2\2\u0145\u0146")
        buf.write("\7v\2\2\u0146(\3\2\2\2\u0147\u0148\7u\2\2\u0148\u0149")
        buf.write("\7v\2\2\u0149\u014a\7t\2\2\u014a*\3\2\2\2\u014b\u014c")
        buf.write("\7n\2\2\u014c\u014d\7k\2\2\u014d\u014e\7u\2\2\u014e\u014f")
        buf.write("\7v\2\2\u014f,\3\2\2\2\u0150\u0151\7u\2\2\u0151\u0152")
        buf.write("\7g\2\2\u0152\u0153\7v\2\2\u0153.\3\2\2\2\u0154\u0155")
        buf.write("\7d\2\2\u0155\u0156\7q\2\2\u0156\u0157\7q\2\2\u0157\u0158")
        buf.write("\7n\2\2\u0158\u0159\7g\2\2\u0159\u015a\7c\2\2\u015a\u015b")
        buf.write("\7p\2\2\u015b\60\3\2\2\2\u015c\u015d\5\63\32\2\u015d\u015e")
        buf.write("\59\35\2\u015e\62\3\2\2\2\u015f\u0160\7U\2\2\u0160\64")
        buf.write("\3\2\2\2\u0161\u0162\7C\2\2\u0162\66\3\2\2\2\u0163\u0164")
        buf.write("\7R\2\2\u01648\3\2\2\2\u0165\u0166\7)\2\2\u0166:\3\2\2")
        buf.write("\2\u0167\u0168\7k\2\2\u0168\u0169\7h\2\2\u0169<\3\2\2")
        buf.write("\2\u016a\u016b\7g\2\2\u016b\u016c\7n\2\2\u016c\u016d\7")
        buf.write("u\2\2\u016d\u016e\7g\2\2\u016e>\3\2\2\2\u016f\u0170\7")
        buf.write("g\2\2\u0170\u0171\7n\2\2\u0171\u0172\7k\2\2\u0172\u0173")
        buf.write("\7h\2\2\u0173@\3\2\2\2\u0174\u0175\7k\2\2\u0175\u0176")
        buf.write("\7p\2\2\u0176B\3\2\2\2\u0177\u0178\7k\2\2\u0178\u0179")
        buf.write("\7p\2\2\u0179\u017a\7k\2\2\u017a\u017b\7v\2\2\u017bD\3")
        buf.write("\2\2\2\u017c\u017d\7w\2\2\u017d\u017e\7p\2\2\u017e\u017f")
        buf.write("\7v\2\2\u017f\u0180\7k\2\2\u0180\u0181\7n\2\2\u0181F\3")
        buf.write("\2\2\2\u0182\u0183\7y\2\2\u0183\u0184\7k\2\2\u0184\u0185")
        buf.write("\7v\2\2\u0185\u0186\7j\2\2\u0186H\3\2\2\2\u0187\u0188")
        buf.write("\7v\2\2\u0188\u0189\7j\2\2\u0189\u018a\7g\2\2\u018a\u018b")
        buf.write("\7p\2\2\u018bJ\3\2\2\2\u018c\u018d\7p\2\2\u018d\u018e")
        buf.write("\7g\2\2\u018e\u018f\7x\2\2\u018f\u0190\7g\2\2\u0190\u0191")
        buf.write("\7t\2\2\u0191L\3\2\2\2\u0192\u0193\7o\2\2\u0193\u0194")
        buf.write("\7c\2\2\u0194\u0195\7k\2\2\u0195\u0196\7p\2\2\u0196N\3")
        buf.write("\2\2\2\u0197\u0198\7c\2\2\u0198\u0199\7p\2\2\u0199\u019a")
        buf.write("\7f\2\2\u019aP\3\2\2\2\u019b\u019c\7q\2\2\u019c\u019d")
        buf.write("\7t\2\2\u019dR\3\2\2\2\u019e\u019f\7p\2\2\u019f\u01a0")
        buf.write("\7q\2\2\u01a0\u01a1\7v\2\2\u01a1T\3\2\2\2\u01a2\u01a3")
        buf.write("\7V\2\2\u01a3\u01a4\7t\2\2\u01a4\u01a5\7w\2\2\u01a5\u01a6")
        buf.write("\7g\2\2\u01a6V\3\2\2\2\u01a7\u01a8\7H\2\2\u01a8\u01a9")
        buf.write("\7c\2\2\u01a9\u01aa\7n\2\2\u01aa\u01ab\7u\2\2\u01ab\u01ac")
        buf.write("\7g\2\2\u01acX\3\2\2\2\u01ad\u01ae\7C\2\2\u01ae\u01af")
        buf.write("\7p\2\2\u01af\u01b0\7{\2\2\u01b0Z\3\2\2\2\u01b1\u01b2")
        buf.write("\7<\2\2\u01b2\u01b3\7?\2\2\u01b3\\\3\2\2\2\u01b4\u01b5")
        buf.write("\7/\2\2\u01b5\u01b6\7@\2\2\u01b6^\3\2\2\2\u01b7\u01b8")
        buf.write("\7?\2\2\u01b8`\3\2\2\2\u01b9\u01ba\7,\2\2\u01ba\u01bb")
        buf.write("\7?\2\2\u01bbb\3\2\2\2\u01bc\u01bd\7\61\2\2\u01bd\u01be")
        buf.write("\7?\2\2\u01bed\3\2\2\2\u01bf\u01c0\7-\2\2\u01c0\u01c1")
        buf.write("\7?\2\2\u01c1f\3\2\2\2\u01c2\u01c3\7/\2\2\u01c3\u01c4")
        buf.write("\7?\2\2\u01c4h\3\2\2\2\u01c5\u01c6\7?\2\2\u01c6\u01c7")
        buf.write("\7?\2\2\u01c7j\3\2\2\2\u01c8\u01c9\7@\2\2\u01c9\u01ca")
        buf.write("\7?\2\2\u01cal\3\2\2\2\u01cb\u01cc\7>\2\2\u01cc\u01cd")
        buf.write("\7?\2\2\u01cdn\3\2\2\2\u01ce\u01cf\7#\2\2\u01cf\u01d0")
        buf.write("\7?\2\2\u01d0p\3\2\2\2\u01d1\u01d2\7<\2\2\u01d2r\3\2\2")
        buf.write("\2\u01d3\u01d4\7.\2\2\u01d4t\3\2\2\2\u01d5\u01d6\7]\2")
        buf.write("\2\u01d6v\3\2\2\2\u01d7\u01d8\7_\2\2\u01d8x\3\2\2\2\u01d9")
        buf.write("\u01da\7}\2\2\u01daz\3\2\2\2\u01db\u01dc\7\177\2\2\u01dc")
        buf.write("|\3\2\2\2\u01dd\u01de\7*\2\2\u01de~\3\2\2\2\u01df\u01e0")
        buf.write("\7+\2\2\u01e0\u0080\3\2\2\2\u01e1\u01e2\7>\2\2\u01e2\u0082")
        buf.write("\3\2\2\2\u01e3\u01e4\7@\2\2\u01e4\u0084\3\2\2\2\u01e5")
        buf.write("\u01e6\7,\2\2\u01e6\u0086\3\2\2\2\u01e7\u01e8\7\61\2\2")
        buf.write("\u01e8\u0088\3\2\2\2\u01e9\u01ea\7-\2\2\u01ea\u008a\3")
        buf.write("\2\2\2\u01eb\u01ec\7/\2\2\u01ec\u008c\3\2\2\2\u01ed\u01ee")
        buf.write("\7$\2\2\u01ee\u008e\3\2\2\2\u01ef\u01f0\5\u0091I\2\u01f0")
        buf.write("\u01f4\5\u0097L\2\u01f1\u01f3\5\u0099M\2\u01f2\u01f1\3")
        buf.write("\2\2\2\u01f3\u01f6\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f4\u01f5")
        buf.write("\3\2\2\2\u01f5\u0090\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f7")
        buf.write("\u01fb\5\u0099M\2\u01f8\u01fa\5\u009bN\2\u01f9\u01f8\3")
        buf.write("\2\2\2\u01fa\u01fd\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fb\u01fc")
        buf.write("\3\2\2\2\u01fc\u0092\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fe")
        buf.write("\u0200\5\u009dO\2\u01ff\u01fe\3\2\2\2\u0200\u0201\3\2")
        buf.write("\2\2\u0201\u01ff\3\2\2\2\u0201\u0202\3\2\2\2\u0202\u0203")
        buf.write("\3\2\2\2\u0203\u0205\5\u0097L\2\u0204\u0206\5\u009dO\2")
        buf.write("\u0205\u0204\3\2\2\2\u0206\u0207\3\2\2\2\u0207\u0205\3")
        buf.write("\2\2\2\u0207\u0208\3\2\2\2\u0208\u0094\3\2\2\2\u0209\u020b")
        buf.write("\5\u009dO\2\u020a\u0209\3\2\2\2\u020b\u020c\3\2\2\2\u020c")
        buf.write("\u020a\3\2\2\2\u020c\u020d\3\2\2\2\u020d\u0096\3\2\2\2")
        buf.write("\u020e\u020f\7\60\2\2\u020f\u0098\3\2\2\2\u0210\u0212")
        buf.write("\t\2\2\2\u0211\u0210\3\2\2\2\u0212\u009a\3\2\2\2\u0213")
        buf.write("\u0217\5\u0099M\2\u0214\u0217\5\u009dO\2\u0215\u0217\7")
        buf.write("a\2\2\u0216\u0213\3\2\2\2\u0216\u0214\3\2\2\2\u0216\u0215")
        buf.write("\3\2\2\2\u0217\u009c\3\2\2\2\u0218\u0219\t\3\2\2\u0219")
        buf.write("\u009e\3\2\2\2\u021a\u021c\t\4\2\2\u021b\u021a\3\2\2\2")
        buf.write("\u021c\u021d\3\2\2\2\u021d\u021b\3\2\2\2\u021d\u021e\3")
        buf.write("\2\2\2\u021e\u00a0\3\2\2\2\u021f\u0223\7%\2\2\u0220\u0222")
        buf.write("\n\5\2\2\u0221\u0220\3\2\2\2\u0222\u0225\3\2\2\2\u0223")
        buf.write("\u0221\3\2\2\2\u0223\u0224\3\2\2\2\u0224\u00a2\3\2\2\2")
        buf.write("\u0225\u0223\3\2\2\2\u0226\u0229\5\u009fP\2\u0227\u0229")
        buf.write("\5\u00a1Q\2\u0228\u0226\3\2\2\2\u0228\u0227\3\2\2\2\u0229")
        buf.write("\u022a\3\2\2\2\u022a\u022b\bR\2\2\u022b\u00a4\3\2\2\2")
        buf.write("\u022c\u022d\13\2\2\2\u022d\u00a6\3\2\2\2\22\2\u00a8\u00ae")
        buf.write("\u00b2\u00b8\u00bb\u01f4\u01fb\u0201\u0207\u020c\u0211")
        buf.write("\u0216\u021d\u0223\u0228\3\b\2\2")
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
    BOOL = 25
    S_PRIME = 26
    S = 27
    A = 28
    P = 29
    PRIME = 30
    IF = 31
    ELSE = 32
    ELIF = 33
    IN = 34
    INIT = 35
    UNTIL = 36
    WITH = 37
    THEN = 38
    NEVER = 39
    MAIN = 40
    AND = 41
    OR = 42
    NOT = 43
    TRUE = 44
    FALSE = 45
    ANY_CONDITION = 46
    BIND = 47
    PREDICT = 48
    ASSIGN = 49
    TIMES_EQ = 50
    DIV_EQ = 51
    PLUS_EQ = 52
    MINUS_EQ = 53
    EQ_TO = 54
    GT_EQ = 55
    LT_EQ = 56
    NOT_EQ = 57
    COL = 58
    COM = 59
    L_BRK = 60
    R_BRK = 61
    L_CBRK = 62
    R_CBRK = 63
    L_PAR = 64
    R_PAR = 65
    LT = 66
    GT = 67
    TIMES = 68
    DIVIDE = 69
    PLUS = 70
    MINUS = 71
    QUOTE = 72
    FNAME = 73
    IDENTIFIER = 74
    DECIMAL = 75
    INTEGER = 76
    DOT = 77
    SKIP_ = 78
    ANY = 79

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'import'", "'Proposition'", "'Predicate'", "'Feature'", "'Factor'", 
            "'Goal'", "'Class'", "'Object'", "'Constant'", "'Action'", "'Effect'", 
            "'Reward'", "'Policy'", "'Execute'", "'Option'", "'MarkovFeature'", 
            "'int'", "'float'", "'str'", "'list'", "'set'", "'boolean'", 
            "'S'", "'A'", "'P'", "'''", "'if'", "'else'", "'elif'", "'in'", 
            "'init'", "'until'", "'with'", "'then'", "'never'", "'main'", 
            "'and'", "'or'", "'not'", "'True'", "'False'", "'Any'", "':='", 
            "'->'", "'='", "'*='", "'/='", "'+='", "'-='", "'=='", "'>='", 
            "'<='", "'!='", "':'", "','", "'['", "']'", "'{'", "'}'", "'('", 
            "')'", "'<'", "'>'", "'*'", "'/'", "'+'", "'-'", "'\"'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "NL", "IMPORT", "PROPOSITION", "PREDICATE", 
            "FEATURE", "FACTOR", "GOAL", "CLASS", "OBJECT", "CONSTANT", 
            "ACTION", "EFFECT", "REWARD", "POLICY", "EXECUTE", "OPTION", 
            "MARKOVFEATURE", "INT", "FLOAT", "STR", "LIST", "SET", "BOOL", 
            "S_PRIME", "S", "A", "P", "PRIME", "IF", "ELSE", "ELIF", "IN", 
            "INIT", "UNTIL", "WITH", "THEN", "NEVER", "MAIN", "AND", "OR", 
            "NOT", "TRUE", "FALSE", "ANY_CONDITION", "BIND", "PREDICT", 
            "ASSIGN", "TIMES_EQ", "DIV_EQ", "PLUS_EQ", "MINUS_EQ", "EQ_TO", 
            "GT_EQ", "LT_EQ", "NOT_EQ", "COL", "COM", "L_BRK", "R_BRK", 
            "L_CBRK", "R_CBRK", "L_PAR", "R_PAR", "LT", "GT", "TIMES", "DIVIDE", 
            "PLUS", "MINUS", "QUOTE", "FNAME", "IDENTIFIER", "DECIMAL", 
            "INTEGER", "DOT", "SKIP_", "ANY" ]

    ruleNames = [ "NL", "IMPORT", "PROPOSITION", "PREDICATE", "FEATURE", 
                  "FACTOR", "GOAL", "CLASS", "OBJECT", "CONSTANT", "ACTION", 
                  "EFFECT", "REWARD", "POLICY", "EXECUTE", "OPTION", "MARKOVFEATURE", 
                  "INT", "FLOAT", "STR", "LIST", "SET", "BOOL", "S_PRIME", 
                  "S", "A", "P", "PRIME", "IF", "ELSE", "ELIF", "IN", "INIT", 
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



