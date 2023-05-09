from tuaVisitor import tuaVisitor as TuaVisitor
from tuaLexer import tuaLexer
from tuaParser import tuaParser
from antlr4 import *

def main():
    # Read input from a file or user input.
    input_stream = FileStream("input.tua")

    # Initialize the lexer and parser.
    lexer = tuaLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = tuaParser(tokens)

    # Build the parse tree and create the visitor.
    tree = parser.prog()
    visitor = TuaVisitor()

    # Visit the parse tree using the visitor.
    visitor.visit(tree)

if __name__ == '__main__':
    main()