print(420)
print("yooo")

print ("spaced")

local x = 14

if x == 15 then
    print(x + 2)
elseif x == 14 then
    print(x - 7)
else
    print("bruh")
end

function Bruh:new(o)
    o = o or {}
    setmetatable(o, self)
    self.__index = self
    return o
end

function Bruh:yeet()
    print("yeet \" escaped \" yeet")
end

local uh = Bruh:new()
uh:yeet()

local arr = {1, 2, 3}
for i, v in ipairs(arr) do
    print(i, v)
end

-- comment
local tab = {a=1, b=2} -- inline comment
for k, v in pairs(tab) do
    print(k, v)
end

print(#tab)
