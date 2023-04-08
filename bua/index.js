import peg from 'pegjs';
import fs from 'fs';
import {format} from 'pretty-format';

let grammar = fs.readFileSync('grammar_stubs/lua.pegjs', 'utf8');
let input = fs.readFileSync('programs/smth.lua', 'utf8');

let parser = peg.generate(grammar, {"trace": true});
let ast = parser.parse(input);
console.log(format(ast));