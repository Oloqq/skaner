# Generated from ../grammars/tua.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .tuaParser import tuaParser
else:
    from tuaParser import tuaParser

# This class defines a complete listener for a parse tree produced by tuaParser.
class tuaListener(ParseTreeListener):

    # Enter a parse tree produced by tuaParser#program.
    def enterProgram(self, ctx:tuaParser.ProgramContext):
        pass

    # Exit a parse tree produced by tuaParser#program.
    def exitProgram(self, ctx:tuaParser.ProgramContext):
        pass


    # Enter a parse tree produced by tuaParser#block.
    def enterBlock(self, ctx:tuaParser.BlockContext):
        pass

    # Exit a parse tree produced by tuaParser#block.
    def exitBlock(self, ctx:tuaParser.BlockContext):
        pass


    # Enter a parse tree produced by tuaParser#stat.
    def enterStat(self, ctx:tuaParser.StatContext):
        pass

    # Exit a parse tree produced by tuaParser#stat.
    def exitStat(self, ctx:tuaParser.StatContext):
        pass


    # Enter a parse tree produced by tuaParser#var.
    def enterVar(self, ctx:tuaParser.VarContext):
        pass

    # Exit a parse tree produced by tuaParser#var.
    def exitVar(self, ctx:tuaParser.VarContext):
        pass


    # Enter a parse tree produced by tuaParser#nametype.
    def enterNametype(self, ctx:tuaParser.NametypeContext):
        pass

    # Exit a parse tree produced by tuaParser#nametype.
    def exitNametype(self, ctx:tuaParser.NametypeContext):
        pass


    # Enter a parse tree produced by tuaParser#type.
    def enterType(self, ctx:tuaParser.TypeContext):
        pass

    # Exit a parse tree produced by tuaParser#type.
    def exitType(self, ctx:tuaParser.TypeContext):
        pass


    # Enter a parse tree produced by tuaParser#tableType.
    def enterTableType(self, ctx:tuaParser.TableTypeContext):
        pass

    # Exit a parse tree produced by tuaParser#tableType.
    def exitTableType(self, ctx:tuaParser.TableTypeContext):
        pass


    # Enter a parse tree produced by tuaParser#unionType.
    def enterUnionType(self, ctx:tuaParser.UnionTypeContext):
        pass

    # Exit a parse tree produced by tuaParser#unionType.
    def exitUnionType(self, ctx:tuaParser.UnionTypeContext):
        pass


    # Enter a parse tree produced by tuaParser#listType.
    def enterListType(self, ctx:tuaParser.ListTypeContext):
        pass

    # Exit a parse tree produced by tuaParser#listType.
    def exitListType(self, ctx:tuaParser.ListTypeContext):
        pass


    # Enter a parse tree produced by tuaParser#prefix.
    def enterPrefix(self, ctx:tuaParser.PrefixContext):
        pass

    # Exit a parse tree produced by tuaParser#prefix.
    def exitPrefix(self, ctx:tuaParser.PrefixContext):
        pass


    # Enter a parse tree produced by tuaParser#suffix.
    def enterSuffix(self, ctx:tuaParser.SuffixContext):
        pass

    # Exit a parse tree produced by tuaParser#suffix.
    def exitSuffix(self, ctx:tuaParser.SuffixContext):
        pass


    # Enter a parse tree produced by tuaParser#exp.
    def enterExp(self, ctx:tuaParser.ExpContext):
        pass

    # Exit a parse tree produced by tuaParser#exp.
    def exitExp(self, ctx:tuaParser.ExpContext):
        pass


    # Enter a parse tree produced by tuaParser#functionbody.
    def enterFunctionbody(self, ctx:tuaParser.FunctionbodyContext):
        pass

    # Exit a parse tree produced by tuaParser#functionbody.
    def exitFunctionbody(self, ctx:tuaParser.FunctionbodyContext):
        pass


    # Enter a parse tree produced by tuaParser#laststat.
    def enterLaststat(self, ctx:tuaParser.LaststatContext):
        pass

    # Exit a parse tree produced by tuaParser#laststat.
    def exitLaststat(self, ctx:tuaParser.LaststatContext):
        pass


    # Enter a parse tree produced by tuaParser#typednamelist.
    def enterTypednamelist(self, ctx:tuaParser.TypednamelistContext):
        pass

    # Exit a parse tree produced by tuaParser#typednamelist.
    def exitTypednamelist(self, ctx:tuaParser.TypednamelistContext):
        pass


    # Enter a parse tree produced by tuaParser#functioncall.
    def enterFunctioncall(self, ctx:tuaParser.FunctioncallContext):
        pass

    # Exit a parse tree produced by tuaParser#functioncall.
    def exitFunctioncall(self, ctx:tuaParser.FunctioncallContext):
        pass


    # Enter a parse tree produced by tuaParser#explist.
    def enterExplist(self, ctx:tuaParser.ExplistContext):
        pass

    # Exit a parse tree produced by tuaParser#explist.
    def exitExplist(self, ctx:tuaParser.ExplistContext):
        pass


    # Enter a parse tree produced by tuaParser#tableconstructor.
    def enterTableconstructor(self, ctx:tuaParser.TableconstructorContext):
        pass

    # Exit a parse tree produced by tuaParser#tableconstructor.
    def exitTableconstructor(self, ctx:tuaParser.TableconstructorContext):
        pass


    # Enter a parse tree produced by tuaParser#fieldlist.
    def enterFieldlist(self, ctx:tuaParser.FieldlistContext):
        pass

    # Exit a parse tree produced by tuaParser#fieldlist.
    def exitFieldlist(self, ctx:tuaParser.FieldlistContext):
        pass


    # Enter a parse tree produced by tuaParser#field.
    def enterField(self, ctx:tuaParser.FieldContext):
        pass

    # Exit a parse tree produced by tuaParser#field.
    def exitField(self, ctx:tuaParser.FieldContext):
        pass


    # Enter a parse tree produced by tuaParser#binopAddSub.
    def enterBinopAddSub(self, ctx:tuaParser.BinopAddSubContext):
        pass

    # Exit a parse tree produced by tuaParser#binopAddSub.
    def exitBinopAddSub(self, ctx:tuaParser.BinopAddSubContext):
        pass


    # Enter a parse tree produced by tuaParser#binopMulDivMod.
    def enterBinopMulDivMod(self, ctx:tuaParser.BinopMulDivModContext):
        pass

    # Exit a parse tree produced by tuaParser#binopMulDivMod.
    def exitBinopMulDivMod(self, ctx:tuaParser.BinopMulDivModContext):
        pass


    # Enter a parse tree produced by tuaParser#binopComparison.
    def enterBinopComparison(self, ctx:tuaParser.BinopComparisonContext):
        pass

    # Exit a parse tree produced by tuaParser#binopComparison.
    def exitBinopComparison(self, ctx:tuaParser.BinopComparisonContext):
        pass


    # Enter a parse tree produced by tuaParser#binopConcat.
    def enterBinopConcat(self, ctx:tuaParser.BinopConcatContext):
        pass

    # Exit a parse tree produced by tuaParser#binopConcat.
    def exitBinopConcat(self, ctx:tuaParser.BinopConcatContext):
        pass


    # Enter a parse tree produced by tuaParser#binopAnd.
    def enterBinopAnd(self, ctx:tuaParser.BinopAndContext):
        pass

    # Exit a parse tree produced by tuaParser#binopAnd.
    def exitBinopAnd(self, ctx:tuaParser.BinopAndContext):
        pass


    # Enter a parse tree produced by tuaParser#binopOr.
    def enterBinopOr(self, ctx:tuaParser.BinopOrContext):
        pass

    # Exit a parse tree produced by tuaParser#binopOr.
    def exitBinopOr(self, ctx:tuaParser.BinopOrContext):
        pass


    # Enter a parse tree produced by tuaParser#binopPower.
    def enterBinopPower(self, ctx:tuaParser.BinopPowerContext):
        pass

    # Exit a parse tree produced by tuaParser#binopPower.
    def exitBinopPower(self, ctx:tuaParser.BinopPowerContext):
        pass


    # Enter a parse tree produced by tuaParser#unop.
    def enterUnop(self, ctx:tuaParser.UnopContext):
        pass

    # Exit a parse tree produced by tuaParser#unop.
    def exitUnop(self, ctx:tuaParser.UnopContext):
        pass


    # Enter a parse tree produced by tuaParser#string.
    def enterString(self, ctx:tuaParser.StringContext):
        pass

    # Exit a parse tree produced by tuaParser#string.
    def exitString(self, ctx:tuaParser.StringContext):
        pass


    # Enter a parse tree produced by tuaParser#number.
    def enterNumber(self, ctx:tuaParser.NumberContext):
        pass

    # Exit a parse tree produced by tuaParser#number.
    def exitNumber(self, ctx:tuaParser.NumberContext):
        pass



del tuaParser