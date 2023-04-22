grammar Rdsp;

program 
    : block EOF
    ;

block 
    : (stat ';'?)* laststat?
    ; 

//wywalamy tablice z różnym typami?
stat
    : nametype '=' exp
    | var '=' exp
    | functioncall
    | 'do' block 'end'
    | 'while' exp 'do' block 'end'
    | 'if' exp 'then' block ('elseif' exp 'then' block)* ('else' block)? 'end'
    | 'for' NAME '=' exp ',' exp (',' exp)? 'do' block 'end'
    //typować element po którym iterujemy? NAME -> nametype?
    | 'for' (NAME ',')? NAME 'in' prefix 'do' block 'end'
    | 'function' NAME functionbody
    ;

var
    : NAME suffix?
    ;

nametype
    : NAME '@' type
    ;

type
    : NAME
    | listType
    ;
    
//wywalamy to? xd
union
    : 'Union' '[' type (',' type)+ ']'
    ;

listType
    : 'List' '[' type | union ']'
    ;

prefix
    : NAME suffix?
    | functioncall suffix? 
    ;

suffix
    : ('['exp']')+
    ;

exp
    : number
    | string
    | TRUE
    | FALSE
    | 'nil'
    // | lambda
    | prefix
    | exp logicalop exp
    | prefix binop exp
    | unop exp
    | tableconstructor
    ;


// lambda
//     : 'function' functionbody
//     ;

functionbody
    : '(' parlist? ')' '->' type block 'end' 
    ;

laststat
    : 'return' explist? | 'break' | 'continue' ';'?
    ;

// usunąć ...?
parlist
    : typednamelist (',' '...')? | '...'
    ;

typednamelist
    : nametype (',' nametype)* 
    ;

functioncall
    : NAME'('explist?')'
    ;

explist
    : exp (',' exp)*
    ;

tableconstructor
    : '{' explist? '}'
    ;

binop       
    : '+'
    | '-'
    | '*'
    | '/'
    | '%'
    | '^'
    | '#'
    | '=='
    | '~='
    | '<='
    | '>='
    | '<'
    | '>'
    ;

logicalop
    : '|'
    | '&'
    | 'or'
    | 'and'
    ;

unop        
    : '-'
    | 'not'
    | '#'
    ;

NAME
    : [a-zA-Z_][a-zA-Z_0-9]*
    ;

string
    : (NORMALSTRING | CHARSTRING) ('..' string)?
    ;

FALSE 
    : 'false'
    ;

TRUE 
    : 'true'
    ;

number
    : INT
    | FLOAT
    ;

INT
    : '0'
    | [1-9] Digit*
    ;

FLOAT
    : Digit+ '.' Digit*
    | '.' Digit+
    ;

NORMALSTRING
    : '"' ( EscapeSequence | ~('\\'|'"') )* '"'
    ;

CHARSTRING
    : '\'' ( EscapeSequence | ~('\''|'\\') )* '\''
    ;

fragment Digit
    : [0-9]
    ;
    
fragment EscapeSequence
    : '\\' [abfnrtvz"'|\\]
    | '\\' '\r'? '\n'
    ;