
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABSTRACT AND ARROW AS ASIGDIV ASIGMINUS ASIGSUM ASIGTIMES ASSERT ASSIGN ASYNC AWAIT BOOLEAN BREAK CASE CATCH CLASS CLEAR_FUNC COMMA CONST CONTINUE DDOTS DIVISION DO DOT DOUBLE_TYPE DYNAMIC ELSE ENUM EQ EQ_V EXPORT EXTENDS FALSE FINALLY FLOAT FOR FUNCTION GT GTE IDENT IF IMPLEMENTS INT INTERFACE INT_TYPE LBRACE LBRACKET LIST LPAREN LT LTE MAP MINUS MINUSMINUS MOD NE NEGATION OR PLUS PLUSPLUS PRINT RBRACE RBRACKET REMOVE_FUNC RETURN RPAREN SEMICOLON SET STRING STRING_TYPE SUPER SWITCH TIMES TOSTRING_FUNC TRUE TYPEDEF VAR VIR VOID WHILEbody : ifstm\n          | idmap\n          | varfuncifstm : IF LPAREN condition RPAREN LBRACE RBRACEcondition : prepositioncondition : preposition operator prepositioncondition :  preposition operator preposition morecondmorecond : operator preposition\n              | operator preposition morecond\n  operator : EQ\n              | NE\n              | AND\n              | OR\n  preposition : typrepreposition : NEGATION typretypre : STRING\n           | INT\n           | TRUE\n           | FALSE\n           | FLOAT\n           | IDENT\n  idmap : tymap IDENT EQ_V dictionarytymap : MAP\n           | MAP LT tykey COMMA tyvalue GTtykey : STRING_TYPE\n           | DOUBLE_TYPE\n           | INT_TYPEtyvalue : STRING_TYPE\n             | DOUBLE_TYPE\n             | INT_TYPE\n             | BOOLEAN\n             | IDENT\n             | iterable\n             | tymapiterable : LIST\n              | SETdictionary : LBRACE item RBRACEitem : key DDOTS value\n          | key DDOTS value COMMA itemkey : STRING\n         | INT\n         | FLOATvalue : STRING\n           | FLOAT\n           | INT\n           | FALSE\n           | TRUE\n           | IDENT\n           | iterable\n           | tymapvarfunc : IDENT DOT functionfunction : CLEAR_FUNC LPAREN RPARENfunction : REMOVE_FUNC LPAREN STRING RPARENfunction : TOSTRING_FUNC LPAREN RPAREN'
    
_lr_action_items = {'IF':([0,],[5,]),'IDENT':([0,6,8,9,16,33,34,35,36,37,44,66,69,71,],[7,10,-23,22,22,22,-10,-11,-12,-13,60,22,79,-24,]),'MAP':([0,44,69,],[8,8,8,]),'$end':([1,2,3,4,24,39,52,54,65,68,70,],[0,-1,-2,-3,-51,-22,-52,-54,-4,-37,-53,]),'LPAREN':([5,25,26,27,],[9,41,42,43,]),'DOT':([7,],[11,]),'GT':([8,55,56,57,58,59,60,61,62,63,64,71,],[-23,71,-28,-29,-30,-31,-32,-33,-34,-35,-36,-24,]),'COMMA':([8,28,29,30,31,63,64,71,73,74,75,76,77,78,79,80,81,],[-23,44,-25,-26,-27,-35,-36,-24,83,-43,-44,-45,-46,-47,-48,-49,-50,]),'RBRACE':([8,45,47,63,64,71,73,74,75,76,77,78,79,80,81,84,],[-23,65,68,-35,-36,-24,-38,-43,-44,-45,-46,-47,-48,-49,-50,-39,]),'LT':([8,],[12,]),'NEGATION':([9,33,34,35,36,37,66,],[16,16,-10,-11,-12,-13,16,]),'STRING':([9,16,33,34,35,36,37,40,42,66,69,83,],[17,17,17,-10,-11,-12,-13,49,53,17,74,49,]),'INT':([9,16,33,34,35,36,37,40,66,69,83,],[18,18,18,-10,-11,-12,-13,50,18,76,50,]),'TRUE':([9,16,33,34,35,36,37,66,69,],[19,19,19,-10,-11,-12,-13,19,78,]),'FALSE':([9,16,33,34,35,36,37,66,69,],[20,20,20,-10,-11,-12,-13,20,77,]),'FLOAT':([9,16,33,34,35,36,37,40,66,69,83,],[21,21,21,-10,-11,-12,-13,51,21,75,51,]),'EQ_V':([10,],[23,]),'CLEAR_FUNC':([11,],[25,]),'REMOVE_FUNC':([11,],[26,]),'TOSTRING_FUNC':([11,],[27,]),'STRING_TYPE':([12,44,],[29,56,]),'DOUBLE_TYPE':([12,44,],[30,57,]),'INT_TYPE':([12,44,],[31,58,]),'RPAREN':([13,14,15,17,18,19,20,21,22,38,41,43,46,53,67,72,82,],[32,-5,-14,-16,-17,-18,-19,-20,-21,-15,52,54,-6,70,-7,-8,-9,]),'EQ':([14,15,17,18,19,20,21,22,38,46,72,],[34,-14,-16,-17,-18,-19,-20,-21,-15,34,34,]),'NE':([14,15,17,18,19,20,21,22,38,46,72,],[35,-14,-16,-17,-18,-19,-20,-21,-15,35,35,]),'AND':([14,15,17,18,19,20,21,22,38,46,72,],[36,-14,-16,-17,-18,-19,-20,-21,-15,36,36,]),'OR':([14,15,17,18,19,20,21,22,38,46,72,],[37,-14,-16,-17,-18,-19,-20,-21,-15,37,37,]),'LBRACE':([23,32,],[40,45,]),'BOOLEAN':([44,],[59,]),'LIST':([44,69,],[63,63,]),'SET':([44,69,],[64,64,]),'DDOTS':([48,49,50,51,],[69,-40,-41,-42,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'body':([0,],[1,]),'ifstm':([0,],[2,]),'idmap':([0,],[3,]),'varfunc':([0,],[4,]),'tymap':([0,44,69,],[6,62,81,]),'condition':([9,],[13,]),'preposition':([9,33,66,],[14,46,72,]),'typre':([9,16,33,66,],[15,38,15,15,]),'function':([11,],[24,]),'tykey':([12,],[28,]),'operator':([14,46,72,],[33,66,66,]),'dictionary':([23,],[39,]),'item':([40,83,],[47,84,]),'key':([40,83,],[48,48,]),'tyvalue':([44,],[55,]),'iterable':([44,69,],[61,80,]),'morecond':([46,72,],[67,82,]),'value':([69,],[73,]),}

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
  ('body -> varfunc','body',1,'p_body','yacc.py',7),
  ('ifstm -> IF LPAREN condition RPAREN LBRACE RBRACE','ifstm',6,'p_ifstm','yacc.py',10),
  ('condition -> preposition','condition',1,'p_condition_single','yacc.py',13),
  ('condition -> preposition operator preposition','condition',3,'p_condition','yacc.py',16),
  ('condition -> preposition operator preposition morecond','condition',4,'p_condition_more','yacc.py',19),
  ('morecond -> operator preposition','morecond',2,'p_morecond','yacc.py',22),
  ('morecond -> operator preposition morecond','morecond',3,'p_morecond','yacc.py',23),
  ('operator -> EQ','operator',1,'p_operator','yacc.py',27),
  ('operator -> NE','operator',1,'p_operator','yacc.py',28),
  ('operator -> AND','operator',1,'p_operator','yacc.py',29),
  ('operator -> OR','operator',1,'p_operator','yacc.py',30),
  ('preposition -> typre','preposition',1,'p_preposition','yacc.py',34),
  ('preposition -> NEGATION typre','preposition',2,'p_preposition_not','yacc.py',37),
  ('typre -> STRING','typre',1,'p_typre','yacc.py',40),
  ('typre -> INT','typre',1,'p_typre','yacc.py',41),
  ('typre -> TRUE','typre',1,'p_typre','yacc.py',42),
  ('typre -> FALSE','typre',1,'p_typre','yacc.py',43),
  ('typre -> FLOAT','typre',1,'p_typre','yacc.py',44),
  ('typre -> IDENT','typre',1,'p_typre','yacc.py',45),
  ('idmap -> tymap IDENT EQ_V dictionary','idmap',4,'p_idmap','yacc.py',49),
  ('tymap -> MAP','tymap',1,'p_tymap','yacc.py',52),
  ('tymap -> MAP LT tykey COMMA tyvalue GT','tymap',6,'p_tymap','yacc.py',53),
  ('tykey -> STRING_TYPE','tykey',1,'p_tykey','yacc.py',56),
  ('tykey -> DOUBLE_TYPE','tykey',1,'p_tykey','yacc.py',57),
  ('tykey -> INT_TYPE','tykey',1,'p_tykey','yacc.py',58),
  ('tyvalue -> STRING_TYPE','tyvalue',1,'p_tyvalue','yacc.py',61),
  ('tyvalue -> DOUBLE_TYPE','tyvalue',1,'p_tyvalue','yacc.py',62),
  ('tyvalue -> INT_TYPE','tyvalue',1,'p_tyvalue','yacc.py',63),
  ('tyvalue -> BOOLEAN','tyvalue',1,'p_tyvalue','yacc.py',64),
  ('tyvalue -> IDENT','tyvalue',1,'p_tyvalue','yacc.py',65),
  ('tyvalue -> iterable','tyvalue',1,'p_tyvalue','yacc.py',66),
  ('tyvalue -> tymap','tyvalue',1,'p_tyvalue','yacc.py',67),
  ('iterable -> LIST','iterable',1,'p_iterable','yacc.py',70),
  ('iterable -> SET','iterable',1,'p_iterable','yacc.py',71),
  ('dictionary -> LBRACE item RBRACE','dictionary',3,'p_dictionary','yacc.py',74),
  ('item -> key DDOTS value','item',3,'p_item','yacc.py',77),
  ('item -> key DDOTS value COMMA item','item',5,'p_item','yacc.py',78),
  ('key -> STRING','key',1,'p_key','yacc.py',81),
  ('key -> INT','key',1,'p_key','yacc.py',82),
  ('key -> FLOAT','key',1,'p_key','yacc.py',83),
  ('value -> STRING','value',1,'p_value','yacc.py',86),
  ('value -> FLOAT','value',1,'p_value','yacc.py',87),
  ('value -> INT','value',1,'p_value','yacc.py',88),
  ('value -> FALSE','value',1,'p_value','yacc.py',89),
  ('value -> TRUE','value',1,'p_value','yacc.py',90),
  ('value -> IDENT','value',1,'p_value','yacc.py',91),
  ('value -> iterable','value',1,'p_value','yacc.py',92),
  ('value -> tymap','value',1,'p_value','yacc.py',93),
  ('varfunc -> IDENT DOT function','varfunc',3,'p_varfunc','yacc.py',96),
  ('function -> CLEAR_FUNC LPAREN RPAREN','function',3,'p_function_clear','yacc.py',99),
  ('function -> REMOVE_FUNC LPAREN STRING RPAREN','function',4,'p_function_remove','yacc.py',102),
  ('function -> TOSTRING_FUNC LPAREN RPAREN','function',3,'p_function_tostring','yacc.py',105),
]
