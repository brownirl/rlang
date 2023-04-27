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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2R")
        buf.write("\u023d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\3\2")
        buf.write("\5\2\u00ab\n\2\3\2\3\2\7\2\u00af\n\2\f\2\16\2\u00b2\13")
        buf.write("\2\3\2\5\2\u00b5\n\2\3\2\3\2\7\2\u00b9\n\2\f\2\16\2\u00bc")
        buf.write("\13\2\5\2\u00be\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3")
        buf.write("%\3%\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3")
        buf.write("(\3)\3)\3)\3*\3*\3*\3*\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3")
        buf.write(",\3-\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61")
        buf.write("\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67\38\38\38\39\3")
        buf.write("9\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3")
        buf.write("B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\7I\u01f8")
        buf.write("\nI\fI\16I\u01fb\13I\3J\3J\3J\7J\u0200\nJ\fJ\16J\u0203")
        buf.write("\13J\3J\3J\7J\u0207\nJ\fJ\16J\u020a\13J\3J\3J\3K\6K\u020f")
        buf.write("\nK\rK\16K\u0210\3K\3K\6K\u0215\nK\rK\16K\u0216\3L\6L")
        buf.write("\u021a\nL\rL\16L\u021b\3M\3M\3N\5N\u0221\nN\3O\3O\3O\5")
        buf.write("O\u0226\nO\3P\3P\3Q\6Q\u022b\nQ\rQ\16Q\u022c\3R\3R\7R")
        buf.write("\u0231\nR\fR\16R\u0234\13R\3S\3S\5S\u0238\nS\3S\3S\3T")
        buf.write("\3T\2\2U\3\5\5\6\7\7\t\b\13\t\r\n\17\13\21\f\23\r\25\16")
        buf.write("\27\17\31\20\33\21\35\22\37\23!\24#\25%\26\'\27)\30+\31")
        buf.write("-\32/\33\61\34\63\35\65\36\67\379 ;!=\"?#A$C%E&G\'I(K")
        buf.write(")M*O+Q,S-U.W/Y\60[\61]\62_\63a\64c\65e\66g\67i8k9m:o;")
        buf.write("q<s=u>w?y@{A}B\177C\u0081D\u0083E\u0085F\u0087G\u0089")
        buf.write("H\u008bI\u008dJ\u008fK\u0091L\u0093M\u0095N\u0097O\u0099")
        buf.write("P\u009b\2\u009d\2\u009f\2\u00a1\2\u00a3\2\u00a5Q\u00a7")
        buf.write("R\3\2\6\4\2C\\c|\3\2\62;\4\2\13\13\"\"\4\2\f\f\16\17\2")
        buf.write("\u0247\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
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
        buf.write("\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2")
        buf.write("\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2")
        buf.write("\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2")
        buf.write("\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097")
        buf.write("\3\2\2\2\2\u0099\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2")
        buf.write("\2\3\u00bd\3\2\2\2\5\u00bf\3\2\2\2\7\u00c6\3\2\2\2\t\u00d2")
        buf.write("\3\2\2\2\13\u00dc\3\2\2\2\r\u00e4\3\2\2\2\17\u00eb\3\2")
        buf.write("\2\2\21\u00f0\3\2\2\2\23\u00f6\3\2\2\2\25\u00fd\3\2\2")
        buf.write("\2\27\u0106\3\2\2\2\31\u010d\3\2\2\2\33\u0114\3\2\2\2")
        buf.write("\35\u011b\3\2\2\2\37\u0122\3\2\2\2!\u012a\3\2\2\2#\u0131")
        buf.write("\3\2\2\2%\u013f\3\2\2\2\'\u0143\3\2\2\2)\u0149\3\2\2\2")
        buf.write("+\u014d\3\2\2\2-\u0152\3\2\2\2/\u0156\3\2\2\2\61\u015e")
        buf.write("\3\2\2\2\63\u0161\3\2\2\2\65\u0163\3\2\2\2\67\u0165\3")
        buf.write("\2\2\29\u0167\3\2\2\2;\u0169\3\2\2\2=\u016c\3\2\2\2?\u0171")
        buf.write("\3\2\2\2A\u0176\3\2\2\2C\u0179\3\2\2\2E\u017e\3\2\2\2")
        buf.write("G\u0184\3\2\2\2I\u0189\3\2\2\2K\u018e\3\2\2\2M\u0194\3")
        buf.write("\2\2\2O\u0199\3\2\2\2Q\u019d\3\2\2\2S\u01a0\3\2\2\2U\u01a4")
        buf.write("\3\2\2\2W\u01a9\3\2\2\2Y\u01af\3\2\2\2[\u01b3\3\2\2\2")
        buf.write("]\u01b7\3\2\2\2_\u01ba\3\2\2\2a\u01bd\3\2\2\2c\u01bf\3")
        buf.write("\2\2\2e\u01c2\3\2\2\2g\u01c5\3\2\2\2i\u01c8\3\2\2\2k\u01cb")
        buf.write("\3\2\2\2m\u01ce\3\2\2\2o\u01d1\3\2\2\2q\u01d4\3\2\2\2")
        buf.write("s\u01d7\3\2\2\2u\u01d9\3\2\2\2w\u01db\3\2\2\2y\u01dd\3")
        buf.write("\2\2\2{\u01df\3\2\2\2}\u01e1\3\2\2\2\177\u01e3\3\2\2\2")
        buf.write("\u0081\u01e5\3\2\2\2\u0083\u01e7\3\2\2\2\u0085\u01e9\3")
        buf.write("\2\2\2\u0087\u01eb\3\2\2\2\u0089\u01ed\3\2\2\2\u008b\u01ef")
        buf.write("\3\2\2\2\u008d\u01f1\3\2\2\2\u008f\u01f3\3\2\2\2\u0091")
        buf.write("\u01f5\3\2\2\2\u0093\u01fc\3\2\2\2\u0095\u020e\3\2\2\2")
        buf.write("\u0097\u0219\3\2\2\2\u0099\u021d\3\2\2\2\u009b\u0220\3")
        buf.write("\2\2\2\u009d\u0225\3\2\2\2\u009f\u0227\3\2\2\2\u00a1\u022a")
        buf.write("\3\2\2\2\u00a3\u022e\3\2\2\2\u00a5\u0237\3\2\2\2\u00a7")
        buf.write("\u023b\3\2\2\2\u00a9\u00ab\7\17\2\2\u00aa\u00a9\3\2\2")
        buf.write("\2\u00aa\u00ab\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00b0")
        buf.write("\7\f\2\2\u00ad\u00af\7\"\2\2\u00ae\u00ad\3\2\2\2\u00af")
        buf.write("\u00b2\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2")
        buf.write("\u00b1\u00be\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b3\u00b5\7")
        buf.write("\17\2\2\u00b4\u00b3\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5")
        buf.write("\u00b6\3\2\2\2\u00b6\u00ba\7\f\2\2\u00b7\u00b9\7\13\2")
        buf.write("\2\u00b8\u00b7\3\2\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00b8")
        buf.write("\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00be\3\2\2\2\u00bc")
        buf.write("\u00ba\3\2\2\2\u00bd\u00aa\3\2\2\2\u00bd\u00b4\3\2\2\2")
        buf.write("\u00be\4\3\2\2\2\u00bf\u00c0\7k\2\2\u00c0\u00c1\7o\2\2")
        buf.write("\u00c1\u00c2\7r\2\2\u00c2\u00c3\7q\2\2\u00c3\u00c4\7t")
        buf.write("\2\2\u00c4\u00c5\7v\2\2\u00c5\6\3\2\2\2\u00c6\u00c7\7")
        buf.write("R\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9\7q\2\2\u00c9\u00ca")
        buf.write("\7r\2\2\u00ca\u00cb\7q\2\2\u00cb\u00cc\7u\2\2\u00cc\u00cd")
        buf.write("\7k\2\2\u00cd\u00ce\7v\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0")
        buf.write("\7q\2\2\u00d0\u00d1\7p\2\2\u00d1\b\3\2\2\2\u00d2\u00d3")
        buf.write("\7R\2\2\u00d3\u00d4\7t\2\2\u00d4\u00d5\7g\2\2\u00d5\u00d6")
        buf.write("\7f\2\2\u00d6\u00d7\7k\2\2\u00d7\u00d8\7e\2\2\u00d8\u00d9")
        buf.write("\7c\2\2\u00d9\u00da\7v\2\2\u00da\u00db\7g\2\2\u00db\n")
        buf.write("\3\2\2\2\u00dc\u00dd\7H\2\2\u00dd\u00de\7g\2\2\u00de\u00df")
        buf.write("\7c\2\2\u00df\u00e0\7v\2\2\u00e0\u00e1\7w\2\2\u00e1\u00e2")
        buf.write("\7t\2\2\u00e2\u00e3\7g\2\2\u00e3\f\3\2\2\2\u00e4\u00e5")
        buf.write("\7H\2\2\u00e5\u00e6\7c\2\2\u00e6\u00e7\7e\2\2\u00e7\u00e8")
        buf.write("\7v\2\2\u00e8\u00e9\7q\2\2\u00e9\u00ea\7t\2\2\u00ea\16")
        buf.write("\3\2\2\2\u00eb\u00ec\7I\2\2\u00ec\u00ed\7q\2\2\u00ed\u00ee")
        buf.write("\7c\2\2\u00ee\u00ef\7n\2\2\u00ef\20\3\2\2\2\u00f0\u00f1")
        buf.write("\7E\2\2\u00f1\u00f2\7n\2\2\u00f2\u00f3\7c\2\2\u00f3\u00f4")
        buf.write("\7u\2\2\u00f4\u00f5\7u\2\2\u00f5\22\3\2\2\2\u00f6\u00f7")
        buf.write("\7Q\2\2\u00f7\u00f8\7d\2\2\u00f8\u00f9\7l\2\2\u00f9\u00fa")
        buf.write("\7g\2\2\u00fa\u00fb\7e\2\2\u00fb\u00fc\7v\2\2\u00fc\24")
        buf.write("\3\2\2\2\u00fd\u00fe\7E\2\2\u00fe\u00ff\7q\2\2\u00ff\u0100")
        buf.write("\7p\2\2\u0100\u0101\7u\2\2\u0101\u0102\7v\2\2\u0102\u0103")
        buf.write("\7c\2\2\u0103\u0104\7p\2\2\u0104\u0105\7v\2\2\u0105\26")
        buf.write("\3\2\2\2\u0106\u0107\7C\2\2\u0107\u0108\7e\2\2\u0108\u0109")
        buf.write("\7v\2\2\u0109\u010a\7k\2\2\u010a\u010b\7q\2\2\u010b\u010c")
        buf.write("\7p\2\2\u010c\30\3\2\2\2\u010d\u010e\7G\2\2\u010e\u010f")
        buf.write("\7h\2\2\u010f\u0110\7h\2\2\u0110\u0111\7g\2\2\u0111\u0112")
        buf.write("\7e\2\2\u0112\u0113\7v\2\2\u0113\32\3\2\2\2\u0114\u0115")
        buf.write("\7T\2\2\u0115\u0116\7g\2\2\u0116\u0117\7y\2\2\u0117\u0118")
        buf.write("\7c\2\2\u0118\u0119\7t\2\2\u0119\u011a\7f\2\2\u011a\34")
        buf.write("\3\2\2\2\u011b\u011c\7R\2\2\u011c\u011d\7q\2\2\u011d\u011e")
        buf.write("\7n\2\2\u011e\u011f\7k\2\2\u011f\u0120\7e\2\2\u0120\u0121")
        buf.write("\7{\2\2\u0121\36\3\2\2\2\u0122\u0123\7G\2\2\u0123\u0124")
        buf.write("\7z\2\2\u0124\u0125\7g\2\2\u0125\u0126\7e\2\2\u0126\u0127")
        buf.write("\7w\2\2\u0127\u0128\7v\2\2\u0128\u0129\7g\2\2\u0129 \3")
        buf.write("\2\2\2\u012a\u012b\7Q\2\2\u012b\u012c\7r\2\2\u012c\u012d")
        buf.write("\7v\2\2\u012d\u012e\7k\2\2\u012e\u012f\7q\2\2\u012f\u0130")
        buf.write("\7p\2\2\u0130\"\3\2\2\2\u0131\u0132\7O\2\2\u0132\u0133")
        buf.write("\7c\2\2\u0133\u0134\7t\2\2\u0134\u0135\7m\2\2\u0135\u0136")
        buf.write("\7q\2\2\u0136\u0137\7x\2\2\u0137\u0138\7H\2\2\u0138\u0139")
        buf.write("\7g\2\2\u0139\u013a\7c\2\2\u013a\u013b\7v\2\2\u013b\u013c")
        buf.write("\7w\2\2\u013c\u013d\7t\2\2\u013d\u013e\7g\2\2\u013e$\3")
        buf.write("\2\2\2\u013f\u0140\7k\2\2\u0140\u0141\7p\2\2\u0141\u0142")
        buf.write("\7v\2\2\u0142&\3\2\2\2\u0143\u0144\7h\2\2\u0144\u0145")
        buf.write("\7n\2\2\u0145\u0146\7q\2\2\u0146\u0147\7c\2\2\u0147\u0148")
        buf.write("\7v\2\2\u0148(\3\2\2\2\u0149\u014a\7u\2\2\u014a\u014b")
        buf.write("\7v\2\2\u014b\u014c\7t\2\2\u014c*\3\2\2\2\u014d\u014e")
        buf.write("\7n\2\2\u014e\u014f\7k\2\2\u014f\u0150\7u\2\2\u0150\u0151")
        buf.write("\7v\2\2\u0151,\3\2\2\2\u0152\u0153\7u\2\2\u0153\u0154")
        buf.write("\7g\2\2\u0154\u0155\7v\2\2\u0155.\3\2\2\2\u0156\u0157")
        buf.write("\7d\2\2\u0157\u0158\7q\2\2\u0158\u0159\7q\2\2\u0159\u015a")
        buf.write("\7n\2\2\u015a\u015b\7g\2\2\u015b\u015c\7c\2\2\u015c\u015d")
        buf.write("\7p\2\2\u015d\60\3\2\2\2\u015e\u015f\5\63\32\2\u015f\u0160")
        buf.write("\59\35\2\u0160\62\3\2\2\2\u0161\u0162\7U\2\2\u0162\64")
        buf.write("\3\2\2\2\u0163\u0164\7C\2\2\u0164\66\3\2\2\2\u0165\u0166")
        buf.write("\7R\2\2\u01668\3\2\2\2\u0167\u0168\7)\2\2\u0168:\3\2\2")
        buf.write("\2\u0169\u016a\7k\2\2\u016a\u016b\7h\2\2\u016b<\3\2\2")
        buf.write("\2\u016c\u016d\7g\2\2\u016d\u016e\7n\2\2\u016e\u016f\7")
        buf.write("u\2\2\u016f\u0170\7g\2\2\u0170>\3\2\2\2\u0171\u0172\7")
        buf.write("g\2\2\u0172\u0173\7n\2\2\u0173\u0174\7k\2\2\u0174\u0175")
        buf.write("\7h\2\2\u0175@\3\2\2\2\u0176\u0177\7k\2\2\u0177\u0178")
        buf.write("\7p\2\2\u0178B\3\2\2\2\u0179\u017a\7k\2\2\u017a\u017b")
        buf.write("\7p\2\2\u017b\u017c\7k\2\2\u017c\u017d\7v\2\2\u017dD\3")
        buf.write("\2\2\2\u017e\u017f\7w\2\2\u017f\u0180\7p\2\2\u0180\u0181")
        buf.write("\7v\2\2\u0181\u0182\7k\2\2\u0182\u0183\7n\2\2\u0183F\3")
        buf.write("\2\2\2\u0184\u0185\7y\2\2\u0185\u0186\7k\2\2\u0186\u0187")
        buf.write("\7v\2\2\u0187\u0188\7j\2\2\u0188H\3\2\2\2\u0189\u018a")
        buf.write("\7v\2\2\u018a\u018b\7j\2\2\u018b\u018c\7g\2\2\u018c\u018d")
        buf.write("\7p\2\2\u018dJ\3\2\2\2\u018e\u018f\7p\2\2\u018f\u0190")
        buf.write("\7g\2\2\u0190\u0191\7x\2\2\u0191\u0192\7g\2\2\u0192\u0193")
        buf.write("\7t\2\2\u0193L\3\2\2\2\u0194\u0195\7o\2\2\u0195\u0196")
        buf.write("\7c\2\2\u0196\u0197\7k\2\2\u0197\u0198\7p\2\2\u0198N\3")
        buf.write("\2\2\2\u0199\u019a\7c\2\2\u019a\u019b\7p\2\2\u019b\u019c")
        buf.write("\7f\2\2\u019cP\3\2\2\2\u019d\u019e\7q\2\2\u019e\u019f")
        buf.write("\7t\2\2\u019fR\3\2\2\2\u01a0\u01a1\7p\2\2\u01a1\u01a2")
        buf.write("\7q\2\2\u01a2\u01a3\7v\2\2\u01a3T\3\2\2\2\u01a4\u01a5")
        buf.write("\7V\2\2\u01a5\u01a6\7t\2\2\u01a6\u01a7\7w\2\2\u01a7\u01a8")
        buf.write("\7g\2\2\u01a8V\3\2\2\2\u01a9\u01aa\7H\2\2\u01aa\u01ab")
        buf.write("\7c\2\2\u01ab\u01ac\7n\2\2\u01ac\u01ad\7u\2\2\u01ad\u01ae")
        buf.write("\7g\2\2\u01aeX\3\2\2\2\u01af\u01b0\7C\2\2\u01b0\u01b1")
        buf.write("\7p\2\2\u01b1\u01b2\7{\2\2\u01b2Z\3\2\2\2\u01b3\u01b4")
        buf.write("\7C\2\2\u01b4\u01b5\7n\2\2\u01b5\u01b6\7n\2\2\u01b6\\")
        buf.write("\3\2\2\2\u01b7\u01b8\7<\2\2\u01b8\u01b9\7?\2\2\u01b9^")
        buf.write("\3\2\2\2\u01ba\u01bb\7/\2\2\u01bb\u01bc\7@\2\2\u01bc`")
        buf.write("\3\2\2\2\u01bd\u01be\7?\2\2\u01beb\3\2\2\2\u01bf\u01c0")
        buf.write("\7,\2\2\u01c0\u01c1\7?\2\2\u01c1d\3\2\2\2\u01c2\u01c3")
        buf.write("\7\61\2\2\u01c3\u01c4\7?\2\2\u01c4f\3\2\2\2\u01c5\u01c6")
        buf.write("\7-\2\2\u01c6\u01c7\7?\2\2\u01c7h\3\2\2\2\u01c8\u01c9")
        buf.write("\7/\2\2\u01c9\u01ca\7?\2\2\u01caj\3\2\2\2\u01cb\u01cc")
        buf.write("\7?\2\2\u01cc\u01cd\7?\2\2\u01cdl\3\2\2\2\u01ce\u01cf")
        buf.write("\7@\2\2\u01cf\u01d0\7?\2\2\u01d0n\3\2\2\2\u01d1\u01d2")
        buf.write("\7>\2\2\u01d2\u01d3\7?\2\2\u01d3p\3\2\2\2\u01d4\u01d5")
        buf.write("\7#\2\2\u01d5\u01d6\7?\2\2\u01d6r\3\2\2\2\u01d7\u01d8")
        buf.write("\7<\2\2\u01d8t\3\2\2\2\u01d9\u01da\7.\2\2\u01dav\3\2\2")
        buf.write("\2\u01db\u01dc\7]\2\2\u01dcx\3\2\2\2\u01dd\u01de\7_\2")
        buf.write("\2\u01dez\3\2\2\2\u01df\u01e0\7}\2\2\u01e0|\3\2\2\2\u01e1")
        buf.write("\u01e2\7\177\2\2\u01e2~\3\2\2\2\u01e3\u01e4\7*\2\2\u01e4")
        buf.write("\u0080\3\2\2\2\u01e5\u01e6\7+\2\2\u01e6\u0082\3\2\2\2")
        buf.write("\u01e7\u01e8\7>\2\2\u01e8\u0084\3\2\2\2\u01e9\u01ea\7")
        buf.write("@\2\2\u01ea\u0086\3\2\2\2\u01eb\u01ec\7,\2\2\u01ec\u0088")
        buf.write("\3\2\2\2\u01ed\u01ee\7\61\2\2\u01ee\u008a\3\2\2\2\u01ef")
        buf.write("\u01f0\7-\2\2\u01f0\u008c\3\2\2\2\u01f1\u01f2\7/\2\2\u01f2")
        buf.write("\u008e\3\2\2\2\u01f3\u01f4\7$\2\2\u01f4\u0090\3\2\2\2")
        buf.write("\u01f5\u01f9\5\u009bN\2\u01f6\u01f8\5\u009dO\2\u01f7\u01f6")
        buf.write("\3\2\2\2\u01f8\u01fb\3\2\2\2\u01f9\u01f7\3\2\2\2\u01f9")
        buf.write("\u01fa\3\2\2\2\u01fa\u0092\3\2\2\2\u01fb\u01f9\3\2\2\2")
        buf.write("\u01fc\u01fd\5\u008fH\2\u01fd\u0201\5\u009bN\2\u01fe\u0200")
        buf.write("\5\u009dO\2\u01ff\u01fe\3\2\2\2\u0200\u0203\3\2\2\2\u0201")
        buf.write("\u01ff\3\2\2\2\u0201\u0202\3\2\2\2\u0202\u0204\3\2\2\2")
        buf.write("\u0203\u0201\3\2\2\2\u0204\u0208\5\u0099M\2\u0205\u0207")
        buf.write("\5\u009bN\2\u0206\u0205\3\2\2\2\u0207\u020a\3\2\2\2\u0208")
        buf.write("\u0206\3\2\2\2\u0208\u0209\3\2\2\2\u0209\u020b\3\2\2\2")
        buf.write("\u020a\u0208\3\2\2\2\u020b\u020c\5\u008fH\2\u020c\u0094")
        buf.write("\3\2\2\2\u020d\u020f\5\u009fP\2\u020e\u020d\3\2\2\2\u020f")
        buf.write("\u0210\3\2\2\2\u0210\u020e\3\2\2\2\u0210\u0211\3\2\2\2")
        buf.write("\u0211\u0212\3\2\2\2\u0212\u0214\5\u0099M\2\u0213\u0215")
        buf.write("\5\u009fP\2\u0214\u0213\3\2\2\2\u0215\u0216\3\2\2\2\u0216")
        buf.write("\u0214\3\2\2\2\u0216\u0217\3\2\2\2\u0217\u0096\3\2\2\2")
        buf.write("\u0218\u021a\5\u009fP\2\u0219\u0218\3\2\2\2\u021a\u021b")
        buf.write("\3\2\2\2\u021b\u0219\3\2\2\2\u021b\u021c\3\2\2\2\u021c")
        buf.write("\u0098\3\2\2\2\u021d\u021e\7\60\2\2\u021e\u009a\3\2\2")
        buf.write("\2\u021f\u0221\t\2\2\2\u0220\u021f\3\2\2\2\u0221\u009c")
        buf.write("\3\2\2\2\u0222\u0226\5\u009bN\2\u0223\u0226\5\u009fP\2")
        buf.write("\u0224\u0226\7a\2\2\u0225\u0222\3\2\2\2\u0225\u0223\3")
        buf.write("\2\2\2\u0225\u0224\3\2\2\2\u0226\u009e\3\2\2\2\u0227\u0228")
        buf.write("\t\3\2\2\u0228\u00a0\3\2\2\2\u0229\u022b\t\4\2\2\u022a")
        buf.write("\u0229\3\2\2\2\u022b\u022c\3\2\2\2\u022c\u022a\3\2\2\2")
        buf.write("\u022c\u022d\3\2\2\2\u022d\u00a2\3\2\2\2\u022e\u0232\7")
        buf.write("%\2\2\u022f\u0231\n\5\2\2\u0230\u022f\3\2\2\2\u0231\u0234")
        buf.write("\3\2\2\2\u0232\u0230\3\2\2\2\u0232\u0233\3\2\2\2\u0233")
        buf.write("\u00a4\3\2\2\2\u0234\u0232\3\2\2\2\u0235\u0238\5\u00a1")
        buf.write("Q\2\u0236\u0238\5\u00a3R\2\u0237\u0235\3\2\2\2\u0237\u0236")
        buf.write("\3\2\2\2\u0238\u0239\3\2\2\2\u0239\u023a\bS\2\2\u023a")
        buf.write("\u00a6\3\2\2\2\u023b\u023c\13\2\2\2\u023c\u00a8\3\2\2")
        buf.write("\2\23\2\u00aa\u00b0\u00b4\u00ba\u00bd\u01f9\u0201\u0208")
        buf.write("\u0210\u0216\u021b\u0220\u0225\u022c\u0232\u0237\3\b\2")
        buf.write("\2")
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
    ALL_CONDITION = 47
    BIND = 48
    PREDICT = 49
    ASSIGN = 50
    TIMES_EQ = 51
    DIV_EQ = 52
    PLUS_EQ = 53
    MINUS_EQ = 54
    EQ_TO = 55
    GT_EQ = 56
    LT_EQ = 57
    NOT_EQ = 58
    COL = 59
    COM = 60
    L_BRK = 61
    R_BRK = 62
    L_CBRK = 63
    R_CBRK = 64
    L_PAR = 65
    R_PAR = 66
    LT = 67
    GT = 68
    TIMES = 69
    DIVIDE = 70
    PLUS = 71
    MINUS = 72
    QUOTE = 73
    IDENTIFIER = 74
    FNAME = 75
    DECIMAL = 76
    INTEGER = 77
    DOT = 78
    SKIP_ = 79
    ANY = 80

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'import'", "'Proposition'", "'Predicate'", "'Feature'", "'Factor'", 
            "'Goal'", "'Class'", "'Object'", "'Constant'", "'Action'", "'Effect'", 
            "'Reward'", "'Policy'", "'Execute'", "'Option'", "'MarkovFeature'", 
            "'int'", "'float'", "'str'", "'list'", "'set'", "'boolean'", 
            "'S'", "'A'", "'P'", "'''", "'if'", "'else'", "'elif'", "'in'", 
            "'init'", "'until'", "'with'", "'then'", "'never'", "'main'", 
            "'and'", "'or'", "'not'", "'True'", "'False'", "'Any'", "'All'", 
            "':='", "'->'", "'='", "'*='", "'/='", "'+='", "'-='", "'=='", 
            "'>='", "'<='", "'!='", "':'", "','", "'['", "']'", "'{'", "'}'", 
            "'('", "')'", "'<'", "'>'", "'*'", "'/'", "'+'", "'-'", "'\"'", 
            "'.'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "NL", "IMPORT", "PROPOSITION", "PREDICATE", 
            "FEATURE", "FACTOR", "GOAL", "CLASS", "OBJECT", "CONSTANT", 
            "ACTION", "EFFECT", "REWARD", "POLICY", "EXECUTE", "OPTION", 
            "MARKOVFEATURE", "INT", "FLOAT", "STR", "LIST", "SET", "BOOL", 
            "S_PRIME", "S", "A", "P", "PRIME", "IF", "ELSE", "ELIF", "IN", 
            "INIT", "UNTIL", "WITH", "THEN", "NEVER", "MAIN", "AND", "OR", 
            "NOT", "TRUE", "FALSE", "ANY_CONDITION", "ALL_CONDITION", "BIND", 
            "PREDICT", "ASSIGN", "TIMES_EQ", "DIV_EQ", "PLUS_EQ", "MINUS_EQ", 
            "EQ_TO", "GT_EQ", "LT_EQ", "NOT_EQ", "COL", "COM", "L_BRK", 
            "R_BRK", "L_CBRK", "R_CBRK", "L_PAR", "R_PAR", "LT", "GT", "TIMES", 
            "DIVIDE", "PLUS", "MINUS", "QUOTE", "IDENTIFIER", "FNAME", "DECIMAL", 
            "INTEGER", "DOT", "SKIP_", "ANY" ]

    ruleNames = [ "NL", "IMPORT", "PROPOSITION", "PREDICATE", "FEATURE", 
                  "FACTOR", "GOAL", "CLASS", "OBJECT", "CONSTANT", "ACTION", 
                  "EFFECT", "REWARD", "POLICY", "EXECUTE", "OPTION", "MARKOVFEATURE", 
                  "INT", "FLOAT", "STR", "LIST", "SET", "BOOL", "S_PRIME", 
                  "S", "A", "P", "PRIME", "IF", "ELSE", "ELIF", "IN", "INIT", 
                  "UNTIL", "WITH", "THEN", "NEVER", "MAIN", "AND", "OR", 
                  "NOT", "TRUE", "FALSE", "ANY_CONDITION", "ALL_CONDITION", 
                  "BIND", "PREDICT", "ASSIGN", "TIMES_EQ", "DIV_EQ", "PLUS_EQ", 
                  "MINUS_EQ", "EQ_TO", "GT_EQ", "LT_EQ", "NOT_EQ", "COL", 
                  "COM", "L_BRK", "R_BRK", "L_CBRK", "R_CBRK", "L_PAR", 
                  "R_PAR", "LT", "GT", "TIMES", "DIVIDE", "PLUS", "MINUS", 
                  "QUOTE", "IDENTIFIER", "FNAME", "DECIMAL", "INTEGER", 
                  "DOT", "LETTER", "ANY_CHAR", "DIGIT", "SPACES", "COMMENT", 
                  "SKIP_", "ANY" ]

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



