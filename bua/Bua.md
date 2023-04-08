# Obciecie gramatyki
- zostajemy przy oficjalnej gramatyce (na razie)
- tylko pojedyncze przypisania
  - bez `a, b, c = 1, 2, 3`
- powiedzmy ze table ma indeksy tylko int lub string

### sprawdz czy pairs iteruje po funkcjach

w ast sprawdzamy
- przypisania
- przekazywanie argumentow
- dodawanie do tablic (to samo co wczesniejsze)
- nie pozwalamy na typ any

# Definicja typu
- definicja zmiennej
- return funkcji
- argumenty funkcji
- poki co @, moze : nie zepsuje gramatyki

```lua
local b @int = 4

function name(x @int, y @int) -> int
    return 2
end

for i=1,10 do
    print(i)
end

object @Table = {x = 2, y = 3,
    bruh = function() -> int return 2 end
    }
array @List[ Union[int, string] ] = {2, 3, 4, "dd", nil, nil, 10}
print(array[7]) -- nil
array[#array + 10] = 3
table.insert(array, 3)

for i, value in ipairs(array) do

end

for k, value in pairs(object) do

end

-- tu jest problem wiec jebac any
x @any = 1
y @number

y = x -- warning lub error
if type(x) == "number" then
    y = x -- ok
end

```

```python
x: any
if isinstance(x, str):
  x.replace()
```