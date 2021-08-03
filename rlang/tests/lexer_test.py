from antlr4 import CommonTokenStream, InputStream, Token
import sys, os
sys.path.append(os.path.abspath("../"))
from rlang.src.language.RLangLexer import RLangLexer

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def tokenize_from_string(input_string):
    input_stream = InputStream(input_string)
    lexer = RLangLexer(input_stream)
    # lexer.addErrorListener(MyErrorListener)
    stream = CommonTokenStream(lexer)
    stream.fill()
    return stream.tokens


# All tests must begin with 'test_'


def test_predicate_token():
    file = open(os.path.join(__location__, "tests_resources/predicate.rlang"), "r")
    for line in file:
        tokens = tokenize_from_string(line)
        assert tokens[0].type == RLangLexer.PREDICATE
        assert tokens[1].type == RLangLexer.IDENTIFIER
        assert tokens[2].type == RLangLexer.BIND
    
    file.seek(0)

    lines = file.readlines()
    tokens = tokenize_from_string(lines[1])
    assert tokens[3].type == RLangLexer.IDENTIFIER
    assert tokens[4].type == RLangLexer.NOT_EQ
    assert tokens[5].type == RLangLexer.IDENTIFIER
    assert tokens[6].type == RLangLexer.AND
    assert tokens[7].type == RLangLexer.IDENTIFIER
    assert tokens[8].type == RLangLexer.NOT_EQ
    assert tokens[9].type == RLangLexer.IDENTIFIER
    assert len(tokens) == 12

    tokens = tokenize_from_string(lines[4])
    assert tokens[3].type == RLangLexer.NOT
    assert tokens[4].type == RLangLexer.L_PAR
    assert tokens[5].type == RLangLexer.TRUE
    assert tokens[6].type == RLangLexer.R_PAR
    assert len(tokens) == 9

    tokens = tokenize_from_string(lines[5])
    assert tokens[3].type == RLangLexer.FALSE
    assert len(tokens) == 6

    tokens = tokenize_from_string(lines[2])
    assert tokens[3].type == RLangLexer.IDENTIFIER
    assert tokens[4].type == RLangLexer.AND
    assert tokens[5].type == RLangLexer.IDENTIFIER
    assert tokens[6].type == RLangLexer.OR
    assert tokens[7].type == RLangLexer.IDENTIFIER
    assert tokens[8].type == RLangLexer.AND
    assert tokens[9].type == RLangLexer.INTEGER
    assert tokens[10].type == RLangLexer.EQ_TO
    assert tokens[11].type == RLangLexer.INTEGER
    assert len(tokens) == 14

    tokens = tokenize_from_string(lines[6])
    assert tokens[3].type == RLangLexer.IDENTIFIER
    assert tokens[4].type == RLangLexer.IN
    assert tokens[5].type == RLangLexer.IDENTIFIER
    assert len(tokens) == 8

    file.close()

def test_feature_token():
    file = open(os.path.join(__location__, "tests_resources/feature.rlang"), "r")
    for line in file:
        tokens = tokenize_from_string(line)
        assert tokens[0].type == RLangLexer.FEATURE
        assert tokens[1].type == RLangLexer.IDENTIFIER
        assert tokens[2].type == RLangLexer.BIND
        assert tokens[3].type == RLangLexer.IDENTIFIER 
    
    file.seek(0)

    lines = file.readlines()
    tokens = tokenize_from_string(lines[0])
    assert tokens[4].type == RLangLexer.L_BRK
    assert tokens[5].type == RLangLexer.INTEGER
    assert tokens[6].type == RLangLexer.R_BRK
    assert len(tokens) == 9

    tokens = tokenize_from_string(lines[2])
    assert tokens[4].type == RLangLexer.L_BRK
    assert tokens[5].type == RLangLexer.INTEGER
    assert tokens[6].type == RLangLexer.COL
    assert tokens[7].type == RLangLexer.INTEGER
    assert tokens[8].type == RLangLexer.R_BRK
    assert len(tokens) == 11

    file.close()

def test_factor_token():
    file = open(os.path.join(__location__, "tests_resources/factor.rlang"), "r")
    for line in file:
        tokens = tokenize_from_string(line)
        assert tokens[0].type == RLangLexer.FACTOR
        assert tokens[1].type == RLangLexer.IDENTIFIER
        assert tokens[2].type == RLangLexer.BIND
        assert tokens[3].type == RLangLexer.S

    file.seek(0)

    lines = file.readlines()
    tokens = tokenize_from_string(lines[3])
    assert tokens[4].type == RLangLexer.L_BRK
    assert tokens[5].type == RLangLexer.INTEGER
    assert tokens[6].type == RLangLexer.COL
    assert tokens[7].type == RLangLexer.MINUS
    assert tokens[8].type == RLangLexer.INTEGER
    assert tokens[9].type == RLangLexer.R_BRK
    assert len(tokens) == 12
    
    file.close()

def test_goal_token():
    file = open(os.path.join(__location__, "tests_resources/goal.rlang"), "r")
    lines = file.readlines()

    tokens = tokenize_from_string(lines[0])
    assert tokens[0].type == RLangLexer.GOAL
    assert tokens[1].type == RLangLexer.IDENTIFIER
    assert tokens[2].type == RLangLexer.GT_EQ
    assert tokens[3].type == RLangLexer.INTEGER
    assert len(tokens) == 6

    tokens = tokenize_from_string(lines[1])
    assert tokens[0].type == RLangLexer.GOAL
    assert tokens[1].type == RLangLexer.IDENTIFIER
    assert len(tokens) == 4

    tokens = tokenize_from_string(lines[2])
    assert tokens[0].type == RLangLexer.GOAL
    assert tokens[1].type == RLangLexer.IDENTIFIER
    assert tokens[2].type == RLangLexer.EQ_TO
    assert tokens[3].type == RLangLexer.INTEGER
    print(tokens[5].type)
    assert len(tokens) == 6

    file.close()

def test_constant_token():
    file = open(os.path.join(__location__, "tests_resources/constant.rlang"), "r")
    for line in file:
        tokens = tokenize_from_string(line)
        assert tokens[0].type == RLangLexer.CONSTANT
        assert tokens[1].type == RLangLexer.IDENTIFIER

    file.seek(0)
    lines = file.readlines()
    tokens = tokenize_from_string(lines[1])
    assert tokens[3].type == RLangLexer.L_BRK
    assert tokens[4].type == RLangLexer.INTEGER
    assert tokens[5].type == RLangLexer.COM
    assert tokens[6].type == RLangLexer.INTEGER
    assert tokens[7].type == RLangLexer.R_BRK
    assert len(tokens) == 10

    tokens = tokenize_from_string(lines[3])
    assert tokens[3].type == RLangLexer.MINUS
    assert tokens[4].type == RLangLexer.DECIMAL

    tokens = tokenize_from_string(lines[4])
    assert tokens[3].type == RLangLexer.DECIMAL
    
    tokens = tokenize_from_string(lines[5])
    assert tokens[2].type == RLangLexer.BIND
    assert tokens[3].type == RLangLexer.INTEGER
    assert tokens[4].type == RLangLexer.TIMES
    assert tokens[5].type == RLangLexer.DECIMAL

    tokens = tokenize_from_string(lines[6])
    assert tokens[3].type == RLangLexer.INTEGER
    assert tokens[4].type == RLangLexer.DIVIDE
    assert tokens[5].type == RLangLexer.DECIMAL

    file.close()

def test_action_token():
    file = open(os.path.join(__location__, "tests_resources/action.rlang"), "r")
    lines = file.readlines()
    tokens = tokenize_from_string(lines[0])
    assert tokens[0].type == RLangLexer.ACTION
    assert tokens[1].type == RLangLexer.IDENTIFIER
    assert tokens[2].type == RLangLexer.BIND
    assert tokens[3].type == RLangLexer.L_BRK
    assert tokens[4].type == RLangLexer.INTEGER
    assert tokens[5].type == RLangLexer.COM
    assert tokens[6].type == RLangLexer.INTEGER
    assert tokens[7].type == RLangLexer.COM
    assert tokens[8].type == RLangLexer.INTEGER
    assert tokens[9].type == RLangLexer.R_BRK
    assert len(tokens) == 12

    file.close()

def test_effect_token():
    file = open(os.path.join(__location__, "tests_resources/effect.rlang"), "r")
    lines = file.readlines()

    tokens = tokenize_from_string(lines[0])
    assert tokens[0].type == RLangLexer.EFFECT
    assert tokens[1].type == RLangLexer.A
    assert tokens[2].type == RLangLexer.EQ_TO
    assert tokens[3].type == RLangLexer.IDENTIFIER
    assert tokens[4].type == RLangLexer.COL
    assert len(tokens) == 7

    tokens = tokenize_from_string(lines[1])
    assert tokens[0].type == RLangLexer.INDENT
    assert tokens[1].type == RLangLexer.IDENTIFIER
    assert tokens[2].type == RLangLexer.PLUS_EQ
    assert tokens[3].type == RLangLexer.L_BRK
    assert tokens[4].type == RLangLexer.INTEGER
    assert tokens[5].type == RLangLexer.COM
    assert tokens[6].type == RLangLexer.INTEGER
    assert tokens[7].type == RLangLexer.R_BRK
    # should NL be before DEDENT? / does order matter?
    assert tokens[8].type == RLangLexer.NL
    assert tokens[9].type == RLangLexer.DEDENT
    assert len(tokens) == 11

    tokens = tokenize_from_string(lines[3])
    assert tokens[0].type == RLangLexer.EFFECT
    assert tokens[1].type == RLangLexer.IDENTIFIER
    assert tokens[2].type == RLangLexer.COL
    assert len(tokens) == 5
    
    tokens = tokenize_from_string(lines[4])
    assert tokens[0].type == RLangLexer.INDENT
    assert tokens[1].type == RLangLexer.IDENTIFIER
    assert tokens[2].type == RLangLexer.PLUS_EQ
    assert tokens[3].type == RLangLexer.INTEGER
    assert tokens[4].type == RLangLexer.NL
    assert tokens[5].type == RLangLexer.DEDENT
    assert len(tokens) == 7

    tokens = tokenize_from_string(lines[5])
    assert tokens[0].type == RLangLexer.INDENT
    assert tokens[1].type == RLangLexer.IDENTIFIER
    assert tokens[2].type == RLangLexer.L_BRK
    assert tokens[3].type == RLangLexer.INTEGER
    assert tokens[4].type == RLangLexer.R_BRK
    assert tokens[5].type == RLangLexer.PLUS_EQ
    assert tokens[6].type == RLangLexer.INTEGER
    assert tokens[7].type == RLangLexer.NL
    assert tokens[8].type == RLangLexer.DEDENT
    assert len(tokens) == 10

    tokens = tokenize_from_string(lines[8])
    assert tokens[0].type == RLangLexer.INDENT
    assert tokens[1].type == RLangLexer.REWARD
    assert tokens[2].type == RLangLexer.INTEGER
    assert tokens[3].type == RLangLexer.NL
    assert tokens[4].type == RLangLexer.DEDENT
    assert len(tokens) == 6

    file.close()

def test_policy_token():
    file = open(os.path.join(__location__, "tests_resources/policy.rlang"), "r")
    lines = file.readlines()

    tokens = tokenize_from_string(lines[3])
    assert tokens[0].type == RLangLexer.POLICY
    assert tokens[1].type == RLangLexer.IDENTIFIER
    assert tokens[2].type == RLangLexer.COL

    tokens = tokenize_from_string(lines[4])
    assert tokens[0].type == RLangLexer.INDENT
    assert tokens[1].type == RLangLexer.IF
    assert tokens[2].type == RLangLexer.IDENTIFIER
    assert tokens[3].type == RLangLexer.COL
    assert tokens[4].type == RLangLexer.NL
    assert tokens[5].type == RLangLexer.DEDENT

    tokens = tokenize_from_string(lines[6])
    assert tokens[0].type == RLangLexer.INDENT
    assert tokens[1].type == RLangLexer.ELIF
    assert tokens[2].type == RLangLexer.IDENTIFIER
    assert tokens[3].type == RLangLexer.GT_EQ
    assert tokens[4].type == RLangLexer.INTEGER
    assert tokens[5].type == RLangLexer.COL
    assert tokens[6].type == RLangLexer.NL
    assert tokens[7].type == RLangLexer.DEDENT

    tokens = tokenize_from_string(lines[7])
    assert tokens[0].type == RLangLexer.INDENT
    assert tokens[1].type == RLangLexer.EXECUTE
    assert tokens[2].type == RLangLexer.IDENTIFIER
    assert tokens[3].type == RLangLexer.NL
    assert tokens[4].type == RLangLexer.DEDENT

    tokens = tokenize_from_string(lines[8])
    assert tokens[0].type == RLangLexer.INDENT
    assert tokens[1].type == RLangLexer.ELSE
    assert tokens[2].type == RLangLexer.COL
    assert tokens[3].type == RLangLexer.NL
    assert tokens[4].type == RLangLexer.DEDENT

    file.close()

def test_option_token():
    file = open(os.path.join(__location__, "tests_resources/option.rlang"), "r")
    lines = file.readlines()

    tokens = tokenize_from_string(lines[0])
    assert tokens[0].type == RLangLexer.OPTION
    assert tokens[1].type == RLangLexer.IDENTIFIER
    assert tokens[2].type == RLangLexer.COL

    tokens = tokenize_from_string(lines[1])
    assert tokens[0].type == RLangLexer.INDENT
    assert tokens[1].type == RLangLexer.INIT
    assert tokens[2].type == RLangLexer.L_PAR
    assert tokens[3].type == RLangLexer.TRUE
    assert tokens[4].type == RLangLexer.R_PAR
    assert tokens[5].type == RLangLexer.NL
    assert tokens[6].type == RLangLexer.DEDENT

    # tokens = tokenize_from_string(lines[2])
    # assert tokens[0].type == RLangLexer.INDENT
    # assert tokens[1].type == RLangLexer.FIND
    # assert tokens[2].type == RLangLexer.NL
    # assert tokens[3].type == RLangLexer.DEDENT
    # assert len(tokens) == 5

    tokens = tokenize_from_string(lines[3])
    assert tokens[0].type == RLangLexer.INDENT
    assert tokens[1].type == RLangLexer.UNTIL
    assert tokens[2].type == RLangLexer.IDENTIFIER
    assert tokens[3].type == RLangLexer.NL
    assert tokens[4].type == RLangLexer.DEDENT
    assert len(tokens) == 6

    tokens = tokenize_from_string(lines[7])
    assert tokens[0].type == RLangLexer.INDENT
    assert tokens[1].type == RLangLexer.EXECUTE
    assert tokens[2].type == RLangLexer.IDENTIFIER
    assert tokens[3].type == RLangLexer.NL
    assert tokens[4].type == RLangLexer.DEDENT
    assert len(tokens) == 6

    file.close()

    def test_markov_feature():
        file = open(os.path.join(__location__, "tests_resources/markov_feature.rlang"), "r")
        lines = file.readlines()
        for line in file:
            tokens = tokenize_from_string(line)
            assert tokens[0].type == RLangLexer.MARKOVFEATURE
            assert tokens[1].type == RLangLexer.IDENTIFIER
            assert tokens[2].type == RLangLexer.BIND
        
        file.seek(0)
        lines = file.readlines()
        tokens = tokenize_from_string(lines[1])
        assert tokens[3].type == RLangLexer.S_PRIME
        assert tokens[4].type == RLangLexer.MINUS
        assert tokens[5].type == RLangLexer.S
        assert len(tokens) == 8

    file.close()
        
    
    

