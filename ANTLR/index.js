// 🙂🙂🙂🙂🙂🙂🙂🙂🙂🙂🙂🙂🙂🙂🙂🙂🙂 pls help 
const fs = require("fs")

const antlr4 = require('antlr4');
const LuaLexer = require('.\\generated\\LuaLexer.js');
const LuaParser = require('.\\generated\\LuaParser.js');

const input = fs.readFileSync(".\\programs\\Player.lua", "utf-8");

const chars = new antlr4.InputStream(input);
const lexer = LuaLexer.LuaLexer(chars);

lexer.strictMode = false; // do not use js strictMode

const tokens = new antlr4.CommonTokenStream(lexer);
const parser = new LuaParser.LuaParser(tokens);
const tree = parser.program();

console.log(tree.toStringTree(parser.ruleNames));