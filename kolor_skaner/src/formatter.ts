import { Token } from "./scanner";

export class Formatter {
  column = 0;
  line = 0;

  constructor() {

  }

  format(token: Token) {
    let result: string = "";
    while (this.line < token.row) {
      this.line++;
      this.column = 0;
      result += "<br>\n";
    }
    while (this.column < token.column) {
      this.column++;
      result += "&nbsp";
    }
    this.column = token.column + token.value.length;

    return result + `<span class=${token.kind}>${token.value}</span>`;
  }
}