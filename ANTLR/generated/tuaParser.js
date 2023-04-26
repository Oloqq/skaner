// Generated from grammars/tua.g4 by ANTLR 4.12.0
// jshint ignore: start
import antlr4 from 'antlr4';
import tuaListener from './tuaListener.js';
import tuaVisitor from './tuaVisitor.js';

const serializedATN = [4,1,56,343,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,
4,2,5,7,5,2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,
2,13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,
20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,2,27,
7,27,2,28,7,28,2,29,7,29,1,0,1,0,1,0,1,1,1,1,3,1,66,8,1,5,1,68,8,1,10,1,
12,1,71,9,1,1,1,3,1,74,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,104,
8,2,10,2,12,2,107,9,2,1,2,1,2,3,2,111,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
2,1,2,1,2,3,2,123,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
2,1,2,1,2,1,2,1,2,3,2,142,8,2,1,3,1,3,3,3,146,8,3,1,4,1,4,1,4,1,4,1,5,1,
5,1,5,1,5,1,5,3,5,157,8,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,4,7,169,
8,7,11,7,12,7,170,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,3,9,183,8,9,3,
9,185,8,9,1,10,1,10,1,10,1,10,1,10,1,10,4,10,193,8,10,11,10,12,10,194,1,
11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
1,11,1,11,1,11,3,11,215,8,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
11,1,11,1,11,1,11,1,11,5,11,245,8,11,10,11,12,11,248,9,11,1,12,1,12,3,12,
252,8,12,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,3,13,262,8,13,1,13,1,13,
3,13,266,8,13,1,13,3,13,269,8,13,1,14,1,14,1,14,5,14,274,8,14,10,14,12,14,
277,9,14,1,15,1,15,1,15,3,15,282,8,15,1,15,1,15,1,16,1,16,1,16,5,16,289,
8,16,10,16,12,16,292,9,16,1,17,1,17,3,17,296,8,17,1,17,1,17,1,18,1,18,1,
18,5,18,303,8,18,10,18,12,18,306,9,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
1,19,1,19,1,19,1,19,1,19,1,19,3,19,321,8,19,1,20,1,20,1,21,1,21,1,22,1,22,
1,23,1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,27,1,27,1,28,1,28,1,29,1,29,1,
29,0,1,22,30,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
44,46,48,50,52,54,56,58,0,8,1,0,29,30,1,0,31,34,1,0,35,40,1,0,42,43,1,0,
44,45,2,0,30,30,47,47,1,0,54,55,1,0,52,53,364,0,60,1,0,0,0,2,69,1,0,0,0,
4,141,1,0,0,0,6,143,1,0,0,0,8,147,1,0,0,0,10,156,1,0,0,0,12,158,1,0,0,0,
14,163,1,0,0,0,16,174,1,0,0,0,18,184,1,0,0,0,20,192,1,0,0,0,22,214,1,0,0,
0,24,249,1,0,0,0,26,265,1,0,0,0,28,270,1,0,0,0,30,278,1,0,0,0,32,285,1,0,
0,0,34,293,1,0,0,0,36,299,1,0,0,0,38,320,1,0,0,0,40,322,1,0,0,0,42,324,1,
0,0,0,44,326,1,0,0,0,46,328,1,0,0,0,48,330,1,0,0,0,50,332,1,0,0,0,52,334,
1,0,0,0,54,336,1,0,0,0,56,338,1,0,0,0,58,340,1,0,0,0,60,61,3,2,1,0,61,62,
5,0,0,1,62,1,1,0,0,0,63,65,3,4,2,0,64,66,5,1,0,0,65,64,1,0,0,0,65,66,1,0,
0,0,66,68,1,0,0,0,67,63,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,
0,70,73,1,0,0,0,71,69,1,0,0,0,72,74,3,26,13,0,73,72,1,0,0,0,73,74,1,0,0,
0,74,3,1,0,0,0,75,76,3,8,4,0,76,77,5,2,0,0,77,78,3,22,11,0,78,142,1,0,0,
0,79,80,3,6,3,0,80,81,5,2,0,0,81,82,3,22,11,0,82,142,1,0,0,0,83,142,3,30,
15,0,84,85,5,3,0,0,85,86,3,2,1,0,86,87,5,4,0,0,87,142,1,0,0,0,88,89,5,5,
0,0,89,90,3,22,11,0,90,91,5,3,0,0,91,92,3,2,1,0,92,93,5,4,0,0,93,142,1,0,
0,0,94,95,5,6,0,0,95,96,3,22,11,0,96,97,5,7,0,0,97,105,3,2,1,0,98,99,5,8,
0,0,99,100,3,22,11,0,100,101,5,7,0,0,101,102,3,2,1,0,102,104,1,0,0,0,103,
98,1,0,0,0,104,107,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,110,1,0,0,
0,107,105,1,0,0,0,108,109,5,9,0,0,109,111,3,2,1,0,110,108,1,0,0,0,110,111,
1,0,0,0,111,112,1,0,0,0,112,113,5,4,0,0,113,142,1,0,0,0,114,115,5,10,0,0,
115,116,5,48,0,0,116,117,5,2,0,0,117,118,3,22,11,0,118,119,5,11,0,0,119,
122,3,22,11,0,120,121,5,11,0,0,121,123,3,22,11,0,122,120,1,0,0,0,122,123,
1,0,0,0,123,124,1,0,0,0,124,125,5,3,0,0,125,126,3,2,1,0,126,127,5,4,0,0,
127,142,1,0,0,0,128,129,5,10,0,0,129,130,5,48,0,0,130,131,5,11,0,0,131,132,
5,48,0,0,132,133,5,12,0,0,133,134,3,30,15,0,134,135,5,3,0,0,135,136,3,2,
1,0,136,137,5,4,0,0,137,142,1,0,0,0,138,139,5,13,0,0,139,140,5,48,0,0,140,
142,3,24,12,0,141,75,1,0,0,0,141,79,1,0,0,0,141,83,1,0,0,0,141,84,1,0,0,
0,141,88,1,0,0,0,141,94,1,0,0,0,141,114,1,0,0,0,141,128,1,0,0,0,141,138,
1,0,0,0,142,5,1,0,0,0,143,145,5,48,0,0,144,146,3,20,10,0,145,144,1,0,0,0,
145,146,1,0,0,0,146,7,1,0,0,0,147,148,5,48,0,0,148,149,5,14,0,0,149,150,
3,10,5,0,150,9,1,0,0,0,151,157,5,48,0,0,152,157,5,51,0,0,153,157,3,16,8,
0,154,157,3,14,7,0,155,157,3,12,6,0,156,151,1,0,0,0,156,152,1,0,0,0,156,
153,1,0,0,0,156,154,1,0,0,0,156,155,1,0,0,0,157,11,1,0,0,0,158,159,5,15,
0,0,159,160,5,16,0,0,160,161,3,10,5,0,161,162,5,17,0,0,162,13,1,0,0,0,163,
164,5,18,0,0,164,165,5,16,0,0,165,168,3,10,5,0,166,167,5,11,0,0,167,169,
3,10,5,0,168,166,1,0,0,0,169,170,1,0,0,0,170,168,1,0,0,0,170,171,1,0,0,0,
171,172,1,0,0,0,172,173,5,17,0,0,173,15,1,0,0,0,174,175,5,19,0,0,175,176,
5,16,0,0,176,177,3,10,5,0,177,178,5,17,0,0,178,17,1,0,0,0,179,185,3,6,3,
0,180,182,3,30,15,0,181,183,3,20,10,0,182,181,1,0,0,0,182,183,1,0,0,0,183,
185,1,0,0,0,184,179,1,0,0,0,184,180,1,0,0,0,185,19,1,0,0,0,186,187,5,16,
0,0,187,188,3,22,11,0,188,189,5,17,0,0,189,193,1,0,0,0,190,191,5,20,0,0,
191,193,5,48,0,0,192,186,1,0,0,0,192,190,1,0,0,0,193,194,1,0,0,0,194,192,
1,0,0,0,194,195,1,0,0,0,195,21,1,0,0,0,196,197,6,11,-1,0,197,198,5,21,0,
0,198,199,3,22,11,0,199,200,5,22,0,0,200,215,1,0,0,0,201,215,3,58,29,0,202,
215,3,56,28,0,203,215,5,50,0,0,204,215,5,49,0,0,205,215,5,51,0,0,206,215,
3,18,9,0,207,208,3,54,27,0,208,209,3,22,11,9,209,215,1,0,0,0,210,211,3,54,
27,0,211,212,3,22,11,2,212,215,1,0,0,0,213,215,3,34,17,0,214,196,1,0,0,0,
214,201,1,0,0,0,214,202,1,0,0,0,214,203,1,0,0,0,214,204,1,0,0,0,214,205,
1,0,0,0,214,206,1,0,0,0,214,207,1,0,0,0,214,210,1,0,0,0,214,213,1,0,0,0,
215,246,1,0,0,0,216,217,10,10,0,0,217,218,3,52,26,0,218,219,3,22,11,10,219,
245,1,0,0,0,220,221,10,8,0,0,221,222,3,42,21,0,222,223,3,22,11,9,223,245,
1,0,0,0,224,225,10,7,0,0,225,226,3,40,20,0,226,227,3,22,11,8,227,245,1,0,
0,0,228,229,10,6,0,0,229,230,3,46,23,0,230,231,3,22,11,6,231,245,1,0,0,0,
232,233,10,5,0,0,233,234,3,44,22,0,234,235,3,22,11,6,235,245,1,0,0,0,236,
237,10,4,0,0,237,238,3,48,24,0,238,239,3,22,11,5,239,245,1,0,0,0,240,241,
10,3,0,0,241,242,3,50,25,0,242,243,3,22,11,4,243,245,1,0,0,0,244,216,1,0,
0,0,244,220,1,0,0,0,244,224,1,0,0,0,244,228,1,0,0,0,244,232,1,0,0,0,244,
236,1,0,0,0,244,240,1,0,0,0,245,248,1,0,0,0,246,244,1,0,0,0,246,247,1,0,
0,0,247,23,1,0,0,0,248,246,1,0,0,0,249,251,5,21,0,0,250,252,3,28,14,0,251,
250,1,0,0,0,251,252,1,0,0,0,252,253,1,0,0,0,253,254,5,22,0,0,254,255,5,23,
0,0,255,256,3,10,5,0,256,257,3,2,1,0,257,258,5,4,0,0,258,25,1,0,0,0,259,
261,5,24,0,0,260,262,3,32,16,0,261,260,1,0,0,0,261,262,1,0,0,0,262,266,1,
0,0,0,263,266,5,25,0,0,264,266,5,26,0,0,265,259,1,0,0,0,265,263,1,0,0,0,
265,264,1,0,0,0,266,268,1,0,0,0,267,269,5,1,0,0,268,267,1,0,0,0,268,269,
1,0,0,0,269,27,1,0,0,0,270,275,3,8,4,0,271,272,5,11,0,0,272,274,3,8,4,0,
273,271,1,0,0,0,274,277,1,0,0,0,275,273,1,0,0,0,275,276,1,0,0,0,276,29,1,
0,0,0,277,275,1,0,0,0,278,279,5,48,0,0,279,281,5,21,0,0,280,282,3,32,16,
0,281,280,1,0,0,0,281,282,1,0,0,0,282,283,1,0,0,0,283,284,5,22,0,0,284,31,
1,0,0,0,285,290,3,22,11,0,286,287,5,11,0,0,287,289,3,22,11,0,288,286,1,0,
0,0,289,292,1,0,0,0,290,288,1,0,0,0,290,291,1,0,0,0,291,33,1,0,0,0,292,290,
1,0,0,0,293,295,5,27,0,0,294,296,3,36,18,0,295,294,1,0,0,0,295,296,1,0,0,
0,296,297,1,0,0,0,297,298,5,28,0,0,298,35,1,0,0,0,299,304,3,38,19,0,300,
301,5,11,0,0,301,303,3,38,19,0,302,300,1,0,0,0,303,306,1,0,0,0,304,302,1,
0,0,0,304,305,1,0,0,0,305,37,1,0,0,0,306,304,1,0,0,0,307,308,5,16,0,0,308,
309,3,22,11,0,309,310,5,17,0,0,310,311,5,14,0,0,311,312,3,10,5,0,312,313,
5,2,0,0,313,314,3,22,11,0,314,321,1,0,0,0,315,316,3,8,4,0,316,317,5,2,0,
0,317,318,3,22,11,0,318,321,1,0,0,0,319,321,3,22,11,0,320,307,1,0,0,0,320,
315,1,0,0,0,320,319,1,0,0,0,321,39,1,0,0,0,322,323,7,0,0,0,323,41,1,0,0,
0,324,325,7,1,0,0,325,43,1,0,0,0,326,327,7,2,0,0,327,45,1,0,0,0,328,329,
5,41,0,0,329,47,1,0,0,0,330,331,7,3,0,0,331,49,1,0,0,0,332,333,7,4,0,0,333,
51,1,0,0,0,334,335,5,46,0,0,335,53,1,0,0,0,336,337,7,5,0,0,337,55,1,0,0,
0,338,339,7,6,0,0,339,57,1,0,0,0,340,341,7,7,0,0,341,59,1,0,0,0,27,65,69,
73,105,110,122,141,145,156,170,182,184,192,194,214,244,246,251,261,265,268,
275,281,290,295,304,320];


const atn = new antlr4.atn.ATNDeserializer().deserialize(serializedATN);

const decisionsToDFA = atn.decisionToState.map( (ds, index) => new antlr4.dfa.DFA(ds, index) );

const sharedContextCache = new antlr4.atn.PredictionContextCache();

export default class tuaParser extends antlr4.Parser {

    static grammarFileName = "tua.g4";
    static literalNames = [ null, "';'", "'='", "'do'", "'end'", "'while'", 
                            "'if'", "'then'", "'elseif'", "'else'", "'for'", 
                            "','", "'in'", "'function'", "':'", "'Table'", 
                            "'['", "']'", "'Union'", "'List'", "'.'", "'('", 
                            "')'", "'->'", "'return'", "'break'", "'continue'", 
                            "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                            "'//'", "'=='", "'~='", "'<='", "'>='", "'<'", 
                            "'>'", "'..'", "'and'", "'&'", "'or'", "'|'", 
                            "'^'", "'not'", null, "'false'", "'true'", "'nil'" ];
    static symbolicNames = [ null, null, null, null, null, null, null, null, 
                             null, null, null, null, null, null, null, null, 
                             null, null, null, null, null, null, null, null, 
                             null, null, null, null, null, null, null, null, 
                             null, null, null, null, null, null, null, null, 
                             null, null, null, null, null, null, null, null, 
                             "NAME", "FALSE", "TRUE", "NIL", "INT", "FLOAT", 
                             "DOUBLEQUOTESTRING", "SINGLEQUOTESTRING", "WHITESPACE" ];
    static ruleNames = [ "program", "block", "stat", "var", "nametype", 
                         "type", "tableType", "unionType", "listType", "prefix", 
                         "suffix", "exp", "functionbody", "laststat", "typednamelist", 
                         "functioncall", "explist", "tableconstructor", 
                         "fieldlist", "field", "binopAddSub", "binopMulDivMod", 
                         "binopComparison", "binopConcat", "binopAnd", "binopOr", 
                         "binopPower", "unop", "string", "number" ];

    constructor(input) {
        super(input);
        this._interp = new antlr4.atn.ParserATNSimulator(this, atn, decisionsToDFA, sharedContextCache);
        this.ruleNames = tuaParser.ruleNames;
        this.literalNames = tuaParser.literalNames;
        this.symbolicNames = tuaParser.symbolicNames;
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
    			return this.precpred(this._ctx, 10);
    		case 1:
    			return this.precpred(this._ctx, 8);
    		case 2:
    			return this.precpred(this._ctx, 7);
    		case 3:
    			return this.precpred(this._ctx, 6);
    		case 4:
    			return this.precpred(this._ctx, 5);
    		case 5:
    			return this.precpred(this._ctx, 4);
    		case 6:
    			return this.precpred(this._ctx, 3);
    		default:
    			throw "No predicate with index:" + predIndex;
    	}
    };




	program() {
	    let localctx = new ProgramContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 0, tuaParser.RULE_program);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 60;
	        this.block();
	        this.state = 61;
	        this.match(tuaParser.EOF);
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
	    this.enterRule(localctx, 2, tuaParser.RULE_block);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 69;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        while((((_la) & ~0x1f) === 0 && ((1 << _la) & 9320) !== 0) || _la===48) {
	            this.state = 63;
	            this.stat();
	            this.state = 65;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            if(_la===1) {
	                this.state = 64;
	                this.match(tuaParser.T__0);
	            }

	            this.state = 71;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        }
	        this.state = 73;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        if((((_la) & ~0x1f) === 0 && ((1 << _la) & 117440512) !== 0)) {
	            this.state = 72;
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
	    this.enterRule(localctx, 4, tuaParser.RULE_stat);
	    var _la = 0;
	    try {
	        this.state = 141;
	        this._errHandler.sync(this);
	        var la_ = this._interp.adaptivePredict(this._input,6,this._ctx);
	        switch(la_) {
	        case 1:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 75;
	            this.nametype();
	            this.state = 76;
	            this.match(tuaParser.T__1);
	            this.state = 77;
	            this.exp(0);
	            break;

	        case 2:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 79;
	            this.var_();
	            this.state = 80;
	            this.match(tuaParser.T__1);
	            this.state = 81;
	            this.exp(0);
	            break;

	        case 3:
	            this.enterOuterAlt(localctx, 3);
	            this.state = 83;
	            this.functioncall();
	            break;

	        case 4:
	            this.enterOuterAlt(localctx, 4);
	            this.state = 84;
	            this.match(tuaParser.T__2);
	            this.state = 85;
	            this.block();
	            this.state = 86;
	            this.match(tuaParser.T__3);
	            break;

	        case 5:
	            this.enterOuterAlt(localctx, 5);
	            this.state = 88;
	            this.match(tuaParser.T__4);
	            this.state = 89;
	            this.exp(0);
	            this.state = 90;
	            this.match(tuaParser.T__2);
	            this.state = 91;
	            this.block();
	            this.state = 92;
	            this.match(tuaParser.T__3);
	            break;

	        case 6:
	            this.enterOuterAlt(localctx, 6);
	            this.state = 94;
	            this.match(tuaParser.T__5);
	            this.state = 95;
	            this.exp(0);
	            this.state = 96;
	            this.match(tuaParser.T__6);
	            this.state = 97;
	            this.block();
	            this.state = 105;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            while(_la===8) {
	                this.state = 98;
	                this.match(tuaParser.T__7);
	                this.state = 99;
	                this.exp(0);
	                this.state = 100;
	                this.match(tuaParser.T__6);
	                this.state = 101;
	                this.block();
	                this.state = 107;
	                this._errHandler.sync(this);
	                _la = this._input.LA(1);
	            }
	            this.state = 110;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            if(_la===9) {
	                this.state = 108;
	                this.match(tuaParser.T__8);
	                this.state = 109;
	                this.block();
	            }

	            this.state = 112;
	            this.match(tuaParser.T__3);
	            break;

	        case 7:
	            this.enterOuterAlt(localctx, 7);
	            this.state = 114;
	            this.match(tuaParser.T__9);
	            this.state = 115;
	            this.match(tuaParser.NAME);
	            this.state = 116;
	            this.match(tuaParser.T__1);
	            this.state = 117;
	            this.exp(0);
	            this.state = 118;
	            this.match(tuaParser.T__10);
	            this.state = 119;
	            this.exp(0);
	            this.state = 122;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            if(_la===11) {
	                this.state = 120;
	                this.match(tuaParser.T__10);
	                this.state = 121;
	                this.exp(0);
	            }

	            this.state = 124;
	            this.match(tuaParser.T__2);
	            this.state = 125;
	            this.block();
	            this.state = 126;
	            this.match(tuaParser.T__3);
	            break;

	        case 8:
	            this.enterOuterAlt(localctx, 8);
	            this.state = 128;
	            this.match(tuaParser.T__9);
	            this.state = 129;
	            this.match(tuaParser.NAME);
	            this.state = 130;
	            this.match(tuaParser.T__10);
	            this.state = 131;
	            this.match(tuaParser.NAME);
	            this.state = 132;
	            this.match(tuaParser.T__11);
	            this.state = 133;
	            this.functioncall();
	            this.state = 134;
	            this.match(tuaParser.T__2);
	            this.state = 135;
	            this.block();
	            this.state = 136;
	            this.match(tuaParser.T__3);
	            break;

	        case 9:
	            this.enterOuterAlt(localctx, 9);
	            this.state = 138;
	            this.match(tuaParser.T__12);
	            this.state = 139;
	            this.match(tuaParser.NAME);
	            this.state = 140;
	            this.functionbody();
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
	    this.enterRule(localctx, 6, tuaParser.RULE_var);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 143;
	        this.match(tuaParser.NAME);
	        this.state = 145;
	        this._errHandler.sync(this);
	        var la_ = this._interp.adaptivePredict(this._input,7,this._ctx);
	        if(la_===1) {
	            this.state = 144;
	            this.suffix();

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



	nametype() {
	    let localctx = new NametypeContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 8, tuaParser.RULE_nametype);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 147;
	        this.match(tuaParser.NAME);
	        this.state = 148;
	        this.match(tuaParser.T__13);
	        this.state = 149;
	        this.type();
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



	type() {
	    let localctx = new TypeContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 10, tuaParser.RULE_type);
	    try {
	        this.state = 156;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case 48:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 151;
	            this.match(tuaParser.NAME);
	            break;
	        case 51:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 152;
	            this.match(tuaParser.NIL);
	            break;
	        case 19:
	            this.enterOuterAlt(localctx, 3);
	            this.state = 153;
	            this.listType();
	            break;
	        case 18:
	            this.enterOuterAlt(localctx, 4);
	            this.state = 154;
	            this.unionType();
	            break;
	        case 15:
	            this.enterOuterAlt(localctx, 5);
	            this.state = 155;
	            this.tableType();
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



	tableType() {
	    let localctx = new TableTypeContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 12, tuaParser.RULE_tableType);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 158;
	        this.match(tuaParser.T__14);
	        this.state = 159;
	        this.match(tuaParser.T__15);
	        this.state = 160;
	        this.type();
	        this.state = 161;
	        this.match(tuaParser.T__16);
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



	unionType() {
	    let localctx = new UnionTypeContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 14, tuaParser.RULE_unionType);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 163;
	        this.match(tuaParser.T__17);
	        this.state = 164;
	        this.match(tuaParser.T__15);
	        this.state = 165;
	        this.type();
	        this.state = 168; 
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        do {
	            this.state = 166;
	            this.match(tuaParser.T__10);
	            this.state = 167;
	            this.type();
	            this.state = 170; 
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        } while(_la===11);
	        this.state = 172;
	        this.match(tuaParser.T__16);
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



	listType() {
	    let localctx = new ListTypeContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 16, tuaParser.RULE_listType);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 174;
	        this.match(tuaParser.T__18);
	        this.state = 175;
	        this.match(tuaParser.T__15);
	        this.state = 176;
	        this.type();
	        this.state = 177;
	        this.match(tuaParser.T__16);
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



	prefix() {
	    let localctx = new PrefixContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 18, tuaParser.RULE_prefix);
	    try {
	        this.state = 184;
	        this._errHandler.sync(this);
	        var la_ = this._interp.adaptivePredict(this._input,11,this._ctx);
	        switch(la_) {
	        case 1:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 179;
	            this.var_();
	            break;

	        case 2:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 180;
	            this.functioncall();
	            this.state = 182;
	            this._errHandler.sync(this);
	            var la_ = this._interp.adaptivePredict(this._input,10,this._ctx);
	            if(la_===1) {
	                this.state = 181;
	                this.suffix();

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



	suffix() {
	    let localctx = new SuffixContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 20, tuaParser.RULE_suffix);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 192; 
	        this._errHandler.sync(this);
	        var _alt = 1;
	        do {
	        	switch (_alt) {
	        	case 1:
	        		this.state = 192;
	        		this._errHandler.sync(this);
	        		switch(this._input.LA(1)) {
	        		case 16:
	        		    this.state = 186;
	        		    this.match(tuaParser.T__15);
	        		    this.state = 187;
	        		    this.exp(0);
	        		    this.state = 188;
	        		    this.match(tuaParser.T__16);
	        		    break;
	        		case 20:
	        		    this.state = 190;
	        		    this.match(tuaParser.T__19);
	        		    this.state = 191;
	        		    this.match(tuaParser.NAME);
	        		    break;
	        		default:
	        		    throw new antlr4.error.NoViableAltException(this);
	        		}
	        		break;
	        	default:
	        		throw new antlr4.error.NoViableAltException(this);
	        	}
	        	this.state = 194; 
	        	this._errHandler.sync(this);
	        	_alt = this._interp.adaptivePredict(this._input,13, this._ctx);
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


	exp(_p) {
		if(_p===undefined) {
		    _p = 0;
		}
	    const _parentctx = this._ctx;
	    const _parentState = this.state;
	    let localctx = new ExpContext(this, this._ctx, _parentState);
	    let _prevctx = localctx;
	    const _startState = 22;
	    this.enterRecursionRule(localctx, 22, tuaParser.RULE_exp, _p);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 214;
	        this._errHandler.sync(this);
	        var la_ = this._interp.adaptivePredict(this._input,14,this._ctx);
	        switch(la_) {
	        case 1:
	            this.state = 197;
	            this.match(tuaParser.T__20);
	            this.state = 198;
	            this.exp(0);
	            this.state = 199;
	            this.match(tuaParser.T__21);
	            break;

	        case 2:
	            this.state = 201;
	            this.number();
	            break;

	        case 3:
	            this.state = 202;
	            this.string();
	            break;

	        case 4:
	            this.state = 203;
	            this.match(tuaParser.TRUE);
	            break;

	        case 5:
	            this.state = 204;
	            this.match(tuaParser.FALSE);
	            break;

	        case 6:
	            this.state = 205;
	            this.match(tuaParser.NIL);
	            break;

	        case 7:
	            this.state = 206;
	            this.prefix();
	            break;

	        case 8:
	            this.state = 207;
	            this.unop();
	            this.state = 208;
	            this.exp(9);
	            break;

	        case 9:
	            this.state = 210;
	            this.unop();
	            this.state = 211;
	            this.exp(2);
	            break;

	        case 10:
	            this.state = 213;
	            this.tableconstructor();
	            break;

	        }
	        this._ctx.stop = this._input.LT(-1);
	        this.state = 246;
	        this._errHandler.sync(this);
	        var _alt = this._interp.adaptivePredict(this._input,16,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                if(this._parseListeners!==null) {
	                    this.triggerExitRuleEvent();
	                }
	                _prevctx = localctx;
	                this.state = 244;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,15,this._ctx);
	                switch(la_) {
	                case 1:
	                    localctx = new ExpContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, tuaParser.RULE_exp);
	                    this.state = 216;
	                    if (!( this.precpred(this._ctx, 10))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 10)");
	                    }
	                    this.state = 217;
	                    this.binopPower();
	                    this.state = 218;
	                    this.exp(10);
	                    break;

	                case 2:
	                    localctx = new ExpContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, tuaParser.RULE_exp);
	                    this.state = 220;
	                    if (!( this.precpred(this._ctx, 8))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 8)");
	                    }
	                    this.state = 221;
	                    this.binopMulDivMod();
	                    this.state = 222;
	                    this.exp(9);
	                    break;

	                case 3:
	                    localctx = new ExpContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, tuaParser.RULE_exp);
	                    this.state = 224;
	                    if (!( this.precpred(this._ctx, 7))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 7)");
	                    }
	                    this.state = 225;
	                    this.binopAddSub();
	                    this.state = 226;
	                    this.exp(8);
	                    break;

	                case 4:
	                    localctx = new ExpContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, tuaParser.RULE_exp);
	                    this.state = 228;
	                    if (!( this.precpred(this._ctx, 6))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 6)");
	                    }
	                    this.state = 229;
	                    this.binopConcat();
	                    this.state = 230;
	                    this.exp(6);
	                    break;

	                case 5:
	                    localctx = new ExpContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, tuaParser.RULE_exp);
	                    this.state = 232;
	                    if (!( this.precpred(this._ctx, 5))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 5)");
	                    }
	                    this.state = 233;
	                    this.binopComparison();
	                    this.state = 234;
	                    this.exp(6);
	                    break;

	                case 6:
	                    localctx = new ExpContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, tuaParser.RULE_exp);
	                    this.state = 236;
	                    if (!( this.precpred(this._ctx, 4))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 4)");
	                    }
	                    this.state = 237;
	                    this.binopAnd();
	                    this.state = 238;
	                    this.exp(5);
	                    break;

	                case 7:
	                    localctx = new ExpContext(this, _parentctx, _parentState);
	                    this.pushNewRecursionContext(localctx, _startState, tuaParser.RULE_exp);
	                    this.state = 240;
	                    if (!( this.precpred(this._ctx, 3))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 3)");
	                    }
	                    this.state = 241;
	                    this.binopOr();
	                    this.state = 242;
	                    this.exp(4);
	                    break;

	                } 
	            }
	            this.state = 248;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,16,this._ctx);
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



	functionbody() {
	    let localctx = new FunctionbodyContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 24, tuaParser.RULE_functionbody);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 249;
	        this.match(tuaParser.T__20);
	        this.state = 251;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        if(_la===48) {
	            this.state = 250;
	            this.typednamelist();
	        }

	        this.state = 253;
	        this.match(tuaParser.T__21);
	        this.state = 254;
	        this.match(tuaParser.T__22);
	        this.state = 255;
	        this.type();
	        this.state = 256;
	        this.block();
	        this.state = 257;
	        this.match(tuaParser.T__3);
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
	    this.enterRule(localctx, 26, tuaParser.RULE_laststat);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 265;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case 24:
	            this.state = 259;
	            this.match(tuaParser.T__23);
	            this.state = 261;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            if((((_la) & ~0x1f) === 0 && ((1 << _la) & 1210056704) !== 0) || ((((_la - 47)) & ~0x1f) === 0 && ((1 << (_la - 47)) & 511) !== 0)) {
	                this.state = 260;
	                this.explist();
	            }

	            break;
	        case 25:
	            this.state = 263;
	            this.match(tuaParser.T__24);
	            break;
	        case 26:
	            this.state = 264;
	            this.match(tuaParser.T__25);
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	        this.state = 268;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        if(_la===1) {
	            this.state = 267;
	            this.match(tuaParser.T__0);
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



	typednamelist() {
	    let localctx = new TypednamelistContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 28, tuaParser.RULE_typednamelist);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 270;
	        this.nametype();
	        this.state = 275;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        while(_la===11) {
	            this.state = 271;
	            this.match(tuaParser.T__10);
	            this.state = 272;
	            this.nametype();
	            this.state = 277;
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



	functioncall() {
	    let localctx = new FunctioncallContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 30, tuaParser.RULE_functioncall);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 278;
	        this.match(tuaParser.NAME);
	        this.state = 279;
	        this.match(tuaParser.T__20);
	        this.state = 281;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        if((((_la) & ~0x1f) === 0 && ((1 << _la) & 1210056704) !== 0) || ((((_la - 47)) & ~0x1f) === 0 && ((1 << (_la - 47)) & 511) !== 0)) {
	            this.state = 280;
	            this.explist();
	        }

	        this.state = 283;
	        this.match(tuaParser.T__21);
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
	    this.enterRule(localctx, 32, tuaParser.RULE_explist);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 285;
	        this.exp(0);
	        this.state = 290;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        while(_la===11) {
	            this.state = 286;
	            this.match(tuaParser.T__10);
	            this.state = 287;
	            this.exp(0);
	            this.state = 292;
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



	tableconstructor() {
	    let localctx = new TableconstructorContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 34, tuaParser.RULE_tableconstructor);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 293;
	        this.match(tuaParser.T__26);
	        this.state = 295;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        if((((_la) & ~0x1f) === 0 && ((1 << _la) & 1210122240) !== 0) || ((((_la - 47)) & ~0x1f) === 0 && ((1 << (_la - 47)) & 511) !== 0)) {
	            this.state = 294;
	            this.fieldlist();
	        }

	        this.state = 297;
	        this.match(tuaParser.T__27);
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
	    this.enterRule(localctx, 36, tuaParser.RULE_fieldlist);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 299;
	        this.field();
	        this.state = 304;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        while(_la===11) {
	            this.state = 300;
	            this.match(tuaParser.T__10);
	            this.state = 301;
	            this.field();
	            this.state = 306;
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



	field() {
	    let localctx = new FieldContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 38, tuaParser.RULE_field);
	    try {
	        this.state = 320;
	        this._errHandler.sync(this);
	        var la_ = this._interp.adaptivePredict(this._input,26,this._ctx);
	        switch(la_) {
	        case 1:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 307;
	            this.match(tuaParser.T__15);
	            this.state = 308;
	            this.exp(0);
	            this.state = 309;
	            this.match(tuaParser.T__16);
	            this.state = 310;
	            this.match(tuaParser.T__13);
	            this.state = 311;
	            this.type();
	            this.state = 312;
	            this.match(tuaParser.T__1);
	            this.state = 313;
	            this.exp(0);
	            break;

	        case 2:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 315;
	            this.nametype();
	            this.state = 316;
	            this.match(tuaParser.T__1);
	            this.state = 317;
	            this.exp(0);
	            break;

	        case 3:
	            this.enterOuterAlt(localctx, 3);
	            this.state = 319;
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



	binopAddSub() {
	    let localctx = new BinopAddSubContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 40, tuaParser.RULE_binopAddSub);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 322;
	        _la = this._input.LA(1);
	        if(!(_la===29 || _la===30)) {
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



	binopMulDivMod() {
	    let localctx = new BinopMulDivModContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 42, tuaParser.RULE_binopMulDivMod);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 324;
	        _la = this._input.LA(1);
	        if(!(((((_la - 31)) & ~0x1f) === 0 && ((1 << (_la - 31)) & 15) !== 0))) {
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



	binopComparison() {
	    let localctx = new BinopComparisonContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 44, tuaParser.RULE_binopComparison);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 326;
	        _la = this._input.LA(1);
	        if(!(((((_la - 35)) & ~0x1f) === 0 && ((1 << (_la - 35)) & 63) !== 0))) {
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



	binopConcat() {
	    let localctx = new BinopConcatContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 46, tuaParser.RULE_binopConcat);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 328;
	        this.match(tuaParser.T__40);
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



	binopAnd() {
	    let localctx = new BinopAndContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 48, tuaParser.RULE_binopAnd);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 330;
	        _la = this._input.LA(1);
	        if(!(_la===42 || _la===43)) {
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



	binopOr() {
	    let localctx = new BinopOrContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 50, tuaParser.RULE_binopOr);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 332;
	        _la = this._input.LA(1);
	        if(!(_la===44 || _la===45)) {
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



	binopPower() {
	    let localctx = new BinopPowerContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 52, tuaParser.RULE_binopPower);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 334;
	        this.match(tuaParser.T__45);
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



	unop() {
	    let localctx = new UnopContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 54, tuaParser.RULE_unop);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 336;
	        _la = this._input.LA(1);
	        if(!(_la===30 || _la===47)) {
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
	    this.enterRule(localctx, 56, tuaParser.RULE_string);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 338;
	        _la = this._input.LA(1);
	        if(!(_la===54 || _la===55)) {
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



	number() {
	    let localctx = new NumberContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 58, tuaParser.RULE_number);
	    var _la = 0;
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 340;
	        _la = this._input.LA(1);
	        if(!(_la===52 || _la===53)) {
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

tuaParser.EOF = antlr4.Token.EOF;
tuaParser.T__0 = 1;
tuaParser.T__1 = 2;
tuaParser.T__2 = 3;
tuaParser.T__3 = 4;
tuaParser.T__4 = 5;
tuaParser.T__5 = 6;
tuaParser.T__6 = 7;
tuaParser.T__7 = 8;
tuaParser.T__8 = 9;
tuaParser.T__9 = 10;
tuaParser.T__10 = 11;
tuaParser.T__11 = 12;
tuaParser.T__12 = 13;
tuaParser.T__13 = 14;
tuaParser.T__14 = 15;
tuaParser.T__15 = 16;
tuaParser.T__16 = 17;
tuaParser.T__17 = 18;
tuaParser.T__18 = 19;
tuaParser.T__19 = 20;
tuaParser.T__20 = 21;
tuaParser.T__21 = 22;
tuaParser.T__22 = 23;
tuaParser.T__23 = 24;
tuaParser.T__24 = 25;
tuaParser.T__25 = 26;
tuaParser.T__26 = 27;
tuaParser.T__27 = 28;
tuaParser.T__28 = 29;
tuaParser.T__29 = 30;
tuaParser.T__30 = 31;
tuaParser.T__31 = 32;
tuaParser.T__32 = 33;
tuaParser.T__33 = 34;
tuaParser.T__34 = 35;
tuaParser.T__35 = 36;
tuaParser.T__36 = 37;
tuaParser.T__37 = 38;
tuaParser.T__38 = 39;
tuaParser.T__39 = 40;
tuaParser.T__40 = 41;
tuaParser.T__41 = 42;
tuaParser.T__42 = 43;
tuaParser.T__43 = 44;
tuaParser.T__44 = 45;
tuaParser.T__45 = 46;
tuaParser.T__46 = 47;
tuaParser.NAME = 48;
tuaParser.FALSE = 49;
tuaParser.TRUE = 50;
tuaParser.NIL = 51;
tuaParser.INT = 52;
tuaParser.FLOAT = 53;
tuaParser.DOUBLEQUOTESTRING = 54;
tuaParser.SINGLEQUOTESTRING = 55;
tuaParser.WHITESPACE = 56;

tuaParser.RULE_program = 0;
tuaParser.RULE_block = 1;
tuaParser.RULE_stat = 2;
tuaParser.RULE_var = 3;
tuaParser.RULE_nametype = 4;
tuaParser.RULE_type = 5;
tuaParser.RULE_tableType = 6;
tuaParser.RULE_unionType = 7;
tuaParser.RULE_listType = 8;
tuaParser.RULE_prefix = 9;
tuaParser.RULE_suffix = 10;
tuaParser.RULE_exp = 11;
tuaParser.RULE_functionbody = 12;
tuaParser.RULE_laststat = 13;
tuaParser.RULE_typednamelist = 14;
tuaParser.RULE_functioncall = 15;
tuaParser.RULE_explist = 16;
tuaParser.RULE_tableconstructor = 17;
tuaParser.RULE_fieldlist = 18;
tuaParser.RULE_field = 19;
tuaParser.RULE_binopAddSub = 20;
tuaParser.RULE_binopMulDivMod = 21;
tuaParser.RULE_binopComparison = 22;
tuaParser.RULE_binopConcat = 23;
tuaParser.RULE_binopAnd = 24;
tuaParser.RULE_binopOr = 25;
tuaParser.RULE_binopPower = 26;
tuaParser.RULE_unop = 27;
tuaParser.RULE_string = 28;
tuaParser.RULE_number = 29;

class ProgramContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = tuaParser.RULE_program;
    }

	block() {
	    return this.getTypedRuleContext(BlockContext,0);
	};

	EOF() {
	    return this.getToken(tuaParser.EOF, 0);
	};

	enterRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.enterProgram(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.exitProgram(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof tuaVisitor ) {
	        return visitor.visitProgram(this);
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
        this.ruleIndex = tuaParser.RULE_block;
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
	    if(listener instanceof tuaListener ) {
	        listener.enterBlock(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.exitBlock(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof tuaVisitor ) {
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
        this.ruleIndex = tuaParser.RULE_stat;
    }

	nametype() {
	    return this.getTypedRuleContext(NametypeContext,0);
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

	var_() {
	    return this.getTypedRuleContext(VarContext,0);
	};

	functioncall() {
	    return this.getTypedRuleContext(FunctioncallContext,0);
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

	NAME = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(tuaParser.NAME);
	    } else {
	        return this.getToken(tuaParser.NAME, i);
	    }
	};


	functionbody() {
	    return this.getTypedRuleContext(FunctionbodyContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.enterStat(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.exitStat(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof tuaVisitor ) {
	        return visitor.visitStat(this);
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
        this.ruleIndex = tuaParser.RULE_var;
    }

	NAME() {
	    return this.getToken(tuaParser.NAME, 0);
	};

	suffix() {
	    return this.getTypedRuleContext(SuffixContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.enterVar(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.exitVar(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof tuaVisitor ) {
	        return visitor.visitVar(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class NametypeContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = tuaParser.RULE_nametype;
    }

	NAME() {
	    return this.getToken(tuaParser.NAME, 0);
	};

	type() {
	    return this.getTypedRuleContext(TypeContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.enterNametype(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.exitNametype(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof tuaVisitor ) {
	        return visitor.visitNametype(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class TypeContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = tuaParser.RULE_type;
    }

	NAME() {
	    return this.getToken(tuaParser.NAME, 0);
	};

	NIL() {
	    return this.getToken(tuaParser.NIL, 0);
	};

	listType() {
	    return this.getTypedRuleContext(ListTypeContext,0);
	};

	unionType() {
	    return this.getTypedRuleContext(UnionTypeContext,0);
	};

	tableType() {
	    return this.getTypedRuleContext(TableTypeContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.enterType(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.exitType(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof tuaVisitor ) {
	        return visitor.visitType(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class TableTypeContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = tuaParser.RULE_tableType;
    }

	type() {
	    return this.getTypedRuleContext(TypeContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.enterTableType(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.exitTableType(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof tuaVisitor ) {
	        return visitor.visitTableType(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class UnionTypeContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = tuaParser.RULE_unionType;
    }

	type = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(TypeContext);
	    } else {
	        return this.getTypedRuleContext(TypeContext,i);
	    }
	};

	enterRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.enterUnionType(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.exitUnionType(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof tuaVisitor ) {
	        return visitor.visitUnionType(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class ListTypeContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = tuaParser.RULE_listType;
    }

	type() {
	    return this.getTypedRuleContext(TypeContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.enterListType(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.exitListType(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof tuaVisitor ) {
	        return visitor.visitListType(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class PrefixContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = tuaParser.RULE_prefix;
    }

	var_() {
	    return this.getTypedRuleContext(VarContext,0);
	};

	functioncall() {
	    return this.getTypedRuleContext(FunctioncallContext,0);
	};

	suffix() {
	    return this.getTypedRuleContext(SuffixContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.enterPrefix(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.exitPrefix(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof tuaVisitor ) {
	        return visitor.visitPrefix(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class SuffixContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = tuaParser.RULE_suffix;
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

	NAME = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(tuaParser.NAME);
	    } else {
	        return this.getToken(tuaParser.NAME, i);
	    }
	};


	enterRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.enterSuffix(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.exitSuffix(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof tuaVisitor ) {
	        return visitor.visitSuffix(this);
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
        this.ruleIndex = tuaParser.RULE_exp;
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

	number() {
	    return this.getTypedRuleContext(NumberContext,0);
	};

	string() {
	    return this.getTypedRuleContext(StringContext,0);
	};

	TRUE() {
	    return this.getToken(tuaParser.TRUE, 0);
	};

	FALSE() {
	    return this.getToken(tuaParser.FALSE, 0);
	};

	NIL() {
	    return this.getToken(tuaParser.NIL, 0);
	};

	prefix() {
	    return this.getTypedRuleContext(PrefixContext,0);
	};

	unop() {
	    return this.getTypedRuleContext(UnopContext,0);
	};

	tableconstructor() {
	    return this.getTypedRuleContext(TableconstructorContext,0);
	};

	binopPower() {
	    return this.getTypedRuleContext(BinopPowerContext,0);
	};

	binopMulDivMod() {
	    return this.getTypedRuleContext(BinopMulDivModContext,0);
	};

	binopAddSub() {
	    return this.getTypedRuleContext(BinopAddSubContext,0);
	};

	binopConcat() {
	    return this.getTypedRuleContext(BinopConcatContext,0);
	};

	binopComparison() {
	    return this.getTypedRuleContext(BinopComparisonContext,0);
	};

	binopAnd() {
	    return this.getTypedRuleContext(BinopAndContext,0);
	};

	binopOr() {
	    return this.getTypedRuleContext(BinopOrContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.enterExp(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.exitExp(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof tuaVisitor ) {
	        return visitor.visitExp(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class FunctionbodyContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = tuaParser.RULE_functionbody;
    }

	type() {
	    return this.getTypedRuleContext(TypeContext,0);
	};

	block() {
	    return this.getTypedRuleContext(BlockContext,0);
	};

	typednamelist() {
	    return this.getTypedRuleContext(TypednamelistContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.enterFunctionbody(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.exitFunctionbody(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof tuaVisitor ) {
	        return visitor.visitFunctionbody(this);
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
        this.ruleIndex = tuaParser.RULE_laststat;
    }

	explist() {
	    return this.getTypedRuleContext(ExplistContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.enterLaststat(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.exitLaststat(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof tuaVisitor ) {
	        return visitor.visitLaststat(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class TypednamelistContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = tuaParser.RULE_typednamelist;
    }

	nametype = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(NametypeContext);
	    } else {
	        return this.getTypedRuleContext(NametypeContext,i);
	    }
	};

	enterRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.enterTypednamelist(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.exitTypednamelist(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof tuaVisitor ) {
	        return visitor.visitTypednamelist(this);
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
        this.ruleIndex = tuaParser.RULE_functioncall;
    }

	NAME() {
	    return this.getToken(tuaParser.NAME, 0);
	};

	explist() {
	    return this.getTypedRuleContext(ExplistContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.enterFunctioncall(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.exitFunctioncall(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof tuaVisitor ) {
	        return visitor.visitFunctioncall(this);
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
        this.ruleIndex = tuaParser.RULE_explist;
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
	    if(listener instanceof tuaListener ) {
	        listener.enterExplist(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.exitExplist(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof tuaVisitor ) {
	        return visitor.visitExplist(this);
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
        this.ruleIndex = tuaParser.RULE_tableconstructor;
    }

	fieldlist() {
	    return this.getTypedRuleContext(FieldlistContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.enterTableconstructor(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.exitTableconstructor(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof tuaVisitor ) {
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
        this.ruleIndex = tuaParser.RULE_fieldlist;
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

	enterRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.enterFieldlist(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.exitFieldlist(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof tuaVisitor ) {
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
        this.ruleIndex = tuaParser.RULE_field;
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

	type() {
	    return this.getTypedRuleContext(TypeContext,0);
	};

	nametype() {
	    return this.getTypedRuleContext(NametypeContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.enterField(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.exitField(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof tuaVisitor ) {
	        return visitor.visitField(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class BinopAddSubContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = tuaParser.RULE_binopAddSub;
    }


	enterRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.enterBinopAddSub(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.exitBinopAddSub(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof tuaVisitor ) {
	        return visitor.visitBinopAddSub(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class BinopMulDivModContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = tuaParser.RULE_binopMulDivMod;
    }


	enterRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.enterBinopMulDivMod(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.exitBinopMulDivMod(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof tuaVisitor ) {
	        return visitor.visitBinopMulDivMod(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class BinopComparisonContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = tuaParser.RULE_binopComparison;
    }


	enterRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.enterBinopComparison(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.exitBinopComparison(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof tuaVisitor ) {
	        return visitor.visitBinopComparison(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class BinopConcatContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = tuaParser.RULE_binopConcat;
    }


	enterRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.enterBinopConcat(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.exitBinopConcat(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof tuaVisitor ) {
	        return visitor.visitBinopConcat(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class BinopAndContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = tuaParser.RULE_binopAnd;
    }


	enterRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.enterBinopAnd(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.exitBinopAnd(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof tuaVisitor ) {
	        return visitor.visitBinopAnd(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class BinopOrContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = tuaParser.RULE_binopOr;
    }


	enterRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.enterBinopOr(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.exitBinopOr(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof tuaVisitor ) {
	        return visitor.visitBinopOr(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class BinopPowerContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = tuaParser.RULE_binopPower;
    }


	enterRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.enterBinopPower(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.exitBinopPower(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof tuaVisitor ) {
	        return visitor.visitBinopPower(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class UnopContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = tuaParser.RULE_unop;
    }


	enterRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.enterUnop(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.exitUnop(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof tuaVisitor ) {
	        return visitor.visitUnop(this);
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
        this.ruleIndex = tuaParser.RULE_string;
    }

	DOUBLEQUOTESTRING() {
	    return this.getToken(tuaParser.DOUBLEQUOTESTRING, 0);
	};

	SINGLEQUOTESTRING() {
	    return this.getToken(tuaParser.SINGLEQUOTESTRING, 0);
	};

	enterRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.enterString(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.exitString(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof tuaVisitor ) {
	        return visitor.visitString(this);
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
        this.ruleIndex = tuaParser.RULE_number;
    }

	INT() {
	    return this.getToken(tuaParser.INT, 0);
	};

	FLOAT() {
	    return this.getToken(tuaParser.FLOAT, 0);
	};

	enterRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.enterNumber(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof tuaListener ) {
	        listener.exitNumber(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof tuaVisitor ) {
	        return visitor.visitNumber(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}




tuaParser.ProgramContext = ProgramContext; 
tuaParser.BlockContext = BlockContext; 
tuaParser.StatContext = StatContext; 
tuaParser.VarContext = VarContext; 
tuaParser.NametypeContext = NametypeContext; 
tuaParser.TypeContext = TypeContext; 
tuaParser.TableTypeContext = TableTypeContext; 
tuaParser.UnionTypeContext = UnionTypeContext; 
tuaParser.ListTypeContext = ListTypeContext; 
tuaParser.PrefixContext = PrefixContext; 
tuaParser.SuffixContext = SuffixContext; 
tuaParser.ExpContext = ExpContext; 
tuaParser.FunctionbodyContext = FunctionbodyContext; 
tuaParser.LaststatContext = LaststatContext; 
tuaParser.TypednamelistContext = TypednamelistContext; 
tuaParser.FunctioncallContext = FunctioncallContext; 
tuaParser.ExplistContext = ExplistContext; 
tuaParser.TableconstructorContext = TableconstructorContext; 
tuaParser.FieldlistContext = FieldlistContext; 
tuaParser.FieldContext = FieldContext; 
tuaParser.BinopAddSubContext = BinopAddSubContext; 
tuaParser.BinopMulDivModContext = BinopMulDivModContext; 
tuaParser.BinopComparisonContext = BinopComparisonContext; 
tuaParser.BinopConcatContext = BinopConcatContext; 
tuaParser.BinopAndContext = BinopAndContext; 
tuaParser.BinopOrContext = BinopOrContext; 
tuaParser.BinopPowerContext = BinopPowerContext; 
tuaParser.UnopContext = UnopContext; 
tuaParser.StringContext = StringContext; 
tuaParser.NumberContext = NumberContext; 
