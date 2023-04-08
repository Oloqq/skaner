
# lua.pegjs

## 


### chunk

![chunk](.\lua/chunk.svg)

Used by: [block](#block)
References: [_](#_), [stat_semicolon](#stat_semicolon), [laststat_semicolon](#laststat_semicolon)

### stat_semicolon

![stat_semicolon](.\lua/stat_semicolon.svg)

Used by: [chunk](#chunk)
References: [stat](#stat), [_](#_)

### laststat_semicolon

![laststat_semicolon](.\lua/laststat_semicolon.svg)

Used by: [chunk](#chunk)
References: [laststat](#laststat), [_](#_)

### block

![block](.\lua/block.svg)

Used by: [stat](#stat), [funcbody](#funcbody)
References: [chunk](#chunk)

### stat

![stat](.\lua/stat.svg)

Used by: [stat_semicolon](#stat_semicolon)
References: [varlist](#varlist), [_](#_), [explist](#explist), [functioncall](#functioncall), [do](#do), [block](#block), [end](#end), [while](#while), [exp](#exp), [repeat](#repeat), [until](#until), [if](#if), [then](#then), [elseif](#elseif), [else](#else), [for](#for), [Name](#Name), [namelist](#namelist), [in](#in), [funcname](#funcname), [funcbody](#funcbody), [local](#local)

### laststat

![laststat](.\lua/laststat.svg)

Used by: [laststat_semicolon](#laststat_semicolon)
References: [return](#return), [_](#_), [explist](#explist), [break](#break)

### funcname

![funcname](.\lua/funcname.svg)

Used by: [stat](#stat)
References: [Name](#Name), [_](#_)

### varlist

![varlist](.\lua/varlist.svg)

Used by: [stat](#stat)
References: [var](#var), [comma_var](#comma_var)

### comma_var

![comma_var](.\lua/comma_var.svg)

Used by: [varlist](#varlist)
References: [_](#_), [var](#var)

### var

![var](.\lua/var.svg)

Used by: [varlist](#varlist), [comma_var](#comma_var), [value](#value), [prefixexp](#prefixexp)
References: [prefix](#prefix), [_](#_), [suffix](#suffix), [Name](#Name)

### namelist

![namelist](.\lua/namelist.svg)

Used by: [stat](#stat), [parlist1](#parlist1)
References: [Name](#Name), [comma_name](#comma_name)

### comma_name

![comma_name](.\lua/comma_name.svg)

Used by: [namelist](#namelist)
References: [_](#_), [Name](#Name)

### explist

![explist](.\lua/explist.svg)

Used by: [stat](#stat), [laststat](#laststat), [args](#args)
References: [exp](#exp), [comma_exp](#comma_exp)

### comma_exp

![comma_exp](.\lua/comma_exp.svg)

Used by: [explist](#explist)
References: [_](#_), [exp](#exp)

### value

![value](.\lua/value.svg)

Used by: [exp](#exp)
References: [nil](#nil), [false](#false), [true](#true), [Number](#Number), [String](#String), [function](#function), [tableconstructor](#tableconstructor), [functioncall](#functioncall), [var](#var), [exp](#exp)

### exp

![exp](.\lua/exp.svg)

Used by: [stat](#stat), [explist](#explist), [comma_exp](#comma_exp), [value](#value), [exp](#exp), [prefix](#prefix), [index](#index), [prefixexp](#prefixexp), [field](#field)
References: [value](#value), [_](#_), [binop](#binop), [exp](#exp), [unop](#unop)

### prefix

![prefix](.\lua/prefix.svg)

Used by: [var](#var), [functioncall](#functioncall)
References: [_](#_), [exp](#exp), [Name](#Name)

### index

![index](.\lua/index.svg)

Used by: [suffix](#suffix)
References: [_](#_), [exp](#exp), [Name](#Name)

### call

![call](.\lua/call.svg)

Used by: [suffix](#suffix)
References: [args](#args), [_](#_), [Name](#Name)

### suffix

![suffix](.\lua/suffix.svg)

Used by: [var](#var), [functioncall](#functioncall)
References: [call](#call), [index](#index)

### prefixexp

![prefixexp](.\lua/prefixexp.svg)

References: [var](#var), [functioncall](#functioncall), [_](#_), [exp](#exp)

### functioncall

![functioncall](.\lua/functioncall.svg)

Used by: [stat](#stat), [value](#value), [prefixexp](#prefixexp)
References: [prefix](#prefix), [_](#_), [suffix](#suffix)

### args

![args](.\lua/args.svg)

Used by: [call](#call)
References: [_](#_), [explist](#explist), [tableconstructor](#tableconstructor), [String](#String)

### function

![function](.\lua/function.svg)

Used by: [value](#value)
References: [_](#_), [funcbody](#funcbody)

### funcbody

![funcbody](.\lua/funcbody.svg)

Used by: [stat](#stat), [function](#function)
References: [_](#_), [parlist1](#parlist1), [block](#block), [end](#end)

### parlist1

![parlist1](.\lua/parlist1.svg)

Used by: [funcbody](#funcbody)
References: [namelist](#namelist), [_](#_)

### tableconstructor

![tableconstructor](.\lua/tableconstructor.svg)

Used by: [value](#value), [args](#args)
References: [_](#_), [fieldlist](#fieldlist)

### fieldlist

![fieldlist](.\lua/fieldlist.svg)

Used by: [tableconstructor](#tableconstructor)
References: [field](#field), [_](#_), [fieldsep](#fieldsep)

### field

![field](.\lua/field.svg)

Used by: [fieldlist](#fieldlist)
References: [_](#_), [exp](#exp), [Name](#Name)

### fieldsep

![fieldsep](.\lua/fieldsep.svg)

Used by: [fieldlist](#fieldlist)

### binop

![binop](.\lua/binop.svg)

Used by: [exp](#exp)
References: [and](#and), [or](#or)

### unop

![unop](.\lua/unop.svg)

Used by: [exp](#exp)
References: [not](#not)

### _

![_](.\lua/_.svg)

Used by: [chunk](#chunk), [stat_semicolon](#stat_semicolon), [laststat_semicolon](#laststat_semicolon), [stat](#stat), [laststat](#laststat), [funcname](#funcname), [comma_var](#comma_var), [var](#var), [comma_name](#comma_name), [comma_exp](#comma_exp), [exp](#exp), [prefix](#prefix), [index](#index), [call](#call), [prefixexp](#prefixexp), [functioncall](#functioncall), [args](#args), [function](#function), [funcbody](#funcbody), [parlist1](#parlist1), [tableconstructor](#tableconstructor), [fieldlist](#fieldlist), [field](#field)

### do

![do](.\lua/do.svg)

Used by: [stat](#stat)

### end

![end](.\lua/end.svg)

Used by: [stat](#stat), [funcbody](#funcbody)

### while

![while](.\lua/while.svg)

Used by: [stat](#stat)

### repeat

![repeat](.\lua/repeat.svg)

Used by: [stat](#stat)

### until

![until](.\lua/until.svg)

Used by: [stat](#stat)

### if

![if](.\lua/if.svg)

Used by: [stat](#stat)

### then

![then](.\lua/then.svg)

Used by: [stat](#stat)

### else

![else](.\lua/else.svg)

Used by: [stat](#stat)

### elseif

![elseif](.\lua/elseif.svg)

Used by: [stat](#stat)

### for

![for](.\lua/for.svg)

Used by: [stat](#stat)

### in

![in](.\lua/in.svg)

Used by: [stat](#stat)

### local

![local](.\lua/local.svg)

Used by: [stat](#stat)

### return

![return](.\lua/return.svg)

Used by: [laststat](#laststat)

### break

![break](.\lua/break.svg)

Used by: [laststat](#laststat)

### nil

![nil](.\lua/nil.svg)

Used by: [value](#value)

### false

![false](.\lua/false.svg)

Used by: [value](#value)

### true

![true](.\lua/true.svg)

Used by: [value](#value)

### and

![and](.\lua/and.svg)

Used by: [binop](#binop)

### or

![or](.\lua/or.svg)

Used by: [binop](#binop)

### not

![not](.\lua/not.svg)

Used by: [unop](#unop)

### Name

![Name](.\lua/Name.svg)

Used by: [stat](#stat), [funcname](#funcname), [var](#var), [namelist](#namelist), [comma_name](#comma_name), [prefix](#prefix), [index](#index), [call](#call), [field](#field)

### Exponent

![Exponent](.\lua/Exponent.svg)

Used by: [Number](#Number)

### Number

![Number](.\lua/Number.svg)

Used by: [value](#value)
References: [Exponent](#Exponent)

### String

![String](.\lua/String.svg)

Used by: [value](#value), [args](#args)
References: [DoubleStringCharacter](#DoubleStringCharacter), [SingleStringCharacter](#SingleStringCharacter)

### DoubleStringCharacter

![DoubleStringCharacter](.\lua/DoubleStringCharacter.svg)

Used by: [String](#String)
References: [EscapeSequence](#EscapeSequence)

### SingleStringCharacter

![SingleStringCharacter](.\lua/SingleStringCharacter.svg)

Used by: [String](#String)
References: [EscapeSequence](#EscapeSequence)

### EscapeSequence

![EscapeSequence](.\lua/EscapeSequence.svg)

Used by: [DoubleStringCharacter](#DoubleStringCharacter), [SingleStringCharacter](#SingleStringCharacter)

