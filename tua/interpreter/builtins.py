from .visitor import Tua
from .variables import Value

def print_(_: Tua, *args: Value):
    printables = list(map(lambda arg: arg.value, args))
    print(*printables)

def dump_stack(visitor: Tua):
    print(f"Stack: ", visitor.scope)
