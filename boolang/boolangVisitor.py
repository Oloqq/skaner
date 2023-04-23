# Generated from boolang.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .boolangParser import boolangParser
else:
    from boolangParser import boolangParser

# This class defines a complete generic visitor for a parse tree produced by boolangParser.

class boolangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by boolangParser#prog.
    def visitProg(self, ctx:boolangParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by boolangParser#stat.
    def visitStat(self, ctx:boolangParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by boolangParser#assignment.
    def visitAssignment(self, ctx:boolangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by boolangParser#ifStatement.
    def visitIfStatement(self, ctx:boolangParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by boolangParser#echoStatement.
    def visitEchoStatement(self, ctx:boolangParser.EchoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by boolangParser#boolExpr.
    def visitBoolExpr(self, ctx:boolangParser.BoolExprContext):
        return self.visitChildren(ctx)



del boolangParser