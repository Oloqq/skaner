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

    def setval(self, identifier: str, type: str, rhs: Atom):
        atom = self.current.get(identifier)
        if atom:
            # TODO assert type is not violated
            atom.value = rhs
            raise NotImplementedError
        else: # uhuuhhu new variable incoming :DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
            value = rhs.value if rhs.is_literal() else rhs
            self.current[identifier] = Atom(identifier, type, value)