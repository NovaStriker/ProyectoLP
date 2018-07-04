import ply.yacc as yacc
import MiTokens
tokens = MiTokens.tokens

def p_assignVariable(p):
    '''assignVariable : VARIABLE IGUAL expr
                    | VARIABLE IGUAL COMILLAS STRING COMILLAS
                    | VARIABLE IGUAL lambda'''

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

def p_lambda(p):
    '''lambda : LAMBDA parametros DOSPUNTOS expr'''


yacc.yacc()

