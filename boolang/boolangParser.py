# Generated from boolang.g4 by ANTLR 4.12.0
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
        4,1,11,52,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,4,
        0,14,8,0,11,0,12,0,15,1,0,1,0,1,1,1,1,1,1,3,1,23,8,1,1,2,1,2,1,2,
        1,2,1,3,1,3,1,3,1,3,4,3,33,8,3,11,3,12,3,34,1,3,1,3,4,3,39,8,3,11,
        3,12,3,40,3,3,43,8,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,0,0,6,0,2,4,
        6,8,10,0,1,1,0,7,9,51,0,13,1,0,0,0,2,22,1,0,0,0,4,24,1,0,0,0,6,28,
        1,0,0,0,8,46,1,0,0,0,10,49,1,0,0,0,12,14,3,2,1,0,13,12,1,0,0,0,14,
        15,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,17,1,0,0,0,17,18,5,0,0,
        1,18,1,1,0,0,0,19,23,3,4,2,0,20,23,3,6,3,0,21,23,3,8,4,0,22,19,1,
        0,0,0,22,20,1,0,0,0,22,21,1,0,0,0,23,3,1,0,0,0,24,25,5,9,0,0,25,
        26,5,1,0,0,26,27,3,10,5,0,27,5,1,0,0,0,28,29,5,2,0,0,29,30,3,10,
        5,0,30,32,5,3,0,0,31,33,3,2,1,0,32,31,1,0,0,0,33,34,1,0,0,0,34,32,
        1,0,0,0,34,35,1,0,0,0,35,42,1,0,0,0,36,38,5,4,0,0,37,39,3,2,1,0,
        38,37,1,0,0,0,39,40,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,43,1,
        0,0,0,42,36,1,0,0,0,42,43,1,0,0,0,43,44,1,0,0,0,44,45,5,5,0,0,45,
        7,1,0,0,0,46,47,5,6,0,0,47,48,5,10,0,0,48,9,1,0,0,0,49,50,7,0,0,
        0,50,11,1,0,0,0,5,15,22,34,40,42
    ]

class boolangParser ( Parser ):

    grammarFileName = "boolang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'if'", "'then'", "'else'", "'end'", 
                     "'echo'", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "INT", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_assignment = 2
    RULE_ifStatement = 3
    RULE_echoStatement = 4
    RULE_boolExpr = 5

    ruleNames =  [ "prog", "stat", "assignment", "ifStatement", "echoStatement", 
                   "boolExpr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    ID=9
    INT=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(boolangParser.EOF, 0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(boolangParser.StatContext)
            else:
                return self.getTypedRuleContext(boolangParser.StatContext,i)


        def getRuleIndex(self):
            return boolangParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = boolangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.stat()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 580) != 0)):
                    break

            self.state = 17
            self.match(boolangParser.EOF)
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

        def assignment(self):
            return self.getTypedRuleContext(boolangParser.AssignmentContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(boolangParser.IfStatementContext,0)


        def echoStatement(self):
            return self.getTypedRuleContext(boolangParser.EchoStatementContext,0)


        def getRuleIndex(self):
            return boolangParser.RULE_stat

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

        localctx = boolangParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.assignment()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.ifStatement()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 21
                self.echoStatement()
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


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(boolangParser.ID, 0)

        def boolExpr(self):
            return self.getTypedRuleContext(boolangParser.BoolExprContext,0)


        def getRuleIndex(self):
            return boolangParser.RULE_assignment

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

        localctx = boolangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(boolangParser.ID)
            self.state = 25
            self.match(boolangParser.T__0)
            self.state = 26
            self.boolExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolExpr(self):
            return self.getTypedRuleContext(boolangParser.BoolExprContext,0)


        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(boolangParser.StatContext)
            else:
                return self.getTypedRuleContext(boolangParser.StatContext,i)


        def getRuleIndex(self):
            return boolangParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = boolangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(boolangParser.T__1)
            self.state = 29
            self.boolExpr()
            self.state = 30
            self.match(boolangParser.T__2)
            self.state = 32 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 31
                self.stat()
                self.state = 34 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 580) != 0)):
                    break

            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 36
                self.match(boolangParser.T__3)
                self.state = 38 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 37
                    self.stat()
                    self.state = 40 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 580) != 0)):
                        break



            self.state = 44
            self.match(boolangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EchoStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(boolangParser.INT, 0)

        def getRuleIndex(self):
            return boolangParser.RULE_echoStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEchoStatement" ):
                listener.enterEchoStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEchoStatement" ):
                listener.exitEchoStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEchoStatement" ):
                return visitor.visitEchoStatement(self)
            else:
                return visitor.visitChildren(self)




    def echoStatement(self):

        localctx = boolangParser.EchoStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_echoStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(boolangParser.T__5)
            self.state = 47
            self.match(boolangParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(boolangParser.ID, 0)

        def getRuleIndex(self):
            return boolangParser.RULE_boolExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolExpr" ):
                listener.enterBoolExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolExpr" ):
                listener.exitBoolExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolExpr" ):
                return visitor.visitBoolExpr(self)
            else:
                return visitor.visitChildren(self)




    def boolExpr(self):

        localctx = boolangParser.BoolExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_boolExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0)):
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





