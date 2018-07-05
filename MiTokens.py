import ply.lex as lex

tokens = ['NUMERO','STRING',
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
x= "B = lambda X,Y=\"5aas\": (X * 5)"
x2= "B = lambda X: X*2"
x3= "B = lambda X,Y,Z=1: X + X"
x4 = "B = map(lambda X : X + 3, [0,1,4,6]"
x5 = 'B = map(lambda X: int if X > 4 else "menor",[0,1,4,6])'
x6=  'B = map(lambda Z: str if Z == "verde" else "falso",["verde", "rojo"])'
x7 = 'B = filter(lambda X: X - 2 >= 5, [0,10,14,6])'
x8 = 'reduce(lambda X, Y: X + Y, Nums)'
x9 = 'B = filter(lambda X: X  >= 8, [0,10,14,6])'
x10 = 'B = map(lambda Y: Y *6, Items) '
lex.input(x)
lex.input(x2)
lex.input(x3)
lex.input(x4)
lex.input(x5)
lex.input(x6)
lex.input(x7)
lex.input(x8)
lex.input(x9)
lex.input(x10)

while True:
    tok = lex.token()
    if not tok:
        break
    else:
        print(tok.type + ': ', tok.value)
