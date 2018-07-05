import ply.yacc as yacc
import MiTokens
tokens = MiTokens.tokens

def p_assignVariable(p):
    '''assignVariable : VARIABLE IGUAL expr
                    | VARIABLE IGUAL STRING
                    | VARIABLE IGUAL lambda
                    | VARIABLE IGUAL filter
                    | VARIABLE IGUAL lista'''
def p_lista(p):
    '''lista : ABRIRCORCHETE lisString CERRARCORCHETE
            | ABRIRCORCHETE lisInt CERRARCORCHETE'''

def p_lisString(p):
    '''lisString : lisString COMA STRING
                | STRING'''

def p_lisInt(p):
    '''lisInt : lisInt COMA NUMERO
                | NUMERO'''

def p_error(subexpr):
    raise Exception("Syntax error.")

def p_condicion(p):
    '''condicion : IGUAL IGUAL
                | EXCLAMACION IGUAL
                | MAYORQUE IGUAL
                | MENORQUE IGUAL
                | MAYORQUE
                | MENORQUE'''

def p_evaluarCondicion(p):
    '''evaluarCondicion : expr condicion expr
                        | BOOLEANO
                        | expr IGUAL IGUAL BOOLEANO
                        | expr EXCLAMACION IGUAL BOOLEANO
                        | evaluarCondicion OPERADORLOGICO evaluarCondicion'''

def p_expr(p):
    '''expr : expr MAS term
            | ABRIRPARENTESIS expr MAS term CERRARPARENTESIS
            | expr MENOS term
            | ABRIRPARENTESIS expr MENOS term CERRARPARENTESIS
            | term'''

def p_term(p):
    '''term : term POR term
            | term DIVIDIR term
            | ABRIRPARENTESIS term POR NUMERO CERRARPARENTESIS
            | ABRIRPARENTESIS term DIVIDIR NUMERO CERRARPARENTESIS
            | NUMERO
            | VARIABLE
            | ABRIRPARENTESIS term POR term CERRARPARENTESIS
            | ABRIRPARENTESIS term DIVIDIR term CERRARPARENTESIS'''

def p_parametros(p):
    '''parametros : parametros COMA VARIABLE
                | VARIABLE
                | parametros COMA assignVariable
                | assignVariable
                | '''
def p_cualquierCosa(p):
    '''cualquierCosa : STRING
                    | NUMERO
                    | VARIABLE'''

def p_lambda(p):
    '''lambda : LAMBDA parametros DOSPUNTOS expr
            | LAMBDA parametros DOSPUNTOS evaluarCondicion
            | LAMBDA parametros DOSPUNTOS INT IF evaluarCondicion ELSE cualquierCosa'''

def p_filter(p):
    '''filter : FILTER ABRIRPARENTESIS lambda COMA VARIABLE CERRARPARENTESIS
            | FILTER ABRIRPARENTESIS lambda COMA lista CERRARPARENTESIS'''

def p_reduce(p):
    '''reduce : REDUCE ABRIRPARENTESIS lambda COMA VARIABLE CERRARPARENTESIS
            | REDUCE ABRIRPARENTESIS lambda COMA lista CERRARPARENTESIS'''

def p_mapa(p):
    '''mapa : MAPA ABRIRPARENTESIS lambda COMA VARIABLE CERRARPARENTESIS
            | MAPA ABRIRPARENTESIS lambda COMA lista CERRARPARENTESIS'''

yacc.yacc()

