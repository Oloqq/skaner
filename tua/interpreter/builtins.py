from .visitor import Tua
from .variables import Value

def print_(_: Tua, *args: Value):
    printables = []
    if len(args) > 0 and "List" in args[0].type.id:
        printables = list(map(lambda arg: arg.value, args[0].value))
        print(printables)
    else:
        printables = list(map(lambda arg: arg.value, args))
        print(*printables)


def dump_stack(visitor: Tua):
    print(f"Stack: ", visitor.scope)
