class TuaList:
    def __init__(self, elem_type: str):
        self.content: list[any] = []
        self.type: str = elem_type

    def __repr__(self):
        return f"{self.full_type_str()} = [{self.content_str()}]"

    def full_type_str(self):
        return f"List[{self.type}]"

    def content_str(self):
        return str(self.content)

    def get(self, elem: int) -> any:
        return self.content[elem]

    def set(self, elem: int, val: any):
        if type(val) == self.type:
            self.content[elem] = val
    