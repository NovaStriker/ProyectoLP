import ply.lex as lex

tokens = ['NUMERO','STRING','FLOAT',
          'LAMBDA','FILTER','REDUCE', 'MAPA',
          'MAS','MENOS','POR','DIVIDIR','IGUAL',
          'ABRIRPARENTESIS','CERRARPARENTESIS','ABRIRLLAVES','CERRARLLAVES','ABRIRCORCHETE','CERRARCORCHETE',
          'MAYORQUE','MENORQUE','EXCLAMACION','OPERADORLOGICO','BOOLEANO',
          'PUNTOYCOMA','COMA','DOSPUNTOS',
          'IF','ELSE',
          'VARIABLE','INT', 'STR']

t_ignore = ' \t'

t_INT = r'int'
t_STR = r'str'

t_IF = r'if'
t_ELSE = r'else'

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t


t_STRING = r'"[a-zA-Z0-9_]+"'


t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIVIDIR = r'/'
t_IGUAL = r'='

t_ABRIRPARENTESIS = r'\('
t_CERRARPARENTESIS = r'\)'
t_ABRIRLLAVES = r'\{'
t_CERRARLLAVES = r'\}'
t_ABRIRCORCHETE = r'\['
t_CERRARCORCHETE = r'\]'


t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_EXCLAMACION = r'!'
t_OPERADORLOGICO = r'AND | OR'
t_BOOLEANO = r'True | False'


t_PUNTOYCOMA = r';'
t_COMA = r','
t_DOSPUNTOS = r':'

t_LAMBDA = r'lambda'
t_FILTER = r'filter'
t_REDUCE = r'reduce'
t_MAPA = r'map'

t_VARIABLE = r'[A-Z][\w]*'

def t_error(token):
    print("Token desconocido: \n")
    message = "\ntype:" + token.type
    message += "\nvalue:" + str(token.value)
    message += "\nline:" + str(token.lineno)
    message += "\nposition:" + str(token.lexpos)
    print(message)

lex.lex()
