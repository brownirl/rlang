To run from `antlr/`:
```
rm classfiles/*
antlr4 RLang*.g4 -o classfiles
javac classfiles/RLang*.java
cd classfiles
grun RLang proposition
```
This workflow is not optimal because you need to delete the contents of `classfiles/` and `cd` in and out of it to run `grun`. We should fix this.