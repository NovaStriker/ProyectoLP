import ply.lex as lex

tokens = ['VARIABLE','NUMERO','STRING',
          'MAS','MENOS','POR','DIVIDIR','IGUAL',
          'ABRIRPARENTESIS','CERRARPARENTESIS','ABRIRLLAVES','CERRARLLAVES','COMILLAS',
          'MAYORQUE','MENORQUE','EXCLAMACION','OPERADORLOGICO','BOOLEANO',
          'PUNTOYCOMA','COMA','DOSPUNTOS',
          'LAMBDA']

t_ignore = ' \t'

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t
t_STRING = r'".+"'
t_VARIABLE = r'[a-zA-Z][a-zA-Z0-9_]*'

t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIVIDIR = r'/'
t_IGUAL = r'='

t_ABRIRPARENTESIS = r'\('
t_CERRARPARENTESIS = r'\)'
t_ABRIRLLAVES = r'\{'
t_CERRARLLAVES = r'\}'
t_COMILLAS = r'"'

t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_EXCLAMACION = r'!'
t_OPERADORLOGICO = r'AND | OR'
t_BOOLEANO = r'True | False'


t_PUNTOYCOMA = r';'
t_COMA = r','
t_DOSPUNTOS = r':'

t_LAMBDA = r'lambda'

def t_error(token):
    print("Token desconocido: \n")
    message = "\ntype:" + token.type
    message += "\nvalue:" + str(token.value)
    message += "\nline:" + str(token.lineno)
    message += "\nposition:" + str(token.lexpos)
    print(message)

lex.lex()
x= "b = lambda x,y=\"5aas\": (x * 5)"
lex.input(x)
while True:
    tok = lex.token()
    if not tok:
        break
    else:
        print(tok.type + ': ', tok.value)
