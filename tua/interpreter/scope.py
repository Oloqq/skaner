from pprint import pformat
from .tualist import TuaList
from .variables import Value, Type
import re

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

    def change_value(self, identifier: str, rhs: Value):
        index = None
        pattern = r"\[\d+\]$"

        if re.search(pattern, identifier):
            identifier, sep1, after = identifier.partition('[')
            index, sep2, after = after.partition(']')
            index = int(index)

        for scope in reversed(self.scopes):
            if identifier in scope.keys():
                existing_atom = scope[identifier]
                
                if index is not None:
                    if index > len(existing_atom.value) or index < 0:
                        print(f"Index {index} out of bounds")
                        return
                    if existing_atom.type.id == f'List[{rhs.type.id}]':
                        existing_atom.value[index].value = rhs.value
                        return
                    else:
                        print("Type mismatch")
                        return
                else:
                    if existing_atom.type.id == rhs.type.id:
                        scope[identifier].value = rhs.value
                        return
                    else:
                        print("Type mismatch")
                        return


        print(f"Identifier '{identifier}' does not exist")

    def new_identifier(self, identifier: str, val: Value) -> bool:
        # value = rhs.value if rhs.is_literal() else rhs

        # check if variable already exists
        if self.get(identifier) is None:
            self.current[identifier] = val
            return True

        return False
