from typing_extensions import Self
from .generated.TuaParser import TuaParser
from .generated.TuaVisitor import TuaVisitor
from .log import log

primitives = set(
    ["int", "float", "string", "bool"]
)

class Type:
    def __init__(self, id: str):
        self.id: str = id

    def __repr__(self):
        return f"Type<{self.id}>"

class Value:
    def __init__(self, type: Type, value: any):
        self.type: Type = type
        self.value: any = value

    def __repr__(self):
        return f"{self.type.id} = {self.value}"

    def copy(self) -> Self:
        if self.type.id in primitives:
            return Value(self.type, self.value)
        else:
            return self

    def deepcopy() -> Self:
        raise NotImplementedError

class Param:
    def __init__(self, name: str, type: Type):
        self.name: str = name
        self.type: Type = type

    def __repr__(self):
        return f"Param<{self.name}: {self.type}>"

class Function:
    def __init__(self, name: str, returns: Type, params: list[Param], body: TuaParser.BlockContext):
        self.name: str = name
        self.returns: Type = returns
        self.params: list[str] = params
        self.body: TuaParser.BlockContext = body

    def __repr__(self):
        return f"Function<{self.returns}%{self.params}>)"

    def execute(self, visitor: TuaVisitor, args: list[Value] = []) -> Value:
        # scope will be pushed upon visiting block
        # options
        # 1. visit block no longer manages scope stack (tiresome) (fuck this)
        # 2. execute goes directly into blocks children and manges the stack (may become buggy if visitBlock will be modified one day, and this code not)
        # 3. scope stack holds a buffer used to init the next scope
        log.debug(f"user defined function {self.name}")
        return visitor.visit(self.body)
