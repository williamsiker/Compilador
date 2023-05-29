
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightIDrightASIGNARleftLPARENTRPARENTASIGNAR COMA CREARBOTON CREARETIQUETA CREARFRAME CREARVENTANA DOT FINL ID INICIAR LPARENT NUMBER RPARENT TEXTblock : statement_liststatement_list : statement statement_liststatement_list : statementstatement : crearventana FINL\n    \t\t\t | crearframe FINL\n                 | crearboton FINL\n                 | crearetiqueta FINL\n                 | iniciar FINLcrearventana : ID ASIGNAR CREARVENTANA LPARENT RPARENTcrearframe : ID ASIGNAR CREARFRAME LPARENT argument_list RPARENTcrearboton : ID ASIGNAR CREARBOTON LPARENT argument_list RPARENTcrearetiqueta : ID ASIGNAR CREARETIQUETA LPARENT argument_list RPARENTiniciar : ID DOT INICIAR LPARENT RPARENTargument_list : argumentargument_list : argument COMA argument_listargument : IDargument : TEXT'
    
_lr_action_items = {'ID':([0,3,11,12,13,14,15,24,25,26,37,],[9,9,-4,-5,-6,-7,-8,29,29,29,29,]),'$end':([1,2,3,10,11,12,13,14,15,],[0,-1,-3,-2,-4,-5,-6,-7,-8,]),'FINL':([4,5,6,7,8,28,35,36,38,39,],[11,12,13,14,15,-9,-13,-10,-11,-12,]),'ASIGNAR':([9,],[16,]),'DOT':([9,],[17,]),'CREARVENTANA':([16,],[18,]),'CREARFRAME':([16,],[19,]),'CREARBOTON':([16,],[20,]),'CREARETIQUETA':([16,],[21,]),'INICIAR':([17,],[22,]),'LPARENT':([18,19,20,21,22,],[23,24,25,26,27,]),'RPARENT':([23,27,29,30,31,32,33,34,40,],[28,35,-16,36,-14,-17,38,39,-15,]),'TEXT':([24,25,26,37,],[32,32,32,32,]),'COMA':([29,31,32,],[-16,37,-17,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'block':([0,],[1,]),'statement_list':([0,3,],[2,10,]),'statement':([0,3,],[3,3,]),'crearventana':([0,3,],[4,4,]),'crearframe':([0,3,],[5,5,]),'crearboton':([0,3,],[6,6,]),'crearetiqueta':([0,3,],[7,7,]),'iniciar':([0,3,],[8,8,]),'argument_list':([24,25,26,37,],[30,33,34,40,]),'argument':([24,25,26,37,],[31,31,31,31,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> block","S'",1,None,None,None),
  ('block -> statement_list','block',1,'p_block','a.py',17),
  ('statement_list -> statement statement_list','statement_list',2,'p_statement_list1','a.py',23),
  ('statement_list -> statement','statement_list',1,'p_statement_list2','a.py',28),
  ('statement -> crearventana FINL','statement',2,'p_statement','a.py',33),
  ('statement -> crearframe FINL','statement',2,'p_statement','a.py',34),
  ('statement -> crearboton FINL','statement',2,'p_statement','a.py',35),
  ('statement -> crearetiqueta FINL','statement',2,'p_statement','a.py',36),
  ('statement -> iniciar FINL','statement',2,'p_statement','a.py',37),
  ('crearventana -> ID ASIGNAR CREARVENTANA LPARENT RPARENT','crearventana',5,'p_crearventana','a.py',44),
  ('crearframe -> ID ASIGNAR CREARFRAME LPARENT argument_list RPARENT','crearframe',6,'p_crearframe','a.py',50),
  ('crearboton -> ID ASIGNAR CREARBOTON LPARENT argument_list RPARENT','crearboton',6,'p_crearboton','a.py',56),
  ('crearetiqueta -> ID ASIGNAR CREARETIQUETA LPARENT argument_list RPARENT','crearetiqueta',6,'p_crearetiqueta','a.py',62),
  ('iniciar -> ID DOT INICIAR LPARENT RPARENT','iniciar',5,'p_iniciar','a.py',68),
  ('argument_list -> argument','argument_list',1,'p_argument_list1','a.py',74),
  ('argument_list -> argument COMA argument_list','argument_list',3,'p_argument_list2','a.py',79),
  ('argument -> ID','argument',1,'p_argument1','a.py',85),
  ('argument -> TEXT','argument',1,'p_argument2','a.py',90),
]