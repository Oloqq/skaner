from .visitor import Tua
from .variables import Value

def print_(_: Tua, *args: Value):
    printables = []
    for arg in args:
        if arg.type.id == "bool":
            printables.append(str(arg.value).lower())
        elif "List" in arg.type.id:
            printables.append(list(map(lambda e: e.value, arg.value)))
        else:
            printables.append(arg.value)
    print(*printables)

def type_(_: Tua, arg: Value):
    return arg.type.__repr__

def dump_stack(visitor: Tua):
    print(f"Stack: ", visitor.scope)
