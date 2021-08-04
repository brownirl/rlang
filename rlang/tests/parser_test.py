from sre_constants import FAILURE
from antlr4 import *

import sys, os
sys.path.append(os.path.abspath("../"))
from rlang.src.language.RLangLexer import RLangLexer
from rlang.src.language.RLangParser import RLangParser
from antlr4.tree.ParseTreePatternMatcher import ParseTreePatternMatcher
from rlang.src.language.RLangErrorListener import RLangErrorListener
from antlr4.error.Errors import *

# from .lexer_test import tokenize_from_string

# All tests must begin with 'test_'

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def parse_from_input(input_string):
    input_stream = InputStream(input_string)
    lexer = RLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = RLangParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(RLangErrorListener())

    return parser

def test_factor():
    file = open(os.path.join(__location__, "tests_resources/factor.rlang"), "r")
    for line in file:
        try:
            parser = parse_from_input(line)
            tree = parser.dec()
            # print(tree.getTokens())
            # print(tree.toStringTree())
        except Exception as re:
            assert False

def test_feature():
    file = open(os.path.join(__location__, "tests_resources/feature.rlang"), "r")
    for line in file:
        try:
            parser = parse_from_input(line)
            tree = parser.dec()
        except Exception:
            assert False
        

def test_predicate():
    print(os.getcwd())
    file = open(os.path.join(__location__, "tests_resources/predicate.rlang"), "r")
    for line in file:
        try:
            parser = parse_from_input(line)
            tree = parser.dec()
        except Exception as re:
            assert False

def test_action():
    file = open(os.path.join(__location__, "tests_resources/action.rlang"), "r")
    for line in file:
        try:
            parser = parse_from_input(line)
            tree = parser.dec()
            print(tree.toStringTree())
        except Exception as re:
            assert False
test_action()

def test_constant():
    file = open(os.path.join(__location__, "tests_resources/constant.rlang"), "r")
    for line in file:
        try:
            parser = parse_from_input(line)
            tree = parser.constant()
        except RecognitionException as re:
            print(re.message)
            assert False

def test_goal():
    file = open(os.path.join(__location__, "tests_resources/goal.rlang"), "r")
    for line in file:
        try:
            parser = parse_from_input(line)
            tree = parser.goal()
        except RecognitionException as re:
            print(re.message)
            assert False

def test_markov_feature():
    file = open(os.path.join(__location__, "tests_resources/markov_feature.rlang"), "r")
    for line in file:
        try:
            parser = parse_from_input(line)
            tree = parser.markov_feature()
        except RecognitionException as re:
            print(re.message)
            assert False


def test_option():
    file = open(os.path.join(__location__, "tests_resources/option.rlang"), "r")
    lines = file.readlines()
    option1 = ''.join(lines[0:4])
    # try:
    #     parser= parse_from_input(option1)
    #     tree = parser.option()
    # except RecognitionException as re:
    #     assert False, "option1 failed"

    option2 = ''.join(lines[4:])
    try:
        parser= parse_from_input(option2)
        tree = parser.dec()
    except RecognitionException as re:
        assert False, "option2 failed"    

def test_effect():
    file = open(os.path.join(__location__, "tests_resources/effect.rlang"), "r")
    lines = file.readlines()
    effect1 = ''.join(lines[0:2])
    try:
        parser= parse_from_input(effect1)
        tree = parser.dec()
    except RecognitionException as re:
        assert False, "effect1 failed"

    effect2 = ''.join(lines[3:6])
    try:
        parser= parse_from_input(effect2)
        tree = parser.dec()
    except RecognitionException as re:
        assert False, "effect2 failed"     

    effect3 = ''.join(lines[7:9])
    try:
        parser= parse_from_input(effect3)
        tree = parser.effect()
    except RecognitionException as re:
        assert False, "effect3 failed"  

def test_policy():
    file = open(os.path.join(__location__, "tests_resources/policy.rlang"), "r")
    lines = file.readlines()
    # policy1 = ''.join(lines[0:1])
    # try:
    #     parser= parse_from_input(policy1)
    #     tree = parser.policy()
    # except RecognitionException as re:
    #     assert False, "policy1 failed"

    policy2 = ''.join(lines[3:])
    try:
        parser= parse_from_input(policy2)
        tree = parser.dec()
    except RecognitionException as re:
        assert False, "policy2 failed" 


def test_incorrect_Factor(): 
    try:
        parser= parse_from_input("Factor position = S[0, 1]")
        tree = parser.dec()
    except RecognitionException as re:
        assert re.message != ""
        offending_token = parser.getTokenErrorDisplay(re.offendingToken)
        expected_token = re.getExpectedTokens().toString(parser.literalNames, parser.symbolicNames)
        assert offending_token == "'='"
        assert expected_token == "':='"



    # assert RLangErrorListener.symbol ==  0

    # print(parseTree.decs().dec(0).factor().getRuleIndex())
    # try:
    #     parseTree = parse_tree_from_input("Factor position = S[0, 1]")
    # except RecognitionException:
    #     print("error")
    # print(parseTree.exception)
    # # print(parseTree.getRuleIndex("Factor"))
    # print(parseTree.toStringTree())
    # print(parseTree)

    # print(type(parseTree))
    # matcher.matchRuleIndex(parseTree, "factor", 5)
    # print(parser.getCurrentToken())
    # print(parser.getExpectedTokensWithinCurrentRule())
    # position = StateFactor([0, 1], "position")
