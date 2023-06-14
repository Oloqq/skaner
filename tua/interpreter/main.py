from .generated.TuaLexer import TuaLexer
from .generated.TuaParser import TuaParser
from .visitor import Tua
from antlr4 import *

from .log import log, init_log
import logging

import click

def run_interpreter_line_by_line():
    # Initialize the visitor.
    visitor = Tua()

    buffer = []
    # multiline_mode = False
    code = input(">>>")
    lexer = TuaLexer(InputStream(code))
    tokens = CommonTokenStream(lexer)
    parser = TuaParser(tokens)
    tree = parser.program()
    visitor.visit(tree)

    # for line in iter(input, ''):
    #     buffer.append(line)

        # Check if the current line ends with a trigger word,
        # indicating that we're entering multi-line mode.
        # if any(line.strip().endswith(trigger) for trigger in multi_line_triggers):
        #     multiline_mode = True

        # # Check if we're in multi-line mode and the line ends with 'end',
        # # indicating that the current statement is complete.
        # if multiline_mode and line.strip().endswith('end'):
        #     # Concatenate all lines in the buffer and send them to the lexer and parser.
        #     code = ''.join(buffer)
        #     lexer = TuaLexer(InputStream(code))
        #     tokens = CommonTokenStream(lexer)
        #     parser = TuaParser(tokens)

        #     # Build the parse tree and visit it.
        #     tree = parser.program()
        #     visitor.visit(tree)

        #     # Clear the buffer and exit multi-line mode.
        #     buffer.clear()
        #     multiline_mode = False

        # print('>>> ', end='')

def run_interpreter_full_program(input_file):
    # Initialize the lexer and parser.
    program = FileStream(input_file)

    lexer = TuaLexer(program)
    tokens = CommonTokenStream(lexer)
    parser = TuaParser(tokens)

    # Build the parse tree and create the visitor.
    tree = parser.program()
    visitor = Tua()

    # Visit the parse tree using the visitor.
    visitor.visit(tree)

def run_interpreter(input_file, debug):
    init_log(logging.DEBUG if debug else logging.WARNING)
    if input_file != None:
        run_interpreter_full_program(input_file)    
    else:
        run_interpreter_line_by_line()


@click.command()
@click.argument("input_file", type=click.Path(exists=True), required=False)
@click.option("-d", "--debug", is_flag=True)
def cli_run_interpreter(input_file, debug):
    run_interpreter(input_file, debug)
