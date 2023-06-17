from .generated.TuaLexer import TuaLexer
from .generated.TuaParser import TuaParser
from .visitor import Tua
from antlr4 import *

from .log import log, init_log
import logging

import click

class CustomErrorListener:
    def __init__(self):
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Syntax error at line {line}, column {column}: {msg}")


def multiline_triggered(line: str) -> bool:
    words = line.split(" ")
    return words[0] == "function" or words[-1] in ["then", "do"]

# limitations:
# at most one new scope per line
# end must be on it's own line (unless scope was opened at the same line)
def handle_multiline(line):
    level = 1
    buffer = [line]
    while True:
        line = input(">").strip()
        buffer.append(line)
        if multiline_triggered(line):
            level += 1
        if line == "end":
            level -= 1
        if level <= 0:
            break
    return " ".join(buffer)

def run_interpreter_line_by_line():
    visitor = Tua()

    print(">>>", end="")

    for line in iter(input, ''):
        if line == "exit":
            break
        elif multiline_triggered(line):
            code = handle_multiline(line)
        else:
            code = line

        lexer = TuaLexer(InputStream(code))
        tokens = CommonTokenStream(lexer)
        parser = TuaParser(tokens)
        tree = parser.program()
        visitor.visit(tree)
        print('>>> ', end='')

def run_interpreter_full_program(program: FileStream|InputStream):
    # Initialize the lexer and parser.
    lexer = TuaLexer(program)
    tokens = CommonTokenStream(lexer)
    parser = TuaParser(tokens)

    # capture syntax errors
    error_listener = CustomErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    # Build the parse tree and create the visitor.
    tree = parser.program()
    if len(error_listener.errors) > 0:
        print(error_listener.errors[0])
    else:
        visitor = Tua()
        # Visit the parse tree using the visitor.
        visitor.visit(tree)

def run_interpreter(input_file, debug):
    init_log(logging.DEBUG if debug else logging.WARNING)
    if input_file != None:
        run_interpreter_full_program(FileStream(input_file))
    else:
        run_interpreter_line_by_line()


@click.command()
@click.argument("input_file", type=click.Path(exists=True), required=False)
@click.option("-d", "--debug", is_flag=True)
def cli_run_interpreter(input_file, debug):
    run_interpreter(input_file, debug)
