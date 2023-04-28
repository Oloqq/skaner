// Generated from c:\Users\oleg0\Desktop\studia\tkik\boolang\rdsp.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class rdspParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, T__36=37, T__37=38, 
		T__38=39, T__39=40, T__40=41, T__41=42, T__42=43, T__43=44, T__44=45, 
		T__45=46, T__46=47, T__47=48, NAME=49, FALSE=50, TRUE=51, INT=52, FLOAT=53, 
		DOUBLEQUOTESTRING=54, SINGLEQUOTESTRING=55, WHITESPACE=56;
	public static final int
		RULE_program = 0, RULE_block = 1, RULE_stat = 2, RULE_var = 3, RULE_nametype = 4, 
		RULE_type = 5, RULE_tableType = 6, RULE_unionType = 7, RULE_listType = 8, 
		RULE_prefix = 9, RULE_suffix = 10, RULE_exp = 11, RULE_functionbody = 12, 
		RULE_laststat = 13, RULE_typednamelist = 14, RULE_functioncall = 15, RULE_explist = 16, 
		RULE_tableconstructor = 17, RULE_fieldlist = 18, RULE_field = 19, RULE_binop = 20, 
		RULE_unop = 21, RULE_string = 22, RULE_number = 23;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "block", "stat", "var", "nametype", "type", "tableType", "unionType", 
			"listType", "prefix", "suffix", "exp", "functionbody", "laststat", "typednamelist", 
			"functioncall", "explist", "tableconstructor", "fieldlist", "field", 
			"binop", "unop", "string", "number"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'='", "'do'", "'end'", "'while'", "'if'", "'then'", "'elseif'", 
			"'else'", "'for'", "','", "'in'", "'function'", "':'", "'Table'", "'['", 
			"']'", "'Union'", "'List'", "'.'", "'nil'", "'('", "')'", "'->'", "'return'", 
			"'break'", "'continue'", "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", "'%'", 
			"'^'", "'#'", "'=='", "'~='", "'<='", "'>='", "'<'", "'>'", "'|'", "'&'", 
			"'or'", "'and'", "'..'", "'not'", null, "'false'", "'true'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, "NAME", "FALSE", "TRUE", "INT", "FLOAT", "DOUBLEQUOTESTRING", "SINGLEQUOTESTRING", 
			"WHITESPACE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "rdsp.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public rdspParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode EOF() { return getToken(rdspParser.EOF, 0); }
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			block();
			setState(49);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlockContext extends ParserRuleContext {
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public LaststatContext laststat() {
			return getRuleContext(LaststatContext.class,0);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(57);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__2) | (1L << T__4) | (1L << T__5) | (1L << T__9) | (1L << T__12) | (1L << NAME))) != 0)) {
				{
				{
				setState(51);
				stat();
				setState(53);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__0) {
					{
					setState(52);
					match(T__0);
					}
				}

				}
				}
				setState(59);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(61);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__24) | (1L << T__25) | (1L << T__26))) != 0)) {
				{
				setState(60);
				laststat();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatContext extends ParserRuleContext {
		public NametypeContext nametype() {
			return getRuleContext(NametypeContext.class,0);
		}
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public FunctioncallContext functioncall() {
			return getRuleContext(FunctioncallContext.class,0);
		}
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public List<TerminalNode> NAME() { return getTokens(rdspParser.NAME); }
		public TerminalNode NAME(int i) {
			return getToken(rdspParser.NAME, i);
		}
		public FunctionbodyContext functionbody() {
			return getRuleContext(FunctionbodyContext.class,0);
		}
		public StatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stat; }
	}

	public final StatContext stat() throws RecognitionException {
		StatContext _localctx = new StatContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_stat);
		int _la;
		try {
			setState(129);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(63);
				nametype();
				setState(64);
				match(T__1);
				setState(65);
				exp(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(67);
				var();
				setState(68);
				match(T__1);
				setState(69);
				exp(0);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(71);
				functioncall();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(72);
				match(T__2);
				setState(73);
				block();
				setState(74);
				match(T__3);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(76);
				match(T__4);
				setState(77);
				exp(0);
				setState(78);
				match(T__2);
				setState(79);
				block();
				setState(80);
				match(T__3);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(82);
				match(T__5);
				setState(83);
				exp(0);
				setState(84);
				match(T__6);
				setState(85);
				block();
				setState(93);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__7) {
					{
					{
					setState(86);
					match(T__7);
					setState(87);
					exp(0);
					setState(88);
					match(T__6);
					setState(89);
					block();
					}
					}
					setState(95);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(98);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__8) {
					{
					setState(96);
					match(T__8);
					setState(97);
					block();
					}
				}

				setState(100);
				match(T__3);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(102);
				match(T__9);
				setState(103);
				match(NAME);
				setState(104);
				match(T__1);
				setState(105);
				exp(0);
				setState(106);
				match(T__10);
				setState(107);
				exp(0);
				setState(110);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__10) {
					{
					setState(108);
					match(T__10);
					setState(109);
					exp(0);
					}
				}

				setState(112);
				match(T__2);
				setState(113);
				block();
				setState(114);
				match(T__3);
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(116);
				match(T__9);
				setState(117);
				match(NAME);
				setState(118);
				match(T__10);
				setState(119);
				match(NAME);
				setState(120);
				match(T__11);
				setState(121);
				functioncall();
				setState(122);
				match(T__2);
				setState(123);
				block();
				setState(124);
				match(T__3);
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(126);
				match(T__12);
				setState(127);
				match(NAME);
				setState(128);
				functionbody();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VarContext extends ParserRuleContext {
		public TerminalNode NAME() { return getToken(rdspParser.NAME, 0); }
		public SuffixContext suffix() {
			return getRuleContext(SuffixContext.class,0);
		}
		public VarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var; }
	}

	public final VarContext var() throws RecognitionException {
		VarContext _localctx = new VarContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_var);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(131);
			match(NAME);
			setState(133);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				{
				setState(132);
				suffix();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NametypeContext extends ParserRuleContext {
		public TerminalNode NAME() { return getToken(rdspParser.NAME, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public NametypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_nametype; }
	}

	public final NametypeContext nametype() throws RecognitionException {
		NametypeContext _localctx = new NametypeContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_nametype);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(135);
			match(NAME);
			setState(136);
			match(T__13);
			setState(137);
			type();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypeContext extends ParserRuleContext {
		public TerminalNode NAME() { return getToken(rdspParser.NAME, 0); }
		public ListTypeContext listType() {
			return getRuleContext(ListTypeContext.class,0);
		}
		public UnionTypeContext unionType() {
			return getRuleContext(UnionTypeContext.class,0);
		}
		public TableTypeContext tableType() {
			return getRuleContext(TableTypeContext.class,0);
		}
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_type);
		try {
			setState(143);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NAME:
				enterOuterAlt(_localctx, 1);
				{
				setState(139);
				match(NAME);
				}
				break;
			case T__18:
				enterOuterAlt(_localctx, 2);
				{
				setState(140);
				listType();
				}
				break;
			case T__17:
				enterOuterAlt(_localctx, 3);
				{
				setState(141);
				unionType();
				}
				break;
			case T__14:
				enterOuterAlt(_localctx, 4);
				{
				setState(142);
				tableType();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TableTypeContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TableTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tableType; }
	}

	public final TableTypeContext tableType() throws RecognitionException {
		TableTypeContext _localctx = new TableTypeContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_tableType);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(145);
			match(T__14);
			setState(146);
			match(T__15);
			setState(147);
			type();
			setState(148);
			match(T__16);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class UnionTypeContext extends ParserRuleContext {
		public List<TypeContext> type() {
			return getRuleContexts(TypeContext.class);
		}
		public TypeContext type(int i) {
			return getRuleContext(TypeContext.class,i);
		}
		public UnionTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unionType; }
	}

	public final UnionTypeContext unionType() throws RecognitionException {
		UnionTypeContext _localctx = new UnionTypeContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_unionType);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(150);
			match(T__17);
			setState(151);
			match(T__15);
			setState(152);
			type();
			setState(155); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(153);
				match(T__10);
				setState(154);
				type();
				}
				}
				setState(157); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==T__10 );
			setState(159);
			match(T__16);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ListTypeContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public ListTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listType; }
	}

	public final ListTypeContext listType() throws RecognitionException {
		ListTypeContext _localctx = new ListTypeContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_listType);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(161);
			match(T__18);
			setState(162);
			match(T__15);
			setState(163);
			type();
			setState(164);
			match(T__16);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PrefixContext extends ParserRuleContext {
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public FunctioncallContext functioncall() {
			return getRuleContext(FunctioncallContext.class,0);
		}
		public SuffixContext suffix() {
			return getRuleContext(SuffixContext.class,0);
		}
		public PrefixContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prefix; }
	}

	public final PrefixContext prefix() throws RecognitionException {
		PrefixContext _localctx = new PrefixContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_prefix);
		try {
			setState(171);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(166);
				var();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(167);
				functioncall();
				setState(169);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
				case 1:
					{
					setState(168);
					suffix();
					}
					break;
				}
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SuffixContext extends ParserRuleContext {
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public List<TerminalNode> NAME() { return getTokens(rdspParser.NAME); }
		public TerminalNode NAME(int i) {
			return getToken(rdspParser.NAME, i);
		}
		public SuffixContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_suffix; }
	}

	public final SuffixContext suffix() throws RecognitionException {
		SuffixContext _localctx = new SuffixContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_suffix);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(179); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					setState(179);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case T__15:
						{
						setState(173);
						match(T__15);
						setState(174);
						exp(0);
						setState(175);
						match(T__16);
						}
						break;
					case T__19:
						{
						setState(177);
						match(T__19);
						setState(178);
						match(NAME);
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(181); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpContext extends ParserRuleContext {
		public NumberContext number() {
			return getRuleContext(NumberContext.class,0);
		}
		public StringContext string() {
			return getRuleContext(StringContext.class,0);
		}
		public TerminalNode TRUE() { return getToken(rdspParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(rdspParser.FALSE, 0); }
		public PrefixContext prefix() {
			return getRuleContext(PrefixContext.class,0);
		}
		public UnopContext unop() {
			return getRuleContext(UnopContext.class,0);
		}
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public TableconstructorContext tableconstructor() {
			return getRuleContext(TableconstructorContext.class,0);
		}
		public BinopContext binop() {
			return getRuleContext(BinopContext.class,0);
		}
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
	}

	public final ExpContext exp() throws RecognitionException {
		return exp(0);
	}

	private ExpContext exp(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpContext _localctx = new ExpContext(_ctx, _parentState);
		ExpContext _prevctx = _localctx;
		int _startState = 22;
		enterRecursionRule(_localctx, 22, RULE_exp, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(194);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
			case FLOAT:
				{
				setState(184);
				number();
				}
				break;
			case DOUBLEQUOTESTRING:
			case SINGLEQUOTESTRING:
				{
				setState(185);
				string();
				}
				break;
			case TRUE:
				{
				setState(186);
				match(TRUE);
				}
				break;
			case FALSE:
				{
				setState(187);
				match(FALSE);
				}
				break;
			case T__20:
				{
				setState(188);
				match(T__20);
				}
				break;
			case NAME:
				{
				setState(189);
				prefix();
				}
				break;
			case T__30:
			case T__35:
			case T__47:
				{
				setState(190);
				unop();
				setState(191);
				exp(2);
				}
				break;
			case T__27:
				{
				setState(193);
				tableconstructor();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(202);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ExpContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_exp);
					setState(196);
					if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
					setState(197);
					binop();
					setState(198);
					exp(4);
					}
					} 
				}
				setState(204);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class FunctionbodyContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TypednamelistContext typednamelist() {
			return getRuleContext(TypednamelistContext.class,0);
		}
		public FunctionbodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionbody; }
	}

	public final FunctionbodyContext functionbody() throws RecognitionException {
		FunctionbodyContext _localctx = new FunctionbodyContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_functionbody);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(205);
			match(T__21);
			setState(207);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NAME) {
				{
				setState(206);
				typednamelist();
				}
			}

			setState(209);
			match(T__22);
			setState(210);
			match(T__23);
			setState(211);
			type();
			setState(212);
			block();
			setState(213);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LaststatContext extends ParserRuleContext {
		public ExplistContext explist() {
			return getRuleContext(ExplistContext.class,0);
		}
		public LaststatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_laststat; }
	}

	public final LaststatContext laststat() throws RecognitionException {
		LaststatContext _localctx = new LaststatContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_laststat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(221);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__24:
				{
				setState(215);
				match(T__24);
				setState(217);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__20) | (1L << T__27) | (1L << T__30) | (1L << T__35) | (1L << T__47) | (1L << NAME) | (1L << FALSE) | (1L << TRUE) | (1L << INT) | (1L << FLOAT) | (1L << DOUBLEQUOTESTRING) | (1L << SINGLEQUOTESTRING))) != 0)) {
					{
					setState(216);
					explist();
					}
				}

				}
				break;
			case T__25:
				{
				setState(219);
				match(T__25);
				}
				break;
			case T__26:
				{
				setState(220);
				match(T__26);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(224);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__0) {
				{
				setState(223);
				match(T__0);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypednamelistContext extends ParserRuleContext {
		public List<NametypeContext> nametype() {
			return getRuleContexts(NametypeContext.class);
		}
		public NametypeContext nametype(int i) {
			return getRuleContext(NametypeContext.class,i);
		}
		public TypednamelistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typednamelist; }
	}

	public final TypednamelistContext typednamelist() throws RecognitionException {
		TypednamelistContext _localctx = new TypednamelistContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_typednamelist);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(226);
			nametype();
			setState(231);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__10) {
				{
				{
				setState(227);
				match(T__10);
				setState(228);
				nametype();
				}
				}
				setState(233);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctioncallContext extends ParserRuleContext {
		public TerminalNode NAME() { return getToken(rdspParser.NAME, 0); }
		public ExplistContext explist() {
			return getRuleContext(ExplistContext.class,0);
		}
		public FunctioncallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functioncall; }
	}

	public final FunctioncallContext functioncall() throws RecognitionException {
		FunctioncallContext _localctx = new FunctioncallContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_functioncall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(234);
			match(NAME);
			setState(235);
			match(T__21);
			setState(237);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__20) | (1L << T__27) | (1L << T__30) | (1L << T__35) | (1L << T__47) | (1L << NAME) | (1L << FALSE) | (1L << TRUE) | (1L << INT) | (1L << FLOAT) | (1L << DOUBLEQUOTESTRING) | (1L << SINGLEQUOTESTRING))) != 0)) {
				{
				setState(236);
				explist();
				}
			}

			setState(239);
			match(T__22);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExplistContext extends ParserRuleContext {
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public ExplistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_explist; }
	}

	public final ExplistContext explist() throws RecognitionException {
		ExplistContext _localctx = new ExplistContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_explist);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(241);
			exp(0);
			setState(246);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__10) {
				{
				{
				setState(242);
				match(T__10);
				setState(243);
				exp(0);
				}
				}
				setState(248);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TableconstructorContext extends ParserRuleContext {
		public FieldlistContext fieldlist() {
			return getRuleContext(FieldlistContext.class,0);
		}
		public TableconstructorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tableconstructor; }
	}

	public final TableconstructorContext tableconstructor() throws RecognitionException {
		TableconstructorContext _localctx = new TableconstructorContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_tableconstructor);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(249);
			match(T__27);
			setState(251);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__15) | (1L << T__20) | (1L << T__27) | (1L << T__30) | (1L << T__35) | (1L << T__47) | (1L << NAME) | (1L << FALSE) | (1L << TRUE) | (1L << INT) | (1L << FLOAT) | (1L << DOUBLEQUOTESTRING) | (1L << SINGLEQUOTESTRING))) != 0)) {
				{
				setState(250);
				fieldlist();
				}
			}

			setState(253);
			match(T__28);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FieldlistContext extends ParserRuleContext {
		public List<FieldContext> field() {
			return getRuleContexts(FieldContext.class);
		}
		public FieldContext field(int i) {
			return getRuleContext(FieldContext.class,i);
		}
		public FieldlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fieldlist; }
	}

	public final FieldlistContext fieldlist() throws RecognitionException {
		FieldlistContext _localctx = new FieldlistContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_fieldlist);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(255);
			field();
			setState(260);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__10) {
				{
				{
				setState(256);
				match(T__10);
				setState(257);
				field();
				}
				}
				setState(262);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FieldContext extends ParserRuleContext {
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public NametypeContext nametype() {
			return getRuleContext(NametypeContext.class,0);
		}
		public FieldContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_field; }
	}

	public final FieldContext field() throws RecognitionException {
		FieldContext _localctx = new FieldContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_field);
		try {
			setState(276);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,25,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(263);
				match(T__15);
				setState(264);
				exp(0);
				setState(265);
				match(T__16);
				setState(266);
				match(T__13);
				setState(267);
				type();
				setState(268);
				match(T__1);
				setState(269);
				exp(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(271);
				nametype();
				setState(272);
				match(T__1);
				setState(273);
				exp(0);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(275);
				exp(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BinopContext extends ParserRuleContext {
		public BinopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_binop; }
	}

	public final BinopContext binop() throws RecognitionException {
		BinopContext _localctx = new BinopContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_binop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(278);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__29) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << T__33) | (1L << T__34) | (1L << T__35) | (1L << T__36) | (1L << T__37) | (1L << T__38) | (1L << T__39) | (1L << T__40) | (1L << T__41) | (1L << T__42) | (1L << T__43) | (1L << T__44) | (1L << T__45) | (1L << T__46))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class UnopContext extends ParserRuleContext {
		public UnopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unop; }
	}

	public final UnopContext unop() throws RecognitionException {
		UnopContext _localctx = new UnopContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_unop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(280);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__30) | (1L << T__35) | (1L << T__47))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StringContext extends ParserRuleContext {
		public TerminalNode DOUBLEQUOTESTRING() { return getToken(rdspParser.DOUBLEQUOTESTRING, 0); }
		public TerminalNode SINGLEQUOTESTRING() { return getToken(rdspParser.SINGLEQUOTESTRING, 0); }
		public StringContext string() {
			return getRuleContext(StringContext.class,0);
		}
		public StringContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_string; }
	}

	public final StringContext string() throws RecognitionException {
		StringContext _localctx = new StringContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_string);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(282);
			_la = _input.LA(1);
			if ( !(_la==DOUBLEQUOTESTRING || _la==SINGLEQUOTESTRING) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(285);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,26,_ctx) ) {
			case 1:
				{
				setState(283);
				match(T__46);
				setState(284);
				string();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NumberContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(rdspParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(rdspParser.FLOAT, 0); }
		public NumberContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_number; }
	}

	public final NumberContext number() throws RecognitionException {
		NumberContext _localctx = new NumberContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_number);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(287);
			_la = _input.LA(1);
			if ( !(_la==INT || _la==FLOAT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 11:
			return exp_sempred((ExpContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean exp_sempred(ExpContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 3);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3:\u0124\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\3\2\3\2\3\2\3\3\3\3\5\38\n\3\7\3:\n\3\f\3\16\3=\13\3\3\3\5\3@\n\3\3\4"+
		"\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3"+
		"\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4^\n\4\f\4\16\4a\13\4\3\4\3\4"+
		"\5\4e\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4q\n\4\3\4\3\4\3\4"+
		"\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u0084\n\4"+
		"\3\5\3\5\5\5\u0088\n\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\5\7\u0092\n\7\3"+
		"\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\6\t\u009e\n\t\r\t\16\t\u009f\3"+
		"\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\5\13\u00ac\n\13\5\13\u00ae\n"+
		"\13\3\f\3\f\3\f\3\f\3\f\3\f\6\f\u00b6\n\f\r\f\16\f\u00b7\3\r\3\r\3\r\3"+
		"\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00c5\n\r\3\r\3\r\3\r\3\r\7\r\u00cb"+
		"\n\r\f\r\16\r\u00ce\13\r\3\16\3\16\5\16\u00d2\n\16\3\16\3\16\3\16\3\16"+
		"\3\16\3\16\3\17\3\17\5\17\u00dc\n\17\3\17\3\17\5\17\u00e0\n\17\3\17\5"+
		"\17\u00e3\n\17\3\20\3\20\3\20\7\20\u00e8\n\20\f\20\16\20\u00eb\13\20\3"+
		"\21\3\21\3\21\5\21\u00f0\n\21\3\21\3\21\3\22\3\22\3\22\7\22\u00f7\n\22"+
		"\f\22\16\22\u00fa\13\22\3\23\3\23\5\23\u00fe\n\23\3\23\3\23\3\24\3\24"+
		"\3\24\7\24\u0105\n\24\f\24\16\24\u0108\13\24\3\25\3\25\3\25\3\25\3\25"+
		"\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u0117\n\25\3\26\3\26\3\27"+
		"\3\27\3\30\3\30\3\30\5\30\u0120\n\30\3\31\3\31\3\31\2\3\30\32\2\4\6\b"+
		"\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\2\6\3\2 \61\5\2!!&&\62\62"+
		"\3\289\3\2\66\67\2\u0137\2\62\3\2\2\2\4;\3\2\2\2\6\u0083\3\2\2\2\b\u0085"+
		"\3\2\2\2\n\u0089\3\2\2\2\f\u0091\3\2\2\2\16\u0093\3\2\2\2\20\u0098\3\2"+
		"\2\2\22\u00a3\3\2\2\2\24\u00ad\3\2\2\2\26\u00b5\3\2\2\2\30\u00c4\3\2\2"+
		"\2\32\u00cf\3\2\2\2\34\u00df\3\2\2\2\36\u00e4\3\2\2\2 \u00ec\3\2\2\2\""+
		"\u00f3\3\2\2\2$\u00fb\3\2\2\2&\u0101\3\2\2\2(\u0116\3\2\2\2*\u0118\3\2"+
		"\2\2,\u011a\3\2\2\2.\u011c\3\2\2\2\60\u0121\3\2\2\2\62\63\5\4\3\2\63\64"+
		"\7\2\2\3\64\3\3\2\2\2\65\67\5\6\4\2\668\7\3\2\2\67\66\3\2\2\2\678\3\2"+
		"\2\28:\3\2\2\29\65\3\2\2\2:=\3\2\2\2;9\3\2\2\2;<\3\2\2\2<?\3\2\2\2=;\3"+
		"\2\2\2>@\5\34\17\2?>\3\2\2\2?@\3\2\2\2@\5\3\2\2\2AB\5\n\6\2BC\7\4\2\2"+
		"CD\5\30\r\2D\u0084\3\2\2\2EF\5\b\5\2FG\7\4\2\2GH\5\30\r\2H\u0084\3\2\2"+
		"\2I\u0084\5 \21\2JK\7\5\2\2KL\5\4\3\2LM\7\6\2\2M\u0084\3\2\2\2NO\7\7\2"+
		"\2OP\5\30\r\2PQ\7\5\2\2QR\5\4\3\2RS\7\6\2\2S\u0084\3\2\2\2TU\7\b\2\2U"+
		"V\5\30\r\2VW\7\t\2\2W_\5\4\3\2XY\7\n\2\2YZ\5\30\r\2Z[\7\t\2\2[\\\5\4\3"+
		"\2\\^\3\2\2\2]X\3\2\2\2^a\3\2\2\2_]\3\2\2\2_`\3\2\2\2`d\3\2\2\2a_\3\2"+
		"\2\2bc\7\13\2\2ce\5\4\3\2db\3\2\2\2de\3\2\2\2ef\3\2\2\2fg\7\6\2\2g\u0084"+
		"\3\2\2\2hi\7\f\2\2ij\7\63\2\2jk\7\4\2\2kl\5\30\r\2lm\7\r\2\2mp\5\30\r"+
		"\2no\7\r\2\2oq\5\30\r\2pn\3\2\2\2pq\3\2\2\2qr\3\2\2\2rs\7\5\2\2st\5\4"+
		"\3\2tu\7\6\2\2u\u0084\3\2\2\2vw\7\f\2\2wx\7\63\2\2xy\7\r\2\2yz\7\63\2"+
		"\2z{\7\16\2\2{|\5 \21\2|}\7\5\2\2}~\5\4\3\2~\177\7\6\2\2\177\u0084\3\2"+
		"\2\2\u0080\u0081\7\17\2\2\u0081\u0082\7\63\2\2\u0082\u0084\5\32\16\2\u0083"+
		"A\3\2\2\2\u0083E\3\2\2\2\u0083I\3\2\2\2\u0083J\3\2\2\2\u0083N\3\2\2\2"+
		"\u0083T\3\2\2\2\u0083h\3\2\2\2\u0083v\3\2\2\2\u0083\u0080\3\2\2\2\u0084"+
		"\7\3\2\2\2\u0085\u0087\7\63\2\2\u0086\u0088\5\26\f\2\u0087\u0086\3\2\2"+
		"\2\u0087\u0088\3\2\2\2\u0088\t\3\2\2\2\u0089\u008a\7\63\2\2\u008a\u008b"+
		"\7\20\2\2\u008b\u008c\5\f\7\2\u008c\13\3\2\2\2\u008d\u0092\7\63\2\2\u008e"+
		"\u0092\5\22\n\2\u008f\u0092\5\20\t\2\u0090\u0092\5\16\b\2\u0091\u008d"+
		"\3\2\2\2\u0091\u008e\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0090\3\2\2\2\u0092"+
		"\r\3\2\2\2\u0093\u0094\7\21\2\2\u0094\u0095\7\22\2\2\u0095\u0096\5\f\7"+
		"\2\u0096\u0097\7\23\2\2\u0097\17\3\2\2\2\u0098\u0099\7\24\2\2\u0099\u009a"+
		"\7\22\2\2\u009a\u009d\5\f\7\2\u009b\u009c\7\r\2\2\u009c\u009e\5\f\7\2"+
		"\u009d\u009b\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u00a0"+
		"\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2\7\23\2\2\u00a2\21\3\2\2\2\u00a3"+
		"\u00a4\7\25\2\2\u00a4\u00a5\7\22\2\2\u00a5\u00a6\5\f\7\2\u00a6\u00a7\7"+
		"\23\2\2\u00a7\23\3\2\2\2\u00a8\u00ae\5\b\5\2\u00a9\u00ab\5 \21\2\u00aa"+
		"\u00ac\5\26\f\2\u00ab\u00aa\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ae\3"+
		"\2\2\2\u00ad\u00a8\3\2\2\2\u00ad\u00a9\3\2\2\2\u00ae\25\3\2\2\2\u00af"+
		"\u00b0\7\22\2\2\u00b0\u00b1\5\30\r\2\u00b1\u00b2\7\23\2\2\u00b2\u00b6"+
		"\3\2\2\2\u00b3\u00b4\7\26\2\2\u00b4\u00b6\7\63\2\2\u00b5\u00af\3\2\2\2"+
		"\u00b5\u00b3\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b8"+
		"\3\2\2\2\u00b8\27\3\2\2\2\u00b9\u00ba\b\r\1\2\u00ba\u00c5\5\60\31\2\u00bb"+
		"\u00c5\5.\30\2\u00bc\u00c5\7\65\2\2\u00bd\u00c5\7\64\2\2\u00be\u00c5\7"+
		"\27\2\2\u00bf\u00c5\5\24\13\2\u00c0\u00c1\5,\27\2\u00c1\u00c2\5\30\r\4"+
		"\u00c2\u00c5\3\2\2\2\u00c3\u00c5\5$\23\2\u00c4\u00b9\3\2\2\2\u00c4\u00bb"+
		"\3\2\2\2\u00c4\u00bc\3\2\2\2\u00c4\u00bd\3\2\2\2\u00c4\u00be\3\2\2\2\u00c4"+
		"\u00bf\3\2\2\2\u00c4\u00c0\3\2\2\2\u00c4\u00c3\3\2\2\2\u00c5\u00cc\3\2"+
		"\2\2\u00c6\u00c7\f\5\2\2\u00c7\u00c8\5*\26\2\u00c8\u00c9\5\30\r\6\u00c9"+
		"\u00cb\3\2\2\2\u00ca\u00c6\3\2\2\2\u00cb\u00ce\3\2\2\2\u00cc\u00ca\3\2"+
		"\2\2\u00cc\u00cd\3\2\2\2\u00cd\31\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\u00d1"+
		"\7\30\2\2\u00d0\u00d2\5\36\20\2\u00d1\u00d0\3\2\2\2\u00d1\u00d2\3\2\2"+
		"\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4\7\31\2\2\u00d4\u00d5\7\32\2\2\u00d5"+
		"\u00d6\5\f\7\2\u00d6\u00d7\5\4\3\2\u00d7\u00d8\7\6\2\2\u00d8\33\3\2\2"+
		"\2\u00d9\u00db\7\33\2\2\u00da\u00dc\5\"\22\2\u00db\u00da\3\2\2\2\u00db"+
		"\u00dc\3\2\2\2\u00dc\u00e0\3\2\2\2\u00dd\u00e0\7\34\2\2\u00de\u00e0\7"+
		"\35\2\2\u00df\u00d9\3\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00de\3\2\2\2\u00e0"+
		"\u00e2\3\2\2\2\u00e1\u00e3\7\3\2\2\u00e2\u00e1\3\2\2\2\u00e2\u00e3\3\2"+
		"\2\2\u00e3\35\3\2\2\2\u00e4\u00e9\5\n\6\2\u00e5\u00e6\7\r\2\2\u00e6\u00e8"+
		"\5\n\6\2\u00e7\u00e5\3\2\2\2\u00e8\u00eb\3\2\2\2\u00e9\u00e7\3\2\2\2\u00e9"+
		"\u00ea\3\2\2\2\u00ea\37\3\2\2\2\u00eb\u00e9\3\2\2\2\u00ec\u00ed\7\63\2"+
		"\2\u00ed\u00ef\7\30\2\2\u00ee\u00f0\5\"\22\2\u00ef\u00ee\3\2\2\2\u00ef"+
		"\u00f0\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\u00f2\7\31\2\2\u00f2!\3\2\2\2"+
		"\u00f3\u00f8\5\30\r\2\u00f4\u00f5\7\r\2\2\u00f5\u00f7\5\30\r\2\u00f6\u00f4"+
		"\3\2\2\2\u00f7\u00fa\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9"+
		"#\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fb\u00fd\7\36\2\2\u00fc\u00fe\5&\24\2"+
		"\u00fd\u00fc\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0100"+
		"\7\37\2\2\u0100%\3\2\2\2\u0101\u0106\5(\25\2\u0102\u0103\7\r\2\2\u0103"+
		"\u0105\5(\25\2\u0104\u0102\3\2\2\2\u0105\u0108\3\2\2\2\u0106\u0104\3\2"+
		"\2\2\u0106\u0107\3\2\2\2\u0107\'\3\2\2\2\u0108\u0106\3\2\2\2\u0109\u010a"+
		"\7\22\2\2\u010a\u010b\5\30\r\2\u010b\u010c\7\23\2\2\u010c\u010d\7\20\2"+
		"\2\u010d\u010e\5\f\7\2\u010e\u010f\7\4\2\2\u010f\u0110\5\30\r\2\u0110"+
		"\u0117\3\2\2\2\u0111\u0112\5\n\6\2\u0112\u0113\7\4\2\2\u0113\u0114\5\30"+
		"\r\2\u0114\u0117\3\2\2\2\u0115\u0117\5\30\r\2\u0116\u0109\3\2\2\2\u0116"+
		"\u0111\3\2\2\2\u0116\u0115\3\2\2\2\u0117)\3\2\2\2\u0118\u0119\t\2\2\2"+
		"\u0119+\3\2\2\2\u011a\u011b\t\3\2\2\u011b-\3\2\2\2\u011c\u011f\t\4\2\2"+
		"\u011d\u011e\7\61\2\2\u011e\u0120\5.\30\2\u011f\u011d\3\2\2\2\u011f\u0120"+
		"\3\2\2\2\u0120/\3\2\2\2\u0121\u0122\t\5\2\2\u0122\61\3\2\2\2\35\67;?_"+
		"dp\u0083\u0087\u0091\u009f\u00ab\u00ad\u00b5\u00b7\u00c4\u00cc\u00d1\u00db"+
		"\u00df\u00e2\u00e9\u00ef\u00f8\u00fd\u0106\u0116\u011f";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}