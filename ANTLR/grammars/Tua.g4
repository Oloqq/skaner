grammar Tua;

program
    : block EOF
    ;

block
    : (stat ';'?)* laststat?
    ;

stat
    : nametype '=' exp // nowa zmienna
    | var '=' exp // przypisanie
    | functioncall
    | 'do' block 'end'
    | 'while' exp 'do' block 'end'
    | 'if' exp 'then' block ('elseif' exp 'then' block)* ('else' block)? 'end'
    | 'for' NAME '=' exp ',' exp (',' exp)? 'do' block 'end' // over an integer range
    | 'for' NAME ',' NAME 'in' functioncall 'do' block 'end' // where functioncall is an iterator like pairs
    | 'function' NAME functionbody
    ;

var
    : NAME suffix?
    ;

nametype
    : NAME ':' type
    ;

type
    : NAME
    | NIL
    | listType
    | unionType
    | tableType
    ;

tableType // type in square brackets defines type under integer keys
    : 'Table' '[' type ']'
    ;

unionType
    : 'Union' '[' type (',' type)+ ']'
    ;

listType
    : 'List' '[' type ']'
    ;

prefix
    : var
    | functioncall suffix?
    ;

suffix
    : ('[' exp ']' | '.' NAME)+
    ;

exp
    : '('exp')'
    | number
    | string
    | TRUE
    | FALSE
    | NIL
    | prefix
    | <assoc=right> exp binopPower exp
    | unop exp
    | exp binopMulDivMod exp
    | exp binopAddSub exp
    | <assoc=right> exp binopConcat exp
    | exp binopComparison exp
    | exp binopAnd exp
    | exp binopOr exp
    | unop exp
    | tableconstructor
    ;

functionbody
    : '(' typednamelist? ')' '->' type block 'end'
    ;

laststat
    : ('return' explist? | 'break' | 'continue') ';'?
    ;

typednamelist
    : nametype (',' nametype)*
    ;

functioncall
    : NAME '(' explist? ')'
    ;

explist
    : exp (',' exp)*
    ;

tableconstructor
    : '{' fieldlist? '}'
    ;

fieldlist
    : field (',' field)*
    ;

field
    : '[' exp ']' ':' type '=' exp
    | nametype '=' exp // foo: string = "bar" === ["foo"]: string = "bar"
    | exp // integer keys
    ;

binopAddSub
    : '+'
    | '-'
    ;

binopMulDivMod
    :  '*'
    | '/'
    | '%'
    | '//'
    ;

binopComparison
    : '=='
    | '~='
    | '<='
    | '>='
    | '<'
    | '>'
    ;

binopConcat
    : '..'
    ;

binopAnd
    : 'and'
    | '&'
    ;

binopOr
    : 'or'
    | '|'
    ;

binopPower
    : '^'
    ;

unop
    : '-'
    | 'not'
    ;

string
    : (DOUBLEQUOTESTRING | SINGLEQUOTESTRING)
    ;

number
    : INT
    | FLOAT
    ;

NAME
    : [a-zA-Z_][a-zA-Z_0-9]*
    ;


FALSE
    : 'false'
    ;

TRUE
    : 'true'
    ;

NIL
    : 'nil'
    ;

INT
    : '0'
    | [1-9] [0-9]*
    ;

FLOAT
    : [0-9]+ '.' [0-9]*
    | '.' [0-9]+
    ;

DOUBLEQUOTESTRING
    : '"' ( EscapeSequence | ~('\\'|'"') )* '"'
    ;

SINGLEQUOTESTRING
    : '\'' ( EscapeSequence | ~('\''|'\\') )* '\''
    ;

fragment EscapeSequence
    : '\\' [abfnrtvz"'|\\]
    | '\\' '\r'? '\n'
    ;

WHITESPACE
    : [ \t\u000C\r\n]+ -> skip
    ;
