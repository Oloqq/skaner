# Generated from ../grammars/Tua.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TuaParser import TuaParser
else:
    from TuaParser import TuaParser

# This class defines a complete generic visitor for a parse tree produced by TuaParser.

class TuaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TuaParser#program.
    def visitProgram(self, ctx:TuaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#block.
    def visitBlock(self, ctx:TuaParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#stat.
    def visitStat(self, ctx:TuaParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#assignment.
    def visitAssignment(self, ctx:TuaParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#newvariable.
    def visitNewvariable(self, ctx:TuaParser.NewvariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#var.
    def visitVar(self, ctx:TuaParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#nametype.
    def visitNametype(self, ctx:TuaParser.NametypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#type.
    def visitType(self, ctx:TuaParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#tableType.
    def visitTableType(self, ctx:TuaParser.TableTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#unionType.
    def visitUnionType(self, ctx:TuaParser.UnionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#listType.
    def visitListType(self, ctx:TuaParser.ListTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#prefix.
    def visitPrefix(self, ctx:TuaParser.PrefixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#suffix.
    def visitSuffix(self, ctx:TuaParser.SuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#exp.
    def visitExp(self, ctx:TuaParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#functionbody.
    def visitFunctionbody(self, ctx:TuaParser.FunctionbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#dostat.
    def visitDostat(self, ctx:TuaParser.DostatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#whilestat.
    def visitWhilestat(self, ctx:TuaParser.WhilestatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#ifstat.
    def visitIfstat(self, ctx:TuaParser.IfstatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#forintstat.
    def visitForintstat(self, ctx:TuaParser.ForintstatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#foriteratorstat.
    def visitForiteratorstat(self, ctx:TuaParser.ForiteratorstatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#functiondef.
    def visitFunctiondef(self, ctx:TuaParser.FunctiondefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#laststat.
    def visitLaststat(self, ctx:TuaParser.LaststatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#typednamelist.
    def visitTypednamelist(self, ctx:TuaParser.TypednamelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#functioncall.
    def visitFunctioncall(self, ctx:TuaParser.FunctioncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#explist.
    def visitExplist(self, ctx:TuaParser.ExplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#tableconstructor.
    def visitTableconstructor(self, ctx:TuaParser.TableconstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#fieldlist.
    def visitFieldlist(self, ctx:TuaParser.FieldlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#field.
    def visitField(self, ctx:TuaParser.FieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#binopAddSub.
    def visitBinopAddSub(self, ctx:TuaParser.BinopAddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#binopMulDivMod.
    def visitBinopMulDivMod(self, ctx:TuaParser.BinopMulDivModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#binopComparison.
    def visitBinopComparison(self, ctx:TuaParser.BinopComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#binopConcat.
    def visitBinopConcat(self, ctx:TuaParser.BinopConcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#binopAnd.
    def visitBinopAnd(self, ctx:TuaParser.BinopAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#binopOr.
    def visitBinopOr(self, ctx:TuaParser.BinopOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#binopPower.
    def visitBinopPower(self, ctx:TuaParser.BinopPowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#unop.
    def visitUnop(self, ctx:TuaParser.UnopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#string.
    def visitString(self, ctx:TuaParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#number.
    def visitNumber(self, ctx:TuaParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuaParser#bool.
    def visitBool(self, ctx:TuaParser.BoolContext):
        return self.visitChildren(ctx)



del TuaParser