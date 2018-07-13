import MiTokens
import Parser

from ply.lex import lex
from ply.yacc import yacc


lexer = lex(module=MiTokens)
parser = yacc(module=Parser)

x1= "B = lambda X,Y=\"5aas\": (X * 5)"
x2= "Bjhghjg = lambda X: X*2"
x3= "B1 = lambda X: X + 3"
x4 = "B = map(lambda X: X + 3.00009 , [0,1,4,6])"
x5 = 'B = map(lambda X: int if X > 4 else "menor",[0,1,4,6])'
x6=  'B = filter(lambda Z: str if Z == "verde0" else 0.7 ,["verde", "rojo"])'
x7 = 'B = filter(lambda X: X - 2 >= 5, [0,10,14,6])'
x8 = 'B = reduce(lambda X, Y: X + Y, Nums)'
x9 = 'B = filter(lambda X: X  >< 8, [0,10,14,6])'
x10 = 'B = map(lambda Y: Y +6, A + B) '

ast = parser.parse(x9, lexer)
#MiTokens.lex.input(x)
#MiTokens.lex.input(x2)
#MiTokens.lex.input(x3)
#MiTokens.lex.input(x4)
#MiTokens.lex.input(x5)
MiTokens.lex.input(x9)
#MiTokens.lex.input(x7)
#MiTokens.lex.input(x8)
#MiTokens.lex.input(x9)
#MiTokens.lex.input(x10)

while True:
    tok = MiTokens.lex.token()
    if not tok:
        break
    else:
        print(tok.type + ': ', tok.value)


print(ast)