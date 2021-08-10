from antlr4 import *

import sys, os

from antlr4.error.ErrorListener import ConsoleErrorListener
from antlr4.error.ErrorStrategy import BailErrorStrategy
sys.path.append(os.path.abspath("../"))
from rlang.src.language.RLangErrorListener import RLangErrorListener
from rlang.src.language.RLangErrorHandler import RLangErrorHandler
from rlang.src.language.RLangLexer import RLangLexer
from rlang.src.language.RLangParser import RLangParser
from antlr4.tree.ParseTreePatternMatcher import ParseTreePatternMatcher
from antlr4.error.Errors import *

# All tests must begin with 'test_'

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def parse_from_input(input_string):
    input_stream = InputStream(input_string)
    lexer = RLangLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(RLangErrorListener())
    stream = CommonTokenStream(lexer)
    parser = RLangParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(RLangErrorListener())

    return parser

def get_invalid_tokens(input_string):
    try:
        parser = parse_from_input(input_string)
        tree = parser.program()
    except Exception as ex:
        if type(ex.args[0]) == NoViableAltException:
            offending_token = parser.getTokenErrorDisplay(ex.args[0].offendingToken)
            return offending_token, None
        elif type(ex.args[0]) == LexerNoViableAltException:
            offending_token = ex.args[0].input.getText(ex.args[0].startIndex, ex.args[0].startIndex)
            return offending_token, None
        else: 
            offending_token = parser.getTokenErrorDisplay(ex.args[0].offendingToken)
            expected_token = ex.args[0].getExpectedTokens().toString(parser.literalNames, parser.symbolicNames)
            return offending_token, expected_token
    return None


def test_factor():
    file = open(os.path.join(__location__, "tests_resources/factor.rlang"), "r")
    for line in file:
        try:
            parser = parse_from_input(line)
            tree = parser.dec()
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
        except Exception as re:
            assert False

def test_constant():
    file = open(os.path.join(__location__, "tests_resources/constant.rlang"), "r")
    for line in file:
        try:
            parser = parse_from_input(line)
            tree = parser.dec()
        except Exception as re:
            assert False

def test_goal():
    file = open(os.path.join(__location__, "tests_resources/goal.rlang"), "r")
    for line in file:
        try:
            parser = parse_from_input(line)
            tree = parser.dec()
        except Exception as re:
            assert False

def test_markov_feature():
    file = open(os.path.join(__location__, "tests_resources/markov_feature.rlang"), "r")
    for line in file:
        try:
            parser = parse_from_input(line)
            tree = parser.dec()
        except Exception as re:
            assert False

def test_option():
    file = open(os.path.join(__location__, "tests_resources/option.rlang"), "r")
    lines = file.readlines()
    # option1 = ''.join(lines[0:4])
    # try:
    #     parser= parse_from_input(option1)
    #     tree = parser.dec()
    # except Exception as re:
    #     assert False, "option1 failed"

    option2 = ''.join(lines[4:])
    try:
        parser= parse_from_input(option2)
        tree = parser.dec()
    except Exception as re:
        assert False, "option2 failed"    


def test_effect():
    file = open(os.path.join(__location__, "tests_resources/effect.rlang"), "r")
    lines = file.readlines()
    effect1 = ''.join(lines[0:2])
    try:
        parser= parse_from_input(effect1)
        tree = parser.dec()
    except Exception as re:
        assert False, "effect1 failed"

    effect2 = ''.join(lines[3:6])
    try:
        parser= parse_from_input(effect2)
        tree = parser.dec()
    except Exception as re:
        assert False, "effect2 failed"     

    effect3 = ''.join(lines[7:12])
    try:
        parser= parse_from_input(effect3)
        tree = parser.effect()
    except Exception as re:
        assert False, "effect3 failed"  

def test_policy():
    file = open(os.path.join(__location__, "tests_resources/policy.rlang"), "r")
    lines = file.readlines()
    policy1 = ''.join(lines[:2])
    try:
        parser= parse_from_input(policy1)
        tree = parser.policy()
    except Exception as re:
        assert False, "policy1 failed"

    policy2 = ''.join(lines[3:])
    try:
        parser= parse_from_input(policy2)
        tree = parser.dec()
    except Exception as re:
        assert False, "policy2 failed" 

def test_invalid_action():
    file = open(os.path.join(__location__, "tests_resources/invalid_tests/invalid_action.rlang"), "r")
    lines = file.readlines()
    
    offending_token, expected_token = get_invalid_tokens(lines[0])
    assert offending_token == "'['"
    assert expected_token == "INTEGER"

    offending_token, expected_token = get_invalid_tokens(lines[1])
    assert offending_token == "'=='"
    assert expected_token == "NL"

    offending_token, expected_token = get_invalid_tokens(lines[2])
    assert offending_token == "'1.0'"
    assert expected_token == "INTEGER"

    offending_token, expected_token = get_invalid_tokens(lines[3])
    assert offending_token == "'S'"
    assert expected_token == "IDENTIFIER"

def test_invalid_constant():
    file = open(os.path.join(__location__, "tests_resources/invalid_tests/invalid_constant.rlang"), "r")
    lines = file.readlines()

    offending_token, expected_token = get_invalid_tokens(lines[0])
    assert offending_token == "@"
    assert expected_token == None

    offending_token, expected_token = get_invalid_tokens(lines[1])
    assert offending_token == "'+'"
    assert expected_token == None
    
    offending_token, expected_token = get_invalid_tokens(lines[2])
    assert offending_token == "'Effect'"
    assert expected_token == "NL"
    
    offending_token, expected_token = get_invalid_tokens(lines[3])
    assert offending_token == "'-='"
    print(expected_token)
    assert expected_token == "{'S'', 'S', 'A', 'not', 'True', 'False', '[', '(', '-', IDENTIFIER, DECIMAL, INTEGER}"

def test_invalid_factor():
    file = open(os.path.join(__location__, "tests_resources/invalid_tests/invalid_factor.rlang"), "r")
    lines = file.readlines()
    
    offending_token, expected_token = get_invalid_tokens(lines[0])
    assert offending_token == "'Sinventory'"
    assert expected_token == "'S'"

    offending_token, expected_token = get_invalid_tokens(lines[1])
    assert offending_token == "'+'"
    assert expected_token == "NL"

    offending_token, expected_token = get_invalid_tokens(lines[2])
    assert offending_token == "'*'"
    assert expected_token == "']'"

def test_invalid_feature():
    file = open(os.path.join(__location__, "tests_resources/invalid_tests/invalid_feature.rlang"), "r")
    lines = file.readlines()
    
    offending_token, expected_token = get_invalid_tokens(lines[0])
    assert offending_token == "'=='"
    assert expected_token == "NL"
    
    offending_token, expected_token = get_invalid_tokens(lines[1])
    assert offending_token == "'['"
    assert expected_token == None

def test_invalid_goal():
    file = open(os.path.join(__location__, "tests_resources/invalid_tests/invalid_goal.rlang"), "r")
    lines = file.readlines()

    offending_token, expected_token = get_invalid_tokens(lines[0])
    assert offending_token == "'Effect'"
    assert expected_token == "IDENTIFIER"

    offending_token, expected_token = get_invalid_tokens(lines[1])
    assert offending_token == "'and'"
    assert expected_token == None

    offending_token, expected_token = get_invalid_tokens(lines[2])
    assert offending_token == "'+'"
    assert expected_token == "NL"

def test_invalid_effect():
    file = open(os.path.join(__location__, "tests_resources/invalid_tests/invalid_effect.rlang"), "r")
    lines = file.readlines()

    offending_token, expected_token = get_invalid_tokens("".join(lines[:5]))
    print(offending_token)
    assert offending_token == "'Feature'"
    assert expected_token == "{DEDENT, NL, 'Constant', 'Reward', 'S'', IDENTIFIER}"

    offending_token, expected_token = get_invalid_tokens("".join(lines[6:8]))
    assert offending_token == "'\\n'"
    assert expected_token == "INDENT"

    offending_token, expected_token = get_invalid_tokens("".join(lines[9:11]))
    assert offending_token == "'ten'"
    assert expected_token == "{'-', DECIMAL, INTEGER}"
    
    offending_token, expected_token = get_invalid_tokens("".join(lines[12:16]))
    assert offending_token == "':'"
    assert expected_token == None

test_invalid_effect()

def test_invalid_option():
    file = open(os.path.join(__location__, "tests_resources/invalid_tests/invalid_option.rlang"), "r")
    lines = file.readlines()

    option1 = "".join(lines[:5])
    offending_token, expected_token = get_invalid_tokens(option1)
    assert offending_token == "'newLine'"
    assert expected_token == "IDENTIFIER"

    offending_token, expected_token = get_invalid_tokens("".join(lines[6:9]))
    assert offending_token == "'Execute'"
    assert expected_token == "'init'"

def test_invalid_policy():
    file = open(os.path.join(__location__, "tests_resources/invalid_tests/invalid_policy.rlang"), "r")
    lines = file.readlines()

    get_invalid_tokens("".join(lines[:6]))
    offending_token, expected_token = get_invalid_tokens("".join(lines[:6]))
    assert offending_token == "'elif'"
    assert expected_token == "{DEDENT, 'Execute', 'if'}"

    get_invalid_tokens("".join(lines[6:11]))
    offending_token, expected_token = get_invalid_tokens("".join(lines[6:11]))
    assert offending_token == "'init'"
    assert expected_token == "{DEDENT, 'Execute', 'if'}"

# test_invalid_policy()

def test_invalid_predicate():
    file = open(os.path.join(__location__, "tests_resources/invalid_tests/invalid_predicate.rlang"), "r")
    lines = file.readlines()

    offending_token, expected_token = get_invalid_tokens(lines[0])
    assert offending_token == "'in'"
    assert expected_token == "{'S'', 'S', 'A', 'not', 'True', 'False', '[', '(', '-', IDENTIFIER, DECIMAL, INTEGER}"

    offending_token, expected_token = get_invalid_tokens(lines[1])
    assert offending_token == "'+'"
    assert expected_token == "NL"

def test_misc():
    file = open(os.path.join(__location__, "tests_resources/miscellaneous.rlang"), "r")
    lines = file.readlines()

    for line in lines[:2]:
        try:
            parser = parse_from_input(line)
            tree = parser.imports()
        except Exception as re:
            assert False
    
    for line in lines[4:]:
        try:
            parser = parse_from_input(line)
            tree = parser.arithmetic_exp()
        except Exception as re:
            assert False