import peg from "pegjs";
import fs from "fs";
import {format} from "pretty-format";

if (process.argv.length < 3) {
  console.log("Pass a path to a Lua program as an argument.\n (npm start -- programs/smth.lua)");
  process.exit(1);
}

const programPath = process.argv[2];
const outputPath = (() => {
  let pathPieces = programPath.replaceAll("\\", "/").replaceAll(".lua", ".json").split("/");
  return "output/" + pathPieces[pathPieces.length - 1];
})();

let grammar = fs.readFileSync("grammar_stubs/lua.pegjs", "utf8");
let parser = peg.generate(grammar, {"trace": false});

let input = fs.readFileSync(programPath, "utf8");
let ast = parser.parse(input);
fs.writeFileSync(outputPath, JSON.stringify(ast, null, 2));