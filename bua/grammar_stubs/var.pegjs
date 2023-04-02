start
    = var_untyped / var_typed

var_untyped
    = 'local' _ ident _ '=' _ integer

var_typed
    = 'local' _ name:ident _ ':' _ type:ident _ '=' _ integer
    { return {
        "name": name,
        "type": type
    }}

ident
    = [a-z_]i[a-z0-9_]i*
    { return text(); } //return text() jest potrzebne zeby zwrocilo caly tekst a nie pojedyncze znaki

integer
    = [0-9]+ { return parseInt(text(), 10); }

_ "whitespace"
    = [ \t\n\r]*