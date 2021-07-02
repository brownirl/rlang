parser grammar RLangParser;

options {
    tokenVocab=RLangLexer;
}

predicate: PREDICATE IDENTIFIER ASSIGN IDENTIFIER;