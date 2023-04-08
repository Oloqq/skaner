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

space "at least one whitespace"
    = [ \t\n\r]+

// keywords
keyword = do / end / while / repeat / until / if / then / else / elseif / for / in / local / return / break / nil / false / true / and / or / not
do = space 'do' space { return "keyword do"; }
end = space 'end' space { return "keyword end"; }
while = space 'while' space { return "keyword while"; }
repeat = space 'repeat' space { return "keyword repeat"; }
until = space 'until' space { return "keyword until"; }
if = space 'if' space { return "keyword if"; }
then = space 'then' space { return "keyword then"; }
else = space 'else' space { return "keyword else"; }
elseif = space 'elseif' space { return "keyword elseif"; }
for = space 'for' space { return "keyword for"; }
in = space 'in' space { return "keyword in"; }
local = space 'local' space { return "keyword local"; }
return = space 'return' space { return "keyword return"; }
break = space 'break' space { return "keyword break"; }
nil = space 'nil' space { return "keyword nil"; }
false = space 'false' space { return "keyword false"; }
true = space 'true' space { return "keyword true"; }
and = space 'and' space { return "keyword and"; }
or = space 'or' space { return "keyword or"; }
not = space 'not' space { return "keyword not"; }

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