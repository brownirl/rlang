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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2S")
        buf.write("\u0244\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("U\3\2\5\2\u00ad\n\2\3\2\3\2\7\2\u00b1\n\2\f\2\16\2\u00b4")
        buf.write("\13\2\3\2\5\2\u00b7\n\2\3\2\3\2\7\2\u00bb\n\2\f\2\16\2")
        buf.write("\u00be\13\2\5\2\u00c0\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3")
        buf.write("!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3")
        buf.write("%\3%\3%\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3")
        buf.write("(\3(\3(\3)\3)\3)\3)\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3,\3")
        buf.write(",\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/\3/\3\60\3\60")
        buf.write("\3\60\3\61\3\61\3\61\3\62\3\62\3\63\3\63\3\63\3\64\3\64")
        buf.write("\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67\38")
        buf.write("\38\38\39\39\39\3:\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3")
        buf.write("?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3")
        buf.write("H\3I\3I\3J\3J\7J\u01ff\nJ\fJ\16J\u0202\13J\3K\3K\3K\7")
        buf.write("K\u0207\nK\fK\16K\u020a\13K\3K\3K\7K\u020e\nK\fK\16K\u0211")
        buf.write("\13K\3K\3K\3L\6L\u0216\nL\rL\16L\u0217\3L\3L\6L\u021c")
        buf.write("\nL\rL\16L\u021d\3M\6M\u0221\nM\rM\16M\u0222\3N\3N\3O")
        buf.write("\5O\u0228\nO\3P\3P\3P\5P\u022d\nP\3Q\3Q\3R\6R\u0232\n")
        buf.write("R\rR\16R\u0233\3S\3S\7S\u0238\nS\fS\16S\u023b\13S\3T\3")
        buf.write("T\5T\u023f\nT\3T\3T\3U\3U\2\2V\3\5\5\6\7\7\t\b\13\t\r")
        buf.write("\n\17\13\21\f\23\r\25\16\27\17\31\20\33\21\35\22\37\23")
        buf.write("!\24#\25%\26\'\27)\30+\31-\32/\33\61\34\63\35\65\36\67")
        buf.write("\379 ;!=\"?#A$C%E&G\'I(K)M*O+Q,S-U.W/Y\60[\61]\62_\63")
        buf.write("a\64c\65e\66g\67i8k9m:o;q<s=u>w?y@{A}B\177C\u0081D\u0083")
        buf.write("E\u0085F\u0087G\u0089H\u008bI\u008dJ\u008fK\u0091L\u0093")
        buf.write("M\u0095N\u0097O\u0099P\u009bQ\u009d\2\u009f\2\u00a1\2")
        buf.write("\u00a3\2\u00a5\2\u00a7R\u00a9S\3\2\6\4\2C\\c|\3\2\62;")
        buf.write("\4\2\13\13\"\"\4\2\f\f\16\17\2\u024e\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2")
        buf.write("\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3")
        buf.write("\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W")
        buf.write("\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2")
        buf.write("a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2")
        buf.write("\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2")
        buf.write("\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2")
        buf.write("\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2")
        buf.write("\2\2\u009b\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\3\u00bf")
        buf.write("\3\2\2\2\5\u00c1\3\2\2\2\7\u00c8\3\2\2\2\t\u00d4\3\2\2")
        buf.write("\2\13\u00de\3\2\2\2\r\u00e6\3\2\2\2\17\u00ed\3\2\2\2\21")
        buf.write("\u00f2\3\2\2\2\23\u00f8\3\2\2\2\25\u00ff\3\2\2\2\27\u0108")
        buf.write("\3\2\2\2\31\u010f\3\2\2\2\33\u0116\3\2\2\2\35\u011d\3")
        buf.write("\2\2\2\37\u0124\3\2\2\2!\u0129\3\2\2\2#\u0131\3\2\2\2")
        buf.write("%\u0138\3\2\2\2\'\u0146\3\2\2\2)\u014a\3\2\2\2+\u0150")
        buf.write("\3\2\2\2-\u0154\3\2\2\2/\u0159\3\2\2\2\61\u015d\3\2\2")
        buf.write("\2\63\u0165\3\2\2\2\65\u0168\3\2\2\2\67\u016a\3\2\2\2")
        buf.write("9\u016c\3\2\2\2;\u016e\3\2\2\2=\u0170\3\2\2\2?\u0173\3")
        buf.write("\2\2\2A\u0178\3\2\2\2C\u017d\3\2\2\2E\u0180\3\2\2\2G\u0185")
        buf.write("\3\2\2\2I\u018b\3\2\2\2K\u0190\3\2\2\2M\u0195\3\2\2\2")
        buf.write("O\u019b\3\2\2\2Q\u01a0\3\2\2\2S\u01a4\3\2\2\2U\u01a7\3")
        buf.write("\2\2\2W\u01ab\3\2\2\2Y\u01b0\3\2\2\2[\u01b6\3\2\2\2]\u01ba")
        buf.write("\3\2\2\2_\u01be\3\2\2\2a\u01c1\3\2\2\2c\u01c4\3\2\2\2")
        buf.write("e\u01c6\3\2\2\2g\u01c9\3\2\2\2i\u01cc\3\2\2\2k\u01cf\3")
        buf.write("\2\2\2m\u01d2\3\2\2\2o\u01d5\3\2\2\2q\u01d8\3\2\2\2s\u01db")
        buf.write("\3\2\2\2u\u01de\3\2\2\2w\u01e0\3\2\2\2y\u01e2\3\2\2\2")
        buf.write("{\u01e4\3\2\2\2}\u01e6\3\2\2\2\177\u01e8\3\2\2\2\u0081")
        buf.write("\u01ea\3\2\2\2\u0083\u01ec\3\2\2\2\u0085\u01ee\3\2\2\2")
        buf.write("\u0087\u01f0\3\2\2\2\u0089\u01f2\3\2\2\2\u008b\u01f4\3")
        buf.write("\2\2\2\u008d\u01f6\3\2\2\2\u008f\u01f8\3\2\2\2\u0091\u01fa")
        buf.write("\3\2\2\2\u0093\u01fc\3\2\2\2\u0095\u0203\3\2\2\2\u0097")
        buf.write("\u0215\3\2\2\2\u0099\u0220\3\2\2\2\u009b\u0224\3\2\2\2")
        buf.write("\u009d\u0227\3\2\2\2\u009f\u022c\3\2\2\2\u00a1\u022e\3")
        buf.write("\2\2\2\u00a3\u0231\3\2\2\2\u00a5\u0235\3\2\2\2\u00a7\u023e")
        buf.write("\3\2\2\2\u00a9\u0242\3\2\2\2\u00ab\u00ad\7\17\2\2\u00ac")
        buf.write("\u00ab\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00ae\3\2\2\2")
        buf.write("\u00ae\u00b2\7\f\2\2\u00af\u00b1\7\"\2\2\u00b0\u00af\3")
        buf.write("\2\2\2\u00b1\u00b4\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b3")
        buf.write("\3\2\2\2\u00b3\u00c0\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b5")
        buf.write("\u00b7\7\17\2\2\u00b6\u00b5\3\2\2\2\u00b6\u00b7\3\2\2")
        buf.write("\2\u00b7\u00b8\3\2\2\2\u00b8\u00bc\7\f\2\2\u00b9\u00bb")
        buf.write("\7\13\2\2\u00ba\u00b9\3\2\2\2\u00bb\u00be\3\2\2\2\u00bc")
        buf.write("\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00c0\3\2\2\2")
        buf.write("\u00be\u00bc\3\2\2\2\u00bf\u00ac\3\2\2\2\u00bf\u00b6\3")
        buf.write("\2\2\2\u00c0\4\3\2\2\2\u00c1\u00c2\7k\2\2\u00c2\u00c3")
        buf.write("\7o\2\2\u00c3\u00c4\7r\2\2\u00c4\u00c5\7q\2\2\u00c5\u00c6")
        buf.write("\7t\2\2\u00c6\u00c7\7v\2\2\u00c7\6\3\2\2\2\u00c8\u00c9")
        buf.write("\7R\2\2\u00c9\u00ca\7t\2\2\u00ca\u00cb\7q\2\2\u00cb\u00cc")
        buf.write("\7r\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce\7u\2\2\u00ce\u00cf")
        buf.write("\7k\2\2\u00cf\u00d0\7v\2\2\u00d0\u00d1\7k\2\2\u00d1\u00d2")
        buf.write("\7q\2\2\u00d2\u00d3\7p\2\2\u00d3\b\3\2\2\2\u00d4\u00d5")
        buf.write("\7R\2\2\u00d5\u00d6\7t\2\2\u00d6\u00d7\7g\2\2\u00d7\u00d8")
        buf.write("\7f\2\2\u00d8\u00d9\7k\2\2\u00d9\u00da\7e\2\2\u00da\u00db")
        buf.write("\7c\2\2\u00db\u00dc\7v\2\2\u00dc\u00dd\7g\2\2\u00dd\n")
        buf.write("\3\2\2\2\u00de\u00df\7H\2\2\u00df\u00e0\7g\2\2\u00e0\u00e1")
        buf.write("\7c\2\2\u00e1\u00e2\7v\2\2\u00e2\u00e3\7w\2\2\u00e3\u00e4")
        buf.write("\7t\2\2\u00e4\u00e5\7g\2\2\u00e5\f\3\2\2\2\u00e6\u00e7")
        buf.write("\7H\2\2\u00e7\u00e8\7c\2\2\u00e8\u00e9\7e\2\2\u00e9\u00ea")
        buf.write("\7v\2\2\u00ea\u00eb\7q\2\2\u00eb\u00ec\7t\2\2\u00ec\16")
        buf.write("\3\2\2\2\u00ed\u00ee\7I\2\2\u00ee\u00ef\7q\2\2\u00ef\u00f0")
        buf.write("\7c\2\2\u00f0\u00f1\7n\2\2\u00f1\20\3\2\2\2\u00f2\u00f3")
        buf.write("\7E\2\2\u00f3\u00f4\7n\2\2\u00f4\u00f5\7c\2\2\u00f5\u00f6")
        buf.write("\7u\2\2\u00f6\u00f7\7u\2\2\u00f7\22\3\2\2\2\u00f8\u00f9")
        buf.write("\7Q\2\2\u00f9\u00fa\7d\2\2\u00fa\u00fb\7l\2\2\u00fb\u00fc")
        buf.write("\7g\2\2\u00fc\u00fd\7e\2\2\u00fd\u00fe\7v\2\2\u00fe\24")
        buf.write("\3\2\2\2\u00ff\u0100\7E\2\2\u0100\u0101\7q\2\2\u0101\u0102")
        buf.write("\7p\2\2\u0102\u0103\7u\2\2\u0103\u0104\7v\2\2\u0104\u0105")
        buf.write("\7c\2\2\u0105\u0106\7p\2\2\u0106\u0107\7v\2\2\u0107\26")
        buf.write("\3\2\2\2\u0108\u0109\7C\2\2\u0109\u010a\7e\2\2\u010a\u010b")
        buf.write("\7v\2\2\u010b\u010c\7k\2\2\u010c\u010d\7q\2\2\u010d\u010e")
        buf.write("\7p\2\2\u010e\30\3\2\2\2\u010f\u0110\7G\2\2\u0110\u0111")
        buf.write("\7h\2\2\u0111\u0112\7h\2\2\u0112\u0113\7g\2\2\u0113\u0114")
        buf.write("\7e\2\2\u0114\u0115\7v\2\2\u0115\32\3\2\2\2\u0116\u0117")
        buf.write("\7T\2\2\u0117\u0118\7g\2\2\u0118\u0119\7y\2\2\u0119\u011a")
        buf.write("\7c\2\2\u011a\u011b\7t\2\2\u011b\u011c\7f\2\2\u011c\34")
        buf.write("\3\2\2\2\u011d\u011e\7R\2\2\u011e\u011f\7q\2\2\u011f\u0120")
        buf.write("\7n\2\2\u0120\u0121\7k\2\2\u0121\u0122\7e\2\2\u0122\u0123")
        buf.write("\7{\2\2\u0123\36\3\2\2\2\u0124\u0125\7R\2\2\u0125\u0126")
        buf.write("\7n\2\2\u0126\u0127\7c\2\2\u0127\u0128\7p\2\2\u0128 \3")
        buf.write("\2\2\2\u0129\u012a\7G\2\2\u012a\u012b\7z\2\2\u012b\u012c")
        buf.write("\7g\2\2\u012c\u012d\7e\2\2\u012d\u012e\7w\2\2\u012e\u012f")
        buf.write("\7v\2\2\u012f\u0130\7g\2\2\u0130\"\3\2\2\2\u0131\u0132")
        buf.write("\7Q\2\2\u0132\u0133\7r\2\2\u0133\u0134\7v\2\2\u0134\u0135")
        buf.write("\7k\2\2\u0135\u0136\7q\2\2\u0136\u0137\7p\2\2\u0137$\3")
        buf.write("\2\2\2\u0138\u0139\7O\2\2\u0139\u013a\7c\2\2\u013a\u013b")
        buf.write("\7t\2\2\u013b\u013c\7m\2\2\u013c\u013d\7q\2\2\u013d\u013e")
        buf.write("\7x\2\2\u013e\u013f\7H\2\2\u013f\u0140\7g\2\2\u0140\u0141")
        buf.write("\7c\2\2\u0141\u0142\7v\2\2\u0142\u0143\7w\2\2\u0143\u0144")
        buf.write("\7t\2\2\u0144\u0145\7g\2\2\u0145&\3\2\2\2\u0146\u0147")
        buf.write("\7k\2\2\u0147\u0148\7p\2\2\u0148\u0149\7v\2\2\u0149(\3")
        buf.write("\2\2\2\u014a\u014b\7h\2\2\u014b\u014c\7n\2\2\u014c\u014d")
        buf.write("\7q\2\2\u014d\u014e\7c\2\2\u014e\u014f\7v\2\2\u014f*\3")
        buf.write("\2\2\2\u0150\u0151\7u\2\2\u0151\u0152\7v\2\2\u0152\u0153")
        buf.write("\7t\2\2\u0153,\3\2\2\2\u0154\u0155\7n\2\2\u0155\u0156")
        buf.write("\7k\2\2\u0156\u0157\7u\2\2\u0157\u0158\7v\2\2\u0158.\3")
        buf.write("\2\2\2\u0159\u015a\7u\2\2\u015a\u015b\7g\2\2\u015b\u015c")
        buf.write("\7v\2\2\u015c\60\3\2\2\2\u015d\u015e\7d\2\2\u015e\u015f")
        buf.write("\7q\2\2\u015f\u0160\7q\2\2\u0160\u0161\7n\2\2\u0161\u0162")
        buf.write("\7g\2\2\u0162\u0163\7c\2\2\u0163\u0164\7p\2\2\u0164\62")
        buf.write("\3\2\2\2\u0165\u0166\5\65\33\2\u0166\u0167\5;\36\2\u0167")
        buf.write("\64\3\2\2\2\u0168\u0169\7U\2\2\u0169\66\3\2\2\2\u016a")
        buf.write("\u016b\7C\2\2\u016b8\3\2\2\2\u016c\u016d\7R\2\2\u016d")
        buf.write(":\3\2\2\2\u016e\u016f\7)\2\2\u016f<\3\2\2\2\u0170\u0171")
        buf.write("\7k\2\2\u0171\u0172\7h\2\2\u0172>\3\2\2\2\u0173\u0174")
        buf.write("\7g\2\2\u0174\u0175\7n\2\2\u0175\u0176\7u\2\2\u0176\u0177")
        buf.write("\7g\2\2\u0177@\3\2\2\2\u0178\u0179\7g\2\2\u0179\u017a")
        buf.write("\7n\2\2\u017a\u017b\7k\2\2\u017b\u017c\7h\2\2\u017cB\3")
        buf.write("\2\2\2\u017d\u017e\7k\2\2\u017e\u017f\7p\2\2\u017fD\3")
        buf.write("\2\2\2\u0180\u0181\7k\2\2\u0181\u0182\7p\2\2\u0182\u0183")
        buf.write("\7k\2\2\u0183\u0184\7v\2\2\u0184F\3\2\2\2\u0185\u0186")
        buf.write("\7w\2\2\u0186\u0187\7p\2\2\u0187\u0188\7v\2\2\u0188\u0189")
        buf.write("\7k\2\2\u0189\u018a\7n\2\2\u018aH\3\2\2\2\u018b\u018c")
        buf.write("\7y\2\2\u018c\u018d\7k\2\2\u018d\u018e\7v\2\2\u018e\u018f")
        buf.write("\7j\2\2\u018fJ\3\2\2\2\u0190\u0191\7v\2\2\u0191\u0192")
        buf.write("\7j\2\2\u0192\u0193\7g\2\2\u0193\u0194\7p\2\2\u0194L\3")
        buf.write("\2\2\2\u0195\u0196\7p\2\2\u0196\u0197\7g\2\2\u0197\u0198")
        buf.write("\7x\2\2\u0198\u0199\7g\2\2\u0199\u019a\7t\2\2\u019aN\3")
        buf.write("\2\2\2\u019b\u019c\7o\2\2\u019c\u019d\7c\2\2\u019d\u019e")
        buf.write("\7k\2\2\u019e\u019f\7p\2\2\u019fP\3\2\2\2\u01a0\u01a1")
        buf.write("\7c\2\2\u01a1\u01a2\7p\2\2\u01a2\u01a3\7f\2\2\u01a3R\3")
        buf.write("\2\2\2\u01a4\u01a5\7q\2\2\u01a5\u01a6\7t\2\2\u01a6T\3")
        buf.write("\2\2\2\u01a7\u01a8\7p\2\2\u01a8\u01a9\7q\2\2\u01a9\u01aa")
        buf.write("\7v\2\2\u01aaV\3\2\2\2\u01ab\u01ac\7V\2\2\u01ac\u01ad")
        buf.write("\7t\2\2\u01ad\u01ae\7w\2\2\u01ae\u01af\7g\2\2\u01afX\3")
        buf.write("\2\2\2\u01b0\u01b1\7H\2\2\u01b1\u01b2\7c\2\2\u01b2\u01b3")
        buf.write("\7n\2\2\u01b3\u01b4\7u\2\2\u01b4\u01b5\7g\2\2\u01b5Z\3")
        buf.write("\2\2\2\u01b6\u01b7\7C\2\2\u01b7\u01b8\7p\2\2\u01b8\u01b9")
        buf.write("\7{\2\2\u01b9\\\3\2\2\2\u01ba\u01bb\7C\2\2\u01bb\u01bc")
        buf.write("\7n\2\2\u01bc\u01bd\7n\2\2\u01bd^\3\2\2\2\u01be\u01bf")
        buf.write("\7<\2\2\u01bf\u01c0\7?\2\2\u01c0`\3\2\2\2\u01c1\u01c2")
        buf.write("\7/\2\2\u01c2\u01c3\7@\2\2\u01c3b\3\2\2\2\u01c4\u01c5")
        buf.write("\7?\2\2\u01c5d\3\2\2\2\u01c6\u01c7\7,\2\2\u01c7\u01c8")
        buf.write("\7?\2\2\u01c8f\3\2\2\2\u01c9\u01ca\7\61\2\2\u01ca\u01cb")
        buf.write("\7?\2\2\u01cbh\3\2\2\2\u01cc\u01cd\7-\2\2\u01cd\u01ce")
        buf.write("\7?\2\2\u01cej\3\2\2\2\u01cf\u01d0\7/\2\2\u01d0\u01d1")
        buf.write("\7?\2\2\u01d1l\3\2\2\2\u01d2\u01d3\7?\2\2\u01d3\u01d4")
        buf.write("\7?\2\2\u01d4n\3\2\2\2\u01d5\u01d6\7@\2\2\u01d6\u01d7")
        buf.write("\7?\2\2\u01d7p\3\2\2\2\u01d8\u01d9\7>\2\2\u01d9\u01da")
        buf.write("\7?\2\2\u01dar\3\2\2\2\u01db\u01dc\7#\2\2\u01dc\u01dd")
        buf.write("\7?\2\2\u01ddt\3\2\2\2\u01de\u01df\7<\2\2\u01dfv\3\2\2")
        buf.write("\2\u01e0\u01e1\7.\2\2\u01e1x\3\2\2\2\u01e2\u01e3\7]\2")
        buf.write("\2\u01e3z\3\2\2\2\u01e4\u01e5\7_\2\2\u01e5|\3\2\2\2\u01e6")
        buf.write("\u01e7\7}\2\2\u01e7~\3\2\2\2\u01e8\u01e9\7\177\2\2\u01e9")
        buf.write("\u0080\3\2\2\2\u01ea\u01eb\7*\2\2\u01eb\u0082\3\2\2\2")
        buf.write("\u01ec\u01ed\7+\2\2\u01ed\u0084\3\2\2\2\u01ee\u01ef\7")
        buf.write(">\2\2\u01ef\u0086\3\2\2\2\u01f0\u01f1\7@\2\2\u01f1\u0088")
        buf.write("\3\2\2\2\u01f2\u01f3\7,\2\2\u01f3\u008a\3\2\2\2\u01f4")
        buf.write("\u01f5\7\61\2\2\u01f5\u008c\3\2\2\2\u01f6\u01f7\7-\2\2")
        buf.write("\u01f7\u008e\3\2\2\2\u01f8\u01f9\7/\2\2\u01f9\u0090\3")
        buf.write("\2\2\2\u01fa\u01fb\7$\2\2\u01fb\u0092\3\2\2\2\u01fc\u0200")
        buf.write("\5\u009dO\2\u01fd\u01ff\5\u009fP\2\u01fe\u01fd\3\2\2\2")
        buf.write("\u01ff\u0202\3\2\2\2\u0200\u01fe\3\2\2\2\u0200\u0201\3")
        buf.write("\2\2\2\u0201\u0094\3\2\2\2\u0202\u0200\3\2\2\2\u0203\u0204")
        buf.write("\5\u0091I\2\u0204\u0208\5\u009dO\2\u0205\u0207\5\u009f")
        buf.write("P\2\u0206\u0205\3\2\2\2\u0207\u020a\3\2\2\2\u0208\u0206")
        buf.write("\3\2\2\2\u0208\u0209\3\2\2\2\u0209\u020b\3\2\2\2\u020a")
        buf.write("\u0208\3\2\2\2\u020b\u020f\5\u009bN\2\u020c\u020e\5\u009d")
        buf.write("O\2\u020d\u020c\3\2\2\2\u020e\u0211\3\2\2\2\u020f\u020d")
        buf.write("\3\2\2\2\u020f\u0210\3\2\2\2\u0210\u0212\3\2\2\2\u0211")
        buf.write("\u020f\3\2\2\2\u0212\u0213\5\u0091I\2\u0213\u0096\3\2")
        buf.write("\2\2\u0214\u0216\5\u00a1Q\2\u0215\u0214\3\2\2\2\u0216")
        buf.write("\u0217\3\2\2\2\u0217\u0215\3\2\2\2\u0217\u0218\3\2\2\2")
        buf.write("\u0218\u0219\3\2\2\2\u0219\u021b\5\u009bN\2\u021a\u021c")
        buf.write("\5\u00a1Q\2\u021b\u021a\3\2\2\2\u021c\u021d\3\2\2\2\u021d")
        buf.write("\u021b\3\2\2\2\u021d\u021e\3\2\2\2\u021e\u0098\3\2\2\2")
        buf.write("\u021f\u0221\5\u00a1Q\2\u0220\u021f\3\2\2\2\u0221\u0222")
        buf.write("\3\2\2\2\u0222\u0220\3\2\2\2\u0222\u0223\3\2\2\2\u0223")
        buf.write("\u009a\3\2\2\2\u0224\u0225\7\60\2\2\u0225\u009c\3\2\2")
        buf.write("\2\u0226\u0228\t\2\2\2\u0227\u0226\3\2\2\2\u0228\u009e")
        buf.write("\3\2\2\2\u0229\u022d\5\u009dO\2\u022a\u022d\5\u00a1Q\2")
        buf.write("\u022b\u022d\7a\2\2\u022c\u0229\3\2\2\2\u022c\u022a\3")
        buf.write("\2\2\2\u022c\u022b\3\2\2\2\u022d\u00a0\3\2\2\2\u022e\u022f")
        buf.write("\t\3\2\2\u022f\u00a2\3\2\2\2\u0230\u0232\t\4\2\2\u0231")
        buf.write("\u0230\3\2\2\2\u0232\u0233\3\2\2\2\u0233\u0231\3\2\2\2")
        buf.write("\u0233\u0234\3\2\2\2\u0234\u00a4\3\2\2\2\u0235\u0239\7")
        buf.write("%\2\2\u0236\u0238\n\5\2\2\u0237\u0236\3\2\2\2\u0238\u023b")
        buf.write("\3\2\2\2\u0239\u0237\3\2\2\2\u0239\u023a\3\2\2\2\u023a")
        buf.write("\u00a6\3\2\2\2\u023b\u0239\3\2\2\2\u023c\u023f\5\u00a3")
        buf.write("R\2\u023d\u023f\5\u00a5S\2\u023e\u023c\3\2\2\2\u023e\u023d")
        buf.write("\3\2\2\2\u023f\u0240\3\2\2\2\u0240\u0241\bT\2\2\u0241")
        buf.write("\u00a8\3\2\2\2\u0242\u0243\13\2\2\2\u0243\u00aa\3\2\2")
        buf.write("\2\23\2\u00ac\u00b2\u00b6\u00bc\u00bf\u0200\u0208\u020f")
        buf.write("\u0217\u021d\u0222\u0227\u022c\u0233\u0239\u023e\3\b\2")
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
    ASSIGN = 51
    TIMES_EQ = 52
    DIV_EQ = 53
    PLUS_EQ = 54
    MINUS_EQ = 55
    EQ_TO = 56
    GT_EQ = 57
    LT_EQ = 58
    NOT_EQ = 59
    COL = 60
    COM = 61
    L_BRK = 62
    R_BRK = 63
    L_CBRK = 64
    R_CBRK = 65
    L_PAR = 66
    R_PAR = 67
    LT = 68
    GT = 69
    TIMES = 70
    DIVIDE = 71
    PLUS = 72
    MINUS = 73
    QUOTE = 74
    IDENTIFIER = 75
    FNAME = 76
    DECIMAL = 77
    INTEGER = 78
    DOT = 79
    SKIP_ = 80
    ANY = 81

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
            "':='", "'->'", "'='", "'*='", "'/='", "'+='", "'-='", "'=='", 
            "'>='", "'<='", "'!='", "':'", "','", "'['", "']'", "'{'", "'}'", 
            "'('", "')'", "'<'", "'>'", "'*'", "'/'", "'+'", "'-'", "'\"'", 
            "'.'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "NL", "IMPORT", "PROPOSITION", "PREDICATE", 
            "FEATURE", "FACTOR", "GOAL", "CLASS", "OBJECT", "CONSTANT", 
            "ACTION", "EFFECT", "REWARD", "POLICY", "PLAN", "EXECUTE", "OPTION", 
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
                  "EFFECT", "REWARD", "POLICY", "PLAN", "EXECUTE", "OPTION", 
                  "MARKOVFEATURE", "INT", "FLOAT", "STR", "LIST", "SET", 
                  "BOOL", "S_PRIME", "S", "A", "P", "PRIME", "IF", "ELSE", 
                  "ELIF", "IN", "INIT", "UNTIL", "WITH", "THEN", "NEVER", 
                  "MAIN", "AND", "OR", "NOT", "TRUE", "FALSE", "ANY_CONDITION", 
                  "ALL_CONDITION", "BIND", "PREDICT", "ASSIGN", "TIMES_EQ", 
                  "DIV_EQ", "PLUS_EQ", "MINUS_EQ", "EQ_TO", "GT_EQ", "LT_EQ", 
                  "NOT_EQ", "COL", "COM", "L_BRK", "R_BRK", "L_CBRK", "R_CBRK", 
                  "L_PAR", "R_PAR", "LT", "GT", "TIMES", "DIVIDE", "PLUS", 
                  "MINUS", "QUOTE", "IDENTIFIER", "FNAME", "DECIMAL", "INTEGER", 
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



