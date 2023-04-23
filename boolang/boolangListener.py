# Generated from boolang.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .boolangParser import boolangParser
else:
    from boolangParser import boolangParser

# This class defines a complete listener for a parse tree produced by boolangParser.
class boolangListener(ParseTreeListener):

    # Enter a parse tree produced by boolangParser#prog.
    def enterProg(self, ctx:boolangParser.ProgContext):
        pass

    # Exit a parse tree produced by boolangParser#prog.
    def exitProg(self, ctx:boolangParser.ProgContext):
        pass


    # Enter a parse tree produced by boolangParser#stat.
    def enterStat(self, ctx:boolangParser.StatContext):
        pass

    # Exit a parse tree produced by boolangParser#stat.
    def exitStat(self, ctx:boolangParser.StatContext):
        pass


    # Enter a parse tree produced by boolangParser#assignment.
    def enterAssignment(self, ctx:boolangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by boolangParser#assignment.
    def exitAssignment(self, ctx:boolangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by boolangParser#ifStatement.
    def enterIfStatement(self, ctx:boolangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by boolangParser#ifStatement.
    def exitIfStatement(self, ctx:boolangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by boolangParser#echoStatement.
    def enterEchoStatement(self, ctx:boolangParser.EchoStatementContext):
        pass

    # Exit a parse tree produced by boolangParser#echoStatement.
    def exitEchoStatement(self, ctx:boolangParser.EchoStatementContext):
        pass


    # Enter a parse tree produced by boolangParser#boolExpr.
    def enterBoolExpr(self, ctx:boolangParser.BoolExprContext):
        pass

    # Exit a parse tree produced by boolangParser#boolExpr.
    def exitBoolExpr(self, ctx:boolangParser.BoolExprContext):
        pass



del boolangParser