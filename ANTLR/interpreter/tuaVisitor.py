# Generated from ../grammars/tua.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .tuaParser import tuaParser
else:
    from tuaParser import tuaParser

# This class defines a complete generic visitor for a parse tree produced by tuaParser.

class tuaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by tuaParser#program.
    def visitProgram(self, ctx:tuaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tuaParser#block.
    def visitBlock(self, ctx:tuaParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tuaParser#stat.
    def visitStat(self, ctx:tuaParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tuaParser#var.
    def visitVar(self, ctx:tuaParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tuaParser#nametype.
    def visitNametype(self, ctx:tuaParser.NametypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tuaParser#type.
    def visitType(self, ctx:tuaParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tuaParser#tableType.
    def visitTableType(self, ctx:tuaParser.TableTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tuaParser#unionType.
    def visitUnionType(self, ctx:tuaParser.UnionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tuaParser#listType.
    def visitListType(self, ctx:tuaParser.ListTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tuaParser#prefix.
    def visitPrefix(self, ctx:tuaParser.PrefixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tuaParser#suffix.
    def visitSuffix(self, ctx:tuaParser.SuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tuaParser#exp.
    def visitExp(self, ctx:tuaParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tuaParser#functionbody.
    def visitFunctionbody(self, ctx:tuaParser.FunctionbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tuaParser#laststat.
    def visitLaststat(self, ctx:tuaParser.LaststatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tuaParser#typednamelist.
    def visitTypednamelist(self, ctx:tuaParser.TypednamelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tuaParser#functioncall.
    def visitFunctioncall(self, ctx:tuaParser.FunctioncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tuaParser#explist.
    def visitExplist(self, ctx:tuaParser.ExplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tuaParser#tableconstructor.
    def visitTableconstructor(self, ctx:tuaParser.TableconstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tuaParser#fieldlist.
    def visitFieldlist(self, ctx:tuaParser.FieldlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tuaParser#field.
    def visitField(self, ctx:tuaParser.FieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tuaParser#binopAddSub.
    def visitBinopAddSub(self, ctx:tuaParser.BinopAddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tuaParser#binopMulDivMod.
    def visitBinopMulDivMod(self, ctx:tuaParser.BinopMulDivModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tuaParser#binopComparison.
    def visitBinopComparison(self, ctx:tuaParser.BinopComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tuaParser#binopConcat.
    def visitBinopConcat(self, ctx:tuaParser.BinopConcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tuaParser#binopAnd.
    def visitBinopAnd(self, ctx:tuaParser.BinopAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tuaParser#binopOr.
    def visitBinopOr(self, ctx:tuaParser.BinopOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tuaParser#binopPower.
    def visitBinopPower(self, ctx:tuaParser.BinopPowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tuaParser#unop.
    def visitUnop(self, ctx:tuaParser.UnopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tuaParser#string.
    def visitString(self, ctx:tuaParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tuaParser#number.
    def visitNumber(self, ctx:tuaParser.NumberContext):
        return self.visitChildren(ctx)



del tuaParser