import { Token } from "./scanner";

const builtins = [
  "pairs",
  "ipairs",
  "print"
]

export class Formatter {
  column = 0;
  line = 0;

  constructor() {

  }

  format(token: Token) {
    let result: string = "";
    while (this.line < token.line) {
      this.line++;
      this.column = 0;
      result += "<br>\n";
    }
    while (this.column < token.column) {
      this.column++;
      result += "&nbsp";
    }
    this.column = token.column + token.value.length;

    let formatting: string = token.kind;
    if (token.kind == "identifier") {
      if (token.value.startsWith("__")) {
        formatting = "__identifier";
      }
      else if (builtins.includes(token.value)) {
        formatting = "builtin";
      }
    }

    return result + `<span class=${formatting}>${token.value}</span>`;
  }
}