Object = {}
Object.__index = Object
Object[a[6]] = 7


function new() -> List[Union [int, List[string], List[Union[float,bool]]] ]
end

i: int = 5;
i = i + 4

function Objectextend() -> xd
  cls = {x = 3, "xd"="xd", 5, {1,2} = {1,{2,3}}}
  for k, v in pairs(self) do
    if find("__") == 1 then
      cls[k] = v
      return "error"
    end
  end
  cls.__index = cls
  cls.super = self
  setmetatable(cls, self)
  return cls
end

---------------

function Object:implement(...)
  for _, cls in pairs({...}) do
    for k, v in pairs(cls) do
      if self[k] == nil and type(v) == "function" then
        self[k] = v
      end
    end
  end
end


function Object:is(T)
  local mt = getmetatable(self)
  while mt do
    if mt == T then
      return true
    end
    mt = getmetatable(mt)
  end
  return false
end


function Object:__tostring()
  return "Object"
end


function Object:__call(...)
  local obj = setmetatable({}, self)
  obj:new(...)
  return obj
end


return Object