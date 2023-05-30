grammar Tua;

program
    : block EOF
    ;

block
    : (stat ';'?)* laststat?
    ;

stat
    : newvariable
    | assignment
    | functioncall
    | dostat
    | whilestat
    | ifstat
    | forintstat // over an integer range
    | foriteratorstat // where functioncall is an iterator like pairs
    | functiondef
    ;

assignment
    : var '=' exp
    ;

newvariable
    : nametype '=' exp
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
    : '(' exp ')'
    | number
    | string
    | bool
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
    | tableconstructor
    ;

functionbody
    : '(' typednamelist? ')' '->' type block 'end'
    ;

dostat
    : 'do' block 'end'
    ;

whilestat
    : 'while' exp 'do' block 'end'
    ;

ifstat
    : 'if' exp 'then' block ('elseif' exp 'then' block)* ('else' block)? 'end'
    ;

forintstat
    : 'for' NAME '=' exp ',' exp (',' exp)? 'do' block 'end'
    ;

foriteratorstat
    : 'for' NAME ',' NAME 'in' functioncall 'do' block 'end'
    ;

functiondef
    : 'function' NAME functionbody
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

bool
    : TRUE
    | FALSE
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

NAME
    : [a-zA-Z_][a-zA-Z_0-9]*
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

fragment SingleLineInputCharacter
    : ~[\r\n\u0085\u2028\u2029]
    ;

LINE_COMMENT
    : '--' SingleLineInputCharacter* -> channel(HIDDEN)
    ;

WHITESPACE
    : [ \t\u000C\r\n]+ -> skip
    ;
