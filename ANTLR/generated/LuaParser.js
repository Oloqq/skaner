// Generated from grammars/Lua.g4 by ANTLR 4.12.0
// jshint ignore: start
import antlr4 from 'antlr4';
import LuaListener from './LuaListener.js';
import LuaVisitor from './LuaVisitor.js';

const serializedATN = [4,1,68,426,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,
4,2,5,7,5,2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,
2,13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,
20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,2,27,
7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,7,33,2,34,7,
34,2,35,7,35,2,36,7,36,1,0,1,0,1,0,1,1,5,1,79,8,1,10,1,12,1,82,9,1,1,1,3,
1,85,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
5,2,121,8,2,10,2,12,2,124,9,2,1,2,1,2,3,2,128,8,2,1,2,1,2,1,2,1,2,1,2,1,
2,1,2,1,2,1,2,1,2,3,2,140,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,166,8,2,3,2,168,
8,2,1,3,1,3,1,3,1,3,1,3,5,3,175,8,3,10,3,12,3,178,9,3,1,4,1,4,1,4,3,4,183,
8,4,1,5,1,5,3,5,187,8,5,1,5,1,5,1,5,3,5,192,8,5,3,5,194,8,5,1,6,1,6,1,6,
1,6,1,7,1,7,1,7,5,7,203,8,7,10,7,12,7,206,9,7,1,7,1,7,3,7,210,8,7,1,8,1,
8,1,8,5,8,215,8,8,10,8,12,8,218,9,8,1,9,1,9,1,9,5,9,223,8,9,10,9,12,9,226,
9,9,1,10,1,10,1,10,5,10,231,8,10,10,10,12,10,234,9,10,1,10,1,10,1,11,1,11,
1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,251,8,11,1,11,
1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
1,11,1,11,5,11,285,8,11,10,11,12,11,288,9,11,1,12,1,12,5,12,292,8,12,10,
12,12,12,295,9,12,1,13,1,13,4,13,299,8,13,11,13,12,13,300,1,14,1,14,1,14,
1,14,1,14,3,14,308,8,14,1,15,1,15,1,15,1,15,1,15,1,15,3,15,316,8,15,1,15,
5,15,319,8,15,10,15,12,15,322,9,15,1,16,5,16,325,8,16,10,16,12,16,328,9,
16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,336,8,16,1,17,1,17,3,17,340,8,17,1,
17,1,17,1,18,1,18,3,18,346,8,18,1,18,1,18,1,18,3,18,351,8,18,1,19,1,19,1,
19,1,20,1,20,3,20,358,8,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,3,21,367,8,
21,1,21,3,21,370,8,21,1,22,1,22,3,22,374,8,22,1,22,1,22,1,23,1,23,1,23,1,
23,5,23,382,8,23,10,23,12,23,385,9,23,1,23,3,23,388,8,23,1,24,1,24,1,24,
1,24,1,24,1,24,1,24,1,24,1,24,1,24,3,24,400,8,24,1,25,1,25,1,26,1,26,1,27,
1,27,1,28,1,28,1,29,1,29,1,30,1,30,1,31,1,31,1,32,1,32,1,33,1,33,1,34,1,
34,1,35,1,35,1,36,1,36,1,36,0,1,22,37,0,2,4,6,8,10,12,14,16,18,20,22,24,
26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,
0,8,2,0,1,1,15,15,2,0,19,20,38,41,1,0,43,44,1,0,45,48,1,0,49,53,3,0,44,44,
51,51,54,55,1,0,61,64,1,0,58,60,455,0,74,1,0,0,0,2,80,1,0,0,0,4,167,1,0,
0,0,6,169,1,0,0,0,8,182,1,0,0,0,10,193,1,0,0,0,12,195,1,0,0,0,14,199,1,0,
0,0,16,211,1,0,0,0,18,219,1,0,0,0,20,232,1,0,0,0,22,250,1,0,0,0,24,289,1,
0,0,0,26,296,1,0,0,0,28,307,1,0,0,0,30,315,1,0,0,0,32,326,1,0,0,0,34,339,
1,0,0,0,36,350,1,0,0,0,38,352,1,0,0,0,40,355,1,0,0,0,42,369,1,0,0,0,44,371,
1,0,0,0,46,377,1,0,0,0,48,399,1,0,0,0,50,401,1,0,0,0,52,403,1,0,0,0,54,405,
1,0,0,0,56,407,1,0,0,0,58,409,1,0,0,0,60,411,1,0,0,0,62,413,1,0,0,0,64,415,
1,0,0,0,66,417,1,0,0,0,68,419,1,0,0,0,70,421,1,0,0,0,72,423,1,0,0,0,74,75,
3,2,1,0,75,76,5,0,0,1,76,1,1,0,0,0,77,79,3,4,2,0,78,77,1,0,0,0,79,82,1,0,
0,0,80,78,1,0,0,0,80,81,1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,83,85,3,10,5,
0,84,83,1,0,0,0,84,85,1,0,0,0,85,3,1,0,0,0,86,168,5,1,0,0,87,88,3,16,8,0,
88,89,5,2,0,0,89,90,3,20,10,0,90,168,1,0,0,0,91,168,3,26,13,0,92,168,3,12,
6,0,93,168,5,3,0,0,94,95,5,4,0,0,95,168,5,57,0,0,96,97,5,5,0,0,97,98,3,2,
1,0,98,99,5,6,0,0,99,168,1,0,0,0,100,101,5,7,0,0,101,102,3,22,11,0,102,103,
5,5,0,0,103,104,3,2,1,0,104,105,5,6,0,0,105,168,1,0,0,0,106,107,5,8,0,0,
107,108,3,2,1,0,108,109,5,9,0,0,109,110,3,22,11,0,110,168,1,0,0,0,111,112,
5,10,0,0,112,113,3,22,11,0,113,114,5,11,0,0,114,122,3,2,1,0,115,116,5,12,
0,0,116,117,3,22,11,0,117,118,5,11,0,0,118,119,3,2,1,0,119,121,1,0,0,0,120,
115,1,0,0,0,121,124,1,0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,127,1,0,
0,0,124,122,1,0,0,0,125,126,5,13,0,0,126,128,3,2,1,0,127,125,1,0,0,0,127,
128,1,0,0,0,128,129,1,0,0,0,129,130,5,6,0,0,130,168,1,0,0,0,131,132,5,14,
0,0,132,133,5,57,0,0,133,134,5,2,0,0,134,135,3,22,11,0,135,136,5,15,0,0,
136,139,3,22,11,0,137,138,5,15,0,0,138,140,3,22,11,0,139,137,1,0,0,0,139,
140,1,0,0,0,140,141,1,0,0,0,141,142,5,5,0,0,142,143,3,2,1,0,143,144,5,6,
0,0,144,168,1,0,0,0,145,146,5,14,0,0,146,147,3,18,9,0,147,148,5,16,0,0,148,
149,3,20,10,0,149,150,5,5,0,0,150,151,3,2,1,0,151,152,5,6,0,0,152,168,1,
0,0,0,153,154,5,17,0,0,154,155,3,14,7,0,155,156,3,40,20,0,156,168,1,0,0,
0,157,158,5,18,0,0,158,159,5,17,0,0,159,160,5,57,0,0,160,168,3,40,20,0,161,
162,5,18,0,0,162,165,3,6,3,0,163,164,5,2,0,0,164,166,3,20,10,0,165,163,1,
0,0,0,165,166,1,0,0,0,166,168,1,0,0,0,167,86,1,0,0,0,167,87,1,0,0,0,167,
91,1,0,0,0,167,92,1,0,0,0,167,93,1,0,0,0,167,94,1,0,0,0,167,96,1,0,0,0,167,
100,1,0,0,0,167,106,1,0,0,0,167,111,1,0,0,0,167,131,1,0,0,0,167,145,1,0,
0,0,167,153,1,0,0,0,167,157,1,0,0,0,167,161,1,0,0,0,168,5,1,0,0,0,169,170,
5,57,0,0,170,176,3,8,4,0,171,172,5,15,0,0,172,173,5,57,0,0,173,175,3,8,4,
0,174,171,1,0,0,0,175,178,1,0,0,0,176,174,1,0,0,0,176,177,1,0,0,0,177,7,
1,0,0,0,178,176,1,0,0,0,179,180,5,19,0,0,180,181,5,57,0,0,181,183,5,20,0,
0,182,179,1,0,0,0,182,183,1,0,0,0,183,9,1,0,0,0,184,186,5,21,0,0,185,187,
3,20,10,0,186,185,1,0,0,0,186,187,1,0,0,0,187,194,1,0,0,0,188,194,5,3,0,
0,189,191,5,22,0,0,190,192,5,1,0,0,191,190,1,0,0,0,191,192,1,0,0,0,192,194,
1,0,0,0,193,184,1,0,0,0,193,188,1,0,0,0,193,189,1,0,0,0,194,11,1,0,0,0,195,
196,5,23,0,0,196,197,5,57,0,0,197,198,5,23,0,0,198,13,1,0,0,0,199,204,5,
57,0,0,200,201,5,24,0,0,201,203,5,57,0,0,202,200,1,0,0,0,203,206,1,0,0,0,
204,202,1,0,0,0,204,205,1,0,0,0,205,209,1,0,0,0,206,204,1,0,0,0,207,208,
5,25,0,0,208,210,5,57,0,0,209,207,1,0,0,0,209,210,1,0,0,0,210,15,1,0,0,0,
211,216,3,30,15,0,212,213,5,15,0,0,213,215,3,30,15,0,214,212,1,0,0,0,215,
218,1,0,0,0,216,214,1,0,0,0,216,217,1,0,0,0,217,17,1,0,0,0,218,216,1,0,0,
0,219,224,5,57,0,0,220,221,5,15,0,0,221,223,5,57,0,0,222,220,1,0,0,0,223,
226,1,0,0,0,224,222,1,0,0,0,224,225,1,0,0,0,225,19,1,0,0,0,226,224,1,0,0,
0,227,228,3,22,11,0,228,229,5,15,0,0,229,231,1,0,0,0,230,227,1,0,0,0,231,
234,1,0,0,0,232,230,1,0,0,0,232,233,1,0,0,0,233,235,1,0,0,0,234,232,1,0,
0,0,235,236,3,22,11,0,236,21,1,0,0,0,237,238,6,11,-1,0,238,251,5,26,0,0,
239,251,5,27,0,0,240,251,5,28,0,0,241,251,3,70,35,0,242,251,3,72,36,0,243,
251,5,29,0,0,244,251,3,38,19,0,245,251,3,24,12,0,246,251,3,44,22,0,247,248,
3,66,33,0,248,249,3,22,11,8,249,251,1,0,0,0,250,237,1,0,0,0,250,239,1,0,
0,0,250,240,1,0,0,0,250,241,1,0,0,0,250,242,1,0,0,0,250,243,1,0,0,0,250,
244,1,0,0,0,250,245,1,0,0,0,250,246,1,0,0,0,250,247,1,0,0,0,251,286,1,0,
0,0,252,253,10,9,0,0,253,254,3,68,34,0,254,255,3,22,11,9,255,285,1,0,0,0,
256,257,10,7,0,0,257,258,3,62,31,0,258,259,3,22,11,8,259,285,1,0,0,0,260,
261,10,6,0,0,261,262,3,60,30,0,262,263,3,22,11,7,263,285,1,0,0,0,264,265,
10,5,0,0,265,266,3,58,29,0,266,267,3,22,11,5,267,285,1,0,0,0,268,269,10,
4,0,0,269,270,3,56,28,0,270,271,3,22,11,5,271,285,1,0,0,0,272,273,10,3,0,
0,273,274,3,54,27,0,274,275,3,22,11,4,275,285,1,0,0,0,276,277,10,2,0,0,277,
278,3,52,26,0,278,279,3,22,11,3,279,285,1,0,0,0,280,281,10,1,0,0,281,282,
3,64,32,0,282,283,3,22,11,2,283,285,1,0,0,0,284,252,1,0,0,0,284,256,1,0,
0,0,284,260,1,0,0,0,284,264,1,0,0,0,284,268,1,0,0,0,284,272,1,0,0,0,284,
276,1,0,0,0,284,280,1,0,0,0,285,288,1,0,0,0,286,284,1,0,0,0,286,287,1,0,
0,0,287,23,1,0,0,0,288,286,1,0,0,0,289,293,3,28,14,0,290,292,3,34,17,0,291,
290,1,0,0,0,292,295,1,0,0,0,293,291,1,0,0,0,293,294,1,0,0,0,294,25,1,0,0,
0,295,293,1,0,0,0,296,298,3,28,14,0,297,299,3,34,17,0,298,297,1,0,0,0,299,
300,1,0,0,0,300,298,1,0,0,0,300,301,1,0,0,0,301,27,1,0,0,0,302,308,3,30,
15,0,303,304,5,30,0,0,304,305,3,22,11,0,305,306,5,31,0,0,306,308,1,0,0,0,
307,302,1,0,0,0,307,303,1,0,0,0,308,29,1,0,0,0,309,316,5,57,0,0,310,311,
5,30,0,0,311,312,3,22,11,0,312,313,5,31,0,0,313,314,3,32,16,0,314,316,1,
0,0,0,315,309,1,0,0,0,315,310,1,0,0,0,316,320,1,0,0,0,317,319,3,32,16,0,
318,317,1,0,0,0,319,322,1,0,0,0,320,318,1,0,0,0,320,321,1,0,0,0,321,31,1,
0,0,0,322,320,1,0,0,0,323,325,3,34,17,0,324,323,1,0,0,0,325,328,1,0,0,0,
326,324,1,0,0,0,326,327,1,0,0,0,327,335,1,0,0,0,328,326,1,0,0,0,329,330,
5,32,0,0,330,331,3,22,11,0,331,332,5,33,0,0,332,336,1,0,0,0,333,334,5,24,
0,0,334,336,5,57,0,0,335,329,1,0,0,0,335,333,1,0,0,0,336,33,1,0,0,0,337,
338,5,25,0,0,338,340,5,57,0,0,339,337,1,0,0,0,339,340,1,0,0,0,340,341,1,
0,0,0,341,342,3,36,18,0,342,35,1,0,0,0,343,345,5,30,0,0,344,346,3,20,10,
0,345,344,1,0,0,0,345,346,1,0,0,0,346,347,1,0,0,0,347,351,5,31,0,0,348,351,
3,44,22,0,349,351,3,72,36,0,350,343,1,0,0,0,350,348,1,0,0,0,350,349,1,0,
0,0,351,37,1,0,0,0,352,353,5,17,0,0,353,354,3,40,20,0,354,39,1,0,0,0,355,
357,5,30,0,0,356,358,3,42,21,0,357,356,1,0,0,0,357,358,1,0,0,0,358,359,1,
0,0,0,359,360,5,31,0,0,360,361,3,2,1,0,361,362,5,6,0,0,362,41,1,0,0,0,363,
366,3,18,9,0,364,365,5,15,0,0,365,367,5,29,0,0,366,364,1,0,0,0,366,367,1,
0,0,0,367,370,1,0,0,0,368,370,5,29,0,0,369,363,1,0,0,0,369,368,1,0,0,0,370,
43,1,0,0,0,371,373,5,34,0,0,372,374,3,46,23,0,373,372,1,0,0,0,373,374,1,
0,0,0,374,375,1,0,0,0,375,376,5,35,0,0,376,45,1,0,0,0,377,383,3,48,24,0,
378,379,3,50,25,0,379,380,3,48,24,0,380,382,1,0,0,0,381,378,1,0,0,0,382,
385,1,0,0,0,383,381,1,0,0,0,383,384,1,0,0,0,384,387,1,0,0,0,385,383,1,0,
0,0,386,388,3,50,25,0,387,386,1,0,0,0,387,388,1,0,0,0,388,47,1,0,0,0,389,
390,5,32,0,0,390,391,3,22,11,0,391,392,5,33,0,0,392,393,5,2,0,0,393,394,
3,22,11,0,394,400,1,0,0,0,395,396,5,57,0,0,396,397,5,2,0,0,397,400,3,22,
11,0,398,400,3,22,11,0,399,389,1,0,0,0,399,395,1,0,0,0,399,398,1,0,0,0,400,
49,1,0,0,0,401,402,7,0,0,0,402,51,1,0,0,0,403,404,5,36,0,0,404,53,1,0,0,
0,405,406,5,37,0,0,406,55,1,0,0,0,407,408,7,1,0,0,408,57,1,0,0,0,409,410,
5,42,0,0,410,59,1,0,0,0,411,412,7,2,0,0,412,61,1,0,0,0,413,414,7,3,0,0,414,
63,1,0,0,0,415,416,7,4,0,0,416,65,1,0,0,0,417,418,7,5,0,0,418,67,1,0,0,0,
419,420,5,56,0,0,420,69,1,0,0,0,421,422,7,6,0,0,422,71,1,0,0,0,423,424,7,
7,0,0,424,73,1,0,0,0,37,80,84,122,127,139,165,167,176,182,186,191,193,204,
209,216,224,232,250,284,286,293,300,307,315,320,326,335,339,345,350,357,
366,369,373,383,387,399];


const atn = new antlr4.atn.ATNDeserializer().deserialize(serializedATN);

const decisionsToDFA = atn.decisionToState.map( (ds, index) => new antlr4.dfa.DFA(ds, index) );

const sharedContextCache = new antlr4.atn.PredictionContextCache();

export default class LuaParser extends antlr4.Parser {

    static grammarFileName = "Lua.g4";
    static literalNames = [ null, "';'", "'='", "'break'", "'goto'", "'do'", 
                            "'end'", "'while'", "'repeat'", "'until'", "'if'", 
                            "'then'", "'elseif'", "'else'", "'for'", "','", 
                            "'in'", "'function'", "'local'", "'<'", "'>'", 
                            "'return'", "'continue'", "'::'", "'.'", "':'", 
                            "'nil'", "'false'", "'true'", "'...'", "'('", 
                            "')'", "'['", "']'", "'{'", "'}'", "'or'", "'and'", 
                            "'<='", "'>='", "'~='", "'=='", "'..'", "'+'", 
                            "'-'", "'*'", "'/'", "'%'", "'//'", "'&'", "'|'", 
                            "'~'", "'<<'", "'>>'", "'not'", "'#'", "'^'" ];
    static symbolicNames = [ null, null, null, null, null, null, null, null, 
                             null, null, null, null, null, null, null, null, 
                             null, null, null, null, null, null, null, null, 
                             null, null, null, null, null, null, null, null, 
                             null, null, null, null, null, null, null, null, 
                             null, null, null, null, null, null, null, null, 
                             null, null, null, null, null, null, null, null, 
                             null, "NAME", "NORMALSTRING", "CHARSTRING", 
                             "LONGSTRING", "INT", "HEX", "FLOAT", "HEX_FLOAT", 
                             "COMMENT", "LINE_COMMENT", "WS", "SHEBANG" ];
    static ruleNames = [ "chunk", "block", "stat", "attnamelist", "attrib", 
                         "laststat", "label", "funcname", "varlist", "namelist", 
                         "explist", "exp", "prefixexp", "functioncall", 
                         "varOrExp", "var", "varSuffix", "nameAndArgs", 
                         "args", "functiondef", "funcbody", "parlist", "tableconstructor", 
                         "fieldlist", "field", "fieldsep", "operatorOr", 
                         "operatorAnd", "operatorComparison", "operatorStrcat", 
                         "operatorAddSub", "operatorMulDivMod", "operatorBitwise", 
                         "operatorUnary", "operatorPower", "number", "string" ];

    constructor(input) {
        super(input);
        this._interp = new antlr4.atn.ParserATNSimulator(this, atn, decisionsToDFA, sharedContextCache);
        this.ruleNames = LuaParser.ruleNames;
        this.literalNames = LuaParser.literalNames;
        this.symbolicNames = LuaParser.symbolicNames;
    }

    sempred(localctx, ruleIndex, predIndex) {
    	switch(ruleIndex) {
    	case 11:
    	    		return this.exp_sempred(localctx, predIndex);
        default:
            throw "No predicate with index:" + ruleIndex;
       }
    }

    exp_sempred(localctx, predIndex) {
    	switch(predIndex) {
    		case 0:
    			return this.precpred(this._ctx, 9);
    		case 1:
    			return this.precpred(this._ctx, 7);
    		case 2:
    			return this.precpred(this._ctx, 6);
    		case 3:
    			return this.precpred(this._ctx, 5);
    		case 4:
    			return this.precpred(this._ctx, 4);
    		case 5:
    			return this.precpred(this._ctx, 3);
    		case 6:
    			return this.precpred(this._ctx, 2);
    		case 7:
    			return this.precpred(this._ctx, 1);
    		default:
    			throw "No predicate with index:" + predIndex;
    	}
    };




	chunk() {
	    let localctx = new ChunkContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 0, LuaParser.RULE_chunk);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 74;
	        this.block();
	        this.state = 75;
	        this.match(LuaParser.EOF);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	block() {
	    let localctx = new BlockContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 2, LuaParser.RULE_block);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 80;
	        this._errHandler.sync(this);
	        var _alt = this._interp.adaptivePredict(this._input,0,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                this.state = 77;
	                this.stat(); 
	            }
	            this.state = 82;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,0,this._ctx);
	        }

	        this.state = 84;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        if((((_la) & ~0x1f) === 0 && ((1 << _la) & 6291464) !== 0)) {
	            this.state = 83;
	            this.laststat();
	        }

	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	stat() {
	    let localctx = new StatContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 4, LuaParser.RULE_stat);
	    var _la = 0;
	    try {
	        this.state = 167;
	        this._errHandler.sync(this);
	        var la_ = this._interp.adaptivePredict(this._input,6,this._ctx);
	        switch(la_) {
	        case 1:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 86;
	            this.match(LuaParser.T__0);
	            break;

	        case 2:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 87;
	            this.varlist();
	            this.state = 88;
	            this.match(LuaParser.T__1);
	            this.state = 89;
	            this.explist();
	            break;

	        case 3:
	            this.enterOuterAlt(localctx, 3);
	            this.state = 91;
	            this.functioncall();
	            break;

	        case 4:
	            this.enterOuterAlt(localctx, 4);
	            this.state = 92;
	            this.label();
	            break;

	        case 5:
	            this.enterOuterAlt(localctx, 5);
	            this.state = 93;
	            this.match(LuaParser.T__2);
	            break;

	        case 6:
	            this.enterOuterAlt(localctx, 6);
	            this.state = 94;
	            this.match(LuaParser.T__3);
	            this.state = 95;
	            this.match(LuaParser.NAME);
	            break;

	        case 7:
	            this.enterOuterAlt(localctx, 7);
	            this.state = 96;
	            this.match(LuaParser.T__4);
	            this.state = 97;
	            this.block();
	            this.state = 98;
	            this.match(LuaParser.T__5);
	            break;

	        case 8:
	            this.enterOuterAlt(localctx, 8);
	            this.state = 100;
	            this.match(LuaParser.T__6);
	            this.state = 101;
	            this.exp(0);
	            this.state = 102;
	            this.match(LuaParser.T__4);
	            this.state = 103;
	            this.block();
	            this.state = 104;
	            this.match(LuaParser.T__5);
	            break;

	        case 9:
	            this.enterOuterAlt(localctx, 9);
	            this.state = 106;
	            this.match(LuaParser.T__7);
	            this.state = 107;
	            this.block();
	            this.state = 108;
	            this.match(LuaParser.T__8);
	            this.state = 109;
	            this.exp(0);
	            break;

	        case 10:
	            this.enterOuterAlt(localctx, 10);
	            this.state = 111;
	            this.match(LuaParser.T__9);
	            this.state = 112;
	            this.exp(0);
	            this.state = 113;
	            this.match(LuaParser.T__10);
	            this.state = 114;
	            this.block();
	            this.state = 122;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            while(_la===12) {
	                this.state = 115;
	                this.match(LuaParser.T__11);
	                this.state = 116;
	                this.exp(0);
	                this.state = 117;
	                this.match(LuaParser.T__10);
	                this.state = 118;
	                this.block();
	                this.state = 124;
	                this._errHandler.sync(this);
	                _la = this._input.LA(1);
	            }
	            this.state = 127;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            if(_la===13) {
	                this.state = 125;
	                this.match(LuaParser.T__12);
	                this.state = 126;
	                this.block();
	            }

	            this.state = 129;
	            this.match(LuaParser.T__5);
	            break;

	        case 11:
	            this.enterOuterAlt(localctx, 11);
	            this.state = 131;
	            this.match(LuaParser.T__13);
	            this.state = 132;
	            this.match(LuaParser.NAME);
	            this.state = 133;
	            this.match(LuaParser.T__1);
	            this.state = 134;
	            this.exp(0);
	            this.state = 135;
	            this.match(LuaParser.T__14);
	            this.state = 136;
	            this.exp(0);
	            this.state = 139;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            if(_la===15) {
	                this.state = 137;
	                this.match(LuaParser.T__14);
	                this.state = 138;
	                this.exp(0);
	            }

	            this.state = 141;
	            this.match(LuaParser.T__4);
	            this.state = 142;
	            this.block();
	            this.state = 143;
	            this.match(LuaParser.T__5);
	            break;

	        case 12:
	            this.enterOuterAlt(localctx, 12);
	            this.state = 145;
	            this.match(LuaParser.T__13);
	            this.state = 146;
	            this.namelist();
	            this.state = 147;
	            this.match(LuaParser.T__15);
	            this.state = 148;
	            this.explist();
	            this.state = 149;
	            this.match(LuaParser.T__4);
	            this.state = 150;
	            this.block();
	            this.state = 151;
	            this.match(LuaParser.T__5);
	            break;

	        case 13:
	            this.enterOuterAlt(localctx, 13);
	            this.state = 153;
	            this.match(LuaParser.T__16);
	            this.state = 154;
	            this.funcname();
	            this.state = 155;
	            this.funcbody();
	            break;

	        case 14:
	            this.enterOuterAlt(localctx, 14);
	            this.state = 157;
	            this.match(LuaParser.T__17);
	            this.state = 158;
	            this.match(LuaParser.T__16);
	            this.state = 159;
	            this.match(LuaParser.NAME);
	            this.state = 160;
	            this.funcbody();
	            break;

	        case 15:
	            this.enterOuterAlt(localctx, 15);
	            this.state = 161;
	            this.match(LuaParser.T__17);
	            this.state = 162;
	            this.attnamelist();
	            this.state = 165;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            if(_la===2) {
	                this.state = 163;
	                this.match(LuaParser.T__1);
	                this.state = 164;
	                this.explist();
	            }

	            break;

	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	attnamelist() {
	    let localctx = new AttnamelistContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 6, LuaParser.RULE_attnamelist);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 169;
	        this.match(LuaParser.NAME);
	        this.state = 170;
	        this.attrib();
	        this.state = 176;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        while(_la===15) {
	            this.state = 171;
	            this.match(LuaParser.T__14);
	            this.state = 172;
	            this.match(LuaParser.NAME);
	            this.state = 173;
	            this.attrib();
	            this.state = 178;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	attrib() {
	    let localctx = new AttribContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 8, LuaParser.RULE_attrib);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 182;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        if(_la===19) {
	            this.state = 179;
	            this.match(LuaParser.T__18);
	            this.state = 180;
	            this.match(LuaParser.NAME);
	            this.state = 181;
	            this.match(LuaParser.T__19);
	        }

	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	laststat() {
	    let localctx = new LaststatContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 10, LuaParser.RULE_laststat);
	    var _la = 0;
	    try {
	        this.state = 193;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case 21:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 184;
	            this.match(LuaParser.T__20);
	            this.state = 186;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            if((((_la) & ~0x1f) === 0 && ((1 << _la) & 2080505856) !== 0) || ((((_la - 34)) & ~0x1f) === 0 && ((1 << (_la - 34)) & 2142372865) !== 0)) {
	                this.state = 185;
	                this.explist();
	            }

	            break;
	        case 3:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 188;
	            this.match(LuaParser.T__2);
	            break;
	        case 22:
	            this.enterOuterAlt(localctx, 3);
	            this.state = 189;
	            this.match(LuaParser.T__21);
	            this.state = 191;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            if(_la===1) {
	                this.state = 190;
	                this.match(LuaParser.T__0);
	            }

	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	label() {
	    let localctx = new LabelContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 12, LuaParser.RULE_label);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 195;
	        this.match(LuaParser.T__22);
	        this.state = 196;
	        this.match(LuaParser.NAME);
	        this.state = 197;
	        this.match(LuaParser.T__22);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	funcname() {
	    let localctx = new FuncnameContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 14, LuaParser.RULE_funcname);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 199;
	        this.match(LuaParser.NAME);
	        this.state = 204;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        while(_la===24) {
	            this.state = 200;
	            this.match(LuaParser.T__23);
	            this.state = 201;
	            this.match(LuaParser.NAME);
	            this.state = 206;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        }
	        this.state = 209;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        if(_la===25) {
	            this.state = 207;
	            this.match(LuaParser.T__24);
	            this.state = 208;
	            this.match(LuaParser.NAME);
	        }

	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	varlist() {
	    let localctx = new VarlistContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 16, LuaParser.RULE_varlist);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 211;
	        this.var_();
	        this.state = 216;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        while(_la===15) {
	            this.state = 212;
	            this.match(LuaParser.T__14);
	            this.state = 213;
	            this.var_();
	            this.state = 218;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	namelist() {
	    let localctx = new NamelistContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 18, LuaParser.RULE_namelist);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 219;
	        this.match(LuaParser.NAME);
	        this.state = 224;
	        this._errHandler.sync(this);
	        var _alt = this._interp.adaptivePredict(this._input,15,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                this.state = 220;
	                this.match(LuaParser.T__14);
	                this.state = 221;
	                this.match(LuaParser.NAME); 
	            }
	            this.state = 226;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,15,this._ctx);
	        }

	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	explist() {
	    let localctx = new ExplistContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 20, LuaParser.RULE_explist);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 232;
	        this._errHandler.sync(this);
	        var _alt = this._interp.adaptivePredict(this._input,16,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                this.state = 227;
	                this.exp(0);
	                this.state = 228;
	                this.match(LuaParser.T__14); 
	            }
	            this.state = 234;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,16,this._ctx);
	        }

	        this.state = 235;
	        this.exp(0);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	exp(_p) {
		if(_p===undefined) {
		    _p = 0;
		}
	    const _parentctx = this._ctx;
	    const _parentState = this.state;
	    let localctx = new ExpContext(this, this._ctx, _parentState);
	    let _prevctx = localctx;
	    const _startState = 22;
	    this.enterRecursionRule(localctx, 22, LuaParser.RULE_exp, _p);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 250;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case 26:
	            this.state = 238;
	            this.match(LuaParser.T__25);
	            break;
	        case 27:
	            this.state = 239;
	            this.match(LuaParser.T__26);
	            break;
	        case 28:
	            this.state = 240;
	            this.match(LuaParser.T__27);
	            break;
	        case 61:
	        case 62:
	        case 63:
	        case 64:
	            this.state = 241;
	            this.number();
	            break;
	        case 58:
	        case 59:
	        case 60:
	            this.state = 242;
	            this.string();
	            break;
	        case 29:
	            this.state = 243;
	            this.match(LuaParser.T__28);
	            break;
	        case 17:
	            this.state = 244;
	            this.functiondef();
	            break;
	        case 30:
	        case 57:
	            this.state = 245;
	            this.prefixexp();
	            break;
	        case 34:
	            this.state = 246;
	            this.tableconstructor();
	            break;
	        case 44:
	        case 51:
	        case 54:
	        case 55:
	            this.state = 247;
	            this.operatorUnary();
	            this.state = 248;
	            this.exp(8);
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	        this._ctx.stop = this._input.LT(-1);
	        this.state = 286;
	        this._errHandler.sync(this);
	        var _alt = this._interp.adaptivePredict(this._input,19,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                if(this._parseListeners!==null) {
	                    this.triggerExitRuleEvent();
	                }
	                _prevctx = localctx;
	                this.state = 284;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,18,this._ctx);
	                switch(la_) {
	                case 1:
	                    localctx = new ExpContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, LuaParser.RULE_exp);
	                    this.state = 252;
	                    if (!( this.precpred(this._ctx, 9))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 9)");
	                    }
	                    this.state = 253;
	                    this.operatorPower();
	                    this.state = 254;
	                    this.exp(9);
	                    break;

	                case 2:
	                    localctx = new ExpContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, LuaParser.RULE_exp);
	                    this.state = 256;
	                    if (!( this.precpred(this._ctx, 7))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 7)");
	                    }
	                    this.state = 257;
	                    this.operatorMulDivMod();
	                    this.state = 258;
	                    this.exp(8);
	                    break;

	                case 3:
	                    localctx = new ExpContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, LuaParser.RULE_exp);
	                    this.state = 260;
	                    if (!( this.precpred(this._ctx, 6))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 6)");
	                    }
	                    this.state = 261;
	                    this.operatorAddSub();
	                    this.state = 262;
	                    this.exp(7);
	                    break;

	                case 4:
	                    localctx = new ExpContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, LuaParser.RULE_exp);
	                    this.state = 264;
	                    if (!( this.precpred(this._ctx, 5))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 5)");
	                    }
	                    this.state = 265;
	                    this.operatorStrcat();
	                    this.state = 266;
	                    this.exp(5);
	                    break;

	                case 5:
	                    localctx = new ExpContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, LuaParser.RULE_exp);
	                    this.state = 268;
	                    if (!( this.precpred(this._ctx, 4))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 4)");
	                    }
	                    this.state = 269;
	                    this.operatorComparison();
	                    this.state = 270;
	                    this.exp(5);
	                    break;

	                case 6:
	                    localctx = new ExpContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, LuaParser.RULE_exp);
	                    this.state = 272;
	                    if (!( this.precpred(this._ctx, 3))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 3)");
	                    }
	                    this.state = 273;
	                    this.operatorAnd();
	                    this.state = 274;
	                    this.exp(4);
	                    break;

	                case 7:
	                    localctx = new ExpContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, LuaParser.RULE_exp);
	                    this.state = 276;
	                    if (!( this.precpred(this._ctx, 2))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 2)");
	                    }
	                    this.state = 277;
	                    this.operatorOr();
	                    this.state = 278;
	                    this.exp(3);
	                    break;

	                case 8:
	                    localctx = new ExpContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, LuaParser.RULE_exp);
	                    this.state = 280;
	                    if (!( this.precpred(this._ctx, 1))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 1)");
	                    }
	                    this.state = 281;
	                    this.operatorBitwise();
	                    this.state = 282;
	                    this.exp(2);
	                    break;

	                } 
	            }
	            this.state = 288;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,19,this._ctx);
	        }

	    } catch( error) {
	        if(error instanceof antlr4.error.RecognitionException) {
		        localctx.exception = error;
		        this._errHandler.reportError(this, error);
		        this._errHandler.recover(this, error);
		    } else {
		    	throw error;
		    }
	    } finally {
	        this.unrollRecursionContexts(_parentctx)
	    }
	    return localctx;
	}



	prefixexp() {
	    let localctx = new PrefixexpContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 24, LuaParser.RULE_prefixexp);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 289;
	        this.varOrExp();
	        this.state = 293;
	        this._errHandler.sync(this);
	        var _alt = this._interp.adaptivePredict(this._input,20,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                this.state = 290;
	                this.nameAndArgs(); 
	            }
	            this.state = 295;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,20,this._ctx);
	        }

	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	functioncall() {
	    let localctx = new FunctioncallContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 26, LuaParser.RULE_functioncall);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 296;
	        this.varOrExp();
	        this.state = 298; 
	        this._errHandler.sync(this);
	        var _alt = 1;
	        do {
	        	switch (_alt) {
	        	case 1:
	        		this.state = 297;
	        		this.nameAndArgs();
	        		break;
	        	default:
	        		throw new antlr4.error.NoViableAltException(this);
	        	}
	        	this.state = 300; 
	        	this._errHandler.sync(this);
	        	_alt = this._interp.adaptivePredict(this._input,21, this._ctx);
	        } while ( _alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER );
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	varOrExp() {
	    let localctx = new VarOrExpContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 28, LuaParser.RULE_varOrExp);
	    try {
	        this.state = 307;
	        this._errHandler.sync(this);
	        var la_ = this._interp.adaptivePredict(this._input,22,this._ctx);
	        switch(la_) {
	        case 1:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 302;
	            this.var_();
	            break;

	        case 2:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 303;
	            this.match(LuaParser.T__29);
	            this.state = 304;
	            this.exp(0);
	            this.state = 305;
	            this.match(LuaParser.T__30);
	            break;

	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	var_() {
	    let localctx = new VarContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 30, LuaParser.RULE_var);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 315;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case 57:
	            this.state = 309;
	            this.match(LuaParser.NAME);
	            break;
	        case 30:
	            this.state = 310;
	            this.match(LuaParser.T__29);
	            this.state = 311;
	            this.exp(0);
	            this.state = 312;
	            this.match(LuaParser.T__30);
	            this.state = 313;
	            this.varSuffix();
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	        this.state = 320;
	        this._errHandler.sync(this);
	        var _alt = this._interp.adaptivePredict(this._input,24,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                this.state = 317;
	                this.varSuffix(); 
	            }
	            this.state = 322;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,24,this._ctx);
	        }

	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	varSuffix() {
	    let localctx = new VarSuffixContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 32, LuaParser.RULE_varSuffix);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 326;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        while(_la===25 || _la===30 || ((((_la - 34)) & ~0x1f) === 0 && ((1 << (_la - 34)) & 117440513) !== 0)) {
	            this.state = 323;
	            this.nameAndArgs();
	            this.state = 328;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        }
	        this.state = 335;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case 32:
	            this.state = 329;
	            this.match(LuaParser.T__31);
	            this.state = 330;
	            this.exp(0);
	            this.state = 331;
	            this.match(LuaParser.T__32);
	            break;
	        case 24:
	            this.state = 333;
	            this.match(LuaParser.T__23);
	            this.state = 334;
	            this.match(LuaParser.NAME);
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	nameAndArgs() {
	    let localctx = new NameAndArgsContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 34, LuaParser.RULE_nameAndArgs);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 339;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        if(_la===25) {
	            this.state = 337;
	            this.match(LuaParser.T__24);
	            this.state = 338;
	            this.match(LuaParser.NAME);
	        }

	        this.state = 341;
	        this.args();
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	args() {
	    let localctx = new ArgsContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 36, LuaParser.RULE_args);
	    var _la = 0;
	    try {
	        this.state = 350;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case 30:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 343;
	            this.match(LuaParser.T__29);
	            this.state = 345;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            if((((_la) & ~0x1f) === 0 && ((1 << _la) & 2080505856) !== 0) || ((((_la - 34)) & ~0x1f) === 0 && ((1 << (_la - 34)) & 2142372865) !== 0)) {
	                this.state = 344;
	                this.explist();
	            }

	            this.state = 347;
	            this.match(LuaParser.T__30);
	            break;
	        case 34:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 348;
	            this.tableconstructor();
	            break;
	        case 58:
	        case 59:
	        case 60:
	            this.enterOuterAlt(localctx, 3);
	            this.state = 349;
	            this.string();
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	functiondef() {
	    let localctx = new FunctiondefContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 38, LuaParser.RULE_functiondef);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 352;
	        this.match(LuaParser.T__16);
	        this.state = 353;
	        this.funcbody();
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	funcbody() {
	    let localctx = new FuncbodyContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 40, LuaParser.RULE_funcbody);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 355;
	        this.match(LuaParser.T__29);
	        this.state = 357;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        if(_la===29 || _la===57) {
	            this.state = 356;
	            this.parlist();
	        }

	        this.state = 359;
	        this.match(LuaParser.T__30);
	        this.state = 360;
	        this.block();
	        this.state = 361;
	        this.match(LuaParser.T__5);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	parlist() {
	    let localctx = new ParlistContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 42, LuaParser.RULE_parlist);
	    var _la = 0;
	    try {
	        this.state = 369;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case 57:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 363;
	            this.namelist();
	            this.state = 366;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            if(_la===15) {
	                this.state = 364;
	                this.match(LuaParser.T__14);
	                this.state = 365;
	                this.match(LuaParser.T__28);
	            }

	            break;
	        case 29:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 368;
	            this.match(LuaParser.T__28);
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	tableconstructor() {
	    let localctx = new TableconstructorContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 44, LuaParser.RULE_tableconstructor);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 371;
	        this.match(LuaParser.T__33);
	        this.state = 373;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        if(((((_la - 17)) & ~0x1f) === 0 && ((1 << (_la - 17)) & 134397441) !== 0) || ((((_la - 51)) & ~0x1f) === 0 && ((1 << (_la - 51)) & 16345) !== 0)) {
	            this.state = 372;
	            this.fieldlist();
	        }

	        this.state = 375;
	        this.match(LuaParser.T__34);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	fieldlist() {
	    let localctx = new FieldlistContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 46, LuaParser.RULE_fieldlist);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 377;
	        this.field();
	        this.state = 383;
	        this._errHandler.sync(this);
	        var _alt = this._interp.adaptivePredict(this._input,34,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                this.state = 378;
	                this.fieldsep();
	                this.state = 379;
	                this.field(); 
	            }
	            this.state = 385;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,34,this._ctx);
	        }

	        this.state = 387;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        if(_la===1 || _la===15) {
	            this.state = 386;
	            this.fieldsep();
	        }

	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	field() {
	    let localctx = new FieldContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 48, LuaParser.RULE_field);
	    try {
	        this.state = 399;
	        this._errHandler.sync(this);
	        var la_ = this._interp.adaptivePredict(this._input,36,this._ctx);
	        switch(la_) {
	        case 1:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 389;
	            this.match(LuaParser.T__31);
	            this.state = 390;
	            this.exp(0);
	            this.state = 391;
	            this.match(LuaParser.T__32);
	            this.state = 392;
	            this.match(LuaParser.T__1);
	            this.state = 393;
	            this.exp(0);
	            break;

	        case 2:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 395;
	            this.match(LuaParser.NAME);
	            this.state = 396;
	            this.match(LuaParser.T__1);
	            this.state = 397;
	            this.exp(0);
	            break;

	        case 3:
	            this.enterOuterAlt(localctx, 3);
	            this.state = 398;
	            this.exp(0);
	            break;

	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	fieldsep() {
	    let localctx = new FieldsepContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 50, LuaParser.RULE_fieldsep);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 401;
	        _la = this._input.LA(1);
	        if(!(_la===1 || _la===15)) {
	        this._errHandler.recoverInline(this);
	        }
	        else {
	        	this._errHandler.reportMatch(this);
	            this.consume();
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	operatorOr() {
	    let localctx = new OperatorOrContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 52, LuaParser.RULE_operatorOr);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 403;
	        this.match(LuaParser.T__35);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	operatorAnd() {
	    let localctx = new OperatorAndContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 54, LuaParser.RULE_operatorAnd);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 405;
	        this.match(LuaParser.T__36);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	operatorComparison() {
	    let localctx = new OperatorComparisonContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 56, LuaParser.RULE_operatorComparison);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 407;
	        _la = this._input.LA(1);
	        if(!(((((_la - 19)) & ~0x1f) === 0 && ((1 << (_la - 19)) & 7864323) !== 0))) {
	        this._errHandler.recoverInline(this);
	        }
	        else {
	        	this._errHandler.reportMatch(this);
	            this.consume();
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	operatorStrcat() {
	    let localctx = new OperatorStrcatContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 58, LuaParser.RULE_operatorStrcat);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 409;
	        this.match(LuaParser.T__41);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	operatorAddSub() {
	    let localctx = new OperatorAddSubContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 60, LuaParser.RULE_operatorAddSub);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 411;
	        _la = this._input.LA(1);
	        if(!(_la===43 || _la===44)) {
	        this._errHandler.recoverInline(this);
	        }
	        else {
	        	this._errHandler.reportMatch(this);
	            this.consume();
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	operatorMulDivMod() {
	    let localctx = new OperatorMulDivModContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 62, LuaParser.RULE_operatorMulDivMod);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 413;
	        _la = this._input.LA(1);
	        if(!(((((_la - 45)) & ~0x1f) === 0 && ((1 << (_la - 45)) & 15) !== 0))) {
	        this._errHandler.recoverInline(this);
	        }
	        else {
	        	this._errHandler.reportMatch(this);
	            this.consume();
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	operatorBitwise() {
	    let localctx = new OperatorBitwiseContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 64, LuaParser.RULE_operatorBitwise);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 415;
	        _la = this._input.LA(1);
	        if(!(((((_la - 49)) & ~0x1f) === 0 && ((1 << (_la - 49)) & 31) !== 0))) {
	        this._errHandler.recoverInline(this);
	        }
	        else {
	        	this._errHandler.reportMatch(this);
	            this.consume();
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	operatorUnary() {
	    let localctx = new OperatorUnaryContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 66, LuaParser.RULE_operatorUnary);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 417;
	        _la = this._input.LA(1);
	        if(!(((((_la - 44)) & ~0x1f) === 0 && ((1 << (_la - 44)) & 3201) !== 0))) {
	        this._errHandler.recoverInline(this);
	        }
	        else {
	        	this._errHandler.reportMatch(this);
	            this.consume();
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	operatorPower() {
	    let localctx = new OperatorPowerContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 68, LuaParser.RULE_operatorPower);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 419;
	        this.match(LuaParser.T__55);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	number() {
	    let localctx = new NumberContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 70, LuaParser.RULE_number);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 421;
	        _la = this._input.LA(1);
	        if(!(((((_la - 61)) & ~0x1f) === 0 && ((1 << (_la - 61)) & 15) !== 0))) {
	        this._errHandler.recoverInline(this);
	        }
	        else {
	        	this._errHandler.reportMatch(this);
	            this.consume();
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	string() {
	    let localctx = new StringContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 72, LuaParser.RULE_string);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 423;
	        _la = this._input.LA(1);
	        if(!(((((_la - 58)) & ~0x1f) === 0 && ((1 << (_la - 58)) & 7) !== 0))) {
	        this._errHandler.recoverInline(this);
	        }
	        else {
	        	this._errHandler.reportMatch(this);
	            this.consume();
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


}

LuaParser.EOF = antlr4.Token.EOF;
LuaParser.T__0 = 1;
LuaParser.T__1 = 2;
LuaParser.T__2 = 3;
LuaParser.T__3 = 4;
LuaParser.T__4 = 5;
LuaParser.T__5 = 6;
LuaParser.T__6 = 7;
LuaParser.T__7 = 8;
LuaParser.T__8 = 9;
LuaParser.T__9 = 10;
LuaParser.T__10 = 11;
LuaParser.T__11 = 12;
LuaParser.T__12 = 13;
LuaParser.T__13 = 14;
LuaParser.T__14 = 15;
LuaParser.T__15 = 16;
LuaParser.T__16 = 17;
LuaParser.T__17 = 18;
LuaParser.T__18 = 19;
LuaParser.T__19 = 20;
LuaParser.T__20 = 21;
LuaParser.T__21 = 22;
LuaParser.T__22 = 23;
LuaParser.T__23 = 24;
LuaParser.T__24 = 25;
LuaParser.T__25 = 26;
LuaParser.T__26 = 27;
LuaParser.T__27 = 28;
LuaParser.T__28 = 29;
LuaParser.T__29 = 30;
LuaParser.T__30 = 31;
LuaParser.T__31 = 32;
LuaParser.T__32 = 33;
LuaParser.T__33 = 34;
LuaParser.T__34 = 35;
LuaParser.T__35 = 36;
LuaParser.T__36 = 37;
LuaParser.T__37 = 38;
LuaParser.T__38 = 39;
LuaParser.T__39 = 40;
LuaParser.T__40 = 41;
LuaParser.T__41 = 42;
LuaParser.T__42 = 43;
LuaParser.T__43 = 44;
LuaParser.T__44 = 45;
LuaParser.T__45 = 46;
LuaParser.T__46 = 47;
LuaParser.T__47 = 48;
LuaParser.T__48 = 49;
LuaParser.T__49 = 50;
LuaParser.T__50 = 51;
LuaParser.T__51 = 52;
LuaParser.T__52 = 53;
LuaParser.T__53 = 54;
LuaParser.T__54 = 55;
LuaParser.T__55 = 56;
LuaParser.NAME = 57;
LuaParser.NORMALSTRING = 58;
LuaParser.CHARSTRING = 59;
LuaParser.LONGSTRING = 60;
LuaParser.INT = 61;
LuaParser.HEX = 62;
LuaParser.FLOAT = 63;
LuaParser.HEX_FLOAT = 64;
LuaParser.COMMENT = 65;
LuaParser.LINE_COMMENT = 66;
LuaParser.WS = 67;
LuaParser.SHEBANG = 68;

LuaParser.RULE_chunk = 0;
LuaParser.RULE_block = 1;
LuaParser.RULE_stat = 2;
LuaParser.RULE_attnamelist = 3;
LuaParser.RULE_attrib = 4;
LuaParser.RULE_laststat = 5;
LuaParser.RULE_label = 6;
LuaParser.RULE_funcname = 7;
LuaParser.RULE_varlist = 8;
LuaParser.RULE_namelist = 9;
LuaParser.RULE_explist = 10;
LuaParser.RULE_exp = 11;
LuaParser.RULE_prefixexp = 12;
LuaParser.RULE_functioncall = 13;
LuaParser.RULE_varOrExp = 14;
LuaParser.RULE_var = 15;
LuaParser.RULE_varSuffix = 16;
LuaParser.RULE_nameAndArgs = 17;
LuaParser.RULE_args = 18;
LuaParser.RULE_functiondef = 19;
LuaParser.RULE_funcbody = 20;
LuaParser.RULE_parlist = 21;
LuaParser.RULE_tableconstructor = 22;
LuaParser.RULE_fieldlist = 23;
LuaParser.RULE_field = 24;
LuaParser.RULE_fieldsep = 25;
LuaParser.RULE_operatorOr = 26;
LuaParser.RULE_operatorAnd = 27;
LuaParser.RULE_operatorComparison = 28;
LuaParser.RULE_operatorStrcat = 29;
LuaParser.RULE_operatorAddSub = 30;
LuaParser.RULE_operatorMulDivMod = 31;
LuaParser.RULE_operatorBitwise = 32;
LuaParser.RULE_operatorUnary = 33;
LuaParser.RULE_operatorPower = 34;
LuaParser.RULE_number = 35;
LuaParser.RULE_string = 36;

class ChunkContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_chunk;
    }

	block() {
	    return this.getTypedRuleContext(BlockContext,0);
	};

	EOF() {
	    return this.getToken(LuaParser.EOF, 0);
	};

	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterChunk(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitChunk(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitChunk(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class BlockContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_block;
    }

	stat = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(StatContext);
	    } else {
	        return this.getTypedRuleContext(StatContext,i);
	    }
	};

	laststat() {
	    return this.getTypedRuleContext(LaststatContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterBlock(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitBlock(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitBlock(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class StatContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_stat;
    }

	varlist() {
	    return this.getTypedRuleContext(VarlistContext,0);
	};

	explist() {
	    return this.getTypedRuleContext(ExplistContext,0);
	};

	functioncall() {
	    return this.getTypedRuleContext(FunctioncallContext,0);
	};

	label() {
	    return this.getTypedRuleContext(LabelContext,0);
	};

	NAME() {
	    return this.getToken(LuaParser.NAME, 0);
	};

	block = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(BlockContext);
	    } else {
	        return this.getTypedRuleContext(BlockContext,i);
	    }
	};

	exp = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(ExpContext);
	    } else {
	        return this.getTypedRuleContext(ExpContext,i);
	    }
	};

	namelist() {
	    return this.getTypedRuleContext(NamelistContext,0);
	};

	funcname() {
	    return this.getTypedRuleContext(FuncnameContext,0);
	};

	funcbody() {
	    return this.getTypedRuleContext(FuncbodyContext,0);
	};

	attnamelist() {
	    return this.getTypedRuleContext(AttnamelistContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterStat(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitStat(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitStat(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class AttnamelistContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_attnamelist;
    }

	NAME = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(LuaParser.NAME);
	    } else {
	        return this.getToken(LuaParser.NAME, i);
	    }
	};


	attrib = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(AttribContext);
	    } else {
	        return this.getTypedRuleContext(AttribContext,i);
	    }
	};

	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterAttnamelist(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitAttnamelist(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitAttnamelist(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class AttribContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_attrib;
    }

	NAME() {
	    return this.getToken(LuaParser.NAME, 0);
	};

	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterAttrib(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitAttrib(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitAttrib(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class LaststatContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_laststat;
    }

	explist() {
	    return this.getTypedRuleContext(ExplistContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterLaststat(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitLaststat(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitLaststat(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class LabelContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_label;
    }

	NAME() {
	    return this.getToken(LuaParser.NAME, 0);
	};

	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterLabel(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitLabel(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitLabel(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class FuncnameContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_funcname;
    }

	NAME = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(LuaParser.NAME);
	    } else {
	        return this.getToken(LuaParser.NAME, i);
	    }
	};


	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterFuncname(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitFuncname(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitFuncname(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class VarlistContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_varlist;
    }

	var_ = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(VarContext);
	    } else {
	        return this.getTypedRuleContext(VarContext,i);
	    }
	};

	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterVarlist(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitVarlist(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitVarlist(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class NamelistContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_namelist;
    }

	NAME = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(LuaParser.NAME);
	    } else {
	        return this.getToken(LuaParser.NAME, i);
	    }
	};


	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterNamelist(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitNamelist(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitNamelist(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class ExplistContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_explist;
    }

	exp = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(ExpContext);
	    } else {
	        return this.getTypedRuleContext(ExpContext,i);
	    }
	};

	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterExplist(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitExplist(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitExplist(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class ExpContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_exp;
    }

	number() {
	    return this.getTypedRuleContext(NumberContext,0);
	};

	string() {
	    return this.getTypedRuleContext(StringContext,0);
	};

	functiondef() {
	    return this.getTypedRuleContext(FunctiondefContext,0);
	};

	prefixexp() {
	    return this.getTypedRuleContext(PrefixexpContext,0);
	};

	tableconstructor() {
	    return this.getTypedRuleContext(TableconstructorContext,0);
	};

	operatorUnary() {
	    return this.getTypedRuleContext(OperatorUnaryContext,0);
	};

	exp = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(ExpContext);
	    } else {
	        return this.getTypedRuleContext(ExpContext,i);
	    }
	};

	operatorPower() {
	    return this.getTypedRuleContext(OperatorPowerContext,0);
	};

	operatorMulDivMod() {
	    return this.getTypedRuleContext(OperatorMulDivModContext,0);
	};

	operatorAddSub() {
	    return this.getTypedRuleContext(OperatorAddSubContext,0);
	};

	operatorStrcat() {
	    return this.getTypedRuleContext(OperatorStrcatContext,0);
	};

	operatorComparison() {
	    return this.getTypedRuleContext(OperatorComparisonContext,0);
	};

	operatorAnd() {
	    return this.getTypedRuleContext(OperatorAndContext,0);
	};

	operatorOr() {
	    return this.getTypedRuleContext(OperatorOrContext,0);
	};

	operatorBitwise() {
	    return this.getTypedRuleContext(OperatorBitwiseContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterExp(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitExp(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitExp(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class PrefixexpContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_prefixexp;
    }

	varOrExp() {
	    return this.getTypedRuleContext(VarOrExpContext,0);
	};

	nameAndArgs = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(NameAndArgsContext);
	    } else {
	        return this.getTypedRuleContext(NameAndArgsContext,i);
	    }
	};

	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterPrefixexp(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitPrefixexp(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitPrefixexp(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class FunctioncallContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_functioncall;
    }

	varOrExp() {
	    return this.getTypedRuleContext(VarOrExpContext,0);
	};

	nameAndArgs = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(NameAndArgsContext);
	    } else {
	        return this.getTypedRuleContext(NameAndArgsContext,i);
	    }
	};

	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterFunctioncall(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitFunctioncall(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitFunctioncall(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class VarOrExpContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_varOrExp;
    }

	var_() {
	    return this.getTypedRuleContext(VarContext,0);
	};

	exp() {
	    return this.getTypedRuleContext(ExpContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterVarOrExp(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitVarOrExp(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitVarOrExp(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class VarContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_var;
    }

	NAME() {
	    return this.getToken(LuaParser.NAME, 0);
	};

	exp() {
	    return this.getTypedRuleContext(ExpContext,0);
	};

	varSuffix = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(VarSuffixContext);
	    } else {
	        return this.getTypedRuleContext(VarSuffixContext,i);
	    }
	};

	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterVar(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitVar(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitVar(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class VarSuffixContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_varSuffix;
    }

	exp() {
	    return this.getTypedRuleContext(ExpContext,0);
	};

	NAME() {
	    return this.getToken(LuaParser.NAME, 0);
	};

	nameAndArgs = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(NameAndArgsContext);
	    } else {
	        return this.getTypedRuleContext(NameAndArgsContext,i);
	    }
	};

	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterVarSuffix(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitVarSuffix(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitVarSuffix(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class NameAndArgsContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_nameAndArgs;
    }

	args() {
	    return this.getTypedRuleContext(ArgsContext,0);
	};

	NAME() {
	    return this.getToken(LuaParser.NAME, 0);
	};

	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterNameAndArgs(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitNameAndArgs(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitNameAndArgs(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class ArgsContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_args;
    }

	explist() {
	    return this.getTypedRuleContext(ExplistContext,0);
	};

	tableconstructor() {
	    return this.getTypedRuleContext(TableconstructorContext,0);
	};

	string() {
	    return this.getTypedRuleContext(StringContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterArgs(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitArgs(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitArgs(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class FunctiondefContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_functiondef;
    }

	funcbody() {
	    return this.getTypedRuleContext(FuncbodyContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterFunctiondef(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitFunctiondef(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitFunctiondef(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class FuncbodyContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_funcbody;
    }

	block() {
	    return this.getTypedRuleContext(BlockContext,0);
	};

	parlist() {
	    return this.getTypedRuleContext(ParlistContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterFuncbody(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitFuncbody(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitFuncbody(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class ParlistContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_parlist;
    }

	namelist() {
	    return this.getTypedRuleContext(NamelistContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterParlist(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitParlist(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitParlist(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class TableconstructorContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_tableconstructor;
    }

	fieldlist() {
	    return this.getTypedRuleContext(FieldlistContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterTableconstructor(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitTableconstructor(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitTableconstructor(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class FieldlistContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_fieldlist;
    }

	field = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(FieldContext);
	    } else {
	        return this.getTypedRuleContext(FieldContext,i);
	    }
	};

	fieldsep = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(FieldsepContext);
	    } else {
	        return this.getTypedRuleContext(FieldsepContext,i);
	    }
	};

	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterFieldlist(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitFieldlist(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitFieldlist(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class FieldContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_field;
    }

	exp = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(ExpContext);
	    } else {
	        return this.getTypedRuleContext(ExpContext,i);
	    }
	};

	NAME() {
	    return this.getToken(LuaParser.NAME, 0);
	};

	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterField(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitField(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitField(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class FieldsepContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_fieldsep;
    }


	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterFieldsep(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitFieldsep(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitFieldsep(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class OperatorOrContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_operatorOr;
    }


	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterOperatorOr(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitOperatorOr(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitOperatorOr(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class OperatorAndContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_operatorAnd;
    }


	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterOperatorAnd(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitOperatorAnd(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitOperatorAnd(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class OperatorComparisonContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_operatorComparison;
    }


	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterOperatorComparison(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitOperatorComparison(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitOperatorComparison(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class OperatorStrcatContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_operatorStrcat;
    }


	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterOperatorStrcat(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitOperatorStrcat(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitOperatorStrcat(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class OperatorAddSubContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_operatorAddSub;
    }


	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterOperatorAddSub(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitOperatorAddSub(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitOperatorAddSub(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class OperatorMulDivModContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_operatorMulDivMod;
    }


	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterOperatorMulDivMod(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitOperatorMulDivMod(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitOperatorMulDivMod(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class OperatorBitwiseContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_operatorBitwise;
    }


	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterOperatorBitwise(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitOperatorBitwise(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitOperatorBitwise(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class OperatorUnaryContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_operatorUnary;
    }


	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterOperatorUnary(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitOperatorUnary(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitOperatorUnary(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class OperatorPowerContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_operatorPower;
    }


	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterOperatorPower(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitOperatorPower(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitOperatorPower(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class NumberContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_number;
    }

	INT() {
	    return this.getToken(LuaParser.INT, 0);
	};

	HEX() {
	    return this.getToken(LuaParser.HEX, 0);
	};

	FLOAT() {
	    return this.getToken(LuaParser.FLOAT, 0);
	};

	HEX_FLOAT() {
	    return this.getToken(LuaParser.HEX_FLOAT, 0);
	};

	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterNumber(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitNumber(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitNumber(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class StringContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = LuaParser.RULE_string;
    }

	NORMALSTRING() {
	    return this.getToken(LuaParser.NORMALSTRING, 0);
	};

	CHARSTRING() {
	    return this.getToken(LuaParser.CHARSTRING, 0);
	};

	LONGSTRING() {
	    return this.getToken(LuaParser.LONGSTRING, 0);
	};

	enterRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.enterString(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof LuaListener ) {
	        listener.exitString(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof LuaVisitor ) {
	        return visitor.visitString(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}




LuaParser.ChunkContext = ChunkContext; 
LuaParser.BlockContext = BlockContext; 
LuaParser.StatContext = StatContext; 
LuaParser.AttnamelistContext = AttnamelistContext; 
LuaParser.AttribContext = AttribContext; 
LuaParser.LaststatContext = LaststatContext; 
LuaParser.LabelContext = LabelContext; 
LuaParser.FuncnameContext = FuncnameContext; 
LuaParser.VarlistContext = VarlistContext; 
LuaParser.NamelistContext = NamelistContext; 
LuaParser.ExplistContext = ExplistContext; 
LuaParser.ExpContext = ExpContext; 
LuaParser.PrefixexpContext = PrefixexpContext; 
LuaParser.FunctioncallContext = FunctioncallContext; 
LuaParser.VarOrExpContext = VarOrExpContext; 
LuaParser.VarContext = VarContext; 
LuaParser.VarSuffixContext = VarSuffixContext; 
LuaParser.NameAndArgsContext = NameAndArgsContext; 
LuaParser.ArgsContext = ArgsContext; 
LuaParser.FunctiondefContext = FunctiondefContext; 
LuaParser.FuncbodyContext = FuncbodyContext; 
LuaParser.ParlistContext = ParlistContext; 
LuaParser.TableconstructorContext = TableconstructorContext; 
LuaParser.FieldlistContext = FieldlistContext; 
LuaParser.FieldContext = FieldContext; 
LuaParser.FieldsepContext = FieldsepContext; 
LuaParser.OperatorOrContext = OperatorOrContext; 
LuaParser.OperatorAndContext = OperatorAndContext; 
LuaParser.OperatorComparisonContext = OperatorComparisonContext; 
LuaParser.OperatorStrcatContext = OperatorStrcatContext; 
LuaParser.OperatorAddSubContext = OperatorAddSubContext; 
LuaParser.OperatorMulDivModContext = OperatorMulDivModContext; 
LuaParser.OperatorBitwiseContext = OperatorBitwiseContext; 
LuaParser.OperatorUnaryContext = OperatorUnaryContext; 
LuaParser.OperatorPowerContext = OperatorPowerContext; 
LuaParser.NumberContext = NumberContext; 
LuaParser.StringContext = StringContext; 
