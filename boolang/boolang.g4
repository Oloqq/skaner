grammar boolang;

// Parser rules
prog: stat+ EOF;

stat: assignment
    | ifStatement
    | echoStatement
    ;

assignment: ID '=' boolExpr;

ifStatement: 'if' boolExpr 'then' stat+ ('else' stat+)? 'end';

echoStatement: 'echo' INT;

boolExpr: 'true'
        | 'false'
        | ID
        ;

// Lexer rules
ID: [a-zA-Z]+;
INT: [0-9]+;
WS: [ \t\r\n]+ -> skip;
