/*
return {
    speak = function ()
        print("meow")
    end,
    x = 3
}

comments
*/

{}

chunk =
    _ stats:(stat_semicolon)* laststat:(laststat_semicolon)?
    { return { node: "chunk", body: stats, laststat: laststat }; }

stat_semicolon =
    s:stat _ ';'? _
    { return s; }

laststat_semicolon =
    s:laststat _ ';'? _
    { return s; }

block =
    c:chunk
    { return { node: "block", value: c }; }

stat =
    lhs:varlist _ '=' _ rhs:explist
    { return { node: "assignment", lhs: lhs, rhs: rhs }; } /
    functioncall  /
    do _ block _ end  /
    while _ exp _ do _ block _ end  /
    repeat _ block _ until _ exp  /
    if _ exp _ then _ block _ (elseif _ exp _ then _ block)* (else _ block)? _ end  /
    for _ Name _ '=' _ exp _ ',' _ exp _ (',' _ exp)? _ do _ block _ end  /
    for _ namelist _ in _ explist _ do _ block _ end  /
    'function' _ funcname _ funcbody  /
    local _ 'function' _ Name _ funcbody  /
    local _ lhs:namelist _ '=' _ rhs:explist
    { return { node: "declaration", lhs: lhs, rhs: rhs }; } /
    local _ lhs:namelist
    { return { node: "declaration", lhs: lhs, rhs: undefined }; }

laststat =
    return _ (explist)?  /  break

funcname =
    Name _ ('.' _ Name)* _ (':' _ Name)?

varlist =
    v1:var varlist:(comma_var)*
    {
        if (!varlist) {
            varlist = [];
        }
        varlist.unshift(v1);
        return { node: "varlist", value: varlist };
    }

comma_var = _ ',' _ v:var { return v; }

var =
    prefix _ suffix+ / Name

namelist =
    n1:Name namelist:(comma_name)*
    {
        if (!namelist) {
            namelist = [];
        }
        namelist.unshift(n1);
        return { node: "namelist", value: namelist };
    }

comma_name =
    _ ',' _ n:Name { return n; }

explist =
    e1:exp explist:(comma_exp)*
    {
        if (!explist) {
            explist = [];
        }
        explist.unshift(e1);
        return { node: "explist", value: explist };
    }

comma_exp = _ ',' _ e:exp { return e; }

value =
    nil / false / true / Number / String / '...' / function /
    tableconstructor / functioncall / var / '(' exp ')'

// stub
exp =
    v:value _ (binop _ exp)?
    { return { value: v }; } /
    unop _ exp

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
    prefix _ (suffix)+

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
    '[' _ exp _ ']' _ '=' _ exp  /  Name _ '=' _ exp  /  exp

fieldsep =
    ','  /  ';'
    { return { node: "fieldsep", value: text() }; }

binop =
    '+'  /  '-'  /  '*'  /  '/'  /  '^'  /  '%'  /  '..'  /
            '<'  /  '<='  /  '>'  /  '>='  /  '=='  /  '~='  /
            and  /  or
    { return { node: "binop", value: text() }; }

unop =
    '-'  /  not  /  '#'
    { return { node: "unop", value: text() }; }

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
Name = [a-zA-Z_]i[a-zA-Z0-9_]i* { return text(); }
Exponent = ('e''-'?[1-9][0-9]*)
Number =
    [0-9]+'.'[0-9]+ Exponent? /
    [0-9][0-9]* Exponent?
    { return text(); }

String	=
    '"' chars:DoubleStringCharacter* '"' { return chars.join(''); }
  / "'" chars:SingleStringCharacter* "'" { return chars.join(''); }

DoubleStringCharacter =
    !('"' / "\\") char:. { return char; }
  / "\\" sequence:EscapeSequence { return sequence; }

SingleStringCharacter =
    !("'" / "\\") char:. { return char; }
  / "\\" sequence:EscapeSequence { return sequence; }

EscapeSequence =
    "'"
  / '"'
  / "\\"
  / "b"  { return "\b";   }
  / "f"  { return "\f";   }
  / "n"  { return "\n";   }
  / "r"  { return "\r";   }
  / "t"  { return "\t";   }
  / "v"  { return "\x0B"; }