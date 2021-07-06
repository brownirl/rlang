`pygrun` does not support the `-gui` option, so to build in java run the following:
```
mvn clean
mvn antlr4:antlr4
javac target/generated-sources/antlr4/RLang*.java
cd target/generate-sources/antlr4/
grun RLang predicate -gui
```

To select Python3 as the output language, uncomment the `-Dlanguage` argument in the `pom.xml` and run the following:
```
mvn clean
mvn antlr4:antlr4
```