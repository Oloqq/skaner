from .generated.TuaVisitor import TuaVisitor
from .generated.TuaParser import TuaParser
from .log import log
from .builtins import builtins

class Tua(TuaVisitor):
    def __init__(self):
        self.variables = {}


    def visitProgram(self, ctx:TuaParser.ProgramContext):
        log.info("Program")
        return self.visitChildren(ctx)


    def visitBlock(self, ctx:TuaParser.BlockContext):
        log.info("Block")
        return self.visitChildren(ctx)


    def visitStat(self, ctx:TuaParser.StatContext):
        log.info("Stat")
        return self.visitChildren(ctx)


    def visitVar(self, ctx:TuaParser.VarContext):
        log.info("Var")
        return self.visitChildren(ctx)


    def visitNametype(self, ctx:TuaParser.NametypeContext):
        log.info("Nametype")
        return self.visitChildren(ctx)


    def visitType(self, ctx:TuaParser.TypeContext):
        log.info("Type")
        return self.visitChildren(ctx)


    def visitTableType(self, ctx:TuaParser.TableTypeContext):
        log.info("TableType")
        return self.visitChildren(ctx)


    def visitUnionType(self, ctx:TuaParser.UnionTypeContext):
        log.info("UnionType")
        return self.visitChildren(ctx)


    def visitListType(self, ctx:TuaParser.ListTypeContext):
        log.info("ListType")
        return self.visitChildren(ctx)


    def visitPrefix(self, ctx:TuaParser.PrefixContext):
        log.info("Prefix")
        return self.visitChildren(ctx)


    def visitSuffix(self, ctx:TuaParser.SuffixContext):
        log.info("Suffix")
        return self.visitChildren(ctx)


    def visitExp(self, ctx:TuaParser.ExpContext):
        log.info("Exp")
        if len(ctx.children) == 1:
            return self.visit(ctx.children[0])
        else:
            raise NotImplementedError


    def visitFunctionbody(self, ctx:TuaParser.FunctionbodyContext):
        log.info("Functionbody")
        return self.visitChildren(ctx)


    def visitLaststat(self, ctx:TuaParser.LaststatContext):
        log.info("Laststat")
        return self.visitChildren(ctx)


    def visitTypednamelist(self, ctx:TuaParser.TypednamelistContext):
        log.info("Typednamelist")
        return self.visitChildren(ctx)


    def visitFunctioncall(self, ctx:TuaParser.FunctioncallContext):
        log.info(f"Functioncall")
        name = ctx.getToken(TuaParser.NAME, 0).getText()
        args = self.visit(ctx.explist())
        if name in builtins:
            builtins[name](*args)
        else:
            # return value returned by function
            raise NotImplementedError


    def visitExplist(self, ctx:TuaParser.ExplistContext):
        log.info("Explist")
        vals = []
        for c in ctx.getChildren():
            vals.append(self.visit(c))
        return vals


    def visitTableconstructor(self, ctx:TuaParser.TableconstructorContext):
        log.info("Tableconstructor")
        return self.visitChildren(ctx)


    def visitFieldlist(self, ctx:TuaParser.FieldlistContext):
        log.info("Fieldlist")
        return self.visitChildren(ctx)


    def visitField(self, ctx:TuaParser.FieldContext):
        log.info("Field")
        return self.visitChildren(ctx)


    def visitBinopAddSub(self, ctx:TuaParser.BinopAddSubContext):
        log.info("BinopAddSub")
        return self.visitChildren(ctx)


    def visitBinopMulDivMod(self, ctx:TuaParser.BinopMulDivModContext):
        log.info("BinopMulDivMod")
        return self.visitChildren(ctx)


    def visitBinopComparison(self, ctx:TuaParser.BinopComparisonContext):
        log.info("BinopComparison")
        return self.visitChildren(ctx)


    def visitBinopConcat(self, ctx:TuaParser.BinopConcatContext):
        log.info("BinopConcat")
        return self.visitChildren(ctx)


    def visitBinopAnd(self, ctx:TuaParser.BinopAndContext):
        log.info("BinopAnd")
        return self.visitChildren(ctx)


    def visitBinopOr(self, ctx:TuaParser.BinopOrContext):
        log.info("BinopOr")
        return self.visitChildren(ctx)


    def visitBinopPower(self, ctx:TuaParser.BinopPowerContext):
        log.info("BinopPower")
        return self.visitChildren(ctx)


    def visitUnop(self, ctx:TuaParser.UnopContext):
        log.info("Unop")
        return self.visitChildren(ctx)


    def visitString(self, ctx:TuaParser.StringContext):
        return ctx.getText()[1:-1] # skip quotes


    def visitNumber(self, ctx:TuaParser.NumberContext):
        log.info("Number")
        return self.visitChildren(ctx)