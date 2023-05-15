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
        return self.current[identifier]

    def set_existing_atom(self, identifier: str, rhs: Value):
        # TODO assert it exists?
        # existing_atom = self.current.get(identifier)

        # TODO assert rhs.type == self.current[identifier].type?

        self.current[identifier].value = rhs.value

    def new_atom(self, identifier: str, val: Value):
        # value = rhs.value if rhs.is_literal() else rhs
        self.current[identifier] = val