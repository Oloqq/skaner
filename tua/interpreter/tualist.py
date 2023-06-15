class TuaList:
    def __init__(self, content: list[any], elem_type: str ):
        self.content: list[any] = content
        self.type: str = elem_type

    def __repr__(self):
        return self.content_str()

    def full_type_str(self):
        return f"List[{self.type}]"

    def content_str(self):
        return str(self.content)

    def length(self):
        return len(self.content)

    def get(self, elem: int) -> any:
        return self.content[elem]

    def set(self, elem: int, val: any):
        if type(val) == self.type:
            self.content[elem] = val

    def append(self, val: any):
        if type(val) == self.type:
            self.content.append(val)

    