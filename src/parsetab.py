
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABSTRACT AND ARROW AS ASIGDIV ASIGMINUS ASIGSUM ASIGTIMES ASSERT ASSIGN ASYNC AWAIT BOOLEAN BREAK CASE CATCH CLASS COMMA CONST CONTINUE DDOTS DIVISION DO DOT DOUBLE_TYPE DYNAMIC ELSE ENUM EQ EQ_V EXPORT EXTENDS FALSE FINALLY FLOAT FOR FUNCTION GT GTE IDENT IF IMPLEMENTS INT INTERFACE INT_TYPE LBRACE LBRACKET LIST LPAREN LT LTE MAP MINUS MINUSMINUS MOD NE NEGATION OR PLUS PLUSPLUS PRINT RBRACE RBRACKET RETURN RPAREN SEMICOLON SET STRING STRING_TYPE SUPER SWITCH TIMES TRUE TYPEDEF VAR VIR VOID WHILEbody : ifstm\n          | idmapifstm : IF LPAREN condition RPAREN LBRACE RBRACEcondition : preposition operator prepositioncondition :  preposition operator preposition morecondmorecond : operator preposition\n              | operator preposition morecond\n  operator : EQ\n              | NE\n              | AND\n              | OR\n  preposition : typrepreposition : NEGATION typretypre : STRING\n           | INT\n           | TRUE\n           | FALSE\n           | FLOAT\n           | IDENT\n  idmap : tymap IDENT EQ_V dictionarytymap : MAP\n           | MAP LT tykey COMMA tyvalue GTtykey : STRING_TYPE\n           | DOUBLE_TYPE\n           | INT_TYPEtyvalue : STRING_TYPE\n             | DOUBLE_TYPE\n             | INT_TYPE\n             | BOOLEAN\n             | IDENT\n             | iterable\n             | tymapiterable : LIST\n              | SETdictionary : LBRACE item RBRACEitem : key DDOTS value\n          | key DDOTS value COMMA itemkey : STRING\n         | INT\n         | FLOATvalue : STRING\n           | FLOAT\n           | INT\n           | FALSE\n           | TRUE\n           | IDENT\n           | iterable\n           | tymap'
    
_lr_action_items = {'IF':([0,],[4,]),'MAP':([0,34,56,],[6,6,6,]),'$end':([1,2,3,32,52,55,],[0,-1,-2,-20,-3,-35,]),'LPAREN':([4,],[7,]),'IDENT':([5,6,7,13,26,27,28,29,30,34,53,56,57,],[8,-21,19,19,19,-8,-9,-10,-11,47,19,65,-22,]),'GT':([6,42,43,44,45,46,47,48,49,50,51,57,],[-21,57,-26,-27,-28,-29,-30,-31,-32,-33,-34,-22,]),'COMMA':([6,21,22,23,24,50,51,57,59,60,61,62,63,64,65,66,67,],[-21,34,-23,-24,-25,-33,-34,-22,69,-41,-42,-43,-44,-45,-46,-47,-48,]),'RBRACE':([6,35,37,50,51,57,59,60,61,62,63,64,65,66,67,70,],[-21,52,55,-33,-34,-22,-36,-41,-42,-43,-44,-45,-46,-47,-48,-37,]),'LT':([6,],[9,]),'NEGATION':([7,26,27,28,29,30,53,],[13,13,-8,-9,-10,-11,13,]),'STRING':([7,13,26,27,28,29,30,33,53,56,69,],[14,14,14,-8,-9,-10,-11,39,14,60,39,]),'INT':([7,13,26,27,28,29,30,33,53,56,69,],[15,15,15,-8,-9,-10,-11,40,15,62,40,]),'TRUE':([7,13,26,27,28,29,30,53,56,],[16,16,16,-8,-9,-10,-11,16,64,]),'FALSE':([7,13,26,27,28,29,30,53,56,],[17,17,17,-8,-9,-10,-11,17,63,]),'FLOAT':([7,13,26,27,28,29,30,33,53,56,69,],[18,18,18,-8,-9,-10,-11,41,18,61,41,]),'EQ_V':([8,],[20,]),'STRING_TYPE':([9,34,],[22,43,]),'DOUBLE_TYPE':([9,34,],[23,44,]),'INT_TYPE':([9,34,],[24,45,]),'RPAREN':([10,12,14,15,16,17,18,19,31,36,54,58,68,],[25,-12,-14,-15,-16,-17,-18,-19,-13,-4,-5,-6,-7,]),'EQ':([11,12,14,15,16,17,18,19,31,36,58,],[27,-12,-14,-15,-16,-17,-18,-19,-13,27,27,]),'NE':([11,12,14,15,16,17,18,19,31,36,58,],[28,-12,-14,-15,-16,-17,-18,-19,-13,28,28,]),'AND':([11,12,14,15,16,17,18,19,31,36,58,],[29,-12,-14,-15,-16,-17,-18,-19,-13,29,29,]),'OR':([11,12,14,15,16,17,18,19,31,36,58,],[30,-12,-14,-15,-16,-17,-18,-19,-13,30,30,]),'LBRACE':([20,25,],[33,35,]),'BOOLEAN':([34,],[46,]),'LIST':([34,56,],[50,50,]),'SET':([34,56,],[51,51,]),'DDOTS':([38,39,40,41,],[56,-38,-39,-40,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'body':([0,],[1,]),'ifstm':([0,],[2,]),'idmap':([0,],[3,]),'tymap':([0,34,56,],[5,49,67,]),'condition':([7,],[10,]),'preposition':([7,26,53,],[11,36,58,]),'typre':([7,13,26,53,],[12,31,12,12,]),'tykey':([9,],[21,]),'operator':([11,36,58,],[26,53,53,]),'dictionary':([20,],[32,]),'item':([33,69,],[37,70,]),'key':([33,69,],[38,38,]),'tyvalue':([34,],[42,]),'iterable':([34,56,],[48,66,]),'morecond':([36,58,],[54,68,]),'value':([56,],[59,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> body","S'",1,None,None,None),
  ('body -> ifstm','body',1,'p_body','yacc.py',5),
  ('body -> idmap','body',1,'p_body','yacc.py',6),
  ('ifstm -> IF LPAREN condition RPAREN LBRACE RBRACE','ifstm',6,'p_ifstm','yacc.py',9),
  ('condition -> preposition operator preposition','condition',3,'p_condition','yacc.py',12),
  ('condition -> preposition operator preposition morecond','condition',4,'p_condition_more','yacc.py',15),
  ('morecond -> operator preposition','morecond',2,'p_morecond','yacc.py',18),
  ('morecond -> operator preposition morecond','morecond',3,'p_morecond','yacc.py',19),
  ('operator -> EQ','operator',1,'p_operator','yacc.py',23),
  ('operator -> NE','operator',1,'p_operator','yacc.py',24),
  ('operator -> AND','operator',1,'p_operator','yacc.py',25),
  ('operator -> OR','operator',1,'p_operator','yacc.py',26),
  ('preposition -> typre','preposition',1,'p_preposition','yacc.py',30),
  ('preposition -> NEGATION typre','preposition',2,'p_preposition_not','yacc.py',33),
  ('typre -> STRING','typre',1,'p_typre','yacc.py',36),
  ('typre -> INT','typre',1,'p_typre','yacc.py',37),
  ('typre -> TRUE','typre',1,'p_typre','yacc.py',38),
  ('typre -> FALSE','typre',1,'p_typre','yacc.py',39),
  ('typre -> FLOAT','typre',1,'p_typre','yacc.py',40),
  ('typre -> IDENT','typre',1,'p_typre','yacc.py',41),
  ('idmap -> tymap IDENT EQ_V dictionary','idmap',4,'p_idmap','yacc.py',45),
  ('tymap -> MAP','tymap',1,'p_tymap','yacc.py',48),
  ('tymap -> MAP LT tykey COMMA tyvalue GT','tymap',6,'p_tymap','yacc.py',49),
  ('tykey -> STRING_TYPE','tykey',1,'p_tykey','yacc.py',52),
  ('tykey -> DOUBLE_TYPE','tykey',1,'p_tykey','yacc.py',53),
  ('tykey -> INT_TYPE','tykey',1,'p_tykey','yacc.py',54),
  ('tyvalue -> STRING_TYPE','tyvalue',1,'p_tyvalue','yacc.py',57),
  ('tyvalue -> DOUBLE_TYPE','tyvalue',1,'p_tyvalue','yacc.py',58),
  ('tyvalue -> INT_TYPE','tyvalue',1,'p_tyvalue','yacc.py',59),
  ('tyvalue -> BOOLEAN','tyvalue',1,'p_tyvalue','yacc.py',60),
  ('tyvalue -> IDENT','tyvalue',1,'p_tyvalue','yacc.py',61),
  ('tyvalue -> iterable','tyvalue',1,'p_tyvalue','yacc.py',62),
  ('tyvalue -> tymap','tyvalue',1,'p_tyvalue','yacc.py',63),
  ('iterable -> LIST','iterable',1,'p_iterable','yacc.py',66),
  ('iterable -> SET','iterable',1,'p_iterable','yacc.py',67),
  ('dictionary -> LBRACE item RBRACE','dictionary',3,'p_dictionary','yacc.py',70),
  ('item -> key DDOTS value','item',3,'p_item','yacc.py',73),
  ('item -> key DDOTS value COMMA item','item',5,'p_item','yacc.py',74),
  ('key -> STRING','key',1,'p_key','yacc.py',77),
  ('key -> INT','key',1,'p_key','yacc.py',78),
  ('key -> FLOAT','key',1,'p_key','yacc.py',79),
  ('value -> STRING','value',1,'p_value','yacc.py',82),
  ('value -> FLOAT','value',1,'p_value','yacc.py',83),
  ('value -> INT','value',1,'p_value','yacc.py',84),
  ('value -> FALSE','value',1,'p_value','yacc.py',85),
  ('value -> TRUE','value',1,'p_value','yacc.py',86),
  ('value -> IDENT','value',1,'p_value','yacc.py',87),
  ('value -> iterable','value',1,'p_value','yacc.py',88),
  ('value -> tymap','value',1,'p_value','yacc.py',89),
]