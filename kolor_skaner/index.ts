// const argv = process.argv.slice(2)

const filename = "./test/bruh.lua";

import fs from "fs";
import { Formatter } from "./src/formatter";
import { Scanner } from "./src/scanner";

const text = fs.readFileSync(filename).toString();
const scanner = new Scanner(text);
const formatter = new Formatter();

(function formatAll() {
  let result = `
  <style>
  html {
    font-family: monospace;
  }
  .identifier {
    color: blue
  }
  .numberLiteral {
    color: orange
  }
  .stringLiteral {
    color: green
  }
  .keyword {
    color: purple
  }
  .builtin {
    color: cyan
  }
  .__identifier {
    color: darkblue
  }
  .comment {
    color: gray
  }
  </style>
  `;

  while (!scanner.eof()) {
    const token = scanner.next();
    if (token.kind == "Unexpected character") {
      console.log(token);
    }

    const html = formatter.format(token);
    result += html;
  }

  // console.log(result);
  fs.writeFileSync("./test/output.html", result);
})();