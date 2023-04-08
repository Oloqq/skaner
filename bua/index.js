import peg from "pegjs";
import fs from "fs";
import { program } from "commander";

program
  .name("bua-compiler")
  .version("0.0.1")
  .description("Bread")
  .argument("<source>", "Path to the Bua program")
  .option("-t --trace", "Trace the parsing process")

program.parse();

const sourcePath = program.args[0];
const outputPath = (() => {
  let pathPieces = sourcePath.replaceAll("\\", "/").replaceAll(".lua", ".json").split("/");
  return "output/" + pathPieces[pathPieces.length - 1];
})();

let grammar = fs.readFileSync("grammar/lua.pegjs", "utf8");
let parser = peg.generate(grammar, {"trace": program.opts()["trace"]});

let input = fs.readFileSync(sourcePath, "utf8");
let ast = parser.parse(input);
fs.writeFileSync(outputPath, JSON.stringify(ast, null, 2));