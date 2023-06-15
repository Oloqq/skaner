from .variables import Value

class TuaList:
    def __init__(self, content: list[Value], elem_type: str ):
        self.content: list[Value] = content
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
        if val.type.id == self.type:
            self.content[elem] = val

    def append(self, val: Value):
        if val.type.id == self.type:
            self.content.append(val)
    
    def pop(self):
        return self.content.pop()
            

    