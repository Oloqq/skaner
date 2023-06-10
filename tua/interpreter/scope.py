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

    def get(self, identifier: str) -> Value:
        for scope in reversed(self.scopes):
            if identifier in scope.keys():
                return scope[identifier]
        
        return None

    def change_value(self, identifier: str, rhs: Value):

        # TODO
        # it only works for literals -> do list etc

        if identifier in self.current.keys():
            existing_atom = self.current[identifier]
            # print(f'do {identifier}: {existing_atom} przypisać {rhs}')
            
            if existing_atom.type.id == rhs.type.id:
                self.current[identifier].value = rhs.value
            else:
                print("Type mismatch")
        else:
            print("Variable does not exist")

        # self.current[identifier].value = rhs.value

    def new_identifier(self, identifier: str, val: Value) -> bool:
        # value = rhs.value if rhs.is_literal() else rhs

        # check if variable already exists
        if self.get(identifier) is None:
            self.current[identifier] = val
            return True
        
        return False
    