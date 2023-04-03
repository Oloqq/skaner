chunk =
    _ (stat ';'?)* _ (laststat ';'?)? _

block =
    chunk
    { return { type: "block", value: text() }; }

stat =
    varlist _ '=' _ explist
    { return { type: "stat", value: text() }; } /
    functioncall  /
    do _ block _ end  /
    while _ exp _ do _ block _ end  /
    repeat _ block _ until _ exp  /
    if _ exp _ then _ block _ (elseif _ exp _ then _ block)* (else _ block)? _ end  /
    for _ Name _ '=' _ exp _ ',' _ exp _ (',' _ exp)? _ do _ block _ end  /
    for _ namelist _ in _ explist _ do _ block _ end  /
    function _ funcname _ funcbody  /
    local _ function _ Name _ funcbody  /
    local _ namelist _ ('=' _ explist)?

laststat =
    return _ (explist)?  /  break

funcname =
    Name _ ('.' _ Name)* _ (':' _ Name)?

varlist =
    var _ (',' _ var)*

var =
    prefix _ (suffix)* _ index / Name

namelist =
    Name _ (',' _ Name)*

explist =
    (exp ',')* _ exp

value =
    nil / false / true / Number / String / '...' / function /
    tableconstructor / functioncall / var / '(' exp ')'

exp =
    value _ (binop _ exp)?  /  unop _ exp

prefix =
    '(' _ exp _ ')' / Name

index =
    '[' _ exp _ ']' / '.' Name

call =
    args / ':' _ Name _ args

suffix =
    call / index

prefixexp =
    var  /  functioncall  /  '(' _ exp _ ')'

functioncall =
    prefix _ (suffix)* _ call

args =
    '(' _ (explist)? _ ')'  /  tableconstructor  /  String

function =
    'function' _ funcbody

funcbody =
    '(' _ (parlist1)? _ ')' _ block _ end

parlist1 =
    namelist _ (',' '...')?  /  '...'

tableconstructor =
    '{' _ (fieldlist)? _ '}'

fieldlist =
    field _ (fieldsep _ field)* _ (fieldsep)?

field =
    '(' _ exp _ ')' _ '=' _ exp  /  Name _ '=' _ exp  /  exp

fieldsep =
    ','  /  ';'
    { return { type: "fieldsep", value: text() }; }

binop =
    '+'  /  '-'  /  '*'  /  '/'  /  '^'  /  '%'  /  '..'  /
            '<'  /  '<='  /  '>'  /  '>='  /  '=='  /  '~='  /
            and  /  or
    { return { type: "binop", value: text() }; }

unop =
    '-'  /  not  /  '#'
    { return { type: "unop", value: text() }; }

_ "(whitespace)*"
    = [ \t\n\r]*

// keywords
do = 'do' { return "keyword do"; }
end = 'end' { return "keyword end"; }
while = 'while' { return "keyword while"; }
repeat = 'repeat' { return "keyword repeat"; }
until = 'until' { return "keyword until"; }
if = 'if' { return "keyword if"; }
then = 'then' { return "keyword then"; }
else = 'else' { return "keyword else"; }
elseif = 'elseif' { return "keyword elseif"; }
for = 'for' { return "keyword for"; }
in = 'in' { return "keyword in"; }
local = 'local' { return "keyword local"; }
return = 'return' { return "keyword return"; }
break = 'break' { return "keyword break"; }
nil = 'nil' { return "keyword nil"; }
false = 'false' { return "keyword false"; }
true = 'true' { return "keyword true"; }
and = 'and' { return "keyword and"; }
or = 'or' { return "keyword or"; }
not = 'not' { return "keyword not"; }

// literals
Name = [a-z_]i[a-z0-9_]i* { return text(); }
Exponent = ('e''-'?[1-9][0-9]*)
Number =
    [0-9]+'.'[0-9]+ Exponent? /
    [1-9][0-9]* Exponent?
    { return text(); }
String = '"'.*'"' { return text(); }