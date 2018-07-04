
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABRIRCORCHETE ABRIRLLAVES ABRIRPARENTESIS BOOLEANO CERRARCORCHETE CERRARLLAVES CERRARPARENTESIS COMA COMILLAS DIVIDIR DOSPUNTOS EXCLAMACION FILTER IGUAL LAMBDA MAS MAYORQUE MENORQUE MENOS NUMERO OPERADORLOGICO POR PUNTOYCOMA STRING VARIABLEassignVariable : VARIABLE IGUAL expr\n                    | VARIABLE IGUAL STRING\n                    | VARIABLE IGUAL lambda\n                    | VARIABLE IGUAL filter\n                    | VARIABLE IGUAL listalista : ABRIRCORCHETE lisString CERRARCORCHETE\n            | ABRIRCORCHETE lisInt CERRARCORCHETElisString : lisString COMA STRING\n                | STRINGlisInt : lisInt COMA NUMERO\n                | NUMEROcondicion : IGUAL IGUAL\n                | EXCLAMACION IGUAL\n                | MAYORQUE IGUAL\n                | MENORQUE IGUAL\n                | MAYORQUE\n                | MENORQUEevaluarCondicion : expr condicion expr\n                        | BOOLEANO\n                        | evaluarCondicion OPERADORLOGICO evaluarCondicionexpr : expr MAS term\n            | ABRIRPARENTESIS expr MAS term CERRARPARENTESIS\n            | expr MENOS term\n            | ABRIRPARENTESIS expr MENOS term CERRARPARENTESIS\n            | termterm : term POR term\n            | term DIVIDIR term\n            | ABRIRPARENTESIS term POR NUMERO CERRARPARENTESIS\n            | ABRIRPARENTESIS term DIVIDIR NUMERO CERRARPARENTESIS\n            | NUMERO\n            | VARIABLE\n            | ABRIRPARENTESIS term POR term CERRARPARENTESIS\n            | ABRIRPARENTESIS term DIVIDIR term CERRARPARENTESISparametros : parametros COMA VARIABLE\n                | VARIABLE\n                | parametros COMA assignVariable\n                | assignVariable\n                | lambda : LAMBDA parametros DOSPUNTOS exprfilter : FILTER ABRIRPARENTESIS lambda COMA VARIABLE CERRARPARENTESIS\n            | FILTER ABRIRPARENTESIS lambda COMA lista CERRARPARENTESIS'
    
_lr_action_items = {'VARIABLE':([0,3,11,12,16,17,18,19,31,35,36,37,38,39,40,56,],[2,4,4,23,4,4,4,4,4,4,4,4,4,4,54,65,]),'$end':([1,4,5,6,7,8,9,10,15,30,32,33,34,42,44,53,59,60,61,62,63,64,67,68,],[0,-31,-1,-2,-3,-4,-5,-25,-30,-21,-23,-26,-27,-6,-7,-39,-22,-24,-32,-28,-33,-29,-40,-41,]),'IGUAL':([2,23,54,],[3,3,3,]),'STRING':([3,14,43,],[6,28,57,]),'ABRIRPARENTESIS':([3,11,13,16,17,18,19,31,35,36,37,38,39,],[11,11,25,31,31,31,31,31,31,31,31,31,11,]),'LAMBDA':([3,25,],[12,12,]),'FILTER':([3,],[13,]),'ABRIRCORCHETE':([3,56,],[14,14,]),'NUMERO':([3,11,14,16,17,18,19,31,35,36,37,38,39,45,],[15,15,29,15,15,15,15,15,15,15,50,52,15,58,]),'POR':([4,10,15,21,30,32,33,34,46,47,48,49,50,51,52,61,62,63,64,],[-31,18,-30,37,18,18,18,18,37,18,18,18,-30,18,-30,-32,-28,-33,-29,]),'DIVIDIR':([4,10,15,21,30,32,33,34,46,47,48,49,50,51,52,61,62,63,64,],[-31,19,-30,38,19,19,19,19,38,19,19,19,-30,19,-30,-32,-28,-33,-29,]),'MAS':([4,5,10,15,20,21,30,32,33,34,47,48,49,50,51,52,53,59,60,61,62,63,64,],[-31,16,-25,-30,35,-25,-21,-23,-26,-27,-21,-23,-26,-30,-27,-30,16,-22,-24,-32,-28,-33,-29,]),'MENOS':([4,5,10,15,20,21,30,32,33,34,47,48,49,50,51,52,53,59,60,61,62,63,64,],[-31,17,-25,-30,36,-25,-21,-23,-26,-27,-21,-23,-26,-30,-27,-30,17,-22,-24,-32,-28,-33,-29,]),'DOSPUNTOS':([4,5,6,7,8,9,10,12,15,22,23,24,30,32,33,34,42,44,53,54,55,59,60,61,62,63,64,67,68,],[-31,-1,-2,-3,-4,-5,-25,-38,-30,39,-35,-37,-21,-23,-26,-27,-6,-7,-39,-34,-36,-22,-24,-32,-28,-33,-29,-40,-41,]),'COMA':([4,5,6,7,8,9,10,12,15,22,23,24,26,27,28,29,30,32,33,34,41,42,44,53,54,55,57,58,59,60,61,62,63,64,67,68,],[-31,-1,-2,-3,-4,-5,-25,-38,-30,40,-35,-37,43,45,-9,-11,-21,-23,-26,-27,56,-6,-7,-39,-34,-36,-8,-10,-22,-24,-32,-28,-33,-29,-40,-41,]),'CERRARPARENTESIS':([4,15,33,34,42,44,47,48,49,50,51,52,61,62,63,64,65,66,],[-31,-30,-26,-27,-6,-7,59,60,61,62,63,64,-32,-28,-33,-29,67,68,]),'CERRARCORCHETE':([26,27,28,29,57,58,],[42,44,-9,-11,-8,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'assignVariable':([0,12,40,],[1,24,55,]),'expr':([3,11,39,],[5,20,53,]),'lambda':([3,25,],[7,41,]),'filter':([3,],[8,]),'lista':([3,56,],[9,66,]),'term':([3,11,16,17,18,19,31,35,36,37,38,39,],[10,21,30,32,33,34,46,47,48,49,51,10,]),'parametros':([12,],[22,]),'lisString':([14,],[26,]),'lisInt':([14,],[27,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> assignVariable","S'",1,None,None,None),
  ('assignVariable -> VARIABLE IGUAL expr','assignVariable',3,'p_assignVariable','Parser.py',6),
  ('assignVariable -> VARIABLE IGUAL STRING','assignVariable',3,'p_assignVariable','Parser.py',7),
  ('assignVariable -> VARIABLE IGUAL lambda','assignVariable',3,'p_assignVariable','Parser.py',8),
  ('assignVariable -> VARIABLE IGUAL filter','assignVariable',3,'p_assignVariable','Parser.py',9),
  ('assignVariable -> VARIABLE IGUAL lista','assignVariable',3,'p_assignVariable','Parser.py',10),
  ('lista -> ABRIRCORCHETE lisString CERRARCORCHETE','lista',3,'p_lista','Parser.py',12),
  ('lista -> ABRIRCORCHETE lisInt CERRARCORCHETE','lista',3,'p_lista','Parser.py',13),
  ('lisString -> lisString COMA STRING','lisString',3,'p_lisString','Parser.py',16),
  ('lisString -> STRING','lisString',1,'p_lisString','Parser.py',17),
  ('lisInt -> lisInt COMA NUMERO','lisInt',3,'p_lisInt','Parser.py',20),
  ('lisInt -> NUMERO','lisInt',1,'p_lisInt','Parser.py',21),
  ('condicion -> IGUAL IGUAL','condicion',2,'p_condicion','Parser.py',27),
  ('condicion -> EXCLAMACION IGUAL','condicion',2,'p_condicion','Parser.py',28),
  ('condicion -> MAYORQUE IGUAL','condicion',2,'p_condicion','Parser.py',29),
  ('condicion -> MENORQUE IGUAL','condicion',2,'p_condicion','Parser.py',30),
  ('condicion -> MAYORQUE','condicion',1,'p_condicion','Parser.py',31),
  ('condicion -> MENORQUE','condicion',1,'p_condicion','Parser.py',32),
  ('evaluarCondicion -> expr condicion expr','evaluarCondicion',3,'p_evaluarCondicion','Parser.py',35),
  ('evaluarCondicion -> BOOLEANO','evaluarCondicion',1,'p_evaluarCondicion','Parser.py',36),
  ('evaluarCondicion -> evaluarCondicion OPERADORLOGICO evaluarCondicion','evaluarCondicion',3,'p_evaluarCondicion','Parser.py',37),
  ('expr -> expr MAS term','expr',3,'p_expr','Parser.py',40),
  ('expr -> ABRIRPARENTESIS expr MAS term CERRARPARENTESIS','expr',5,'p_expr','Parser.py',41),
  ('expr -> expr MENOS term','expr',3,'p_expr','Parser.py',42),
  ('expr -> ABRIRPARENTESIS expr MENOS term CERRARPARENTESIS','expr',5,'p_expr','Parser.py',43),
  ('expr -> term','expr',1,'p_expr','Parser.py',44),
  ('term -> term POR term','term',3,'p_term','Parser.py',47),
  ('term -> term DIVIDIR term','term',3,'p_term','Parser.py',48),
  ('term -> ABRIRPARENTESIS term POR NUMERO CERRARPARENTESIS','term',5,'p_term','Parser.py',49),
  ('term -> ABRIRPARENTESIS term DIVIDIR NUMERO CERRARPARENTESIS','term',5,'p_term','Parser.py',50),
  ('term -> NUMERO','term',1,'p_term','Parser.py',51),
  ('term -> VARIABLE','term',1,'p_term','Parser.py',52),
  ('term -> ABRIRPARENTESIS term POR term CERRARPARENTESIS','term',5,'p_term','Parser.py',53),
  ('term -> ABRIRPARENTESIS term DIVIDIR term CERRARPARENTESIS','term',5,'p_term','Parser.py',54),
  ('parametros -> parametros COMA VARIABLE','parametros',3,'p_parametros','Parser.py',57),
  ('parametros -> VARIABLE','parametros',1,'p_parametros','Parser.py',58),
  ('parametros -> parametros COMA assignVariable','parametros',3,'p_parametros','Parser.py',59),
  ('parametros -> assignVariable','parametros',1,'p_parametros','Parser.py',60),
  ('parametros -> <empty>','parametros',0,'p_parametros','Parser.py',61),
  ('lambda -> LAMBDA parametros DOSPUNTOS expr','lambda',4,'p_lambda','Parser.py',64),
  ('filter -> FILTER ABRIRPARENTESIS lambda COMA VARIABLE CERRARPARENTESIS','filter',6,'p_filter','Parser.py',67),
  ('filter -> FILTER ABRIRPARENTESIS lambda COMA lista CERRARPARENTESIS','filter',6,'p_filter','Parser.py',68),
]
