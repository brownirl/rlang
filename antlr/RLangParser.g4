parser grammar RLangParser;

options {
    tokenVocab=RLangLexer;
}

proposition: PROPOSITION IDENTIFIER ASSIGN IDENTIFIER;