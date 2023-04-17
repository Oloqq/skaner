// 🙂
import fs from "fs"
import antlr4 from "antlr4"
import LuaLexer from "./generated/LuaLexer.js";
import LuaParser from "./generated/LuaParser.js";

const input = fs.readFileSync("./programs/player.lua").toString();

const chars = new antlr4.InputStream(input);
const lexer = new LuaLexer(chars);

lexer.strictMode = false; // do not use js strictMode

const tokens = new antlr4.CommonTokenStream(lexer);
const parser = new LuaParser(tokens);
const tree = parser.chunk()

console.log(tree.toStringTree(parser.ruleNames));