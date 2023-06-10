from .generated.TuaVisitor import TuaVisitor
from .generated.TuaParser import TuaParser
from .log import log
from .scope import ScopeStack
from .tualist import TuaList
from .variables import Value, Type, Function, Param
from .tualist import TuaList

class InternalError(Exception):
    pass

class SemanticError(Exception):
    pass

class Tua(TuaVisitor):
    def __init__(self):
        self.scope: ScopeStack = ScopeStack()
        from . import builtins
        self.builtins = {
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
        self.visitChildren(ctx)

    def visitNewvariable(self, ctx:TuaParser.NewvariableContext):
        log.info("Newvariable")
        lhs: Value
        type_annotated: Type
        lhs, type_annotated = self.visit(ctx.nametype())
        rhs: Value = self.visit(ctx.exp())
        if rhs.type.id != type_annotated.id:
            if rhs.type.id == "List[]":
                rhs.type.id = type_annotated.id
            else:
                raise SemanticError(f"Type mismatch: ({rhs.type.id}) ({type_annotated.id})")
            
        var_added_successfully = self.scope.new_identifier(lhs, rhs)

        if not var_added_successfully:
            raise SemanticError(f"Variable named '{lhs}' is already defined")

    def visitAssignment(self, ctx:TuaParser.AssignmentContext):
        log.info("Assignment")
        identifier = self.visit(ctx.var())
        value = self.visit(ctx.exp()) 
        self.scope.change_value(identifier, value)

    def visitVar(self, ctx:TuaParser.VarContext) -> str:
        log.info("Var")
        name = ctx.getToken(TuaParser.NAME, 0).getText()
        if ctx.suffix():
            suffix = self.visit(ctx.suffix())
            return f"{name}{suffix}"
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
        # how to handle list access? when return( eg. print(x[0]) )/assign( eg. x[1] = 5 ) value 
        if ctx.exp():
            arg: Value = self.visit(ctx.exp())
            return arg.value
        return self.visitChildren(ctx)


    def visitExp(self, ctx:TuaParser.ExpContext) -> Value:
        log.info("Exp")
        if ctx.parexp():
            return self.visit(ctx.parexp())
        elif ctx.number():
            value, type = self.visit(ctx.number())
            assert isinstance(type, Type)
            assert isinstance(type.id, str)

            return Value(type, value)
        elif ctx.string():
            return self.visit(ctx.string())
        elif ctx.bool_():
            value, type = self.visit(ctx.bool_())
            return Value(type, value)
        # nil
        elif ctx.prefix():
            identifier = self.visit(ctx.prefix())
            ret = self.scope.get(identifier)
            
            if ret is None:
                raise SemanticError(f"Name '{identifier}' is not defined")
            
            assert isinstance(ret.type, Type)
            assert isinstance(ret.type.id, str)
            return ret
        
        elif ctx.binopPower():
            base = self.visit(ctx.exp(0))
            exp = self.visit(ctx.exp(1))
            
            # check if the values are numbers
            if base.type.id in ("int", "float") and exp.type.id in ("int", "float"):
                result = pow(base.value, exp.value)
                type_ = Type("int") if isinstance(result, int) else Type("float")

                return Value(type_, result)
            
            raise SemanticError(f"Trying to use operator '^' on {base.type} and {exp.type}")
                    
        elif ctx.unop():
            operators = {
                '-' : lambda x : -x,
                'not' : lambda x: not x
            }

            value = self.visit(ctx.exp(0))
            op = self.visit(ctx.unop())

            # check if the correct operator was used on given type
            if (isinstance(value.value, int) and not isinstance(value.value, bool) and op == '-') or (isinstance(value.value, float) and not isinstance(value.value, bool) and op == '-') or (isinstance(value.value, bool) and op == 'not'):
                return Value(value.type, operators[op](value.value))
            
            raise SemanticError(f"Trying to use operator '{op}' on {value.type}")            
        
        elif ctx.binopMulDivMod():
            operators = {
                '*' : lambda x, y : x * y,
                '/' : lambda x, y : x / y,
                '%' : lambda x, y : x % y,
                '//' : lambda x, y : x // y
            }

            val_left = self.visit(ctx.exp(0))
            val_right = self.visit(ctx.exp(1))
            
            op = self.visit(ctx.binopMulDivMod())

            # check if the values are numbers
            if val_left.type.id in ("int", "float") and val_right.type.id in ("int", "float"):
                result = operators[op](val_left.value, val_right.value)
                type_ = Type("int") if isinstance(result, int) else Type("float")

                return Value(type_, result)
            
            raise SemanticError(f"Trying to use operator '{op}' on {val_left.type} and {val_right.type}")            

        elif ctx.binopAddSub():
            operators = {
                '+' : lambda x, y : x + y,
                '-' : lambda x, y : x - y,
            }

            val_left = self.visit(ctx.exp(0))
            val_right = self.visit(ctx.exp(1))
            
            op = self.visit(ctx.binopAddSub())

            # check if the values are numbers
            if val_left.type.id in ("int", "float") and val_right.type.id in ("int", "float"):
                result = operators[op](val_left.value, val_right.value)
                type_ = Type("int") if isinstance(result, int) else Type("float")

                return Value(type_, result)
            
            raise SemanticError(f"Trying to use operator '{op}' on {val_left.type} and {val_right.type}")

        elif ctx.binopConcat():
            val_left = self.visit(ctx.exp(0))
            val_right = self.visit(ctx.exp(1))

            if val_left.type.id == "string" and val_right.type.id == "string":
                return Value(Type("string"), val_left.value + val_right.value)
            
            raise SemanticError(f"Trying to use operator '..' on {val_left.type} and {val_right.type}")

        
        elif ctx.binopComparison():
            operators = {
                '==' : lambda x, y : x == y,
                '~=' : lambda x, y : x != y,
                '<=' : lambda x, y : x <= y,
                '>=' : lambda x, y : x >= y,
                '<' : lambda x, y : x < y,
                '>' : lambda x, y : x > y,
            }

            val_left = self.visit(ctx.exp(0))
            val_right = self.visit(ctx.exp(1))
            
            op = self.visit(ctx.binopComparison())

            # check if the correct operator was used on given types
            if (op in ('==', '~=') and val_left.type.id == val_right.type.id) or (op in ('<=', '>=', '<', '>') and val_left.type.id in ("int", "float", "string") and val_left.type.id == val_right.type.id):
                return Value(Type("bool"), operators[op](val_left.value, val_right.value))
            
            raise SemanticError(f"Trying to use operator '{op}' on {val_left.type} and {val_right.type}")
        
        elif ctx.binopAnd():
            operators = {
                'and' : lambda x, y : x and y,
                '&' : lambda x, y : x & y, 
            }

            val_left = self.visit(ctx.exp(0))
            val_right = self.visit(ctx.exp(1))
            op = self.visit(ctx.binopAnd())
            
            # check if the correct operator was used on given types
            if val_left.type.id == "bool" and val_right.type.id == "bool":
                return Value(Type("bool"), operators[op](val_left.value, val_right.value))

            raise SemanticError(f"Trying to use operator '{op}' on {val_left.type} and {val_right.type}")
        
        elif ctx.binopOr():
            operators = {
                'or' : lambda x, y : x or y,
                '|' : lambda x, y : x | y, 
            }

            val_left = self.visit(ctx.exp(0))
            val_right = self.visit(ctx.exp(1))
            op = self.visit(ctx.binopOr())

            # check if the correct operator was used on given types
            if val_left.type.id == "bool" and val_right.type.id == "bool":
                return Value(Type("bool"), operators[op](val_left.value, val_right.value))
            
            raise SemanticError(f"Trying to use operator '{op}' on {val_left.type} and {val_right.type}")
        
        elif ctx.tableconstructor():
            return self.visit(ctx.tableconstructor())  
        
        else:
            raise InternalError
        

    def visitParexp(self, ctx:TuaParser.ParexpContext):
        return self.visit(ctx.exp())


    def visitFunctionbody(self, ctx:TuaParser.FunctionbodyContext) -> tuple[list[Type], Type, TuaParser.BlockContext]:
        log.info("Functionbody")
        params = [] # TEMP
        return params, Type("nil"), ctx.block()


    def visitDostat(self, ctx:TuaParser.DostatContext):
        return self.visitChildren(ctx)


    def visitWhilestat(self, ctx:TuaParser.WhilestatContext):
        return self.visitChildren(ctx)


    def visitIfstat(self, ctx:TuaParser.IfstatContext):
        n_exps = len(ctx.exp())
        n_blocks = len(ctx.block())

        # if and elseifs
        for i in range(n_exps):
            if self.visit(ctx.exp(i)).value:
                return self.visit(ctx.block(i))

        # else
        if n_blocks > n_exps:
            return self.visit(ctx.block(n_blocks - 1))


    def visitForintstat(self, ctx:TuaParser.ForintstatContext):
        return self.visitChildren(ctx)


    def visitForiteratorstat(self, ctx:TuaParser.ForiteratorstatContext):
        return self.visitChildren(ctx)


    def visitFunctiondef(self, ctx:TuaParser.FunctiondefContext):
        name = ctx.getToken(TuaParser.NAME, 0).getText()
        params, returns, block = self.visit(ctx.functionbody())
        func = Function(name, returns, params, block)
        self.scope.new_identifier(name, Value(Type("function"), func))


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
        type = "" 
        if ctx.fieldlist():
            fields, type = self.visit(ctx.fieldlist())
        else:
            fields = []   
        tualist = TuaList(type)   
        tualist.content = fields  
        return Value(Type(tualist.full_type_str()), tualist.content) 


    def visitFieldlist(self, ctx:TuaParser.FieldlistContext):
        log.info("Fieldlist")
        children = []
        types = []
        for c in ctx.getChildren():
            if isinstance(c, TuaParser.FieldContext):
                child = self.visit(c)
                types.append(child.type.id)
                children.append(child)
        types = set(types)
        if len(types) > 1:
            raise SemanticError(f"Fieldlist contains multiple types: {types}")
        return children, types.pop()


    def visitField(self, ctx:TuaParser.FieldContext):
        log.info("Field")
        return self.visitChildren(ctx)


    def visitBinopAddSub(self, ctx:TuaParser.BinopAddSubContext):
        log.info("BinopAddSub")
        return ctx.getText();


    def visitBinopMulDivMod(self, ctx:TuaParser.BinopMulDivModContext):
        log.info("BinopMulDivMod")
        return ctx.getText();


    def visitBinopComparison(self, ctx:TuaParser.BinopComparisonContext):
        log.info("BinopComparison")
        return ctx.getText();


    def visitBinopConcat(self, ctx:TuaParser.BinopConcatContext):
        log.info("BinopConcat")
        return ctx.getText();


    def visitBinopAnd(self, ctx:TuaParser.BinopAndContext):
        log.info("BinopAnd")
        return ctx.getText();


    def visitBinopOr(self, ctx:TuaParser.BinopOrContext):
        log.info("BinopOr")
        return ctx.getText();


    def visitBinopPower(self, ctx:TuaParser.BinopPowerContext):
        log.info("BinopPower")
        return ctx.getText();


    def visitUnop(self, ctx:TuaParser.UnopContext):
        log.info("Unop")
        return ctx.getText();


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


    def visitBool(self, ctx:TuaParser.BoolContext):
        if ctx.TRUE():
            return True, Type("bool")
        if ctx.FALSE():
            return False, Type("bool")
