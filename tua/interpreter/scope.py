from pprint import pformat

# any identifiable value: variable, function, element of list, etc.
# literal is an atom with no name (name = None)
class Atom:
    def __init__(self, name, type, value) -> None:
        self.name: str|None = name
        self.type: str = type
        self.value: any = value

    def __repr__(self):
        return f"Atom({self.name}: {self.type} = {self.value})"

    def is_literal(self) -> bool:
        return self.name == None

Scope = dict[str, Atom]

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

    def get(self, identifier: str) -> Atom:
        return self.current[identifier]

    def set_exiting_atom(self, identifier: str, rhs: Atom):
        # TODO assert it exists?
        # existing_atom = self.current.get(identifier)

        # TODO assert rhs.type == self.current[identifier].type?

        self.current[identifier].value = rhs.value

    def new_atom(self, identifier: str, type: str, rhs: Atom):
        value = rhs.value if rhs.is_literal() else rhs
        self.current[identifier] = Atom(identifier, type, value)