export class Token {
  kind: string;
  value: string;
  line: number;
  column: number;

  constructor(kind: string, value: string, row: number, column: number) {
    this.kind = kind;
    this.value = value;
    this.line = row;
    this.column = column;
  }
}

function alpha(x: string): boolean {
  if (x.length > 1) throw "Expected single char";
  return (x >= "a" && x <= "z") || (x >= "A" && x <= "Z");
}

function numeric(x: string): boolean {
  if (x.length > 1) throw "Expected single char";
  return (x >= "0" && x <= "9");
}

function alphanumeric(x: string): boolean {
  if (x.length > 1) throw "Expected single char";
  return alpha(x) || numeric(x);
}

const keywords = [
  "local",
  "if",
  "then",
  "elseif",
  "else",
  "end",
  "function",
  "do"
]

export class Scanner {
  source: string;
  cursor = 0;
  row: number = 0;
  column: number = 0;

  constructor(source: string) {
    this.source = source;
  }

  eof(): boolean {
    return this.cursor >= this.source.length;
  }

  private current(): string {
    return this.source.charAt(this.cursor);
  }

  private advance(): void {
    this.cursor++;
  }

  next(): Token {
    let kind: string;
    let start = this.cursor;

    if (numeric(this.current())) {
      kind = "numberLiteral";
      while (numeric(this.current())) {
        this.advance();
      }
    }
    else if (alpha(this.current()) || this.current() == "_") {
      while (alphanumeric(this.current()) || this.current() == "_") {
        this.advance();
      }
      if (keywords.includes(this.source.substring(start, this.cursor))) {
        kind = "keyword";
      }
      else {
        kind = "identifier";
      }
    }
    else if (this.current() == '(') {
      kind = "openParen";
      this.advance();
    }
    else if (this.current() == ')') {
      kind = "closeParen";
      this.advance();
    }
    else if (this.current() == '\r') {
      this.advance();
      if (this.current() != '\n') {
        throw "no \\n after \\r ??????????";
      }
      this.row++;
      this.column = 0;
      while ([' ', '\t'].includes(this.current())) {
        this.column++;
        this.cursor++;
      }
      return this.next();
    }
    else if (this.current() == '\n') {
      this.advance();
      this.row++;
      this.column = 0;
      while ([' ', '\t'].includes(this.current())) {
        this.column++;
        this.cursor++;
      }
      return this.next();
    }
    else if (this.current() == ' ') {
      this.advance();
      this.column++;
      return this.next();
    }
    else if (['"', "'"].includes(this.current())) {
      let quote = this.current();
      kind = "stringLiteral";
      this.advance();
      while (this.current() != quote) { // omitting quote escaping
        this.advance();
      }
      this.advance();
    }
    else if (["+", "-", "/", "*"].includes(this.current())) {
      kind = "infixOperator";
      this.advance();
    }
    else if (this.current() == "=") {
      this.advance();
      if (this.current() == "=") {
        this.advance();
        kind = "comparison";
      }
      else {
        kind = "assignment";
      }
    }
    else {
      kind = "wtf dude";
      this.advance();
    }

    const token = new Token(kind, this.source.substring(start, this.cursor), this.row, this.column);
    this.column += (this.cursor - start);
    return token
  }
}