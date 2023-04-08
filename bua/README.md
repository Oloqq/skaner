### extension highlighting BNF
Vallentin.vscode-bnf

### lua grammar
http://parrot.github.io/parrot-docs0/0.4.7/html/languages/lua/doc/lua51.bnf.html

# Parsers
## Node
- https://stackoverflow.com/questions/43577617/generate-a-parser-from-programatically-generated-bnf
    - ppl mention only haskell tools fuck them

- https://www.npmjs.com/package/bnf-parser
    - maintained (update in march)
    - uses BNF with some extensions

- https://www.npmjs.com/package/bnf
    - seems simple and nice but prolly not maintained

- https://pegjs.org/
    - includes code generation
    - can be tested in the browser https://pegjs.org/online

- https://github.com/Chevrotain/chevrotain
    - "It is important to note that Chevrotain is NOT a parser generator. It solves the same kind of problems as a parser generator, just without any code generation"
    - comparison https://chevrotain.io/docs/FAQ.html#VS_GENERATORS
    - article/guide + extensive example https://tomassetti.me/parsing-in-javascript/#chevrotain

### Peg.js
https://pegjs.org/documentation

Extension for highlighting grammar: SirTobi.pegjs-language

## Tools
### generate grammar documentation
grammkit -t md .\grammar\lua.pegjs

### save parser's trace to a file
npm start -- .\programs\table.lua -t > .\grammar\debug.txt