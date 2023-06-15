# Generated from ../grammars/Tua.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,57,382,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,1,0,1,0,1,0,1,1,1,1,3,1,92,8,1,5,1,
        94,8,1,10,1,12,1,97,9,1,1,1,3,1,100,8,1,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,3,2,111,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,
        3,5,123,8,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,3,7,134,8,7,1,8,
        1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,4,9,146,8,9,11,9,12,9,147,1,
        9,1,9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,3,11,160,8,11,3,11,
        162,8,11,1,12,1,12,1,12,1,12,1,12,1,12,4,12,170,8,12,11,12,12,12,
        171,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,
        185,8,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,5,13,215,8,13,10,13,12,13,218,9,13,1,14,1,14,
        1,14,1,14,1,15,1,15,3,15,226,8,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,5,18,253,8,18,10,18,12,18,256,9,18,
        1,18,1,18,3,18,260,8,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,3,19,272,8,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,22,1,22,1,22,
        3,22,295,8,22,1,22,3,22,298,8,22,1,23,1,23,3,23,302,8,23,1,24,1,
        24,1,25,1,25,1,26,1,26,1,26,5,26,311,8,26,10,26,12,26,314,9,26,1,
        27,1,27,1,27,3,27,319,8,27,1,27,1,27,1,28,1,28,1,28,5,28,326,8,28,
        10,28,12,28,329,9,28,1,29,1,29,3,29,333,8,29,1,29,1,29,1,30,1,30,
        1,30,5,30,340,8,30,10,30,12,30,343,9,30,1,31,1,31,1,31,1,31,1,31,
        1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,31,358,8,31,1,32,1,32,
        1,33,1,33,1,34,1,34,1,35,1,35,1,36,1,36,1,37,1,37,1,38,1,38,1,39,
        1,39,1,40,1,40,1,41,1,41,1,42,1,42,1,42,0,1,26,43,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,
        58,60,62,64,66,68,70,72,74,76,78,80,82,84,0,9,1,0,29,30,1,0,31,34,
        1,0,35,40,1,0,42,43,1,0,44,45,2,0,30,30,47,47,1,0,54,55,1,0,52,53,
        1,0,48,49,388,0,86,1,0,0,0,2,95,1,0,0,0,4,110,1,0,0,0,6,112,1,0,
        0,0,8,116,1,0,0,0,10,120,1,0,0,0,12,124,1,0,0,0,14,133,1,0,0,0,16,
        135,1,0,0,0,18,140,1,0,0,0,20,151,1,0,0,0,22,161,1,0,0,0,24,169,
        1,0,0,0,26,184,1,0,0,0,28,219,1,0,0,0,30,223,1,0,0,0,32,233,1,0,
        0,0,34,237,1,0,0,0,36,243,1,0,0,0,38,263,1,0,0,0,40,277,1,0,0,0,
        42,287,1,0,0,0,44,294,1,0,0,0,46,299,1,0,0,0,48,303,1,0,0,0,50,305,
        1,0,0,0,52,307,1,0,0,0,54,315,1,0,0,0,56,322,1,0,0,0,58,330,1,0,
        0,0,60,336,1,0,0,0,62,357,1,0,0,0,64,359,1,0,0,0,66,361,1,0,0,0,
        68,363,1,0,0,0,70,365,1,0,0,0,72,367,1,0,0,0,74,369,1,0,0,0,76,371,
        1,0,0,0,78,373,1,0,0,0,80,375,1,0,0,0,82,377,1,0,0,0,84,379,1,0,
        0,0,86,87,3,2,1,0,87,88,5,0,0,1,88,1,1,0,0,0,89,91,3,4,2,0,90,92,
        5,1,0,0,91,90,1,0,0,0,91,92,1,0,0,0,92,94,1,0,0,0,93,89,1,0,0,0,
        94,97,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,99,1,0,0,0,97,95,1,
        0,0,0,98,100,3,44,22,0,99,98,1,0,0,0,99,100,1,0,0,0,100,3,1,0,0,
        0,101,111,3,8,4,0,102,111,3,6,3,0,103,111,3,54,27,0,104,111,3,32,
        16,0,105,111,3,34,17,0,106,111,3,36,18,0,107,111,3,38,19,0,108,111,
        3,40,20,0,109,111,3,42,21,0,110,101,1,0,0,0,110,102,1,0,0,0,110,
        103,1,0,0,0,110,104,1,0,0,0,110,105,1,0,0,0,110,106,1,0,0,0,110,
        107,1,0,0,0,110,108,1,0,0,0,110,109,1,0,0,0,111,5,1,0,0,0,112,113,
        3,10,5,0,113,114,5,2,0,0,114,115,3,26,13,0,115,7,1,0,0,0,116,117,
        3,12,6,0,117,118,5,2,0,0,118,119,3,26,13,0,119,9,1,0,0,0,120,122,
        5,51,0,0,121,123,3,24,12,0,122,121,1,0,0,0,122,123,1,0,0,0,123,11,
        1,0,0,0,124,125,5,51,0,0,125,126,5,3,0,0,126,127,3,14,7,0,127,13,
        1,0,0,0,128,134,5,51,0,0,129,134,5,50,0,0,130,134,3,20,10,0,131,
        134,3,18,9,0,132,134,3,16,8,0,133,128,1,0,0,0,133,129,1,0,0,0,133,
        130,1,0,0,0,133,131,1,0,0,0,133,132,1,0,0,0,134,15,1,0,0,0,135,136,
        5,4,0,0,136,137,5,5,0,0,137,138,3,14,7,0,138,139,5,6,0,0,139,17,
        1,0,0,0,140,141,5,7,0,0,141,142,5,5,0,0,142,145,3,14,7,0,143,144,
        5,8,0,0,144,146,3,14,7,0,145,143,1,0,0,0,146,147,1,0,0,0,147,145,
        1,0,0,0,147,148,1,0,0,0,148,149,1,0,0,0,149,150,5,6,0,0,150,19,1,
        0,0,0,151,152,5,9,0,0,152,153,5,5,0,0,153,154,3,14,7,0,154,155,5,
        6,0,0,155,21,1,0,0,0,156,162,3,10,5,0,157,159,3,54,27,0,158,160,
        3,24,12,0,159,158,1,0,0,0,159,160,1,0,0,0,160,162,1,0,0,0,161,156,
        1,0,0,0,161,157,1,0,0,0,162,23,1,0,0,0,163,164,5,5,0,0,164,165,3,
        26,13,0,165,166,5,6,0,0,166,170,1,0,0,0,167,168,5,10,0,0,168,170,
        5,51,0,0,169,163,1,0,0,0,169,167,1,0,0,0,170,171,1,0,0,0,171,169,
        1,0,0,0,171,172,1,0,0,0,172,25,1,0,0,0,173,174,6,13,-1,0,174,185,
        3,28,14,0,175,185,3,82,41,0,176,185,3,80,40,0,177,185,3,84,42,0,
        178,185,5,50,0,0,179,185,3,22,11,0,180,181,3,78,39,0,181,182,3,26,
        13,8,182,185,1,0,0,0,183,185,3,58,29,0,184,173,1,0,0,0,184,175,1,
        0,0,0,184,176,1,0,0,0,184,177,1,0,0,0,184,178,1,0,0,0,184,179,1,
        0,0,0,184,180,1,0,0,0,184,183,1,0,0,0,185,216,1,0,0,0,186,187,10,
        9,0,0,187,188,3,76,38,0,188,189,3,26,13,9,189,215,1,0,0,0,190,191,
        10,7,0,0,191,192,3,66,33,0,192,193,3,26,13,8,193,215,1,0,0,0,194,
        195,10,6,0,0,195,196,3,64,32,0,196,197,3,26,13,7,197,215,1,0,0,0,
        198,199,10,5,0,0,199,200,3,70,35,0,200,201,3,26,13,5,201,215,1,0,
        0,0,202,203,10,4,0,0,203,204,3,68,34,0,204,205,3,26,13,5,205,215,
        1,0,0,0,206,207,10,3,0,0,207,208,3,72,36,0,208,209,3,26,13,4,209,
        215,1,0,0,0,210,211,10,2,0,0,211,212,3,74,37,0,212,213,3,26,13,3,
        213,215,1,0,0,0,214,186,1,0,0,0,214,190,1,0,0,0,214,194,1,0,0,0,
        214,198,1,0,0,0,214,202,1,0,0,0,214,206,1,0,0,0,214,210,1,0,0,0,
        215,218,1,0,0,0,216,214,1,0,0,0,216,217,1,0,0,0,217,27,1,0,0,0,218,
        216,1,0,0,0,219,220,5,11,0,0,220,221,3,26,13,0,221,222,5,12,0,0,
        222,29,1,0,0,0,223,225,5,11,0,0,224,226,3,52,26,0,225,224,1,0,0,
        0,225,226,1,0,0,0,226,227,1,0,0,0,227,228,5,12,0,0,228,229,5,13,
        0,0,229,230,3,14,7,0,230,231,3,2,1,0,231,232,5,14,0,0,232,31,1,0,
        0,0,233,234,5,15,0,0,234,235,3,2,1,0,235,236,5,14,0,0,236,33,1,0,
        0,0,237,238,5,16,0,0,238,239,3,26,13,0,239,240,5,15,0,0,240,241,
        3,2,1,0,241,242,5,14,0,0,242,35,1,0,0,0,243,244,5,17,0,0,244,245,
        3,26,13,0,245,246,5,18,0,0,246,254,3,2,1,0,247,248,5,19,0,0,248,
        249,3,26,13,0,249,250,5,18,0,0,250,251,3,2,1,0,251,253,1,0,0,0,252,
        247,1,0,0,0,253,256,1,0,0,0,254,252,1,0,0,0,254,255,1,0,0,0,255,
        259,1,0,0,0,256,254,1,0,0,0,257,258,5,20,0,0,258,260,3,2,1,0,259,
        257,1,0,0,0,259,260,1,0,0,0,260,261,1,0,0,0,261,262,5,14,0,0,262,
        37,1,0,0,0,263,264,5,21,0,0,264,265,5,51,0,0,265,266,5,2,0,0,266,
        267,3,26,13,0,267,268,5,8,0,0,268,271,3,26,13,0,269,270,5,8,0,0,
        270,272,3,26,13,0,271,269,1,0,0,0,271,272,1,0,0,0,272,273,1,0,0,
        0,273,274,5,15,0,0,274,275,3,2,1,0,275,276,5,14,0,0,276,39,1,0,0,
        0,277,278,5,21,0,0,278,279,5,51,0,0,279,280,5,8,0,0,280,281,5,51,
        0,0,281,282,5,22,0,0,282,283,3,54,27,0,283,284,5,15,0,0,284,285,
        3,2,1,0,285,286,5,14,0,0,286,41,1,0,0,0,287,288,5,23,0,0,288,289,
        5,51,0,0,289,290,3,30,15,0,290,43,1,0,0,0,291,295,3,46,23,0,292,
        295,3,48,24,0,293,295,3,50,25,0,294,291,1,0,0,0,294,292,1,0,0,0,
        294,293,1,0,0,0,295,297,1,0,0,0,296,298,5,1,0,0,297,296,1,0,0,0,
        297,298,1,0,0,0,298,45,1,0,0,0,299,301,5,24,0,0,300,302,3,56,28,
        0,301,300,1,0,0,0,301,302,1,0,0,0,302,47,1,0,0,0,303,304,5,25,0,
        0,304,49,1,0,0,0,305,306,5,26,0,0,306,51,1,0,0,0,307,312,3,12,6,
        0,308,309,5,8,0,0,309,311,3,12,6,0,310,308,1,0,0,0,311,314,1,0,0,
        0,312,310,1,0,0,0,312,313,1,0,0,0,313,53,1,0,0,0,314,312,1,0,0,0,
        315,316,5,51,0,0,316,318,5,11,0,0,317,319,3,56,28,0,318,317,1,0,
        0,0,318,319,1,0,0,0,319,320,1,0,0,0,320,321,5,12,0,0,321,55,1,0,
        0,0,322,327,3,26,13,0,323,324,5,8,0,0,324,326,3,26,13,0,325,323,
        1,0,0,0,326,329,1,0,0,0,327,325,1,0,0,0,327,328,1,0,0,0,328,57,1,
        0,0,0,329,327,1,0,0,0,330,332,5,27,0,0,331,333,3,60,30,0,332,331,
        1,0,0,0,332,333,1,0,0,0,333,334,1,0,0,0,334,335,5,28,0,0,335,59,
        1,0,0,0,336,341,3,62,31,0,337,338,5,8,0,0,338,340,3,62,31,0,339,
        337,1,0,0,0,340,343,1,0,0,0,341,339,1,0,0,0,341,342,1,0,0,0,342,
        61,1,0,0,0,343,341,1,0,0,0,344,345,5,5,0,0,345,346,3,26,13,0,346,
        347,5,6,0,0,347,348,5,3,0,0,348,349,3,14,7,0,349,350,5,2,0,0,350,
        351,3,26,13,0,351,358,1,0,0,0,352,353,3,12,6,0,353,354,5,2,0,0,354,
        355,3,26,13,0,355,358,1,0,0,0,356,358,3,26,13,0,357,344,1,0,0,0,
        357,352,1,0,0,0,357,356,1,0,0,0,358,63,1,0,0,0,359,360,7,0,0,0,360,
        65,1,0,0,0,361,362,7,1,0,0,362,67,1,0,0,0,363,364,7,2,0,0,364,69,
        1,0,0,0,365,366,5,41,0,0,366,71,1,0,0,0,367,368,7,3,0,0,368,73,1,
        0,0,0,369,370,7,4,0,0,370,75,1,0,0,0,371,372,5,46,0,0,372,77,1,0,
        0,0,373,374,7,5,0,0,374,79,1,0,0,0,375,376,7,6,0,0,376,81,1,0,0,
        0,377,378,7,7,0,0,378,83,1,0,0,0,379,380,7,8,0,0,380,85,1,0,0,0,
        27,91,95,99,110,122,133,147,159,161,169,171,184,214,216,225,254,
        259,271,294,297,301,312,318,327,332,341,357
    ]

class TuaParser ( Parser ):

    grammarFileName = "Tua.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "':'", "'Table'", "'['", 
                     "']'", "'Union'", "','", "'List'", "'.'", "'('", "')'", 
                     "'->'", "'end'", "'do'", "'while'", "'if'", "'then'", 
                     "'elseif'", "'else'", "'for'", "'in'", "'function'", 
                     "'return'", "'break'", "'continue'", "'{'", "'}'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'//'", "'=='", 
                     "'~='", "'<='", "'>='", "'<'", "'>'", "'..'", "'and'", 
                     "'&'", "'or'", "'|'", "'^'", "'not'", "'false'", "'true'", 
                     "'nil'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "FALSE", "TRUE", "NIL", "NAME", "INT", "FLOAT", "DOUBLEQUOTESTRING", 
                      "SINGLEQUOTESTRING", "LINE_COMMENT", "WHITESPACE" ]

    RULE_program = 0
    RULE_block = 1
    RULE_stat = 2
    RULE_assignment = 3
    RULE_newvariable = 4
    RULE_var = 5
    RULE_nametype = 6
    RULE_type = 7
    RULE_tableType = 8
    RULE_unionType = 9
    RULE_listType = 10
    RULE_prefix = 11
    RULE_suffix = 12
    RULE_exp = 13
    RULE_parexp = 14
    RULE_functionbody = 15
    RULE_dostat = 16
    RULE_whilestat = 17
    RULE_ifstat = 18
    RULE_forintstat = 19
    RULE_foriteratorstat = 20
    RULE_functiondef = 21
    RULE_laststat = 22
    RULE_return = 23
    RULE_break = 24
    RULE_continue = 25
    RULE_typednamelist = 26
    RULE_functioncall = 27
    RULE_explist = 28
    RULE_tableconstructor = 29
    RULE_fieldlist = 30
    RULE_field = 31
    RULE_binopAddSub = 32
    RULE_binopMulDivMod = 33
    RULE_binopComparison = 34
    RULE_binopConcat = 35
    RULE_binopAnd = 36
    RULE_binopOr = 37
    RULE_binopPower = 38
    RULE_unop = 39
    RULE_string = 40
    RULE_number = 41
    RULE_bool = 42

    ruleNames =  [ "program", "block", "stat", "assignment", "newvariable", 
                   "var", "nametype", "type", "tableType", "unionType", 
                   "listType", "prefix", "suffix", "exp", "parexp", "functionbody", 
                   "dostat", "whilestat", "ifstat", "forintstat", "foriteratorstat", 
                   "functiondef", "laststat", "return", "break", "continue", 
                   "typednamelist", "functioncall", "explist", "tableconstructor", 
                   "fieldlist", "field", "binopAddSub", "binopMulDivMod", 
                   "binopComparison", "binopConcat", "binopAnd", "binopOr", 
                   "binopPower", "unop", "string", "number", "bool" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    FALSE=48
    TRUE=49
    NIL=50
    NAME=51
    INT=52
    FLOAT=53
    DOUBLEQUOTESTRING=54
    SINGLEQUOTESTRING=55
    LINE_COMMENT=56
    WHITESPACE=57

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(TuaParser.BlockContext,0)


        def EOF(self):
            return self.getToken(TuaParser.EOF, 0)

        def getRuleIndex(self):
            return TuaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = TuaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.block()
            self.state = 87
            self.match(TuaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TuaParser.StatContext)
            else:
                return self.getTypedRuleContext(TuaParser.StatContext,i)


        def laststat(self):
            return self.getTypedRuleContext(TuaParser.LaststatContext,0)


        def getRuleIndex(self):
            return TuaParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = TuaParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2251799824400384) != 0):
                self.state = 89
                self.stat()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 90
                    self.match(TuaParser.T__0)


                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 117440512) != 0):
                self.state = 98
                self.laststat()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newvariable(self):
            return self.getTypedRuleContext(TuaParser.NewvariableContext,0)


        def assignment(self):
            return self.getTypedRuleContext(TuaParser.AssignmentContext,0)


        def functioncall(self):
            return self.getTypedRuleContext(TuaParser.FunctioncallContext,0)


        def dostat(self):
            return self.getTypedRuleContext(TuaParser.DostatContext,0)


        def whilestat(self):
            return self.getTypedRuleContext(TuaParser.WhilestatContext,0)


        def ifstat(self):
            return self.getTypedRuleContext(TuaParser.IfstatContext,0)


        def forintstat(self):
            return self.getTypedRuleContext(TuaParser.ForintstatContext,0)


        def foriteratorstat(self):
            return self.getTypedRuleContext(TuaParser.ForiteratorstatContext,0)


        def functiondef(self):
            return self.getTypedRuleContext(TuaParser.FunctiondefContext,0)


        def getRuleIndex(self):
            return TuaParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = TuaParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stat)
        try:
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.newvariable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 103
                self.functioncall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 104
                self.dostat()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 105
                self.whilestat()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 106
                self.ifstat()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 107
                self.forintstat()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 108
                self.foriteratorstat()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 109
                self.functiondef()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(TuaParser.VarContext,0)


        def exp(self):
            return self.getTypedRuleContext(TuaParser.ExpContext,0)


        def getRuleIndex(self):
            return TuaParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = TuaParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.var()
            self.state = 113
            self.match(TuaParser.T__1)
            self.state = 114
            self.exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewvariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nametype(self):
            return self.getTypedRuleContext(TuaParser.NametypeContext,0)


        def exp(self):
            return self.getTypedRuleContext(TuaParser.ExpContext,0)


        def getRuleIndex(self):
            return TuaParser.RULE_newvariable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewvariable" ):
                listener.enterNewvariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewvariable" ):
                listener.exitNewvariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewvariable" ):
                return visitor.visitNewvariable(self)
            else:
                return visitor.visitChildren(self)




    def newvariable(self):

        localctx = TuaParser.NewvariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_newvariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.nametype()
            self.state = 117
            self.match(TuaParser.T__1)
            self.state = 118
            self.exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(TuaParser.NAME, 0)

        def suffix(self):
            return self.getTypedRuleContext(TuaParser.SuffixContext,0)


        def getRuleIndex(self):
            return TuaParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = TuaParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(TuaParser.NAME)
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 121
                self.suffix()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NametypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(TuaParser.NAME, 0)

        def type_(self):
            return self.getTypedRuleContext(TuaParser.TypeContext,0)


        def getRuleIndex(self):
            return TuaParser.RULE_nametype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNametype" ):
                listener.enterNametype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNametype" ):
                listener.exitNametype(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNametype" ):
                return visitor.visitNametype(self)
            else:
                return visitor.visitChildren(self)




    def nametype(self):

        localctx = TuaParser.NametypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_nametype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(TuaParser.NAME)
            self.state = 125
            self.match(TuaParser.T__2)
            self.state = 126
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(TuaParser.NAME, 0)

        def NIL(self):
            return self.getToken(TuaParser.NIL, 0)

        def listType(self):
            return self.getTypedRuleContext(TuaParser.ListTypeContext,0)


        def unionType(self):
            return self.getTypedRuleContext(TuaParser.UnionTypeContext,0)


        def tableType(self):
            return self.getTypedRuleContext(TuaParser.TableTypeContext,0)


        def getRuleIndex(self):
            return TuaParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = TuaParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_type)
        try:
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.match(TuaParser.NAME)
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.match(TuaParser.NIL)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 130
                self.listType()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 131
                self.unionType()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 132
                self.tableType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(TuaParser.TypeContext,0)


        def getRuleIndex(self):
            return TuaParser.RULE_tableType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableType" ):
                listener.enterTableType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableType" ):
                listener.exitTableType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableType" ):
                return visitor.visitTableType(self)
            else:
                return visitor.visitChildren(self)




    def tableType(self):

        localctx = TuaParser.TableTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_tableType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(TuaParser.T__3)
            self.state = 136
            self.match(TuaParser.T__4)
            self.state = 137
            self.type_()
            self.state = 138
            self.match(TuaParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnionTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TuaParser.TypeContext)
            else:
                return self.getTypedRuleContext(TuaParser.TypeContext,i)


        def getRuleIndex(self):
            return TuaParser.RULE_unionType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnionType" ):
                listener.enterUnionType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnionType" ):
                listener.exitUnionType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnionType" ):
                return visitor.visitUnionType(self)
            else:
                return visitor.visitChildren(self)




    def unionType(self):

        localctx = TuaParser.UnionTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_unionType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(TuaParser.T__6)
            self.state = 141
            self.match(TuaParser.T__4)
            self.state = 142
            self.type_()
            self.state = 145 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 143
                self.match(TuaParser.T__7)
                self.state = 144
                self.type_()
                self.state = 147 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==8):
                    break

            self.state = 149
            self.match(TuaParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(TuaParser.TypeContext,0)


        def getRuleIndex(self):
            return TuaParser.RULE_listType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListType" ):
                listener.enterListType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListType" ):
                listener.exitListType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListType" ):
                return visitor.visitListType(self)
            else:
                return visitor.visitChildren(self)




    def listType(self):

        localctx = TuaParser.ListTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_listType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(TuaParser.T__8)
            self.state = 152
            self.match(TuaParser.T__4)
            self.state = 153
            self.type_()
            self.state = 154
            self.match(TuaParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrefixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(TuaParser.VarContext,0)


        def functioncall(self):
            return self.getTypedRuleContext(TuaParser.FunctioncallContext,0)


        def suffix(self):
            return self.getTypedRuleContext(TuaParser.SuffixContext,0)


        def getRuleIndex(self):
            return TuaParser.RULE_prefix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrefix" ):
                listener.enterPrefix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrefix" ):
                listener.exitPrefix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrefix" ):
                return visitor.visitPrefix(self)
            else:
                return visitor.visitChildren(self)




    def prefix(self):

        localctx = TuaParser.PrefixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_prefix)
        try:
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.functioncall()
                self.state = 159
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 158
                    self.suffix()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SuffixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(TuaParser.ExpContext,i)


        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(TuaParser.NAME)
            else:
                return self.getToken(TuaParser.NAME, i)

        def getRuleIndex(self):
            return TuaParser.RULE_suffix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuffix" ):
                listener.enterSuffix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuffix" ):
                listener.exitSuffix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuffix" ):
                return visitor.visitSuffix(self)
            else:
                return visitor.visitChildren(self)




    def suffix(self):

        localctx = TuaParser.SuffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_suffix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 169
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [5]:
                        self.state = 163
                        self.match(TuaParser.T__4)
                        self.state = 164
                        self.exp(0)
                        self.state = 165
                        self.match(TuaParser.T__5)
                        pass
                    elif token in [10]:
                        self.state = 167
                        self.match(TuaParser.T__9)
                        self.state = 168
                        self.match(TuaParser.NAME)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 171 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parexp(self):
            return self.getTypedRuleContext(TuaParser.ParexpContext,0)


        def number(self):
            return self.getTypedRuleContext(TuaParser.NumberContext,0)


        def string(self):
            return self.getTypedRuleContext(TuaParser.StringContext,0)


        def bool_(self):
            return self.getTypedRuleContext(TuaParser.BoolContext,0)


        def NIL(self):
            return self.getToken(TuaParser.NIL, 0)

        def prefix(self):
            return self.getTypedRuleContext(TuaParser.PrefixContext,0)


        def unop(self):
            return self.getTypedRuleContext(TuaParser.UnopContext,0)


        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(TuaParser.ExpContext,i)


        def tableconstructor(self):
            return self.getTypedRuleContext(TuaParser.TableconstructorContext,0)


        def binopPower(self):
            return self.getTypedRuleContext(TuaParser.BinopPowerContext,0)


        def binopMulDivMod(self):
            return self.getTypedRuleContext(TuaParser.BinopMulDivModContext,0)


        def binopAddSub(self):
            return self.getTypedRuleContext(TuaParser.BinopAddSubContext,0)


        def binopConcat(self):
            return self.getTypedRuleContext(TuaParser.BinopConcatContext,0)


        def binopComparison(self):
            return self.getTypedRuleContext(TuaParser.BinopComparisonContext,0)


        def binopAnd(self):
            return self.getTypedRuleContext(TuaParser.BinopAndContext,0)


        def binopOr(self):
            return self.getTypedRuleContext(TuaParser.BinopOrContext,0)


        def getRuleIndex(self):
            return TuaParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TuaParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_exp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.state = 174
                self.parexp()
                pass
            elif token in [52, 53]:
                self.state = 175
                self.number()
                pass
            elif token in [54, 55]:
                self.state = 176
                self.string()
                pass
            elif token in [48, 49]:
                self.state = 177
                self.bool_()
                pass
            elif token in [50]:
                self.state = 178
                self.match(TuaParser.NIL)
                pass
            elif token in [51]:
                self.state = 179
                self.prefix()
                pass
            elif token in [30, 47]:
                self.state = 180
                self.unop()
                self.state = 181
                self.exp(8)
                pass
            elif token in [27]:
                self.state = 183
                self.tableconstructor()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 216
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 214
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = TuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 186
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 187
                        self.binopPower()
                        self.state = 188
                        self.exp(9)
                        pass

                    elif la_ == 2:
                        localctx = TuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 190
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 191
                        self.binopMulDivMod()
                        self.state = 192
                        self.exp(8)
                        pass

                    elif la_ == 3:
                        localctx = TuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 194
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 195
                        self.binopAddSub()
                        self.state = 196
                        self.exp(7)
                        pass

                    elif la_ == 4:
                        localctx = TuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 198
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 199
                        self.binopConcat()
                        self.state = 200
                        self.exp(5)
                        pass

                    elif la_ == 5:
                        localctx = TuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 202
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 203
                        self.binopComparison()
                        self.state = 204
                        self.exp(5)
                        pass

                    elif la_ == 6:
                        localctx = TuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 206
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 207
                        self.binopAnd()
                        self.state = 208
                        self.exp(4)
                        pass

                    elif la_ == 7:
                        localctx = TuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 210
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 211
                        self.binopOr()
                        self.state = 212
                        self.exp(3)
                        pass

             
                self.state = 218
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ParexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(TuaParser.ExpContext,0)


        def getRuleIndex(self):
            return TuaParser.RULE_parexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParexp" ):
                listener.enterParexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParexp" ):
                listener.exitParexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParexp" ):
                return visitor.visitParexp(self)
            else:
                return visitor.visitChildren(self)




    def parexp(self):

        localctx = TuaParser.ParexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_parexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(TuaParser.T__10)
            self.state = 220
            self.exp(0)
            self.state = 221
            self.match(TuaParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionbodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(TuaParser.TypeContext,0)


        def block(self):
            return self.getTypedRuleContext(TuaParser.BlockContext,0)


        def typednamelist(self):
            return self.getTypedRuleContext(TuaParser.TypednamelistContext,0)


        def getRuleIndex(self):
            return TuaParser.RULE_functionbody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionbody" ):
                listener.enterFunctionbody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionbody" ):
                listener.exitFunctionbody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionbody" ):
                return visitor.visitFunctionbody(self)
            else:
                return visitor.visitChildren(self)




    def functionbody(self):

        localctx = TuaParser.FunctionbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_functionbody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(TuaParser.T__10)
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==51:
                self.state = 224
                self.typednamelist()


            self.state = 227
            self.match(TuaParser.T__11)
            self.state = 228
            self.match(TuaParser.T__12)
            self.state = 229
            self.type_()
            self.state = 230
            self.block()
            self.state = 231
            self.match(TuaParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DostatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(TuaParser.BlockContext,0)


        def getRuleIndex(self):
            return TuaParser.RULE_dostat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDostat" ):
                listener.enterDostat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDostat" ):
                listener.exitDostat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDostat" ):
                return visitor.visitDostat(self)
            else:
                return visitor.visitChildren(self)




    def dostat(self):

        localctx = TuaParser.DostatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_dostat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(TuaParser.T__14)
            self.state = 234
            self.block()
            self.state = 235
            self.match(TuaParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhilestatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(TuaParser.ExpContext,0)


        def block(self):
            return self.getTypedRuleContext(TuaParser.BlockContext,0)


        def getRuleIndex(self):
            return TuaParser.RULE_whilestat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhilestat" ):
                listener.enterWhilestat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhilestat" ):
                listener.exitWhilestat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhilestat" ):
                return visitor.visitWhilestat(self)
            else:
                return visitor.visitChildren(self)




    def whilestat(self):

        localctx = TuaParser.WhilestatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_whilestat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(TuaParser.T__15)
            self.state = 238
            self.exp(0)
            self.state = 239
            self.match(TuaParser.T__14)
            self.state = 240
            self.block()
            self.state = 241
            self.match(TuaParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(TuaParser.ExpContext,i)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TuaParser.BlockContext)
            else:
                return self.getTypedRuleContext(TuaParser.BlockContext,i)


        def getRuleIndex(self):
            return TuaParser.RULE_ifstat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfstat" ):
                listener.enterIfstat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfstat" ):
                listener.exitIfstat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstat" ):
                return visitor.visitIfstat(self)
            else:
                return visitor.visitChildren(self)




    def ifstat(self):

        localctx = TuaParser.IfstatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_ifstat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(TuaParser.T__16)
            self.state = 244
            self.exp(0)
            self.state = 245
            self.match(TuaParser.T__17)
            self.state = 246
            self.block()
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 247
                self.match(TuaParser.T__18)
                self.state = 248
                self.exp(0)
                self.state = 249
                self.match(TuaParser.T__17)
                self.state = 250
                self.block()
                self.state = 256
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 257
                self.match(TuaParser.T__19)
                self.state = 258
                self.block()


            self.state = 261
            self.match(TuaParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForintstatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(TuaParser.NAME, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(TuaParser.ExpContext,i)


        def block(self):
            return self.getTypedRuleContext(TuaParser.BlockContext,0)


        def getRuleIndex(self):
            return TuaParser.RULE_forintstat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForintstat" ):
                listener.enterForintstat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForintstat" ):
                listener.exitForintstat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForintstat" ):
                return visitor.visitForintstat(self)
            else:
                return visitor.visitChildren(self)




    def forintstat(self):

        localctx = TuaParser.ForintstatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_forintstat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(TuaParser.T__20)
            self.state = 264
            self.match(TuaParser.NAME)
            self.state = 265
            self.match(TuaParser.T__1)
            self.state = 266
            self.exp(0)
            self.state = 267
            self.match(TuaParser.T__7)
            self.state = 268
            self.exp(0)
            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 269
                self.match(TuaParser.T__7)
                self.state = 270
                self.exp(0)


            self.state = 273
            self.match(TuaParser.T__14)
            self.state = 274
            self.block()
            self.state = 275
            self.match(TuaParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForiteratorstatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(TuaParser.NAME)
            else:
                return self.getToken(TuaParser.NAME, i)

        def functioncall(self):
            return self.getTypedRuleContext(TuaParser.FunctioncallContext,0)


        def block(self):
            return self.getTypedRuleContext(TuaParser.BlockContext,0)


        def getRuleIndex(self):
            return TuaParser.RULE_foriteratorstat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForiteratorstat" ):
                listener.enterForiteratorstat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForiteratorstat" ):
                listener.exitForiteratorstat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForiteratorstat" ):
                return visitor.visitForiteratorstat(self)
            else:
                return visitor.visitChildren(self)




    def foriteratorstat(self):

        localctx = TuaParser.ForiteratorstatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_foriteratorstat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(TuaParser.T__20)
            self.state = 278
            self.match(TuaParser.NAME)
            self.state = 279
            self.match(TuaParser.T__7)
            self.state = 280
            self.match(TuaParser.NAME)
            self.state = 281
            self.match(TuaParser.T__21)
            self.state = 282
            self.functioncall()
            self.state = 283
            self.match(TuaParser.T__14)
            self.state = 284
            self.block()
            self.state = 285
            self.match(TuaParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctiondefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(TuaParser.NAME, 0)

        def functionbody(self):
            return self.getTypedRuleContext(TuaParser.FunctionbodyContext,0)


        def getRuleIndex(self):
            return TuaParser.RULE_functiondef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctiondef" ):
                listener.enterFunctiondef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctiondef" ):
                listener.exitFunctiondef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctiondef" ):
                return visitor.visitFunctiondef(self)
            else:
                return visitor.visitChildren(self)




    def functiondef(self):

        localctx = TuaParser.FunctiondefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_functiondef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(TuaParser.T__22)
            self.state = 288
            self.match(TuaParser.NAME)
            self.state = 289
            self.functionbody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LaststatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def return_(self):
            return self.getTypedRuleContext(TuaParser.ReturnContext,0)


        def break_(self):
            return self.getTypedRuleContext(TuaParser.BreakContext,0)


        def continue_(self):
            return self.getTypedRuleContext(TuaParser.ContinueContext,0)


        def getRuleIndex(self):
            return TuaParser.RULE_laststat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLaststat" ):
                listener.enterLaststat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLaststat" ):
                listener.exitLaststat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLaststat" ):
                return visitor.visitLaststat(self)
            else:
                return visitor.visitChildren(self)




    def laststat(self):

        localctx = TuaParser.LaststatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_laststat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.state = 291
                self.return_()
                pass
            elif token in [25]:
                self.state = 292
                self.break_()
                pass
            elif token in [26]:
                self.state = 293
                self.continue_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 297
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 296
                self.match(TuaParser.T__0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def explist(self):
            return self.getTypedRuleContext(TuaParser.ExplistContext,0)


        def getRuleIndex(self):
            return TuaParser.RULE_return

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn" ):
                listener.enterReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn" ):
                listener.exitReturn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn" ):
                return visitor.visitReturn(self)
            else:
                return visitor.visitChildren(self)




    def return_(self):

        localctx = TuaParser.ReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_return)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(TuaParser.T__23)
            self.state = 301
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 71916857757534208) != 0):
                self.state = 300
                self.explist()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TuaParser.RULE_break

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak" ):
                listener.enterBreak(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak" ):
                listener.exitBreak(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak" ):
                return visitor.visitBreak(self)
            else:
                return visitor.visitChildren(self)




    def break_(self):

        localctx = TuaParser.BreakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(TuaParser.T__24)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TuaParser.RULE_continue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinue" ):
                listener.enterContinue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinue" ):
                listener.exitContinue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue" ):
                return visitor.visitContinue(self)
            else:
                return visitor.visitChildren(self)




    def continue_(self):

        localctx = TuaParser.ContinueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(TuaParser.T__25)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypednamelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nametype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TuaParser.NametypeContext)
            else:
                return self.getTypedRuleContext(TuaParser.NametypeContext,i)


        def getRuleIndex(self):
            return TuaParser.RULE_typednamelist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypednamelist" ):
                listener.enterTypednamelist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypednamelist" ):
                listener.exitTypednamelist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypednamelist" ):
                return visitor.visitTypednamelist(self)
            else:
                return visitor.visitChildren(self)




    def typednamelist(self):

        localctx = TuaParser.TypednamelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_typednamelist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.nametype()
            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 308
                self.match(TuaParser.T__7)
                self.state = 309
                self.nametype()
                self.state = 314
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctioncallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(TuaParser.NAME, 0)

        def explist(self):
            return self.getTypedRuleContext(TuaParser.ExplistContext,0)


        def getRuleIndex(self):
            return TuaParser.RULE_functioncall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctioncall" ):
                listener.enterFunctioncall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctioncall" ):
                listener.exitFunctioncall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctioncall" ):
                return visitor.visitFunctioncall(self)
            else:
                return visitor.visitChildren(self)




    def functioncall(self):

        localctx = TuaParser.FunctioncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_functioncall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(TuaParser.NAME)
            self.state = 316
            self.match(TuaParser.T__10)
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 71916857757534208) != 0):
                self.state = 317
                self.explist()


            self.state = 320
            self.match(TuaParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExplistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(TuaParser.ExpContext,i)


        def getRuleIndex(self):
            return TuaParser.RULE_explist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExplist" ):
                listener.enterExplist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExplist" ):
                listener.exitExplist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplist" ):
                return visitor.visitExplist(self)
            else:
                return visitor.visitChildren(self)




    def explist(self):

        localctx = TuaParser.ExplistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_explist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.exp(0)
            self.state = 327
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 323
                self.match(TuaParser.T__7)
                self.state = 324
                self.exp(0)
                self.state = 329
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableconstructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldlist(self):
            return self.getTypedRuleContext(TuaParser.FieldlistContext,0)


        def getRuleIndex(self):
            return TuaParser.RULE_tableconstructor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableconstructor" ):
                listener.enterTableconstructor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableconstructor" ):
                listener.exitTableconstructor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableconstructor" ):
                return visitor.visitTableconstructor(self)
            else:
                return visitor.visitChildren(self)




    def tableconstructor(self):

        localctx = TuaParser.TableconstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_tableconstructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(TuaParser.T__26)
            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 71916857757534240) != 0):
                self.state = 331
                self.fieldlist()


            self.state = 334
            self.match(TuaParser.T__27)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TuaParser.FieldContext)
            else:
                return self.getTypedRuleContext(TuaParser.FieldContext,i)


        def getRuleIndex(self):
            return TuaParser.RULE_fieldlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldlist" ):
                listener.enterFieldlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldlist" ):
                listener.exitFieldlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldlist" ):
                return visitor.visitFieldlist(self)
            else:
                return visitor.visitChildren(self)




    def fieldlist(self):

        localctx = TuaParser.FieldlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_fieldlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.field()
            self.state = 341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 337
                self.match(TuaParser.T__7)
                self.state = 338
                self.field()
                self.state = 343
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(TuaParser.ExpContext,i)


        def type_(self):
            return self.getTypedRuleContext(TuaParser.TypeContext,0)


        def nametype(self):
            return self.getTypedRuleContext(TuaParser.NametypeContext,0)


        def getRuleIndex(self):
            return TuaParser.RULE_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField" ):
                listener.enterField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField" ):
                listener.exitField(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField" ):
                return visitor.visitField(self)
            else:
                return visitor.visitChildren(self)




    def field(self):

        localctx = TuaParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_field)
        try:
            self.state = 357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                self.match(TuaParser.T__4)
                self.state = 345
                self.exp(0)
                self.state = 346
                self.match(TuaParser.T__5)
                self.state = 347
                self.match(TuaParser.T__2)
                self.state = 348
                self.type_()
                self.state = 349
                self.match(TuaParser.T__1)
                self.state = 350
                self.exp(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
                self.nametype()
                self.state = 353
                self.match(TuaParser.T__1)
                self.state = 354
                self.exp(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 356
                self.exp(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinopAddSubContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TuaParser.RULE_binopAddSub

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinopAddSub" ):
                listener.enterBinopAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinopAddSub" ):
                listener.exitBinopAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinopAddSub" ):
                return visitor.visitBinopAddSub(self)
            else:
                return visitor.visitChildren(self)




    def binopAddSub(self):

        localctx = TuaParser.BinopAddSubContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_binopAddSub)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            _la = self._input.LA(1)
            if not(_la==29 or _la==30):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinopMulDivModContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TuaParser.RULE_binopMulDivMod

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinopMulDivMod" ):
                listener.enterBinopMulDivMod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinopMulDivMod" ):
                listener.exitBinopMulDivMod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinopMulDivMod" ):
                return visitor.visitBinopMulDivMod(self)
            else:
                return visitor.visitChildren(self)




    def binopMulDivMod(self):

        localctx = TuaParser.BinopMulDivModContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_binopMulDivMod)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32212254720) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinopComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TuaParser.RULE_binopComparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinopComparison" ):
                listener.enterBinopComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinopComparison" ):
                listener.exitBinopComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinopComparison" ):
                return visitor.visitBinopComparison(self)
            else:
                return visitor.visitChildren(self)




    def binopComparison(self):

        localctx = TuaParser.BinopComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_binopComparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2164663517184) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinopConcatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TuaParser.RULE_binopConcat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinopConcat" ):
                listener.enterBinopConcat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinopConcat" ):
                listener.exitBinopConcat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinopConcat" ):
                return visitor.visitBinopConcat(self)
            else:
                return visitor.visitChildren(self)




    def binopConcat(self):

        localctx = TuaParser.BinopConcatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_binopConcat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(TuaParser.T__40)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinopAndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TuaParser.RULE_binopAnd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinopAnd" ):
                listener.enterBinopAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinopAnd" ):
                listener.exitBinopAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinopAnd" ):
                return visitor.visitBinopAnd(self)
            else:
                return visitor.visitChildren(self)




    def binopAnd(self):

        localctx = TuaParser.BinopAndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_binopAnd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            _la = self._input.LA(1)
            if not(_la==42 or _la==43):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinopOrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TuaParser.RULE_binopOr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinopOr" ):
                listener.enterBinopOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinopOr" ):
                listener.exitBinopOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinopOr" ):
                return visitor.visitBinopOr(self)
            else:
                return visitor.visitChildren(self)




    def binopOr(self):

        localctx = TuaParser.BinopOrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_binopOr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            _la = self._input.LA(1)
            if not(_la==44 or _la==45):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinopPowerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TuaParser.RULE_binopPower

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinopPower" ):
                listener.enterBinopPower(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinopPower" ):
                listener.exitBinopPower(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinopPower" ):
                return visitor.visitBinopPower(self)
            else:
                return visitor.visitChildren(self)




    def binopPower(self):

        localctx = TuaParser.BinopPowerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_binopPower)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.match(TuaParser.T__45)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TuaParser.RULE_unop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnop" ):
                listener.enterUnop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnop" ):
                listener.exitUnop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnop" ):
                return visitor.visitUnop(self)
            else:
                return visitor.visitChildren(self)




    def unop(self):

        localctx = TuaParser.UnopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_unop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            _la = self._input.LA(1)
            if not(_la==30 or _la==47):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLEQUOTESTRING(self):
            return self.getToken(TuaParser.DOUBLEQUOTESTRING, 0)

        def SINGLEQUOTESTRING(self):
            return self.getToken(TuaParser.SINGLEQUOTESTRING, 0)

        def getRuleIndex(self):
            return TuaParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = TuaParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            _la = self._input.LA(1)
            if not(_la==54 or _la==55):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TuaParser.INT, 0)

        def FLOAT(self):
            return self.getToken(TuaParser.FLOAT, 0)

        def getRuleIndex(self):
            return TuaParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = TuaParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            _la = self._input.LA(1)
            if not(_la==52 or _la==53):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(TuaParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(TuaParser.FALSE, 0)

        def getRuleIndex(self):
            return TuaParser.RULE_bool

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool" ):
                return visitor.visitBool(self)
            else:
                return visitor.visitChildren(self)




    def bool_(self):

        localctx = TuaParser.BoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_bool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            _la = self._input.LA(1)
            if not(_la==48 or _la==49):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.exp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




