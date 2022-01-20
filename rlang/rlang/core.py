"""This module contains simple user-facing functions for parsing RLang
 into an :py:class:`.RLangKnowledge` object, which can be
 provided to an RLang-enabled agent."""

from __future__ import annotations
from antlr4 import *

from .knowledge import RLangKnowledge
from .language.RLangLexer import RLangLexer
from .language.RLangParser import RLangParser
from .language.RLangErrorListener import RLangErrorListener
from .language.RLangListener import RLangListener


def parse_file(rlang_fname: str, prior_knowledge: RLangKnowledge = None) -> RLangKnowledge:
    """Parses an ``.rlang`` file into an :py:class:`.RLangKnowledge` object.

    Args:
        rlang_fname: filename
        prior_knowledge: prior knowledge that should be retained after parsing

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


def parse(rlang: str, prior_knowledge: RLangKnowledge = None) -> RLangKnowledge:
    """Parses an rlang string into an :py:class:`.RLangKnowledge` object.

    Args:
        rlang: string containing rlang
        prior_knowledge: prior knowledge that should be retained after parsing

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

