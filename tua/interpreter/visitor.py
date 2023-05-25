from .generated.TuaVisitor import TuaVisitor
from .generated.TuaParser import TuaParser
from .log import log
from .scope import ScopeStack
from .tualist import TuaList
from .variables import Value, Type, Function, Param

class InternalError(Exception):
    pass

class SemanticError(Exception):
    pass

class Tua(TuaVisitor):
    def __init__(self):
        self.scope: ScopeStack = ScopeStack()
        from . import builtins
        self.builtins = {
            # "type": builtins.type_, 
            "print": builtins.print_,
            "dump_stack": builtins.dump_stack,
        }
        self.cnt = 0 # for temporary testing


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
        if ctx.newvariable() or ctx.assignment() or ctx.functioncall(): # TODO make sure this functioncall does not mess up functioncall in for x,y in ...
            return self.visitChildren(ctx)
        # do block end
        # while
        # if
        # for x=...
        # for x, y in ...
        elif ctx.functionbody():
            name = ctx.getToken(TuaParser.NAME, 0).getText()
            params, returns, block = self.visit(ctx.functionbody())
            func = Function(name, returns, params, block)
            self.scope.new_identifier(name, Value(Type("function"), func))
        else:
            raise NotImplementedError

    def visitNewvariable(self, ctx:TuaParser.NewvariableContext):
        log.info("Newvariable")
        lhs: Value
        type_annotated: Type
        lhs, type_annotated = self.visit(ctx.nametype())
        rhs: Value = self.visit(ctx.exp())
        if rhs.type.id != type_annotated.id:
            raise SemanticError(f"Type mismatch: ({rhs.type.id}) ({type_annotated.id})")
        self.scope.new_identifier(lhs, rhs)

    def visitAssignment(self, ctx:TuaParser.AssignmentContext):
        log.info("Assignment")
        identifier = self.visit(ctx.var())
        value = self.visit(ctx.exp())
        self.scope.change_value(identifier, value)

    def visitVar(self, ctx:TuaParser.VarContext) -> str:
        log.info("Var")
        name = ctx.getToken(TuaParser.NAME, 0).getText()
        if ctx.suffix():
            # suffix = self.visit(ctx.suffix())
            raise NotImplementedError
        return name


    def visitNametype(self, ctx:TuaParser.NametypeContext) -> tuple[str, Type]:
        log.info("Nametype")
        name = ctx.NAME().getText()
        type = self.visit(ctx.type_())
        return (name, type)


    def visitType(self, ctx:TuaParser.TypeContext) -> Type:
        log.info("Type")
        if ctx.NAME():
            return Type(ctx.NAME().getText())
        elif ctx.NIL():
            return Type("nil")
        elif ctx.listType():
            return self.visit(ctx.listType())
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


    def visitListType(self, ctx:TuaParser.ListTypeContext) -> Type:
        log.info("ListType")
        elem_type: Type = self.visit(ctx.type_())
        return Type(f"List[{elem_type.id}]")


    def visitPrefix(self, ctx:TuaParser.PrefixContext):
        log.info("Prefix")
        if ctx.var():
            return self.visit(ctx.var())
        else:
            return NotImplementedError # functioncall


    def visitSuffix(self, ctx:TuaParser.SuffixContext):
        log.info("Suffix")
        return self.visitChildren(ctx)


    def visitExp(self, ctx:TuaParser.ExpContext) -> Value:
        log.info("Exp")
        if ctx.number():
            value, type = self.visit(ctx.number())
            assert isinstance(type, Type)
            assert isinstance(type.id, str)

            return Value(type, value)
        elif ctx.string():
            return self.visit(ctx.string())
        #true, false, nil
        elif ctx.prefix():
            identifier = self.visit(ctx.prefix())
            ret = self.scope.get(identifier)
            assert isinstance(ret.type, Type)
            assert isinstance(ret.type.id, str)
            return ret
        #power, unop?, muldivmod, addsub, concat, comp, and, or, unop?
        elif ctx.tableconstructor():
            return self.visit(ctx.tableconstructor())
        else:
            raise InternalError


    def visitFunctionbody(self, ctx:TuaParser.FunctionbodyContext) -> tuple[list[Type], Type, TuaParser.BlockContext]:
        log.info("Functionbody")
        params = [] # TEMP
        return params, Type("nil"), ctx.block()


    def visitLaststat(self, ctx:TuaParser.LaststatContext):
        log.info("Laststat")
        return self.visitChildren(ctx)


    def visitTypednamelist(self, ctx:TuaParser.TypednamelistContext):
        log.info("Typednamelist")
        return self.visitChildren(ctx)

    def get_args(self, ctx:TuaParser.FunctioncallContext) -> list[Value]:
        if not ctx.explist():
            return []

        args: list[Value] = self.visit(ctx.explist())
        passed = list(map(lambda arg: arg.copy(), args))
        return passed

    def visitFunctioncall(self, ctx:TuaParser.FunctioncallContext):
        log.info(f"Functioncall")
        name = ctx.getToken(TuaParser.NAME, 0).getText()
        args = self.get_args(ctx)

        if name in self.builtins: # TODO order of the checks should be swapped, or overriding builtins banned, to be decided
            return self.builtins[name](self, *args)
        else:
            func = self.scope.get(name)
            if func.type.id != "function":
                raise SemanticError(f"Trying to call non-function {name}")
            func.value.execute(self, *args)
            return None


    def visitExplist(self, ctx:TuaParser.ExplistContext) -> list[Value]:
        log.info("Explist")
        vals = []
        for c in ctx.getChildren():
            vals.append(self.visit(c))
        return vals


    def visitTableconstructor(self, ctx:TuaParser.TableconstructorContext) -> Value:
        log.info("Tableconstructor")
        if ctx.fieldlist():
            fields = self.visit(ctx.fieldlist())
        else:
            fields = []

        return Value(Type("List[int]"), fields)
        # ret = Value(Type("List[int]"), [self.cnt, self.cnt + 1]) # TEMP
        # self.cnt += 2
        # return ret


    def visitFieldlist(self, ctx:TuaParser.FieldlistContext):
        log.info("Fieldlist")
        children = []
        for c in ctx.getChildren():
            if isinstance(c, TuaParser.FieldContext):
                children.append(self.visit(c).value)
        return children


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


    def visitString(self, ctx:TuaParser.StringContext) -> Value:
        content =  ctx.getText()[1:-1] # skip quotes
        return Value(Type("string"), content)


    def visitNumber(self, ctx:TuaParser.NumberContext) -> Type:
        if ctx.INT():
            return int(ctx.getText()), Type("int")
        elif ctx.FLOAT():
            return float(ctx.getText()), Type("float")
        else:
            raise InternalError("Unknown number type")
