## Advice for working on the lexer and parser grammar

~~It's easy to use `grun` to test out grammar productions, 
but `grun` only works on java files. Our target build is 
in Python 3, but `pygrun` (the Python analog to `grun`) 
does not support the `-gui` option, so to build Lexer/Parser 
in java temporarily to use `grun` do the following:~~
1. ~~In `antlr/pom.xml` comment out the entire `<configuration>` 
tag on line 32.~~
2. ~~Run from the `antlr/` directory:~~
```
mvn clean
mvn antlr4:antlr4
javac target/generated-sources/antlr4/RLang*.java
cd target/generate-sources/antlr4/
grun RLang predicate -gui
```

~~Please un-comment the `<configuration>` tag before pushing 
and run `mvn clean` from the root directory before pushing.~~

### Update

After adding `antlr-denter` to the lexer to support Pythonic
 indentation, we can no longer compile using `javac`...
 so no more `grun`. Instead, use `pygrun` with the `-t` option
 ~~and pipe it into`prettyprint.py`~~ from `rlang/language/`:
```
pygrun RLang program -t
```
~~`prettyprint.py` probably should not make it into the final
 package (or it at least should be in a utils folder), but
 it's helpful for developing purposes. It runs [`nltk` under
 the hood to pretty-print](http://www.nltk.org/howto/tree.html) ASTs.~~

### Update 7/20/21

~~Turns out nltk's prettyprint isn't perfect and doesn't always
display nodes in the correct order... keep that in mind.~~

Also, explicit relative imports are necessary in Python3 packages,
but Antlr4 generates code with *implicit* relative imports. I wrote
up a fix [here](https://github.com/antlr/antlr4/issues/3230). It
involves modifying your `pygrun` file by adding two new lines of code
before the lexer `__import__` statement around lines 105:
```python
p = os.path.basename(os.getcwd())
globals().update({'__package__': p})
```
With this fix, `pygrun` should run normally.

### Update 9/8/21

`prettyprint.py` wasn't up to snuff so I nixed it. Just run `pygrun RLang program -t` instead.