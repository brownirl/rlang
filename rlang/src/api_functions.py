from antlr4 import *
from rlang.src.grounding.base import RLangKnowledge
from rlang.src.grounding.internals import MDPMetadata
from rlang.src.language.antlr import *
from rlang.src.language.antlr.RLangErrorListener import RLangErrorListener


def parse_file(rlang_fname: str, mdp_metadata: MDPMetadata = None) -> RLangKnowledge:
    rlang_file = FileStream(rlang_fname)
    lexer = RLangLexer(rlang_file)
    stream = CommonTokenStream(lexer)
    parser = RLangParser(stream)
    parser.addErrorListener(RLangErrorListener())
    tree = parser.program()
    listener = RLangListener(mdp_metadata)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener.rlang_knowledge


def parse(rlang: str, mdp_metadata: MDPMetadata = None) -> RLangKnowledge:
    rlang = InputStream(rlang)
    lexer = RLangLexer(rlang)
    stream = CommonTokenStream(lexer)
    parser = RLangParser(stream)
    parser.addErrorListener(RLangErrorListener())
    tree = parser.program()
    listener = RLangListener(mdp_metadata)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener.rlang_knowledge
