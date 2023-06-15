from .visitor import Tua
from .variables import Value, Type
from .tualist import TuaList

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

def type_(_: Tua, arg: Value):
    return Value(Type("string"), arg.type.__repr__())

def len_(_: Tua, arg: Value):
    if "List" in arg.type.id:
        return Value(Type("int"), arg.value.length())
    elif arg.type.id == "string":
        return Value(Type("int"), len(arg.value))
    else:
        raise TypeError(f"Object of type '{arg.type.id}' has no len()")


def concat_(_: Tua, list1: Value, list2: Value):
    if list1.type.id != list2.type.id and "List" in list1.type.id and "List" in list2.type.id:
        raise TypeError(f"Cannot concatenate {list1.type.id} and {list2.type.id}")

    new_list = []
    for elem in list1.value.content:
        new_list.append(elem.copy())
    
    for elem in list2.value.content:
        new_list.append(elem.copy())

    tualist = TuaList(new_list, list1.value.type)
    return Value(Type(tualist.full_type_str()), tualist)

def dump_stack(visitor: Tua):
    print(f"Stack: ", visitor.scope)
