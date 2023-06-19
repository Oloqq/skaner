# Tua (Typed Lua)

## 1. Autorzy:
Olgierd Piofczyk, Natalia Niedziałek, Kinga Wrona 

## 2. Założenia programu 

Projekt ma na celu stworzenie interpretera własnego języka programowania o nazwie Tua, który jest wzorowany na popularnym języku Lua. Interpreter jest implementowany przy użyciu języka Python, wykorzystując generator ANTLR4 do generowania parsera oraz skanera.

### Główne cele projektu: 

1. Stworzenie języka Tua: Projekt zakłada opracowanie języka programowania Tua, który będzie inspirowany składnią i funkcjonalnościami języka Lua. Język Tua będzie jest okrojoną wersją Lua, rozszerzoną o statyczne typowanie.

2. Implementacja interpretera: Głównym zadaniem projektu jest stworzenie interpretera języka Tua, który będzie odpowiedzialny za analizę i wykonanie kodu napisanego w tym języku. Interpreter będzie obsługiwał podstawowe konstrukcje języka, takie jak instrukcje warunkowe, pętle, funkcje, zmienne i operacje logiczno-matematyczne.

3. Testowanie: testy jednostkowe znajdują się w folderze tua/test. Pojedynczy test uruchamia się komendą *tuatest \<testcase\>*. Polecenie *tuatest* uruchomi wszystkie testy.

## 3. Spis tokenów:

```
SEMICOLON: ';'

EQUALS: '='

DO KEYWORD: 'do'

END KEYWORD: 'end'

WHILE KEYWORD: 'while'

IF KEYWORD: 'if'

THEN KEYWORD: 'then'

ELSEIF KEYWORD: 'elseif'

ELSE KEYWORD: 'else'

FOR KEYWORD: 'for'

COMMA: ','

IN KEYWORD: 'in'

FUNCTION KEYWORD: 'function'

COLON: ':'

TABLE KEYWORD: 'Table'

LEFT SQUARE BRACKET: '['

RIGHT SQUARE BRACKET: ']'

UNION KEYWORD: 'Union'

LIST KEYWORD: 'List'

DOT: '.'

LEFT PARENTHESIS: '('

RIGHT PARENTHESIS: ')'

ARROW: '->'

RETURN KEYWORD: 'return'

BREAK KEYWORD: 'break'

CONTINUE KEYWORD: 'continue'

LEFT CURLY BRACE: '{'

RIGHT CURLY BRACE: '}'

PLUS OPERATOR: '+'

MINUS OPERATOR: '-'

ASTERISK OPERATOR: '*'

SLASH OPERATOR: '/'

MODULO OPERATOR: '%'

FLOOR DIVISION: '//'

EQUALITY OPERATOR: '=='

INEQUALITY OPERATOR: '~='

LESS THAN EQUAL OPERATOR:'<='

MORE THAN EQUAL OPERATOR: '>='

LESS THAN OPERATOR: '<'

GREATER THAT OPERATOR: '>'

CONCATENATION OPERATOR: '..'

LOGICAL AND OPERATOR: 'and'

BITWISE AND OPERATOR: '&'

LOGICL OR: 'or'

BITWISE OR: '|'

POWER OPERATOR: '^'

LOGICAL NOT: 'not'

FALSE KEYWORD: 'false'

TRUE KEYWORD: 'true'

NIL KEYWORD: 'nil'

NAME: [a-zA-Z_][a-zA-Z_0-9]*

INT: '0' | [1-9][0-9]*

FLOAT: [0-9]+ '.' [0-9]* | '.' [0-9]+

DOUBLEQUOTESTRING: '"' ( ESCAPESEQUENCE | ~('\\'|'"') )* '"'

SINGLEQUOTESTRING: '\'' ( ESCAPESEQUENCE| ~('\''|'\\') )* '\''

ESCAPESEQUENCE: '\\' [abfnrtvz"'|\\] | '\\' '\r'? '\n'

WHITESPACE: [ \t\u000C\r\n]+
```

## 4. Gramatyka przetwarzanego formatu 

```antlr
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
    : parexp
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

parexp
    : '(' exp ')'
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

```

## 5. Informacja o stosowanych generatorach skanerów/parserów, pakietach zewnętrznych 
  * Generator skanerów/parserów: ANTLR. Skaner będzie odpowiedzialny za analizę leksykalną kodu, rozpoznawanie tokenów i przekazywanie ich do parsera. Parser będzie odpowiedzialny za analizę składniową kodu, generowanie drzewa składniowego i przekazywanie go do interpretera. 
  * Język interpretera: Python. Język ten charakteryzuje się prostą i czytelną składnią, co ułatwia tworzenie czytelnego i zrozumiałego kodu. Python zapewnia również wsparcie dla programowania obiektowego, co ułatwia modelowanie różnych konstrukcji języka Tua.

Wykorzystanie ANTLR4 i języka Python pozwala na efektywne tworzenie interpretera języka Tua, który jest zarówno wydajny, elastyczny, jak i łatwy do rozwoju i utrzymania.


Pakiety zewnętrzne:
  * antlr4-python3-runtime
  * pyaml
  * typing_extensions

## 6. Krótka instrukcja obsługi
Po zainstalowaniu pythonowego pakietu (np. przez *pip install*) interpreter uruchamiany jest komendą *tua \<program\>*.  Jeśli nie podano ścieżki do programu zostanie uruchomiony interaktywny interpreter umożliwiający wykonywanie kodu linia po linii. 

## 7. Przykłady użycia

1. Deklaracja zmiennych, tworzenie funkcji, instrukcja warunkowa if-else

```Lua
program: |
  x: int = 3
  y: string = "Hello world!"
  z: bool = true
  q: float = 3.14
  n: nil = nil
  
  list: List[int] = {1, 2, 3}
  list2: List[string] = {"a", "b", "c"}

  function test(x: bool, y: string, l: List[int]) -> nil
    if x then
      print(y)
    else
      print(l)
    end
  end

  test(z, y, list)
  z = false
  test(z, y, list)


output: |
  Hello world!
  [1, 2, 3]

```

2. Funkcja rekursywna

```Lua

program: |
  function fact(n: int) -> int
    if n <= 1 then
      return 1
    else
      return n * fact(n - 1)
    end
  end

  print(fact(1))
  print(fact(3))
  print(fact(10))

output: |
  1
  6
  3628800
```

3. Pętla while i operacje na stringach

```Lua
program: |
  lista: List[string] = {'Ala', 'ma', 'kota'}
  x: int = len(lista)

  while x > 0 do
    y: string = ""
    y = lista[0]
    id: int = 1
    while y ~= 'Ala ma kota' do
      y = y .. ' ' .. lista[id]
      id = id + 1
    end
    print(y)
    x = x - 1
  end

output: |
  Ala ma kota
  Ala ma kota
  Ala ma kota
```

4. Wyrażenia arytmetyczne

```Lua
program: |
  print(2 * 3)
  y: float = 9 ^ (1/2)
  z: float = - 5.3 * 3
  print(y)
  print(z)
  print(1 + 3 + 4 * (5.6) - 2 ^ (3 * 1.0) == 18.4)
  d: bool = true | false & false
  print(d)

output: |
  6
  3.0
  -15.899999999999999
  true
  true
```

5. Działania na listach, pętla for

```Lua
program: |
  function make_list(n: int) -> List[int]
    list: List[int] = {}
    for i = 0, i < n do
      append(list, i)
    end
    return list
  end

  function print_list(x: List[int]) -> nil
    for i = 0, i < len(x) do
      print(x[i])
    end
  end

  x: List[int] = make_list(5)
  print_list(x)

output: |
  0
  1
  2
  3
  4
```

