from pprint import pformat
from .tualist import TuaList
from .variables import Value, Type

Scope = dict[str, Value]

class ScopeStack:
    def __init__(self):
        self.scopes: list[Scope] = []
        self.current: Scope
        self.push()

    def __repr__(self):
        return f"ScopeStack({pformat(self.scopes)})"

    def push(self):
        self.current = Scope()
        self.scopes.append(self.current)

    def pop(self):
        self.scopes.pop()
        self.current = self.scopes[-1]

    def get(self, identifier: str) -> Value|None:
        for scope in reversed(self.scopes):
            if identifier in scope.keys():
                return scope[identifier]

        return None


    def get_functions(self) -> list:
        functions = []

        for scope in reversed(self.scopes):
            for elem in scope.items():
                if elem[1].type.id == "function":
                    functions.append([elem[0], elem[1]])

        return functions


    def change_value(self, identifier: str, rhs: Value):
        for scope in reversed(self.scopes):
            if identifier in scope.keys():
                existing_atom = scope[identifier]
                if existing_atom.type.id == rhs.type.id:
                    scope[identifier].value = rhs.value
                    return
                else:
                    print("Type mismatch")
                    return

        print(f"Identifier '{identifier}' does not exist")


    def change_value_with_suffix(self, identifier: str, rhs: Value, suffix: any):
        for scope in reversed(self.scopes):
            if identifier in scope.keys():
                existing_atom = scope[identifier]

                if suffix > existing_atom.value.length() or suffix < 0:
                    print(f"Index {suffix} out of bounds")
                    return

                if existing_atom.type.id == f'List[{rhs.type.id}]':
                    existing_atom.value.content[suffix].value = rhs.value
                    return
                else:
                    print("Type mismatch")
                    return

        print(f"Identifier '{identifier}' does not exist")


    def new_identifier(self, identifier: str, val: Value) -> bool:
        # check if variable already exists
        if self.get(identifier) is None:
            self.current[identifier] = val
            return True

        return False


    def del_identifier(self, identifier: str) -> bool:
        for scope in reversed(self.scopes):
            if identifier in scope.keys():
                scope.pop(identifier)
                return True

        return False