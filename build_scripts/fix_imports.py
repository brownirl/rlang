with open('rlang/src/language/antlr/RLangLexer.py', 'rt') as lexer_file:
    data = lexer_file.read()
    data = data.replace('from RLangParser import RLangParser', 'from .RLangParser import RLangParser')

with open('rlang/src/language/antlr/RLangLexer.py', 'wt') as lexer_file:
    lexer_file.write(data)
