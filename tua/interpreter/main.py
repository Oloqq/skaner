from .generated.TuaLexer import TuaLexer
from .generated.TuaParser import TuaParser
from .visitor import Tua
from antlr4 import *

def run_interpreter():
    # Read input from a file or user input.
    input_stream = FileStream("tmp.tua")

    # Initialize the lexer and parser.
    lexer = TuaLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = TuaParser(tokens)

    # Build the parse tree and create the visitor.
    tree = parser.program()
    visitor = Tua()

    # Visit the parse tree using the visitor.
    visitor.visit(tree)
