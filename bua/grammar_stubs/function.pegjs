start
    = function*

function
    = _ 'function' _ name:ident _ '()' _ 'return' _ (ident / integer)? _ 'end'
    { return {
        "function": name
    } }

ident
    = [a-z_]i[a-z0-9_]i*
    { return text(); } //return text() jest potrzebne zeby zwrocilo caly tekst a nie pojedyncze znaki

integer
    = [0-9]+ { return parseInt(text(), 10); }

_ "whitespace"
    = [ \t\n\r]*