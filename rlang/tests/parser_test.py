from antlr4 import *

import sys, os

from antlr4.error.ErrorListener import ConsoleErrorListener
sys.path.append(os.path.abspath("../"))
from rlang.src.language.RLangErrorHandler import MissingTokenException, RLangErrorHandler, UnwantedTokenException
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
    stream = CommonTokenStream(lexer)
    parser = RLangParser(stream)
    parser._errHandler = RLangErrorHandler()
    # parser.removeErrorListeners()
    # parser.addErrorListener(RLangErrorListener())

    return parser

def get_invalid_tokens(input_string):
    try:
        parser = parse_from_input(input_string)
        tree = parser.program()
    except (InputMismatchException, UnwantedTokenException, MissingTokenException) as e:
        offending_token = parser.getTokenErrorDisplay(e.offendingToken)
        expected_token = e.getExpectedTokens().toString(parser.literalNames, parser.symbolicNames)
        return offending_token, expected_token
    except NoViableAltException as e:
        offending_token = parser.getTokenErrorDisplay(e.offendingToken)
        return offending_token, None
    except Exception as e:
        print(type(e))
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
            print(tree.toStringTree())
        except Exception as re:
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
    #TODO: add more
    pass

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


def test_invalid_option():
    file = open(os.path.join(__location__, "tests_resources/invalid_tests/invalid_option.rlang"), "r")
    lines = file.readlines()

    option1 = "".join(lines[:5])
    print(get_invalid_tokens(option1))
    offending_token, expected_token = get_invalid_tokens(option1)
    assert offending_token == "'newLine'"
    assert expected_token == "IDENTIFIER"

    # offending_token, expected_token = get_invalid_tokens("".join(lines[6:10]))
    # assert offending_token == "'use'"
    # assert expected_token == "DEDENT"

    offending_token, expected_token = get_invalid_tokens("".join(lines[11:14]))
    assert offending_token == "'Execute'"
    assert expected_token == "'init'"

def test_invalid_policy():
    file = open(os.path.join(__location__, "tests_resources/invalid_tests/invalid_policy.rlang"), "r")
    lines = file.readlines()

    offending_token, expected_token = get_invalid_tokens("".join(lines[:6]))
    assert offending_token == "'elif'"
    assert expected_token == "{DEDENT, 'Execute', 'if'}"

    offending_token, expected_token = get_invalid_tokens("".join(lines[6:11]))
    assert offending_token == "'init'"
    assert expected_token == "{DEDENT, 'Execute', 'if'}"

    # offending_token, expected_token = get_invalid_tokens("".join(lines[13:17]))
    # assert offending_token == "'if'"
    # assert expected_token == "{DEDENT, 'Execute', 'if'}"


# test_invalid_policy()

def test_invalid_predicate():
    pass

