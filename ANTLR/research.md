## Beginning
[getting started with ANTLRv4](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md)

[easy ANTLR config (no installations required)](https://github.com/antlr/antlr4-tools)

## Generating lexer and parser
Every time we change the grammar we need to run "antlr4 -Dlanguage=JavaScript -lib grammars -o generated -visitor -Xexact-output-dir <grammar_path>" to generate lexer and parser

## Generating trees in terminal:
antlr4-parse <grammar_path> chunk -tree <br />
antlr4-parse <grammar_path> chunk -tokens -trace <br />
antlr4-parse <grammar_path> chunk -gui

example:
```bash
>antlr4-parse grammars\Lua.g4 chunk -tree       
x = 10
y = x + 5
^Z
(chunk:1 (block:1 (stat:2 (varlist:1 (var:1 x)) = (explist:1 (exp:4 (number:1 10)))) (stat:2 (varlist:1 (var:1 y)) = (explist:1 (exp:13 (exp:8 (prefixexp:1 (varOrExp:1 (var:1 x)))) (operatorAddSub:1 +) (exp:4 (number:1 5)))))) <EOF>)
```


## Some example i guess
https://medium.com/dailyjs/compiler-in-javascript-using-antlr-9ec53fd2780f



