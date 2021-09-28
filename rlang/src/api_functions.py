from __future__ import annotations
from antlr4 import *
from rlang.src.grounding.base import RLangKnowledge
from rlang.src.grounding.internals import MDPMetadata
from rlang.src.language.antlr import *
from rlang.src.language.antlr.RLangErrorListener import RLangErrorListener


def parse_file(rlang_fname: str, mdp_metadata: MDPMetadata = None, prior_knowledge: RLangKnowledge = None) -> RLangKnowledge:
    """Parses a .rlang file

    Args:
        rlang_fname: filename
        mdp_metadata (optional): an MDPMetadata object
        prior_knowledge (optional): an RLangKnowledge object

    Returns:
        An RLangKnowledge object

    """
    rlang_file = FileStream(rlang_fname)
    lexer = RLangLexer(rlang_file)
    stream = CommonTokenStream(lexer)
    parser = RLangParser(stream)
    parser.addErrorListener(RLangErrorListener())
    tree = parser.program()
    listener = RLangListener(mdp_metadata, prior_knowledge)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener.rlang_knowledge


def parse(rlang: str, mdp_metadata: MDPMetadata = None, prior_knowledge: RLangKnowledge = None) -> RLangKnowledge:
    """Parses an rlang string

    Args:
        rlang: string containing rlang
        mdp_metadata (optional): an MDPMetadata object
        prior_knowledge (optional): an RLangKnowledge object

    Returns:
        An RLangKnowledge object

    """
    rlang = InputStream(rlang)
    lexer = RLangLexer(rlang)
    stream = CommonTokenStream(lexer)
    parser = RLangParser(stream)
    parser.addErrorListener(RLangErrorListener())
    tree = parser.program()
    listener = RLangListener(mdp_metadata, prior_knowledge)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener.rlang_knowledge

