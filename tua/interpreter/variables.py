from typing_extensions import Self

primitives = set(
    ["int", "float", "string", "bool"]
)

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
        return f"{self.type.id} = {self.value}"

    def copy(self) -> Self:
        if self.type.id in primitives:
            return Value(self.type, self.value)
        else:
            return self

    def deepcopy() -> Self:
        raise NotImplementedError
