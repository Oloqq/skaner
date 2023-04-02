chunk =
    _ (stat ';'?)* _ (laststat ';'?)? _

block =
    chunk

stat =
    varlist '=' explist /
    functioncall  /
    do block end  /
    while exp do block end  /
    repeat block until exp  /
    if exp then block (elseif exp then block)* (else block)? end  /
    for Name '=' exp ',' exp (',' exp)? do block end  /
    for namelist in explist do block end  /
    function funcname funcbody  /
    local function Name funcbody  /
    local namelist ('=' explist)?

laststat =
    return (explist)?  /  break

funcname =
    Name ('.' Name)* (':' Name)?

varlist =
    var (',' var)*

var =
    Name  /  prefixexp '[' exp ']'  /  prefixexp '.' Name

namelist =
    Name (',' Name)*

explist =
    (exp ',')* exp

exp =
    nil  /  false  /  true  /  Number  /  String  /  '...'  /
    function  /  prefixexp  /  tableconstructor  /  exp binop exp  /  unop exp

prefixexp =
    var  /  functioncall  /  '(' exp ')'

functioncall =
    prefixexp args  /  prefixexp ':' Name args

args =
    '(' (explist)? ')'  /  tableconstructor  /  String

function =
    function funcbody

funcbody =
    '(' (parlist1)? ')' block end

parlist1 =
    namelist (',' '...')?  /  '...'

tableconstructor =
    '(' (fieldlist)? ')*'

fieldlist =
    field (fieldsep field)* (fieldsep)?

field =
    '(' exp ')?' '=' exp  /  Name '=' exp  /  exp

fieldsep =
    ','  /  ';'

binop =
    '+'  /  '-'  /  '*'  /  '/'  /  '^'  /  '%'  /  '..'  /
            '<'  /  '<='  /  '>'  /  '>='  /  '=='  /  '~='  /
            and  /  or

unop =
    '-'  /  not  /  '#'

_ "whitespace"
    = [ \t\n\r]*

// keywords
do = 'do'
end = 'end'
while = 'while'
repeat = 'repeat'
until = 'until'
if = 'if'
then = 'then'
else = 'else'
elseif = 'elseif'
for = 'for'
in = 'in'
local = 'local'
return = 'return'
break = 'break'
nil = 'nil'
false = 'false'
true = 'true'
and = 'and'
or = 'or'
not = 'not'

// literals
Name = [a-z_]i[a-z0-9_]i* { return text(); }
Exponent = ('e''-'?[1-9][0-9]*)
Number =
    [0-9]+'.'[0-9]+ Exponent? /
    [1-9][0-9]* Exponent?
    { return text(); }
String = '"'.*'"' { return text(); }