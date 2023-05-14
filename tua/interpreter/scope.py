from pprint import pformat

class Atom:
    def __init__(self, name, type, value) -> None:
        self.name: str|None = name
        self.type: str = type
        self.value: any = value

    def __repr__(self):
        return f"Atom({self.name}: {self.type} = {self.value})"

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

    def set(self, identifier: str, type: str, value: any):
        self.current[identifier] = Atom(identifier, type, value)