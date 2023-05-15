class Type:
    def __init__(self, id: str):
        self.id: str = id

    def __repr__(self):
        return f"Type<{self.id}>"

class Value:
    def __init__(self, type: Type, value: any):
        self.type: Type = type
        self.value: any = value

    def __repr__(self):
        return f"{self.type.id}({self.value})"
