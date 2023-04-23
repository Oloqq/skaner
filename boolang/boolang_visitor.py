from antlr4 import *
from SimpleBooleanLexer import SimpleBooleanLexer
from boolangParser import boolangParser
from boolangVisitor import boolangVisitor

class MySimpleBooleanVisitor(boolangVisitor):
    def __init__(self):
        self.variables = {}

    def visitProg(self, ctx: boolangParser.ProgContext):
        return self.visitChildren(ctx)

    def visitAssignment(self, ctx: boolangParser.AssignmentContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.boolExpr())
        self.variables[var_name] = value
        return None

    def visitIfStatement(self, ctx: boolangParser.IfStatementContext):
        condition = self.visit(ctx.boolExpr())
        if condition:
            return self.visit(ctx.stat(0))
        elif ctx.stat(1) is not None:
            return self.visit(ctx.stat(1))
        return None

    def visitEchoStatement(self, ctx: boolangParser.EchoStatementContext):
        print(ctx.INT().getText())
        return None

    def visitBoolExpr(self, ctx: boolangParser.BoolExprContext):
        if ctx.getText() == 'true':
            return True
        elif ctx.getText() == 'false':
            return False
        else:
            return self.variables.get(ctx.getText(), False)

def main():
    # Read input from a file or user input.
    input_stream = FileStream("input.txt")

    # Initialize the lexer and parser.
    lexer = SimpleBooleanLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = boolangParser(tokens)

    # Build the parse tree and create the visitor.
    tree = parser.prog()
    visitor = MySimpleBooleanVisitor()

    # Visit the parse tree using the visitor.
    visitor.visit(tree)

if __name__ == '__main__':
    main()