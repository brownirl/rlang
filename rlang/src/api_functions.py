import numpy as np
from antlr4 import *
from rlang.src.grounding.knowledge import RLangKnowledge
from rlang.src.grounding.utils.state_space import MDPMetadata, StateSpace
from rlang.src.language import *
from rlang.src.language.RLangErrorListener import RLangErrorListener


def parse_file(rlang_fname: str) -> RLangKnowledge:
    rlang_file = FileStream(rlang_fname)
    lexer = RLangLexer(rlang_file)
    stream = CommonTokenStream(lexer)
    parser = RLangParser(stream)
    parser.addErrorListener(RLangErrorListener())
    tree = parser.program()
    listener = RLangListener()
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


def metadata_from_state(state_instance: np.ndarray):
    s = StateSpace(state_instance.dtype, state_instance.shape)
    return MDPMetadata(s)
