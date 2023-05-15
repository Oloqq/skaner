class Type:
    def __init__(self, id: str):
        self.id: str = id

class Value:
    def __init__(self, type: Type, value: any):
        self.type: Type = type
        self.value: any = value

class Var:
    def __init__(self, name: str, value: Value):
        self.name: str = name
        self.value: Value = value