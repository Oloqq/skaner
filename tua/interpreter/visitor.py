from .generated.TuaVisitor import TuaVisitor
from .generated.TuaParser import TuaParser
from .log import log
from .scope import ScopeStack, Atom

class InternalError(Exception):
    pass

class Tua(TuaVisitor):
    def __init__(self):
        self.scope: ScopeStack = ScopeStack()
        from . import builtins
        self.builtins = {
            "print": builtins.print_,
            "dump_stack": builtins.dump_stack,
        }

    def builtin_print(self, *args):
        print(*args)

    def builtin_dump_stack(self, *args):
        print("Stack:", *args)

    def visitProgram(self, ctx:TuaParser.ProgramContext):
        log.info("Program")
        return self.visitChildren(ctx)


    def visitBlock(self, ctx:TuaParser.BlockContext):
        log.info("Block")
        self.scope.push()
        result = self.visitChildren(ctx)
        self.scope.pop()
        return result


    def visitStat(self, ctx:TuaParser.StatContext):
        log.info("Stat")
        return self.visitChildren(ctx)

    def visitNewvariable(self, ctx:TuaParser.NewvariableContext):
        log.info("Newvariable")
        lhs, type = self.visit(ctx.nametype())
        rhs = self.visit(ctx.exp())
        self.scope.new_atom(lhs, type, rhs)

    def visitAssignment(self, ctx:TuaParser.AssignmentContext):
        log.info("Assignment")
        identifier = self.visit(ctx.var())
        value = self.visit(ctx.exp())
        self.scope.set_exiting_atom(identifier, value)

    def visitVar(self, ctx:TuaParser.VarContext) -> str:
        log.info("Var")
        name = ctx.getToken(TuaParser.NAME, 0).getText()
        if ctx.suffix():
            # suffix = self.visit(ctx.suffix())
            raise NotImplementedError
        return name


    def visitNametype(self, ctx:TuaParser.NametypeContext):
        log.info("Nametype")
        name = ctx.getToken(TuaParser.NAME, 0).getText()
        type = self.visit(ctx.type_())
        return (name, type)


    def visitType(self, ctx:TuaParser.TypeContext):
        log.info("Type")
        if ctx.NAME():
            return ctx.NAME().getText()
        elif ctx.NIL():
            return "nil"
        elif ctx.listType():
            raise NotImplementedError
        elif ctx.unionType():
            raise NotImplementedError
        elif ctx.tableType():
            raise NotImplementedError
        else:
            raise InternalError


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
        if ctx.var():
            return self.visit(ctx.var())
        else:
            return NotImplementedError # functioncall


    def visitSuffix(self, ctx:TuaParser.SuffixContext):
        log.info("Suffix")
        return self.visitChildren(ctx)


    def visitExp(self, ctx:TuaParser.ExpContext):
        log.info("Exp")
        if ctx.prefix():
            identifier = self.visit(ctx.prefix())
            return self.scope.get(identifier)
        elif ctx.number():
            value, type = self.visit(ctx.number())
            return Atom(None, type, value)
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
        args: list[Atom] = self.visit(ctx.explist())
        passed = []
        for arg in args:
            if arg.type == "int":
                # print(arg, arg.value)
                # print(arg.value, arg.name, arg.type)
                passed.append(arg.value) # copy values of primitive types
            else:
                # passed.append(arg) # pass references to non-primitive types
                raise NotImplementedError

        # print(passed)

        if name in self.builtins:
            return self.builtins[name](self, *passed)
        else:
            # return value returned by function
            raise NotImplementedError


    def visitExplist(self, ctx:TuaParser.ExplistContext) -> list[Atom]:
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
        if ctx.INT():
            return int(ctx.getText()), "int"
        elif ctx.FLOAT():
            return float(ctx.getText()), "float"
        else:
            raise InternalError("Unknown number type")
