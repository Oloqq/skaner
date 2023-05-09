from .generated.TuaVisitor import TuaVisitor
from .generated.TuaParser import TuaParser

class Tua(TuaVisitor):
    def __init__(self):
        self.variables = {}

    def visitProgram(self, ctx: TuaParser.ProgramContext):
        print("visitProgram")
        return self.visitChildren(ctx)