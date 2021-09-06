from antlr4 import *
from rlang.src.grounding.knowledge import RLangKnowledge
from rlang.src.grounding.utils.state_space import MDPMetadata
from rlang.src.language import *


def parseFile(rlang_fname: str) -> RLangKnowledge:
    rlang_file = FileStream(rlang_fname)
    lexer = RLangLexer(rlang_file)
    stream = CommonTokenStream(lexer)
    parser = RLangParser(stream)
    tree = parser.program()
    listener = RLangListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener.rlang_knowledge


def parse(rlang: str, mdp_metadata: MDPMetadata) -> RLangKnowledge:
    rlang = InputStream(rlang)
    lexer = RLangLexer(rlang)
    stream = CommonTokenStream(lexer)
    parser = RLangParser(stream)
    tree = parser.program()
    listener = RLangListener(mdp_metadata)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener.rlang_knowledge
