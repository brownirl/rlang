## Advice for working on the lexer and parser grammar

It's easy to use `grun` to test out grammar productions, 
but `grun` only works on java files. Our target build is 
in Python 3, but `pygrun` (the Python analog to `grun`) 
does not support the `-gui` option, so to build Lexer/Parser 
in java temporarily to use `grun` do the following:
1. In `antlr/pom.xml` comment out the entire `<configuration>` 
tag on line 32.
2. Run from the `antlr/` directory:
```
mvn clean
mvn antlr4:antlr4
javac target/generated-sources/antlr4/RLang*.java
cd target/generate-sources/antlr4/
grun RLang predicate -gui
```

Please un-comment the `<configuration>` tag before pushing 
and run `mvn clean` from the root directory before pushing.