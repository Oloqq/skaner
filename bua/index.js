import peg from 'pegjs';
import fs from 'fs';

let grammar = fs.readFileSync('grammar_stubs/lua.pegjs', 'utf8');
let input = fs.readFileSync('programs/example.bua', 'utf8');

let parser = peg.generate(grammar);
let res = parser.parse(input);
console.log(res);