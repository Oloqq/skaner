from .generated.TuaLexer import TuaLexer
from .generated.TuaParser import TuaParser
from .visitor import Tua
from antlr4 import *

from .log import log, init_log
import logging

import click

def run_interpreter(program, debug):
    init_log(logging.DEBUG if debug else logging.WARNING)

    # Initialize the lexer and parser.
    lexer = TuaLexer(program)
    tokens = CommonTokenStream(lexer)
    parser = TuaParser(tokens)

    # Build the parse tree and create the visitor.
    tree = parser.program()
    visitor = Tua()

    # Visit the parse tree using the visitor.
    visitor.visit(tree)

@click.command()
@click.argument("input_file", type=click.Path(exists=True))
@click.option("-d", "--debug", is_flag=True)
def cli_run_interpreter(input_file, debug):
    program = FileStream(input_file)
    run_interpreter(program, debug)
