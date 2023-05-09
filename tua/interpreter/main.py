from .generated.TuaLexer import TuaLexer
from .generated.TuaParser import TuaParser
from .visitor import Tua
from antlr4 import *

from .log import log, init_log
import logging

import click

@click.command()
@click.argument("input_file", type=click.Path(exists=True))
@click.option("-d", "--debug", is_flag=True)
def run_interpreter(input_file, debug):
    init_log(logging.DEBUG if debug else logging.WARNING)

    # log.debug("bruu")
    # log.info("bruh")
    # log.warning("brrr")
    # log.error("bbbb")

    # Read input from a file or user input.
    input_stream = FileStream(input_file)

    # Initialize the lexer and parser.
    lexer = TuaLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = TuaParser(tokens)

    # Build the parse tree and create the visitor.
    tree = parser.program()
    visitor = Tua()

    # Visit the parse tree using the visitor.
    visitor.visit(tree)
