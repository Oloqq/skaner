from .visitor import Tua
from .variables import Value

def print_(_: Tua, *args: Value):
    printables = []
    for arg in args:
        if arg.type.id == "bool":
            printables.append(str(arg.value).lower())
        elif "List" in arg.type.id:
            printables.append(list(map(lambda e: e.value, arg.value.content)))
        elif arg.value is None:
            printables.append("nil")
        else:
            printables.append(arg.value)
    print(*printables)


# need to fix functioncall first <- recursion required
def type_(_: Tua, arg: Value):
    return arg.type.__repr__

# it probably works but have to fix functioncall first
def len_(_: Tua, arg: Value):
    if "List" in arg.type.id:
        return len(arg.value)
    elif arg.type.id == "string":
        return len(arg.value)
    else:
        raise TypeError(f"Object of type '{arg.type.id}' has no len()")

def dump_stack(visitor: Tua):
    print(f"Stack: ", visitor.scope)
