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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2T")
        buf.write("\u024a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\3\2\5\2\u00af\n\2\3\2\3\2\7\2\u00b3\n\2\f\2\16")
        buf.write("\2\u00b6\13\2\3\2\5\2\u00b9\n\2\3\2\3\2\7\2\u00bd\n\2")
        buf.write("\f\2\16\2\u00c0\13\2\5\2\u00c2\n\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!")
        buf.write("\3!\3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3")
        buf.write("$\3$\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3(\3(\3(\3(\3(\3)\3)\3)\3)\3*\3*\3*\3+\3+\3+\3+\3")
        buf.write(",\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/\3")
        buf.write("/\3\60\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3")
        buf.write("\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\38\38\38\39\39\39\3:\3:\3:\3;\3;\3;\3")
        buf.write("<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3")
        buf.write("E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3K\3K\7K\u0205\nK\f")
        buf.write("K\16K\u0208\13K\3L\3L\3L\7L\u020d\nL\fL\16L\u0210\13L")
        buf.write("\3L\3L\7L\u0214\nL\fL\16L\u0217\13L\3L\3L\3M\6M\u021c")
        buf.write("\nM\rM\16M\u021d\3M\3M\6M\u0222\nM\rM\16M\u0223\3N\6N")
        buf.write("\u0227\nN\rN\16N\u0228\3O\3O\3P\5P\u022e\nP\3Q\3Q\3Q\5")
        buf.write("Q\u0233\nQ\3R\3R\3S\6S\u0238\nS\rS\16S\u0239\3T\3T\7T")
        buf.write("\u023e\nT\fT\16T\u0241\13T\3U\3U\5U\u0245\nU\3U\3U\3V")
        buf.write("\3V\2\2W\3\5\5\6\7\7\t\b\13\t\r\n\17\13\21\f\23\r\25\16")
        buf.write("\27\17\31\20\33\21\35\22\37\23!\24#\25%\26\'\27)\30+\31")
        buf.write("-\32/\33\61\34\63\35\65\36\67\379 ;!=\"?#A$C%E&G\'I(K")
        buf.write(")M*O+Q,S-U.W/Y\60[\61]\62_\63a\64c\65e\66g\67i8k9m:o;")
        buf.write("q<s=u>w?y@{A}B\177C\u0081D\u0083E\u0085F\u0087G\u0089")
        buf.write("H\u008bI\u008dJ\u008fK\u0091L\u0093M\u0095N\u0097O\u0099")
        buf.write("P\u009bQ\u009dR\u009f\2\u00a1\2\u00a3\2\u00a5\2\u00a7")
        buf.write("\2\u00a9S\u00abT\3\2\6\4\2C\\c|\3\2\62;\4\2\13\13\"\"")
        buf.write("\4\2\f\f\16\17\2\u0254\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2")
        buf.write("\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2")
        buf.write("\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b")
        buf.write("\3\2\2\2\2\u009d\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2")
        buf.write("\2\3\u00c1\3\2\2\2\5\u00c3\3\2\2\2\7\u00ca\3\2\2\2\t\u00d6")
        buf.write("\3\2\2\2\13\u00e0\3\2\2\2\r\u00e8\3\2\2\2\17\u00ef\3\2")
        buf.write("\2\2\21\u00f4\3\2\2\2\23\u00fa\3\2\2\2\25\u0101\3\2\2")
        buf.write("\2\27\u010a\3\2\2\2\31\u0111\3\2\2\2\33\u0118\3\2\2\2")
        buf.write("\35\u011f\3\2\2\2\37\u0126\3\2\2\2!\u012b\3\2\2\2#\u0133")
        buf.write("\3\2\2\2%\u013a\3\2\2\2\'\u0148\3\2\2\2)\u014c\3\2\2\2")
        buf.write("+\u0152\3\2\2\2-\u0156\3\2\2\2/\u015b\3\2\2\2\61\u015f")
        buf.write("\3\2\2\2\63\u0167\3\2\2\2\65\u016a\3\2\2\2\67\u016c\3")
        buf.write("\2\2\29\u016e\3\2\2\2;\u0170\3\2\2\2=\u0172\3\2\2\2?\u0175")
        buf.write("\3\2\2\2A\u017a\3\2\2\2C\u017f\3\2\2\2E\u0182\3\2\2\2")
        buf.write("G\u0187\3\2\2\2I\u018d\3\2\2\2K\u0192\3\2\2\2M\u0197\3")
        buf.write("\2\2\2O\u019d\3\2\2\2Q\u01a2\3\2\2\2S\u01a6\3\2\2\2U\u01a9")
        buf.write("\3\2\2\2W\u01ad\3\2\2\2Y\u01b2\3\2\2\2[\u01b8\3\2\2\2")
        buf.write("]\u01bc\3\2\2\2_\u01c0\3\2\2\2a\u01c3\3\2\2\2c\u01c6\3")
        buf.write("\2\2\2e\u01ca\3\2\2\2g\u01cc\3\2\2\2i\u01cf\3\2\2\2k\u01d2")
        buf.write("\3\2\2\2m\u01d5\3\2\2\2o\u01d8\3\2\2\2q\u01db\3\2\2\2")
        buf.write("s\u01de\3\2\2\2u\u01e1\3\2\2\2w\u01e4\3\2\2\2y\u01e6\3")
        buf.write("\2\2\2{\u01e8\3\2\2\2}\u01ea\3\2\2\2\177\u01ec\3\2\2\2")
        buf.write("\u0081\u01ee\3\2\2\2\u0083\u01f0\3\2\2\2\u0085\u01f2\3")
        buf.write("\2\2\2\u0087\u01f4\3\2\2\2\u0089\u01f6\3\2\2\2\u008b\u01f8")
        buf.write("\3\2\2\2\u008d\u01fa\3\2\2\2\u008f\u01fc\3\2\2\2\u0091")
        buf.write("\u01fe\3\2\2\2\u0093\u0200\3\2\2\2\u0095\u0202\3\2\2\2")
        buf.write("\u0097\u0209\3\2\2\2\u0099\u021b\3\2\2\2\u009b\u0226\3")
        buf.write("\2\2\2\u009d\u022a\3\2\2\2\u009f\u022d\3\2\2\2\u00a1\u0232")
        buf.write("\3\2\2\2\u00a3\u0234\3\2\2\2\u00a5\u0237\3\2\2\2\u00a7")
        buf.write("\u023b\3\2\2\2\u00a9\u0244\3\2\2\2\u00ab\u0248\3\2\2\2")
        buf.write("\u00ad\u00af\7\17\2\2\u00ae\u00ad\3\2\2\2\u00ae\u00af")
        buf.write("\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b4\7\f\2\2\u00b1")
        buf.write("\u00b3\7\"\2\2\u00b2\u00b1\3\2\2\2\u00b3\u00b6\3\2\2\2")
        buf.write("\u00b4\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00c2\3")
        buf.write("\2\2\2\u00b6\u00b4\3\2\2\2\u00b7\u00b9\7\17\2\2\u00b8")
        buf.write("\u00b7\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba\3\2\2\2")
        buf.write("\u00ba\u00be\7\f\2\2\u00bb\u00bd\7\13\2\2\u00bc\u00bb")
        buf.write("\3\2\2\2\u00bd\u00c0\3\2\2\2\u00be\u00bc\3\2\2\2\u00be")
        buf.write("\u00bf\3\2\2\2\u00bf\u00c2\3\2\2\2\u00c0\u00be\3\2\2\2")
        buf.write("\u00c1\u00ae\3\2\2\2\u00c1\u00b8\3\2\2\2\u00c2\4\3\2\2")
        buf.write("\2\u00c3\u00c4\7k\2\2\u00c4\u00c5\7o\2\2\u00c5\u00c6\7")
        buf.write("r\2\2\u00c6\u00c7\7q\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9")
        buf.write("\7v\2\2\u00c9\6\3\2\2\2\u00ca\u00cb\7R\2\2\u00cb\u00cc")
        buf.write("\7t\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce\7r\2\2\u00ce\u00cf")
        buf.write("\7q\2\2\u00cf\u00d0\7u\2\2\u00d0\u00d1\7k\2\2\u00d1\u00d2")
        buf.write("\7v\2\2\u00d2\u00d3\7k\2\2\u00d3\u00d4\7q\2\2\u00d4\u00d5")
        buf.write("\7p\2\2\u00d5\b\3\2\2\2\u00d6\u00d7\7R\2\2\u00d7\u00d8")
        buf.write("\7t\2\2\u00d8\u00d9\7g\2\2\u00d9\u00da\7f\2\2\u00da\u00db")
        buf.write("\7k\2\2\u00db\u00dc\7e\2\2\u00dc\u00dd\7c\2\2\u00dd\u00de")
        buf.write("\7v\2\2\u00de\u00df\7g\2\2\u00df\n\3\2\2\2\u00e0\u00e1")
        buf.write("\7H\2\2\u00e1\u00e2\7g\2\2\u00e2\u00e3\7c\2\2\u00e3\u00e4")
        buf.write("\7v\2\2\u00e4\u00e5\7w\2\2\u00e5\u00e6\7t\2\2\u00e6\u00e7")
        buf.write("\7g\2\2\u00e7\f\3\2\2\2\u00e8\u00e9\7H\2\2\u00e9\u00ea")
        buf.write("\7c\2\2\u00ea\u00eb\7e\2\2\u00eb\u00ec\7v\2\2\u00ec\u00ed")
        buf.write("\7q\2\2\u00ed\u00ee\7t\2\2\u00ee\16\3\2\2\2\u00ef\u00f0")
        buf.write("\7I\2\2\u00f0\u00f1\7q\2\2\u00f1\u00f2\7c\2\2\u00f2\u00f3")
        buf.write("\7n\2\2\u00f3\20\3\2\2\2\u00f4\u00f5\7E\2\2\u00f5\u00f6")
        buf.write("\7n\2\2\u00f6\u00f7\7c\2\2\u00f7\u00f8\7u\2\2\u00f8\u00f9")
        buf.write("\7u\2\2\u00f9\22\3\2\2\2\u00fa\u00fb\7Q\2\2\u00fb\u00fc")
        buf.write("\7d\2\2\u00fc\u00fd\7l\2\2\u00fd\u00fe\7g\2\2\u00fe\u00ff")
        buf.write("\7e\2\2\u00ff\u0100\7v\2\2\u0100\24\3\2\2\2\u0101\u0102")
        buf.write("\7E\2\2\u0102\u0103\7q\2\2\u0103\u0104\7p\2\2\u0104\u0105")
        buf.write("\7u\2\2\u0105\u0106\7v\2\2\u0106\u0107\7c\2\2\u0107\u0108")
        buf.write("\7p\2\2\u0108\u0109\7v\2\2\u0109\26\3\2\2\2\u010a\u010b")
        buf.write("\7C\2\2\u010b\u010c\7e\2\2\u010c\u010d\7v\2\2\u010d\u010e")
        buf.write("\7k\2\2\u010e\u010f\7q\2\2\u010f\u0110\7p\2\2\u0110\30")
        buf.write("\3\2\2\2\u0111\u0112\7G\2\2\u0112\u0113\7h\2\2\u0113\u0114")
        buf.write("\7h\2\2\u0114\u0115\7g\2\2\u0115\u0116\7e\2\2\u0116\u0117")
        buf.write("\7v\2\2\u0117\32\3\2\2\2\u0118\u0119\7T\2\2\u0119\u011a")
        buf.write("\7g\2\2\u011a\u011b\7y\2\2\u011b\u011c\7c\2\2\u011c\u011d")
        buf.write("\7t\2\2\u011d\u011e\7f\2\2\u011e\34\3\2\2\2\u011f\u0120")
        buf.write("\7R\2\2\u0120\u0121\7q\2\2\u0121\u0122\7n\2\2\u0122\u0123")
        buf.write("\7k\2\2\u0123\u0124\7e\2\2\u0124\u0125\7{\2\2\u0125\36")
        buf.write("\3\2\2\2\u0126\u0127\7R\2\2\u0127\u0128\7n\2\2\u0128\u0129")
        buf.write("\7c\2\2\u0129\u012a\7p\2\2\u012a \3\2\2\2\u012b\u012c")
        buf.write("\7G\2\2\u012c\u012d\7z\2\2\u012d\u012e\7g\2\2\u012e\u012f")
        buf.write("\7e\2\2\u012f\u0130\7w\2\2\u0130\u0131\7v\2\2\u0131\u0132")
        buf.write("\7g\2\2\u0132\"\3\2\2\2\u0133\u0134\7Q\2\2\u0134\u0135")
        buf.write("\7r\2\2\u0135\u0136\7v\2\2\u0136\u0137\7k\2\2\u0137\u0138")
        buf.write("\7q\2\2\u0138\u0139\7p\2\2\u0139$\3\2\2\2\u013a\u013b")
        buf.write("\7O\2\2\u013b\u013c\7c\2\2\u013c\u013d\7t\2\2\u013d\u013e")
        buf.write("\7m\2\2\u013e\u013f\7q\2\2\u013f\u0140\7x\2\2\u0140\u0141")
        buf.write("\7H\2\2\u0141\u0142\7g\2\2\u0142\u0143\7c\2\2\u0143\u0144")
        buf.write("\7v\2\2\u0144\u0145\7w\2\2\u0145\u0146\7t\2\2\u0146\u0147")
        buf.write("\7g\2\2\u0147&\3\2\2\2\u0148\u0149\7k\2\2\u0149\u014a")
        buf.write("\7p\2\2\u014a\u014b\7v\2\2\u014b(\3\2\2\2\u014c\u014d")
        buf.write("\7h\2\2\u014d\u014e\7n\2\2\u014e\u014f\7q\2\2\u014f\u0150")
        buf.write("\7c\2\2\u0150\u0151\7v\2\2\u0151*\3\2\2\2\u0152\u0153")
        buf.write("\7u\2\2\u0153\u0154\7v\2\2\u0154\u0155\7t\2\2\u0155,\3")
        buf.write("\2\2\2\u0156\u0157\7n\2\2\u0157\u0158\7k\2\2\u0158\u0159")
        buf.write("\7u\2\2\u0159\u015a\7v\2\2\u015a.\3\2\2\2\u015b\u015c")
        buf.write("\7u\2\2\u015c\u015d\7g\2\2\u015d\u015e\7v\2\2\u015e\60")
        buf.write("\3\2\2\2\u015f\u0160\7d\2\2\u0160\u0161\7q\2\2\u0161\u0162")
        buf.write("\7q\2\2\u0162\u0163\7n\2\2\u0163\u0164\7g\2\2\u0164\u0165")
        buf.write("\7c\2\2\u0165\u0166\7p\2\2\u0166\62\3\2\2\2\u0167\u0168")
        buf.write("\5\65\33\2\u0168\u0169\5;\36\2\u0169\64\3\2\2\2\u016a")
        buf.write("\u016b\7U\2\2\u016b\66\3\2\2\2\u016c\u016d\7C\2\2\u016d")
        buf.write("8\3\2\2\2\u016e\u016f\7R\2\2\u016f:\3\2\2\2\u0170\u0171")
        buf.write("\7)\2\2\u0171<\3\2\2\2\u0172\u0173\7k\2\2\u0173\u0174")
        buf.write("\7h\2\2\u0174>\3\2\2\2\u0175\u0176\7g\2\2\u0176\u0177")
        buf.write("\7n\2\2\u0177\u0178\7u\2\2\u0178\u0179\7g\2\2\u0179@\3")
        buf.write("\2\2\2\u017a\u017b\7g\2\2\u017b\u017c\7n\2\2\u017c\u017d")
        buf.write("\7k\2\2\u017d\u017e\7h\2\2\u017eB\3\2\2\2\u017f\u0180")
        buf.write("\7k\2\2\u0180\u0181\7p\2\2\u0181D\3\2\2\2\u0182\u0183")
        buf.write("\7k\2\2\u0183\u0184\7p\2\2\u0184\u0185\7k\2\2\u0185\u0186")
        buf.write("\7v\2\2\u0186F\3\2\2\2\u0187\u0188\7w\2\2\u0188\u0189")
        buf.write("\7p\2\2\u0189\u018a\7v\2\2\u018a\u018b\7k\2\2\u018b\u018c")
        buf.write("\7n\2\2\u018cH\3\2\2\2\u018d\u018e\7y\2\2\u018e\u018f")
        buf.write("\7k\2\2\u018f\u0190\7v\2\2\u0190\u0191\7j\2\2\u0191J\3")
        buf.write("\2\2\2\u0192\u0193\7v\2\2\u0193\u0194\7j\2\2\u0194\u0195")
        buf.write("\7g\2\2\u0195\u0196\7p\2\2\u0196L\3\2\2\2\u0197\u0198")
        buf.write("\7p\2\2\u0198\u0199\7g\2\2\u0199\u019a\7x\2\2\u019a\u019b")
        buf.write("\7g\2\2\u019b\u019c\7t\2\2\u019cN\3\2\2\2\u019d\u019e")
        buf.write("\7o\2\2\u019e\u019f\7c\2\2\u019f\u01a0\7k\2\2\u01a0\u01a1")
        buf.write("\7p\2\2\u01a1P\3\2\2\2\u01a2\u01a3\7c\2\2\u01a3\u01a4")
        buf.write("\7p\2\2\u01a4\u01a5\7f\2\2\u01a5R\3\2\2\2\u01a6\u01a7")
        buf.write("\7q\2\2\u01a7\u01a8\7t\2\2\u01a8T\3\2\2\2\u01a9\u01aa")
        buf.write("\7p\2\2\u01aa\u01ab\7q\2\2\u01ab\u01ac\7v\2\2\u01acV\3")
        buf.write("\2\2\2\u01ad\u01ae\7V\2\2\u01ae\u01af\7t\2\2\u01af\u01b0")
        buf.write("\7w\2\2\u01b0\u01b1\7g\2\2\u01b1X\3\2\2\2\u01b2\u01b3")
        buf.write("\7H\2\2\u01b3\u01b4\7c\2\2\u01b4\u01b5\7n\2\2\u01b5\u01b6")
        buf.write("\7u\2\2\u01b6\u01b7\7g\2\2\u01b7Z\3\2\2\2\u01b8\u01b9")
        buf.write("\7C\2\2\u01b9\u01ba\7p\2\2\u01ba\u01bb\7{\2\2\u01bb\\")
        buf.write("\3\2\2\2\u01bc\u01bd\7C\2\2\u01bd\u01be\7n\2\2\u01be\u01bf")
        buf.write("\7n\2\2\u01bf^\3\2\2\2\u01c0\u01c1\7<\2\2\u01c1\u01c2")
        buf.write("\7?\2\2\u01c2`\3\2\2\2\u01c3\u01c4\7/\2\2\u01c4\u01c5")
        buf.write("\7@\2\2\u01c5b\3\2\2\2\u01c6\u01c7\7/\2\2\u01c7\u01c8")
        buf.write("\7,\2\2\u01c8\u01c9\7@\2\2\u01c9d\3\2\2\2\u01ca\u01cb")
        buf.write("\7?\2\2\u01cbf\3\2\2\2\u01cc\u01cd\7,\2\2\u01cd\u01ce")
        buf.write("\7?\2\2\u01ceh\3\2\2\2\u01cf\u01d0\7\61\2\2\u01d0\u01d1")
        buf.write("\7?\2\2\u01d1j\3\2\2\2\u01d2\u01d3\7-\2\2\u01d3\u01d4")
        buf.write("\7?\2\2\u01d4l\3\2\2\2\u01d5\u01d6\7/\2\2\u01d6\u01d7")
        buf.write("\7?\2\2\u01d7n\3\2\2\2\u01d8\u01d9\7?\2\2\u01d9\u01da")
        buf.write("\7?\2\2\u01dap\3\2\2\2\u01db\u01dc\7@\2\2\u01dc\u01dd")
        buf.write("\7?\2\2\u01ddr\3\2\2\2\u01de\u01df\7>\2\2\u01df\u01e0")
        buf.write("\7?\2\2\u01e0t\3\2\2\2\u01e1\u01e2\7#\2\2\u01e2\u01e3")
        buf.write("\7?\2\2\u01e3v\3\2\2\2\u01e4\u01e5\7<\2\2\u01e5x\3\2\2")
        buf.write("\2\u01e6\u01e7\7.\2\2\u01e7z\3\2\2\2\u01e8\u01e9\7]\2")
        buf.write("\2\u01e9|\3\2\2\2\u01ea\u01eb\7_\2\2\u01eb~\3\2\2\2\u01ec")
        buf.write("\u01ed\7}\2\2\u01ed\u0080\3\2\2\2\u01ee\u01ef\7\177\2")
        buf.write("\2\u01ef\u0082\3\2\2\2\u01f0\u01f1\7*\2\2\u01f1\u0084")
        buf.write("\3\2\2\2\u01f2\u01f3\7+\2\2\u01f3\u0086\3\2\2\2\u01f4")
        buf.write("\u01f5\7>\2\2\u01f5\u0088\3\2\2\2\u01f6\u01f7\7@\2\2\u01f7")
        buf.write("\u008a\3\2\2\2\u01f8\u01f9\7,\2\2\u01f9\u008c\3\2\2\2")
        buf.write("\u01fa\u01fb\7\61\2\2\u01fb\u008e\3\2\2\2\u01fc\u01fd")
        buf.write("\7-\2\2\u01fd\u0090\3\2\2\2\u01fe\u01ff\7/\2\2\u01ff\u0092")
        buf.write("\3\2\2\2\u0200\u0201\7$\2\2\u0201\u0094\3\2\2\2\u0202")
        buf.write("\u0206\5\u009fP\2\u0203\u0205\5\u00a1Q\2\u0204\u0203\3")
        buf.write("\2\2\2\u0205\u0208\3\2\2\2\u0206\u0204\3\2\2\2\u0206\u0207")
        buf.write("\3\2\2\2\u0207\u0096\3\2\2\2\u0208\u0206\3\2\2\2\u0209")
        buf.write("\u020a\5\u0093J\2\u020a\u020e\5\u009fP\2\u020b\u020d\5")
        buf.write("\u00a1Q\2\u020c\u020b\3\2\2\2\u020d\u0210\3\2\2\2\u020e")
        buf.write("\u020c\3\2\2\2\u020e\u020f\3\2\2\2\u020f\u0211\3\2\2\2")
        buf.write("\u0210\u020e\3\2\2\2\u0211\u0215\5\u009dO\2\u0212\u0214")
        buf.write("\5\u009fP\2\u0213\u0212\3\2\2\2\u0214\u0217\3\2\2\2\u0215")
        buf.write("\u0213\3\2\2\2\u0215\u0216\3\2\2\2\u0216\u0218\3\2\2\2")
        buf.write("\u0217\u0215\3\2\2\2\u0218\u0219\5\u0093J\2\u0219\u0098")
        buf.write("\3\2\2\2\u021a\u021c\5\u00a3R\2\u021b\u021a\3\2\2\2\u021c")
        buf.write("\u021d\3\2\2\2\u021d\u021b\3\2\2\2\u021d\u021e\3\2\2\2")
        buf.write("\u021e\u021f\3\2\2\2\u021f\u0221\5\u009dO\2\u0220\u0222")
        buf.write("\5\u00a3R\2\u0221\u0220\3\2\2\2\u0222\u0223\3\2\2\2\u0223")
        buf.write("\u0221\3\2\2\2\u0223\u0224\3\2\2\2\u0224\u009a\3\2\2\2")
        buf.write("\u0225\u0227\5\u00a3R\2\u0226\u0225\3\2\2\2\u0227\u0228")
        buf.write("\3\2\2\2\u0228\u0226\3\2\2\2\u0228\u0229\3\2\2\2\u0229")
        buf.write("\u009c\3\2\2\2\u022a\u022b\7\60\2\2\u022b\u009e\3\2\2")
        buf.write("\2\u022c\u022e\t\2\2\2\u022d\u022c\3\2\2\2\u022e\u00a0")
        buf.write("\3\2\2\2\u022f\u0233\5\u009fP\2\u0230\u0233\5\u00a3R\2")
        buf.write("\u0231\u0233\7a\2\2\u0232\u022f\3\2\2\2\u0232\u0230\3")
        buf.write("\2\2\2\u0232\u0231\3\2\2\2\u0233\u00a2\3\2\2\2\u0234\u0235")
        buf.write("\t\3\2\2\u0235\u00a4\3\2\2\2\u0236\u0238\t\4\2\2\u0237")
        buf.write("\u0236\3\2\2\2\u0238\u0239\3\2\2\2\u0239\u0237\3\2\2\2")
        buf.write("\u0239\u023a\3\2\2\2\u023a\u00a6\3\2\2\2\u023b\u023f\7")
        buf.write("%\2\2\u023c\u023e\n\5\2\2\u023d\u023c\3\2\2\2\u023e\u0241")
        buf.write("\3\2\2\2\u023f\u023d\3\2\2\2\u023f\u0240\3\2\2\2\u0240")
        buf.write("\u00a8\3\2\2\2\u0241\u023f\3\2\2\2\u0242\u0245\5\u00a5")
        buf.write("S\2\u0243\u0245\5\u00a7T\2\u0244\u0242\3\2\2\2\u0244\u0243")
        buf.write("\3\2\2\2\u0245\u0246\3\2\2\2\u0246\u0247\bU\2\2\u0247")
        buf.write("\u00aa\3\2\2\2\u0248\u0249\13\2\2\2\u0249\u00ac\3\2\2")
        buf.write("\2\23\2\u00ae\u00b4\u00b8\u00be\u00c1\u0206\u020e\u0215")
        buf.write("\u021d\u0223\u0228\u022d\u0232\u0239\u023f\u0244\3\b\2")
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
    PLAN = 17
    EXECUTE = 18
    OPTION = 19
    MARKOVFEATURE = 20
    INT = 21
    FLOAT = 22
    STR = 23
    LIST = 24
    SET = 25
    BOOL = 26
    S_PRIME = 27
    S = 28
    A = 29
    P = 30
    PRIME = 31
    IF = 32
    ELSE = 33
    ELIF = 34
    IN = 35
    INIT = 36
    UNTIL = 37
    WITH = 38
    THEN = 39
    NEVER = 40
    MAIN = 41
    AND = 42
    OR = 43
    NOT = 44
    TRUE = 45
    FALSE = 46
    ANY_CONDITION = 47
    ALL_CONDITION = 48
    BIND = 49
    PREDICT = 50
    PREDICT_ALL = 51
    ASSIGN = 52
    TIMES_EQ = 53
    DIV_EQ = 54
    PLUS_EQ = 55
    MINUS_EQ = 56
    EQ_TO = 57
    GT_EQ = 58
    LT_EQ = 59
    NOT_EQ = 60
    COL = 61
    COM = 62
    L_BRK = 63
    R_BRK = 64
    L_CBRK = 65
    R_CBRK = 66
    L_PAR = 67
    R_PAR = 68
    LT = 69
    GT = 70
    TIMES = 71
    DIVIDE = 72
    PLUS = 73
    MINUS = 74
    QUOTE = 75
    IDENTIFIER = 76
    FNAME = 77
    DECIMAL = 78
    INTEGER = 79
    DOT = 80
    SKIP_ = 81
    ANY = 82

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'import'", "'Proposition'", "'Predicate'", "'Feature'", "'Factor'", 
            "'Goal'", "'Class'", "'Object'", "'Constant'", "'Action'", "'Effect'", 
            "'Reward'", "'Policy'", "'Plan'", "'Execute'", "'Option'", "'MarkovFeature'", 
            "'int'", "'float'", "'str'", "'list'", "'set'", "'boolean'", 
            "'S'", "'A'", "'P'", "'''", "'if'", "'else'", "'elif'", "'in'", 
            "'init'", "'until'", "'with'", "'then'", "'never'", "'main'", 
            "'and'", "'or'", "'not'", "'True'", "'False'", "'Any'", "'All'", 
            "':='", "'->'", "'-*>'", "'='", "'*='", "'/='", "'+='", "'-='", 
            "'=='", "'>='", "'<='", "'!='", "':'", "','", "'['", "']'", 
            "'{'", "'}'", "'('", "')'", "'<'", "'>'", "'*'", "'/'", "'+'", 
            "'-'", "'\"'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "NL", "IMPORT", "PROPOSITION", "PREDICATE", 
            "FEATURE", "FACTOR", "GOAL", "CLASS", "OBJECT", "CONSTANT", 
            "ACTION", "EFFECT", "REWARD", "POLICY", "PLAN", "EXECUTE", "OPTION", 
            "MARKOVFEATURE", "INT", "FLOAT", "STR", "LIST", "SET", "BOOL", 
            "S_PRIME", "S", "A", "P", "PRIME", "IF", "ELSE", "ELIF", "IN", 
            "INIT", "UNTIL", "WITH", "THEN", "NEVER", "MAIN", "AND", "OR", 
            "NOT", "TRUE", "FALSE", "ANY_CONDITION", "ALL_CONDITION", "BIND", 
            "PREDICT", "PREDICT_ALL", "ASSIGN", "TIMES_EQ", "DIV_EQ", "PLUS_EQ", 
            "MINUS_EQ", "EQ_TO", "GT_EQ", "LT_EQ", "NOT_EQ", "COL", "COM", 
            "L_BRK", "R_BRK", "L_CBRK", "R_CBRK", "L_PAR", "R_PAR", "LT", 
            "GT", "TIMES", "DIVIDE", "PLUS", "MINUS", "QUOTE", "IDENTIFIER", 
            "FNAME", "DECIMAL", "INTEGER", "DOT", "SKIP_", "ANY" ]

    ruleNames = [ "NL", "IMPORT", "PROPOSITION", "PREDICATE", "FEATURE", 
                  "FACTOR", "GOAL", "CLASS", "OBJECT", "CONSTANT", "ACTION", 
                  "EFFECT", "REWARD", "POLICY", "PLAN", "EXECUTE", "OPTION", 
                  "MARKOVFEATURE", "INT", "FLOAT", "STR", "LIST", "SET", 
                  "BOOL", "S_PRIME", "S", "A", "P", "PRIME", "IF", "ELSE", 
                  "ELIF", "IN", "INIT", "UNTIL", "WITH", "THEN", "NEVER", 
                  "MAIN", "AND", "OR", "NOT", "TRUE", "FALSE", "ANY_CONDITION", 
                  "ALL_CONDITION", "BIND", "PREDICT", "PREDICT_ALL", "ASSIGN", 
                  "TIMES_EQ", "DIV_EQ", "PLUS_EQ", "MINUS_EQ", "EQ_TO", 
                  "GT_EQ", "LT_EQ", "NOT_EQ", "COL", "COM", "L_BRK", "R_BRK", 
                  "L_CBRK", "R_CBRK", "L_PAR", "R_PAR", "LT", "GT", "TIMES", 
                  "DIVIDE", "PLUS", "MINUS", "QUOTE", "IDENTIFIER", "FNAME", 
                  "DECIMAL", "INTEGER", "DOT", "LETTER", "ANY_CHAR", "DIGIT", 
                  "SPACES", "COMMENT", "SKIP_", "ANY" ]

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



