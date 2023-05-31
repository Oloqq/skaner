# Generated from ../grammars/Tua.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TuaParser import TuaParser
else:
    from TuaParser import TuaParser

# This class defines a complete listener for a parse tree produced by TuaParser.
class TuaListener(ParseTreeListener):

    # Enter a parse tree produced by TuaParser#program.
    def enterProgram(self, ctx:TuaParser.ProgramContext):
        pass

    # Exit a parse tree produced by TuaParser#program.
    def exitProgram(self, ctx:TuaParser.ProgramContext):
        pass


    # Enter a parse tree produced by TuaParser#block.
    def enterBlock(self, ctx:TuaParser.BlockContext):
        pass

    # Exit a parse tree produced by TuaParser#block.
    def exitBlock(self, ctx:TuaParser.BlockContext):
        pass


    # Enter a parse tree produced by TuaParser#stat.
    def enterStat(self, ctx:TuaParser.StatContext):
        pass

    # Exit a parse tree produced by TuaParser#stat.
    def exitStat(self, ctx:TuaParser.StatContext):
        pass


    # Enter a parse tree produced by TuaParser#assignment.
    def enterAssignment(self, ctx:TuaParser.AssignmentContext):
        pass

    # Exit a parse tree produced by TuaParser#assignment.
    def exitAssignment(self, ctx:TuaParser.AssignmentContext):
        pass


    # Enter a parse tree produced by TuaParser#newvariable.
    def enterNewvariable(self, ctx:TuaParser.NewvariableContext):
        pass

    # Exit a parse tree produced by TuaParser#newvariable.
    def exitNewvariable(self, ctx:TuaParser.NewvariableContext):
        pass


    # Enter a parse tree produced by TuaParser#var.
    def enterVar(self, ctx:TuaParser.VarContext):
        pass

    # Exit a parse tree produced by TuaParser#var.
    def exitVar(self, ctx:TuaParser.VarContext):
        pass


    # Enter a parse tree produced by TuaParser#nametype.
    def enterNametype(self, ctx:TuaParser.NametypeContext):
        pass

    # Exit a parse tree produced by TuaParser#nametype.
    def exitNametype(self, ctx:TuaParser.NametypeContext):
        pass


    # Enter a parse tree produced by TuaParser#type.
    def enterType(self, ctx:TuaParser.TypeContext):
        pass

    # Exit a parse tree produced by TuaParser#type.
    def exitType(self, ctx:TuaParser.TypeContext):
        pass


    # Enter a parse tree produced by TuaParser#tableType.
    def enterTableType(self, ctx:TuaParser.TableTypeContext):
        pass

    # Exit a parse tree produced by TuaParser#tableType.
    def exitTableType(self, ctx:TuaParser.TableTypeContext):
        pass


    # Enter a parse tree produced by TuaParser#unionType.
    def enterUnionType(self, ctx:TuaParser.UnionTypeContext):
        pass

    # Exit a parse tree produced by TuaParser#unionType.
    def exitUnionType(self, ctx:TuaParser.UnionTypeContext):
        pass


    # Enter a parse tree produced by TuaParser#listType.
    def enterListType(self, ctx:TuaParser.ListTypeContext):
        pass

    # Exit a parse tree produced by TuaParser#listType.
    def exitListType(self, ctx:TuaParser.ListTypeContext):
        pass


    # Enter a parse tree produced by TuaParser#prefix.
    def enterPrefix(self, ctx:TuaParser.PrefixContext):
        pass

    # Exit a parse tree produced by TuaParser#prefix.
    def exitPrefix(self, ctx:TuaParser.PrefixContext):
        pass


    # Enter a parse tree produced by TuaParser#suffix.
    def enterSuffix(self, ctx:TuaParser.SuffixContext):
        pass

    # Exit a parse tree produced by TuaParser#suffix.
    def exitSuffix(self, ctx:TuaParser.SuffixContext):
        pass


    # Enter a parse tree produced by TuaParser#exp.
    def enterExp(self, ctx:TuaParser.ExpContext):
        pass

    # Exit a parse tree produced by TuaParser#exp.
    def exitExp(self, ctx:TuaParser.ExpContext):
        pass


    # Enter a parse tree produced by TuaParser#parexp.
    def enterParexp(self, ctx:TuaParser.ParexpContext):
        pass

    # Exit a parse tree produced by TuaParser#parexp.
    def exitParexp(self, ctx:TuaParser.ParexpContext):
        pass


    # Enter a parse tree produced by TuaParser#functionbody.
    def enterFunctionbody(self, ctx:TuaParser.FunctionbodyContext):
        pass

    # Exit a parse tree produced by TuaParser#functionbody.
    def exitFunctionbody(self, ctx:TuaParser.FunctionbodyContext):
        pass


    # Enter a parse tree produced by TuaParser#dostat.
    def enterDostat(self, ctx:TuaParser.DostatContext):
        pass

    # Exit a parse tree produced by TuaParser#dostat.
    def exitDostat(self, ctx:TuaParser.DostatContext):
        pass


    # Enter a parse tree produced by TuaParser#whilestat.
    def enterWhilestat(self, ctx:TuaParser.WhilestatContext):
        pass

    # Exit a parse tree produced by TuaParser#whilestat.
    def exitWhilestat(self, ctx:TuaParser.WhilestatContext):
        pass


    # Enter a parse tree produced by TuaParser#ifstat.
    def enterIfstat(self, ctx:TuaParser.IfstatContext):
        pass

    # Exit a parse tree produced by TuaParser#ifstat.
    def exitIfstat(self, ctx:TuaParser.IfstatContext):
        pass


    # Enter a parse tree produced by TuaParser#forintstat.
    def enterForintstat(self, ctx:TuaParser.ForintstatContext):
        pass

    # Exit a parse tree produced by TuaParser#forintstat.
    def exitForintstat(self, ctx:TuaParser.ForintstatContext):
        pass


    # Enter a parse tree produced by TuaParser#foriteratorstat.
    def enterForiteratorstat(self, ctx:TuaParser.ForiteratorstatContext):
        pass

    # Exit a parse tree produced by TuaParser#foriteratorstat.
    def exitForiteratorstat(self, ctx:TuaParser.ForiteratorstatContext):
        pass


    # Enter a parse tree produced by TuaParser#functiondef.
    def enterFunctiondef(self, ctx:TuaParser.FunctiondefContext):
        pass

    # Exit a parse tree produced by TuaParser#functiondef.
    def exitFunctiondef(self, ctx:TuaParser.FunctiondefContext):
        pass


    # Enter a parse tree produced by TuaParser#laststat.
    def enterLaststat(self, ctx:TuaParser.LaststatContext):
        pass

    # Exit a parse tree produced by TuaParser#laststat.
    def exitLaststat(self, ctx:TuaParser.LaststatContext):
        pass


    # Enter a parse tree produced by TuaParser#typednamelist.
    def enterTypednamelist(self, ctx:TuaParser.TypednamelistContext):
        pass

    # Exit a parse tree produced by TuaParser#typednamelist.
    def exitTypednamelist(self, ctx:TuaParser.TypednamelistContext):
        pass


    # Enter a parse tree produced by TuaParser#functioncall.
    def enterFunctioncall(self, ctx:TuaParser.FunctioncallContext):
        pass

    # Exit a parse tree produced by TuaParser#functioncall.
    def exitFunctioncall(self, ctx:TuaParser.FunctioncallContext):
        pass


    # Enter a parse tree produced by TuaParser#explist.
    def enterExplist(self, ctx:TuaParser.ExplistContext):
        pass

    # Exit a parse tree produced by TuaParser#explist.
    def exitExplist(self, ctx:TuaParser.ExplistContext):
        pass


    # Enter a parse tree produced by TuaParser#tableconstructor.
    def enterTableconstructor(self, ctx:TuaParser.TableconstructorContext):
        pass

    # Exit a parse tree produced by TuaParser#tableconstructor.
    def exitTableconstructor(self, ctx:TuaParser.TableconstructorContext):
        pass


    # Enter a parse tree produced by TuaParser#fieldlist.
    def enterFieldlist(self, ctx:TuaParser.FieldlistContext):
        pass

    # Exit a parse tree produced by TuaParser#fieldlist.
    def exitFieldlist(self, ctx:TuaParser.FieldlistContext):
        pass


    # Enter a parse tree produced by TuaParser#field.
    def enterField(self, ctx:TuaParser.FieldContext):
        pass

    # Exit a parse tree produced by TuaParser#field.
    def exitField(self, ctx:TuaParser.FieldContext):
        pass


    # Enter a parse tree produced by TuaParser#binopAddSub.
    def enterBinopAddSub(self, ctx:TuaParser.BinopAddSubContext):
        pass

    # Exit a parse tree produced by TuaParser#binopAddSub.
    def exitBinopAddSub(self, ctx:TuaParser.BinopAddSubContext):
        pass


    # Enter a parse tree produced by TuaParser#binopMulDivMod.
    def enterBinopMulDivMod(self, ctx:TuaParser.BinopMulDivModContext):
        pass

    # Exit a parse tree produced by TuaParser#binopMulDivMod.
    def exitBinopMulDivMod(self, ctx:TuaParser.BinopMulDivModContext):
        pass


    # Enter a parse tree produced by TuaParser#binopComparison.
    def enterBinopComparison(self, ctx:TuaParser.BinopComparisonContext):
        pass

    # Exit a parse tree produced by TuaParser#binopComparison.
    def exitBinopComparison(self, ctx:TuaParser.BinopComparisonContext):
        pass


    # Enter a parse tree produced by TuaParser#binopConcat.
    def enterBinopConcat(self, ctx:TuaParser.BinopConcatContext):
        pass

    # Exit a parse tree produced by TuaParser#binopConcat.
    def exitBinopConcat(self, ctx:TuaParser.BinopConcatContext):
        pass


    # Enter a parse tree produced by TuaParser#binopAnd.
    def enterBinopAnd(self, ctx:TuaParser.BinopAndContext):
        pass

    # Exit a parse tree produced by TuaParser#binopAnd.
    def exitBinopAnd(self, ctx:TuaParser.BinopAndContext):
        pass


    # Enter a parse tree produced by TuaParser#binopOr.
    def enterBinopOr(self, ctx:TuaParser.BinopOrContext):
        pass

    # Exit a parse tree produced by TuaParser#binopOr.
    def exitBinopOr(self, ctx:TuaParser.BinopOrContext):
        pass


    # Enter a parse tree produced by TuaParser#binopPower.
    def enterBinopPower(self, ctx:TuaParser.BinopPowerContext):
        pass

    # Exit a parse tree produced by TuaParser#binopPower.
    def exitBinopPower(self, ctx:TuaParser.BinopPowerContext):
        pass


    # Enter a parse tree produced by TuaParser#unop.
    def enterUnop(self, ctx:TuaParser.UnopContext):
        pass

    # Exit a parse tree produced by TuaParser#unop.
    def exitUnop(self, ctx:TuaParser.UnopContext):
        pass


    # Enter a parse tree produced by TuaParser#string.
    def enterString(self, ctx:TuaParser.StringContext):
        pass

    # Exit a parse tree produced by TuaParser#string.
    def exitString(self, ctx:TuaParser.StringContext):
        pass


    # Enter a parse tree produced by TuaParser#number.
    def enterNumber(self, ctx:TuaParser.NumberContext):
        pass

    # Exit a parse tree produced by TuaParser#number.
    def exitNumber(self, ctx:TuaParser.NumberContext):
        pass


    # Enter a parse tree produced by TuaParser#bool.
    def enterBool(self, ctx:TuaParser.BoolContext):
        pass

    # Exit a parse tree produced by TuaParser#bool.
    def exitBool(self, ctx:TuaParser.BoolContext):
        pass



del TuaParser