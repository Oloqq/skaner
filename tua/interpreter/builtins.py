from .visitor import Tua

def print_(_: Tua, *args):
    print(*args)

def dump_stack(visitor: Tua, *args):
    print(f"Stack: ", visitor.scope)