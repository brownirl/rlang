from antlr4 import *

from antlr import RLangLexer
from antlr import RLangParser
from antlr.RLangListener import RLangListener
from .LMDPClass import LMDP


class RLMDP(LMDP):
    def __init__(self, mdp, rlang_fname, factor_names=None, domain_name=None):
        super().__init__(mdp, factor_names, domain_name)
        rlang = FileStream(rlang_fname)
        lexer = RLangLexer(rlang)
        stream = CommonTokenStream(lexer)
        parser = RLangParser(stream)
        tree = parser.program()
        listener = RLangListener(self)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
