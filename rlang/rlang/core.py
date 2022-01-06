from __future__ import annotations
from antlr4 import *

from .knowledge import RLangKnowledge
from .language.RLangLexer import RLangLexer, RLangParser
from .language.RLangErrorListener import RLangErrorListener
from .language.RLangListener import RLangListener
from .grounding.utils.utils import MDPMetadata


def parse_file(rlang_fname: str, mdp_metadata: MDPMetadata = None, prior_knowledge: RLangKnowledge = None) -> RLangKnowledge:
    """Parses a .rlang file

    Args:
        rlang_fname: filename
        mdp_metadata (optional): an MDPMetadata object
        prior_knowledge (optional): an RLangKnowledge object

    Returns:
        An RLangKnowledge object

    """
    if prior_knowledge is None:
        prior_knowledge = RLangKnowledge()

    rlang_file = FileStream(rlang_fname)
    lexer = RLangLexer(rlang_file)
    stream = CommonTokenStream(lexer)
    parser = RLangParser(stream)
    parser.addErrorListener(RLangErrorListener())
    tree = parser.program()
    listener = RLangListener(prior_knowledge)
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
    if prior_knowledge is None:
        prior_knowledge = RLangKnowledge()

    rlang = InputStream(rlang)
    lexer = RLangLexer(rlang)
    stream = CommonTokenStream(lexer)
    parser = RLangParser(stream)
    parser.addErrorListener(RLangErrorListener())
    tree = parser.program()
    listener = RLangListener(prior_knowledge)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener.rlang_knowledge

